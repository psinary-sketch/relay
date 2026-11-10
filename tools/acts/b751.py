# -*- coding: utf-8 -*-
# b751 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R361)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R361)(2) repair it carries. Edited by the Edit tool. Carried at b751 by tools/b751_fold.py (`carry`) from tools/acts/b750.py,
# b750`s names substituted; the citation`s sections adopted from tools/b751_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b750`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b750`s carried till
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
# ### b751, Component 1: THE c1 ROUTE FOR b750'S WEIGHT LINE AND ITS CORRIGENDUM, (R361)(1) and (3). Rewritten at b751 against
# ### b750's own banks (scratch c1sec749.txt, spliced): the closing's lines by needle, the events (5), the defects (18, (i) the navigator's),
# ### the refusals (13 lines at 71bc497a), the v1.29.0 controls and the rules this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '467a1968'          # ### b750's closing push tip, the public relay's main at step zero ((R361)(1))
C1_CLOSING_COMMIT = 'ca4fa5a4'      # ### b750's closing commit (its closing row, data/b750_steps.json)
C1_REFUSAL_AT = '467a1968'          # ### its refusal bank read at its closing push tip (19 lines)
C1_NOTED = '2026-11-10'
C1_CORRIGENDA_LAST = 70
C1_V170 = 'b751_standing_v1310.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.31.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-10 by b751 to b750’s entry (:%d), under `(R361)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The synthesis sitting: 10 of 11 items passed'
C1_TRAIL_NEEDLE = '### b750 — lane two, act one hundred and seventy-seven'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")
# ### b751 step zero: this route written against b750's banks over the carried route (b749's figures under b750's names), which `carry.py ruled`
# ### refused by R5 before the citation check (data/b751_stepzero.txt); nothing composed by the carried route.


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
    for l in _c1_rd('b750_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b750_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b750_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b750_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b750_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b750_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b750_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    sc = json.load(open(os.path.join(D, 'b750_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8 or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b750_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the closing`s scores')
    sdry = _c1_rd('b750_scores_dry.txt')
    if "b746's entry," not in sdry:
        sys.exit('### data/b750_scores_dry.txt: N3`s pre-root clause not read -- NOTHING COMPOSED')
    ar = json.load(open(os.path.join(D, 'b750_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b750_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (ci_, ce_, cf_, cc_, cl_, cr_), l_co = _c1_fl(c, r'^    the generated entry for b749`s events and defects.*: ITEMS (\d+): EVENTS (\d+), DEFECTS (\d+) ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ; ', 'b749`s corrigendum')
    (va, vb), l_v = _c1_fl(c, r'^    tools/standing/ at v1\.30\.0: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.30.0 foot')
    (s1, s2, s3, s4, s5), l_st = _c1_fl(c, r'^    the record of the sitting: .*THE SITTING: DECIDED (\d+) ; PASSED (\d+) ; KEPT (\d+) ; STRUCK (\d+) ; GIT WRITES (\d+) AND THE AGENDA', 'the sitting')
    (q1, q2, q3, q4, q5), l_cq = _c1_fl(c, r'^    \[E\]: .*NEGATIVE (\d+) ; THE SMALLEST NEGATIVE n = (\d+), cQ = (-[0-9.]+) ; WITHIN 1e-40 OF ZERO \d+ \(EXACTLY ZERO (\d+)\), COUNTED NEITHER WAY ; NONNEGATIVE (\d+) ;', 'cQ')
    (_ln, kst, stg), l_ln = _c1_fl(c, r'^    the INTEGRATION line .*: THE LINE: (COMPOSED) ; .*KEYSTONE (\S+) ; STAGE (\S+) ;', 'the line')
    (rr, rp_, rd_, rn_), l_rp = _c1_fl(c, r'^    tools/research/reproduce\.py.*: ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ;', 'the instruments')
    sca, l_sc = _c1_fl(c, r'^    the scan over every commit and bank of the act.*: PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', 'the scan')
    (_tg,), l_tg = _c1_fl(c, r'^### THE KERNELS: .*(no tag beyond v0\.38)', 'the tag')
    _mv, l_mv = _c1_fl('b750_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz, msha, mmd5), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-09-b750)\.zip ; \d+ bytes ; sha256 ([0-9a-f]{8})[0-9a-f]* ; MANIFEST md5 ([0-9a-f]{8})', 'the mirror`s archive')
    _aw1, l_aw1 = _c1_fl('b750_author_words.txt', r'^(Confirmed: §5 next; .* the class-group signature of the negative n\.)$', 'the author`s word at the root')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R360\)\(4\) AND \(8\)\*\*: (section 5 of the paper, .*)$', 'the carried item (a)')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 8)) or len(dr) != 25 or (int(sd), int(se)) != (25, 7):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b750 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b750_closing.txt):* “%s” (data/b750_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b750_steps.json, the record and closing rows). As its rows read: b749’s corrigendum, items %s (events %s, defects %s), CLAIM %s, CLOSE %s, '
            'REPEAT %s (:%d); standing tools v1.30.0, %s of %s (:%d); the sitting: decided %s, passed %s, kept %s, struck %s, git writes %s and the agenda, the author’s words verbatim (:%d; relay data/b750_sitting.txt); '
            '[E] the sign of cQ(n) over n ≤ 3000 from the recursion at v0.38: negative %s, the smallest negative n = %s with cQ = %s, exactly zero %s, nonnegative %s (:%d; relay data/b750_cq_sign.txt, INSTRUMENTS I-109); '
            'the INTEGRATION line %s, keystone %s, stage %s (:%d; relay data/b750_line.txt); '
            'the instruments %s rows, %s reproduce, %s differ, %s not run (:%d); the address scan %s ; %s ; %s ; %s (:%d); %s (:%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push '
            'and %s of %s post-push (:%d, :%d), the failing the three declared on the face; the parts of the prev runs sent out of their order and G-PP-SCOPE’s positive control proving nothing at this act, '
            'the live reading holding (data/b750_events.txt (3), (7), REPEAT b717 (3)). At the scores’ close SCORES %d OF 8 HELD (data/b750_scores_close.json; the closing’s line :%d); N3 read REFUTED before the root '
            'on the sitting prompt’s phrase “b746’s entry,” and HELD once the root prompt was banked, the one reader reading once (relay data/b750_scores_dry.txt). The root %s over %s banks, '
            'chained from %s (data/b750_act_root.json; :%d); the mirror %s at %s, sha256 %s, MANIFEST md5 %s (data/b750_mirror_verify.txt :%d; :%d); '
            'the author’s word at the root “%s” (data/b750_author_words.txt :%d); the closing’s carried item (a): %s (:%d), this act under `(R361)`(2). %d events in data/b750_events.txt, rows (1)-(%d), '
            'entered after the lock; %d defects, (a)–(y), the navigator’s (f) among them (data/b750_defects.txt). '
            'The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. Nothing deposited, no merge, '
            'no new Zenodo version, the draft held at v5; the corrigendum for these rows follows, under `(R361)`(3).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, ci_, ce_, cf_, cc_, cl_, cr_, l_co, vb, va, l_v, s1, s2, s3, s4, s5, l_st,
                q1, q2, q3, q4, q5, l_cq, _ln, kst, stg, l_ln, rr, rp_, rd_, rn_, l_rp, sca[0], sca[1], sca[2], sca[3], l_sc,
                _tg, l_tg, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, len(held), l_sl,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, msha, mmd5, l_mv, l_mz, _aw1[0], l_aw1, ca, l_ca, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b750's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '23:02:12Z', 'defect (a)'), (2, 'REDIR', '23:07:42Z', 'defect (a)'), (3, 'ENV', '23:11:28Z', 'defect (a)'), (4, 'PIPE', '23:18:47Z', 'defect (g)'),
               (5, 'SED', '23:21:41Z', 'defect (g)'), (6, 'REDIR', '23:28:44Z', 'defect (g)'), (7, 'READ', '23:33:36Z', 'defect (g)'), (8, 'READ', '23:37:13Z', 'defect (g)'),
               (9, 'PIPE', '23:56:58Z', 'defect (n)'), (10, 'PIPE', '01:30:01Z', 'defect (q)'), (11, 'READ', '01:52:48Z', 'defect (r)'), (12, 'READ', '02:07:32Z', 'defect (r)'),
               (13, 'READ', '02:07:33Z', 'defect (r)'), (14, 'PIPE', '03:31:16Z', 'defect (v)'), (15, 'REDIR', '04:32:16Z', 'defect (w)'), (16, 'LOCKED', '04:36:58Z', 'event (2)'),
               (17, 'REDIR', '06:32:58Z', 'event (4)'), (18, 'READ', '08:35:19Z', 'event (5)'), (19, 'READ', '08:35:19Z', 'event (5)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing refusal of b750's: b751's hook bank opens at its own step zero, every line b751's own
C1_FLIP = {}      # ### (R361)(3) flips no tag: each item read as its bank tags it
C1_CARRIED = []   # ### (R361)(3): the navigator's one, (f), is lettered in b750's defects bank as the navigator's; none entered by this corrigendum
C1_CORR_TITLE = ('## Corrigendum to b750’s record (relay data/b750_events.txt rows (1)-(7) and data/b750_defects.txt (a)-(y)): seven events and twenty-five defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT, the navigator’s (f) among them; the part-order guard, the (W) refusal in the hook, the composer on every prompt, the line reader’s match, the scan at the gate, '
                 'the rendered modules compiled by the dry, the carry printing every row, the tool’s words and phases, the host’s limit, the refusals printed, at tools/standing/ v1.31.0, '
                 'each controlled, under (R361)(3)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.31.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_rules_line(n):
    t = _c1_rd('b751_rules.txt').split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith('(%d) ' % n)]
    if len(h) != 1:
        sys.exit('### THE RULES BANK: %d LINES OPEN (%d), NOT ONE -- NOTHING COMPOSED' % (len(h), n))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b750_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)   # ### 19 lines at 467a1968
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
    (cc, cd), _l = _c1_fl('b750_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.31.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(7)', sorted(ev) == list(range(1, 8))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 25', len(dr) == 25), ('the refusals 19, each answered as listed', len(rl) == 19 and not bad_ref),
                              ('the navigator`s row in b750`s defects bank (f) alone', [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"] == ['f']),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.31.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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
    """the counter as this corrigendum reads the items: the closing's 32, none entered beside them, no tag flipped."""
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


# ### the repairs each item is met by at v1.31.0 (the controls bank data/b751_standing_v1310.txt, the rules data/b751_rules.txt)
C1_EV_EXTRA = {1: '; no item of `(R361)`(3) names it; the tool’s own refusal, nothing written',
               2: '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed (data/b750_hook_refusals.txt :16)',
               3: '; repair (order), `(R361)`(3)(i): the part runner refuses a part whose predecessor has no bank for the act in the mode asked',
               4: '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed (data/b750_hook_refusals.txt :17)',
               5: '; repair (instances), `(R361)`(3)(x), REPEAT: the refusals printed (data/b750_hook_refusals.txt :18, :19)',
               6: '; repair (limit), `(R361)`(3)(ix): the push sent after the step-rows commit, the instance printed',
               7: '; repair (order), `(R361)`(3)(i), REPEAT: the positive control read with the part order kept; the plant’s own fault printed'}
C1_DF_EXTRA = {'a': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusals printed', 'b': '; repair (words), `(R361)`(3)(viii): the instance printed',
               'c': '; no item of `(R361)`(3) names it; a pushed bank restored to its blob at step zero',
               'd': '; repair (carry), `(R361)`(3)(vii), REPEAT', 'e': '; no item of `(R361)`(3) names it; the window widened before the banked run',
               'f': '; the navigator’s, lettered as the navigator’s ((R361)(3))',
               'g': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusals printed',
               'h': '; repair (wlist), `(R361)`(3)(ii): a Write or Edit of a tracked path outside the (W) list refused by the hook before it lands',
               'i': '; repair (wlist), `(R361)`(3)(ii): the same refusal, tools/act_close.py replayed',
               'j': '; repair (compile), `(R361)`(3)(vi): the standing dry compiles every rendered module and prints the earliest error',
               'k': '; repair (words), `(R361)`(3)(viii): the instance printed',
               'l': '; no item of `(R361)`(3) names it; the v1.30.0 controls’ own runs, their last write 39 of 39',
               'm': '; repair (carry), `(R361)`(3)(vii), REPEAT', 'n': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed',
               'o': '; repair (words), `(R361)`(3)(viii): the instance printed', 'p': '; no item of `(R361)`(3) names it; a reading defect, nothing written',
               'q': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed', 'r': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusals printed',
               's': '; repair (carry), `(R361)`(3)(vii), REPEAT: the ferry banked by the citation tool’s route', 't': '; repair (limit), `(R361)`(3)(ix): the run sent with the limit the tool prints',
               'u': '; repair (words), `(R361)`(3)(viii): the instance printed', 'v': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed',
               'w': '; repair (instances), `(R361)`(3)(x), REPEAT: the refusal printed', 'x': '; repair (gatescan), `(R361)`(3)(v): the gate route runs the staged-set scan',
               'y': '; repair (words), `(R361)`(3)(viii), REPEAT: the instance printed'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b751, to `(R361)`(3)(iii): before b750’s root, N3 read REFUTED on its last clause alone, the root prompt’s sentences about the entry not the composer’s: ["b746’s entry,"] '
            '(relay data/b750_scores_dry.txt); the act module read the last PROMPT row of the answers bank, then the sitting’s prompt, put without the composer; once the root prompt was banked N3 read HELD '
            '(relay data/b750_scores_close.json). The repair (composer) runs every prompt through compose_checked before it is put.',
            'Dated note, b751, to `(R361)`(3)(iv): b750’s line bank read b745-b748’s INTEGRATION lines SYNTHESISED by the cluster without matching each entry’s own finding against the note’s names, and said so '
            '(relay data/b750_line.txt :26-:31); the repair (linematch) matches each finding before it reads SYNTHESISED and reads CLUSTERED where no name matches.')
C1_CLASSES = (
    ('order', 'the suite parts run out of their order (`(R361)`(3)(i), events (3), (7), REPEAT b717 (3))', 'the part runner refuses a part whose predecessor in the standing order has no bank for the act in the mode asked, and prints the order. b750’s standing-a2 replayed before a1: run before, refused after', 1),
    ('wlist', 'the writes outside the (W) list (`(R361)`(3)(ii), defects (h), (i))', 'a Write or Edit of a tracked path not in the act’s (W) list refused by the hook before it lands, the list read from the regenerated bank. b750’s edit of tools/act_close.py replayed: let through before, refused after', 2),
    ('composer', 'every prompt through the composer (`(R361)`(3)(iii), N3 before the root)', 'every prompt the act puts, the sitting items and the halts as well as the root, runs through compose_checked before it is put. b750’s sitting prompt replayed: put before, refused on “b746’s entry,” after', 3),
    ('linematch', 'the line reader’s match (`(R361)`(3)(iv), data/b750_line.txt’s note)', 'the line reader matches each entry’s findings against the names a keystone’s note carries before it reads SYNTHESISED, and reads CLUSTERED where no name matches. b745-b748 replayed with their findings named; a planted entry with an unnamed finding read CLUSTERED', 4),
    ('gatescan', 'the scan left out of a commit (`(R361)`(3)(v), defect (x), REPEAT b749 (c))', 'the gate route runs the staged-set scan as the commit route does. cc1fc182’s sequence replayed: committed before, refused after', 5),
    ('compile', 'the rendered module’s indentation (`(R361)`(3)(vi), defect (j))', 'the standing dry compiles every rendered module and prints the earliest error with its line. v1.30.0’s opening render replayed: the error printed with its line', 6),
    ('carry', 'the carry (`(R361)`(3)(vii), defects (d), (m), (s), REPEAT)', 'the carry prints every row and figure it brings beside the ruling and refuses the ones it does not name; the ferry banked by the citation tool’s route. b750’s carried sections replayed to a refusal', 7),
    ('words', 'the tool’s words and phases (`(R361)`(3)(viii), defects (b), (k), (o), (u), (y), REPEAT)', 'the instances printed; the commit tool’s usage line printed by the carry at step zero', 8),
    ('limit', 'the host’s limit (`(R361)`(3)(ix), defect (t), events (6))', 'a run that may exceed the host’s default sent with the limit the tool prints', 9),
    ('instances', 'the hook’s refusals (`(R361)`(3)(x), defects (a), (g), (n), (q), (r), (v), (w), events (2), (4), (5), REPEAT)', 'the instances printed, b750’s nineteen refusals each by its line', 10),
    ('version', 'the version (`(R361)`(3)(xi))', 'tools/standing/VERSION v1.31.0, landed by a commit of its own (relay %s) with its controls bank and the record’s dry over it, before the gate' % (K.C1_STANDING or '')[:8], 11),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b750’s events bank (relay data/b750_events.txt) carries seven rows, entered after its lock gate and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-five lettered rows, (a)-(y), each tagged in its own bracket (%s); its refusal bank nineteen lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them. '
         'The navigator’s one, (f), is lettered in the defects bank as the navigator’s.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R361)`(3), at tools/standing/ v1.31.0, each with a control on b750’s banks or the trail as it stands, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s; the rules relay data/b751_rules.txt):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what, rule_ in C1_CLASSES:
        at_ = 'relay data/%s :%d; data/b751_rules.txt (%d), :%d' % (C1_V170, _c1_v170_line('### (%s) ' % k_), rule_, _c1_rules_line(rule_))
        L += ['**(%s) %s** -- %s (%s).' % (k_, name, what, at_), '']
    L += ['**b750’s events (1)-(7):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?(2026-11-\d\dT)?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b750_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, ''))]
    L += ['', '**b750’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b750_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b750’s refusals** (relay data/b750_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (seven events, twenty-five defects), as b750’s closing prints it (relay data/b750_closing.txt :5); '
          'no tag is read otherwise here; the CLAIM items %s.' % (nc, nl_, rep, n, n, ', '.join(claims) or 'none'), '',
          '*Filed at b751 on the author’s ruling `(R361)`(3): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b751.py) from '
          'b750’s events and defects banks read unedited, its refusal bank, the v1.31.0 controls bank and the rules; banked as relay `data/b751_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b750’s record; no sealed tool, face, trail or root-named bank of b750 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b751 -- THE CORRIGENDUM FOR b750, (R361)(3) (%s)' % utc(), '',
             '### the banks read unedited: data/b750_events.txt rows (1)-(7), data/b750_defects.txt 25 rows, data/b750_hook_refusals.txt 19 '
             'lines at %s; data/%s (the v1.31.0 controls); data/b751_rules.txt; the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 7, DEFECTS 25 ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE NAVIGATOR`S 1, LETTERED (f) ; DATED NOTES %d ; '
               'v1.31.0: THE PART-ORDER GUARD, THE (W) REFUSAL, THE COMPOSER ON EVERY PROMPT, THE LINE READER`S MATCH, THE SCAN AT THE GATE, THE COMPILED RENDER, THE CARRY, '
               'THE WORDS AND PHASES, THE HOST`S LIMIT, THE REFUSALS PRINTED, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b750 at its weight after its entry, and the corrigendum for b750, landed through b698's guarded
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
                                                   entered=[], flipped={},
                                                   with_entered=dict(zip(('claim', 'close', 'repeat', 'items'), _c1_read_counts(s))),
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.31.0', bank='data/' + C1_V170, rules='data/b751_rules.txt'),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b751, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b751, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b751's name.
# ### b751's own changes are marked "b751, Component 3". The runner overrides read the act's dispatch rows: (R361)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b751_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R360)(7), as b750 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """N1, b751 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b751: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b751, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R361)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b750, naming tools/standing/hook.py, unedited this act (its last edit b750`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b751, C4, defect (n) (the Edit tool): the step-zero bank writes each deleted ref's tip as "(was 7d34b587)" (data/b751_stepzero.txt :44-:45),
# ### b750's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b750-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b751, Component 3 (the Edit tool): b751's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b750-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b751_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b751_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b751, Component 6 (the Edit tool): b751's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b750's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b751, Component 4 (the Edit tool): b750's overrides of checks 1516 and 1659 (hook.py edited by b750's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b751 as it stands
# ### b751, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b751_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b751, Component 4 (the Edit tool): the corrigendum's events rows (1)-(12), b750's twelve (the template's range is a fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 13)) \
#⟪END⟫
# ### b751, Component 4 (the Edit tool): b750's override of checks 1476-1482 (one ERRATA entry at b750's (R360)(5)) removed -- (R361)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b751 as it stands
# ### b751, Component 3 (the Edit tool): G-BRANCHES-DELETED over b751's two repositories (relay, PLACE-papers) and five
# ### refs; b751, Component 4, defect (m): the step-zero bank writes "KEPT as banked (" -- the seat's row at data/b751_stepzero.txt :43 and the
# ### tool's row (tools/standing/carry.py kept b751) in its dated note -- read in its own wording, the tool's row asked by its own head
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked (the tool`s row, tools/standing/carry.py kept b751' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b751, Component 4 (the Edit tool): G-RUNNER-READ's plant on b751's dispatch rows -- run 2's axiom lines carrying sorryAx (b750's
# ### plant read the lv rows' closure log, which b751 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b751, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b751, Component 6 (the Edit tool): the fold bank was b750's own route
# ### (tools/b750_fold.py); b751's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b751_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b750.py -> tools/acts/b751.py' in (rd('b751_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b751, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b751_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b751, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b751_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b751_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b751, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R361): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R361)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b751')
    return '### THE COUNTER ((R361) Component 5, the act`s events and defects together; relay data/b751_defects.txt, data/b751_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b750, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b751 (defect (d')): the order's
# ### state as b751 leaves it -- the carry from b750 said "as b750 left it ... not touched this act", where b751 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act; W-ORD-MECHANISM-ATTRIBUTION as b750 entered it (PLACE-papers 4ba38687); W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as they were entered;',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b751, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)
#⟪END⟫
# ### b751, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b750's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b751_author_answers.txt', 'b751_answer_check.txt', 'b751_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b751, Component 4's probe: v1.27.0's rdn (repair (7)) refuses a missing file, and _counter (record.tpl :2315) reads the events bank,
# ### which the close writes after the seal; read optional for the events bank alone, the defects bank still refused if missing
#⟪OVERRIDE record MARK 26666a71fb1e 1 REPAIR (reader)⟫
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
#⟪END⟫
# ### b751, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b750's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b751, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b750's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b751_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b751_registration_%s.txt' % __import__('b751_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b751, Component 4 (the Edit tool, before the face): b750's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b751, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b751's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b751, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R361)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b751 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b751_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b751: the controls' one route (N1)
#⟪END⟫
# ### b751, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b750's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b751 scorer reads; the needles set to the banks b751's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b751, (R361)(2)(iii): b750's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b751, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b751_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b751, Component 4 (the Edit tool): (R361)(2)[G1], [G2] passed two ERRATA entries; the template's arm wants ERRATA byte-equal to its
# ### blob at the act's base. In its place: no DIFFERS entry; ERRATA at HEAD its base's bytes with the two entries appended and nothing
# ### else, each id once at HEAD and absent at the base, each entry's write the worklist's (ERRATA_IDS); the weight line as before
#⟪OVERRIDE checks MARK dd4dd9cb3d4b 6⟫
    """(R361)(1)-(2): no DIFFERS entry; two ERRATA entries this act ([G1], [G2]) -- ERRATA.md at HEAD its blob at the act's base with the
    two entries appended, nothing before them changed, each id once at HEAD and absent at the base; no b751 differs or errata bank; the
    weight line and the corrigendum at FINDINGS in Component 1's PLACE-papers commit, FINDINGS the one file there."""
    _t = lambda x_: x_.decode('utf-8', 'replace') if isinstance(x_, bytes) else (x_ or '')
    nt_, pt_ = _t(S['errata_pp_now']).replace(chr(13), ''), _t(S['errata_pp_pre']).replace(chr(13), '')
    return bool(pt_) and nt_.startswith(pt_) and nt_ != pt_ and not S['differs'] and not S['errata'] \
        and all(nt_.count('\n## %s ' % i_) == 1 and ('\n## %s ' % i_) not in pt_ for i_, _h in K.ERRATA_IDS) and len(K.ERRATA_IDS) == 2 \
        and K.DIFFERS_LINE is None and K.ERRATA_LINE is None and K.ERRATA_ID is None and S['files']['c1pp'] == ['FINDINGS.md'] \
        and 'weight' in fline(S, K.WEIGHT_LINE).lower()
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'f' else 'SEAT') for c in tuple('abcdefghijklmnopqrstuv')))   # ### (a)-(v) so far, the navigator's (f) (the ruling's path), the rest the seat's (data/b751_defects.txt); reset to the letters entered before the lock
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b751_corrigendum.txt', 'data/b751_standing_v1300.txt', 'data/b751_sitting_agenda.txt', 'data/b751_sitting.txt',
                  'data/b751_cq_sign.txt', 'data/b751_line.txt', 'data/b751_rules.txt', 'data/b751_pathrefusal.txt',
                  'data/b751_reproduce.txt', 'data/b751_reproduce.json', 'data/b751_address_scan.txt', 'data/b751_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b751 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R361)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b751_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R361)(4): the sitting bank's rows by label -- a row opens `[A1] STATE`, `[C] STATE`, `[(7)] ...` at column 0, its fields indented two
    spaces as `KEY: value` (a field's continuation lines deeper and skipped); returned {label: {'state', 'word', 'at', 'confirm', 'file', 'draft'}}.
    Pure in its argument."""
    out, cur = {}, None
    for l in (t or '').split(NL):
        m = re.match(r'^\[([A-Z]\d*|\(\d+\))\] (.+)$', l)
        if m:
            cur = out.setdefault(m.group(1), dict(state=m.group(2).strip()))
            continue
        f = re.match(r'^  ([A-Z][A-Z` ]+?)(?: \(\d+\))?: (.*)$', l)   # ### a numbered field, [A5]'s "THE AUTHOR`S WORD (1)" and "(2)", read as the field, the words joined
        if cur is not None and f:
            k = {'THE AUTHOR`S WORD': 'word', 'AT': 'at', 'CONFIRMATION': 'confirm', 'FILE': 'file', 'DRAFT WRITTEN': 'draft'}.get(f.group(1))
            if k:
                cur[k] = ((cur[k] + ' ; ') if cur.get(k) else '') + f.group(2).strip()
        elif not l.strip():
            cur = None
    return out


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R361)(1)-(4) (b751's keys over b751's objects): the order by time and ancestry; v1.30.0's controls; the agenda, the ten
        # ### items' writes, [E]'s generator, its bank and I-109; the sitting record; the line bank; zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b750's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1300', K.STANDING_COMMIT, K.C1_STANDING), ('v1300_corr', K.C1_STANDING, K.C1_CORR),
                                 ('corr_agenda', K.C1_CORR, K.AGENDA_COMMIT), ('agenda_gen', K.AGENDA_COMMIT, K.CQ_GEN[0]),
                                 ('gen_bank', K.CQ_GEN[0], K.CQ_BANK[0]), ('bank_sitting', K.CQ_BANK[0], K.SITTING_COMMIT),
                                 ('sitting_c3', K.SITTING_COMMIT, K.C3_RELAY[0]))),
        # ### b751 (R361)(1)-(2): the order within PLACE-papers by ancestry -- the weight and corrigendum, then the ten items in the agenda's order
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in [('pre_c1', K.PRE_PP, K.C1_PP), ('c1_%s' % K.ITEM_PP[0][0], K.C1_PP, K.ITEM_PP[0][1])]
                   + [('%s_%s' % (x[0], y[0]), x[1], y[1]) for x, y in zip(K.ITEM_PP, K.ITEM_PP[1:])]),
        v1130=rd('b751_standing_v1300.txt'), v1281=None, plan=read(os.path.join(ROOT, *K.PLAN_BANK.split('/'))), print_=read(os.path.join(ROOT, *K.POSCONTROL_PLAN.split('/'))),
        controls=rd('b751_cq_sign.txt'), notes=rd('b751_sitting.txt'), rows_bank=rd('b751_line.txt'), routes=rd('b751_sitting_agenda.txt'), zanswers=rd('b751_author_answers.txt'),
        cq_src=raw(os.path.join(ROOT, *K.CQ_GEN[1].split('/'))), cq_blob=blob(ROOT, '%s:%s' % (K.CQ_GEN[0], K.CQ_GEN[1])),
        cq_bank_blob=_s(blob(ROOT, '%s:%s' % (K.CQ_BANK[0], K.CQ_BANK[1]))), cq_tools=sorted(f_ for f_ in os.listdir(T) if f_.startswith('b751_cq')),
        instruments=read(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        plan_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.PLAN_BANK))), print_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.POSCONTROL_PLAN))),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP,) + tuple(x[1] for x in K.ITEM_PP)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP,) + tuple(x[1] for x in K.ITEM_PP)),
        numstat=dict((h_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for h_ in tuple(x[1] for x in K.ITEM_PP)),
        c3_blobs=dict((p_, _s(blob(ROOT, '%s:%s' % (K.C3_RELAY[0], p_)))) for p_ in ('data/b751_line.txt', 'tools/b751_line.py')),
        readme=read(os.path.join(PP, 'README.md')), readme_pre=_s(blob(PP, '%s:README.md' % K.PRE_PP)),
        reg_at=_s(blob(PP, '%s:REGISTRY.md' % K.ITEM_PP[4][1])),
        reg_now_pp=read(os.path.join(PP, 'REGISTRY.md')), reg_pre_pp=_s(blob(PP, '%s:REGISTRY.md' % K.PRE_PP)),
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
        sit_files={}, sit_main={},
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b751_dispatch_rows.json') or '[]'), reproduce=rd('b751_reproduce.txt'), reproducej=jl('b751_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b751_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b750 left them
        rebuild=None, rebuild_rows=json.loads(rd('b751_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               agenda=_ct(ROOT, K.AGENDA_COMMIT), gen=_ct(ROOT, K.CQ_GEN[0]), bank=_ct(ROOT, K.CQ_BANK[0]), s2=_ct(ROOT, K.C2_RELAY),
               items=[_ct(PP, x[1]) for x in K.ITEM_PP], c3=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), s2=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY[0]),
                   c1pp_=files_of(PP, K.C1_PP), agenda=files_of(ROOT, K.AGENDA_COMMIT), gen=files_of(ROOT, K.CQ_GEN[0]), bank=files_of(ROOT, K.CQ_BANK[0]),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b751's read-first bank's items by path, as its step zero wrote them (data/b751_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b750_closing.txt |', 'relay data/b750_events.txt |', 'relay data/b750_defects.txt |', 'relay data/b750_author_answers.txt |',
                     'relay data/b750_author_words.txt |', 'relay data/b746_integration_draft.txt |', 'relay data/b743_sitting_agenda.txt |',
                     'PLACE-papers phase1.5/method/THE_METHOD_CANON.md |', 'PLACE-papers README.md |', 'PLACE-papers REGISTRY.md |', 'PLACE-papers SPIRAL_MAP.md |',
                     'PLACE-papers ERRATA.md |', 'PLACE-papers phase1.5/method/INSTRUMENTS.md |', 'relay data/b725_interference.txt |',
                     'SIDE-explicit-formula at 14ca5725 (v0.38) |', 'relay data/b750_ferry.txt |', 'relay data/b750_stepzero.txt |')   # ### data/b751_readfirst.txt :14-:40, read before this edit
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R361)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'SITTING ((R361)(2))', 'LINE ((R361)(4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (180 = 180 + 0, data/b751_citation_check.txt :193), no miss; the
    check CLEAN; the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 180 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b751, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b750's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b751, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R361)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b750()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R361)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b751_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b750's figures, read at FINDINGS :14536 as Component 1 landed them (b750's closing head quoted)
    return landed(S, 0, ['b750 AT ITS WEIGHT', 'suite 111 of 116', 'relay 20ebea8c', '22 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b751's title in the ferry's Component 4 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## The synthesis sitting: 10 of 11 items passed; ',
                 'the stages in the canon as XXIII and criterion (9); the front door at v0.38; 1.5c-21’s grade note; d1-1 kept; ',
                 'cQ(n) over n ≤ 3000: 102 negative, the smallest n = 48; ',
                 'the Epstein cluster seated, THE_EPSTEIN_CONTROL_OBJECT its keystone in progress, Which_Structure_Confines noted; two errata; ',
                 'the append-route for answers and 11 repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R361)(1), (3): the generated entry for b750's twelve events and twenty-two defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(12), the defects by the one lettering (a)-(v); every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 12, CLOSE 22 over 34, REPEAT 14; the navigator's two entered apart); the repairs at
    tools/standing/ v1.30.0 by their controls bank; the corrigenda bank appended at row (70) and nothing before it changed; in Component 1's
    commits (the figures read from data/b751_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 22 and len(items) == j.get('items') == 34 and j.get('row') == 70 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 34 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 12 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 14 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.30.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 and len(j.get('entered') or []) == 2 \
        and '  (70) ' in S['corrigenda'] and '  (71) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R361)(3) orders the rules bank data/b751_rules.txt, one row per repair, thirteen rows (1)-(13); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here first committed with v1.29.0 (C1_RULES), in no other commit."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', S['rules'] or '')] == list(range(1, 14)) and 'data/b751_rules.txt' in S['files']['rules'] \
        and sorted(gs(ROOT, 'log', '--format=%H', '--', 'data/b751_rules.txt').split()) == sorted(gs(ROOT, 'rev-parse', K.C1_RULES).split()) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b751's keys, the report sections' own heads
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.30.0', 'REGISTERED -- THE SITTING', 'REGISTERED -- THE SIGN OF cQ(n)',
               'REGISTERED -- THE INTEGRATION LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b751: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b751, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b751_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b751, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail; the sitting's ten passed items' files: the canon, README, REGISTRY, INSTRUMENTS, SPIRAL_MAP, Which_Structure_Confines_v2_4_0,
    ERRATA), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b751's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The sitting**', '**The sign of cQ(n)**', '**The integration line**',
                 '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b751_corrigendum.txt', 'data/b751_standing_v1300.txt', 'data/b751_rules.txt', 'data/b751_sitting_agenda.txt', 'data/b751_sitting.txt',
                 'data/b751_author_answers.txt', 'data/b751_cq_sign.txt', 'data/b751_line.txt',
                 'data/b751_reproduce.txt', 'data/b751_address_scan.txt', 'data/b751_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ('f',)               # ### b751: the navigator's row of the defects bank, (f) (the ruling's path for [F1]/[F2]); the rest the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R361)(1)-(2), N2, N5 (the name the frozen run list carries): the PLACE-papers writes in their order -- the weight and corrigendum in
    a commit touching FINDINGS alone in one hunk, its first two added lines b750 at its weight ("*Appended 2026-11-09 by b751 to b750’s
    entry") and the corrigendum's heading ("## Corrigendum to b750’s record"), removing none; then the ten passed items, each one commit
    touching its one file (the worklist's ITEM_PP), its lines added and removed as git's numstat prints them ([B1] the one line of :164
    rewritten with its appendix, every other item removing none), in the agenda's order by ancestry, each after the agenda's relay commit;
    the plans of b744 unedited at their step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    t_ = S['t']
    dd_ = S['disch_diff'] or {}
    a0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    r0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('-') and not l.startswith('---')]
    hunks_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(a0_) >= 2 and len(hunks_) == 1 and a0_[0].startswith('+*Appended 2026-11-09 by b751 to b750’s entry') \
        and a0_[1].startswith('+## Corrigendum to b750’s record') and r0_ == []
    files_ = [S['reg_pp'].get(x_[1]) for x_ in K.ITEM_PP]
    ns_ = [S['numstat'].get(x_[1]) or [] for x_ in K.ITEM_PP]
    num_ = all(n_ == [str(x_[3]), str(x_[4]), x_[2]] for n_, x_ in zip(ns_, K.ITEM_PP))
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    its_ = t_.get('items') or []
    return bool(one_) and S['reg_pp'].get(K.C1_PP) == ['FINDINGS.md'] and files_ == [[x_[2]] for x_ in K.ITEM_PP] and num_ and md_ \
        and len(its_) == len(K.ITEM_PP) and all(its_) and t_.get('c1pp') and t_.get('agenda') and t_['c1pp'] <= t_['agenda'] < min(its_) \
        and its_ == sorted(its_) and set(x_[2] for x_ in K.ITEM_PP) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b751_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R361)(1)-(4), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, v1.30.0, the weight and
    corrigendum (PLACE-papers, then relay), the agenda, [E]'s generator before its bank, the sitting record, the line bank; by ancestry
    within the relay v9, v1.30.0, the corrigendum, the agenda, the generator, the bank, the sitting record, the line bank."""
    t_ = S['t']
    ks_ = ('stepzero', 'standing', 'c1pp', 'corr', 'agenda', 'gen', 'bank', 's2', 'c3')
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) and t_['gen'] < t_['bank'] \
        and bool(S['anc']) and len(S['anc']) == 7 and all(v is True for v in S['anc'].values())
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R361)(2)[E], N2, N3 (the name the frozen run list carries): the sign of cQ(n) -- the generator tools/b751_cq_sign.py committed alone
    of the bank (relay CQ_GEN) before the bank's commit (CQ_BANK), its md5 the worklist's in the working tree and at its commit; the bank at
    HEAD its blob at its commit, its four controls' sections before the figure's section, its foot the worklist's CQ_FOOT, the controls all as
    wanted; I-109 in INSTRUMENTS citing the bank, the generator's md5 and both commits, saying nothing about Z_Q's zeros; no other b751
    cQ tool; no network reach in the generator."""
    return _cq_ok(S)


# ### the record section's INTEGRATION_LINE, the same bytes (the checks and the record are separate modules; G-COUNT-ROUTE-PRICED reads the line
# ### bank against it, and the record's entry ends with it)
_INTEG_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
               'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


def _cq_ok(S):
    import hashlib as _hl
    c_ = S['controls'] or ''
    t_ = S['t']
    v_ = _vlast(c_)
    ks_ = [c_.find(h_) for h_ in ('## (K4) ', '## (K1) ', '## (K2) ', '## (K3) ', '## THE FIGURE: ')]
    src_ = S['cq_src'] or b''
    ir_ = next((l_ for l_ in (S['instruments'] or '').replace(chr(13), '').split(NL) if l_.startswith('**Reads.**') and 'b751_cq_sign' in l_), '')
    net_ = re.search(r'\b(?:urllib|requests|http\.client|socket)\b', src_.decode('utf-8', 'replace'))
    return _hl.md5(src_).hexdigest() == K.CQ_GEN[2] and src_ == (S['cq_blob'] or b'') \
        and K.CQ_GEN[1] in S['files']['gen'] and K.CQ_BANK[1] not in S['files']['gen'] and K.CQ_BANK[1] in S['files']['bank'] \
        and all(t_.get(k_) for k_ in ('gen', 'bank')) and t_['gen'] < t_['bank'] \
        and (S['cq_bank_blob'] or '').replace(chr(13), '') == c_.replace(chr(13), '') and all(i_ >= 0 for i_ in ks_) and ks_ == sorted(ks_) \
        and K.CQ_FOOT in v_ and v_.endswith('s.') \
        and bool(ir_) and all(w_ in ir_ for w_ in ('data/b751_cq_sign.txt', K.CQ_GEN[2], K.CQ_GEN[0], K.CQ_BANK[0], 'nothing about Z_Q’s zeros')) \
        and S['cq_tools'] == ['b751_cq_sign.py'] and not net_
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R361)(6) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b750 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b750's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
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
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.30.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1300') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b750's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R361)(2), (4), N2, N3, N5 (the name the frozen run list carries): the sitting and the line -- the agenda committed alone of every
    item's write, before the first; the sitting record's eleven rows, each state the worklist's SITTING_STATES, each passed row's
    CONFIRMATION naming its commit (ITEM_PP, [E] also the generator and the bank), [D]'s none; its foot DECIDED 11, PASSED 10, KEPT 1,
    STRUCK 0, the scan 0 at every commit, the author's words 4; the answers bank carrying the four words between BEGIN and END; the record in
    the sitting commit with the answers pair. The line bank's foot COMPOSED and ALL AS READ, its line the act module's INTEGRATION_LINE, the
    cluster table read, the keystone and the sibling anchor carrying no row of the figure with their positive controls read, the limit of
    (C) printed; Component 3's commit carrying the line bank and its tool; b746's draft unchanged; no Zenodo tool this act."""
    r_ = S['rows_bank'] or ''
    v_ = _vlast(r_)
    sit_ = S['notes'] or ''
    rows_ = _sitting_rows(sit_)
    ip_ = dict((x_[0].strip('[]'), x_[1]) for x_ in K.ITEM_PP)
    st_ = dict((k_.strip('[]'), s_) for k_, s_ in K.SITTING_STATES.items())
    rows_ok_ = sorted(rows_) == sorted(st_) and all((rows_[k_].get('state') or '').startswith(s_) for k_, s_ in st_.items()) \
        and all(ip_[k_] in (rows_[k_].get('confirm') or '') for k_ in ip_) and K.CQ_GEN[0] in (rows_.get('E') or {}).get('confirm', '') \
        and K.CQ_BANK[0] in (rows_.get('E') or {}).get('confirm', '') and 'no commit' in (rows_.get('D') or {}).get('confirm', '')
    foot_ = _vlast(sit_) == 'THE SITTING: DECIDED 11 ; PASSED 10 ; KEPT 1 ; STRUCK 0 ; GIT WRITES 12 AND THE AGENDA ; SCAN 0 ; 0 ; 0 ; 0 AT EVERY COMMIT ; THE AUTHOR`S WORDS 4, VERBATIM.'
    words_ = re.findall(r'BEGIN(.+?)END', S['zanswers'] or '', re.S)
    agf_ = S['files']['agenda']   # ### the agenda's commit: the agenda and the act's step and hash banks, no PLACE-papers path, no item's write
    agenda_alone_ = 'data/b751_sitting_agenda.txt' in agf_ and all(f_.startswith('data/b751_') or f_ == 'tools/b751_worklist.py' for f_ in agf_)
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b751_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return rows_ok_ and foot_ and len(words_) >= 4 and agenda_alone_ \
        and 'data/b751_sitting.txt' in S['files']['c2'] and 'data/b751_author_answers.txt' in S['files']['c2'] \
        and v_.startswith('THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP AFTER THE SITTING ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; STAGE CLUSTERED ;') \
        and v_.endswith('; ALL AS READ.') and ('      %s' % _INTEG_LINE) in r_ and 'THE LIMIT OF (C):' in r_ \
        and re.search(r'its cluster rows ([1-9]\d*) \(the control: the table read, not empty\)', r_) is not None \
        and len(re.findall(r': 0 \(the positive control, rows naming \w+ by the same reader: [1-9]\d*\)', r_)) == 2 \
        and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and {'data/b751_line.txt', 'tools/b751_line.py'} <= set(S['files']['c3']) and zt_ == []

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
    """standing clauses v9 (Component 7 of (R361): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b751_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b750's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R361-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b750's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R361) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b750's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R360)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 8ce7e3ab',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 180 = 180 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b750-\w+) \((?:was )?[0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s C4 form: the synthesis sitting, 10 of 11 items passed; the stages as XXIII and criterion (9); the front door at v0.38; 1.5c-21`s grade note; d1-1 kept; cQ(n) over n <= 3000, 102 negative, the smallest n = 48; the Epstein cluster seated; two errata; the append-route for answers and the repairs landed, counted from v1.30.0`s controls',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R361)(1), (3): the generated corrigendum for b750`s record, landed at FINDINGS :14538: its twelve events and twenty-two defects, 34 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 12 CLOSE 22, REPEAT 14, the navigator`s two entered apart; v1.30.0`s repairs by data/b751_standing_v1300.txt; the corrigenda bank appended at row (70)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R361)(3)`s rules bank data/b751_rules.txt, thirteen rows (1)-(13), committed with v1.30.0 (66efee55) alone',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b751's objects
    ('G-REGISTRATIONS-FIRST', '(R361)(1)-(2), N2, N5: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (4ffea12e), none removed; the ten passed items, each one commit touching its one file, its lines as numstat prints them, in the agenda`s order after the agenda`s commit (7ce3e6ea); the PLACE-papers order by ancestry',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'numstat', lambda d: d.update({K.ITEM_PP[2][1]: ['1', '0', 'README.md']}))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b751_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R361)(1)-(4), N2: the act`s order by time -- step zero, v1.30.0, the weight and corrigendum, the agenda, [E]`s generator before its bank, the sitting record, the line -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(gen_bank=False))),
    ('G-DERIVATION-GRADED', '(R361)(2)[E], N2, N3: the generator tools/b751_cq_sign.py at a1655706, md5 789afca8, before its bank at 56ddafa5; the bank its blob, the controls (K1)-(K4) before the figure, its foot NEGATIVE 102, the smallest n = 48, exactly zero 2498, nonnegative 399, the controls all as wanted; I-109 citing the bank, the md5 and both commits, nothing about Z_Q`s zeros; no network reach',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'controls', (S['controls'] or '').replace('NEGATIVE 102 ;', 'NEGATIVE 101 ;'))),
    ('G-OFFSET-POST-HOC', 'N5, (R361)(6): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.30.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R361)(2), (4), N2, N3, N5: the agenda alone at 7ce3e6ea before the first item; the sitting record`s eleven rows, each state as decided, each passed row confirming its commit, [D] none; its foot DECIDED 11 PASSED 10 KEPT 1 STRUCK 0, the author`s words 4 in the answers bank; the line bank COMPOSED and ALL AS READ, its line the module`s, stage CLUSTERED, the keystone and the sibling anchor read with their positive controls, the limit of (C) printed; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'notes', (S['notes'] or '').replace('[D] KEEP', '[D] PASS'))),
    ('G-DIFFERS-ERRATA', '(R361)(1)-(2): no DIFFERS entry; two ERRATA entries ([G1], [G2]) -- ERRATA.md at HEAD its base`s bytes with E-2026-11-09-1 and E-2026-11-09-2 appended and nothing else, each id once; no differs or errata bank; the weight line and the corrigendum in 4ffea12e, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b751_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R361-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b750`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b750 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b750 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS, OPEN_TRAILS and the sitting`s passed items` files, (R361)(1)-(2)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b750`s trail record on OPEN_TRAILS (:18038) and its root in the chain', lambda S: '### b750 — lane two, act one hundred and seventy-six, the held draft under (R360)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the sitting`s files): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b751 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b750's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b751: (R361)'s rows, written at step zero over b750's carried rows (scratch splice751.py). (1)'s line read by the ruling from the public relay at 467a1968
    pub = _blob('D:/relay', '467a1968', 'data/b750_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b750_closing.txt :1, the head line as the public relay carries it at 467a1968', bool(pub) and pub[0] == at(cl, 1) and 'relay 766f0363' in pub[0] and 'PLACE-papers 88942b4' in pub[0],
        'remote main %s' % rm[:8], '1')
    add('ruling (1)', 'relay remote main read back at 467a1968 after b750`s closing push', rm.startswith('467a1968'), rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root fbd3c1d6dd1a0bc1', '12 prompts answered', 'scores 8 of 8 HELD', '25 defects'):
        add('ruling (1)', 'data/b750_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1), (3)', 'data/b750_closing.txt :5, the counter CLAIM 3, CLOSE 29, REPEAT 17 OF 32, DEFECTS 25, EVENTS 7', 'CLAIM 3, CLOSE 29, REPEAT 17 OF 32' in at(cl, 5) and 'DEFECTS 25, EVENTS 7' in at(cl, 5), at(cl, 5)[-60:], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, 467a1968 and 88942b42', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('467a1968') and gr(PP, 'rev-parse', K.PRE_PP).startswith('88942b42'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    cr_ = lines_of(p('data', 'b750_corrigendum.txt'))
    add('ruling (1)', 'data/b750_corrigendum.txt :92, b749`s corrigendum ITEMS 34 ; CLAIM 12, CLOSE 22 ; REPEAT 14', 'ITEMS 34: EVENTS 12, DEFECTS 22 ; CLAIM 12, CLOSE 22 ; REPEAT 14' in at(cr_, 92), at(cr_, 92)[:60], '1')
    sv_ = lines_of(p('data', 'b750_standing_v1300.txt'))
    add('ruling (1)', 'data/b750_standing_v1300.txt :193, v1.30.0, CASES 39 ; AS WANTED 39', 'v1.30.0' in at(sv_, 193) and 'CASES 39 ; AS WANTED 39' in at(sv_, 193), at(sv_, 193)[:60], '1')
    add('ruling (1)', 'relay 66efee55, tools/standing/ v1.30.0 by a commit of its own', (_blob('D:/relay', '66efee55', 'tools/standing/VERSION') or '').strip() == 'v1.30.0', (_blob('D:/relay', '66efee55', 'tools/standing/VERSION') or '').strip(), '1')
    st_ = lines_of(p('data', 'b750_sitting.txt'))
    add('ruling (1)', 'data/b750_sitting.txt :121, DECIDED 11 ; PASSED 10 ; KEPT 1 ; STRUCK 0 ; GIT WRITES 12 AND THE AGENDA ; THE AUTHOR`S WORDS 4',
        'DECIDED 11 ; PASSED 10 ; KEPT 1 ; STRUCK 0 ; GIT WRITES 12 AND THE AGENDA' in at(st_, 121) and 'THE AUTHOR`S WORDS 4, VERBATIM' in at(st_, 121), at(st_, 121)[:60], '1')
    cq_ = lines_of(p('data', 'b750_cq_sign.txt'))
    add('ruling (1), (4), ferry (read first)', 'data/b750_cq_sign.txt :39, negative 102, n = 48 at -7.742402021816, exactly zero 2498, nonnegative 399, 190.565466363 at n = 2808, (K1)-(K4) as wanted',
        all(w_ in at(cq_, 39) for w_ in ('NEGATIVE 102', 'THE SMALLEST NEGATIVE n = 48, cQ = -7.742402021816', 'EXACTLY ZERO 2498', 'NONNEGATIVE 399', '190.565466363 AT n = 2808', 'CONTROLS (K1)-(K4) ALL AS WANTED')), at(cq_, 39)[:60], '1')
    ln_ = lines_of(p('data', 'b750_line.txt'))
    add('ruling (1), ferry (read first)', 'data/b750_line.txt :9, the INTEGRATION line, keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress), stage CLUSTERED', 'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress)' in at(ln_, 9) and at(ln_, 9).rstrip().endswith('stage CLUSTERED'), at(ln_, 9)[:60], '1')
    rp_ = lines_of(p('data', 'b750_reproduce.txt'))
    add('ruling (1)', 'data/b750_reproduce.txt :275, ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4', 'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4' in at(rp_, 275), at(rp_, 275)[:60], '1')
    asc_ = lines_of(p('data', 'b750_address_scan.txt'))
    add('ruling (1)', 'data/b750_address_scan.txt :34, the scan 0 ; 0 ; 0 ; 0', 'PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0' in at(asc_, 34), at(asc_, 34)[:60], '1')
    for f_ in ('b750_checks.txt', 'b750_checks_postpush.txt'):
        ck_ = lines_of(p('data', f_))
        add('ruling (1)', 'data/%s :16, 116 run, 112 passing, the three declared failing' % f_,
            "ARMS RUN : 116. ### LIVE PASSING : 112. ### LIVE FAILING : 3 ['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH']" in at(ck_, 16), at(ck_, 16)[:60], '1')
    sc9_ = _jl('b750_scores_close.json')
    sc9_ = sc9_.get('scores') or sc9_
    held_ = sorted(k_ for k_, v_ in sc9_.items() if isinstance(v_, list) and v_[:1] == ['HELD'])
    add('ruling (1)', 'data/b750_scores_close.json, 8 of 8 HELD', len(held_) == 8, 'HELD %d' % len(held_), '1')
    sd_ = rd(p('data', 'b750_scores_dry.txt')) or ''
    add('ruling (1), (3)(iii)', 'data/b750_scores_dry.txt, N3 REFUTED before the root on the sitting prompt`s phrase "b746`s entry,"', "b746's entry," in sd_, 'read' if "b746's entry," in sd_ else 'ABSENT', '1')
    ev1_ = lines_of(p('data', 'b750_events.txt'))
    add('ruling (1), (3)(i)', 'data/b750_events.txt :12 (3) and :29 (7), the prev parts out of their order and G-PP-SCOPE`s control, REPEAT b717 (3)', at(ev1_, 12).startswith("    (3) THE SEAT'S [CLOSE ; NEW]") and at(ev1_, 29).startswith("    (7) THE SEAT'S [CLAIM ; REPEAT b717 (3)]"), at(ev1_, 29)[:60], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b750']]
    add('ruling (1)', 'data/act_roots.txt, b750`s root fbd3c1d6 chained from b749`s cd0d867c', len(ar9_) == 1 and ar9_[0][1].startswith('fbd3c1d6') and ar9_[0][2].startswith('cd0d867c'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    b3_ = rd(p('data', 'b750_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE through b750 (b750`s post-push part b3)', 'b750 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b750 AGREE' if 'b750 AGREE' in b3_ else 'ABSENT', '1')
    mv_ = rd(p('data', 'b750_mirror_verify.txt')) or ''
    add('ruling (1)', 'data/b750_mirror_verify.txt, CLEAN ON ALL THREE CLAUSES', 'CLEAN ON ALL THREE CLAUSES' in mv_, 'CLEAN' if 'CLEAN ON ALL THREE CLAUSES' in mv_ else 'ABSENT', '1')
    mi_ = lines_of(p('data', 'b750_mirror.txt'))
    add('ruling (1)', 'data/b750_mirror.txt :2, mirror-refresh-2026-11-09-b750, sha256 d235ecf5', 'mirror-refresh-2026-11-09-b750' in at(mi_, 2) and 'sha256 d235ecf570dc1216' in at(mi_, 2), at(mi_, 2)[:60], '1')
    aw_ = rd(p('data', 'b750_author_words.txt')) or ''
    add('ruling (1), (7), ferry (read first)', 'data/b750_author_words.txt, the author`s word at the root: §5 next, the attribution order`s plan act after it, opening on I-109`s figure',
        'Confirmed: §5 next; the attribution order’s plan act after it, opening on I-109’s figure and the class-group signature of the negative n.' in aw_, 'read', '1')
    rgl_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    for n_, r_ in ((177, '1.5c-21'), (178, '1.5c-22'), (179, '1.5c-23')):
        add('ruling (scope)', 'REGISTRY.md :%d, row %s, an Epstein row' % (n_, r_), at(rgl_, n_).startswith('| %s | The Epstein instance' % r_), at(rgl_, n_)[:60], '1')
    add('ruling (scope), (1)', 'REGISTRY.md :1248, 1.5c-21`s grade note (b750 [C]); :1246, b749`s note to d1-1 kept whole ([D])', at(rgl_, 1248).startswith('*Dated note, b750, 2026-11-09') and '1.5c-21' in at(rgl_, 1248)
        and at(rgl_, 1246).startswith('*Dated note, b749'), at(rgl_, 1248)[:60], '1')
    sml_ = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (scope), (1)', 'SPIRAL_MAP.md :276, the Epstein instance seated, THE_EPSTEIN_CONTROL_OBJECT_v0_1 its keystone in progress', at(sml_, 276).startswith('| **The Epstein instance** (seated 2026-11-09, b750)') and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in at(sml_, 276), at(sml_, 276)[:60], '1')
    cnl_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'THE_METHOD_CANON.md'))
    add('ruling (scope), (1)', 'THE_METHOD_CANON.md :337 criterion (9) and :346 XXIII', at(cnl_, 337).startswith('(9) Synthesis before deposit') and at(cnl_, 346).startswith('## XXIII. The integration line and its stages'), at(cnl_, 346)[:40], '1')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    add('ruling (scope), (1)', 'INSTRUMENTS.md :764, I-109, the sign of cQ(n) over n <= 3000', at(ins_, 764).startswith('## I-109'), at(ins_, 764)[:40], '1')
    add('ruling (scope)', 'the census THE_KEYSTONE_CENSUS_v0_8_3.md at 36 kernels', '36' in NL.join(lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))[:40]), 'read', '1')
    for c_ in ('4ffea12e', 'c26a71e9', '88942b42', '6fc025a1', '0dc0acb3', '90804717'):
        add('ruling (1)', 'PLACE-papers %s, a commit (1) and b750`s banks name' % c_, bool(gr(PP, 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')), gr(PP, 'log', '-1', '--format=%s', c_)[:60], '1')
    for c_ in ('66efee55', '7ce3e6ea', 'a1655706', '56ddafa5', '00dc4267', '118b12b6', 'c671c4cf', 'cb732c95', 'ca4fa5a4', '766f0363', '467a1968'):
        add('ruling (1)', 'relay %s, a commit (1) and b750`s banks name' % c_, bool(gr('D:/relay', 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')), gr('D:/relay', 'log', '-1', '--format=%s', c_)[:60], '1')
    # ### (R361)(2): the two statements, the route and its pins, read from the tree at v0.38 (14ca5725) and from the banks
    EF_ = 'D:/SIDE-explicit-formula'
    tg_ = (gr(EF_, 'rev-parse', 'v0.38') or '').strip()
    tp_ = (gr(EF_, 'rev-parse', 'v0.38^{}') or '').strip()
    add('ruling (2), (6)', 'the tag v0.38 on SIDE-explicit-formula, tag object 21c6edaf, its peel 14ca5725, no tag beyond it', tg_.startswith('21c6edaf') and tp_.startswith('14ca5725') and not gr(EF_, 'tag', '--list', 'v0.39*') and not gr(EF_, 'tag', '--list', 'v0.4?'), '%s ; %s' % (tg_[:8], tp_[:8]), '2')
    em_ = (gr(EF_, 'rev-parse', 'main') or '').strip()
    add('ruling (6)', 'SIDE-explicit-formula main at 8fbab45, unmoved (no merge)', em_.startswith('8fbab45'), em_[:8], '2')
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (5)', 'zq-b730 past v0.38 at 1e658870, kept', zt_.startswith('1e658870'), zt_[:8], '2')
    ef_ = lambda c_, f_: _blob(EF_, c_, f_).replace(chr(13), '').split(NL)   # noqa: E731
    O_ = 'SIDEExplicitFormula/Schema/ZQ/OffZero/'
    sp4_ = ef_('14ca5725', O_ + 'SP4.lean')
    add('ruling (2)(i), ferry (read first)', 'Schema/ZQ/OffZero/SP4.lean :32 zq_offline_zero and :36 zq_li_nonneg_fails at v0.38', at(sp4_, 32).startswith('theorem zq_offline_zero : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1 / 2')
        and at(sp4_, 36).startswith('theorem zq_li_nonneg_fails : ¬ (∀ n : ℕ, 0 ≤ Wide.liCoeff zqZeroConfig n)'), at(sp4_, 32)[:40], '2')
    oz_ = lines_of(p('data', 'b742_offlinezero.txt'))
    add('ruling (2)(i), ferry (read first)', 'data/b742_offlinezero.txt :61-:62, the two statements` axiom lines, propext, Classical.choice, Quot.sound (run 42068096322); :19 the run at 14ca5725',
        all(at(oz_, n_).split()[1:2] == [nm_] and 'propext, Classical.choice, Quot.sound (run 42068096322)' in at(oz_, n_) for n_, nm_ in ((61, 'zq_offline_zero'), (62, 'zq_li_nonneg_fails')))
        and 'sha 14ca5725 | run 42068096322' in at(oz_, 19) and 'KERNEL, exit 0' in at(oz_, 19), at(oz_, 61)[:60], '2')
    add('ruling (2)(i)', 'data/b742_offlinezero.txt :32, the axioms head; :79, SP4 REACHED, NAMES 30 OF 30', at(oz_, 32).startswith('## THE AXIOMS OF EACH PRINTED NAME') and 'SP4 REACHED' in at(oz_, 79) and 'NAMES 30 OF 30' in at(oz_, 79), at(oz_, 79)[:60], '2')
    f43_ = lines_of(p('data', 'b743_ferry.txt'))
    add('ruling (2)(i)', 'data/b743_ferry.txt :11, the three conditions (R353)(2) attached to the discharge: the carrier, the grade confers nothing, one zero with its multiplicity unstated and no n named',
        all(w_ in at(f43_, 11) for w_ in ('(a) the carrier is Z_Q0', '(b) the grade confers nothing', '(c) the located zero is one zero in one box: its multiplicity is not stated', 'no n is named')), at(f43_, 11)[:60], '2')
    for f_ in ('data/b738_sp1.txt', 'data/b740_s5.txt', 'data/b741_c7.txt', 'data/b743_discharge.txt'):
        add('ferry (read first)', '%s -- the path the ferry names: ABSENT; printed absent, the figures read from the banks that carry them' % f_, not os.path.exists(p(*f_.split('/'))), 'absent', '2')
    bx_ = ef_('14ca5725', O_ + 'Box.lean')
    add('ruling (2)(ii)', 'Schema/ZQ/OffZero/Box.lean :21-:24 the corners x0 0.85326, x1 1.05326, y0 16.190216, y1 16.390216 and :31 boxA at v0.38',
        at(bx_, 21).startswith('def x0 : ℝ := 85326 / 100000') and at(bx_, 22).startswith('def x1 : ℝ := 105326 / 100000') and at(bx_, 23).startswith('def y0 : ℝ := 16190216 / 1000000')
        and at(bx_, 24).startswith('def y1 : ℝ := 16390216 / 1000000') and at(bx_, 31).startswith('def boxA : Set ℂ := Ioo x0 x1 ×ℂ Ioo y0 y1'), at(bx_, 31)[:40], '2')
    el_ = ef_('14ca5725', O_ + 'Elem.lean')
    add('ruling (2)(ii)', 'Schema/ZQ/OffZero/Elem.lean :222, the centre cA = 0.95326 + 16.290216 i at v0.38', at(el_, 222).startswith('def cA : ℂ := ⟨95326 / 100000, 16290216 / 1000000⟩'), at(el_, 222)[:40], '2')
    mn_ = ef_('14ca5725', O_ + 'Main.lean')
    o38_ = lines_of(p('data', 'b738_offlinezero.txt'))
    add('ruling (2)(iii)', 'Schema/ZQ/OffZero/Main.lean :24 zq_offline_of_box at v0.38; data/b738_offlinezero.txt :40 its axioms, :80 S5a-S5b', at(mn_, 24).startswith('theorem zq_offline_of_box (c : ℂ) (hc : c ∈ boxA)')
        and 'zq_offline_of_box' in at(o38_, 40) and 'propext, Classical.choice, Quot.sound' in at(o38_, 40) and 'S5a-S5b' in at(o38_, 80), at(mn_, 24)[:40], '2')
    mm_ = ef_('14ca5725', O_ + 'MinModulus.lean')
    add('ruling (2)(iii)', 'Schema/ZQ/OffZero/MinModulus.lean :30, Complex.norm_le_of_forall_mem_frontier_norm_le applied to the reciprocal (hd.inv h)', 'Complex.norm_le_of_forall_mem_frontier_norm_le hU (hd.inv h)' in at(mm_, 30), at(mm_, 30)[:60], '2')
    lm_ = ef_('14ca5725', 'lake-manifest.json')
    am_ = _blob('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'de5ce8a9', 'Mathlib/Analysis/Complex/AbsMax.lean').replace(chr(13), '').split(NL)
    add('ruling (2)(iii), ferry (read first)', 'Mathlib`s AbsMax.lean :405 at the pin de5ce8a9 the kernel`s lake-manifest names (:10)', '"rev": "de5ce8a9' in at(lm_, 10) and 'mathlib' in at(lm_, 11)
        and at(am_, 405).startswith('theorem norm_le_of_forall_mem_frontier_norm_le'), at(am_, 405)[:50], '2')
    ce_ = ef_('14ca5725', O_ + 'Centre.lean')
    add('ruling (2)(iii)', 'Schema/ZQ/OffZero/Centre.lean :247 lamM_centre_encl, within 6 / 10 ^ 13, at v0.38', at(ce_, 247).startswith('theorem lamM_centre_encl') and '≤ 6 / 10 ^ 13' in at(ce_, 247), at(ce_, 247)[:40], '2')
    o41_ = lines_of(p('data', 'b741_offlinezero.txt'))
    add('ruling (2)(iii)', 'data/b741_offlinezero.txt :68, ‖zqFn cA‖ ≤ about 0.0125885 (zqFn_centre_eps), compiled', 'about 0.0125885' in at(o41_, 68) and 'compiled True' in at(o41_, 68), at(o41_, 68)[:60], '2')
    c7_ = lines_of(p('data', 'b741_c7_plan.txt'))
    add('ruling (2)(iii), (iv)', 'data/b741_c7_plan.txt :119 decide at 158 ms; :35 about 1e-14 absolute and 7e-13 relative per point-term', 'type checking 158 ms' in at(c7_, 119) and 'about 1e-14 absolute, 7e-13 relative' in at(c7_, 35), at(c7_, 119)[:50], '2')
    s6_ = lines_of(p('data', 'b742_s6_plan.txt'))
    add('ruling (2)(iii)', 'data/b742_s6_plan.txt :18 10.6 orders of cancellation (the Lipschitz route); :41 the sample radius 0.49; :43 the plan`s B_3 = 7.8004', '10.6 orders of cancellation' in at(s6_, 18)
        and 'radius 0.49' in at(s6_, 41) and 'B_3 = 7.8004' in at(s6_, 43), at(s6_, 18)[:50], '2')
    on_ = lines_of(p('data', 'b742_offlinezero_notes.txt'))
    add('ruling (2)(iii), ferry (read first)', 'data/b742_offlinezero_notes.txt :3 B = 120 and MARGIN 1.0725e-11 against 1e-12; :5 LPq = 6.098e-10; :8 the centre; :9 80 check points', 'B = 120' in at(on_, 3)
        and 'MARGIN 1.0725e-11 against 1e-12' in at(on_, 3) and 'LPq = 6.098e-10' in at(on_, 5) and '6e-13 < 1e-12' in at(on_, 8) and '80 check points' in at(on_, 9), at(on_, 3)[:50], '2')
    fd_ = ef_('14ca5725', O_ + 'FrontierData.lean')
    fr_ = ef_('14ca5725', O_ + 'Frontier.lean')
    stp_ = ef_('14ca5725', O_ + 'Strip.lean')
    ip_ = ef_('14ca5725', O_ + 'Interp.lean')
    add('ruling (2)(iii)', 'at v0.38: FrontierData.lean :373 lp_le and :398 margin; Frontier.lean :140 lamF_frontier_ge; Strip.lean :106 lamF_sphere_le (≤ 120); Interp.lean :220 the discrete Cauchy bound',
        at(fd_, 373).startswith('theorem lp_le') and at(fd_, 398).startswith('theorem margin') and at(fr_, 140).startswith('theorem lamF_frontier_ge') and at(stp_, 106).startswith('theorem lamF_sphere_le')
        and '≤ 120' in at(stp_, 106) and at(ip_, 220).startswith('theorem DiffContOnCl.norm_sub_discreteCauchy_le'), at(fr_, 140)[:40], '2')
    for t_ in ('tools/b741_g5gen.py', 'tools/b742_s6gen.py'):
        add('ruling (2)(iii), ferry (read first)', '%s tracked, its last commit printed' % t_, bool(gr('D:/relay', 'ls-files', '--', t_)), gr('D:/relay', 'log', '-1', '--format=%h', '--', t_), '2')
    ez_ = ef_('14ca5725', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean')
    add('ruling (2)(v)', 'Schema/EpsteinZQ.lean :19 at v0.38, the kernel`s docstring citing Davenport-Heilbronn for Re s > 1', 'Re s > 1 (Davenport-Heilbronn' in at(ez_, 19), at(ez_, 19)[:50], '2')
    kp_ = lines_of(os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'))
    add('ruling (2), ferry (read first)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md :3 v0.1; :9 b748`s note (§3-§4); :170 the heading of §5 standing empty, :172 §6', at(kp_, 3).startswith('*v0.1, a skeleton') and at(kp_, 9).startswith('*Dated note, 2026-11-08, b748')
        and at(kp_, 170).startswith('## 5. The located zero') and not at(kp_, 171).strip() and at(kp_, 172).startswith('## 6.'), at(kp_, 170)[:40], '2')
    mt_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'CERTIFIED_EVALUATION_IN_THE_STRIP_v0_1.md'))
    add('ruling (2)(iv), ferry (read first)', 'phase1.5/method/CERTIFIED_EVALUATION_IN_THE_STRIP_v0_1.md, its skeleton: :1 the title, :19 §8 limits and costs', at(mt_, 1).startswith('# CERTIFIED EVALUATION') and at(mt_, 19).startswith('## 8. Limits and costs'), at(mt_, 19)[:40], '2')
    ag3_ = lines_of(p('data', 'b743_sitting_agenda.txt'))
    add('ferry (read first)', 'data/b743_sitting_agenda.txt :105, [D8] among the headings D0-D9 (:96-:106)', at(ag3_, 105).lstrip().startswith('[D8] 8. What this does not say'), at(ag3_, 105)[:50], '2')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.31.0's commit's parent once it lands, HEAD's blob before
    add('ferry', 'tools/standing/VERSION v1.30.0 entering the act', v0_ == 'v1.30.0', v0_, '1')
    for f_ in ('data/b750_relay_push-b750-closing_push_out.txt', 'tools/mirror_prevbuild.json', 'data/b750_address_scan_commits.txt'):
        add('ruling (3)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (3), ferry (read first)', 'events (1)-(7) and 25 defects (data/b750_events.txt, data/b750_defects.txt)',
        starts == list(range(1, 8)) and len(letters) == 25, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    ev = lines_of(p('data', 'b750_events.txt'))
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    for n_, k_, w_ in ((4, 1, "THE SEAT'S [CLOSE ; NEW]"), (7, 2, "THE SEAT'S [CLOSE ; NEW]"), (12, 3, "THE SEAT'S [CLOSE ; NEW]"),
                       (18, 4, "THE SEAT'S [CLOSE ; REPEAT b750 (a)]"), (20, 5, "THE SEAT'S [CLOSE ; REPEAT b750 (g)]"), (22, 6, "THE SEAT'S [CLOSE ; NEW]"),
                       (29, 7, "THE SEAT'S [CLAIM ; REPEAT b717 (3)]")):
        add('ruling (3), ferry (read first)', 'data/b750_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    add('ruling (3)(i)', 'data/b750_events.txt :12, (3) standing-a2 run before standing-a1 had banked its half, standing-b3 before b2a-d', 'standing-a2 at' in at(ev, 12) and 'standing-b3 at 05:45:05Z' in NL.join(ev[11:15]), at(ev, 12)[:60], '1')
    add('ruling (3)(i)', 'data/b750_events.txt :29-:36, (7) G-PP-SCOPE "POS PASSES -- DEFECTIVE", its plant README.md inside the allowed set', 'POS PASSES -- DEFECTIVE' in NL.join(ev[28:36]) and 'README.md' in NL.join(ev[28:36]), at(ev, 30)[:60], '1')
    add('ruling (3)(ix)', 'data/b750_events.txt :22, (6) the push refused for an uncommitted step row', 'THE STEP BANK data/b750_steps.json CARRIES AN UNCOMMITTED ROW' in NL.join(ev[21:25]), at(ev, 22)[:60], '1')
    df_ = lines_of(p('data', 'b750_defects.txt'))
    TAGS_ = (('a', "THE SEAT'S", 'CLOSE ; REPEAT b749 (a)'), ('b', "THE SEAT'S", 'CLOSE ; NEW'), ('c', "THE SEAT'S", 'CLOSE ; REPEAT b749 (c)'), ('d', "THE SEAT'S", 'CLAIM ; REPEAT b749 (d)'),
             ('e', "THE SEAT'S", 'CLOSE ; NEW'), ('f', "THE NAVIGATOR'S", 'CLAIM ; NEW'), ('g', "THE SEAT'S", 'CLOSE ; REPEAT b750 (a)'), ('h', "THE SEAT'S", 'CLOSE ; NEW'),
             ('i', "THE SEAT'S", 'CLOSE ; NEW'), ('j', "THE SEAT'S", 'CLOSE ; NEW'), ('k', "THE SEAT'S", 'CLOSE ; NEW'), ('l', "THE SEAT'S", 'CLOSE ; REPEAT b749 (f)'),
             ('m', "THE SEAT'S", 'CLOSE ; REPEAT b749 (g)'), ('n', "THE SEAT'S", 'CLOSE ; REPEAT b750 (a)'), ('o', "THE SEAT'S", 'CLOSE ; NEW'), ('p', "THE SEAT'S", 'CLOSE ; NEW'),
             ('q', "THE SEAT'S", 'CLOSE ; REPEAT b750 (a)'), ('r', "THE SEAT'S", 'CLOSE ; REPEAT b750 (g)'), ('s', "THE SEAT'S", 'CLOSE ; REPEAT b749 (o)'), ('t', "THE SEAT'S", 'CLOSE ; NEW'),
             ('u', "THE SEAT'S", 'CLOSE ; REPEAT b750 (o)'), ('v', "THE SEAT'S", 'CLOSE ; REPEAT b750 (a)'), ('w', "THE SEAT'S", 'CLOSE ; REPEAT b750 (a)'), ('x', "THE SEAT'S", 'CLOSE ; NEW'),
             ('y', "THE SEAT'S", 'CLOSE ; REPEAT b749 (v)'))
    for n_, (l_, o_, t_) in zip(range(7, 32), TAGS_):
        add('ruling (3), ferry (read first)', "data/b750_defects.txt :%d, (%s) %s [%s]" % (n_, l_, o_, t_), at(df_, n_).startswith("    (%s) %s [%s]" % (l_, o_, t_)), at(df_, n_)[:60], '1')
    add('ruling (3)', 'data/b750_defects.txt :12, (f) the navigator`s, the project mirror`s path given for a PLACE-papers file', "(f) THE NAVIGATOR'S" in at(df_, 12) and 'Which_Structure_Confines' in at(df_, 12), at(df_, 12)[:60], '1')
    add('ruling (3)(ii)', 'data/b750_defects.txt :14 (h) and :15 (i), writes outside the (W) list (tools/standing/deletes.py by Write; tools/act_close.py by Edit)', 'tools/standing/deletes.py' in at(df_, 14) and 'tools/act_close.py' in at(df_, 15), at(df_, 15)[:60], '1')
    add('ruling (3)(v)', 'data/b750_defects.txt :30, (x) the address scan left out of a commit', 'left out of relay cc1fc182' in at(df_, 30), at(df_, 30)[:60], '1')
    add('ruling (3)(vi)', 'data/b750_defects.txt :16, (j) the rendered module`s IndentationError', 'IndentationError' in at(df_, 16), at(df_, 16)[:60], '1')
    add('ruling (3)(ix)', 'data/b750_defects.txt :26, (t) the run moved to the background by the host`s default limit', 'default two minutes' in at(df_, 26), at(df_, 26)[:60], '1')
    hr_ = lines_of(p('data', 'b750_hook_refusals.txt'))
    add('ruling (3)(x)', 'data/b750_hook_refusals.txt, 19 refusals', len([l_ for l_ in hr_ if l_.strip()]) == 19, '%d lines' % len([l_ for l_ in hr_ if l_.strip()]), '1')
    ln4_ = lines_of(p('data', 'b750_line.txt'))
    add('ruling (3)(iv)', 'data/b750_line.txt :26-:29, b745-b748 read SYNTHESISED by the cluster, the entry`s own finding not matched; :31 the limit', all('as the maps read now SYNTHESISED' in at(ln4_, n_) for n_ in (26, 27, 28, 29)) and at(ln4_, 31).lstrip().startswith('THE LIMIT OF (C)'), at(ln4_, 31)[:50], '1')
    add('ruling (1)', 'FINDINGS :%d, b750`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## '), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b749`s weight line and corrigendum (b750`s), the form b751`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fi, K.B711_WEIGHT)) and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum'), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b750`s trail record, its hand section' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b750 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (1)', 'OPEN_TRAILS :%d, b750`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('ferry (read first)', 'the hook`s settings file D:/.claude/settings.json by its hash alone', bool(__import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), __import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.30.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.30.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R361)(1): b750's export, the mirror's last
    add('ruling (1)', '%s, b750`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: SIDE-explicit-formula and the other clones at the paths the worklist holds, each listed, a path absent printed absent
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R361)(3), (5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), (6)', 'the push-b750-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R361)(3), (5): act_current alone, then b750's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b750_relay_push-b750-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['tools/mirror_prevbuild.json'])):
        if fs_ == ['tools/mirror_prevbuild.json'] and not c_:   # ### b751: committed alone if it differs from HEAD's blob beyond line endings, else restored
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
    add('ferry (read first)', 'data/b751_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b751_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b751 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b750_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.30.0's controls and the rules, the sitting's agenda and record, the cQ bank, the line bank, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R361)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R361)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R361)(6): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b751 ((R361)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R360)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b751 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTY-SEVEN, THE SYNTHESIS SITTING: b750 AT ITS WEIGHT AND ITS CORRIGENDUM; '
              'v1.30.0; THE SITTING, ELEVEN ITEMS DECIDED; THE SIGN OF cQ(n) OVER n <= 3000 BANKED AS I-109; THE INTEGRATION LINE, UNDER (R361).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b750's sections over b750's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.30.0: the answers route appending, the hook`s row (65) and the design list, a halt question naming its costs, the author`s words composed at the close, the closing dry`s design banks, N5 on the Zenodo banks, the question count, the lock print, the permission rule, the carry`s R5 and shared_edits, the retries rule, the delete reader, each case failing before its repair and passing after', 'b751_standing_v1300.txt'),
                ('the thirteen rules of (R361)(3)', 'b751_rules.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE SITTING ((R361)(2))', [
                ('the record of the sitting: eleven items decided, ten passed, [D] kept with no write, none struck, the author`s words verbatim', 'b751_sitting.txt'),
                ('[E]: the sign of cQ(n) over n <= 3000, its four controls before its figure', 'b751_cq_sign.txt'),
                ('the probe-path refusal printed before the lock gate', 'b751_pathrefusal.txt')]),
            ('THE LINE ((R361)(4))', [
                ('the INTEGRATION line from REGISTRY and SPIRAL_MAP after the sitting, stage CLUSTERED, the earlier lines read again, none rewritten', 'b751_line.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b751_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b750`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument entered, a planted wrong figure per run row', 'b751_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R360)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R361)(6)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b750 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b750-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the agenda banked with every draft before the first item, [E]`s generator committed before its run and its controls before its figure, each item`s CURRENT read at HEAD, the tools` controls before their figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: the sitting`s writes read where they landed -- the Current sentence and [F2]`s note closing on RH and h2 standing where they stood, no literature claim, I-109 saying what was computed and nothing about Z_Q`s zeros ; no sentence saying a thing was deposited, published or versioned ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b751_address_scan.txt, data/b751_address_scan_postlock.txt, data/b751_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS (the trail), and the sitting`s ten passed items, one write each: THE_METHOD_CANON (XXIII, criterion (9)), README (:164, Current), REGISTRY (the 1.5c-21 note), INSTRUMENTS (I-109), SPIRAL_MAP (the Epstein row), Which_Structure_Confines_v2_4_0 (the [F2] note), ERRATA (two entries) ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b751`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.30.0 by (R361)(3) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b750 unedited, act_current`s shared_edits empty ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R361)(4) AND (8)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s question, the act after this one (section 5 of the paper, confirmed or renamed), its answer in relay data/b751_author_answers.txt ;',
    '        the line bank`s reading of b745-b748`s INTEGRATION lines as SYNTHESISED by the cluster, each entry`s finding not matched by needle, for the author`s keep or strike (relay data/b751_line.txt (C)) ; the attribution order`s plan act, opening on [E]`s figure (relay data/b751_cq_sign.txt) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b751_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b750 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b751: the standing repairs are v1.30.0's ((R361)(3), relay data/b751_standing_v1300.txt, read in the corrigendum section); the
    # ### carry's diffs here (b751 carried at step zero before the fold; its tools since are the templates and tools/acts/b751.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b750 left them; port-b707 at b712`s tip %s)' % (
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
    b751's form over b751's objects: the corrigendum's foot and v1.30.0's controls; the sitting record's foot; the cQ bank's foot; the line
    bank's foot; the rules bank's rows; the citation check; the reproduction run; the address scan; each by its own lines through _bfig,
    which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1300.txt' % ACT, r'\*\*v1\.30\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.30.0`s controls')
    si_ = _bfig('%s_sitting.txt' % ACT, r'\*\*THE SITTING: DECIDED (\d+) ; PASSED (\d+) ; KEPT (\d+) ; STRUCK (\d+) ; GIT WRITES (\d+) AND THE AGENDA ; '
                r'SCAN 0 ; 0 ; 0 ; 0 AT EVERY COMMIT ; THE AUTHOR`S WORDS (\d+), VERBATIM\.\*\*', 'the sitting`s foot')
    cq_ = _bfig('%s_cq_sign.txt' % ACT, r'\*\*cQ\(n\), n = 2\.\.(\d+), FROM THE RECURSION AT v0\.38: NEGATIVE (\d+) ; THE SMALLEST NEGATIVE n = (\d+), cQ = (-?[\d.]+) ; '
                r'WITHIN 1e-40 OF ZERO (\d+) \(EXACTLY ZERO (\d+)\), COUNTED NEITHER WAY ; NONNEGATIVE (\d+) ; THE LARGEST \|cQ\| ([\d.]+) AT n = (\d+) ; '
                r'CONTROLS \(K1\)-\(K4\) (ALL AS WANTED) ;', 'the cQ bank`s foot')
    ln_ = _bfig('%s_line.txt' % ACT, r'\*\*THE LINE: (COMPOSED) ; FROM REGISTRY 1\.5c-21 TO 1\.5c-23 AND SPIRAL_MAP AFTER THE SITTING ; KEYSTONE (\S+) ; STAGE (\w+) ; '
                r'THE EARLIER LINES READ AGAIN (\d+), NONE REWRITTEN ; THE CARRIED ITEMS LANDED (\d+) ; (ALL AS READ)\.\*\*', 'the line bank`s foot')
    reps_ = [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', rdn('%s_rules.txt' % ACT))]   # ### the rules bank's rows
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b751: no order entered this act ((R361) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], rules_rows=reps_,
                repairs=len([c_ for c_ in v5[0].split(', ') if c_.strip('()') not in ('answers', 'version')]),   # ### the repairs beside the one the title names (the answers route), the version not a repair
                si_decided=int(si_[0]), si_passed=int(si_[1]), si_kept=int(si_[2]), si_struck=int(si_[3]), si_writes=int(si_[4]), si_words=int(si_[5]),
                cq_n=int(cq_[0]), cq_neg=int(cq_[1]), cq_nmin=int(cq_[2]), cq_vmin=cq_[3], cq_band=int(cq_[4]), cq_zero=int(cq_[5]),
                cq_nonneg=int(cq_[6]), cq_max=cq_[7], cq_nmax=int(cq_[8]), cq_ok=(cq_[9] == 'ALL AS WANTED'),
                ln_keystone=ln_[1], ln_stage=ln_[2], ln_earlier=int(ln_[3]), ln_landed=int(ln_[4]), ln_ok=(ln_[5] == 'ALL AS READ'),
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R361)(3): the kernel rows of one kind as banked (data/b751_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R361): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b751_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b751_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b751's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b751_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b751_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b751_standing_v1300.txt', '## THE CONTROLS', '### ### **v1.30.0: CONTROLS '),
               ('data/b751_cq_sign.txt', '## (K4) rQ: THE ENUMERATION AGAINST THE LEAN BOX', '## THE FIGURE: cQ(n), n = 1..3000'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, the sitting: in the sitting record every item's CURRENT read at HEAD and compared to the agenda before its draft was written,
# ### the eleven rows each carrying both fields (the record's own words, data/b751_sitting.txt)
N2_SECTIONS = ()
N2_SIT_FIELDS = ('  CURRENT READ: ', '  COMPARED TO THE AGENDA: EQUAL')
N2_FIGURE_NEEDLES = ('b751_cq_sign', '7.742402', 'NEGATIVE 102')   # ### [E]'s figure: no other item's diff carries it


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R361): the agenda's drafts banked before any item is put; [E]'s generator committed before it ran (the bank in a later commit, not
    in the generator's) and its controls printed before its figure; no item but [E]'s row citing [E]'s figure; each item's CURRENT read at
    HEAD and compared to the agenda (the sitting record's eleven rows); each passed item one PLACE-papers write touching its one file; each
    tool's controls before its figures; the standing version before the gate; the (W) regeneration, the pre-lock comparison and the
    probe-path refusal before the lock gate. Step zero, v1.30.0, the weight and corrigendum, the corrigendum banks, the agenda, the items
    in their order with [E]'s generator and bank before its row, the sitting record and the line bank in that order by time; v1.30.0 an
    ancestor of the sitting record, and that of HEAD."""
    it_ = list(K.ITEM_PP)
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.AGENDA_COMMIT)] \
        + [(PP, x[1]) for x in it_[:5]] + [(ROOT, K.CQ_GEN[0]), (ROOT, K.CQ_BANK[0])] + [(PP, x[1]) for x in it_[5:]] \
        + [(ROOT, K.SITTING_COMMIT), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.SITTING_COMMIT], capture_output=True).returncode == 0 \
        and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.SITTING_COMMIT, 'HEAD'], capture_output=True).returncode == 0
    dfiles_ = [sorted(x for x in g(PP, 'show', '--name-only', '--format=', x_[1]).split() if x.strip()) for x_ in it_]
    disch_ = dfiles_ == [[x_[2]] for x_ in it_] and sorted(x for x in g(PP, 'show', '--name-only', '--format=', K.C1_PP).split() if x.strip()) == ['FINDINGS.md']
    genf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.CQ_GEN[0]).split() if x.strip()]
    bankf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.CQ_BANK[0]).split() if x.strip()]
    gen_ = K.CQ_GEN[1] in genf_ and K.CQ_BANK[1] not in genf_ and K.CQ_BANK[1] in bankf_ and _first_add(K.CQ_BANK[1]) == g(ROOT, 'rev-parse', K.CQ_BANK[0]).strip()
    cites_ = [x_[0] for x_ in it_ if x_[0] != '[E]' and any(n_ in (g(PP, 'show', '--format=', '-U0', x_[1]) or '') for n_ in N2_FIGURE_NEEDLES)]
    sit_ = rdn('%s_sitting.txt' % ACT)
    agenda_first_ = bool(all(tm_)) and tm_[4] < min(tm_[5:10] + tm_[12:17])
    sect_ = all(sit_.count(f_) == len(K.SITTING_STATES) for f_ in N2_SIT_FIELDS) and gen_ and not cites_ and agenda_first_
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
        'the weight and corrigendum (PLACE-papers %s) FINDINGS alone and each passed item one PLACE-papers write touching its one file (%d writes): %s; the agenda (relay %s) before the first item: %s; [E]`s generator (relay %s) committed before its bank (relay %s), the bank not in the generator`s commit: %s; items citing [E]`s figure beside [E]`s own row: %s; the sitting record`s rows each with CURRENT read and compared EQUAL: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.30.0, the weight and corrigendum, the corrigendum banks, the agenda, the items with [E]`s generator and bank before its row, the sitting record and the line bank in that order by time: %s (%s), v1.30.0 an ancestor of the sitting record and that of HEAD: %s; the tools` controls before their figures: %s' % (
            K.C1_PP[:8], len(it_), disch_, K.AGENDA_COMMIT, agenda_first_, K.CQ_GEN[0], K.CQ_BANK[0], gen_, ', '.join(cites_) or 'none',
            all(sit_.count(f_) == len(K.SITTING_STATES) for f_ in N2_SIT_FIELDS), regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b751's objects; b750's in git at b750's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b751_standing_v1300.txt', ('ALL AS WANTED',)), ('b751_sitting.txt', ('THE SITTING: DECIDED 11', 'STRUCK 0')),
             ('b751_cq_sign.txt', ('NEGATIVE 102', 'ALL AS WANTED')),
             ('b751_line.txt', ('THE LINE: COMPOSED', 'ALL AS READ')),
             ('b751_corrigendum.txt', ('ITEMS',)), ('b751_citation_check.txt', ('THE CHECK CLEAN',)), ('b751_reproduce.txt', ('REPRODUCES',)), ('b751_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### the entry's last line, the INTEGRATION line, in canon XXIII (A)'s form, read from REGISTRY and SPIRAL_MAP after the sitting through
# ### relaypath (relay data/b751_line.txt :9): the Epstein instance, its keystone THE_EPSTEIN_CONTROL_OBJECT, CLUSTERED, the cQ figure
# ### carried by neither file the cluster row names
INTEGRATION_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
                    'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')
FIXED_SENTENCES = ()   # ### b751: no fixed sentence ordered by (R361)


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
    """N3 (R361): no sentence says anything was deposited, published or versioned; the dated note on d1-1 says discarded, unchanged and a
    fresh draft on the rubric's word, and no more (its further sentences printed, each one a fault); the entry's INTEGRATION line its last
    line, reading REGISTRY's row d1-1 and SPIRAL_MAP's keystone row as they stand; no sentence calling the work the earliest of its kind in
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
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b751: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    # ### N3 over the sitting's writes, each read where it landed: README's Current sentence ([B2]), [F2]'s note, I-109's row ([E]), the
    # ### 1.5c-21 note ([C]); each saying what its statements say and no more
    _rl = lambda p_: (rd(os.path.join(PP, *p_.split('/'))) or '').replace(chr(13), '').split(NL)
    rm_ = _rl('README.md')
    ci_ = [n_ for n_, l_ in enumerate(rm_) if l_.strip() == '#### Current']
    cur_ = next((l_ for l_ in rm_[ci_[0] + 1:ci_[0] + 4] if l_.strip()), '') if len(ci_) == 1 else ''
    f2_ = next((l_ for l_ in _rl('day1/Which_Structure_Confines_v2_4_0.md') if l_.startswith("*(Appended under the author's ruling `(R361)`(2)[F2]")), '')
    ir_ = next((l_ for l_ in _rl('phase1.5/method/INSTRUMENTS.md') if l_.startswith('**Reads.**') and 'b751_cq_sign' in l_), '')
    cn_ = [l_ for l_ in _rl('REGISTRY.md') if l_.startswith('*Dated note, b751,')]
    n_ = cn_[0] if len(cn_) == 1 else ''
    unmoved_ = 'RH and h2 stand where they stood'
    said_ = bool(cur_) and cur_.rstrip().endswith(unmoved_ + '.') and bool(f2_) and f2_.rstrip().endswith(unmoved_ + '.') \
        and bool(ir_) and 'nothing about Z_Q’s zeros' in ir_ and bool(n_) and 'The cell is unedited' in n_
    lit_ = [x for x in re.split(r'(?<=[.;])\s+', cur_) if re.search(r'\b(?:literature|known|novel|new result|first|earliest|previously)\b', x, re.I)]
    meant_ = [x for x in re.split(r'(?<=[.;])\s+', ir_) if re.search(r'\b(?:suggests?|implies|evidence|means|meaning|consistent with|supports?|indicates?)\b', x, re.I)]
    more_ = lit_ + meant_   # ### N3: the Current sentence carries no literature claim; [E]'s row says what was computed and nothing of what it means
    nsents_ = [x for t_ in (cur_, f2_, ir_, n_) for x in re.split(r'(?<=[.;])\s+', t_.strip('*')) if x.strip()]
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
    nouns_ = [w_ for w_ in ('XXIII', 'criterion (9)', 'I-109', 'E-2026-11-09-1', 'E-2026-11-09-2', '1.5c-21', 'd1-1', 'THE_EPSTEIN_CONTROL_OBJECT',
                            'Which_Structure_Confines', 'data/%s_sitting.txt' % ACT, 'data/%s_cq_sign.txt' % ACT, 'data/%s_line.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and said_ and not more_ and not dep_ and not first_ and not loc_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the sitting`s writes read where they landed -- README`s Current sentence and [F2]`s note closing "RH and h2 stand where they stood", I-109`s row saying nothing about Z_Q`s zeros, the 1.5c-21 note leaving its cell unedited: %s; a literature claim in the Current sentence or a sentence of I-109 saying what the figure means: %s; a sentence of those writes or the entry saying a thing was deposited, published or versioned outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY 1.5c-21 and SPIRAL_MAP`s Epstein row read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), said_, more_ or 'NONE', dep_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R361) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R361)(5))
# ### (R361)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R361)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
    # ### same reader the ceiling takes; the face's `locked at (UTC)` line no longer dates it
    import lockdate as LD
    lc = LD.lock_of(ACT, os.path.join(ROOT, 'data'))
    lock = LD.lock_epoch(lc, ROOT) if lc else None
    # ### v1.30.0, (R361)(3)(viii), b750 events (12): the lock's time printed from the one reader's epoch; b750's module left lock_iso unset and
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
    # ### (R361) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b750's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b751, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b750's face
# ### read them; (R361)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
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
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R361)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R361)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b750 left them; the address scan's count from its bank (relay data/b751_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R361)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R361)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R361)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    # ### v1.30.0, (R361)(3)(vi), b750 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R361)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and not zdel_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b751_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    f_ = _figs()
    return ('### b751 — lane two, act one hundred and seventy-seven, the synthesis sitting under (R361): b750 at its weight and its corrigendum; '
            'v1.30.0; the sitting, %d of %d items passed; cQ(n) over n ≤ %d, %d negative; the integration line' % (
                f_['si_passed'], f_['si_decided'], f_['cq_n'], f_['cq_neg']))
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects in the ferry's C4 form ("the synthesis sitting: <p> of <n> items passed; the stages in the canon as
    XXIII and criterion (9); the front door at v0.38; 1.5c-21's grade note; d1-1 <kept | noted>; cQ(n) over n ≤ 3000: <none negative | k
    negative, the smallest n = m>; the Epstein cluster seated, THE_EPSTEIN_CONTROL_OBJECT its keystone in progress, Which_Structure_Confines
    noted; two errata; the append-route for answers and <r> repairs landed"); every figure from the banks (the sitting's foot and its [D]
    row, the cQ bank's foot, v1.30.0's controls less (answers) and (version))."""
#⟪END⟫
#⟪SECTION record 31⟫
    ctl_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if 'answers' not in ctl_:
        sys.exit('### v1.30.0`S CONTROLS DO NOT NAME (answers) -- NOTHING COMPOSED')
    if f['rules_rows'] != list(range(1, len(f['rules_rows']) + 1)) or len(f['rules_rows']) < 3:
        sys.exit('### THE RULES BANK`S ROWS ARE NOT (1)-(n) IN ORDER -- NOTHING COMPOSED')
    if not (f['cq_ok'] and f['ln_ok']) or f['si_decided'] != len(K.SITTING_STATES):
        sys.exit('### THE cQ BANK, THE LINE BANK OR THE SITTING`S COUNT NOT AS READ -- NOTHING COMPOSED')
    rows_ = _sitting_rows_r(rdn('%s_sitting.txt' % ACT))
    d_ = (rows_.get('D') or {}).get('state', '')
    dword_ = 'kept' if d_.startswith('KEEP') else ('noted' if d_.startswith('PASS') else None)
    if dword_ is None:
        sys.exit('### THE SITTING`S [D] ROW READS NEITHER KEEP NOR PASS -- NOTHING COMPOSED')
    cqw_ = ('none negative' if f['cq_neg'] == 0 else '%d negative, the smallest n = %d' % (f['cq_neg'], f['cq_nmin']))
    return ('## The synthesis sitting: %d of %d items passed; the stages in the canon as XXIII and criterion (9); the front door at v0.38; '
            '1.5c-21’s grade note; d1-1 %s; cQ(n) over n ≤ %d: %s; the Epstein cluster seated, THE_EPSTEIN_CONTROL_OBJECT its keystone in '
            'progress, Which_Structure_Confines noted; two errata; the append-route for answers and %d repairs landed' % (
                f['si_passed'], f['si_decided'], dword_, f['cq_n'], cqw_, f['repairs']))


def _sitting_rows_r(t):
    """the sitting record's rows by label ([A1], [D], ...): {label: {'state': the words after the label}}; pure in its argument."""
    out = {}
    for l in (t or '').split(NL):
        m = re.match(r'^\[([A-Z]\d*)\] (.+)$', l)
        if m:
            out[m.group(1)] = dict(state=m.group(2).strip())
    return out
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the thirteen rules of relay data/b751_rules.txt, the seat`s reading of (R361)(3), each for the author`s strike; (2) the line bank`s reading of b745-b748`s INTEGRATION lines as SYNTHESISED by the cluster, through the [F2] note in Which_Structure_Confines_v2_4_0.md, each entry`s own finding not matched by needle (relay data/b751_line.txt (C), its limit printed there), for the author`s keep or strike, no FINDINGS line rewritten; (3) [D] kept at the sitting: REGISTRY :1246, b750`s d1-1 note, stands with its further words as b750 wrote them; '
            +
            '(4) %s and the seat’s %s defect%s as lettered' % (
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b751: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R361)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b751's objects; b750's composer in git at
    b750's record tool). Its last line the INTEGRATION line ((R361)(4))."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R361)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R360)(2)(v)
    rg_ = (rd(os.path.join(PP, 'REGISTRY.md')) or '').replace(chr(13), '').split(NL)
    dn_ = [i_ + 1 for i_, l_ in enumerate(rg_) if l_.startswith('*Dated note, b751,')]
    r21_ = [i_ + 1 for i_, l_ in enumerate(rg_) if l_.startswith('| 1.5c-21 |')]
    ins_ = (rd(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')) or '').replace(chr(13), '').split(NL)
    i109_ = [i_ + 1 for i_, l_ in enumerate(ins_) if l_.startswith('## I-109 ')]
    if len(dn_) != 1 or len(r21_) != 1 or len(i109_) != 1:
        sys.exit('### THE LINES THE ENTRY CITES DO NOT READ AS EXPECTED (the dated note %s, the 1.5c-21 row %s, I-109 %s) -- NOTHING COMPOSED' % (dn_, r21_, i109_))
    ip_ = dict((x_[0], x_[1]) for x_ in K.ITEM_PP)
    e = ['', _title(), '',
         'The synthesis sitting decided %d items: %d passed, %d kept, %d struck, in %d git writes after its agenda (relay %s), each item read at HEAD and compared to the agenda before its draft was written (relay data/b751_sitting.txt). cQ(n) for 2 ≤ n ≤ %d, from the recursion at SIDE-explicit-formula v0.38, is negative at %d n, the smallest n = %d with cQ = %s, exactly zero at %d n and nonnegative at %d n, its four controls as wanted (relay data/b751_cq_sign.txt; INSTRUMENTS I-109, :%d).' % (
             f['si_decided'], f['si_passed'], f['si_kept'], f['si_struck'], f['si_writes'], K.AGENDA_COMMIT, f['cq_n'], f['cq_neg'], f['cq_nmin'], f['cq_vmin'],
             f['cq_zero'], f['cq_nonneg'], i109_[0]), '',
         '*Filed at b751 on the author’s ruling `(R361)`; %d question%s put before the root. Banks: relay '
         '`data/b751_corrigendum.txt`, `data/b751_standing_v1300.txt`, `data/b751_rules.txt`, `data/b751_sitting_agenda.txt`, `data/b751_sitting.txt`, `data/b751_author_answers.txt`, `data/b751_cq_sign.txt`, `data/b751_line.txt`, `data/b751_prelock.txt`, `data/b751_pathrefusal.txt`, '
         '`data/b751_reproduce.txt`, `data/b751_address_scan.txt`, `data/b751_touch.txt`, `data/b751_standing_figures.txt`, `data/b751_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R361)(1), (3); %s, %s, %s): b750 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b750’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b751_corrigendum.txt); tools/standing/ at %s by a commit of its own, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b751_standing_v1300.txt): the answers route appending and refusing to rewrite a line already in its bank, the hook’s row (65) and the design list, a halt question naming every score its routes would cost, the author’s words composed at the close, the closing dry reading the design banks, N5 on the Zenodo banks alone, the question count, the lock print, the permission rule, the carry refusing unnamed rows, the retries rule, the delete reader; the rules, %d rows, in relay data/b751_rules.txt.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], len(f['rules_rows'])), '',
         '**The sitting** ((R361)(2), N2, N3): the agenda banked at relay %s with every draft before the first item was put; each item put in b736’s form, its CURRENT read at HEAD, passed or kept by the author’s number, one PLACE-papers write per passed item, the scan over the staged set at every commit. [A1] the integration line and its stages as THE_METHOD_CANON section XXIII (PLACE-papers %s); [A2] criterion (9), synthesis before deposit (%s); [B1] README’s deposit note (:164 at its write, :170 after [B2]’s lines) gains the v0.38 kernel line (%s); [B2] README’s claim section gains Current, one sentence closing on the author’s clause “and RH and h2 stand where they stood”, the earlier sentences under History (%s); [C] a dated note to REGISTRY row 1.5c-21 (:%d), the note at :%d, the cell unedited (%s); [D] kept, no write: REGISTRY :1246, b750’s d1-1 note, stands as written; [E] the generator committed before its run (relay %s), its bank (relay %s), INSTRUMENTS I-109 (%s); [F1] SPIRAL_MAP’s cluster table gains the Epstein instance, its keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 in progress, its sibling anchor Which_Structure_Confines_v2_4_0 (%s); [F2] a dated note in Which_Structure_Confines_v2_4_0 after :95 with the author’s two clauses (%s); [G1] ERRATA E-2026-11-09-1 (%s); [G2] ERRATA E-2026-11-09-2 (%s). The author’s words on [B2], [E], [F1] and [F2], %d, banked verbatim with their times by the appending route (relay data/b751_author_answers.txt); the record at relay %s (relay data/b751_sitting.txt).' % (
             K.AGENDA_COMMIT, ip_['[A1]'], ip_['[A2]'], ip_['[B1]'], ip_['[B2]'], r21_[0], dn_[0], ip_['[C]'], K.CQ_GEN[0], K.CQ_BANK[0], ip_['[E]'], ip_['[F1]'], ip_['[F2]'],
             ip_['[G1]'], ip_['[G2]'], f['si_words'], K.SITTING_COMMIT), '',
         '**The sign of cQ(n)** ((R361)(2)[E], the author’s word at b750’s root): tools/b751_cq_sign.py, its md5 %s at relay %s, run after that commit; its controls first -- (K1) r ≡ 1 returning Λ(n), (K2) ζ_K’s coefficients, (K3) the Dirichlet-inverse route, (K4) rQ against the Lean box -- all as wanted; then the figure over 2 ≤ n ≤ %d: negative %d, the smallest n = %d, cQ = %s; within 1e-40 of zero %d, all exactly zero, counted neither way by the author’s clause; nonnegative %d; the largest |cQ| %s at n = %d (relay data/b751_cq_sign.txt). INSTRUMENTS I-109 enters what was computed, its range n ≤ %d and nothing about Z_Q’s zeros; no other item cites the figure.' % (
             K.CQ_GEN[2], K.CQ_GEN[0], f['cq_n'], f['cq_neg'], f['cq_nmin'], f['cq_vmin'], f['cq_band'], f['cq_nonneg'], f['cq_max'], f['cq_nmax'], f['cq_n']), '',
         '**The integration line** ((R361)(4)): this entry’s line read by tools/b751_line.py from REGISTRY and SPIRAL_MAP after the sitting’s writes: the cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23, the cluster row seated at [F1]), the keystone %s, stage %s, the figure carried by neither file the cluster row names (relay data/b751_line.txt); the earlier entries’ lines read again by the same stages, %d of them, none rewritten, and the carried items landed, %d.' % (
             f['ln_keystone'], f['ln_stage'], f['ln_earlier'], f['ln_landed']), '',
         '**The order of the act** (N2): %s at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the agenda at relay %s; the items at PLACE-papers %s, with [E]’s generator at relay %s and its bank at relay %s before its row; the sitting record at relay %s; the line bank at relay %s; the per-commit scan to its own bank at every commit; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b751_prelock.txt, data/b751_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             f['ver'], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.AGENDA_COMMIT, ', '.join(x_[1] for x_ in K.ITEM_PP), K.CQ_GEN[0], K.CQ_BANK[0], K.SITTING_COMMIT, K.C3_RELAY[0][:8]), '',
         '**What this act is not**: nothing deposits; no new version; no draft published; no Zenodo call; no kernel’s main touched, no branch merged, no tag beyond v0.38, no Lean file written; the doors and records edited are those of the sitting’s passed items alone.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b751_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b751_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b751_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b751 -- %s, %s, %s, %s -- against b750’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b751_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the sitting and the figure read one way: the sitting placed the clustered findings of b738-b750 in the canon’s stages, the front door and a file the Epstein cluster names, each by the author’s number; the figure entered as an instrument row that says what was computed, and the act’s own line stays CLUSTERED because no file the cluster names carries it.', '',
         '**Carried to:** %s, per (R361): the root’s question, the act after this one, put once and answered in relay data/b751_author_answers.txt; the line bank’s reading of b745-b748’s lines for the author’s keep or strike; the thirteen rules for the author’s strike; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b750():
    """b750's form over b750's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b751's objects; b750's composer in git at b750's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the sitting; the sign of cQ(n); the line."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R361)(3)(vii): the composed prompts' rows, the sitting rows read apart
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R361) ratified.** Its components as the ferry orders them (relay data/b751_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b750’s weight), :%s (the corrigendum), :%s (the entry); the sitting’s ten passed items, one PLACE-papers write each (%s); no order entered; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), ', '.join(x_[1] for x_ in K.ITEM_PP)), '',
             '**The sitting:** %d items decided, %d passed, %d kept ([D], no write), %d struck; the agenda at relay %s before the first item; the record at relay %s; the author’s words %d, verbatim (relay data/b751_sitting_agenda.txt, data/b751_sitting.txt, data/b751_author_answers.txt).' % (
                 f['si_decided'], f['si_passed'], f['si_kept'], f['si_struck'], K.AGENDA_COMMIT, K.SITTING_COMMIT, f['si_words']), '',
             '**The sign of cQ(n):** over 2 ≤ n ≤ %d, negative %d, the smallest n = %d (cQ = %s), exactly zero %d, nonnegative %d; the generator at relay %s before its run, the bank at relay %s; INSTRUMENTS I-109 (relay data/b751_cq_sign.txt).' % (
                 f['cq_n'], f['cq_neg'], f['cq_nmin'], f['cq_vmin'], f['cq_zero'], f['cq_nonneg'], K.CQ_GEN[0], K.CQ_BANK[0]), '',
             '**The integration line:** b751’s at the foot of its entry, cluster the Epstein instance, keystone %s, stage %s (relay data/b751_line.txt); the earlier lines read again %d, none rewritten.' % (
                 f['ln_keystone'], f['ln_stage'], f['ln_earlier']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b751_standing_v1300.txt); the line bank`s reading of b745-b748`s lines for the author`s keep or strike.' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b751_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b751_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b751_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b751 `%s` (previous `%s`, b750’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b751_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b751_standing_v1300.txt); the standing '
             'report tool (relay data/b751_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b750 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b751_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b750’s %s, %s, %s, %s (relay data/b751_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b751_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b750():
    """b750's trail record over b750's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b750 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b750`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none; no kernel`s main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b750-closing, push-b750-preroot, push-b750-record; PLACE-papers push-b750-preroot, push-b750-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b751_stepzero.txt :44-:48).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: one dated note appended at the foot to row 1.5c-21 ([C], PLACE-papers 510eeea9), no row added.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R361)(3): FINDINGS :14538.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R361)(3): row (70).'),
    ('ERRATA entries filed', 2, 2, 'entries', '### (R361)(2)[G1], [G2]: E-2026-11-09-1 and E-2026-11-09-2, each on the author`s pass, one write each (PLACE-papers 00188c31, 2d145638).'),
    ('sitting items decided', 11, 11, 'items', '### (R361)(2): [A1]-[G2], ten passed, [D] kept, none struck (relay data/b751_sitting.txt).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R361) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b751_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.30.0`s controls, the sign of cQ(n), the line, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none this act: no registered object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R361)(6)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R361)(3): tools/standing/ to v1.30.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b751_address_scan.txt (the address never printed).'),
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
    # ### b751: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b751_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b751_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1300', 'cq_sign', 'line', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b751_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b751_registration_%s.txt -- b751, THE SYNTHESIS SITTING: b750 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.30.0; "
                             "THE SITTING, ELEVEN ITEMS; THE SIGN OF cQ(n) OVER n <= 3000 AS I-109; THE INTEGRATION LINE; NO DEPOSIT, NO LEAN, UNDER (R361)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b750's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b751: b750's lines read banks this
act does not write, and are not carried; the lines are b751's: tools/standing/ v1.30.0 by its controls (CERTIFIED), the sitting, the sign
of cQ(n) and the INTEGRATION line by their banks (REGISTERED), and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b751's lines, each from the record tool's figures over b751's banks
    # ------------------------------------------------------------------ REGISTERED: (R361)(2), the sitting, read from its record
    sz = seat('%s_sitting.txt' % ACT, '**THE SITTING: DECIDED ')
    sk = sz   # ### (R360)(2)(ii): the name the template appends
    keys['SITTING'] = ('REGISTERED -- THE SITTING: %d items decided, %d passed, %d kept, %d struck; %d git writes after the agenda (relay %s); the author`s words %d, verbatim; the record at relay %s. SOURCE %s.' % (
        f['si_decided'], f['si_passed'], f['si_kept'], f['si_struck'], f['si_writes'], K.AGENDA_COMMIT, f['si_words'], K.SITTING_COMMIT, sz['text']))
    snz = seat('%s_cq_sign.txt' % ACT, '**cQ(n), n = 2..')
    keys['CQ'] = ('REGISTERED -- THE SIGN OF cQ(n) over 2 <= n <= %d: negative %d, the smallest n = %d (cQ = %s); exactly zero %d; nonnegative %d; controls (K1)-(K4) %s; the generator at relay %s before its run; INSTRUMENTS I-109. SOURCE %s.' % (
        f['cq_n'], f['cq_neg'], f['cq_nmin'], f['cq_vmin'], f['cq_zero'], f['cq_nonneg'], 'ALL AS WANTED' if f['cq_ok'] else 'NOT ALL AS WANTED', K.CQ_GEN[0], snz['text']))
    seats.append(snz)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.30.0 ((R361)(3)), by its controls
    sw = seat('%s_standing_v1300.txt' % ACT, '**v1.30.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1300'] = ('CERTIFIED -- tools/standing/ v1.30.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the INTEGRATION line ((R361)(4))
    so = seat('%s_line.txt' % ACT, '**THE LINE: ')
    keys['LINE'] = ('REGISTERED -- THE INTEGRATION LINE from REGISTRY and SPIRAL_MAP after the sitting: cluster the Epstein instance, keystone %s, stage %s; the earlier lines read again %d, none rewritten; the carried items landed %d. SOURCE %s.' % (
        f['ln_keystone'], f['ln_stage'], f['ln_earlier'], f['ln_landed'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R361)(6))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1300']), ('REGISTERED', ['SITTING', 'CQ', 'LINE']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b751 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
