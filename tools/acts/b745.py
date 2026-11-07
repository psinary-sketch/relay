# -*- coding: utf-8 -*-
# b745 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R355)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R355)(2) repair it carries. Edited by the Edit tool. Carried at b745 by tools/b745_fold.py (`carry`) from tools/acts/b744.py,
# b744`s names substituted; the citation`s sections adopted from tools/b745_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b744`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b744`s carried till
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
# ### b745, Component 1 (the Edit tool): THE c1 ROUTE FOR b744'S WEIGHT LINE AND ITS CORRIGENDUM, (R355)(1) and (2). Rewritten at b745 against
# ### b744's own banks (scratch splicec1_744.py): the closing's lines by needle, the events (15), the defects (23), the refusals (17 lines), the
# ### discharge and the sitting's foot, the v1.23.0 and v1.23.1 controls, and the v1.24.0 controls this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '7d448774'          # ### b744's closing push tip (its step row 21), the public relay's main
C1_CLOSING_COMMIT = 'd75dffb7'      # ### b744's closing commit (its closing row)
C1_REFUSAL_AT = '7d448774'          # ### its refusal bank read at its closing push tip
C1_NOTED = '2026-11-07'
C1_CORRIGENDA_LAST = 64
C1_V170 = 'b745_standing_v1250.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.25.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-07 by b745 to b744’s entry (:%d), under `(R355)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL planned'
C1_TRAIL_NEEDLE = '### b744 — lane two, act one hundred and seventy-one,'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


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
    for l in _c1_rd('b744_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b744_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b744_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b744_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b744_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b744_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b744_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b744_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8 or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b744_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) REFUTED \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the record-time scores')
    ar = json.load(open(os.path.join(D, 'b744_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b744_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    _zb, l_zb = _c1_fl(c, r'^    (W-ORD-ZETA-BOX): zeta_box at t₁ = 12, t₂ = 16', 'the ζ box plan`s row')
    _pc, l_pc = _c1_fl(c, r'^    (W-ORD-POSITIVE-CONTROL): pcConfig', 'the positive control plan`s row')
    (zl,), l_zl = _c1_fl('b744_zetabox_plan.txt', r'(450-1,100) LINES?.*6 DISPATCHES NOMINAL, 12 AT MOST', 'the ζ box price')
    (pl,), l_pl = _c1_fl('b744_poscontrol_plan.txt', r'^.*?(108-290) lines.*1 dispatch nominal', 'the positive control price')
    (va, vb), l_v = _c1_fl('b744_standing_v1240.txt', r'^### ### \*\*v1\.24\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*$', 'the v1.24.0 foot')
    _mv, l_mv = _c1_fl('b744_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-06-b744)\.zip ; ', 'the mirror`s archive')
    _aw1, l_aw1 = _c1_fl('b744_author_answers.txt', r'^RESULT .*="(Both, positive first \(Recommended\))"', 'the author`s first answer')
    _aw2, l_aw2 = _c1_fl('b744_author_answers.txt', r'^RESULT .*="(the answer is yes — a tag on zq-b730 at 14ca5725, no merge, cut at b745’s step zero\.)"', 'the author`s second answer')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R354\)\(6\)\*\*: (per \(R354\)\(6\), named by the author at the root)\.', 'the carried item (a)')
    am = json.load(open(os.path.join(D, 'b744_amendments.json'), encoding='utf-8'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 7)) or len(dr) != 17 or (int(sd), int(se)) != (17, 6):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b744 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b744_closing.txt):* “%s” (data/b744_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b744_steps.json, the record and closing rows). As its rows read: %s planned, no build, %s lines, 6 dispatches nominal and 12 at most '
            '(:%d; data/b744_zetabox_plan.txt :%d); %s planned, no build, %s lines, 1 dispatch nominal (:%d; data/b744_poscontrol_plan.txt :%d); the author’s amendment to `(R354)`(4) carried out, '
            'REGISTRY’s Epstein rows renumbered 1.5c-21, -22, -23 (PLACE-papers 0d51a02; relay data/b744_amendments.json, %d row). Standing tools v1.24.0, %s of %s (data/b744_standing_v1240.txt :%d); '
            'the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), G-AXIOM-CLAIM and G-RULE-POSTSEAL-READ declared on the face, G-RUNNER-GATE VACUOUS; '
            'the record-time scores N3 REFUTED, the rest HELD (:%d), and at the scores’ close SCORES %d OF 8 HELD (data/b744_scores_close.json). '
            'The root %s over %s banks, chained from %s (data/b744_act_root.json; :%d); the mirror %s at %s (data/b744_mirror_verify.txt :%d; :%d); %s prompts banked as put by the seat (:%d), '
            'the author’s answers at the root “%s” (data/b744_author_answers.txt :%d) and “%s” (:%d); the closing’s carried item (a): %s (:%d), the author naming this act by `(R355)`. '
            '%d events in data/b744_events.txt, rows (1)-(%d), entered after the lock; %d defects, (a)–(q) (data/b744_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and '
            'defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. The draft at v5 (data/b744_report.txt :10, (4) HELD); nothing deposited, no merge, no tag at b744, no new Zenodo version; the corrigendum '
            'for these rows follows, under `(R355)`(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, _zb[0], zl, l_zb, l_zl, _pc[0], pl, l_pc, l_pl, len(am if isinstance(am, list) else am.get('rows') or [am]),
                vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, l_sl, len(held),
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, _aw1[0], l_aw1, _aw2[0], l_aw2, ca, l_ca, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b744's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '19:35:11Z', 'defect (c)'), (2, 'READ', '19:37:51Z', 'defect (c)'), (3, 'PIPE', '20:07:36Z', 'defect (c)'), (4, 'PIPE', '20:40:07Z', 'defect (f)'),
               (5, 'PIPE', '20:51:53Z', 'defect (f)'), (6, 'PIPE', '23:11:25Z', 'defect (j)'), (7, 'READ', '23:11:35Z', 'defect (j)'), (8, 'REDIR', '23:11:55Z', 'defect (j)'),
               (9, 'READ', '23:12:11Z', 'defect (j)'), (10, 'READ', '23:14:31Z', 'defect (j)'), (11, 'SED', '23:48:29Z', 'defect (j)'), (12, 'PIPE', '23:49:13Z', 'defect (j)'),
               (13, 'PIPE', '03:17:12Z', 'event (1)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing refusal of b744's: b745's hook bank opens at 14:47:57Z, every line b745's own
C1_FLIP = {}      # ### (R355)(2) flips no tag: each item read as its bank tags it
C1_CORR_TITLE = ('## Corrigendum to b744’s record (relay data/b744_events.txt rows (1)-(6) and data/b744_defects.txt): six events and seventeen defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the row’s ID, the hold at the root and every record route, standing-b3 after its chain parts, the exempt set and every commit’s row or exemption, the step-row subject, '
                 'at tools/standing/ v1.25.0, each controlled, under (R355)(2)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.25.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b744_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b744_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.25.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(6)', sorted(ev) == list(range(1, 7))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 17', len(dr) == 17), ('the refusals 13, each answered as listed', len(rl) == 13 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.25.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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
    """the counter as this corrigendum reads the items: no tag flipped ((R355)(2) names none)."""
    nc, nl_, rep, n = _c1_counts(s)
    flip = sum(1 for k_ in C1_FLIP if s['tags'][k_][1] == 'NEW')
    return nc, nl_, rep + flip, n


def _c1_owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v_, k_.lower().replace("'s", '’s').replace("'", '’')) for k_, v_ in sorted(c.items(), key=lambda kv: -kv[1]))


def _c1_col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’').replace('`', '’')


# ### the repairs each item is met by at v1.25.0 (the rules bank data/b745_rules.txt)
C1_EV_EXTRA = {1: '; rule (6) of data/b745_rules.txt: the hook’s PIPE row held, REPEAT ((R355)(2)(vi))',
               2: '; repair (b3); rule (3) of data/b745_rules.txt: standing-b3 refuses itself while a chain part’s bank is absent',
               3: '; repair (hold); rule (2) of data/b745_rules.txt: the hold binds the root route and every record route, the route refusing itself and printing the figure',
               4: '; repair (exempt); rule (4) of data/b745_rules.txt: the post-lock scan bank in the exempt set, every commit printed with its row or its exemption',
               5: '; repair (subject); rule (5) of data/b745_rules.txt: the step-row subject composed from the rows the commit adds, a typed one refused by the hook',
               6: '; rule (6) of data/b745_rules.txt: the suite’s self-refusal working, REPEAT ((R355)(2)(vi))'}
C1_DF_EXTRA = {}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b745, to event (3) (`(R355)`(2)(ii)), tagged in its bank THE TOOLS’ [CLAIM ; NEW]: the free memory 2,360 MB read before `record root_arm`, beneath the hold 2,560 MB; '
            'the route ran, the record tool’s dispatch reading no hold before it; the root’s figures it computed stand as banked (data/b744_root_arm.json), the repair binding the route from v1.25.0.',
            'Dated note, b745, to the ID rule (`(R355)`(2)(i)): REGISTRY.md at PLACE-papers 5937961 holds seventeen IDs under two or three rows each (1.5a-5, 1.5a-6, 1.5a-7, 1.5a-8, 1.5b-6, 1.5c-16, '
            '1.5d-4, 1.5f-4, 1.5g-4, 1.5h-3, 1.5h-7, 1.5h-8, 1.5h-9, d1-1, p2-16, p2-27, p2-4; relay data/b745_standing_v1250.txt, the (rowid) block); they are older than the rule, stand as found, '
            'and are not this act’s to repair; the rule binds the rows a commit adds.')
C1_CLASSES = (
    ('rowid', 'the row’s ID (`(R355)`(2)(i), b743’s [B1]-[B3])', 'rule (1) of data/b745_rules.txt; tools/standing/rowid.py allocates from the file’s maximum over every table carrying the prefix and refuses an added row whose ID the base file holds; tools/standing/hook.py refuses such a PLACE-papers commit (kind ROWID). b743’s three rows refused against their parents and through the hook on a scratch clone; b744’s renumbered rows accepted; the next 1.5c ID before b743’s sitting 1.5c-21'),
    ('hold', 'the hold at the root and every record route (`(R355)`(2)(ii), event (3))', 'rule (2) of data/b745_rules.txt; the rendered record tool asks tools/standing/hold.py before any route. b744’s `record root_arm` at 2,360 MB refused; at 3,000 MB it runs; `record step` at 2,559 MB refused'),
    ('b3', 'standing-b3 after its four chain parts (`(R355)`(2)(iii), event (2))', 'rule (3) of data/b745_rules.txt; the checks tool’s part standing-b3 refuses itself while a half bank of its run is absent. b744’s sequence refused on four absent banks; with them present it runs'),
    ('exempt', 'the exempt set and every commit’s row or exemption (`(R355)`(2)(iv), event (4))', 'rule (4) of data/b745_rules.txt; tools/standing/repeat.py’s set takes the post-lock scan bank, row_or_exemption prints each commit. da9910f9 needing a row before, exempt after; b744’s relay commits printed, none NO ROW'),
    ('subject', 'the step-row subject (`(R355)`(2)(v), event (5))', 'rule (5) of data/b745_rules.txt; tools/standing/subjects.py composes the step-row subject from the rows the staged step bank adds, tools/standing/hook.py refuses another. f5ff3680’s subject faulted; regenerated as “b744 record: the step row for relay e4ab0a4b”'),
    ('repeat', 'the REPEAT instances (`(R355)`(2)(vi), events (1), (6))', 'rule (6) of data/b745_rules.txt; guards: the hook’s PIPE row, the suite’s self-refusal'),
    ('version', 'the version (`(R355)`(2)(vii))', 'rule (7) of data/b745_rules.txt; tools/standing/VERSION v1.25.0, landed by a commit of its own (%s) with its controls bank' % K.C1_STANDING),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b744’s events bank (relay data/b744_events.txt) carries six rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank seventeen lettered rows, (a)-(q), each tagged in its own bracket (%s); its refusal bank thirteen lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R355)`(2), at tools/standing/ v1.25.0, each with a control on b744’s or b743’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b744’s events (1)-(6):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b744_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b744’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b744_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b744’s refusals** (relay data/b744_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (six events, seventeen defects), as b744’s closing prints it (relay data/b744_closing.txt :5); '
          'no tag is read otherwise here; the CLAIM items %s.' % (nc, nl_, rep, n, n, ', '.join(claims) or 'none'), '',
          '*Filed at b745 on the author’s ruling `(R355)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b745.py) from '
          'b744’s events and defects banks read unedited, its refusal bank, and the v1.25.0 controls bank; banked as relay `data/b745_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b744’s record; no sealed tool, face, trail or root-named bank of b744 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    return (['b745 -- THE CORRIGENDUM FOR b744, (R355)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b744_events.txt rows (1)-(6), data/b744_defects.txt 17 rows, data/b744_hook_refusals.txt 13 '
             'lines at %s; data/%s (the v1.25.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 6, DEFECTS 17 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.25.0: THE ROW`S ID, THE HOLD AT THE ROOT AND EVERY RECORD ROUTE, '
               'b3 AFTER ITS CHAIN PARTS, THE EXEMPT SET AND EVERY COMMIT`S ROW OR EXEMPTION, THE STEP-ROW SUBJECT, THE REPEAT INSTANCES, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (
                   n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b744 at its weight after its entry, and the corrigendum for b744, landed through b698's guarded
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
        rc, rl_, rr, rn = _c1_read_counts(s)
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=nc, close=nl_, repeat=rep, items=n,
                                                   read_here=dict(claim=rc, close=rl_, repeat=rr, items=rn),
                                                   events=[dict(row=k_, owner=s['tags'][k_][2], tag=s['tags'][k_][0], column=s['tags'][k_][1]) for k_ in sorted(s['events'])],
                                                   entered=[], flipped=dict((str(k_), v_) for k_, v_ in C1_FLIP.items()),
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.25.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; AS READ HERE %d, %d, %d OF %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, rc, rl_, rr, rn, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b745, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b745, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b745's name.
# ### b745's own changes are marked "b745, Component 3". The runner overrides read the act's dispatch rows: (R355)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b745_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R354)(7), as b744 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R355)(3)(c), N1, b745: two print dispatches allowed, none sent; no row and no run; VACUOUS on the read of a run, the plant a planted row refused."""
    rows = S['drows'] or []
    return not rows and not K.EF_RUNS and K.MAX_DISPATCHES == 2
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b745: no dispatch, no row; the order VACUOUS
#⟪END⟫
# ### b745, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R355)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b744, naming tools/standing/hook.py, edited by v1.24.0 alone (the LOCKED scope, (R355)(2)(iii); its blob at c9396ad0 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b745, Component 3 (the Edit tool): b745's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### six push-b744-* refs deleted at step zero (relay three, PLACE-papers two, SIDE-explicit-formula push-b744-sitting by (R355)(2)(v)), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 6 and 'data/b745_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b745, Component 6 (the Edit tool): b745's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b744's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b745, Component 4 (the Edit tool): b744's overrides of checks 1516 and 1659 (hook.py edited by b744's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b745 as it stands
# ### b745, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b745_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b745, Component 4 (the Edit tool): b744's override of checks 1476-1482 (one ERRATA entry at b744's (R354)(5)) removed -- (R355)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b745 as it stands
# ### b745, Component 3 (the Edit tool): G-BRANCHES-DELETED over b745's three repositories (relay, PLACE-papers, SIDE-explicit-formula) and six
# ### refs; the step-zero bank writes "KEPT as banked:" (data/b745_stepzero.txt :33), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 3 and len(NAMED_PUSH) == 6 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b745, Component 4 (the Edit tool): G-RUNNER-READ's plant on b745's dispatch rows -- run 2's axiom lines carrying sorryAx (b744's
# ### plant read the lv rows' closure log, which b745 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b745, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b745, Component 6 (the Edit tool): the fold bank was b744's own route
# ### (tools/b744_fold.py); b745's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b745_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b744.py -> tools/acts/b745.py' in (rd('b745_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b745, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b745_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b745, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b745_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b745_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b745, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R355): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R355)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b745')
    return '### THE COUNTER ((R355) Component 5, the act`s events and defects together; relay data/b745_defects.txt, data/b745_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b744, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b745 (defect (d')): the order's
# ### state as b745 leaves it -- the carry from b744 said "as b744 left it ... not touched this act", where b745 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL, entered at b744, priced this act in their plan banks and not built; W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as b744 entered them;',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b745, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b744's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b745, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b744's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b745_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b745_registration_%s.txt' % __import__('b745_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b745, Component 4 (the Edit tool, before the face): b744's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b745, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b745's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b745, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R355)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b745 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b745: no dispatch route this act (N1)
#⟪END⟫
# ### b745, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b744's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b745 scorer reads; the needles set to the banks b745's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b745, (R355)(2)(iii): b744's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b745, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b745_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopq')))   # ### (a)-(q), entered before the lock, every one the seat's (data/b745_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b745_corrigendum.txt', 'data/b745_standing_v1240.txt', 'data/b745_rules.txt', 'data/b745_zetabox_plan.txt', 'data/b745_poscontrol_plan.txt',
                  'data/b745_amendments.json', 'data/b745_pathrefusal.txt',
                  'data/b745_reproduce.txt', 'data/b745_reproduce.json', 'data/b745_address_scan.txt', 'data/b745_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b745 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R355)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b745_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R355)(4): the sitting bank's rows by label -- a row opens `[A1] STATE`, `[C] STATE`, `[(7)] ...` at column 0, its fields indented two
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
        # ### (R355)(2)-(4) (b745's keys over b745's objects): the order by time and ancestry; v1.24.0's controls; the two plan banks and the
        # ### amendment row; SIDE-explicit-formula's main and branches unmoved; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the plan at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_print', K.C1_CORR, K.PRINT_COMMIT),
                                 ('plan_plan', K.C2_PLAN_FIRST, K.C2_RELAY), ('print_amend', K.PRINT_COMMIT, K.C2_AMEND_RELAY))),
        v1130=rd('b745_standing_v1240.txt'), plan=rd('b745_zetabox_plan.txt'), print_=rd('b745_poscontrol_plan.txt'), rows_bank=rd('b745_amendments.json'), sittingj={},
        amendj=jl('b745_amendments.json'), plan_at=_s(blob(ROOT, '%s:%s' % (K.C2_PLAN_FIRST, K.PLAN_BANK))), print_at=_s(blob(ROOT, '%s:%s' % (K.C2_RELAY, K.POSCONTROL_PLAN))),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in K.C2_AMEND_PP),
        reg_now_pp=read(os.path.join(PP, 'REGISTRY.md')), reg_pre_pp=_s(blob(PP, '%s:REGISTRY.md' % K.PRE_PP)),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        sit_files={}, sit_main={},
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b745_dispatch_rows.json') or '[]'), reproduce=rd('b745_reproduce.txt'), reproducej=jl('b745_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b745_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b744 left them
        rebuild=None, rebuild_rows=json.loads(rd('b745_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.REG_COMMIT), amend_pp=_ct(PP, K.C2_AMEND_PP[0]), amend_pp_last=_ct(PP, K.C2_AMEND_PP[-1]),
               amend=_ct(ROOT, K.C2_AMEND_RELAY), v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.PRINT_COMMIT), v9=files_of(ROOT, K.STANDING_COMMIT), plan1=files_of(ROOT, K.C2_PLAN_FIRST), amend=files_of(ROOT, K.C2_AMEND_RELAY),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b745's read-first bank's items by path, as its step zero wrote them (data/b745_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b744_closing.txt |', 'relay data/b744_events.txt |', 'relay data/b744_defects.txt |', 'relay data/b744_sitting.txt |',
                     'PLACE-papers OPEN_TRAILS.md at d79ecaf |', 'relay data/b737_offlinezero_plan.txt (149 lines) and data/b741_c7_plan.txt (122 lines) |',
                     'relay data/b742_offlinezero.txt |', 'relay data/b735_explicitformula.txt |', 'SIDE-explicit-formula at zq-b730 14ca5725 |',
                     'Mathlib at the pin de5ce8a9 |', 'relay tools/b745_worklist.py whole;')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R355)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'TWO PLANS AND THE AMENDMENT ((R355)(3), (4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (141 = 141 + 0, data/b745_citation_check.txt); the check CLEAN;
    the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 141 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b745, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b744's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b745, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b744()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b745_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b744's figures, read at FINDINGS :13838 as Component 1 landed them
    return landed(S, 0, ['b744 AT ITS WEIGHT', 'suite 112 of 116', 'relay eca0f83c', '23 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b745's title in the ferry's Component 3 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL planned, no build: ', 'the ζ box at 450-1,100 lines, 6 dispatches by the θ split and b741’s instrument; ',
                 'the positive control on pcConfig at 108-290 lines, 1 dispatch; ', 'both in one act, the positive control first, put to the author; ',
                 'v1.24.0: the repair phase, the prev-mode dry and 4 further repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R355)(1)-(2): the generated entry for b744's fifteen events and twenty-three defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(15), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 12, CLOSE 26 over 38, REPEAT 14); the repairs at tools/standing/ v1.24.0 by their controls
    bank; the corrigenda bank appended at row (64) and nothing before it changed; in Component 1's commits (the figures read from
    data/b745_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 23 and len(items) == j.get('items') == 38 and j.get('row') == 64 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 38 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 12 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 14 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.24.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 \
        and '  (64) ' in S['corrigenda'] and '  (65) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b745_rules.txt carries (R355)(2)'s eight rules, written at Component 1 (e810c5ba); data/b745_rules.txt (by form in (R355)(4)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    not written: the author's word amending (R355)(4) carries its rule to (R355) ("a row's ID is allocated from the file's maximum, not from the table it joins"), the next ruling's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and 'THE PRE-LOCK DRY RUNS EVERY PART' in r1 and 'A REPAIR BETWEEN THE LOCK AND THE SEAL' in r1 and 'A PUSHED BANK IS NEVER REWRITTEN' in r1 \
        and '(8) THE VERSION' in r1 and 'data/b745_rules.txt' in S['files']['rules'] and not os.path.exists(os.path.join(D, 'b745_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b745's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- NO LEAN FILE THIS ACT', 'CERTIFIED -- tools/standing/ v1.24.0', 'REGISTERED -- THE TWO PLANS',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b745: no dispatch this act -- no dispatch command in the capture, no row; VACUOUS on every row's read; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### N1: no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|_record\.py"? (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 2
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b745, N1: no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the dated note, the entry;
    OPEN_TRAILS: the dated note, the trail; REGISTRY by the author's word amending (R355)(4)), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b745's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The ζ box**', '**The positive control**', '**The recommendation**',
                 '**The amendment to (R355)(4)**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b745_corrigendum.txt', 'data/b745_standing_v1240.txt', 'data/b745_rules.txt', 'data/b745_zetabox_plan.txt', 'data/b745_poscontrol_plan.txt', 'data/b745_amendments.json',
                 'data/b745_reproduce.txt', 'data/b745_address_scan.txt', 'data/b745_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b745: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R355)(2)-(3), N2 (the name the frozen run list carries): v1.24.0's commit, the corrigendum's, then the first plan bank's and the second's, in
    that order by time and by ancestry within the relay, each plan committed before any Lean file (none this act); the first plan at HEAD its
    text at its commit, the second likewise; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('standing', 'corr', 'plan', 'print')
    return K.REGISTRATIONS in S['files']['plan1'] and bool(reg) and reg == head and bool(S['print_at']) and S['print_at'] == S['print_'] \
        and K.POSCONTROL_PLAN in S['files']['c2'] and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) and not S['zq_files'] \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b745_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R355)(2)-(4), N2 (the name the frozen run list carries): (2) whole before (3) -- v1.24.0, then the weight and corrigendum on PLACE-papers
    and the corrigendum's relay commit, before the first plan bank, by the commits' times; the second plan after the first; the author's word
    amending (R355)(4) after the plans: its three PLACE-papers writes, then its amendment row on the relay, before the face."""
    t_ = S['t']
    return K.REGISTRATIONS in S['files']['plan1'] and all(t_.get(k_) for k_ in ('standing', 'c1pp', 'corr', 'plan', 'print', 'amend_pp', 'amend_pp_last', 'amend')) \
        and t_['standing'] < t_['c1pp'] <= t_['corr'] < t_['plan'] < t_['print'] < t_['amend_pp'] <= t_['amend_pp_last'] <= t_['amend'] \
        and S['anc'].get('corr_print') is True and S['anc'].get('print_amend') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R355)(3), N2, N3 (the name the frozen run list carries): each plan bank in the form of b737's and b741's plans -- its controls block
    the first section, before any figure; the statement as a Prop with its binders (zeta_box's ∃ ρ : ℂ, ζ ρ = 0 ∧ ρ.re = 1/2 ∧ 12 < ρ.im < 16;
    pc_online drawn through Wide.li_nonneg_cfg_imp_online_ne_zero, [F2]'s condition printed as that theorem); the price; the stop points; the
    recommendation; the foot NOT BUILT and NO DISPATCH THIS ACT."""
    def secs(t):
        return [l for l in (t or '').split(NL) if l.startswith('## ')]
    z, p = S['plan'] or '', S['print_'] or ''
    zs, ps = secs(z), secs(p)
    vz, vp = _vlast(z), _vlast(p)
    return bool(zs) and zs[0].startswith('## THE CONTROLS') and bool(ps) and ps[0].startswith('## THE CONTROLS') \
        and 'theorem zeta_box : ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ ρ.re = 1 / 2 ∧ (12 : ℝ) < ρ.im ∧ ρ.im < 16' in z \
        and 'Wide.li_nonneg_cfg_imp_online_ne_zero pcConfig pc_count pc_ne_zero pc_li_nonneg' in p and 'theorem pc_online : ∀ ρ ∈ pcConfig.carrier, ρ.re = 1 / 2' in p \
        and any(s_.startswith('## (g) THE STOP POINTS') for s_ in zs) and any(s_.startswith('## (g) THE STOP POINTS') for s_ in ps) \
        and any('RECOMMENDATION' in s_ for s_ in zs) and any('RECOMMENDATION' in s_ for s_ in ps) \
        and vz.startswith('THE PLAN: zeta_box') and vp.startswith('THE PLAN: pcConfig') and all('NOT BUILT' in v_ and 'NO DISPATCH THIS ACT' in v_ for v_ in (vz, vp))
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R355)(5): no kernel's main touched -- SIDE-explicit-formula's main at the worklist's EF_MAIN (8fbab45d, as b744 left it), the branches
    each at the worklist's tip locally and at origin; zq-b730's diff against its entering tip 14ca5725 empty, no Lean file this act; no sitting kernel."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN == K.EF_BASE and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and not S['zq_files'] and K.ZQ_TIP == K.ZQ_ENTERING and not K.SITTING_TIPS

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.18.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b744's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R355)(3), (4) as amended, N2, N5 (the name the frozen run list carries): the first plan bank unmoved at its commit's md5; the amendment
    row banked (the author's words, its clause (R355)(4), its widening of REGISTRY, OPEN_TRAILS and FINDINGS); REGISTRY's three Epstein rows
    at :177-:179 reading 1.5c-21, 1.5c-22, 1.5c-23, the old IDs held once each by their own documents, the dated note naming b744, every other
    line of REGISTRY its line at the act's base; the three PLACE-papers writes one file each."""
    import hashlib as _hl
    rows_ = (S['amendj'] or {}).get('rows') or []
    w_ = rows_[0] if len(rows_) == 1 else {}
    now_ = (S['reg_now_pp'] or '').replace(chr(13), '').split(NL)
    pre_ = (S['reg_pre_pp'] or '').replace(chr(13), '').split(NL)
    cells = [l_.split('|')[1].strip() if l_.startswith('|') else '' for l_ in now_[176:179]]
    moved = [i_ + 1 for i_, (a_, b_) in enumerate(zip(pre_, now_)) if a_ != b_]
    note = now_[len(pre_):] if len(now_) > len(pre_) else []
    files_ = [S['reg_pp'].get(h_) for h_ in K.C2_AMEND_PP]
    return _hl.md5(raw(os.path.join(ROOT, *K.REGISTRATIONS.split('/')))).hexdigest() == K.PLAN_MD5 \
        and w_.get('clause') == '(R355)(4)' and sorted(w_.get('widens') or []) == ['PLACE-papers/FINDINGS.md', 'PLACE-papers/OPEN_TRAILS.md', 'PLACE-papers/REGISTRY.md'] \
        and '(R355) carries the rule' in (w_.get('words') or '') and cells == ['1.5c-21', '1.5c-22', '1.5c-23'] and moved == [177, 178, 179] \
        and any('b744' in l_ and 'collision' in l_ for l_ in note) and files_ == [['REGISTRY.md'], ['OPEN_TRAILS.md'], ['FINDINGS.md']] \
        and K.C2_AMEND_RELAY and 'data/b745_amendments.json' in S['files']['amend']


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
    """standing clauses v9 (Component 7 of (R355): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b745_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b744's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R355-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b744's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R355) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b744's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R354)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base b41fa006',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 141 = 141 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b744-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 3 form: the two controls planned, no build, each at its lines and dispatches by its route or carrier, the recommendation, v1.24.0`s repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R355)(1)-(2): the generated corrigendum for b744`s record, landed at FINDINGS :13840: its fifteen events and twenty-three defects, 38 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 12 CLOSE 26, REPEAT 14; v1.24.0`s repairs by data/b745_standing_v1240.txt; the corrigenda bank appended at row (64)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b745_rules.txt carrying (R355)(2)`s eight rules in Component 1`s commit, no data/b745_rules.txt (the amendment`s rule carried to (R355))',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b745's objects
    ('G-REGISTRATIONS-FIRST', '(R355)(2)-(3), N2: v1.24.0`s commit, the corrigendum`s, then the first plan bank`s (2e1caea2) and the second`s (28a554eb), in that order by time and ancestry, no Lean file; each plan at HEAD its text at its commit; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_print=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b745_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R355)(2)-(4), N2: (2) whole before (3) -- v1.24.0, the weight and corrigendum, then the first plan, the second; the amendment`s three PLACE-papers writes and its row after the plans, by time and ancestry',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(print_amend=False))),
    ('G-DERIVATION-GRADED', '(R355)(3), N2, N3: each plan bank in the plan form -- the controls block first, the statement as a Prop (zeta_box; pc_online through Wide.li_nonneg_cfg_imp_online_ne_zero, [F2]`s condition), the stop points, the recommendation, the foot NOT BUILT, NO DISPATCH THIS ACT',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'print_', (S['print_'] or '').replace('## THE CONTROLS', '## THE FIGURES', 1))),
    ('G-OFFSET-POST-HOC', 'N5, (R355)(5): no kernel`s main touched -- SIDE-explicit-formula`s main at 8fbab45d as b744 left it, the branches each at the worklist`s tip locally and at origin; zq-b730`s diff against 14ca5725 empty, no Lean file this act',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at b41fa006, VERSION 9; v8 at HEAD its blob at b41fa006; no v10; v9`s commit an ancestor of v1.24.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R355)(3)-(4) as amended, N2, N5: the first plan bank unmoved at its commit`s md5; the amendment row banked, widening REGISTRY, OPEN_TRAILS and FINDINGS; REGISTRY`s Epstein rows at :177-:179 1.5c-21 to 1.5c-23, nothing else moved, the dated note naming b744; one PLACE-papers write per file',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'reg_now_pp', (S['reg_now_pp'] or '').replace('| 1.5c-23 |', '| 1.5c-18 |'))),
    ('G-DIFFERS-ERRATA', '(R355)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at the act`s base, no differs or errata bank, the worklist naming no line or id; the weight line and the corrigendum in f697b01, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b745_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R355-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b744`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no dispatch this act, no row and no run; VACUOUS on the rows` read, the plant a planted dispatch refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture and no row, the order and memory reads VACUOUS; no b721-b744 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b744 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b744 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS and OPEN_TRAILS, REGISTRY by the author`s word amending (R355)(4)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b744`s trail record on OPEN_TRAILS (:17718) and its root in the chain', lambda S: '### b744 — lane two, act one hundred and seventy, the discharge sitting under (R354)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS, REGISTRY by the amendment): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b745 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b744's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b745: (R355)'s rows, set at step zero by the splice route (scratch splice745.py). (1)'s line read by the ruling from the public relay at 7d448774
    pub = _blob('D:/relay', '7d448774', 'data/b744_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b744_closing.txt :1, the head line as the public relay carries it at 7d448774', bool(pub) and pub[0] == at(cl, 1) and 'relay f5ff3680' in pub[0] and 'PLACE-papers 5937961' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 113 of 116', 'root 3c30761bc54fbfd4', '2 prompts answered', 'scores 8 of 8 HELD', '17 defects'):
        add('ruling (1)', 'data/b744_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'data/b744_closing.txt :5, the counter CLAIM 12, CLOSE 11, REPEAT 9 OF 23, DEFECTS 17, EVENTS 6', 'CLAIM 12, CLOSE 11, REPEAT 9 OF 23' in at(cl, 5) and 'DEFECTS 17, EVENTS 6' in at(cl, 5), at(cl, 5)[-60:], '1')
    import hashlib as _hl
    for f_, n_, md_, ws_ in (('data/b744_poscontrol_plan.txt', 137, 'b72ad7bbe28693a1192cfa60329fc607', ('pcConfig', 'pc_count', 'pc_ne_zero', 'pc_li_nonneg', 'pc_online', 'li_nonneg_cfg_imp_online_ne_zero', '108-290')),
                             ('data/b744_zetabox_plan.txt', 183, 'ef777cc24752911990d56d2214fe38b6', ('SPZ1', 'SPZ2', 'SPZ3', '450-1,100', 'hurwitzEvenFEPair', '12 AT MOST'))):
        by_ = open(p(*f_.split('/')), 'rb').read() if os.path.exists(p(*f_.split('/'))) else b''
        md5_ = _hl.md5(by_).hexdigest()
        add('ruling (1), (4), ferry (read first)', '%s whole, %d lines, md5 %s, unrewritten' % (f_, n_, md_), md5_ == md_ and by_.count(b'\n') == n_ and not gr('D:/relay', 'status', '--porcelain', '--', f_),
            'md5 %s ; lines %d' % (md5_, by_.count(b'\n')), '2' if 'poscontrol' in f_ else '3')
        tx_ = by_.decode('utf-8', 'replace')
        for w_ in ws_:
            add('ruling (1), ferry (read first)', '%s carries %s' % (f_, w_), w_ in tx_, 'present' if w_ in tx_ else 'ABSENT', '2' if 'poscontrol' in f_ else '3')
    rgl_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    for n_, r_ in ((177, '1.5c-21'), (178, '1.5c-22'), (179, '1.5c-23')):
        add('ruling (1), (3), ferry (read first)', 'REGISTRY.md :%d, row %s, an Epstein row' % (n_, r_), at(rgl_, n_).startswith('| %s | The Epstein instance' % r_), at(rgl_, n_)[:60], '1')
    add('ruling (scope), ferry (read first)', 'REGISTRY.md :1242, the foot note on the collision (b744`s dated note)', at(rgl_, 1242).startswith("*Dated note, b744, 2026-11-06, on the author's word amending"), at(rgl_, 1242)[:60], '1')
    rgs_ = gr(PP, 'log', '-1', '--format=%s', '0d51a02')
    add('ruling (1)', 'PLACE-papers 0d51a02, the renumbering commit', 'b744' in rgs_, rgs_[:60], '1')
    add('ruling (1), ferry (read first)', 'data/b744_amendments.json, the author`s amendment row', os.path.exists(p('data', 'b744_amendments.json')) and bool(gr('D:/relay', 'ls-files', '--', 'data/b744_amendments.json')), 'tracked', '1')
    em_ = (gr('D:/SIDE-explicit-formula', 'rev-parse', 'main') or '').strip()
    add('ruling (3), (6)', 'SIDE-explicit-formula main at 8fbab45, unmoved', em_.startswith('8fbab45'), em_[:8], '1')
    sv_ = lines_of(p('data', 'b744_standing_v1240.txt'))
    add('ruling (1)', 'data/b744_standing_v1240.txt :146, v1.24.0, CASES 29 ; AS WANTED 29', 'v1.24.0' in at(sv_, 146) and 'CASES 29 ; AS WANTED 29' in at(sv_, 146), at(sv_, 146)[:60], '1')
    ck_ = lines_of(p('data', 'b744_checks.txt'))
    add('ruling (1)', 'data/b744_checks.txt :16, 116 run, 113 passing, G-AXIOM-CLAIM and G-RULE-POSTSEAL-READ failing',
        "ARMS RUN : 116. ### LIVE PASSING : 113. ### LIVE FAILING : 2 ['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ']" in at(ck_, 16), at(ck_, 16)[:60], '1')
    sc9_ = _jl('b744_scores_close.json')
    held_ = sorted(k_ for k_, v_ in sc9_.items() if v_[:1] == ['HELD'])
    add('ruling (1)', 'data/b744_scores_close.json, 8 of 8 HELD', len(held_) == 8, 'HELD %s' % ' '.join(held_), '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b744']]
    add('ruling (1)', 'data/act_roots.txt, b744`s root 3c30761b chained from b743`s 72f9741c', len(ar9_) == 1 and ar9_[0][1].startswith('3c30761b') and ar9_[0][2].startswith('72f9741c'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    rbj_ = _jl('b744_root_banks.json')
    add('ruling (1)', 'data/b744_root_banks.json, 115 banks', len(rbj_.get('rows') or []) == 115, 'rows %d' % len(rbj_.get('rows') or []), '1')
    b3_ = rd(p('data', 'b744_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b744 (b744`s post-push part b3)', 'b744 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b744 AGREE' if 'b744 AGREE' in b3_ else 'ABSENT', '1')
    mv_ = rd(p('data', 'b744_mirror_verify.txt')) or ''
    add('ruling (1)', 'data/b744_mirror_verify.txt, CLEAN ON ALL THREE CLAUSES', 'CLEAN ON ALL THREE CLAUSES' in mv_, 'CLEAN' if 'CLEAN ON ALL THREE CLAUSES' in mv_ else 'ABSENT', '1')
    add('ruling (1)', 'data/b744_closing.txt, the mirror mirror-refresh-2026-11-06-b744', 'mirror-refresh-2026-11-06-b744' in NL.join(cl), 'read', '1')
    aa_ = rd(p('data', 'b744_author_answers.txt')) or ''
    add('ruling (1)', 'data/b744_author_answers.txt, the two answers: both controls, positive first; the tag, yes', 'positive first' in aa_ and 'zq-b730' in aa_, 'read', '1')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.25.0's commit's parent once it lands, HEAD's blob before
    add('ruling (1)', 'tools/standing/VERSION v1.24.0 entering the act', v0_ == 'v1.24.0', v0_, '1')
    for f_ in ('data/b744_relay_push-b744-closing_push_out.txt', 'tools/mirror_prevbuild.json'):
        add('ruling (2)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), (2), ferry (read first)', 'events (1)-(6) and 17 defects (data/b744_events.txt, data/b744_defects.txt)',
        starts == list(range(1, 7)) and len(letters) == 17, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    ev = lines_of(p('data', 'b744_events.txt'))
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    for n_, k_, w_ in ((4, 1, "THE SEAT'S [CLOSE ; REPEAT b743 (c)]"), (5, 2, "THE SEAT'S [CLAIM ; NEW]"), (8, 3, "THE TOOLS' [CLAIM ; NEW]"),
                       (11, 4, "THE SEAT'S [CLAIM ; NEW]"), (14, 5, "THE SEAT'S [CLAIM ; NEW]"), (17, 6, "THE SEAT'S [CLOSE ; REPEAT b743 (14)]")):
        add('ruling (2), ferry (read first)', 'data/b744_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    for n_, w_ in ((5, 'standing-b3'), (8, 'root_arm'), (14, 'f5ff3680'), (17, 'post-push part standing-a1')):
        add('ruling (2), ferry (read first)', 'data/b744_events.txt :%d carries %s' % (n_, w_), w_ in at(ev, n_), at(ev, n_)[:60], '1')
    ev8_ = NL.join(ev[7:10])
    add('ruling (2)(ii)', 'data/b744_events.txt (3), the root arm at 2,360 MB under the 2,560 MB hold', '2360' in ev8_.replace(',', '') and '2560' in ev8_.replace(',', ''), 'read', '1')
    rp_ = lines_of(p('tools', 'standing', 'repeat.py'))
    add('ruling (2)(iv)', 'tools/standing/repeat.py :133, the exempt set (its name in the code: keep)', at(rp_, 133).lstrip().startswith('keep = {'), at(rp_, 133)[:60], '1')   # ### b745: the first needle read the word "exempt", absent from the line (step-zero defect)
    for c_ in ('da9910f9', 'f5ff3680'):
        add('ruling (2)(iv)-(v)', 'relay %s, the commit the events name' % c_, bool(gr('D:/relay', 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')), gr('D:/relay', 'log', '-1', '--format=%s', c_)[:60], '1')
    add('ferry (read first)', 'data/b744_closing.txt, its CARRIED items beneath the head', any('CARRIED' in l for l in cl), 'read', '0')
    b41_ = lines_of(p('data', 'b741_c7_plan.txt'))
    add('ferry (read first)', 'data/b741_c7_plan.txt :1, the instrument`s plan head', bool(at(b41_, 1)), at(b41_, 1)[:60], '3')
    ob_ = lines_of(p('data', 'b742_offlinezero.txt'))
    for n_, k_, w_ in ((67, '(3)', 'L_P <= LPq = 6.098e-10, lemma lp_le'), (68, '(4)', 'the generator tools/b742_s6gen.py was committed at relay 22f8d6b1')):
        add('ruling (4)(c), ferry (read first)', 'data/b742_offlinezero.txt :%d, note %s carries %s' % (n_, k_, w_), at(ob_, n_).startswith('  ' + k_) and w_ in at(ob_, n_), at(ob_, n_)[:60], '3')
    ef_ = lines_of(p('data', 'b735_explicitformula.txt'))
    add('ferry (read first)', 'data/b735_explicitformula.txt :184-:185, zq_li_nonneg_imp_online_instance', 'theorem zq_li_nonneg_imp_online_instance' in at(ef_, 184)
        and '0 ≤ Wide.liCoeff zqZeroConfig n' in at(ef_, 185), at(ef_, 184)[:60], '2')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (3), (4)', 'zq-b730 at 14ca5725 entering the act (the tag`s commit)', zt_.startswith('14ca5725') or bool(K.ZQ_COMMITS), zt_[:8], '1')
    for br_ in ('c2-b725', 'keiper-b725', 'detect-b729'):
        add('ruling (5)', '%s kept on SIDE-explicit-formula' % br_, bool(gr(EF_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for f_, n_, w_ in (('SIDEExplicitFormula/Schema/Wide/Config.lean', 28, 'structure WideConfig where'),
                       ('SIDEExplicitFormula/Schema/Wide/Config.lean', 38, '  finite_window :'),
                       ('SIDEExplicitFormula/Schema/Wide/Config.lean', 49, 'def HCount (Z : WideConfig)'),
                       ('SIDEExplicitFormula/Schema/Wide/StripFree.lean', 157, 'theorem li_nonneg_cfg_imp_online_ne_zero'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 166, '  h.count.elim fun _ hc => Wide.li_nonneg_cfg_imp_online_ne_zero'),
                       ('SIDEExplicitFormula/Schema/ZQ/OffZero/IncGamma.lean', 29, 'def incGamma1')):
        bl_ = _blob(EF_, '14ca5725', f_).replace(chr(13), '')
        ok_ = at(bl_.split(NL), n_).startswith(w_)
        add('ruling (1), ferry (read first)', '%s at 14ca5725 :%d carries %s' % (f_, n_, w_), ok_, at(bl_.split(NL), n_)[:60] if bl_ else 'ABSENT', '2' if 'IncGamma' not in f_ else '3')
    oz_ = [x_.split('/')[-1][:-5] for x_ in gr(EF_, 'ls-tree', '--name-only', '14ca5725', 'SIDEExplicitFormula/Schema/ZQ/OffZero/').split()]
    add('ferry (read first)', 'the OffZero modules by name at 14ca5725, 29', sorted(oz_) == sorted(K.ZQ_OFFZERO_MODULES), '%d: %s' % (len(oz_), ' '.join(oz_)[:60]), '3')
    ML_ = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
    mh_ = (gr(ML_, 'rev-parse', 'HEAD') or '').strip()
    add('ferry (read first)', 'Mathlib at the pin de5ce8a9', mh_.startswith('de5ce8a9'), mh_[:8], '3')
    rz_ = _blob(ML_, 'HEAD', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean').replace(chr(13), '').split(NL)
    add('ferry (read first)', 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean :121, def riemannZeta', at(rz_, 121).startswith('def riemannZeta'), at(rz_, 121)[:60], '3')
    hz_ = _blob(ML_, 'HEAD', 'Mathlib/NumberTheory/LSeries/HurwitzZetaEven.lean')
    add('ferry (read first)', 'Mathlib/NumberTheory/LSeries/HurwitzZetaEven.lean, hurwitzEvenFEPair by name', 'def hurwitzEvenFEPair' in hz_, 'present' if 'def hurwitzEvenFEPair' in hz_ else 'ABSENT', '3')
    gm_ = gr(ML_, 'ls-tree', '--name-only', 'HEAD', 'Mathlib/Analysis/SpecialFunctions/Gamma/').split()
    add('ferry (read first)', 'Mathlib/Analysis/SpecialFunctions/Gamma/* by name', 'Mathlib/Analysis/SpecialFunctions/Gamma/Basic.lean' in gm_, '%d files' % len(gm_), '3')
    iv_ = _blob(ML_, 'HEAD', 'Mathlib/Topology/Order/IntermediateValue.lean')
    add('ferry (read first)', 'the intermediate value theorem by name (intermediate_value_Icc, Mathlib/Topology/Order/IntermediateValue.lean)', 'theorem intermediate_value_Icc ' in iv_, 'present' if 'theorem intermediate_value_Icc ' in iv_ else 'ABSENT', '3')
    add('ruling (1)', 'FINDINGS :%d, b744`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## '), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b744`s weight line and corrigendum, the form b745`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fi, K.B711_WEIGHT)) and bool(at(fi, K.B711_CORRIGENDUM)), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b744`s trail record, its hand section' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b744 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (2)', 'OPEN_TRAILS :%d, b744`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    sm_ = gr(PP, 'ls-files', '--', 'SPIRAL_MAP.md')
    add('ruling (3)', 'SPIRAL_MAP.md tracked at PLACE-papers (its 2D block the tag`s note goes to)', bool(sm_) and '2D' in (rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''), 'tracked' if sm_ else 'ABSENT', '1')
    add('ruling (scope)', 'the census THE_KEYSTONE_CENSUS_v0_8_3.md at 36 kernels', '36' in NL.join(lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))[:40]), 'read', '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.24.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.24.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R355)(4): b744's export, the mirror's last
    add('ruling (4)', '%s, b744`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R355)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b744-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R355)(2), (4): act_current alone, then b744's terminal tables and its closing capture, each committed alone (mirror_prevbuild restored to HEAD's blob, no commit)
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b744_relay_push-b744-closing_push_out.txt'])):   # ### b745: no terminal table carried (b744 left none)
        if not c_:
            add('ruling (4)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (2), (4)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (4)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (4)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b745_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b745_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b745 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b744_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.24.0's controls, the two plan banks and the amendment row, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R355)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R355)(6)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R355)(5): no kernel's main touched, no Lean file, no tag).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b745 ((R355)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R354)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b745 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTY-ONE, THE PLAN ACT OF THE TWO CONTROLS: b744 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE THREE IMPROVISED ROUTES AND THE BANK REWRITTEN AFTER ITS PUSH; '
              'W-ORD-ZETA-BOX AND W-ORD-POSITIVE-CONTROL PRICED, NO BUILD, UNDER (R355).**')   # ### the ferry's :25
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b744's sections over b744's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.24.0: the pre-lock dry in prev mode, the repair phase, the hook`s scope, no pushed bank rewritten and the tags at the dry, the face`s branch list, the kernel push before the root, the repeat readings, the version, each case failing before its repair and passing after', 'b745_standing_v1240.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE TWO PLANS AND THE AMENDMENT ((R355)(3), (4))', [
                ('W-ORD-ZETA-BOX: zeta_box at t₁ = 12, t₂ = 16, the controls first, the price, the stop points, not built', 'b745_zetabox_plan.txt'),
                ('W-ORD-POSITIVE-CONTROL: pcConfig, [F2]`s condition as the theorem pc_online is drawn through, the controls first, the price, not built', 'b745_poscontrol_plan.txt'),
                ('the probe-path refusal printed before the lock gate', 'b745_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b745_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b744`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b745_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R354)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R355)(5)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, untagged, the tag put to the author ; no Lean file ; no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches of the two allowed (N1: each a print; none sent) ; the rebuild-b721 branches of the wave 1 kernels as b744 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b744-* branches of relay and PLACE-papers and push-b744-sitting of SIDE-explicit-formula deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: each plan committed before any Lean file and opening with its controls, the tools` controls before their figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate ;',
    '    N3: each plan`s statement a Prop with its binders, [F2]`s condition the theorem pc_online is drawn through ; no sentence says a control built or run ; ζ, RH and h2 not moved ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b745_address_scan.txt, data/b745_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo field touched ; the deposit route untouched, publish never called, the draft held at v5 ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the dated note to :13812, the entry), OPEN_TRAILS (the dated note to :17716, the trail), REGISTRY (three ID cells and a dated note, by the author`s word amending (R355)(4)) ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b745`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.24.0 by (R355)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b744 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R355)(6)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL (OPEN_TRAILS), their plan banks at their prices and stop points (relay data/b745_zetabox_plan.txt, data/b745_poscontrol_plan.txt) ;',
    '        the tag on zq-b730 at 14ca5725 as the author answers ((R355)(5)) ; (R355)`s rule, a row`s ID allocated from the file`s maximum (relay data/b745_amendments.json) ; [F3]`s reading note for W-ORD-LI-ARITH (relay data/b744_sitting.txt) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b745_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b744 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b745: the standing repairs are v1.24.0's ((R355)(2), relay data/b745_standing_v1240.txt, read in the corrigendum section); the
    # ### carry's diffs here (b745 carried at step zero before the fold; its tools since are the templates and tools/acts/b745.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main touched this act; '
          'no Lean file; the %s branches of the wave 1 kernels as b744 left them; port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b745's form over b745's objects (b744's form in git at b744's record tool): the corrigendum's foot and v1.24.0's controls; the two plan banks'
    feet and the navigator's lean; the amendment row; the citation check; the reproduction run; the address scan; each by its own lines through
    _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1240.txt' % ACT, r'\*\*v1\.24\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.24.0`s controls')
    zb = _bfig('%s_zetabox_plan.txt' % ACT, r'\*\*THE PLAN: zeta_box AT t₁ = (\d+), t₂ = (\d+) ; [^;]+ ; ([\d,]+-[\d,]+) LINES, [^;]+ ; (\d+) DISPATCHES NOMINAL, (\d+) AT MOST ; '
               r'NO DISPATCH THIS ACT ; NOT BUILT\.\*\*', 'the ζ box plan`s foot')
    pc = _bfig('%s_poscontrol_plan.txt' % ACT, r'\*\*THE PLAN: pcConfig = (\{[^}]+\}) ; pc_online DRAWN THROUGH (\S+) \(StripFree\.lean :(\d+)\), [^;]+ ; [^;]+ ; ([\d,]+-[\d,]+) LINES ; '
               r'(\d+) DISPATCH NOMINAL ; NO DISPATCH THIS ACT ; NOT BUILT\.\*\*', 'the positive control plan`s foot')
    lean_ = _bfig('%s_poscontrol_plan.txt' % ACT, r"THE NAVIGATOR'S LEAN, printed as the seat's: ([A-Z][A-Z ,-]+[A-Z])\.", 'the navigator`s lean')[0]
    if 'BOTH IN ONE ACT' not in lean_ or 'POSITIVE-CONTROL FIRST' not in lean_:
        sys.exit('### THE NAVIGATOR`S LEAN READS %r, NOT THE COMPOSER`S WORDING -- NOTHING COMPOSED' % lean_)
    rr_ = [l_ for l_ in rdn('%s_rules.txt' % ACT).split(NL) if re.match(r'^\(\d+\) ', l_)]
    reps_ = [l_ for l_ in rr_ if 'HELD' not in l_.split('(R355)')[0] and 'THE VERSION' not in l_.split('(R355)')[0]]
    am_ = jl('%s_amendments.json' % ACT).get('rows') or []
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], repairs=len(reps_), further=len(reps_) - 2,
                zb_t1=zb[0], zb_t2=zb[1], zb_lines=zb[2], zb_disp=int(zb[3]), zb_most=int(zb[4]),
                pc_carrier=pc[0], pc_thm=pc[1], pc_line=pc[2], pc_lines=pc[3], pc_disp=int(pc[4]),
                rec='both in one act, the positive control first',
                amend_n=len(am_), amend_clause=(am_[0].get('clause') if am_ else None), amend_widens=len((am_[0].get('widens') or []) if am_ else []),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R355)(3): the kernel rows of one kind as banked (data/b745_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R355)(3)(c), (4): no lean process runs on this host; the runner dispatches those of (R355)(3), two at most, each a print -- none sent
    this act (the worklist's EF_RUNS empty, MAX_DISPATCHES 2); no suite part in the background. From the command bank (the seat's commands, read
    live from the capture by the `commands` route), the dispatch rows (none: their free_mb read VACUOUS) and the hook's refusal bank (a suite
    part sent in the background refused BACKGROUND)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    runs_ = sorted(set(reads_)) == sorted(str(x) for x in K.EF_RUNS)
    free_ = [r for r in _ef_kind(rows_, 'dispatch') + _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    bg_ = [l for l in rdn('%s_hook_refusals.txt' % ACT).split(NL) if '| BACKGROUND |' in l]
    bgc_ = [r['n'] for r in ((cm.get('rows') or []) if cm else []) if r.get('bg') and re.search(r'fold\.py"? checks\b|_checks\.py', r.get('cmd') or '')]
    refused_ = _ef_kind(rows_, 'dispatch_refused')
    ok = bool(cm) and not seat_lean and len(disp or []) <= K.MAX_DISPATCHES == 2 and len(disp or []) == len(K.EF_RUNS) == len(_ef_kind(rows_, 'dispatch')) \
        and runs_ and not free_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b745_commands.json): %s; dispatch commands in the capture: %s (two at most, each a print), sends refused by the host: %d; the worklist`s runs %d; dispatch rows %d (VACUOUS on a row`s free memory where no row exists); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), len(K.EF_RUNS), len(rows_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b745's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b745_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b745_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b745_standing_v1240.txt', '## THE CONTROLS', '### the instances read at their commits'),
               ('data/b745_zetabox_plan.txt', '## THE CONTROLS', '## (a) THE OBJECT AND THE STATEMENT'),
               ('data/b745_poscontrol_plan.txt', '## THE CONTROLS', "## (a) [F2]'S CONDITION"))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R355): each plan bank committed before any Lean file (none this act) and opening with its controls; (2) whole before (3) -- step zero's
    banks, v1.24.0's commit, the weight and corrigendum on PLACE-papers, the corrigendum's relay commit, the first plan, the second, then the
    amendment's PLACE-papers writes and its row, in that order by time, v1.24.0's commit an ancestor of the second plan's; the first plan at HEAD
    its blob at its one commit, its md5 the worklist's, no later commit touching it; every figure bank opens with its controls; the (W)
    regeneration, the pre-lock comparison (both modes of the pre-lock dry among it) and the probe-path refusal print before the lock gate."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_PLAN_FIRST), (ROOT, K.C2_RELAY),
              (PP, K.C2_AMEND_PP[0]), (ROOT, K.C2_AMEND_RELAY)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.PRINT_COMMIT], capture_output=True).returncode == 0
    later_ = [h_[:8] for h_ in g(ROOT, 'log', '--format=%H', '%s..HEAD' % K.REG_COMMIT, '--', K.REGISTRATIONS).split() if h_.strip()]
    same_ = _s_md5(os.path.join(ROOT, *K.REGISTRATIONS.split('/'))) == K.PLAN_MD5 \
        and rdn(K.REGISTRATIONS[len('data/'):]) == g(ROOT, 'show', '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS)).replace(chr(13), '') and not later_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the first plan its md5 %s and its blob at %s, a later commit touching it: %s -- %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.24.0, the weight and corrigendum, the corrigendum`s relay commit, the first plan, the second, the amendment`s first PLACE-papers write and its row in that order by time: %s (%s), v1.24.0 an ancestor of the second plan: %s; the tools` controls before their figures: %s' % (
            K.PLAN_MD5[:8], K.REG_COMMIT, later_ or 'NONE', same_, regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b745's objects; b744's in git at b744's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b745_standing_v1240.txt', ('ALL AS WANTED',)), ('b745_zetabox_plan.txt', ('THE PLAN: zeta_box', 'NOT BUILT')),
             ('b745_poscontrol_plan.txt', ('THE PLAN: pcConfig', 'NOT BUILT')),
             ('b745_corrigendum.txt', ('ITEMS',)), ('b745_citation_check.txt', ('THE CHECK CLEAN',)), ('b745_reproduce.txt', ('REPRODUCES',)), ('b745_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R355): each plan's statement prints as a Prop with its binders; [F2]'s condition prints as the theorem the control's conclusion is drawn
    through; no sentence says either control has been built or run, nothing of ζ beyond the box's own sentence, nothing of RH; the entry's nouns
    the banks'; the root prompt's sentences about the entry the composer's. From the banks' last lines, the plan banks, the entry's sentences
    and the root prompt in the answers bank (standing.rootprompt.entry_unbacked)."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    z_, p_ = rdn('%s_zetabox_plan.txt' % ACT), rdn('%s_poscontrol_plan.txt' % ACT)
    props_ = 'theorem zeta_box : ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ ρ.re = 1 / 2 ∧ (12 : ℝ) < ρ.im ∧ ρ.im < 16' in z_ \
        and 'theorem pc_online : ∀ ρ ∈ pcConfig.carrier, ρ.re = 1 / 2' in p_
    f2_ = 'Wide.li_nonneg_cfg_imp_online_ne_zero pcConfig pc_count pc_ne_zero pc_li_nonneg' in p_
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None|unbuilt|planned|priced|would|if)\b'
    built_ = [s_ for s_ in sents if re.search(r'\b(?:built|compiled|ran|dispatched)\b', s_) and re.search(r'\b(?:ZETA-BOX|POSITIVE-CONTROL|ζ box|positive control|zeta_box|pc_online)\b', s_) and not re.search(neg_, s_)]
    loc_ = [s_ for s_ in sents if re.search(r'\b(?:RH|GRH|h2)\b.*\b(?:holds|fails|proved|refuted|moved)\b', s_) and not re.search(neg_, s_)]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and props_ and f2_ and not built_ and not loc_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the statements as Props with their binders: %s; [F2]`s condition as the theorem pc_online is drawn through: %s; read from %s, a sentence saying a control built, compiled, ran or dispatched outside a negation: %s; a sentence saying RH, GRH or h2 holds, fails or moved outside a negation: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), props_, f2_, src, built_ or 'NONE', loc_ or 'NONE', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R355) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R355)(5))
# ### (R355)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


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
    # ### (R355) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b744's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
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
    # ### (R355)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b744 left them; the address scan's count from its bank (relay data/b745_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R355)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R355)(5), N5: no Zenodo write, no release, no new version, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    ghe_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+release\b|/actions/newversion|zenodo\.org/api|\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b745_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a Zenodo route or a repository`s edit in the capture: %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b745 — lane two, act one hundred and seventy-one, the plan act of the two controls under (R355): b744 at its weight and its corrigendum; v1.24.0; '
            'W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL priced, no build; REGISTRY`s Epstein rows renumbered by the author`s word')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 3 form adjusted to what the act did; every figure from the banks (the plans' feet,
    the navigator's lean, the rules bank's repairs)."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## W-ORD-ZETA-BOX and W-ORD-POSITIVE-CONTROL planned, no build: the ζ box at %s lines, %d dispatches by the θ split and b741’s instrument; '
            'the positive control on pcConfig at %s lines, %d dispatch%s; %s, put to the author; v1.24.0: the repair phase, the prev-mode dry and %d further repairs landed' % (
                f['zb_lines'], f['zb_disp'], f['pc_lines'], f['pc_disp'], '' if f['pc_disp'] == 1 else 'es', f['rec'], f['further']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the author’s word amending (R355)(4): REGISTRY’s three Epstein rows renumbered 1.5c-21 to 1.5c-23, the collision b744’s, the rule carried to (R355) (relay data/b745_amendments.json); (2) [F2]’s literal route cannot be met by a finite carrier (ZQPremises), the control’s conclusion drawn through Wide.li_nonneg_cfg_imp_online_ne_zero, the theorem Epstein’s is drawn through, for the author’s strike (relay data/b745_poscontrol_plan.txt (a)); (3) the reality of the completed function on the line (lemma Z3) and Hardy’s Z ABSENT at the pin, priced in the ζ box plan (relay data/b745_zetabox_plan.txt (d)); (4) no print dispatch of the two allowed was sent, the names and signatures read from the tree; '
            +
            '(5) %s and the seat’s %s defect%s as lettered' % (
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R355)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b745's objects; b744's composer in git at
    b744's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot, not a row quoting another act's (b745 defect (a'))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R354)(2)(v)
    e = ['', _title(), '',
         'Two controls are priced from their statements and neither is built. The ζ box: zeta_box, a zero of ζ on the line with ordinate between %s and %s, by a sign change of the completed function at the two named points through the θ split Mathlib carries and the exact-ℚ series and Lipschitz carry of b741, at %s lines and %d dispatches nominal (%d at most); the reality of the completed function on the line is ABSENT at the pin and priced. The positive control: pcConfig %s, its zeros on the line by construction, Li nonnegative for every n by the proved bound, the on-line conclusion drawn through %s (StripFree.lean :%s), the theorem Epstein’s conclusion is drawn through, at %s lines and %d dispatch%s. The recommendation, put to the author: %s. The draft stands at v5, HELD.' % (
             f['zb_t1'], f['zb_t2'], f['zb_lines'], f['zb_disp'], f['zb_most'], f['pc_carrier'], f['pc_thm'], f['pc_line'], f['pc_lines'], f['pc_disp'], '' if f['pc_disp'] == 1 else 'es', f['rec']), '',
         '*Filed at b745 on the author’s ruling `(R355)`; %d question%s put before the root. Banks: relay '
         '`data/b745_corrigendum.txt`, `data/b745_standing_v1240.txt`, `data/b745_rules.txt`, `data/b745_zetabox_plan.txt`, `data/b745_poscontrol_plan.txt`, `data/b745_amendments.json`, `data/b745_prelock.txt`, `data/b745_pathrefusal.txt`, '
         '`data/b745_reproduce.txt`, `data/b745_address_scan.txt`, `data/b745_touch.txt`, `data/b745_standing_figures.txt`, `data/b745_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R355)(1)-(2), %s, %s, %s): b744 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b744’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b745_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b745_standing_v1240.txt); the rules that answer them at relay data/b745_rules.txt.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): v1.24.0 at %s, then the weight and the corrigendum at PLACE-papers %s and relay %s, then the ζ box plan at %s and the positive control plan at %s, each committed as its own bank before any Lean, each opening with its controls; the first plan’s md5 %s equal to its blob at %s; the pre-lock comparison with the dry in prev mode, and the probe-path refusal, printed before the lock gate (relay data/b745_prelock.txt, data/b745_pathrefusal.txt). No lean process on this host and no dispatch of the two allowed: the runner arms read VACUOUS, no row existing to read.' % (K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8], K.PLAN_MD5[:8], K.REG_COMMIT[:8]), '',
         '**The ζ box** ((R355)(3)(a), N3): the statement `theorem zeta_box : ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ ρ.re = 1 / 2 ∧ (12 : ℝ) < ρ.im ∧ ρ.im < 16` with the standard three; its steps the reality on the line and the sign at t₁ = %s and t₂ = %s, by completedRiemannZeta split through hurwitzEvenFEPair 0 into incomplete-Γ terms, one shell per point; the cost law’s factor at γ ≈ 14.13 printed beside b741’s at 16.29; an instrument control on a known case, nothing new of ζ, nothing of RH (relay data/b745_zetabox_plan.txt).' % (f['zb_t1'], f['zb_t2']), '',
         '**The positive control** ((R355)(3)(b), N3): the carrier pcConfig %s, a finite WideConfig on the line by construction; `theorem pc_online : ∀ ρ ∈ pcConfig.carrier, ρ.re = 1 / 2` drawn through %s with the count and ρ ≠ 0 proved, [F2]’s condition read as that theorem because ZQPremises cannot be met by a finite carrier, the closure print to check it; Li nonnegative for every n, λ_n = 2(1 − cos nθ); the implication exercised with a true antecedent beside Epstein’s false one, nothing of ζ (relay data/b745_poscontrol_plan.txt).' % (f['pc_carrier'], f['pc_thm']), '',
         '**The recommendation** ((R355)(3)(c)): the ζ box %s lines and %d dispatches nominal, the positive control %s lines and %d; together within one act’s measured reach; the navigator’s lean %s, put to the author in the root prompt as one question.' % (
             f['zb_lines'], f['zb_disp'], f['pc_lines'], f['pc_disp'], f['rec']), '',
         '**The amendment to (R355)(4)** (the author’s word, relay data/b745_amendments.json): REGISTRY’s three Epstein rows renumbered 1.5c-21, 1.5c-22 and 1.5c-23, the IDs b744 gave them held by other rows, with a dated note naming the collision and b744 as its act; OPEN_TRAILS’ [F4] and FINDINGS’ b744 entry each a dated note; one PLACE-papers write per file (%s, %s, %s); the (W) list regenerated from it; the rule carried to (R355): a row’s ID is allocated from the file’s maximum, not from the table it joins.' % tuple(h_[:7] for h_ in K.C2_AMEND_PP), '',
         '**What this act is not**: no build, no Lean file written, no dispatch, no deposit, no tag, no merge, no Zenodo edit, no kernel’s main touched. The plans price two controls; nothing here bears on ζ, RH or h2.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b745_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b745_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b745_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b745 -- %s, %s, %s, %s -- against b744’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b745_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the two plans read one way: each prices a control of the instrument -- the ζ box its evaluation on a case whose answer is known, the positive control the schema’s implication with a true antecedent -- so the paper path has its cost and nothing of either is built.', '',
         '**Carried to:** %s, (R355)(6): the build of the control the author names, with its plan bank and stop points; the tag on zq-b730 at 14ca5725 as the author answers; (R355)’s rule on REGISTRY IDs; W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as entered; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds, and nothing here bears on ζ.*', '']
    return _title(), NL.join(e)


def _finding_text_b744():
    """b744's form over b744's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b745's objects; b744's composer in git at b744's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD, the two controls priced and open, no order closed or entered this act."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if not all(w_ in op for w_ in ('W-ORD-ZETA-BOX', 'W-ORD-POSITIVE-CONTROL')):
        sys.exit('### THE TRAIL: A PRICED ORDER NOT READ OPEN -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R355) ratified.** Its components as the ferry orders them (relay data/b745_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b744’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** W-ORD-ZETA-BOX priced at %s lines and %d dispatches (relay data/b745_zetabox_plan.txt, %s); W-ORD-POSITIVE-CONTROL priced at %s lines and %d (relay data/b745_poscontrol_plan.txt, %s); neither built, both open; no order entered or closed this act.' % (
                 f['zb_lines'], f['zb_disp'], K.C2_PLAN_FIRST[:8], f['pc_lines'], f['pc_disp'], K.C2_RELAY[:8]), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b745_standing_v1240.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The amendment:** the author’s word amending (R355)(4), REGISTRY’s Epstein rows 1.5c-21 to 1.5c-23 with dated notes at OPEN_TRAILS :17716 and FINDINGS :13812 (relay data/b745_amendments.json); the rule carried to (R355).', '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b745_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b745_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b745_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b745 `%s` (previous `%s`, b744’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b745_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b745_standing_v1240.txt); the standing '
             'report tool (relay data/b745_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched, no Lean file, no tag; SIDE-explicit-formula`s main at %s and zq-b730 at %s unmoved; %d dispatches; the %s branches as b744 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b745_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b744’s %s, %s, %s, %s (relay data/b745_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b745_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b744():
    """b744's trail record over b744's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: two at most, each a print; none sent; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b744 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b744`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none; no kernel`s main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 6, 6, 'branches', '### (R355)(2): relay push-b744-closing, push-b744-preroot, push-b744-record; PLACE-papers push-b744-preroot, push-b744-record; SIDE-explicit-formula push-b744-sitting; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: the author`s word amending (R355)(4) renumbers three ID cells (1.5c-21, 1.5c-22, 1.5c-23 at :177-:179) and appends a dated note.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### three, the ID cells of :177-:179, by the author`s word; MEASURED off git diff --numstat from the act`s first PLACE-papers head (d79ecaf3) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R355)(2): FINDINGS :13840.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R355)(2): row (64).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none: (R355) orders none.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: the two controls priced, entered at b744, open; no order entered or closed this act.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b745_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.24.0`s controls, the two plans` controls and figures, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 2, 2, 'commits', '### the two plan banks, each by a commit of its own before any Lean: 2e1caea2 and 28a554eb.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: each plan carries its own figures after its controls; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: no figure bank precedes the plans (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none, N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R355)(2): tools/standing/ to v1.24.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b745_address_scan.txt (the address never printed).'),
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
    # ### (R355)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b745_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b745_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1240', 'zetabox_plan', 'poscontrol_plan', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b745_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b745_registration_%s.txt -- b745, THE PLAN ACT OF THE TWO CONTROLS: b744 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.24.0; W-ORD-ZETA-BOX AND W-ORD-POSITIVE-CONTROL PRICED, NO BUILD; "
                             "REGISTRY`S EPSTEIN ROWS RENUMBERED BY THE AUTHOR`S WORD; NO DEPOSIT, NO TAG, UNDER (R355)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b744's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b745: b744's lines read banks this
act does not write, and are not carried; the lines are b745's: no Lean file this act (KERNEL, read from the ferry's (5)), tools/standing/ v1.24.0
by its controls (CERTIFIED), the two plans (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b745's lines, each from the record tool's figures over b745's banks
    # ------------------------------------------------------------------ KERNEL: (R355)(5), no Lean file, no kernel's main touched
    sz = seat('%s_ferry.txt' % ACT, 'no Lean file written')
    sk = sz   # ### (R354)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- NO LEAN FILE THIS ACT: zq-b730 of SIDE-explicit-formula at %s unmoved and untagged, the tag put to the author; no kernel`s main touched; no dispatch of the two allowed. SOURCE %s.' % (K.ZQ_TIP[:8], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.24.0 ((R355)(2)), by its controls
    sw = seat('%s_standing_v1240.txt' % ACT, '**v1.24.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.24.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the two plans, read from their banks
    so = seat('%s_poscontrol_plan.txt' % ACT, '**THE PLAN: pcConfig')
    keys['ORD'] = ('REGISTERED -- THE TWO PLANS: the ζ box at %s lines, %d dispatches nominal (relay data/b745_zetabox_plan.txt at %s, md5 %s); the positive control on pcConfig at %s lines, %d dispatch (data/b745_poscontrol_plan.txt at %s); neither built; %s. SOURCE %s.' % (
        f['zb_lines'], f['zb_disp'], K.C2_PLAN_FIRST[:8], K.PLAN_MD5[:8], f['pc_lines'], f['pc_disp'], K.C2_RELAY[:8], f['rec'] + ', put to the author', so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R355)(5))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b745 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
