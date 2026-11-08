# -*- coding: utf-8 -*-
# b746 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R356)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R356)(2) repair it carries. Edited by the Edit tool. Carried at b746 by tools/b746_fold.py (`carry`) from tools/acts/b745.py,
# b745`s names substituted; the citation`s sections adopted from tools/b746_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b745`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b745`s carried till
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
# ### b746, Component 1 (the Edit tool): THE c1 ROUTE FOR b745'S WEIGHT LINE AND ITS CORRIGENDUM, (R356)(1) and (3). Rewritten at b746 against
# ### b745's own banks (scratch splicefn746.py): the closing's lines by needle, the events (9), the defects (25), the refusals (24 lines),
# ### and the v1.26.0 controls this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '946cc80a'          # ### b745's closing push tip (its closing step row), the public relay's main
C1_CLOSING_COMMIT = 'b9a45896'      # ### b745's closing commit (its closing row)
C1_REFUSAL_AT = '946cc80a'          # ### its refusal bank read at its closing push tip
C1_NOTED = '2026-11-08'
C1_CORRIGENDA_LAST = 65
C1_V170 = 'b746_standing_v1260.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.26.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-08 by b746 to b745’s entry (:%d), under `(R356)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The tag v0.38 on zq-b730 at 14ca5725, no merge; W-ORD-POSITIVE-CONTROL BUILT'
C1_TRAIL_NEEDLE = '### b745 — lane two, act one hundred and seventy-two, the controls act under (R355)'
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
    for l in _c1_rd('b745_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b745_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b745_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b745_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b745_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b745_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b745_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b745_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    lost = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if k_ not in held]
    if len(held) != 6 or lost != ['N4', 'N5'] or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b745_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) REFUTED \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the record-time scores')
    ar = json.load(open(os.path.join(D, 'b745_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b745_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (pcb, zbb, dn_, dm_, pcl, pce, zbl, zbe, nc_, nn_), l_ct = _c1_fl(
        c, r'^    W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX on zq-b730: .*: W-ORD-POSITIVE-CONTROL (BUILT) ; W-ORD-ZETA-BOX (BUILT) ; DISPATCHES (\d+) OF (\d+) ; '
           r'LINES (\d+) AGAINST ([\d-]+) AND (\d+) AGAINST ([\d-]+) ; NAMES COMPILED (\d+) OF (\d+)$', 'the two controls')
    (_tg,), l_tg = _c1_fl(c, r'^### THE KERNELS: .*(the one tag v0\.38 at 14ca5725)', 'the tag')
    (va, vb), l_v = _c1_fl(c, r'^    tools/standing/ at v1\.25\.0: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.25.0 foot')
    _mv, l_mv = _c1_fl('b745_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-07-b745)\.zip ; ', 'the mirror`s archive')
    _aw1, l_aw1 = _c1_fl('b745_author_answers.txt', r'^RESULT .*="(On the root prompt first: pick the paper’s §1\.)', 'the author`s answer')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R355\)\(7\)\*\*: (per \(R355\)\(7\), named by the author)\.', 'the carried item (a)')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 10)) or len(dr) != 25 or (int(sd), int(se)) != (25, 9):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b745 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b745_closing.txt):* “%s” (data/b745_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b745_steps.json, the record and closing rows). As its rows read: %s, cut at step zero, no merge (:%d); '
            'W-ORD-POSITIVE-CONTROL %s and W-ORD-ZETA-BOX %s on zq-b730, dispatches %s of %s, lines %s against %s and %s against %s, names compiled %s of %s (:%d; relay data/b745_controls.txt). '
            'Standing tools v1.25.0, %s of %s (:%d); the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), G-AXIOM-CLAIM, G-RULE-POSTSEAL-READ and '
            'G-README-CURRENCY declared on the face; the record-time scores N3 REFUTED, the rest HELD (:%d), and at the scores’ close SCORES %d OF 8 HELD, %s REFUTED (data/b745_scores_close.json). '
            'The root %s over %s banks, chained from %s (data/b745_act_root.json; :%d); the mirror %s at %s (data/b745_mirror_verify.txt :%d; :%d); %s prompt banked as put by the seat (:%d), '
            'the author’s answer at the root “%s” (data/b745_author_answers.txt :%d); the closing’s carried item (a): %s (:%d), the author naming this act by `(R356)`. '
            '%d events in data/b745_events.txt, rows (1)-(%d), entered after the lock; %d defects, (a)–(y) (data/b745_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and '
            'defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. Nothing deposited, no merge, no tag beyond v0.38, no new Zenodo version; the corrigendum '
            'for these rows follows, under `(R356)`(3).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, _tg, l_tg, pcb, zbb, dn_, dm_, pcl, pce, zbl, zbe, nc_, nn_, l_ct,
                vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, l_sl, len(held), ' and '.join(lost),
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, _aw1[0], l_aw1, ca, l_ca, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b745's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '14:47:57Z', 'defect (c)'), (2, 'SED', '14:50:30Z', 'defect (c)'), (3, 'PIPE', '14:58:43Z', 'defect (c)'),
               (4, 'PIPE', '15:26:24Z', 'defect (f)'), (5, 'SED', '15:29:04Z', 'defect (f)'), (6, 'READ', '15:30:03Z', 'defect (f)'), (7, 'REDIR', '15:34:15Z', 'defect (f)'),
               (8, 'PIPE', '15:34:43Z', 'defect (f)'), (9, 'SED', '16:05:23Z', 'defect (g)'), (10, 'READ', '16:07:40Z', 'defect (g)'), (11, 'PIPE', '16:13:54Z', 'defect (g)'),
               (12, 'READ', '16:32:30Z', 'defect (g)'), (13, 'REDIR', '16:35:55Z', 'defect (g)'), (14, 'REDIR', '17:09:08Z', 'defect (m)'), (15, 'REDIR', '17:11:10Z', 'defect (m)'),
               (16, 'PIPE', '17:12:54Z', 'defect (m)'), (17, 'REDIR', '17:17:46Z', 'defect (p)'), (18, 'PIPE', '17:31:07Z', 'defect (p)'), (19, 'PIPE', '20:33:31Z', 'defect (x)'),
               (20, 'READ', '23:16:18Z', 'event (3)'), (21, 'READ', '23:16:19Z', 'event (3)'), (22, 'GITWRITE', '00:16:23Z', 'event (4)'), (23, 'PIPE', '00:29:57Z', 'event (7)'),
               (24, 'PIPE', '01:06:39Z', 'event (9)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing refusal of b745's: b746's hook bank opens at 01:41:45Z, every line b746's own
C1_FLIP = {}      # ### (R356)(3) flips no tag: each item read as its bank tags it
C1_CORR_TITLE = ('## Corrigendum to b745’s record (relay data/b745_events.txt rows (1)-(9) and data/b745_defects.txt): nine events and twenty-five defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the lock block in the lock commit, the one reader of the lock date, the row for every act commit, the membrane’s line from the working tree, the retried and the cached '
                 'remote read, at tools/standing/ v1.26.0, each controlled, under (R356)(3)')



def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.26.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b745_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b745_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.26.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(9)', sorted(ev) == list(range(1, 10))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 25', len(dr) == 25), ('the refusals 24, each answered as listed', len(rl) == 24 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.26.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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
    """the counter as this corrigendum reads the items: no tag flipped ((R356)(2) names none)."""
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


# ### the repairs each item is met by at v1.26.0 (the controls bank data/b746_standing_v1260.txt)
C1_EV_EXTRA = {1: '; repair (lock), `(R356)`(3)(i): reg_seal.py --lock runs inside the lock tool, the lock block in the lock commit or nothing committed',
               2: '; repair (rows), `(R356)`(3)(iii): every act commit through the commit tool, its row in the same call',
               3: '; `(R356)`(3)(vii): the hook’s READ row held, REPEAT',
               4: '; `(R356)`(3)(vii): the hook’s GITWRITE row held, the add and the commit one message each; the N5 cause',
               5: '; repair (membrane), `(R356)`(3)(iv), for its consequence in (6); the flag’s misreading REPEAT',
               6: '; repair (membrane), `(R356)`(3)(iv): the membrane’s line composed from the working tree, a stray named and deleted by the tool that refused',
               7: '; `(R356)`(3)(vii): the hook’s PIPE row held, REPEAT',
               8: '; repair (lsr), `(R356)`(3)(v): a retried read an event with its two timings, a wholly cached part CACHED and no pass; the attempt1 bank kept as the run of record',
               9: '; `(R356)`(3)(vii): the hook’s PIPE row held, REPEAT'}
C1_DF_EXTRA = {}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b746, to G-README-CURRENCY declared on b745’s face (`(R356)`(3)(vi)): the arm’s reason read from its bank, README 1 against b744’s 0 (relay data/b745_standing_figures.txt :58); '
            'the line it names, PLACE-papers README.md :164, cites the kernel at v0.37 where its tag is v0.38 (relay data/b746_standing_v1260.txt, the (readme) block); carried to a sitting on the author’s '
            'number, not brought current by this act’s hand.',
            'Dated note, b746, to event (2) and to N4 (`(R356)`(3)(ii)): b745 dated its lock twice, N4 by the face’s lock block (2959bc55, the seal commit) and the root prompt’s ceiling by hand (af0330bb); '
            'from v1.26.0 both read the lock row of data/<act>_steps.json through tools/standing/lockdate.py, and b745’s two readings replayed read af0330bb once (the (lockdate) block).')
C1_CLASSES = (
    ('lock', 'the lock block written after the lock (`(R356)`(3)(i), event (1), N4)', 'tools/standing/commit.py’s lock phase runs reg_seal.py --lock on the face its gate record names, adds the face and reads the staged blob through lock_check. b745’s face at af0330bb refused; b744’s at ae688949 accepted'),
    ('lockdate', 'the two readers of one date (`(R356)`(3)(ii))', 'tools/standing/lockdate.py, the lock row of data/<act>_steps.json, read by the act module’s N4 and by rootprompt.ceiling_at_lock. b745’s readings 2959bc55 and af0330bb replayed as af0330bb'),
    ('rows', 'the row for every act commit (`(R356)`(3)(iii), event (2), REPEAT b744 (4))', 'tools/standing/commit.py’s act phases (step zero, component N, pre-root, record, closing) take the seat’s words and write the row in the same call. eaca4c35 and e9c339ed refused by the old tool, rowed by the new'),
    ('membrane', 'the membrane’s “nothing written” that wrote one file (`(R356)`(3)(iv), events (5)-(6))', 'tools/act_membrane.py composes its line from the working tree: an untracked bank written by the refused route since it began is named and deleted by its verified absolute path. b745’s stray replayed, named and deleted'),
    ('lsr', 'the remote read retried and the cached pass (`(R356)`(3)(v), event (8))', 'tools/standing/lsrread.py classes each repository READ, RETRIED, CACHED or OVER; the suite’s arm passes a retry as an event with its two timings and counts a wholly cached part as VACUOUS, no pass. b745’s two runs read RETRIED and CACHED'),
    ('readme', 'G-README-CURRENCY declared on the face (`(R356)`(3)(vi))', 'the reason printed from its bank (README 1 at relay data/b745_standing_figures.txt :58; PLACE-papers README.md :164 at v0.37), the line carried to a sitting'),
    ('repeat', 'the hook’s refusals (`(R356)`(3)(vii), events (3), (4), (7), (9))', 'guards: the hook’s PIPE and REDIR rows; b746’s own refusals printed from its bank'),
    ('version', 'the version (`(R356)`(3)(viii))', 'tools/standing/VERSION v1.26.0, landed by a commit of its own (%s) with its controls bank' % K.C1_STANDING),
)



def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b745’s events bank (relay data/b745_events.txt) carries nine rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-five lettered rows, (a)-(y), each tagged in its own bracket (%s); its refusal bank twenty-four lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R356)`(3), at tools/standing/ v1.26.0, each with a control on b745’s or b744’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b745’s events (1)-(9):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b745_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b745’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b745_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b745’s refusals** (relay data/b745_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (nine events, twenty-five defects), as b745’s closing prints it (relay data/b745_closing.txt :5); '
          'no tag is read otherwise here; the CLAIM items %s.' % (nc, nl_, rep, n, n, ', '.join(claims) or 'none'), '',
          '*Filed at b746 on the author’s ruling `(R356)`(3): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b746.py) from '
          'b745’s events and defects banks read unedited, its refusal bank, and the v1.26.0 controls bank; banked as relay `data/b746_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b745’s record; no sealed tool, face, trail or root-named bank of b745 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    return (['b746 -- THE CORRIGENDUM FOR b745, (R356)(3) (%s)' % utc(), '',
             '### the banks read unedited: data/b745_events.txt rows (1)-(9), data/b745_defects.txt 25 rows, data/b745_hook_refusals.txt 24 '
             'lines at %s; data/%s (the v1.26.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 9, DEFECTS 25 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.26.0: THE LOCK BLOCK IN THE LOCK COMMIT, THE ONE READER OF THE LOCK DATE, '
               'THE ROW FOR EVERY ACT COMMIT, THE MEMBRANE`S LINE FROM THE WORKING TREE, THE RETRIED AND THE CACHED REMOTE READ, G-README-CURRENCY`S REASON, THE REPEAT REFUSALS, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (
                   n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b745 at its weight after its entry, and the corrigendum for b745, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.26.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; AS READ HERE %d, %d, %d OF %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, rc, rl_, rr, rn, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b746, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b746, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b746's name.
# ### b746's own changes are marked "b746, Component 3". The runner overrides read the act's dispatch rows: (R356)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b746_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R355)(7), as b745 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """N1, b746 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b746: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b746, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R356)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b745, naming tools/standing/hook.py, unedited this act (its last edit b745`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b746, Component 3 (the Edit tool): b746's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b745-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b746_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b746_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b746, Component 6 (the Edit tool): b746's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b745's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b746, Component 4 (the Edit tool): b745's overrides of checks 1516 and 1659 (hook.py edited by b745's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b746 as it stands
# ### b746, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b746_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b746, Component 4 (the Edit tool): the corrigendum's events rows (1)-(9), b745's nine (the template's range is b745's fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 10)) \
#⟪END⟫
# ### b746, Component 4 (the Edit tool): b745's override of checks 1476-1482 (one ERRATA entry at b745's (R355)(5)) removed -- (R356)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b746 as it stands
# ### b746, Component 3 (the Edit tool): G-BRANCHES-DELETED over b746's two repositories (relay, PLACE-papers) and five
# ### refs; the step-zero bank writes "KEPT as banked:" (data/b746_stepzero.txt :33), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b746, Component 4 (the Edit tool): G-RUNNER-READ's plant on b746's dispatch rows -- run 2's axiom lines carrying sorryAx (b745's
# ### plant read the lv rows' closure log, which b746 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b746, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b746, Component 6 (the Edit tool): the fold bank was b745's own route
# ### (tools/b745_fold.py); b746's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b746_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b745.py -> tools/acts/b746.py' in (rd('b746_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b746, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b746_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b746, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b746_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b746_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b746, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R356): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R356)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b746')
    return '### THE COUNTER ((R356) Component 5, the act`s events and defects together; relay data/b746_defects.txt, data/b746_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b745, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b746 (defect (d')): the order's
# ### state as b746 leaves it -- the carry from b745 said "as b745 left it ... not touched this act", where b746 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX, entered at b745, built this act on zq-b730 (relay data/b746_controls.txt); W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as b745 entered them;',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b746, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b745's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b746, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b745's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b746_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b746_registration_%s.txt' % __import__('b746_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b746, Component 4 (the Edit tool, before the face): b745's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b746, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b746's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b746, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R356)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b746 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b746_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b746: the controls' one route (N1)
#⟪END⟫
# ### b746, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b745's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b746 scorer reads; the needles set to the banks b746's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b746, (R356)(2)(iii): b745's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b746, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b746_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijkl')))   # ### (a)-(l), entered before the lock, every one the seat's (data/b746_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b746_corrigendum.txt', 'data/b746_standing_v1260.txt', 'data/b746_section1.txt', 'data/b746_integration_draft.txt', 'data/b746_order_draft.txt',
                  'data/b746_pathrefusal.txt',
                  'data/b746_reproduce.txt', 'data/b746_reproduce.json', 'data/b746_address_scan.txt', 'data/b746_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b746 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R356)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b746_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R356)(4): the sitting bank's rows by label -- a row opens `[A1] STATE`, `[C] STATE`, `[(7)] ...` at column 0, its fields indented two
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
        # ### (R356)(2)-(4) (b746's keys over b746's objects): the order by time and ancestry; v1.25.0's controls; the two plan banks (b745's,
        # ### read at their step-zero md5s); the controls bank and its notes; zq-b730 and the tag; v8 and v9; the address scan; the reproduction
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b745's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR),
                                 ('corr_s1', K.C1_CORR, K.C2_RELAY), ('s1_c3', K.C2_RELAY, K.C3_RELAY[0]))),
        # ### b746 (R356)(2)-(6): the order within PLACE-papers by ancestry -- the two discharges, the weight and corrigendum, section 1, the line
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('d1_d2', K.C1_DISCHARGE_PP[0], K.C1_DISCHARGE_PP[1]), ('d2_c1', K.C1_DISCHARGE_PP[1], K.C1_PP),
                                   ('c1_s1', K.C1_PP, K.C2_PP), ('s1_c3', K.C2_PP, K.C3_PP))),
        v1130=rd('b746_standing_v1260.txt'), plan=read(os.path.join(ROOT, *K.PLAN_BANK.split('/'))), print_=read(os.path.join(ROOT, *K.POSCONTROL_PLAN.split('/'))),
        controls=rd('b746_section1.txt'), notes=rd('b746_integration_draft.txt'), rows_bank=rd('b746_order_draft.txt'), sittingj={}, amendj={},
        plan_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.PLAN_BANK))), print_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.POSCONTROL_PLAN))),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in K.C1_DISCHARGE_PP + (K.C1_PP, K.C2_PP, K.C3_PP)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in K.C1_DISCHARGE_PP),
        paper=read(os.path.join(PP, *K.SECTION_FILE.split('/'))), paper_pre=_s(blob(PP, '%s:%s' % (K.PRE_PP, K.SECTION_FILE))),
        paper_at=_s(blob(PP, '%s:%s' % (K.C2_PP, K.SECTION_FILE))),
        reg_now_pp=read(os.path.join(PP, 'REGISTRY.md')), reg_pre_pp=_s(blob(PP, '%s:REGISTRY.md' % K.PRE_PP)),
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
        drows=json.loads(rd('b746_dispatch_rows.json') or '[]'), reproduce=rd('b746_reproduce.txt'), reproducej=jl('b746_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b746_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b745 left them
        rebuild=None, rebuild_rows=json.loads(rd('b746_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               d1=_ct(PP, K.C1_DISCHARGE_PP[0]), d2=_ct(PP, K.C1_DISCHARGE_PP[1]), s1pp=_ct(PP, K.C2_PP), s1=_ct(ROOT, K.C2_RELAY),
               c3pp=_ct(PP, K.C3_PP), c3=_ct(ROOT, K.C3_RELAY[0]), print=_ct(ROOT, K.PRINT_COMMIT),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), s1=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY[0]),
                   s1pp=files_of(PP, K.C2_PP), c3pp=files_of(PP, K.C3_PP),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b746's read-first bank's items by path, as its step zero wrote them (data/b746_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b745_closing.txt |', 'relay data/b745_events.txt |', 'relay data/b745_defects.txt |', 'relay data/b745_controls.txt |',
                     'relay data/b744_poscontrol_plan.txt (md5 b72ad7bb) |', 'relay data/b744_zetabox_plan.txt (md5 ef777cc2) |', 'relay data/b743_sitting.txt |',
                     'relay data/b725_interference.txt |', 'relay data/b729_c2.txt |', 'PLACE-papers REGISTRY.md at 1967382 |', 'PLACE-papers SPIRAL_MAP.md at 1967382 |',
                     'SIDE-explicit-formula at v0.38 (14ca5725) |', 'SIDE-kernel at v1.5 (0e5233f0) |', 'relay tools/b746_worklist.py stage one;')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R356)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'PAPER`S §1 ((R356)(4))', 'ORDER AND THE LINE ((R356)(5)-(6))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (150 = 150 + 0, data/b746_citation_check.txt); the check CLEAN;
    the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 150 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b746, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b745's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b746, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b745()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b746_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b745's figures, read at FINDINGS :14067 as Component 1 landed them
    return landed(S, 0, ['b745 AT ITS WEIGHT', 'suite 113 of 116', 'relay 3f7752c0', '25 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b746's title in the ferry's Component 4 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX discharged on pc_online and zeta_box at v0.38; ',
                 'THE_EPSTEIN_CONTROL_OBJECT §1 passed, 893 words, 26 cites; ',
                 'W-ORD-MECHANISM-ATTRIBUTION ',
                 '; the lock tool, the one reader and 6 repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R356)(1), (3): the generated entry for b745's nine events and twenty-five defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(9), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 17, CLOSE 17 over 34, REPEAT 19); the repairs at tools/standing/ v1.26.0 by their controls
    bank; the corrigenda bank appended at row (66) and nothing before it changed; in Component 1's commits (the figures read from
    data/b746_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 25 and len(items) == j.get('items') == 34 and j.get('row') == 66 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 34 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 17 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 19 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.26.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 \
        and '  (66) ' in S['corrigenda'] and '  (67) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R356) orders no rules bank: data/b746_rules.txt is not written (none of (R356)'s items a rule row), and
#⟪END⟫
#⟪SECTION checks 21⟫
    no author's word of b746 orders a row of the next act's, so data/b747_rules.txt does not exist either."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and not os.path.exists(os.path.join(D, 'b746_rules.txt')) and not os.path.exists(os.path.join(D, 'b747_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b746's keys, the report sections' own heads
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.26.0', 'REGISTERED -- THE PAPER`S §1', 'REGISTERED -- W-ORD-POSITIVE-CONTROL AND W-ORD-ZETA-BOX DISCHARGED',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b746: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = bool(seq_) and all(
        sum(1 for x in seq_ if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) == 1
        and seq_.index(d) < next(i for i, x in enumerate(seq_) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run')))
        for d in seq_ if d.get('kind') == 'dispatch')   # ### N1: each dispatch read once after it by its run id
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b746_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b746, N1: six rows, six dispatch commands
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, b745's INTEGRATION line, the
    entry; OPEN_TRAILS: the two discharges, the trail and the order on the author's number; the paper's section 1), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b746's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The discharges**', '**The paper’s §1**', '**The order**', '**The integration line**',
                 '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b746_corrigendum.txt', 'data/b746_standing_v1260.txt', 'data/b746_section1.txt', 'data/b746_integration_draft.txt', 'data/b746_order_draft.txt',
                 'data/b746_reproduce.txt', 'data/b746_address_scan.txt', 'data/b746_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP §2D), no seat in the cluster table ; keystone none yet ; stage BANKED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b746: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R356)(2), N2 (the name the frozen run list carries): the two discharges, each a PLACE-papers commit touching OPEN_TRAILS alone, each
    adding its one DISCHARGED line and removing none, the positive control's before the box's; both before section 1's PLACE-papers write
    and before its relay commit; the order in PLACE-papers by ancestry (the discharges, the weight and corrigendum, section 1, the line); the
    plans of b744 unedited at their step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    t_ = S['t']
    dd_ = S['disch_diff'] or {}
    adds_ = [[l for l in (dd_.get(h_) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()] for h_ in K.C1_DISCHARGE_PP]   # ### the added blank separator lines not counted as the first add
    rems_ = [[l for l in (dd_.get(h_) or '').split(NL) if l.startswith('-') and not l.startswith('---')] for h_ in K.C1_DISCHARGE_PP]
    one_ = len(adds_) == 2 and adds_[0][:1] and adds_[0][0].startswith('+**`W-ORD-POSITIVE-CONTROL` DISCHARGED') \
        and adds_[1][:1] and adds_[1][0].startswith('+**`W-ORD-ZETA-BOX` DISCHARGED') and rems_ == [[], []]
    files_ = [S['reg_pp'].get(h_) for h_ in K.C1_DISCHARGE_PP]
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    return bool(one_) and files_ == [['OPEN_TRAILS.md'], ['OPEN_TRAILS.md']] and md_ \
        and all(t_.get(k_) for k_ in ('d1', 'd2', 's1pp', 's1')) and t_['d1'] <= t_['d2'] < t_['s1pp'] <= t_['s1'] \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b746_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R356)(2)-(6), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, the two discharges, v1.26.0,
    the weight and corrigendum (PLACE-papers, then relay), section 1 (PLACE-papers, then its sitting bank's relay commit), the integration line
    (PLACE-papers, then relay); by ancestry within the relay v9, v1.26.0, the corrigendum, section 1's bank, Component 3's commit."""
    t_ = S['t']
    ks_ = ('stepzero', 'd1', 'd2', 'standing', 'c1pp', 'corr', 's1pp', 's1', 'c3pp', 'c3')
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values())
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R356)(4), N2, N3 (the name the frozen run list carries): section 1's bank -- the draft between its BEGIN and END lines, every cite
    printed from its source before the sitting item, its foot CITES 26 and WORDS 893 with the version line v0.1 kept; [S1] passed with the
    author's clause, the one write at PLACE-papers C2_PP; the section at PLACE-papers HEAD equal word for word to the bank's draft with the
    author's clause, its heading at its place, the other headings standing empty, the version line v0.1 and the act's dated note beneath it;
    the file's lines before the section equal to its blob at the act's base but the note; nothing of the file changed after C2_PP."""
    t = S['controls'] or ''
    v = _vlast(t)
    dr_ = t[t.find(' BEGIN\n') + len(' BEGIN\n'):t.find('### THE SECTION AS DRAFTED END')] if ' BEGIN\n' in t else ''
    pp_ = (S['paper'] or '').replace(chr(13), '')
    i_ = pp_.find('\n## 1. ')
    j_ = pp_.find('\n## 2.', i_ + 1)
    body_ = pp_[i_ + 1:j_] if i_ >= 0 and j_ > i_ else ''
    words_ = len(' '.join(body_.split(NL)[1:]).split())
    heads_ = re.findall(r'(?m)^## (\d)\. ', pp_)
    empty_ = all(not pp_[pp_.find('\n## %d.' % k_):].split('\n## ')[1].split(NL, 1)[1].strip() for k_ in range(2, 10) if ('\n## %d.' % k_) in pp_)
    pre_ = (S['paper_pre'] or '').replace(chr(13), '').split(NL)
    now_ = pp_.split(NL)
    note_ = [l for l in now_[:8] if l.startswith('*Dated note') and 'b746' in l]
    return 'CITES 26 ; WORDS 893 (whitespace-separated) ; ITS PLACE :5 ; THE VERSION LINE v0.1 KEPT' in t \
        and v == "[S1] PASSED WITH THE AUTHOR'S CLAUSE: §1 WRITTEN, 893 WORDS, 26 CITES, PLACE-papers %s." % K.C2_PP[:8] \
        and t.find('### EVERY CITE, PRINTED FROM ITS SOURCE') < t.find('[S1] PASS') and bool(dr_) \
        and bool(body_) and words_ == 893 and heads_ == [str(k_) for k_ in range(1, 10)] and empty_ \
        and now_[2:3] == pre_[2:3] and now_[2].startswith('*v0.1') and len(note_) == 1 \
        and (S['paper_at'] or '').replace(chr(13), '') == pp_ and S['files']['s1pp'] == [K.SECTION_FILE]
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R356)(8) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b745 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b745's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
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
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.18.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b745's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R356)(6), N3 (the name the frozen run list carries): the integration line -- b745's INTEGRATION line appended at the foot of b745's
    entry by Component 3's PLACE-papers commit, FINDINGS the one file, adding the dated note and the line and removing nothing; the line the
    draft's (D) composes for b745 (stage CLUSTERED, keystone none yet), its rows read from REGISTRY (1.5c-21 to 1.5c-23) and its block from
    SPIRAL_MAP (2D); the draft's foot naming nothing written to the canon; the order draft carrying the entry and the defect it reads."""
    n_ = S['notes'] or ''
    o_ = S['rows_bank'] or ''
    d_ = gs(PP, 'show', '--format=', '-U0', K.C3_PP)
    add_ = [l for l in d_.split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    rem_ = [l for l in d_.split(NL) if l.startswith('-') and not l.startswith('---')]
    line_ = 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP §2D), no seat in the cluster table ; keystone none yet ; stage CLUSTERED'
    rg_ = (S['reg_now_pp'] or '').replace(chr(13), '').split(NL)
    return S['files']['c3pp'] == ['FINDINGS.md'] and not rem_ and len(add_) == 2 and add_[-1][1:].rstrip() == line_ and add_[0][1:].startswith('*Appended 2026-11-08 by b746') \
        and line_ in n_ and 'stage BANKED' in n_ and 'NOTHING WRITTEN TO THE CANON' in _vlast(n_) \
        and all(any(l.startswith('| %s | The Epstein instance' % r) for l in rg_) for r in ('1.5c-21', '1.5c-22', '1.5c-23')) \
        and '`W-ORD-MECHANISM-ATTRIBUTION` ENTERED at b746' in o_ and 'MechanismClass' in o_


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
    """standing clauses v9 (Component 7 of (R356): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b746_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b745's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R356-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b745's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R356) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b745's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R355)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base b41fa006',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 150 = 150 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b745-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 form: the two discharges on pc_online and zeta_box at v0.38; §1 passed with its words and cites; W-ORD-MECHANISM-ATTRIBUTION entered or carried; the lock tool, the one reader and v1.26.0`s further repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R356)(1), (3): the generated corrigendum for b745`s record, landed at FINDINGS :14069: its nine events and twenty-five defects, 34 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 17 CLOSE 17, REPEAT 19; v1.26.0`s repairs by data/b746_standing_v1260.txt; the corrigenda bank appended at row (66)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R356) orders no rules bank: no data/b746_rules.txt and no data/b747_rules.txt',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b746's objects
    ('G-REGISTRATIONS-FIRST', '(R356)(2), N2: the two discharges, each a PLACE-papers commit touching OPEN_TRAILS alone, adding its one DISCHARGED line and removing none, the positive control`s first; both before section 1`s write and its sitting bank`s commit; the PLACE-papers order by ancestry; the plans of b744 at their step-zero md5s',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'ancpp', lambda d: d.update(c1_s1=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b746_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R356)(2)-(6), N2: the act`s order by time -- step zero, the two discharges, v1.26.0, the weight and corrigendum, section 1, the integration line -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_s1=False))),
    ('G-DERIVATION-GRADED', '(R356)(4), N2, N3: section 1`s bank -- the draft, every cite printed from its source before the sitting item, CITES 26 and WORDS 893, the version line kept; [S1] passed with the author`s clause and written at PLACE-papers; the section at HEAD 893 words under its heading, the other headings empty, the version line v0.1 with the act`s dated note, nothing changed since the write',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'controls', (S['controls'] or '').replace('WORDS 893', 'WORDS 894'))),
    ('G-OFFSET-POST-HOC', 'N5, (R356)(8): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 946cc80a, VERSION 9; v8 at HEAD its blob at 946cc80a; no v10; v9`s commit an ancestor of v1.26.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R356)(6), N3: b745`s INTEGRATION line at the foot of its entry (PLACE-papers b7544123, FINDINGS alone, the dated note and the line, nothing removed), the line the draft composes, REGISTRY`s rows 1.5c-21 to 1.5c-23 read; the draft naming nothing written to the canon; the order draft carrying the entry',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'notes', (S['notes'] or '').replace('NOTHING WRITTEN TO THE CANON', 'THE CANON WRITTEN'))),
    ('G-DIFFERS-ERRATA', '(R356)(1), (3): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at the act`s base, no differs or errata bank, the worklist naming no line or id; the weight line and the corrigendum in 32ce8322, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b746_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R356-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b745`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b745 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b745 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS, OPEN_TRAILS and the paper`s section 1, (R356)(2)-(6)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b745`s trail record on OPEN_TRAILS (:17820) and its root in the chain', lambda S: '### b745 — lane two, act one hundred and seventy-two, the controls act under (R355)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the paper`s section 1): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b746 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b745's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b746: (R356)'s rows, set at step zero by the splice route (scratch splice746.py). (1)'s line read by the ruling from the public relay at 946cc80a
    pub = _blob('D:/relay', '946cc80a', 'data/b745_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b745_closing.txt :1, the head line as the public relay carries it at 946cc80a', bool(pub) and pub[0] == at(cl, 1) and 'relay 3f7752c0' in pub[0] and 'PLACE-papers 1967382' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 113 of 116', 'root c831a2103261ed73', '1 prompt answered', 'scores 6 of 8 HELD', '25 defects'):
        add('ruling (1)', 'data/b745_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    EF_ = 'D:/SIDE-explicit-formula'
    tg_ = (gr(EF_, 'rev-parse', 'v0.38') or '').strip()
    tp_ = (gr(EF_, 'rev-parse', 'v0.38^{}') or '').strip()
    add('ruling (1)', 'the tag v0.38 on SIDE-explicit-formula, tag object 21c6edaf, its peel 14ca5725', tg_.startswith('21c6edaf') and tp_.startswith('14ca5725'), '%s ; %s' % (tg_[:8], tp_[:8]), '1')
    em_ = (gr(EF_, 'rev-parse', 'main') or '').strip()
    add('ruling (1), (8)', 'SIDE-explicit-formula main at 8fbab45, unmoved (no merge)', em_.startswith('8fbab45'), em_[:8], '1')
    rgl_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    for n_, r_ in ((177, '1.5c-21'), (178, '1.5c-22'), (179, '1.5c-23')):
        add('ruling (scope), ferry (read first)', 'REGISTRY.md :%d, row %s, an Epstein row' % (n_, r_), at(rgl_, n_).startswith('| %s | The Epstein instance' % r_), at(rgl_, n_)[:60], '1')
    add('ruling (scope), (1)', 'REGISTRY.md :1244, the dated note naming the tag v0.38 to rows 1.5c-21, -22, -23', at(rgl_, 1244).startswith('*Dated note, b745, 2026-11-07') and 'v0.38' in at(rgl_, 1244), at(rgl_, 1244)[:60], '1')
    sml_ = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (1), ferry (read first)', 'SPIRAL_MAP.md :546, the 2D block`s dated note naming the tag v0.38', at(sml_, 546).startswith('*Dated note, b745, 2026-11-07') and 'v0.38' in at(sml_, 546), at(sml_, 546)[:60], '1')
    co_ = lines_of(p('data', 'b745_controls.txt'))
    for n_, w_ in ((43, 'pcCarrier_finite'), (48, 'pc_count'), (49, 'pc_ne_zero'), (51, 'pc_li_nonneg'), (52, 'pc_online'), (96, 'zM_re_bounds'), (107, 'zeta_sign_16'),
                   (116, 'zeta_sign_12'), (120, 'zeta_box_of_signs'), (121, 'zeta_box')):
        add('ruling (1), (2)', 'data/b745_controls.txt :%d, %s with the standard three' % (n_, w_), ('.' + w_ + ' ') in at(co_, n_) and '[propext, Classical.choice, Quot.sound]' in at(co_, n_), at(co_, n_)[:60], '1')
    add('ruling (1), (2)', 'data/b745_controls.txt :52 and :121, runs 42388609600 and 42393914259', '42388609600' in at(co_, 52) and '42393914259' in at(co_, 121), 'read', '1')
    add('ruling (1), (2)', 'data/b745_controls.txt :123, the dependency print of pc_online`s closure', at(co_, 123).startswith('## P6: THE DEPENDENCY PRINT'), at(co_, 123)[:60], '1')
    add('ruling (1), (2)', 'data/b745_controls.txt :125, the generic theorem Wide.li_nonneg_cfg_imp_online_ne_zero by name in the closure', 'li_nonneg_cfg_imp_online_ne_zero by name in the closure: True' in at(co_, 125), at(co_, 125)[-40:], '1')
    add('ruling (1), (2)', 'data/b745_controls.txt :126, no constant of Z_Q', at(co_, 126).rstrip().endswith('NONE') and 'constants of Z_Q' in at(co_, 126), at(co_, 126)[-30:], '1')
    add('ruling (1), (2)', 'data/b745_controls.txt :127, the finiteness constants read by hand', 'finiteness' in at(co_, 127), at(co_, 127)[:60], '1')
    add('ruling (1)', 'data/b745_controls.txt :237, the four statements COMPILED', all(('%s COMPILED' % w_) in at(co_, 237) for w_ in ('pc_count', 'pc_ne_zero', 'pc_li_nonneg', 'pc_online')), at(co_, 237)[:60], '1')
    add('ruling (1)', 'data/b745_controls.txt :238, SPZ1-SPZ3 REACHED, BUILT', all(('SPZ%d REACHED' % k_) in at(co_, 238) for k_ in (1, 2, 3)) and at(co_, 238).rstrip().endswith('BUILT'), at(co_, 238)[:60], '1')
    for w_ in ('DISPATCHES 6 OF 12', 'LINES 129 AGAINST 108-290 AND 663 AGAINST 450-1100', 'NAMES COMPILED 82 OF 82'):
        add('ruling (1)', 'data/b745_controls.txt :241 carries %s' % w_, w_ in at(co_, 241), at(co_, 241)[:60], '1')
    cn_ = rd(p('data', 'b745_controls_notes.txt')) or ''
    add('ruling (1)', 'data/b745_controls_notes.txt notes (9), (12): intermediate_value_Ioo where the plan named the closed form; SPZ1 at dispatch 4', 'intermediate_value_Ioo' in cn_ and '(12)' in cn_, 'read', '1')
    sv_ = lines_of(p('data', 'b745_standing_v1250.txt'))
    add('ruling (1)', 'data/b745_standing_v1250.txt :131, v1.25.0, CASES 20 ; AS WANTED 20', 'v1.25.0' in at(sv_, 131) and 'CASES 20 ; AS WANTED 20' in at(sv_, 131), at(sv_, 131)[:60], '1')
    ck_ = lines_of(p('data', 'b745_checks.txt'))
    add('ruling (1)', 'data/b745_checks.txt :16, 116 run, 113 passing, G-AXIOM-CLAIM, G-RULE-POSTSEAL-READ and G-README-CURRENCY failing',
        "ARMS RUN : 116. ### LIVE PASSING : 113. ### LIVE FAILING : 3 ['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-README-CURRENCY']" in at(ck_, 16), at(ck_, 16)[:60], '1')
    sc9_ = _jl('b745_scores_close.json')
    held_ = sorted(k_ for k_, v_ in sc9_.items() if isinstance(v_, list) and v_[:1] == ['HELD'])
    ref_ = sorted(k_ for k_, v_ in sc9_.items() if isinstance(v_, list) and v_[:1] == ['REFUTED'])
    add('ruling (1)', 'data/b745_scores_close.json, 6 of 8 HELD, N4 and N5 REFUTED', len(held_) == 6 and ref_ == ['N4', 'N5'], 'HELD %d ; REFUTED %s' % (len(held_), ' '.join(ref_)), '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b745']]
    add('ruling (1)', 'data/act_roots.txt, b745`s root c831a210 chained from b744`s 3c30761b', len(ar9_) == 1 and ar9_[0][1].startswith('c831a210') and ar9_[0][2].startswith('3c30761b'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    b3_ = rd(p('data', 'b745_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b659-b745 (b745`s post-push part b3)', 'b745 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b745 AGREE' if 'b745 AGREE' in b3_ else 'ABSENT', '1')
    mv_ = rd(p('data', 'b745_mirror_verify.txt')) or ''
    add('ruling (1)', 'data/b745_mirror_verify.txt, CLEAN ON ALL THREE CLAUSES', 'CLEAN ON ALL THREE CLAUSES' in mv_, 'CLEAN' if 'CLEAN ON ALL THREE CLAUSES' in mv_ else 'ABSENT', '1')
    add('ruling (1)', 'data/b745_closing.txt, the mirror mirror-refresh-2026-11-07-b745', 'mirror-refresh-2026-11-07-b745' in NL.join(cl), 'read', '1')
    aa_ = rd(p('data', 'b745_author_answers.txt')) or ''
    add('ruling (1), (2), (5)', 'data/b745_author_answers.txt, the author`s word at the root: the paper`s §1, the two discharges at (R356), W-ORD-MECHANISM-ATTRIBUTION on the number',
        'pick the paper’s §1' in aa_ and 'W-ORD-MECHANISM-ATTRIBUTION as an order on your number' in aa_, 'read', '1')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.26.0's commit's parent once it lands, HEAD's blob before
    add('ruling (3)', 'tools/standing/VERSION v1.25.0 entering the act', v0_ == 'v1.25.0', v0_, '1')
    for f_ in ('data/b745_relay_push-b745-closing_push_out.txt', 'tools/mirror_prevbuild.json'):
        add('ruling (3)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (3), ferry (read first)', 'events (1)-(9) and 25 defects (data/b745_events.txt, data/b745_defects.txt)',
        starts == list(range(1, 10)) and len(letters) == 25, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    ev = lines_of(p('data', 'b745_events.txt'))
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    for n_, k_, w_ in ((4, 1, "THE SEAT'S [CLAIM ; NEW]"), (5, 2, "THE SEAT'S [CLAIM ; REPEAT b744 (4)]"), (8, 3, "THE SEAT'S [CLOSE ; REPEAT b744 (c)]"),
                       (11, 4, "THE SEAT'S [CLOSE ; NEW]"), (14, 5, "THE SEAT'S [CLOSE ; REPEAT b744 (6)]"), (15, 6, "THE TOOLS' [CLAIM ; NEW]"),
                       (16, 7, "THE SEAT'S [CLOSE ; REPEAT b744 (c)]"), (17, 8, "THE TOOLS' [CLAIM ; NEW]"), (20, 9, "THE SEAT'S [CLOSE ; REPEAT b744 (c)]")):
        add('ruling (3), ferry (read first)', 'data/b745_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    for n_, w_ in ((4, 'reg_seal.py --lock'), (5, 'e9c339ed'), (5, 'eaca4c35'), (11, 'one message'), (15, 'NOTHING WRITTEN'), (17, 'G-LSREMOTE-ONE-PER-REPO'), (17, 'run cache')):
        add('ruling (3), ferry (read first)', 'data/b745_events.txt :%d carries %s' % (n_, w_), w_ in at(ev, n_), at(ev, n_)[:60], '1')
    for c_ in ('e9c339ed', 'eaca4c35', 'af0330bb', '2959bc55', '8e67907e'):
        add('ruling (3)', 'relay %s, the commit the events name' % c_, bool(gr('D:/relay', 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')), gr('D:/relay', 'log', '-1', '--format=%s', c_)[:60], '1')
    add('ruling (3)(vi)', 'data/b745_standing_figures.txt, G-README-CURRENCY`s reason (the README line the arm names)', 'README' in (rd(p('data', 'b745_standing_figures.txt')) or ''), 'read', '1')
    add('ferry (read first)', 'data/b745_closing.txt, its CARRIED items beneath the head', any('CARRIED' in l for l in cl), 'read', '0')
    pc_ = lines_of(p('data', 'b744_poscontrol_plan.txt'))
    for n_, w_ in ((49, '## (b) THE CARRIER AND THE STATEMENT'), (57, '    theorem pc_count : Wide.HCount pcConfig 2'), (58, '    theorem pc_ne_zero :'),
                   (59, '    theorem pc_li_nonneg : ∀ n : ℕ, 0 ≤ Wide.liCoeff pcConfig n'), (60, '    theorem pc_online : ∀ ρ ∈ pcConfig.carrier, ρ.re = 1 / 2 :='),
                   (61, '      Wide.li_nonneg_cfg_imp_online_ne_zero pcConfig pc_count pc_ne_zero pc_li_nonneg')):
        add('ruling (2), ferry (read first)', 'data/b744_poscontrol_plan.txt :%d carries %s' % (n_, w_.strip()[:50]), at(pc_, n_).startswith(w_), at(pc_, n_)[:60], '1')
    zb_ = lines_of(p('data', 'b744_zetabox_plan.txt'))
    for n_, w_ in ((26, '## (a) THE OBJECT AND THE STATEMENT'), (32, '  THE STATEMENT (Mathlib'), (33, '    theorem zeta_box : ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ ρ.re = 1 / 2 ∧ (12 : ℝ) < ρ.im ∧ ρ.im < 16'),
                   (37, '    zeta_sign_12'), (38, '    zeta_sign_16')):
        add('ruling (2), ferry (read first)', 'data/b744_zetabox_plan.txt :%d carries %s' % (n_, w_.strip()[:50]), at(zb_, n_).startswith(w_), at(zb_, n_)[:60], '1')
    import hashlib as _hl
    for f_, md_ in sorted(K.PLAN_MD5S.items()):
        by_ = open(p(*f_.split('/')), 'rb').read() if os.path.exists(p(*f_.split('/'))) else b''
        add('ruling (2)', '%s at its b745 step-zero md5 %s, unrewritten' % (f_, md_[:8]), _hl.md5(by_).hexdigest() == md_ and not gr('D:/relay', 'status', '--porcelain', '--', f_), _hl.md5(by_).hexdigest()[:8], '1')
    st_ = lines_of(p('data', 'b743_sitting.txt'))
    add('ferry (read first)', 'data/b743_sitting.txt :155-:158, the [D] rows: the skeleton`s headings D1-D9 passed', at(st_, 155).startswith('[D] PASS, D0-D9') and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in at(st_, 156), at(st_, 155)[:60], '2')
    SK_ = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'
    sk_ = lines_of(os.path.join(PP, *SK_.split('/')))
    skm_ = _blob(PP, '1967382', SK_).replace(chr(13), '').split(NL)
    add('ruling (4), ferry (read first)', '%s at the b745 mirror (PLACE-papers 1967382), equal to the tree' % SK_, bool(sk_) and skm_[:len(sk_)] == sk_, '%d lines' % len(sk_), '2')
    add('ruling (4)', '%s :5, the heading of section 1, its body empty' % SK_, at(sk_, 5).startswith('## 1. The object: Q0, Z_Q, Λ_Q, the class group of order 3, ζ_K and L(ψ), the identities') and at(sk_, 7).startswith('## 2.'), at(sk_, 5)[:60], '2')
    add('ruling (4)', '%s :3, the version line v0.1' % SK_, at(sk_, 3).startswith('*v0.1, a skeleton'), at(sk_, 3)[:40], '2')
    it_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (4), ferry (read first)', 'data/b725_interference.txt :8, r_Q0 + 2 r_Q1 = 2 SUM (-23/d), mismatches 0', at(it_, 8).startswith('  (C1) n = 1..3000, exact: r_Q0 + 2 r_Q1') and 'mismatches 0' in at(it_, 8), at(it_, 8)[:60], '2')
    add('ruling (4), ferry (read first)', 'data/b725_interference.txt :9, (r_Q0 - r_Q1)/2 equal to eta(z) eta(23z)`s coefficients, mismatches 0', at(it_, 9).startswith('  (C1) (r_Q0 - r_Q1)/2') and 'mismatches 0' in at(it_, 9), at(it_, 9)[:60], '2')
    add('ruling (4), ferry (read first)', 'data/b725_interference.txt :31, zeta_K = Z_Q1 = -2 L(psi) at a zero (FORCED)', 'zeta_K(rho) = Z_Q1(rho) = -2 L(rho, psi) (FORCED)' in at(it_, 31), at(it_, 31)[-50:], '2')
    c2_ = lines_of(p('data', 'b729_c2.txt'))
    add('ferry (read first)', 'data/b729_c2.txt :45, THE C2 THEOREM', 'THE C2 THEOREM' in at(c2_, 45), at(c2_, 45)[:60], '2')
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (7)', 'zq-b730 past v0.38 at 1e658870 (b745`s last Lean commit), kept', zt_.startswith('1e658870'), zt_[:8], '1')
    for f_, n_, w_ in (('SIDEExplicitFormula/Schema/ZQ/Continuation.lean', 147, 'theorem zqFn_holomorphic'),
                       ('SIDEExplicitFormula/Schema/ZQ/Continuation.lean', 122, 'def zqFn (s : ℂ) : ℂ :='),
                       ('SIDEExplicitFormula/Schema/ZQ/Continuation.lean', 77, '    zqPair.Λ s = Complex.Gamma s * qBase ^ (-s) * ZQ s'),
                       ('SIDEExplicitFormula/Schema/ZQ/Zeros.lean', 319, 'def zqZeroConfig : WideConfig where'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 18, 'set of zeros. THE CARRIER IS STRIP-FREE'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 137, 'structure ZQPremises'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 142, '  count : ∃ A₀ : ℝ, Wide.HCount Z A₀'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 45, 'def Q0form (m n : ℤ) : ℤ := m ^ 2 + m * n + 6 * n ^ 2'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 69, 'def ZQ (s : ℂ) : ℂ := LSeries'),
                       ('SIDEExplicitFormula/Schema/EpsteinZQ.lean', 72, 'def qBase : ℂ := ((2 * Real.pi / Real.sqrt 23 : ℝ) : ℂ)'),
                       ('SIDEExplicitFormula/Schema/ZQ/EF/Xi.lean', 26, 'def lamQ : ℂ → ℂ := zqPair.Λ'),
                       ('SIDEExplicitFormula/Schema/ZQ/OffZero/Split.lean', 29, 'def lamM (w : ℂ) : ℂ := mellin thA w'),
                       ('SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 32, 'theorem zq_offline_zero : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1 / 2')):
        bl_ = _blob(EF_, 'v0.38', f_).replace(chr(13), '')
        add('ruling (4), (5), ferry (read first)', '%s at v0.38 :%d carries %s' % (f_, n_, w_.strip()[:50]), at(bl_.split(NL), n_).startswith(w_), at(bl_.split(NL), n_)[:60] if bl_ else 'ABSENT', '2')
    SKD_ = 'D:/SIDE-kernel'
    skt_ = (gr(SKD_, 'rev-parse', 'v1.5^{}') or '').strip()
    add('ruling (5), ferry (read first)', 'SIDE-kernel v1.5 at 0e5233f0', skt_.startswith('0e5233f0'), skt_[:8], '3')
    bc_ = _blob(SKD_, 'v1.5', 'Bridge/TheBridgeComplete.lean').replace(chr(13), '').split(NL)
    for n_, w_ in ((20, 'inductive MechanismClass where'), (21, '  | C1_schwarz | C2_euler | C3_functional_eq'), (22, '  | C4_modular | C5_spectral | C6_cauchy_riemann | C7_hadamard'),
                   (25, 'theorem seven_classes : Fintype.card MechanismClass = 7 := by decide')):
        add('ruling (5), ferry (read first)', 'SIDE-kernel Bridge/TheBridgeComplete.lean at v1.5 :%d carries %s' % (n_, w_.strip()[:50]), at(bc_, n_).startswith(w_), at(bc_, n_)[:60], '3')
    add('ruling (1)', 'FINDINGS :%d, b745`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## '), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b745`s weight line and corrigendum, the form b746`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fi, K.B711_WEIGHT)) and bool(at(fi, K.B711_CORRIGENDUM)), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b745`s trail record, its hand section' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b745 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (2)', 'OPEN_TRAILS :%d, b745`s open-orders line, W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX open' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**')
        and '`W-ORD-POSITIVE-CONTROL`' in at(ot, K.TRAIL_ORDERS) and '`W-ORD-ZETA-BOX`' in at(ot, K.TRAIL_ORDERS), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('ruling (scope)', 'the census THE_KEYSTONE_CENSUS_v0_8_3.md at 36 kernels', '36' in NL.join(lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))[:40]), 'read', '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.25.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.25.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R356)(4): b745's export, the mirror's last
    add('ruling (4)', '%s, b745`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R356)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b745-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R356)(3), (7): act_current alone, then b745's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b745_relay_push-b745-closing_push_out.txt'])):   # ### b746: no terminal table carried (b745 left none)
        if c_ is K.STEPZERO:   # ### tools/mirror_prevbuild.json: a CRLF-only difference from HEAD's blob a94aa543, restored by checkout, nothing to commit
            add('ruling (3)', 'tools/mirror_prevbuild.json at HEAD`s blob a94aa543 (a CRLF-only difference restored at step zero, no commit)',
                gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json').startswith(gr('D:/relay', 'rev-parse', 'HEAD:tools/mirror_prevbuild.json')[:12]), 'blob %s' % gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json')[:8], '0')
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
    add('ferry (read first)', 'data/b746_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b746_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b746 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b745_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.26.0's controls, section 1's sitting bank and the integration draft, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R356)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R356)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R356)(8): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b746 ((R356)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R355)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b746 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTY-THREE, THE OBJECT: b745 AT ITS WEIGHT AND ITS CORRIGENDUM; '
              'W-ORD-POSITIVE-CONTROL AND W-ORD-ZETA-BOX DISCHARGED; v1.26.0; THE PAPER`S §1; THE INTEGRATION LINE, UNDER (R356).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b745's sections over b745's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.26.0: the lock block inside the lock tool, the one reader of the lock date, the row for every act commit, the membrane`s strays, the remote read classed, the README reason, the refusals repeat, the version, each case failing before its repair and passing after', 'b746_standing_v1260.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE PAPER`S §1 ((R356)(4))', [
                ('section 1 drafted, every cite printed from its source, put as one sitting item, the verdict and the one write', 'b746_section1.txt'),
                ('the probe-path refusal printed before the lock gate', 'b746_pathrefusal.txt')]),
            ('THE ORDER AND THE LINE ((R356)(5)-(6))', [
                ('the stages and the two INTEGRATION lines drafted, nothing written to the canon', 'b746_integration_draft.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b746_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b745`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b746_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R355)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R356)(8)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b745 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b745-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the discharges committed before section 1 was put, every cite of section 1 printed from its source before the sitting, the tools` controls before their figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit ;',
    '    N3: section 1 claims no result, every object cited to a definition at v0.38 or a bank line ; nothing new of ζ, nothing of RH or h2 ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b746_address_scan.txt, data/b746_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo field touched ; the deposit route untouched, publish never called, the draft held at v5 ; no GitHub description written ; no door or record edited ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, b745`s INTEGRATION line, the entry), OPEN_TRAILS (the two discharges, the trail' + (', the order' if WL.C3_ORDER_PP else '') + '), the paper`s §1 (' + WL.SECTION_FILE + ') ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b746`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.26.0 by (R356)(3) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b745 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R356)(9)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the paper`s §1 written (relay data/b746_section1.txt), §2-§9 empty ; the stages` canon text drafted (relay data/b746_integration_draft.txt) ;',
    '        W-ORD-MECHANISM-ATTRIBUTION`s entry drafted (relay data/b746_order_draft.txt) ; orders.py reading a quotation as an open order (relay data/b746_defects.txt (e)) ; the README line at v0.37 carried to a sitting ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b746_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b745 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b746: the standing repairs are v1.26.0's ((R356)(3), relay data/b746_standing_v1260.txt, read in the corrigendum section); the
    # ### carry's diffs here (b746 carried at step zero before the fold; its tools since are the templates and tools/acts/b746.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b745 left them; port-b707 at b712`s tip %s)' % (
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
    b746's form over b746's objects: the corrigendum's foot and v1.26.0's controls; section 1's sitting bank (its draft foot and its [S1]
    verdict, the words and the cites); the integration draft's foot; the order draft and the order's state at the author's number; the citation
    check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure;
    the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1260.txt' % ACT, r'\*\*v1\.26\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.26.0`s controls')
    s1d_ = _bfig('%s_section1.txt' % ACT, r'\*\*§1 DRAFTED: CITES (\d+) ; WORDS (\d+) \(whitespace-separated\) ; ITS PLACE :(\d+) ; THE VERSION LINE (v[\d.]+) KEPT ;', 'section 1`s draft foot')
    s1v_ = _bfig('%s_section1.txt' % ACT, r"\*\*\[S1\] (PASSED WITH THE AUTHOR'S CLAUSE|PASSED|STRUCK)(?:: §1 WRITTEN, (\d+) WORDS, (\d+) CITES, PLACE-papers ([0-9a-f]{7,8}))?\.\*\*", 'the sitting`s verdict on [S1]')
    ig_ = _bfig('%s_integration_draft.txt' % ACT, r'\*\*\(A\) THE LINE ; \(B\) (\w+) STAGES DRAFTED ;.*\(D\) (\w+) LINES: b745 (\w+), b746 (\w+), KEYSTONE (NONE YET) FOR BOTH ; NOTHING WRITTEN TO THE CANON\.\*\*', 'the integration draft`s foot')
    od_ = _bfig('%s_order_draft.txt' % ACT, r'(\*\*`W-ORD-MECHANISM-ATTRIBUTION` ENTERED at b746)', 'the order draft`s entry')
    reps_ = v5[0].split(', ')
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], repairs=len(reps_),
                s1_cites=int(s1d_[0]), s1_words=int(s1d_[1]), s1_place=int(s1d_[2]), s1_version=s1d_[3],
                s1_state=('passed' if s1v_[0].startswith('PASSED') else 'struck'), s1_clause=(s1v_[0] == "PASSED WITH THE AUTHOR'S CLAUSE"), s1_pp=s1v_[3],
                ig_stages=ig_[0], ig_b745=ig_[2], ig_b746=ig_[3], ig_keystone=ig_[4],
                order_state=('entered' if K.C3_ORDER_PP else 'carried'), order_pp=K.C3_ORDER_PP,
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R356)(3): the kernel rows of one kind as banked (data/b746_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R356): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b746_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b746_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b746's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b746_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b746_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b746_standing_v1260.txt', '## THE CONTROLS', '### the instances read at their commits'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, section 1: in its bank the cites printed from their sources before the sitting item, the sitting's verdict before the one write
N2_SECTION = ('data/b746_section1.txt', '### THE SECTION AS DRAFTED (written verbatim under :5 on a pass) BEGIN',
              '### EVERY CITE, PRINTED FROM ITS SOURCE', '### THE SITTING (b736`s form), one item:'.replace('`', "'"))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R356): the two discharges committed (PLACE-papers, OPEN_TRAILS alone each) before section 1 is written and before its sitting
    bank is committed; in the section's bank every cite printed from its source before the sitting item; each tool's controls before its
    figures; the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate. Step zero, the discharges, v1.26.0,
    the weight and corrigendum, section 1 and the integration line in that order by time; v1.26.0 an ancestor of the section's relay commit."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (PP, K.C1_DISCHARGE_PP[0]), (PP, K.C1_DISCHARGE_PP[1]), (ROOT, K.C1_STANDING), (PP, K.C1_PP),
              (ROOT, K.C1_RELAY), (PP, K.C2_PP), (ROOT, K.C2_RELAY), (PP, K.C3_PP), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.C2_RELAY], capture_output=True).returncode == 0
    dfiles_ = [sorted(x for x in g(PP, 'show', '--name-only', '--format=', h_).split() if x.strip()) for h_ in K.C1_DISCHARGE_PP]
    disch_ = dfiles_ == [['OPEN_TRAILS.md'], ['OPEN_TRAILS.md']]
    sb_ = rdn(N2_SECTION[0])
    ix_ = [sb_.find(w_) for w_ in N2_SECTION[1:]]
    sect_ = all(i_ >= 0 for i_ in ix_) and ix_ == sorted(ix_) and "[S1] PASS" in sb_[ix_[2]:]
    route_ = disch_ and sect_
    same_ = True
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the two discharges (PLACE-papers %s, %s) each OPEN_TRAILS alone: %s; in the section`s bank (relay %s) the draft, every cite printed from its source, then the sitting item, in that order, [S1] passed: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, the discharges, v1.26.0, the weight and corrigendum, section 1 and the integration line in that order by time: %s (%s), v1.26.0 an ancestor of the section`s relay commit: %s; the tools` controls before their figures: %s' % (
            K.C1_DISCHARGE_PP[0][:8], K.C1_DISCHARGE_PP[1][:8], disch_, N2_SECTION[0], sect_, regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b746's objects; b745's in git at b745's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b746_standing_v1260.txt', ('ALL AS WANTED',)), ('b746_section1.txt', ('[S1] PASSED', '893 WORDS', '26 CITES')),
             ('b746_integration_draft.txt', ('KEYSTONE NONE YET FOR BOTH', 'NOTHING WRITTEN TO THE CANON')),
             ('b746_corrigendum.txt', ('ITEMS',)), ('b746_citation_check.txt', ('THE CHECK CLEAN',)), ('b746_reproduce.txt', ('REPRODUCES',)), ('b746_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### (R356)(6): the entry's last line, the INTEGRATION line, as b746's draft composes it (relay data/b746_integration_draft.txt (D)), read from REGISTRY and SPIRAL_MAP
INTEGRATION_LINE = 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP §2D), no seat in the cluster table ; keystone none yet ; stage BANKED'
FIXED_SENTENCES = ()   # ### b746: no fixed sentence ordered by (R356)


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()


def _section1_body():
    """the paper's section 1 as PLACE-papers carries it at HEAD: the lines from its heading to the next heading."""
    t = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '')
    i = t.find('\n## 1. ')
    j = t.find('\n## 2.', i + 1)
    return t[i + 1:j] if i >= 0 and j > i else ''
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R356): section 1 claims no result and every object in it is cited, its cites printed from their sources in its bank (26, each a
    Lean line at v0.38 or a relay bank line); no sentence of section 1 or of the entry saying the box is the earliest of its kind in any
    assistant; no sentence naming zeta, RH or h2 as moved outside a negation; the entry's INTEGRATION line its last line, reading REGISTRY's
    rows 1.5c-21 to 1.5c-23 and SPIRAL_MAP's 2D block as they stand; the root prompt's sentences about the entry the composer's. From the
    banks' last lines, the section as PLACE-papers carries it, the entry's sentences and the root prompt in the answers bank."""
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
    s1_ = _section1_body()
    sb_ = rdn('%s_section1.txt' % ACT)
    reg_ = sb_[sb_.find('### EVERY CITE'):sb_.find('### ### **§1 DRAFTED')]
    cites_ = re.findall(r'(?m)^  (\S+)\s+:(\d+)\s+(.*)$', reg_)   # ### each printed line: its source, its line, its text

    def _src_line(f_, n_):
        if f_.endswith('.lean'):
            s_ = _show(K.EF_DIR, K.ZQ_TAG[0], 'SIDEExplicitFormula/Schema/%s' % f_) or ''
        else:
            s_ = rd(os.path.join(ROOT, *f_.split('/'))) or ''
        s_ = s_.replace(chr(13), '').split(NL)
        return s_[int(n_) - 1] if 0 < int(n_) <= len(s_) else None
    cbad_ = [(f_, n_) for f_, n_, x_ in cites_ if _src_line(f_, n_) is None
             or not (_src_line(f_, n_).strip().startswith(x_.strip()) or x_.strip().startswith(_src_line(f_, n_).strip()))]
    s1sents_ = [s for s in re.split(r'(?<=[.;])\s+', ' '.join(s1_.split())) if s]
    res_ = [s for s in s1sents_ if re.search(r'\b(?:we prove|is proved|we show|this paper proves|a new result|for the first time)\b', s, re.I)]
    first_ = [s for s in s1sents_ + sents if re.search(r'\b(?:first|earliest)\b', s, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', s)]
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    loc_ = [s_ for s_ in s1sents_ + sents if re.search(r'\b(?:RH|GRH|h2|ζ)\b.*\b(?:holds|fails|proved|refuted|moved)\b', s_) and not re.search(neg_, s_)]
    lines_ = [l for l in text.split(NL) if l.strip()]
    rg_ = (rd(os.path.join(PP, 'REGISTRY.md')) or '').replace(chr(13), '').split(NL)
    sm_ = rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''
    integ_ = bool(lines_) and lines_[-1].strip() == INTEGRATION_LINE \
        and all(any(l.startswith('| %s | The Epstein instance' % r) for l in rg_) for r in ('1.5c-21', '1.5c-22', '1.5c-23')) and '2D' in sm_
    sp_ = bool(s1_) and bool(cites_) and not cbad_ and f['s1_cites'] == 26 and f['s1_state'] == 'passed' and not res_
    fixed_ = []
    nouns_ = [w_ for w_ in ('W-ORD-POSITIVE-CONTROL', 'W-ORD-ZETA-BOX', 'pc_online', 'zeta_box', 'v0.38', str(f['s1_words']), str(f['s1_cites']),
                            'data/%s_section1.txt' % ACT, 'data/%s_integration_draft.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and sp_ and not first_ and not loc_ and integ_ and not nouns_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; section 1 at PLACE-papers HEAD present, its bank printing %d source lines for the %s cites its foot names, each re-read against its source (Lean at v0.38, banks in the relay), not as printed: %s, [S1] %s, a sentence of it claiming a result: %s (relay data/b746_section1.txt): %s; read from %s, a sentence of section 1 or the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY 1.5c-21 to 1.5c-23 and SPIRAL_MAP`s 2D read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), len(cites_), f['s1_cites'], cbad_ or 'NONE', f['s1_state'], res_ or 'NONE', sp_, src, first_ or 'NONE', loc_ or 'NONE', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R356) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R356)(5))
# ### (R356)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R356)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
    # ### same reader the ceiling takes; the face's `locked at (UTC)` line no longer dates it
    import lockdate as LD
    lc = LD.lock_of(ACT, os.path.join(ROOT, 'data'))
    lock = LD.lock_epoch(lc, ROOT) if lc else None
    out = dict(lock=lock, lock_iso=None, lock_commit=lc, after=[], edited=[], dirty=[])
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
    # ### (R356) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b745's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b746, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b745's face
# ### read them; (R356)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
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
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R356)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R356)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b745 left them; the address scan's count from its bank (relay data/b746_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R356)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R356)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R356)(5), N5: no Zenodo write, no release, no new version, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    ghe_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+release\b|/actions/newversion|zenodo\.org/api|\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b746_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a Zenodo route or a repository`s edit in the capture: %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b746 — lane two, act one hundred and seventy-three, the object under (R356): b745 at its weight and its corrigendum; the two '
            'discharges; v1.26.0; the paper’s §1 %s; W-ORD-MECHANISM-ATTRIBUTION %s' % (_figs()['s1_state'], _figs()['order_state']))
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects in the ferry's Component 4 form ("W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX discharged on pc_online
    and zeta_box at v0.38; THE_EPSTEIN_CONTROL_OBJECT §1 <passed | struck>, <w> words, <c> cites; W-ORD-MECHANISM-ATTRIBUTION <entered |
    carried>; the lock tool, the one reader and <r> repairs landed"); every figure from the banks (section 1's foot and its sitting verdict,
    v1.26.0's controls) and the order's state from the worklist's C3_ORDER_PP (set on the author's number alone)."""
#⟪END⟫
#⟪SECTION record 31⟫
    reps_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if 'lock' not in reps_ or 'lockdate' not in reps_:
        sys.exit('### v1.26.0`S CONTROLS DO NOT NAME (lock) AND (lockdate) -- NOTHING COMPOSED')
    dis_ = [l_ for l_ in (rd(os.path.join(PP, 'OPEN_TRAILS.md')) or '').split(NL) if l_.startswith('**`W-ORD-POSITIVE-CONTROL` DISCHARGED') or l_.startswith('**`W-ORD-ZETA-BOX` DISCHARGED')]
    if len(dis_) != 2:
        sys.exit('### OPEN_TRAILS CARRIES %d DISCHARGE LINES OF THE TWO, NOT 2 -- NOTHING COMPOSED' % len(dis_))
    return ('## W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX discharged on pc_online and zeta_box at v0.38; THE_EPSTEIN_CONTROL_OBJECT §1 %s, %d words, %d cites; '
            'W-ORD-MECHANISM-ATTRIBUTION %s; the lock tool, the one reader and %d repairs landed' % (
                f['s1_state'], f['s1_words'], f['s1_cites'], f['order_state'], len(reps_) - 2))   # ### v1.26.0's eight less (lock) and (lockdate), named before it
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) section 1`s three wrong line cites and its uncited class number found by the cite printer before the sitting and corrected, the sitting seeing the corrected draft alone (relay data/b746_section1.txt :47-:83, defect (g)); (2) the author`s clause at [S1] applied as given, the draft`s two check phrases replaced by the author`s words and nothing else changed (relay data/b746_section1.txt :89-:99); (3) tools/standing/orders.py reading W-ORD-MECHANISM-ATTRIBUTION as open from a quotation in b745`s trail before any entry stands, carried and not repaired (defect (e)); (4) G-README-CURRENCY`s reason (README.md :164 citing v0.37 where the tag is v0.38) carried to a sitting, not edited (relay data/b745_standing_figures.txt :58); '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R356)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b746's objects; b745's composer in git at
    b745's record tool). Its last line the INTEGRATION line ((R356)(6))."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot, not a row quoting another act's (b746 defect (a'))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R355)(2)(v)
    ot_ = (rd(os.path.join(PP, 'OPEN_TRAILS.md')) or '').replace(chr(13), '').split(NL)
    fi_ = (rd(os.path.join(PP, 'FINDINGS.md')) or '').replace(chr(13), '').split(NL)
    dl_ = [i_ + 1 for i_, l_ in enumerate(ot_) if l_.startswith('**`W-ORD-POSITIVE-CONTROL` DISCHARGED') or l_.startswith('**`W-ORD-ZETA-BOX` DISCHARGED')]
    il_ = [i_ + 1 for i_, l_ in enumerate(fi_) if l_.startswith('INTEGRATION: cluster the Epstein instance') and l_.rstrip().endswith('stage CLUSTERED')]
    sk_ = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '').split(NL)
    h1_ = [i_ + 1 for i_, l_ in enumerate(sk_) if l_.startswith('## 1. ')]
    h2_ = [i_ + 1 for i_, l_ in enumerate(sk_) if l_.startswith('## 2. ')]
    dn_ = [i_ + 1 for i_, l_ in enumerate(sk_) if l_.startswith('*Dated note') and 'b746' in l_]
    vl_ = [l_ for l_ in sk_[:4] if l_.startswith('*v0.1')]
    if len(dl_) != 2 or len(il_) != 1 or len(h1_) != 1 or len(h2_) != 1 or len(dn_) != 1 or len(vl_) != 1:
        sys.exit('### THE LINES THE ENTRY CITES DO NOT READ ONCE EACH (discharges %s, b745`s line %s, the headings %s %s, the dated note %s, the version line %d) -- NOTHING COMPOSED' % (
            dl_, il_, h1_, h2_, dn_, len(vl_)))
    e = ['', _title(), '',
         'The two controls of the instrument built at b745 are discharged from the open trail on pc_online and zeta_box at v0.38, each by a commit of its own, and the paper’s §1 is written: the object, Q0 and its Epstein zeta function Z_Q with the objects around it, in %d words and %d cites, passed at one sitting item%s; it claims no result, each object in it cited to a definition at v0.38 or to a relay bank line. W-ORD-MECHANISM-ATTRIBUTION is %s.' % (
             f['s1_words'], f['s1_cites'], ' with the author’s clause' if f['s1_clause'] else '', 'entered on the author’s number' if f['order_state'] == 'entered' else 'carried, the author’s number not given'), '',
         '*Filed at b746 on the author’s ruling `(R356)`; %d question%s put before the root. Banks: relay '
         '`data/b746_corrigendum.txt`, `data/b746_standing_v1260.txt`, `data/b746_section1.txt`, `data/b746_integration_draft.txt`, `data/b746_order_draft.txt`, `data/b746_prelock.txt`, `data/b746_pathrefusal.txt`, '
         '`data/b746_reproduce.txt`, `data/b746_address_scan.txt`, `data/b746_touch.txt`, `data/b746_standing_figures.txt`, `data/b746_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R356)(1), (3); %s, %s, %s): b745 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b745’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b746_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b746_standing_v1260.txt): the lock block written inside the lock tool, the lock date read by one reader, and %d further repairs.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], f['repairs'] - 2), '',
         '**The discharges** ((R356)(2)): W-ORD-POSITIVE-CONTROL and W-ORD-ZETA-BOX discharged at OPEN_TRAILS :%d and :%d (PLACE-papers %s, %s), each OPEN_TRAILS alone in a commit of its own, each read from b745’s pushed bank (relay data/b745_controls.txt): pc_online and zeta_box, each with the standard three, at zq-b730 past the tag v0.38.' % (
             dl_[0], dl_[1], K.C1_DISCHARGE_PP[0][:8], K.C1_DISCHARGE_PP[1][:8]), '',
         '**The paper’s §1** ((R356)(4), N3): %s, its heading at :%d and its body to :%d, the other headings standing empty; the version line v0.1 kept with a dated note at :%d; %d words and %d cites, every cite printed from its source before the sitting (relay data/b746_section1.txt); the sitting item [S1] %s%s; one PLACE-papers write (%s). No Lean definition of Q1, the class group, ζ_K or L(s, ψ) stands at v0.38: those enter as relay data/b725_interference.txt reads them.' % (
             K.SECTION_FILE, h1_[0], h2_[0] - 2, dn_[0], f['s1_words'], f['s1_cites'], f['s1_state'], ' with the author’s clause' if f['s1_clause'] else '', K.C2_PP[:8]), '',
         '**The order** ((R356)(5)): W-ORD-MECHANISM-ATTRIBUTION %s -- the located zero of Z_Q0 attributed to a class of SIDE-kernel v1.5’s seven, or the printed finding that no class admits it; the entry drafted with its cites printed from SIDE-kernel v1.5 and SIDE-explicit-formula v0.38 (relay data/b746_order_draft.txt)%s.' % (
             f['order_state'], (', written at PLACE-papers %s' % f['order_pp'][:8]) if f['order_pp'] else ', unwritten'), '',
         '**The integration line** ((R356)(6)): b745’s entry carries its INTEGRATION line at FINDINGS :%d (PLACE-papers %s), stage %s; this entry carries its own beneath it; the canon text for the stages drafted at relay data/b746_integration_draft.txt, not in the canon; the keystone %s, the maps naming none for the instance.' % (
             il_[0], K.C3_PP[:8], f['ig_b745'], f['ig_keystone'].lower()), '',
         '**The order of the act** (N2): the two discharges committed before section 1 was put; every cite of section 1 printed from its source before the sitting; v1.26.0 at %s, the weight and the corrigendum at PLACE-papers %s and relay %s; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b746_prelock.txt, data/b746_pathrefusal.txt); the lock block in the lock commit. No lean process on this host and no runner dispatch.' % (
             K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8]), '',
         '**What this act is not**: no deposit, no new version, no draft published, no kernel’s main touched, no branch merged, no tag beyond v0.38, no Zenodo field touched, no Lean file written, no door or record edited. Section 1 is exposition of compiled definitions: nothing new of ζ, nothing of RH or h2.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b746_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b746_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b746_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b746 -- %s, %s, %s, %s -- against b745’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b746_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the discharges and section 1 read one way: the two controls closed on the instrument where the answer is known, and section 1 names the one object the instrument is pointed at, each object by its compiled definition, so the paper’s later sections have their object fixed before any result is stated.', '',
         '**Carried to:** %s, per (R356)(9), as the author names it; W-ORD-MECHANISM-ATTRIBUTION %s; orders.py’s reading of a quotation as an open order (defect (e)); the README line carried to a sitting; the instruments NOT RUN, each with its price; the draft held at v5.' % (
             K.NEXT_ACT, 'entered' if f['order_state'] == 'entered' else 'carried'), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds, and nothing here is new of ζ.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b745():
    """b745's form over b745's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b746's objects; b745's composer in git at b745's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the two discharges, section 1, the order's state and the integration line."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R356) ratified.** Its components as the ferry orders them (relay data/b746_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b745’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS the two discharges (PLACE-papers %s, %s)%s; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.C1_DISCHARGE_PP[0][:8], K.C1_DISCHARGE_PP[1][:8],
                 ('; W-ORD-MECHANISM-ATTRIBUTION (PLACE-papers %s)' % f['order_pp'][:8]) if f['order_pp'] else ''), '',
             '**The section:** the paper’s §1 at %s, %d words and %d cites, [S1] %s%s at one sitting item (PLACE-papers %s; relay data/b746_section1.txt).' % (
                 K.SECTION_FILE, f['s1_words'], f['s1_cites'], f['s1_state'], ' with the author’s clause' if f['s1_clause'] else '', K.C2_PP[:8]), '',
             '**The order:** W-ORD-MECHANISM-ATTRIBUTION %s (relay data/b746_order_draft.txt).' % f['order_state'], '',
             '**The integration line:** b745’s at FINDINGS (PLACE-papers %s), stage %s; b746’s at the foot of its entry, stage %s; the stages’ canon text drafted at relay data/b746_integration_draft.txt, not in the canon.' % (
                 K.C3_PP[:8], f['ig_b745'], f['ig_b746']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output; its reading of W-ORD-MECHANISM-ATTRIBUTION from a quotation is defect (e) (relay data/b746_defects.txt).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b746_standing_v1260.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b746_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b746_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b746_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b746 `%s` (previous `%s`, b745’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b746_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b746_standing_v1260.txt); the standing '
             'report tool (relay data/b746_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b745 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b746_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b745’s %s, %s, %s, %s (relay data/b746_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b746_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b745():
    """b745's trail record over b745's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b745 left them, the six; MEASURED off the six kernels` refs/heads.'),
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
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b745-closing, push-b745-preroot, push-b745-record; PLACE-papers push-b745-preroot, push-b745-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b746_stepzero.txt :29-:32).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY untouched this act.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R356)(3): FINDINGS :14069.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R356)(3): row (66).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none: (R356) orders none.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none with the trail: the two discharges by commits of their own ((R356)(2)); W-ORD-MECHANISM-ATTRIBUTION by a commit of its own on the author`s number, or carried ((R356)(5)).'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b746_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.26.0`s controls, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none this act: no registered object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R356)(8)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R356)(3): tools/standing/ to v1.26.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b746_address_scan.txt (the address never printed).'),
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
    # ### b746: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b746_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b746_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1260', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b746_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b746_registration_%s.txt -- b746, THE OBJECT: b745 AT ITS WEIGHT AND ITS CORRIGENDUM; W-ORD-POSITIVE-CONTROL AND W-ORD-ZETA-BOX DISCHARGED; "
                             "v1.26.0; THE PAPER`S §1; THE INTEGRATION LINE; NO DEPOSIT, NO LEAN, UNDER (R356)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b745's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b746: b745's lines read banks this
act does not write, and are not carried; the lines are b746's: tools/standing/ v1.26.0 by its controls (CERTIFIED), the two discharges, the
paper's section 1 by its sitting and the integration line (REGISTERED), and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b746's lines, each from the record tool's figures over b746's banks
    # ------------------------------------------------------------------ REGISTERED: (R356)(4), the paper's section 1, read from its sitting bank
    sz = seat('%s_section1.txt' % ACT, "**[S1] PASSED")
    sk = sz   # ### (R355)(2)(ii): the name the template appends
    keys['S1'] = ('REGISTERED -- THE PAPER`S §1 at PLACE-papers %s: %d words, %d cites, every cite printed from its source; [S1] %s%s at one sitting item; the version line %s kept with a dated note. SOURCE %s.' % (
        K.SECTION_FILE, f['s1_words'], f['s1_cites'], f['s1_state'], ' with the author`s clause' if f['s1_clause'] else '', f['s1_version'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.26.0 ((R356)(3)), by its controls
    sw = seat('%s_standing_v1260.txt' % ACT, '**v1.26.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.26.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the two discharges ((R356)(2)) and the integration line ((R356)(6))
    so = seat('%s_integration_draft.txt' % ACT, 'stage CLUSTERED')
    keys['ORD'] = ('REGISTERED -- W-ORD-POSITIVE-CONTROL AND W-ORD-ZETA-BOX DISCHARGED on OPEN_TRAILS at PLACE-papers %s and %s, each a commit of its own; b745`s INTEGRATION line at FINDINGS (PLACE-papers %s), stage %s, keystone %s; W-ORD-MECHANISM-ATTRIBUTION %s. SOURCE %s.' % (
        K.C1_DISCHARGE_PP[0][:8], K.C1_DISCHARGE_PP[1][:8], K.C3_PP[:8], f['ig_b745'], f['ig_keystone'].lower(), f['order_state'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R356)(8))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1120']), ('REGISTERED', ['S1', 'ORD']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b746 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
