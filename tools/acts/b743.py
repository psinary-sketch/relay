# -*- coding: utf-8 -*-
# b743 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R353)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R353)(2) repair it carries. Edited by the Edit tool. Carried at b743 by tools/b743_fold.py (`carry`) from tools/acts/b742.py,
# b742`s names substituted; the citation`s sections adopted from tools/b743_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b742`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b742`s carried till
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
# ### b743, Component 1 (the Edit tool): THE c1 ROUTE FOR b742'S WEIGHT LINE AND ITS CORRIGENDUM, (R353)(1) and (3). Rewritten at b743 against
# ### b742's own banks: the closing's lines by needle, the events (6), the defects (19), the refusals (25 lines, two of them b741's slips), the
# ### build's grade, the v1.22.0 controls, and the v1.23.0 controls this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '16a36428'          # ### b742's closing commit
C1_REFUSAL_AT = '16a36428'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-06'
C1_CORRIGENDA_LAST = 62
C1_V170 = 'b743_standing_v1230.txt'   # ### (carried name) the controls bank of the repairs this corrigendum lands
C1_WEIGHT_HEAD = '*Appended 2026-11-06 by b743 to b742’s entry (:%d), under `(R353)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-OFFLINE-ZERO, S6: the route on Λ_Q by'
C1_TRAIL_NEEDLE = '### b742 — lane two, act one hundred and sixty-nine'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


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
    for l in _c1_rd('b742_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b742_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b742_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b742_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b742_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b742_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b742_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b742_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    refd = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'REFUTED']
    if len(held) != 8 or refd or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b742_scores_close.json: HELD %s, REFUTED %s -- NOTHING COMPOSED' % (held, refd))
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the record-time scores')
    ar = json.load(open(os.path.join(D, 'b742_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b742_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    gr, l_gr = _c1_fl('b742_offlinezero.txt', r'^### ### \*\*SP4 (REACHED) ; DISPATCHES (\d+) OF (\d+) ; LINES (\d+) AGAINST ([\d-]+) \(THE CEILING (\d+)\) ; NAMES (\d+) OF (\d+)\.\*\*$', 'the build`s grade')
    _s1, l_s1 = _c1_fl('b742_offlinezero.txt', r'^\s+G6\s+(zq_offline_zero)\s', 'the first statement`s axiom line')
    _s2, l_s2 = _c1_fl('b742_offlinezero.txt', r'^\s+G6\s+(zq_li_nonneg_fails)\s', 'the second statement`s axiom line')
    (bb, bp), l_bb = _c1_fl('b742_offlinezero.txt', r"B = (120)\b.*in place of the plan[’'`]s (7\.8004)", 'the far circle`s bound')
    (pl1,), l_pl1 = _c1_fl('b742_s6_plan.txt', r'^b742 -- W-ORD-ZQ-OFFLINE-ZERO, S6, THE PLAN, .*: (COMMITTED BEFORE ANY LEAN OF b742) ', 'the plan`s head')
    (aw0,), l_aw0 = _c1_fl('b742_author_answers.txt', r'^(The author’s word amending \(R352\)\(3\))', 'the author`s word')
    (va, vb), l_v = _c1_fl('b742_standing_v1220.txt', r'^### ### \*\*v1\.22\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*$', 'the v1.22.0 foot')
    _mv, l_mv = _c1_fl('b742_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'(mirror-refresh-2026-11-05-b742)\.zip ; ', 'the mirror`s archive')
    _aw, l_aw = _c1_fl('b742_author_answers.txt', r'^  (OPTION 1: Land as composed) ::', 'the author`s answer, as put')
    _aw13, l_aw13 = _c1_fl('b742_author_answers.txt', r'^RESULT .*="(Land as composed)"', 'the author`s answer, as given')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R352\)\(6\)\*\*: (per \(R352\)\(6\), named by the author)\.$', 'the carried item (a)')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != [1, 2, 3, 4, 5, 6] or len(dr) != 19 or (int(sd), int(se)) != (19, 6):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b742 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b742_closing.txt):* “%s” (data/b742_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b742_steps.json, the record and closing rows). As its rows read: S6 planned in relay data/b742_s6_plan.txt, '
            '%s (:%d), on Λ_Q by interpolation by %s (data/b742_author_answers.txt :%d); built on SIDE-explicit-formula’s zq-b730 to %s: SP4 %s, %s of %s dispatches, %s lines against %s '
            '(the ceiling %s not approached), names %s of %s (data/b742_offlinezero.txt :%d), %s and %s each on the standard three (:%d, :%d); the far circle’s bound B = %s in place of the plan’s %s (:%d). '
            'Standing tools v1.22.0, %s of %s (data/b742_standing_v1220.txt :%d); the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), '
            'G-AXIOM-CLAIM and G-RULE-POSTSEAL-READ failing, both declared on the face; SCORES %d OF 8 HELD (data/b742_scores_close.json; the closing’s score line :%d); '
            'the option the author took at the root prompt “%s” (data/b742_author_answers.txt :%d, the answer :%d). '
            'The root %s over %s banks, chained from %s (data/b742_act_root.json; :%d); '
            'the mirror %s at %s (data/b742_mirror_verify.txt :%d; :%d); %s prompts banked as put by the seat (:%d); the closing’s carried item (a): %s (:%d), the author naming this act by `(R353)`. '
            '%d events in data/b742_events.txt, rows (1)-(%d); %d defects, (a)–(s) '
            '(data/b742_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'The draft at v5; nothing deposited, no new Zenodo version; the corrigendum for these rows follows, under `(R353)`(3).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, pl1.lower().replace('lean', 'Lean'), l_pl1, aw0.replace('The author’s', 'the author’s').replace('(R352)(3)', '`(R352)`(3)'), l_aw0,
                _c1_git('rev-parse', 'refs/heads/zq-b730', repo='D:/SIDE-explicit-formula').strip()[:8], gr[0], gr[1], gr[2], gr[3], gr[4], gr[5], gr[6], gr[7], l_gr, _s1[0], _s2[0], l_s1, l_s2, bb, bp, l_bb,
                vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                len(held), l_sl, _aw[0].replace('OPTION 1: ', ''), l_aw, l_aw13,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, ca, l_ca, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b742's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row); :1-:2 are b741's slips, recorded
# ### by b742's corrigendum (FINDINGS :13619, its rule (4) and event (5))
C1_REFUSALS = [(1, 'READ', '07:24:51Z', 'b742’s corrigendum (b741’s post-closing slip, its rule (4))'), (2, 'GITWRITE', '07:26:03Z', 'b742’s corrigendum (b741’s event (5), entered there)'),
               (3, 'READ', '13:50:36Z', 'defect (b)'), (4, 'READ', '13:50:36Z', 'defect (b)'), (5, 'PIPE', '13:50:44Z', 'defect (b)'),
               (6, 'PIPE', '13:52:10Z', 'defect (c)'), (7, 'READ', '13:55:12Z', 'defect (c)'), (8, 'PIPE', '13:59:33Z', 'defect (c)'), (9, 'PIPE', '14:15:52Z', 'defect (c)'),
               (10, 'READ', '14:33:18Z', 'defect (e)'), (11, 'REDIR', '14:51:48Z', 'defect (e)'),
               (12, 'READ', '15:21:00Z', 'defect (i)'), (13, 'SED', '15:21:18Z', 'defect (i)'), (14, 'READ', '15:25:53Z', 'defect (i)'), (15, 'READ', '15:25:53Z', 'defect (i)'),
               (16, 'READ', '15:25:54Z', 'defect (i)'), (17, 'PIPE', '15:35:04Z', 'defect (i)'), (18, 'READ', '15:57:36Z', 'defect (i)'), (19, 'READ', '16:04:33Z', 'defect (i)'),
               (20, 'READ', '17:10:42Z', 'defect (n)'), (21, 'PIPE', '17:20:16Z', 'defect (n)'), (22, 'READ', '17:22:05Z', 'defect (n)'),
               (23, 'REDIR', '18:54:26Z', 'defect (p)'), (24, 'PIPE', '18:56:13Z', 'defect (p)'), (25, 'PIPE', '23:57:29Z', 'event (6)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing event of b742's: b743's hook bank opens at 02:25:57Z, every line b743's own
C1_FLIP = {5: 'REPEAT of b727 event (13)'}   # ### (R353)(3)(iv): the hold's instance, tagged NEW in b742's bank, printed REPEAT (the (repeat) case)
C1_CORR_TITLE = ('## Corrigendum to b742’s record (relay data/b742_events.txt rows (1)-(6) and data/b742_defects.txt): six events and nineteen defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the root prompt’s remote figures, the commit tool taking no subject text, the push tool’s pre-check, the hold and the hook as REPEAT, the dispatch’s '
                 'targets and labels, the “=” file’s origin and the citation reader’s label, at tools/standing/ v1.23.0, each controlled, under (R353)(3)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.23.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b742_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at[:8] not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        if not (row.startswith('defect') or row.startswith('event')):
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if 'hook' not in src.lower() and at[:5] not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b742_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.23.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(6)', sorted(ev) == [1, 2, 3, 4, 5, 6]), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 19', len(dr) == 19), ('the refusals 25, each answered as listed', len(rl) == 25 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.23.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the hold`s instance tagged NEW in its bank', tags[5][1] == 'NEW'),
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
    """the counter as this corrigendum reads the items: event (5) REPEAT of b727 event (13) ((R353)(3)(iv))."""
    nc, nl_, rep, n = _c1_counts(s)
    flip = sum(1 for k_ in C1_FLIP if s['tags'][k_][1] == 'NEW')
    return nc, nl_, rep + flip, n


def _c1_owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v_, k_.lower().replace("'s", '’s')) for k_, v_ in sorted(c.items(), key=lambda kv: -kv[1]))


def _c1_col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’').replace('`', '’')


# ### the repairs each item is met by at v1.23.0
C1_EV_EXTRA = {1: '; repair (subjects); rule (2) of data/b743_rules.txt: the commit tool takes no subject text for the seal',
               2: '; repair (subjects); rule (2) of data/b743_rules.txt: the seal and lock subject the composer’s whole, nothing after it',
               3: '; repair (remote); rule (1) of data/b743_rules.txt: the remote figures read from the remote by the composer',
               4: '; repair (push); rule (3) of data/b743_rules.txt: the push tool refuses at itself, exit 13, when its branch or step row is absent',
               5: '; rule (4) of data/b743_rules.txt: the hold held; printed REPEAT of b727 event (13), read so in the counter below',
               6: '; rule (4) of data/b743_rules.txt: the hook held, REPEAT of b741 defect (s); the file’s origin, rule (6), in the dated notes'}
C1_DF_EXTRA = {'k': '; repair (dispatch); rule (5) of data/b743_rules.txt: a target no module of the tree refused', 'l': '; repair (dispatch); rule (5) of data/b743_rules.txt: a commit already rowed refused, the label from the dispatch count'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b743, to event (6) (`(R353)`(3)(vi)): the zero-byte file “=” at the relay root was created and last written 2026-09-24T18:18:38Z, inside b511 (its act commit fc9f9e9d at 18:21:02Z). b511’s defect (e) (relay data/b511_defects.txt) records that its defects bank was first written through a double-quoted shell string whose backtick possessives the shell ran as command substitution; defect (d)’s words “VACUOUS where B >= |m|” stand inside such a backtick span, and the shell read the “>=” there as a redirect to a file named “=”. Reproduced in an empty directory, the same words in a double-quoted string make one empty file “=” (relay data/b743_standing_v1230.txt, the (origin) case). No session transcript of that window survives. Delete or leave is the author’s word at the sitting (`(R353)`(4)(G)).',
            'Dated note, b743, to event (3) (`(R353)`(3)(i)): the clause “nothing past bce5605d pushed” came from the seat’s progress note, not from a remote read. Composed from the remote heads as they stood at prompt time it reads “relay remote at 13498fd2; local 25 commits past it; PLACE-papers remote at efce669f; local 1 commit past it” (the (remote) case). The author’s answer is carried as given.',
            'Dated note, b743, to event (5) (`(R353)`(3)(iv)): the row is tagged THE HOST’S, NEW; the hold refused the part beneath 2560 MB and nothing ran, the class of b727 event (13), and this corrigendum reads it REPEAT in its counter. Event (6) is tagged REPEAT in its own bracket, the class of b741 defect (s).',
            'Dated note, b743, to defects (k) and (l) (`(R353)`(3)(v)): dispatch 4 (run 42061332755) spent a dispatch on fourteen bare names, none a module of zq-b730 at 4c04916c; the commit 4c04916c was rowed G4-G6 and again R5, beside the true R5 c2d4f29c. Both replayed through the repaired writer, both refused; dispatch 5’s full names pass.')
C1_CLASSES = (
    ('cites', 'the citation reader’s item label (b743 step-zero defect (f))', 'rule (8) of data/b743_rules.txt; tools/standing/cites.py lean_rows skips the names before a path cited for an item label opening its parenthesis (“(S4’, Carrier.lean :21)”). b743’s ferry :11: a row zqFn beside Carrier.lean before, none after; b742’s ferry, eight rows before and after, equal'),
    ('remote', 'the root prompt’s remote figures (`(R353)`(3)(i), event (3); CLAIM ; NEW)', 'rule (1) of data/b743_rules.txt; tools/standing/rootprompt.py remote_read reads the remote once and banks the heads, remote_clause composes “remote at <sha>; local <n> commits past it”, and compose_checked given the heads refuses a clause naming a commit as pushed that no remote head is. b742’s prompt: put before, refused at “nothing past bce5605d pushed” after; regenerated, refusing nothing'),
    ('subjects', 'the commit tool and the seat’s subject text (`(R353)`(3)(ii), events (1)-(2))', 'rule (2) of data/b743_rules.txt; tools/standing/commit.py takes no words for lock, gate and seal; subjects.py composes the gate subject from the index and the banks and checks a seal or lock subject as the composer’s whole. b742’s “97 files” words refused for the count alone before, the same words with 96 accepted; refused as words after. 86f033a3’s doubled head composed and passed before, refused after'),
    ('push', 'the push tool’s pre-check (`(R353)`(3)(iii), event (4))', 'rule (3) of data/b743_rules.txt; tools/standing/pushcheck.py, called by tools/push_gated.sh before any ref is read: the branch must stand and the act’s step bank be committed, exit 13. b742’s 22:01:12Z send replayed with the branch absent: exit 128 at the ref before, exit 13 at the tool after'),
    ('dispatch', 'the dispatch’s targets and row labels (`(R353)`(3)(v), defects (k), (l))', 'rule (5) of data/b743_rules.txt; tools/standing/dispatchrows.py targets_refused, label, series: a target no .lean file of the tree or not in the plan’s module list refused, a repair commit labelled from the dispatch count, a commit already rowed refused. Dispatch 4’s fourteen names refused, dispatch 5’s full names passing; the second row of 4c04916c refused'),
    ('repeat', 'the hold and the hook (`(R353)`(3)(iv), events (5)-(6))', 'rule (4) of data/b743_rules.txt; guards: the hold, REPEAT of b727 event (13); the hook, REPEAT of b741 defect (s), each class read from the acts before b742'),
    ('origin', 'the “=” file (`(R353)`(3)(vi), event (6))', 'rule (6) of data/b743_rules.txt; guards: the file’s time against b511’s defect (e), and the reproduction in an empty directory'),
    ('version', 'the version (`(R353)`(3)(vii))', 'rule (7) of data/b743_rules.txt; tools/standing/VERSION v1.23.0, landed by a commit of its own (%s) with its controls bank' % K.C1_STANDING),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b742’s events bank (relay data/b742_events.txt) carries six rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank nineteen lettered rows, (a)-(s), each tagged in its own bracket (%s); its refusal bank twenty-five lines at %s, '
         'each recorded by a row, the first two b741’s. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R353)`(3), at tools/standing/ v1.23.0, each with a control on b742’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b742’s events (1)-(6):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?(-\d\d:\d\dZ)?( \([^)]*\))?( and \d\d:\d\d:\d\dZ \([^)]*\))?|post-push|pre-push and post-push)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b742_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b742’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b742_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b742’s refusals** (relay data/b742_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (six events, nineteen defects), as b742’s closing prints it (relay data/b742_closing.txt :5); '
          'as this corrigendum reads them, event (5) REPEAT of b727 event (13) by `(R353)`(3)(iv), CLAIM %d, CLOSE %d, REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, rep, n, n, rc, rl_, rr, rn, ', '.join(claims) or 'none'), '',
          '*Filed at b743 on the author’s ruling `(R353)`(3): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b743.py) from '
          'b742’s events and defects banks read unedited, its refusal bank, and the v1.23.0 controls bank; banked as relay `data/b743_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b742’s record; no sealed tool, face, trail or root-named bank of b742 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr, rn = _c1_read_counts(s)
    return (['b743 -- THE CORRIGENDUM FOR b742, (R353)(3) (%s)' % utc(), '',
             '### the banks read unedited: data/b742_events.txt rows (1)-(6), data/b742_defects.txt 19 rows, data/b742_hook_refusals.txt 25 '
             'lines at %s; data/%s (the v1.23.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 6, DEFECTS 19 ; CLAIM %d, CLOSE %d ; REPEAT %d ; AS READ HERE, EVENT (5) REPEAT: CLAIM %d, CLOSE %d, REPEAT %d OF %d ; DATED NOTES %d ; v1.23.0: THE CITATION READER`S LABEL, '
               'THE ROOT PROMPT`S REMOTE FIGURES, NO SUBJECT TEXT, THE PUSH PRE-CHECK, THE DISPATCH TARGETS AND LABELS, THE HOLD AND THE HOOK AS REPEAT, THE "=" ORIGIN, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (
                   n, nc, nl_, rep, rc, rl_, rr, rn, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b742 at its weight after its entry, and the corrigendum for b742, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.23.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; AS READ HERE %d, %d, %d OF %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, rc, rl_, rr, rn, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b743, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b743 ran three
# ### ((R353)(4)(iii)-(iv), N1), rowed in data/b743_dispatch_rows.json. Replaced for b743 alone; the arms' names stand, their plants on b743's rows.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R352)(7), as b742 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R353)(3)(b), N1, b743 (b738's form): fourteen dispatches allowed, seven made (the refused send of defect (j) rowed
    `dispatch_refused`, no run, not counted); each dispatch row carrying free_mb, its run id the worklist's in order, read once after it by
    that id; the plant a dispatch row with no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    return len(ds) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 14 and [r.get('run') for r in ds] == list(K.EF_RUNS) \
        and all(isinstance(r.get('free_mb'), int) for r in ds + rs) \
        and all(sum(1 for x in rs if str(x.get('run')) == str(d.get('run'))) == 1
                and rows.index(d) < next(i for i, x in enumerate(rows) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) for d in ds)
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b743: each dispatch read once after it by its run id (seven this act)
#⟪END⟫
# ### b743, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R353)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b742, naming tools/standing/hook.py, unedited by v1.22.0 (its blob at 147342a2 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b743, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b742's record has twelve
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 5)) \
#⟪END⟫
# ### b743, Component 4 (the Edit tool): b743's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b742's override of checks 526 -- no registration commit -- removed: b743
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b743_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b743, Component 6 (the Edit tool): b743's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b742's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b743, Component 4 (the Edit tool): b742's overrides of checks 1516 and 1659 (hook.py edited by b742's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b743 as it stands
# ### b743, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b743_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b743, Component 4 (the Edit tool): b742's override of checks 1476-1482 (one ERRATA entry at b742's (R352)(5)) removed -- (R353)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b743 as it stands
# ### b743, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b742's step-zero wording; b743's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b743, Component 4 (the Edit tool): G-RUNNER-READ's plant on b743's dispatch rows -- run 2's axiom lines carrying sorryAx (b742's
# ### plant read the lv rows' closure log, which b743 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='planted', run=1)))),
#⟪END⟫
# ### b743, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b743, Component 6 (the Edit tool): the fold bank was b742's own route
# ### (tools/b742_fold.py); b743's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b743_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b742.py -> tools/acts/b743.py' in (rd('b743_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b743, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b743_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b743, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b743_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b743_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b743, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R353): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R353)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b743')
    return '### THE COUNTER ((R353) Component 5, the act`s events and defects together; relay data/b743_defects.txt, data/b743_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b742, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b743 (defect (d')): the order's
# ### state as b743 leaves it -- the carry from b742 said "as b742 left it ... not touched this act", where b743 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-OFFLINE-ZERO open, SP4 REACHED this act on route (K) at zq_offline_zero and zq_li_nonneg_fails, its discharge the author`s to rule,',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b743, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b742's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b743, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b742's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b743_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b743_registration_%s.txt' % __import__('b743_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b743, Component 4 (the Edit tool, before the face): b742's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b743, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b743's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b743, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R353)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b743 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b743_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b743: the build's one route
#⟪END⟫
# ### b743, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b742's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b743 scorer reads; the needles set to the banks b743's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b743, (R353)(2)(iii): b742's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b743, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b743_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrstuvwxyz')))   # ### (a)-(z) as entered before the lock, every one the seat's (data/b743_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b743_corrigendum.txt', 'data/b743_standing_v1220.txt', 'data/b743_rules.txt', 'data/b743_s6_plan.txt', 'data/b743_offlinezero.txt',
                  'data/b743_offlinezero_notes.txt', 'data/b743_dispatch_rows.json', 'data/b743_pathrefusal.txt',
                  'data/b743_reproduce.txt', 'data/b743_reproduce.json', 'data/b743_address_scan.txt', 'data/b743_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b743 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R353)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b743_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R353)(4): the sitting bank's rows by number -- a row opens `[n] STATE` at column 0, its fields indented two spaces as `KEY: value`;
    returned {n: {'state', 'word', 'at', 'confirm', 'file', 'draft'}}. Pure in its argument."""
    out, cur = {}, None
    for l in (t or '').split(NL):
        m = re.match(r'^\[(\d+)\] (.+)$', l)
        if m:
            cur = out.setdefault(m.group(1), dict(state=m.group(2).strip()))
            continue
        f = re.match(r'^  ([A-Z][A-Z` ]+): (.*)$', l)
        if cur is not None and f:
            k = {'THE AUTHOR`S WORD': 'word', 'AT': 'at', 'CONFIRMATION': 'confirm', 'FILE': 'file', 'DRAFT WRITTEN': 'draft'}.get(f.group(1))
            if k:
                cur[k] = f.group(2).strip()
        elif not l.strip():
            cur = None
    return out


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R353)(2)-(4) (b743's keys over b743's objects): the order by time and ancestry; v1.22.0's controls; the plan read as
        # ### committed; the build bank and its notes; zq-b730; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.C2_RELAY, K.STATEMENTS_BANK))) or None, _s(blob(ROOT, 'HEAD:' + K.STATEMENTS_BANK)) or None),   # ### the statements at Component 2's commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_build', K.C1_CORR, K.C2_RELAY),
                                 ('stmt_build', K.C2_RELAY, K.PRINT_COMMIT))),
        v1130=rd('b743_standing_v1220.txt'), plan=rd('b743_s6_plan.txt'), print_=rd('b743_offlinezero.txt'), rows_bank=rd('b743_s6_plan.txt'),
        notes=rd('b743_offlinezero_notes.txt'),
        plan_first_files=files_of(ROOT, K.C2_RELAY), plan_files=files_of(ROOT, K.PRINT_COMMIT), price_files=(),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..%s' % (K.ZQ_ENTERING, K.ZQ_TIP)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--contains', K.ZQ_FIRST).split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b743_dispatch_rows.json') or '[]'), reproduce=rd('b743_reproduce.txt'), reproducej=jl('b743_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b743_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b742 left them
        rebuild=None, rebuild_rows=json.loads(rd('b743_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.C2_RELAY), zq_first=_ct(EF, K.ZQ_FIRST),
               zq_tip=_ct(EF, K.ZQ_TIP), sitting=_ct(ROOT, K.PRINT_COMMIT),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.C2_RELAY), sitting=files_of(ROOT, K.PRINT_COMMIT), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b743's read-first bank's items by path, as its step zero wrote them (data/b743_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b742_closing.txt |', 'relay data/b742_events.txt |', 'relay data/b742_defects.txt |', 'relay data/b742_touch.txt |',
                     'relay data/b742_offlinezero.txt |', 'relay data/b742_c7_plan.txt |', 'relay data/b738_offlinezero.txt |',
                     'relay data/b737_offlinezero_plan.txt |', 'relay data/b735_explicitformula.txt |', 'relay data/b742_author_answers.txt |',
                     'relay data/b743_author_answers.txt |', 'SIDE-explicit-formula zq-b730 at 3329eaa1 |', 'Mathlib at de5ce8a9 |',
                     'relay data/b742_checks.txt |', 'relay data/b743_hook_refusals.txt |', 'relay data/b742_standing_v1210.txt |',
                     'PLACE-papers FINDINGS.md :13493, :13495, :13575', 'relay tools/b743_worklist.py whole;')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R353)(1)-(2))', 'CERTIFICATE TO SP4 ((R353)(3))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (160 = 160 + 0, data/b743_citation_check.txt); the check CLEAN;
    the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 160 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b743, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b742's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b743, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b742()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b743_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b742's figures, read at FINDINGS :13617 as Component 1 landed them
    return landed(S, 0, ['b742 AT ITS WEIGHT', 'suite 114 of 116', 'relay 605b5641', '21 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b743's title in the ferry's Component 4 form (the record tool's _title over the banks); the opening phrase lowercase after "## " as the
# ### ferry orders, read by tools/standing/armnorm.py cannot_pass before the lock ((R353)(2)(i))
TITLE_NEEDLES = ('## W-ORD-ZQ-OFFLINE-ZERO, S6: the route on Λ_Q by interpolation', ' by the author’s word; SP4 REACHED, zq_offline_zero and zq_li_nonneg_fails compiled; ',
                 ' dispatches of ', ' lines; ', ' names on the standard three; ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R353)(1)-(2): the generated entry for b742's four events and twenty-one defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(4), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 5, CLOSE 20 over 25, REPEAT 14); the repairs at tools/standing/ v1.22.0 by their controls
    bank; the corrigenda bank appended at row (62) and nothing before it changed; in Component 1's commits (the figures read from
    data/b743_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 21 and len(items) == j.get('items') == 25 and j.get('row') == 62 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 25 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 5 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 14 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.22.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 5 \
        and '  (62) ' in S['corrigenda'] and '  (63) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b743_rules.txt carries (R353)(2)'s six rules, in its own commit ad371df2; data/b743_rules.txt (by form in (R353)(4)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b742's form, its names b743's); no author's word of b743 orders a row of the next act's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and "(1) A DISPATCH CONDITIONED ON THE AUTHOR'S WORD WAITS ON THE COMMIT" in r1 and '(6) THE VERSION' in r1 and '(7) ' not in r1 and S['files']['rules'] == ['data/b743_rules.txt'] \
        and not os.path.exists(os.path.join(D, 'b743_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b743's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO S6 TO SP4', 'CERTIFIED -- tools/standing/ v1.22.0', 'REGISTERED -- THE FAR CIRCLE`S BOUND AS BUILT',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b743: seven dispatches of the fourteen (R353)(3)(b) allows -- each dispatch command in the capture a row (the one send GitHub
    refused with HTTP 500 rowed `dispatch_refused`, no run made, defect (j)), each row carrying free_mb and read once after it by its run
    id; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = bool(seq_) and all(
        sum(1 for x in seq_ if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) == 1
        and seq_.index(d) < next(i for i, x in enumerate(seq_) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run')))
        for d in seq_ if d.get('kind') == 'dispatch')   # ### N1: each dispatch read once after it by its run id
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b743_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) <= K.MAX_DISPATCHES \
        and len(cmds) == len(K.EF_RUNS) + len([r for r in rows if r.get('kind') == 'dispatch_refused']) \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b743, N1: seven rows, eight dispatch commands, one refused by the host
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (the ledgers, FINDINGS and OPEN_TRAILS), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b743's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The plan before any Lean**', '**The certificate to SP4**', 'One deviation from the plan: the bound on the far circle',
                 '**The dispatches**', '**The git writes**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b743_corrigendum.txt', 'data/b743_standing_v1220.txt', 'data/b743_s6_plan.txt', 'data/b743_offlinezero.txt', 'data/b743_offlinezero_notes.txt',
                 'data/b743_reproduce.txt', 'data/b743_address_scan.txt', 'data/b743_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b743: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R353)(3)(a) as amended (data/b743_author_answers.txt :7), N2 (the name the frozen run list carries): the S6 plan read as committed --
    its blob at Component 2's commit f15c3a8d a prefix of its blob at HEAD, the rest the one appended section "## (7) DATED NOTES" and no row
    of (0)-(6) rewritten; that commit carrying it and the build bank's not; its seven sections (0)-(6), the two ruled routes STOPPED, the
    interpolation route taken, the author's five items printed; the plan bank's md5 the step zero print's, printed in the build bank; v1.22.0's
    commit, the corrigendum's, the plan's and the build bank's in that order by time and by ancestry; the earlier acts' registrations at HEAD
    their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('standing', 'corr', 'plan', 'print')
    base_ = (reg or '').rstrip(NL)
    tail_ = (head or '')[len(base_):] if (head or '').startswith(base_) else None
    secs_ = re.findall(r'(?m)^## \((\d)\) ', reg or '')
    return bool(reg) and bool(base_) and tail_ is not None and tail_.lstrip(NL).startswith('## (7) DATED NOTES') \
        and K.STATEMENTS_BANK in S['plan_first_files'] and K.STATEMENTS_BANK not in S['plan_files'] \
        and secs_ == ['0', '1', '2', '3', '4', '5', '6'] \
        and all(w_ in reg for w_ in ('## (1) THE TWO RULED ROUTES, PRICED: STOPPED', '## (2) THE ROUTE TAKEN: INTERPOLATION', "## (3) THE AUTHOR'S FIVE ITEMS")) \
        and 'data/b743_s6_plan.txt md5 %s ; step zero`s %s ; equal True' % (K.PLAN_MD5, K.PLAN_MD5) in (S['print_'] or '') \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b743_address_scan.py run live over every commit of the act (relay and
    PLACE-papers; fields, messages and added lines; zq-b730's three Lean commits scanned at each commit by the seat), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R353)(2)-(3), N2 (the name the frozen run list carries): (2) whole before (3) -- v1.22.0, the weight and corrigendum on PLACE-papers
    and the corrigendum banks before the plan bank; the plan before the first Lean commit on zq-b730 ((R353)(3)(a)); the last
    Lean commit before the build bank, by the commits' times; the corrigendum an ancestor of the plan, the plan of the build bank."""
    t_ = S['t']
    return all(t_.get(k_) for k_ in ('c1pp', 'c1', 'standing', 'plan', 'zq_first', 'zq_tip', 'print')) \
        and max(t_['standing'], t_['c1pp'], t_['c1']) < t_['plan'] < t_['zq_first'] <= t_['zq_tip'] < t_['print'] \
        and S['anc'].get('corr_build') is True and S['anc'].get('stmt_build') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R353)(3)(b) as amended, N1, N3 (the name the frozen run list carries): the build bank's dispatch table -- one row per dispatch, its
    run id the worklist's in order, each row's sha one of zq-b730's six commits, its free memory and its licence 1f96d4ea printed, each graded
    KERNEL or BREAKS, the last KERNEL; the lines measured per group and in all against 3970-6810 and the three-times rule (20430); every
    printed name of the build, 30, on the standard three, the two SP4 statements among G6's; the foot SP4 REACHED, 7 of 14 dispatches."""
    t = S['print_'] or ''
    rows = re.findall(r'^  (\d+) \| group (\S+)\s*\| (.+?) \| sha ([0-9a-f]{8}) \| run (\d+) \| free (\d+) MB \| licence ([0-9a-f]{8}) \| (KERNEL|BREAKS),', t, re.M)
    v = _vlast(t)
    std = 'propext, Classical.choice, Quot.sound (run %d)' % K.EF_RUNS[-1]
    built = re.findall(r'^  (G\d)  ([\w.]+)\s+(propext.*)$', t, re.M)
    return bool(rows) and [int(r[4]) for r in rows] == list(K.EF_RUNS) and [int(r[0]) for r in rows] == list(range(1, len(K.EF_RUNS) + 1)) \
        and all(any(c.startswith(r[3]) for c in K.ZQ_COMMITS) for r in rows) and all(r[6] == K.STEPZERO_ANSWERS[:8] for r in rows) and rows[-1][7] == 'KERNEL' \
        and 'THE ROUTE IN ALL: measured 4097 ; the estimate 3970-6810' in t and 'THE THREE-TIMES RULE: the ceiling 20430 lines ; measured 4097 ;' in t \
        and len(built) == 30 and all(a_.strip() == std for _g, _n, a_ in built) \
        and {'zq_offline_zero', 'zq_li_nonneg_fails'} <= set(n_ for _g, n_, _a in built if _g == 'G6') \
        and v == 'SP4 REACHED ; DISPATCHES 7 OF 14 ; LINES 4097 AGAINST 3970-6810 (THE CEILING 20430) ; NAMES 30 OF 30.'
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip
    locally and at origin; zq-b730's diff against its entering tip 3329eaa1 the fourteen S6 modules (Interp, Frame, Strip, Amplify,
    NodeBase, Omega, Nodes0-3, NodesF, FrontierData, Frontier, SP4) and print_targets.txt alone, its six commits the worklist's in order; no tag and no other branch carrying the act's first Lean commit (no merge)."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and sorted(S['zq_files']) == sorted(K.ZQ_FILES) and S['zq_log'] == list(K.ZQ_COMMITS) \
        and not S['zq_tags'] and S['zq_merged'] == [K.ZQ_BRANCH]

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
    arm list since b742's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R353)(3)(b) as amended, N3, N5 (the name the frozen run list carries): the three-times rule kept -- 4097 lines within 20,430, no
    group over its own figure; no OffZero module beyond the fourteen among zq-b730's files and no file on a main; N3, the Lipschitz figure
    printed as a proved bound with its lemma's name (notes (3): LPq = 6.098e-10, lemma lp_le); the far-circle bound's deviation printed
    (notes (1): B = 120 against the plan's 7.8004, MARGIN 1.0725e-11 against 1e-12); the price line in OPEN_TRAILS at :17400 unmoved."""
    t = S['print_'] or ''
    n_ = S['notes'] or ''
    return 'THE THREE-TIMES RULE: the ceiling 20430 lines ; measured 4097 ; groups over their own figure NONE ; within' in t \
        and not [f_ for f_ in S['zq_files'] if f_ not in K.ZQ_FILES] and not [f_ for f_ in S['zq_files'] if '/Main' in f_] \
        and re.search(r'(?m)^\(3\) N3, the Lipschitz figure printed as a proved bound: L_P <= LPq = 6\.098e-10, lemma lp_le ', n_) is not None \
        and re.search(r'(?m)^\(1\) The bound on the far circle: B = 120 .* in place of the plan.s 7\.8004;.* MARGIN 1\.0725e-11 against 1e-12', n_) is not None \
        and 'W-ORD-ZQ-OFFLINE-ZERO' in oline(S, K.PRICE_LINE)


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
    """standing clauses v9 (Component 7 of (R353): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b743_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b742's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R353-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b742's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R353) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b742's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R352)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base fe2150b3',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 141 = 141 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b742-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 form: W-ORD-ZQ-OFFLINE-ZERO, S6, the route on Λ_Q by interpolation by the author`s word, SP4 graded with its two statements, the dispatches of the cap, the lines, the names, the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R353)(1)-(2): the generated corrigendum for b742`s record, landed at FINDINGS :13619: its four events and twenty-one defects, 25 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 5 CLOSE 20, REPEAT 14; v1.22.0`s repairs by data/b743_standing_v1220.txt; the corrigenda bank appended at row (62)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b743_rules.txt carrying (R353)(2)`s rules in its own commit ad371df2',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b743's objects
    ('G-REGISTRATIONS-FIRST', '(R353)(3)(a) as amended, N2: the S6 plan read as committed, its blob at f15c3a8d a prefix of HEAD`s, the rest its dated notes (7) alone; seven sections (0)-(6), the two ruled routes STOPPED, the interpolation route taken, the author`s five items; the plan`s md5 the step zero print`s in the build bank; v1.22.0`s, the corrigendum`s, the plan`s and the build bank`s commits in that order by time and ancestry; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(stmt_build=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b743_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R353)(2)-(3), N2: (2) whole before (3) -- v1.22.0, the weight and corrigendum and their banks before the plan; the plan before the first Lean commit; the last Lean commit before the build bank, by time; the corrigendum an ancestor of the plan, the plan of the build bank',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_build=False))),
    ('G-DERIVATION-GRADED', '(R353)(3)(b) as amended, N1, N3: the build bank`s dispatch table -- the worklist`s seven runs in order, each sha a zq-b730 commit, free memory and the licence 1f96d4ea printed, KERNEL or BREAKS, the last KERNEL; 4097 lines against 3970-6810 within 20,430; all 30 printed names on the standard three, zq_offline_zero and zq_li_nonneg_fails among them; the foot SP4 REACHED, 7 of 14 dispatches',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'print_', (S['print_'] or '').replace('| run 42054839204 |', '| run 42054839205 |'))),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against 3329eaa1 the fourteen S6 modules and print_targets.txt alone, its six commits the worklist`s; no tag and no other branch carrying them',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at fe2150b3, VERSION 9; v8 at HEAD its blob at fe2150b3; no v10; v9`s commit an ancestor of v1.22.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R353)(3)(b) as amended, N3, N5: the three-times rule kept (4097 within 20,430), no OffZero module beyond the fourteen; N3`s Lipschitz figure a proved bound with its lemma (notes (3), lp_le); the far-circle deviation printed (notes (1), B = 120 against 7.8004, MARGIN 1.0725e-11 against 1e-12); the price line at OPEN_TRAILS :17400',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'notes', (S['notes'] or '').replace('lemma lp_le ', 'lemma planted '))),
    ('G-DIFFERS-ERRATA', '(R353): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 6e86bd1e, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b743_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R353-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b742`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: fourteen dispatches allowed by (R353)(3)(b), seven made, each row carrying free_mb, each read after it by its run id, the worklist`s runs in order; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: eight dispatch commands in the capture, one refused by the host with HTTP 500 and rowed dispatch_refused, seven rows, each read after it by its run id, each carrying free_mb; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b742 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0; zq-b730`s six commits read at G-OFFSET-POST-HOC',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers, FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b742`s trail record on OPEN_TRAILS (:17612) and its root in the chain', lambda S: '### b742 — lane two, act one hundred and sixty-eight, the certificate act under (R352)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers, FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b742`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: seven of the fourteen, and one send refused by the host; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b743 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b742's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b743: (R353)'s rows, set at step zero by the Edit route (scratch splice743.py). (1)'s line read by the ruling from the public relay at 16a36428
    pub = _blob('D:/relay', '16a36428', 'data/b742_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b742_closing.txt :1, the head line as the public relay carries it at 16a36428', bool(pub) and pub[0] == at(cl, 1) and 'relay ced30a77' in pub[0] and 'PLACE-papers 3dc9c05' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 114 of 116', 'root 9c9c6a90c282a4a4', '2 prompts answered', 'scores 8 of 8 HELD', '19 defects'):
        add('ruling (1)', 'data/b742_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'data/b742_closing.txt :5, the counter CLAIM 8, CLOSE 17, REPEAT 13 OF 25, DEFECTS 19, EVENTS 6', 'CLAIM 8, CLOSE 17, REPEAT 13 OF 25' in at(cl, 5) and 'DEFECTS 19, EVENTS 6' in at(cl, 5), at(cl, 5)[-60:], '1')
    ob_ = lines_of(p('data', 'b742_offlinezero.txt'))
    for n_, w_ in ((61, 'G6  zq_offline_zero'), (62, 'G6  zq_li_nonneg_fails')):
        add('ruling (1), (2), ferry (read first)', 'data/b742_offlinezero.txt :%d, %s on the standard three, run 42068096322' % (n_, w_),
            w_ in at(ob_, n_) and 'propext, Classical.choice, Quot.sound (run 42068096322)' in at(ob_, n_), at(ob_, n_)[:60], '1')
    for n_, k_, w_ in ((65, '(1)', 'B = 120'), (65, '(1)', "in place of the plan's 7.8004"), (65, '(1)', 'REM = 4.4989e-13'), (67, '(3)', 'L_P <= LPq = 6.098e-10, lemma lp_le'),
                       (68, '(4)', 'committed at relay 22f8d6b1, 6467c061 and 3194b6eb'), (69, '(5)', 'dispatch 4 was spent on a target of bare module names'),
                       (70, '(6)', '||lamF cA|| <= 6e-13 < 1e-12'), (71, '(7)', '80 check points, 20 to an edge at spacing 1/100'), (71, '(7)', 'within 1/200 of one'),
                       (71, '(7)', 'MLO = 1.7e-11 against the least |P^| of 1.7480e-11')):
        add('ruling (1), ferry (read first)', 'data/b742_offlinezero.txt :%d, note %s carries %s' % (n_, k_, w_), at(ob_, n_).startswith('  ' + k_) and w_ in at(ob_, n_), at(ob_, n_)[:60], '1')
    add('ruling (1), ferry (read first)', 'data/b742_offlinezero.txt :76, SP4`s statements both COMPILED', 'zq_offline_zero COMPILED ; zq_li_nonneg_fails COMPILED' in at(ob_, 76), at(ob_, 76)[:60], '1')
    for w_ in ('SP4 REACHED', 'DISPATCHES 7 OF 14', 'LINES 4097 AGAINST 3970-6810', 'NAMES 30 OF 30'):
        add('ruling (1), ferry (read first)', 'data/b742_offlinezero.txt :79, the grade line carries %s' % w_, w_ in at(ob_, 79), at(ob_, 79)[:60], '1')
    s6_ = lines_of(p('data', 'b742_s6_plan.txt'))
    for n_, w_ in ((8, '## (0) THE OBJECT AND THE FRAME'), (10, 'F(z) = zqPair.Λ₀ z − 1/(z (1 − z))'), (12, 'Carrier.lean :21 carrier_of_box finishes S4'),
                   (13, "SP1' : ‖F cA‖ < m_Λ"), (89, 'zq_offline_zero : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1/2'), (90, '¬ (∀ n : ℕ, 0 ≤ Wide.liCoeff zqZeroConfig n)')):
        add('ruling (2), ferry (read first)', 'data/b742_s6_plan.txt :%d, %s' % (n_, w_), w_ in at(s6_, n_), at(s6_, n_)[:60], '1')
    df_ = lines_of(p('data', 'b742_defects.txt'))
    for n_, k_, w_ in ((16, '(k)', 'bare module names'), (17, '(l)', 'rowed the earlier commit 4c04916c a second time under the item R5')):
        add('ruling (3)(v), ferry (read first)', 'data/b742_defects.txt :%d, %s carries %s' % (n_, k_, w_), at(df_, n_).startswith('    ' + k_) and w_ in at(df_, n_), at(df_, n_)[:60], '1')
    ev_ = lines_of(p('data', 'b742_events.txt'))
    for n_, w_ in ((4, '(1) THE SEAT\'S [CLAIM ; NEW]'), (4, '"97 files"'), (5, '(2) THE SEAT\'S [CLOSE ; NEW]'), (8, '(3) THE SEAT\'S [CLAIM ; NEW]'), (8, 'nothing past bce5605d pushed'),
                   (9, '(4) THE SEAT\'S [CLOSE ; REPEAT]'), (12, '(5) THE HOST\'S [CLOSE ; NEW]'), (12, 'BENEATH THE HOLD 2560 MB'), (15, '(6) THE SEAT\'S [CLOSE ; REPEAT]'),
                   (15, 'created and last written 2026-09-24T18:18:38Z')):
        add('ruling (3), ferry (read first)', 'data/b742_events.txt :%d carries %s' % (n_, w_), w_ in at(ev_, n_), at(ev_, n_)[:60], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b742']]
    add('ruling (1)', 'data/act_roots.txt, b742`s root 9c9c6a90 chained from b741`s 5dd16337', len(ar9_) == 1 and ar9_[0][1].startswith('9c9c6a90') and ar9_[0][2].startswith('5dd16337'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    b3_ = rd(p('data', 'b742_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b742 (b742`s post-push part b3)', 'b742 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b742 AGREE' if 'b742 AGREE' in b3_ else 'ABSENT', '1')
    ck_ = rd(p('data', 'b742_checks.txt')) or ''
    add('ruling (1)', 'data/b742_checks.txt, 116 run, 114 passing, G-AXIOM-CLAIM and G-RULE-POSTSEAL-READ failing',
        "ARMS RUN : 116. ### LIVE PASSING : 114. ### LIVE FAILING : 2 ['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ']" in ck_, 'read', '1')
    sc9_ = _jl('b742_scores_close.json')
    held_ = sorted(k_ for k_, v_ in sc9_.items() if v_[:1] == ['HELD'])
    add('ruling (1)', 'data/b742_scores_close.json, 8 of 8 HELD', len(held_) == 8, 'HELD %s' % ' '.join(held_), '1')
    mv_ = rd(p('data', 'b742_mirror_verify.txt')) or ''
    add('ruling (1)', 'data/b742_mirror_verify.txt, CLEAN ON ALL THREE CLAUSES', 'CLEAN ON ALL THREE CLAUSES' in mv_, 'CLEAN' if 'CLEAN ON ALL THREE CLAUSES' in mv_ else 'ABSENT', '1')
    add('ruling (1)', 'data/b742_closing.txt, the mirror mirror-refresh-2026-11-05-b742', 'mirror-refresh-2026-11-05-b742.zip' in NL.join(cl), 'read', '1')
    sv_ = rd(p('data', 'b742_standing_v1220.txt')) or ''
    add('ruling (1)', 'data/b742_standing_v1220.txt, v1.22.0, 13 cases, 13 as wanted', 'v1.22.0' in sv_ and 'CASES 13 ; AS WANTED 13' in sv_, 'read', '1')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.23.0's commit's parent once it lands, HEAD's blob before (the working copy carries v1.23.0 unlanded)
    add('ruling (1)', 'tools/standing/VERSION v1.22.0 entering the act', v0_ == 'v1.22.0', v0_, '1')
    for f_ in ('data/b742_steps.json', 'data/b742_relay_push-b742-closing_push_out.txt', 'tools/mirror_prevbuild.json'):
        add('ruling (3)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
    # ### the readfirst list's relay banks, each printed from the tree; a path absent printed absent
    for f_ in ('data/b736_sitting.txt', 'data/b733_2c_note.txt', 'data/b725_interference.txt', 'data/b729_c2.txt', 'data/b739_zenodo_readback.json'):
        add('ferry (read first)', '%s, printed from the tree' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)), 'tracked' if gr('D:/relay', 'ls-files', '--', f_) else 'ABSENT', '0')
    fd36_ = bool(gr('D:/relay', 'ls-files', '--', 'data/b736_phase2_frontdoors.txt'))
    add('ferry (read first)', 'data/b736_phase2_frontdoors.txt -- ABSENT from the tree; the bank of that name is data/b732_phase2_frontdoors.txt (its :799 the instance)', not fd36_,
        'ABSENT' if not fd36_ else 'PRESENT', '0')
    f32_ = lines_of(p('data', 'b732_phase2_frontdoors.txt'))
    add('ferry (read first)', 'data/b732_phase2_frontdoors.txt :799, the DRAFT naming the Epstein zeta Z_Q of x² + xy + 6y²', 'Epstein zeta Z_Q of x² + xy + 6y²' in at(f32_, 799), at(f32_, 799)[:60], '0')
    c2n_ = lines_of(p('data', 'b733_2c_note.txt'))
    add('ferry (read first)', 'data/b733_2c_note.txt :8, the 2C note naming the Epstein zeta', 'the Epstein zeta Z_Q of x² + xy + 6y²' in at(c2n_, 8), at(c2n_, 8)[:60], '0')
    it_ = lines_of(p('data', 'b725_interference.txt'))
    add('ferry (read first)', 'data/b725_interference.txt :31, the zero table`s head', 'zeta_K(rho) = Z_Q1(rho) = -2 L(rho, psi) (FORCED)' in at(it_, 31), at(it_, 31)[:60], '0')
    add('ferry (read first)', 'data/b725_interference.txt :106, ZEROS 69, THE HYPOTHESIS HELD', 'ZEROS 69' in at(it_, 106) and 'THE HYPOTHESIS HELD' in at(it_, 106), at(it_, 106)[:60], '0')
    c2_ = lines_of(p('data', 'b729_c2.txt'))
    add('ferry (read first)', 'data/b729_c2.txt :45, THE C2 THEOREM COMPILED AT 18 OF 18', 'c2_value_law AND c2_least_negative COMPILED AT 18 OF 18' in at(c2_, 45), at(c2_, 45)[:60], '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), (3), ferry (read first)', 'events (1)-(6) and 19 defects (data/b742_events.txt, data/b742_defects.txt)',
        starts == [1, 2, 3, 4, 5, 6] and len(letters) == 19, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b742_closing.txt, its CARRIED items beneath the head', any('CARRIED' in l for l in cl), 'read', '0')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (1), (2), (5)', 'zq-b730 at 14ca5725, SP4`s tip, kept and unmoved', zt_.startswith('14ca5725'), zt_[:8], '1')
    for br_ in ('c2-b725', 'keiper-b725', 'detect-b729'):
        add('ruling (5)', '%s kept on SIDE-explicit-formula' % br_, bool(gr(EF_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    em_ = (gr(EF_, 'rev-parse', 'main') or '').strip()
    add('ferry (read first), (4)(A)', 'SIDE-explicit-formula main at badacccb, README.md read there', em_.startswith('badacccb') and bool(_blob(EF_, 'main', 'README.md')), em_[:8], '2')
    for f_, n_, w_ in (('SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 0, 'theorem zq_offline_zero'), ('SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 0, 'theorem zq_li_nonneg_fails'),
                       ('SIDEExplicitFormula/Schema/ZQ/OffZero/Carrier.lean', 21, 'theorem carrier_of_box')):
        bl_ = _blob(EF_, '14ca5725', f_).replace(chr(13), '')
        ok_ = (w_ in bl_) if not n_ else at(bl_.split(NL), n_).startswith(w_)
        add('ruling (2)', '%s at 14ca5725%s carries %s' % (f_, (' :%d' % n_) if n_ else '', w_), ok_, 'present' if ok_ else 'ABSENT', '1')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :%d, b742`s entry' % K.B711_ENTRY, at(fd_, K.B711_ENTRY).startswith('## '), at(fd_, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :13691, the deviation paragraph: B = 120 against the plan`s 7.8004', '120' in at(fd_, 13691) and '7.8004' in at(fd_, 13691), at(fd_, 13691)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b742`s weight line and corrigendum, the form b743`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fd_, K.B711_WEIGHT)) and bool(at(fd_, K.B711_CORRIGENDUM)), at(fd_, K.B711_WEIGHT)[:40], '0')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ferry (read first)', 'OPEN_TRAILS :%d, b742`s trail record, its hand section' % K.B711_TRAIL, at(ot_, K.B711_TRAIL).startswith('### b742 '), at(ot_, K.B711_TRAIL)[:50], '0')
    add('ruling (4)(F)', 'OPEN_TRAILS :%d, b742`s open-orders line' % K.TRAIL_ORDERS, at(ot_, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot_, K.TRAIL_ORDERS)[:50], '0')
    add('ruling (1)', 'OPEN_TRAILS :17400, W-ORD-ZQ-OFFLINE-ZERO`s price line', bool(at(ot_, 17400)), at(ot_, 17400)[:50], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope), (4)(B)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    for f_ in ('REGISTRY.md', 'SPIRAL_MAP.md', 'ERRATA.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'phase1.5/method/THE_METHOD_CANON.md',
               'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 'day1/Which_Structure_Confines_v2_4_0.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'):
        add('ferry (read first)', '%s at PLACE-papers, printed from the tree' % f_, bool(gr(PP, 'ls-files', '--', f_)), 'tracked' if gr(PP, 'ls-files', '--', f_) else 'ABSENT', '0')
    f7_ = lines_of(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND_v0_7.md'))
    add('ruling (4)(A), ferry (read first)', 'THE_FINDINGS_AS_THEY_STAND_v0_7.md :624, the paragraph of the Epstein instance', 'the Epstein zeta Z_Q of x² + xy + 6y²' in at(f7_, 624), at(f7_, 624)[:60], '2')
    w4_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines_v2_4_0.md'))
    add('ruling (4)(A), ferry (read first)', 'Which_Structure_Confines_v2_4_0.md :93, the class-number-2 line', at(w4_, 93).startswith('For class number 2 and Re s > 1, log(Z_Q/2)'), at(w4_, 93)[:60], '2')
    add('ruling (scope)', 'the census THE_KEYSTONE_CENSUS_v0_8_3.md at 36 kernels', '36' in NL.join(lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))[:40]), 'read', '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.22.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.22.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R353)(4): b742's export, the mirror's last
    add('ruling (4)', '%s, b742`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R353)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b742-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R353)(2), (4): act_current alone, then b742's step row 19 and its closing capture, each committed alone; tools/mirror_prevbuild.json's
    # ### LF form equal to HEAD's (2d637131), nothing to commit (b742's build rewrote it with CRLF endings, its content unchanged)
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b742_steps.json'),
                   (K.STEPZERO, 'data/b742_relay_push-b742-closing_push_out.txt')):
        if not c_:
            add('ruling (2)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (2)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
    pb_ = open(p('tools', 'mirror_prevbuild.json'), 'rb').read() if os.path.exists(p('tools', 'mirror_prevbuild.json')) else b''
    add('ruling (2)', 'tools/mirror_prevbuild.json, its working bytes equal to HEAD`s blob (LF), nothing to carry', bool(pb_) and pb_ == _blob('D:/relay', 'HEAD', 'tools/mirror_prevbuild.json').encode('utf-8') and b'\r' not in pb_,
        'equal, LF' if bool(pb_) and b'\r' not in pb_ else 'DIFFERS OR CRLF', '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (4)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (4)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b743_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b743_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b743 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b742_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.22.0's controls, the certificate to SP4 with its plan, notes and dispatch rows, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R353)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R353)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: zq-b730 of SIDE-explicit-formula alone, six commits under (R353)(3) as amended; no main's code, no merge, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b743 ((R353)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R352)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b743 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY-NINE, THE FRONTIER ACT: b742 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE DISPATCH`S LICENCE; '
              'W-ORD-ZQ-OFFLINE-ZERO, S6 ON Λ_Q BY INTERPOLATION BY THE AUTHOR`S WORD, SP4 REACHED ON ROUTE (K), UNDER (R353).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b742's sections over b742's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.22.0: the dispatch`s licence at the head, one remote read per repository per suite run, the counter composed once with its set named, the two post-closing slips, the refusal printed with its class, the version, each case failing before its repair and passing after', 'b743_standing_v1220.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE CERTIFICATE TO SP4 ((R353)(3))', [
                ('the S6 plan, the two ruled routes STOPPED, the interpolation route taken, the author`s five items printed, committed before any Lean file', 'b743_s6_plan.txt', r'(?m)^## \(2\) THE ROUTE TAKEN[^\n]*'),
                ('W-ORD-ZQ-OFFLINE-ZERO, S6 to SP4: the dispatches, the lines against 3970-6810 and the three-times rule, the axioms of every printed name, the grade', 'b743_offlinezero.txt'),
                ('the notes beside the build bank, the far circle`s bound first', 'b743_offlinezero_notes.txt', r'(?m)^\(1\) The bound on the far circle[^\n]*'),
                ('the probe-path refusal printed before the lock gate', 'b743_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b743_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b742`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b743_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R352)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; zq-b730 from ' + WL.ZQ_ENTERING[:8] + ' to ' + WL.ZQ_TIP[:8] + ', six commits, every Lean file of the act on it, off main, no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: of the fourteen (R353)(3)(b) allows, each read by its run id; one send refused by the host with HTTP 500, no run, not counted) ; the rebuild-b721 branches of the wave 1 kernels as b742 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b742-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the S6 plan committed before any Lean file, the generator tools/b743_s6gen.py before the modules it generates, their md5s equal at the tip, the order printed by ancestry ; the author`s word amending (R353)(3) banked at 1f96d4ea before the first dispatch, every dispatch row carrying it ; the build bank`s controls before its figures, the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate ;',
    '    N3: SP4 graded REACHED with both statements` axiom lines printed in full ; the Lipschitz figure printed as a proved bound with its lemma`s name (lp_le) ; the far circle`s bound printed as built beside the plan`s ; the entry`s nouns the banks` ; one git write per message ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b743_address_scan.txt, data/b743_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads, the seven workflow dispatches (and one send the host refused, no run) and their artifact downloads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo field touched ; the deposit route untouched, the draft held at v5 unpublished ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the price line, the trail) written ; no paper moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY or faces page byte ; data/act_roots.txt (b743`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.22.0 by (R353)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b742 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R353)(6)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZQ-OFFLINE-ZERO with SP4 REACHED (relay data/b743_offlinezero.txt), zq_offline_zero and zq_li_nonneg_fails compiled on zq-b730, the order`s discharge the author`s to rule ; the wave 1 deposit ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b743_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b742 left them; push-b742-sitting on b742`s 21 kernels, local; the build clone D:/zq-b738.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on any kernel`s main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b742`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b743: the standing repairs are v1.22.0's ((R353)(2), relay data/b743_standing_v1220.txt, read in the corrigendum section); the
    # ### carry's diffs here (b743 carried at step zero before the fold; its tools since are the templates and tools/acts/b743.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, the act`s one written branch; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b742 left them; port-b707 at b712`s tip %s)' % (
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
    b743's form over b743's objects (b738's build form, in git at b738's record tool): the corrigendum's foot and v1.22.0's controls; the
    build bank's foot and its lines; the notes' far-circle bound and N3's Lipschitz figure; the citation check; the reproduction run; the
    address scan; each by its own lines through _bfig, which
    refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1220.txt' % ACT, r'\*\*v1\.22\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.22.0`s controls')
    bd = _bfig('%s_offlinezero.txt' % ACT, r'\*\*SP4 (REACHED|NOT REACHED AT \S+|STOPPED[^;]*) ; DISPATCHES (\d+) OF (\d+) ; LINES (\d+) AGAINST (\d+-\d+) '
               r'\(THE CEILING (\d+)\) ; NAMES (\d+) OF (\d+)\.\*\*', 'the build bank`s foot')
    gl_ = re.findall(r'^  (G\d)  .+? measured (\d+) ; the estimate (\d+-\d+) ;', rdn('%s_offlinezero.txt' % ACT), re.M)
    if len(gl_) != 7:
        sys.exit('### THE BUILD BANK CARRIES NOT SEVEN GROUP LINES -- NOTHING COMPOSED')
    nb = _bfig('%s_offlinezero_notes.txt' % ACT, r'\(1\) The bound on the far circle: B = (\d+) .*? in place of the plan.s ([\d.]+); .*?MARGIN ([\d.e-]+) against ([\d.e-]+) ',
               'the far circle`s bound (notes (1))')
    lp = _bfig('%s_offlinezero_notes.txt' % ACT, r'\(3\) N3, the Lipschitz figure printed as a proved bound: L_P <= LPq = ([\d.e-]+), lemma (\w+) ', 'N3`s figure (notes (3))')
    am = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], repairs=len(v5[0].split(', ')),
                bd_grade=bd[0], bd_disp=int(bd[1]), bd_max=int(bd[2]), bd_lines=int(bd[3]), bd_est=bd[4], bd_ceil=int(bd[5]),
                bd_names=int(bd[6]), bd_namesof=int(bd[7]),
                far_b=nb[0], far_plan=nb[1], far_margin=nb[2], far_need=nb[3], lp_fig=lp[0], lp_lemma=lp[1],
                bd_groups=[(g_, int(n_), e_) for g_, n_, e_ in gl_], amend_n=len(am),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R353)(3): the kernel rows of one kind as banked (data/b743_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R353): no lean process runs on this host; the runner dispatches those of (R353)(3), fourteen at most, each read by its run id, each
    row carrying free_mb and naming its licensing commit (the author's word at 1f96d4ea); a send the host refused rowed `dispatch_refused`
    and not counted; no suite part in the background. From the command bank (the seat's commands, read live from the capture by the
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
    lic_ = [r for r in _ef_kind(rows_, 'dispatch') if ((r.get('licence') or {}).get('commit') or '') != K.STEPZERO_ANSWERS_FULL]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) + len(refused_) and len(_ef_kind(rows_, 'dispatch')) == len(K.EF_RUNS) <= K.MAX_DISPATCHES \
        and runs_ and not free_ and not lic_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b743_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d (R353)(3)(b) allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b743_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_ANSWERS_FULL[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b743's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b743_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b743_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b743_standing_v1220.txt', '## THE CONTROLS', '### the instances read at their commits'),
               ('data/b743_offlinezero.txt', '## THE CONTROLS', '## THE DISPATCHES'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R353): the plan before any Lean ((R353)(3)(a)); the generator committed before the modules it generates, and the generated
    modules' md5s at zq-b730's tip equal to its output (relay data/b743_offlinezero_notes.txt (4)); every figure bank opens with its
    controls; the (W) regeneration, the pre-lock comparison and the probe-path refusal print before the lock gate. Step zero, v1.22.0's
    commit, the corrigendum's, the plan's, the first Lean commit, the last and the build bank's in that order by time, the plan an
    ancestor of the build bank; the plan bank at HEAD its blob at its last commit (6b282935), its md5 the step zero print's."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (ROOT, K.C1_CORR), (ROOT, K.C2_RELAY), (K.EF_DIR, K.ZQ_FIRST),
              (K.EF_DIR, K.ZQ_TIP), (ROOT, K.PRINT_COMMIT)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C2_RELAY, K.PRINT_COMMIT], capture_output=True).returncode == 0
    md5_ = K.PLAN_MD5 in rdn(K.CITATION_BANK)
    later_ = [h_[:8] for h_ in g(ROOT, 'log', '--format=%H', '%s..HEAD' % K.C2_PLAN_FIRST, '--', K.PLAN_BANK).split() if h_.strip()]
    same_ = _s_md5(os.path.join(ROOT, *K.PLAN_BANK.split('/'))) == K.PLAN_MD5 \
        and rdn(K.PLAN_BANK[len('data/'):]) == g(ROOT, 'show', '%s:%s' % (K.C2_PLAN_FIRST, K.PLAN_BANK)).replace(chr(13), '') and not later_
    # ### b743, N2: the generator before the modules it generates -- each generator commit (relay) older than the zq-b730 commit it fed, and
    # ### the relay commit an ancestor of HEAD; the generated modules at zq-b730's tip by md5 the generator's output (K.GEN_MD5)
    gen_ = [(a_, b_, int((g(ROOT, 'log', '-1', '--format=%ct', a_) or '0').strip() or 0), int((g(K.EF_DIR, 'log', '-1', '--format=%ct', b_) or '0').strip() or 0))
            for a_, b_ in K.GEN_COMMITS]
    genok_ = all(ta_ and tb2_ and ta_ < tb2_ for _a, _b, ta_, tb2_ in gen_) \
        and all(subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a_, 'HEAD'], capture_output=True).returncode == 0 for a_, _b in K.GEN_COMMITS)
    import hashlib as _hl
    md5s_ = dict((m_, _hl.md5(subprocess.run(['git', '-C', K.EF_DIR, 'show', '%s:SIDEExplicitFormula/Schema/ZQ/OffZero/%s.lean' % (K.ZQ_TIP, m_)],
                                              capture_output=True).stdout).hexdigest()) for m_ in K.GEN_MD5)
    md5ok_ = md5s_ == K.GEN_MD5 and all(K.GEN_MD5[m_] in rdn('%s_offlinezero_notes.txt' % ACT) for m_ in ('FrontierData', 'NodesF'))
    # ### the plan before any Lean: its first commit older than zq-b730's first Lean commit
    tp_ = int((g(ROOT, 'log', '-1', '--format=%ct', K.C2_RELAY) or '0').strip() or 0)
    tz_ = int((g(K.EF_DIR, 'log', '-1', '--format=%ct', K.ZQ_FIRST) or '0').strip() or 0)
    route_ = bool(tp_) and bool(tz_) and tp_ < tz_ and genok_ and md5ok_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the plan (relay %s) before the first Lean commit %s: %s; the generator %s committed before each zq-b730 commit it fed: %s (%s); the generated modules at %s by md5 the generator`s output: %s (%s); the plan bank md5 %s, its blob at %s, a later commit touching it: %s -- %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked: %s; the probe-path refusal banked and clear: %s; step zero, v1.22.0, the corrigendum, the plan, the first Lean commit, the last and the build bank in that order by time: %s (%s), the plan an ancestor of the build bank: %s; the tools` controls before their figures: %s' % (
            K.C2_RELAY[:8], K.ZQ_FIRST[:8], bool(tp_) and bool(tz_) and tp_ < tz_, K.GENERATOR, genok_, ', '.join('%s<%s' % (a_[:8], b_[:8]) for a_, b_, _x, _y in gen_), K.ZQ_TIP[:8], md5ok_,
            ', '.join('%s %s' % (m_, h_[:8]) for m_, h_ in sorted(md5s_.items())), K.PLAN_MD5[:8], K.C2_PLAN_FIRST[:8], later_ or 'NONE', same_, regen_, bool(tz),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b743's objects; b742's in git at b742's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b743_standing_v1220.txt', ('ALL AS WANTED',)), ('b743_offlinezero.txt', ('SP4 REACHED', 'DISPATCHES 7 OF 14', 'NAMES 30 OF 30')),
             ('b743_corrigendum.txt', ('ITEMS',)), ('b743_citation_check.txt', ('THE CHECK CLEAN',)), ('b743_reproduce.txt', ('REPRODUCES',)), ('b743_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R353): SP4 prints REACHED, NOT REACHED or STOPPED, and every printed name its axiom print in full; the Lipschitz figure printed as
    a proved bound with its lemma's name (notes (3)) and in the entry; the entry's nouns are the banks'; no sentence says RH or GRH holds or
    fails save in a negation; no comparative sentence contradicts the table it cites (the citation check's comparative read); the root prompt's sentences about the entry
    are the composer's. From the banks' last lines, the build bank's axiom section, the entry's sentences and the root prompt in the
    answers bank (standing.rootprompt.entry_unbacked)."""
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
    bt_ = rdn('%s_offlinezero.txt' % ACT)
    ax_ = 'propext, Classical.choice, Quot.sound'
    built_ = re.findall(r'^  (G\d)  ([\w.]+)\s+(propext.*)$', bt_, re.M)
    sp_ = len(built_) == 30 and all(a_.strip() == '%s (run %d)' % (ax_, K.EF_RUNS[-1]) for _g, _n, a_ in built_) \
        and re.search(r'\*\*SP4 (REACHED|NOT REACHED AT|STOPPED)', bt_) is not None \
        and re.search(r'(?m)^\(3\) N3, the Lipschitz figure printed as a proved bound: L_P <= LPq = %s, lemma %s ' % (re.escape(f['lp_fig']), f['lp_lemma']),
                      rdn('%s_offlinezero_notes.txt' % ACT)) is not None
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None|Nothing)\b'
    loc_ = [s_ for s_ in sents if re.search(r'\b(?:RH|GRH)\b.*\b(?:holds|fails|proved|refuted)\b', s_) and not re.search(neg_, s_)]
    nouns_ = [w_ for w_ in ('SP4', 'zq_offline_zero', 'zq_li_nonneg_fails', f['lp_fig'], f['lp_lemma'], f['far_b'], f['far_margin'], str(f['bd_disp']), str(f['bd_lines']),
                            'data/%s_offlinezero.txt' % ACT, 'data/%s_s6_plan.txt' % ACT) if w_ not in text]
    cmp_ = re.search(r'COMPARATIVE[^\n]*CONTRADICTS (\d+)', rdn(K.CITATION_BANK))
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and sp_ and not loc_ and not nouns_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; SP4 graded, every printed name of the build with the standard three in full, and the Lipschitz figure a proved bound with its lemma (relay data/b743_offlinezero.txt, notes (3)): %s; read from %s, a sentence saying RH or GRH holds or fails outside a negation: %s; the build bank`s nouns absent from the entry: %s; the citation check`s comparative line: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), sp_, src, loc_ or 'NONE', nouns_ or 'NONE', cmp_.group(0) if cmp_ else 'NO COMPARATIVE SENTENCE IN THE ACT`S BANKS READ', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))   # ### the entry`s nouns the banks`: SP3, the open row and the built terminal, the figures, the two banks
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R353) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R353)(5))
# ### (R353)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R353) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b742's form, carried) -- read from git,
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
    # ### (R353)(3), (5), N5: no ref of any kernel carrying a commit made after the act's opening commit (no kernel touched); no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b742 left them; the address scan's count from its bank (relay data/b743_address_scan.txt), the suite's arm recounting it live;
    # ### the five records and no other (the read-back bank), no gh repo edit in the capture, the token in none of the act's files (read from the environment, never printed)
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if not (kn in K.SITTING_TIPS and r_[0] in ('refs/heads/main', 'refs/heads/' + K.SITTING_BRANCH) and r_[1].startswith(K.SITTING_TIPS[kn])):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R353)(3)(c), N5: no Zenodo write, no GitHub description, no release, no new version in the capture; no zenodo route of the act's
    ghe_ = [r_['n'] for r_ in (jl('%s_commands.json' % ACT).get('rows') or []) if re.search(r'\bgh\s+repo\s+edit\b|\bgh\s+release\b|/actions/newversion|zenodo\.org/api', r_.get('cmd') or '')]
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b743_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit, release, a new version or a Zenodo route in the capture: %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghe_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b743 — lane two, act one hundred and sixty-nine, the frontier act under (R353): b742 at its weight and its corrigendum; v1.22.0; '
            'W-ORD-ZQ-OFFLINE-ZERO, S6 on the interpolation route on Λ_Q by the author`s word, SP4 REACHED on route (K)')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form; every figure from the banks (the build bank's foot, v1.22.0's
    controls) and the two SP4 statements read from SP4.lean at zq-b730's tip (each a theorem of that name)."""
#⟪END⟫
#⟪SECTION record 31⟫
    if f['bd_grade'] != 'REACHED' or f['bd_names'] != f['bd_namesof']:
        sys.exit('### THE TITLE`S FORM IS THE REACHED ONE AND THE BANK READS %s, NAMES %s OF %s -- NOTHING COMPOSED' % (f['bd_grade'], f['bd_names'], f['bd_namesof']))
    sp4_ = g(K.EF_DIR, 'show', '%s:SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean' % K.ZQ_TIP)
    n_st = len(re.findall(r'(?m)^theorem (?:zq_offline_zero|zq_li_nonneg_fails)\b', sp4_))
    if n_st != 2:
        sys.exit('### SP4.LEAN AT %s CARRIES %d OF THE TWO STATEMENTS -- NOTHING COMPOSED' % (K.ZQ_TIP[:8], n_st))
    return ('## W-ORD-ZQ-OFFLINE-ZERO, S6: the route on Λ_Q by interpolation, the two ruled routes stopped, by the author’s word; SP4 REACHED, zq_offline_zero and zq_li_nonneg_fails compiled; '
            '%s dispatches of %s, %s lines; %d names on the standard three; %d repairs landed' % (
                f['bd_disp'], f['bd_max'], f['bd_lines'], f['bd_names'], f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the far circle`s bound B = %s as built (Strip.lean lamF_sphere_le), in place of the plan`s %s, carried in the margin: MARGIN %s against %s (relay data/b743_offlinezero_notes.txt (1)); (2) the generated modules NodesF and FrontierData made by tools/b743_s6gen.py, committed at relay 22f8d6b1, 6467c061 and 3194b6eb before each zq-b730 commit it fed, its output equal by md5 to each module at %s (notes (4)); (3) the plan`s dated note (7.1) appended at 6b282935 after the plan`s commit f15c3a8d and before any Lean, no row of (0)-(6) rewritten (relay data/b743_s6_plan.txt (7)); (4) the step bank written at Component 4 for step zero and components 1-3, each row`s time its last commit`s (relay data/b743_steps.json, defect (m)); ' % (
                f['far_b'], f['far_plan'], f['far_margin'], f['far_need'], K.ZQ_TIP[:8])
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R353)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b743's objects; b742's composer in git at
    b742's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot, not the seat's row quoting b742's (defect (a'))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R352)(2)(v)
    e = ['', _title(), '',
         'SP4 of W-ORD-ZQ-OFFLINE-ZERO is REACHED on zq-b730 of SIDE-explicit-formula at %s, off main and untagged, six commits from %s: zq_offline_zero : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1/2, and zq_li_nonneg_fails : ¬ (∀ n : ℕ, 0 ≤ Wide.liCoeff zqZeroConfig n), each depending on axioms [propext, Classical.choice, Quot.sound] (run %d); %s of %s printed names compile on the standard three. The route is S6 on Λ_Q by interpolation, taken by the author’s word amending (R353)(3) (relay data/b743_author_answers.txt :7), the two ruled routes STOPPED by the three-times rule before any Lean: F = lamM z + lamM (1 − z) − 1/(z (1 − z)) sampled at 20 nodes on the circle of radius 49/100 about 1/2 + 16.290216 i, inside the strip, the discrete Cauchy polynomial bounding F on the frontier of box A from below by 1/10^12, and ‖F cA‖ ≤ 6/10^13 at the centre, so the minimum-modulus lemma gives the zero. The checking route (K), every numeric fact decided by the kernel over rational certificates. %s lines against %s, within the three-times ceiling of %s; %s of the %s dispatches spent, each read by its run id. The draft stands at v5, HELD.' % (
             K.ZQ_TIP[:8], K.ZQ_ENTERING[:8], K.EF_RUNS[-1], f['bd_names'], f['bd_namesof'], f['bd_lines'], f['bd_est'], f['bd_ceil'], f['bd_disp'], f['bd_max']), '',
         'One deviation from the plan: the bound on the far circle came out B = %s as built (Strip.lean lamF_sphere_le, from norm_lamM_le_58 and the pole term) against the plan’s %s, and the margin still clears: MARGIN %s against %s (FrontierData.lean margin; relay data/b743_offlinezero_notes.txt (1)).' % (
             f['far_b'], f['far_plan'], f['far_margin'], f['far_need']), '',
         '*Filed at b743 on the author’s ruling `(R353)`; %d question%s put to the author. Banks: relay '
         '`data/b743_corrigendum.txt`, `data/b743_standing_v1220.txt`, `data/b743_rules.txt`, `data/b743_s6_plan.txt`, `data/b743_s6_price.txt`, `data/b743_offlinezero.txt`, `data/b743_offlinezero_notes.txt`, `data/b743_dispatch_rows.json`, `data/b743_prelock.txt`, `data/b743_pathrefusal.txt`, '
         '`data/b743_reproduce.txt`, `data/b743_address_scan.txt`, `data/b743_touch.txt`, `data/b743_standing_figures.txt`, `data/b743_report.txt`; the generator `tools/b743_s6gen.py`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R353)(1)-(2), %s, %s, %s): b742 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b742’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b743_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b743_standing_v1220.txt); the dispatch’s licence '
         'at their head: every dispatch row carries the commit of the author’s word, read before `gh workflow run` is called (relay data/b743_rules.txt (1)).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): the build bank opens with its controls before its figures, the S6 plan bank among them at md5 %s, the step zero print’s. tools/standing/ v1.22.0 at %s, the weight and the corrigendum at PLACE-papers %s and their banks at %s, (2) whole before (3); the plan at %s, its dated note (7.1) at %s, before the first Lean commit %s on zq-b730 from %s; the generator tools/b743_s6gen.py committed at relay 22f8d6b1, 6467c061 and 3194b6eb, each before the Lean commit holding what it generated; the last Lean commit %s, then the build bank at %s. The step bank was not written at step zero or components 1-3 and was rowed at Component 4 from the commits as logged (defect (m)). No lean process on this host; %s dispatches, each row carrying free_mb and the licence 1f96d4ea, each read once by its run id (relay data/b743_dispatch_rows.json).' % (
             K.PLAN_MD5[:8], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_RELAY[:8], K.C2_PLAN_FIRST[:8], K.ZQ_FIRST[:8], K.ZQ_ENTERING[:8], K.ZQ_TIP[:8], K.PRINT_COMMIT[:8], f['bd_disp']), '',
         '**The plan before any Lean** ((R353)(3)(a) as amended): the two ruled routes priced and STOPPED before any Lean -- a Lipschitz cover of the frontier wanting 1.78e11 points for F and 3.27e11 for zqFn, each more than nine orders over three times the plan’s figure; the interpolation route taken, ρ = 49/100, M = 20, R = 3; the author’s five items printed: the farthest frontier point, r = 5623/10000 at the right corners, and the error bound there; the amplification A = 99.51 and the per-sample δ it forces; the frontier’s Re z > 1 part, bounded by the polynomial alone; the margins in one line; and the aliasing lemma stated generally; 3,970-6,810 lines and 8-17 dispatches against the cap of 14 (relay data/b743_s6_plan.txt, data/b743_s6_price.txt). Its dated note (7.1), the aliasing lemma built through the Cauchy integral formula in place of the power series, appended before any Lean, no row of (0)-(6) rewritten.', '',
         '**The certificate to SP4** ((R353)(3)(b) as amended, N1, N3): Frame.lean, F, its differentiability, zqFn written through F (zqFn_eq_lamF), the minimum-modulus and Li corollaries over F; Interp.lean, the discrete Cauchy identity and the aliasing bound over a primitive root of unity; Amplify.lean, the polynomial’s Lipschitz step; Strip.lean, the bound on the far circle; NodeBase.lean and Nodes0-3.lean, lamM at the 20 nodes, the mid shells bounded shell by shell; NodesF.lean and FrontierData.lean, generated by tools/b743_s6gen.py, the node values, the rounded coefficients, the Lipschitz figure L_P ≤ %s (lemma %s, N3: a proved bound) and 80 check points decided by the kernel; Omega.lean, the nodes and the grid; Frontier.lean, the frontier bound lamF_frontier_ge; SP4.lean, the two statements. %s lines in all against %s, the ceiling %s; per group %s; NAMES %s OF %s (relay data/b743_offlinezero.txt, notes (1)-(7)).' % (
             f['lp_fig'], f['lp_lemma'], f['bd_lines'], f['bd_est'], f['bd_ceil'], ', '.join('%s %d against %s' % g_ for g_ in f['bd_groups']), f['bd_names'], f['bd_namesof']), '',
         '**The dispatches** (N1): %s of %s -- G1 BREAKS on three errors; G0-G3 BREAKS on seven; G2-G4h, through NodeBase, KERNEL; the whole build sent with bare module names, stopped at an unknown target, a dispatch spent on the seat’s own string (defect (k)); the whole build BREAKS on nine errors (a simp that turned ofReal cos into Complex.cos, casts from ℚ, a generated section left open); BREAKS on five (the check points’ bound variable read over ℚ, which no Decidable instance decides, and edge goals left open in Frontier.lean); KERNEL, SP4. One send before the fourth was refused by GitHub with HTTP 500, made no run and is not counted (defect (j)). Each row carries free_mb (relay data/b743_dispatch_rows.json, notes (5)).' % (f['bd_disp'], f['bd_max']), '',
         '**The git writes** (N5): one git write per message, add and commit in separate messages, across the relay, PLACE-papers, the kernel clone D:/zq-b738 and the kernel tree D:/SIDE-explicit-formula; the act read by the suite’s arm over the capture.', '',
         '**What this act is not**: no deposit, no new version, no Zenodo field, no GitHub description; no tag, no draft published, no merge, no kernel’s main touched; every Lean file of the act on zq-b730 alone. SP4 is a statement about zqZeroConfig, the zeros of Λ_Q with their orders as the kernel defines them (Zeros.lean): a zero of Λ_Q off the line, in box A, and Li nonnegativity failing for it; nothing is stated of ζ or of any L-function. Nothing here proves or refutes RH or GRH.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b743_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b743_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b743_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b743 -- %s, %s, %s, %s -- against b742’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b743_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the plan and the build read one way: the plan priced the route the build took, its %s lines against the %s measured; where the build departed from the plan’s figure -- the far circle’s B = %s against %s -- the margin absorbed it and the bank prints both; each bank is read as committed, its slips noted beside it (plan (7.1), defects (h)-(m)).' % (f['bd_est'], f['bd_lines'], f['far_b'], f['far_plan']), '',
         '**Carried to:** %s, named by the author ((R353)(6)); W-ORD-ZQ-OFFLINE-ZERO with SP4 REACHED, its state the author’s to rule; the wave 1 deposit; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails; the zero shown is a zero of Λ_Q, in box A.*', '']
    return _title(), NL.join(e)


def _finding_text_b742():
    """b742's form over b742's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b743's objects; b742's composer in git at b742's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD, W-ORD-ZQ-DERIVES closed at b736 and W-ORD-ZQ-OFFLINE-ZERO open, SP4 reached,
    its discharge the author's to rule."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-ZQ-DERIVES' in op or 'W-ORD-ZQ-OFFLINE-ZERO' not in op:
        sys.exit('### THE TRAIL: THE DISCHARGED ORDER READ OPEN, OR THE ENTERED ORDER NOT -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R353) ratified.** Its components as the ferry orders them (relay data/b743_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b742’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** W-ORD-ZQ-OFFLINE-ZERO (priced at OPEN_TRAILS :%d): S6 built on Λ_Q by interpolation on zq-b730 at %s, route (K); SP4 %s, zq_offline_zero and zq_li_nonneg_fails compiled on the standard three; the far circle’s B = %s against the plan’s %s, MARGIN %s against %s; the order OPEN, its discharge the author’s to rule.' % (
                 K.PRICE_LINE, K.ZQ_TIP[:8], f['bd_grade'], f['far_b'], f['far_plan'], f['far_margin'], f['far_need']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b743_standing_v1220.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The build:** SP4 %s; names %s of %s, each with the standard three (run %d); N3: L_P ≤ %s, lemma %s; %s lines against %s, the ceiling %s; %s dispatches of %s (relay data/b743_s6_plan.txt, data/b743_offlinezero.txt, data/b743_offlinezero_notes.txt, data/b743_dispatch_rows.json).' % (
                 f['bd_grade'], f['bd_names'], f['bd_namesof'], K.EF_RUNS[-1], f['lp_fig'], f['lp_lemma'], f['bd_lines'], f['bd_est'], f['bd_ceil'], f['bd_disp'], f['bd_max']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b743_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b743_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b743_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b743 `%s` (previous `%s`, b742’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b743_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b743_standing_v1220.txt); the standing '
             'report tool (relay data/b743_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** zq-b730 of SIDE-explicit-formula from %s to %s, six commits, fourteen Lean files under Schema/ZQ/OffZero (Interp, Frame, Strip, Amplify, NodeBase, Omega, Nodes0-3, NodesF, FrontierData, Frontier, SP4) and print_targets.txt, off main, untagged; no kernel’s main touched; %d dispatches; the %s branches as b742 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.ZQ_ENTERING[:8], K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b743_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b742’s %s, %s, %s, %s (relay data/b743_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b743_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b742():
    """b742's trail record over b742's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: eight sends, one refused by the host with HTTP 500 (no run, not counted), seven of the fourteen (R353)(3)(b) allows; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725 and detect-b729 kept, unmoved; zq-b730 at the build`s tip; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b742 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b730-b742`s and this act`s fourteen (Interp, Frame, Strip, Amplify, NodeBase, Omega, Nodes0-3, NodesF, FrontierData, Frontier, SP4); MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R353)(5): relay push-b742-closing, push-b742-preroot, push-b742-record; PLACE-papers push-b742-preroot, push-b742-record; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: fourteen Lean files and print_targets.txt alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R353) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from PLACE-papers main before the act`s own commits (efce669f, b742`s record) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R353)(2): FINDINGS :13619.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R353)(2): row (62).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-OFFLINE-ZERO entered at b737 (OPEN_TRAILS :17400), open, SP4 reached this act.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b743_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.22.0`s controls, the build bank, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none alone: the S6 plan committed at f15c3a8d with its price bank and the worklist`s line, before any Lean file (N2).'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none named; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: the build bank first committed after the plan and the last Lean commit (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### fourteen on zq-b730 (Interp, Frame, Strip, Amplify, NodeBase, Omega, Nodes0-3, NodesF, FrontierData, Frontier, SP4), N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R353)(2): tools/standing/ to v1.22.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b743_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, the gh reads, the eight workflow sends (seven dispatches, one refused by the host) and their artifact downloads under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### (R353)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b743_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b743_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1220', 'offlinezero', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b743_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b743_registration_%s.txt -- b743, THE FRONTIER ACT: b742 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.22.0; W-ORD-ZQ-OFFLINE-ZERO S6 ON Λ_Q BY INTERPOLATION BY THE AUTHOR`S WORD, SP4 REACHED ON ROUTE (K); "
                             "NO DEPOSIT, NO NEW VERSION, NO MERGE, NO TAG, UNDER (R353)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b742's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b743: b742's lines read banks this
act does not write, and are not carried; the lines are b743's: S6 built and SP4 REACHED (KERNEL, the names compiled, the two
statements' axioms printed), tools/standing/ v1.22.0 by its controls (CERTIFIED), the far circle's bound against the plan's with the
margin, and N3's Lipschitz figure (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b743's lines, each from the record tool's figures over b743's banks
    # ------------------------------------------------------------------ KERNEL: (R353)(3) as amended, S6 on zq-b730, SP4 graded
    sz = seat('%s_offlinezero.txt' % ACT, '**SP4 ')
    sk = sz   # ### (R352)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO S6 TO SP4: SP4 %s, zq_offline_zero and zq_li_nonneg_fails on propext, Classical.choice, Quot.sound; names compiled %s of %s on the standard three; %s lines against %s (the ceiling %s); on zq-b730 at %s; %s dispatches of %s. SOURCE %s.' % (
        f['bd_grade'], f['bd_names'], f['bd_namesof'], f['bd_lines'], f['bd_est'], f['bd_ceil'], K.ZQ_TIP[:8], f['bd_disp'], f['bd_max'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.22.0 ((R353)(2)), by its controls
    sw = seat('%s_standing_v1220.txt' % ACT, '**v1.22.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.22.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the far circle's bound against the plan's, from the notes
    so = seat('%s_offlinezero_notes.txt' % ACT, '(1) The bound on the far circle: B = ')
    seats.append(so)
    keys['ORD'] = ('REGISTERED -- THE FAR CIRCLE`S BOUND AS BUILT: B = %s against the plan`s %s; MARGIN %s against %s; N3: L_P <= %s, lemma %s. SOURCE %s.' % (
        f['far_b'], f['far_plan'], f['far_margin'], f['far_need'], f['lp_fig'], f['lp_lemma'], so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R353)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]   # ### b743's four lines
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b743 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
