# -*- coding: utf-8 -*-
# b749 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R359)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R359)(2) repair it carries. Edited by the Edit tool. Carried at b749 by tools/b749_fold.py (`carry`) from tools/acts/b748.py,
# b748`s names substituted; the citation`s sections adopted from tools/b749_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b748`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b748`s carried till
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
# ### b749, Component 1: THE c1 ROUTE FOR b748'S WEIGHT LINE AND ITS CORRIGENDUM, (R359)(1) and (3). Rewritten at b749 against
# ### b748's own banks (scratch c1sec749.txt, spliced): the closing's lines by needle, the events (5), the defects (18, (i) the navigator's),
# ### the refusals (13 lines at 71bc497a), the v1.29.0 controls and the rules this corrigendum lands. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '71bc497a'          # ### b748's closing push tip, the public relay's main at step zero
C1_CLOSING_COMMIT = '9e3970df'      # ### b748's closing commit (its closing row)
C1_REFUSAL_AT = '71bc497a'          # ### its refusal bank read at its closing push tip
C1_NOTED = '2026-11-09'
C1_CORRIGENDA_LAST = 68
C1_V170 = 'b749_standing_v1290.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.29.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-09 by b749 to b748’s entry (:%d), under `(R359)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## THE_EPSTEIN_CONTROL_OBJECT §3 passed'
C1_TRAIL_NEEDLE = '### b748 — lane two, act one hundred and seventy-five'
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
    for l in _c1_rd('b748_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b748_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b748_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b748_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b748_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b748_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b748_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b748_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    lost = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if k_ not in held]
    if len(held) != 7 or lost != ['N5'] or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b748_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) (HELD) \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the record-time scores')
    ar = json.load(open(os.path.join(D, 'b748_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b748_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (ci_, cc_, cl_, cr_), l_co = _c1_fl(c, r'^    the generated entry for b747`s events and defects.*: ITEMS (\d+): .*; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ; ', 'b747`s corrigendum')
    (va, vb), l_v = _c1_fl(c, r'^    tools/standing/ at v1\.28\.0: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.28.0 foot')
    (wa, wb), l_w = _c1_fl(c, r'^    tools/standing/ at v1\.28\.1: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.28.1 foot')
    (s3w, s3c, s3p), l_s3 = _c1_fl(c, r"^    §3, the five discharges.*: \[S3\] PASSED WITH THE AUTHOR`S CLAUSE: §3 WRITTEN, ([0-9,]+) WORDS, (\d+) CITES, PLACE-papers ([0-9a-f]{8})$", 'section 3')
    (s4w, s4c, s4p), l_s4 = _c1_fl(c, r"^    §4, the three premise-free forms.*: \[S4\] PASSED WITH THE AUTHOR`S CLAUSE: §4 WRITTEN, ([0-9,]+) WORDS, (\d+) CITES, PLACE-papers ([0-9a-f]{8})$", 'section 4')
    (_ln,), l_ln = _c1_fl(c, r'^    the INTEGRATION line .*: THE LINE: (COMPOSED) ; FROM REGISTRY 1\.5c-21 TO 1\.5c-23 AND SPIRAL_MAP §2D ;', 'the line')
    (_tg,), l_tg = _c1_fl(c, r'^### THE KERNELS: .*(no tag beyond v0\.38)', 'the tag')
    _mv, l_mv = _c1_fl('b748_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-08-b748)\.zip ; ', 'the mirror`s archive')
    _aw1, l_aw1 = _c1_fl('b748_author_answers.txt', r'^(Synthesis sitting at b750, taking with it the front-door sitting’s items .* as its opening control\.)$', 'the author`s answer')
    (ca,), l_ca = _c1_fl(c, r'^    \(a\) ### \*\*THE NEXT, \(R358\)\(4\) AND \(8\)\*\*: (the Tier 3 act over the held v1\.2\.0 draft 23228113 per \(R358\)\(4\))', 'the carried item (a)')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 6)) or len(dr) != 18 or (int(sd), int(se)) != (18, 5):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b748 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b748_closing.txt):* “%s” (data/b748_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b748_steps.json, the record and closing rows). As its rows read: b747’s corrigendum, items %s, CLAIM %s, CLOSE %s, REPEAT %s (:%d); '
            'standing tools v1.28.0, %s of %s (:%d), and v1.28.1, %s of %s (:%d); the paper’s §3 passed with the author’s clause, %s words, %s cites, PLACE-papers %s (:%d; relay data/b748_section3.txt), '
            'and §4, %s words, %s cites, PLACE-papers %s (:%d; relay data/b748_section4.txt); the INTEGRATION line %s from REGISTRY 1.5c-21 to 1.5c-23 and SPIRAL_MAP §2D (:%d; relay data/b748_line.txt); '
            '%s (:%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), the failing declared on the face; the record-time scores every one HELD (:%d), '
            'N3, S1 and S2 written PENDING before the root (data/b748_events.txt (5)), and at the scores’ close SCORES %d OF 8 HELD, %s REFUTED on its one clause “one git write per message” '
            '(data/b748_scores_close.json; data/b748_events.txt (2)). The root %s over %s banks, chained from %s (data/b748_act_root.json; :%d); the mirror %s at %s (data/b748_mirror_verify.txt :%d; :%d); '
            '%s prompts banked as put by the seat (:%d), the author’s answer at the root “%s” (data/b748_author_answers.txt :%d); the closing’s carried item (a): %s (:%d), this act under `(R359)`(2). '
            '%d events in data/b748_events.txt, rows (1)-(%d), entered after the lock; %d defects, (a)–(r) (data/b748_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects '
            'together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. Nothing deposited, no merge, no new Zenodo version; the corrigendum for these rows follows, under `(R359)`(3).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, ci_, cc_, cl_, cr_, l_co, vb, va, l_v, wb, wa, l_w, s3w, s3c, s3p, l_s3, s4w, s4c, s4p, l_s4, _ln, l_ln,
                _tg, l_tg, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, l_sl, len(held), ' and '.join(lost),
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, _aw1[0], l_aw1, ca, l_ca, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b748's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '21:25:10Z', 'defect (a)'), (2, 'READ', '21:25:42Z', 'defect (a)'), (3, 'READ', '21:25:43Z', 'defect (a)'), (4, 'READ', '21:53:58Z', 'defect (e)'),
               (5, 'PIPE', '21:56:03Z', 'defect (e)'), (6, 'REDIR', '21:56:41Z', 'defect (e)'), (7, 'ENV', '22:13:36Z', 'defect (f)'), (8, 'READ', '23:33:24Z', 'defect (m)'),
               (9, 'PIPE', '23:34:25Z', 'defect (m)'), (10, 'READ', '00:15:50Z', 'defect (p)'), (11, 'PIPE', '00:47:50Z', 'defect (p)'), (12, 'READ', '03:56:06Z', 'event (1)'),
               (13, 'GITWRITE', '04:12:16Z', 'event (2)')]
C1_UNROWED = []
C1_ENTERED = []   # ### no post-closing refusal of b748's: b749's hook bank opens at its own step zero, every line b749's own
C1_FLIP = {}      # ### (R359)(3) flips no tag: each item read as its bank tags it
C1_CARRIED = []   # ### (R359)(3) letters no carried item: the 23 rows are b748's banks whole
C1_CORR_TITLE = ('## Corrigendum to b748’s record (relay data/b748_events.txt rows (1)-(5) and data/b748_defects.txt): five events and eighteen defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; one call of the tool per message, the per-commit scan’s own bank, no commit without the scan, the record’s readers refusing a missing path, the carry row by row and the '
                 'kept row by the tool, a prior act’s log by its step rows, the retry rule, the refusals, at tools/standing/ v1.29.0, each controlled, under (R359)(3)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.29.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_rules_line(n):
    t = _c1_rd('b749_rules.txt').split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith('(%d) ' % n)]
    if len(h) != 1:
        sys.exit('### THE RULES BANK: %d LINES OPEN (%d), NOT ONE -- NOTHING COMPOSED' % (len(h), n))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b748_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)   # ### 13 lines at 71bc497a
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
    (cc, cd), _l = _c1_fl('b748_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.29.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(5)', sorted(ev) == list(range(1, 6))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 18', len(dr) == 18), ('the refusals 13, each answered as listed', len(rl) == 13 and not bad_ref),
                              ('the navigator`s (i)', [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"] == ['i']),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.29.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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
    """the counter as this corrigendum reads the items: the closing's 23, no carried item, no tag flipped."""
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


# ### the repairs each item is met by at v1.29.0 (the controls bank data/b749_standing_v1290.txt, the rules data/b749_rules.txt)
C1_EV_EXTRA = {1: '; repair (refusals), `(R359)`(3)(x), REPEAT, the instance printed',
               2: '; repair (calls), `(R359)`(3)(i): the one-call tool refuses a call while another git write landed in the same message, the bare add counted',
               3: '; the retry rule, `(R359)`(3)(viii): each retry an event with two timings (relay data/b749_rules.txt (8))',
               4: '; the retry rule, `(R359)`(3)(viii): a reader failing twice on one repository runs alone before the part is re-run',
               5: '; `(R359)`(3)(ix): no change, the close reads once'}
C1_DF_EXTRA = {'a': '; repair (refusals), `(R359)`(3)(x), REPEAT', 'b': '; repair (plain), `(R359)`(3)(iii): the commit tool runs the scan itself, a commit without it refused',
               'c': '; repair (carry), `(R359)`(3)(v): the carry prints every carried row beside the ruling and refuses an unnamed one',
               'd': '; repair (calls), `(R359)`(3)(i): the bare add is a git write', 'e': '; repair (refusals), `(R359)`(3)(x), REPEAT',
               'f': '; repair (refusals), `(R359)`(3)(x), REPEAT', 'g': '; repair (log), `(R359)`(3)(vi): a prior act’s log read to its lock, its commits by step rows',
               'h': '; the tool’s own refusal as designed, no repair', 'i': '; the navigator’s, entered as the navigator’s',
               'j': '; repair (reader), `(R359)`(3)(iv): every reader of the record refuses a nonexistent path and prints it',
               'k': '; repair (calls), `(R359)`(3)(i)', 'l': '; repair (log), `(R359)`(3)(vi)', 'm': '; repair (refusals), `(R359)`(3)(x), REPEAT',
               'n': '; repair (carry), `(R359)`(3)(v)', 'o': '; repair (carry), `(R359)`(3)(v): the step-zero KEPT row written by the tool from the branch listing',
               'p': '; repair (refusals), `(R359)`(3)(x), REPEAT', 'q': '; `(R359)`(3)(vii): the gate sent before its bank, the instance printed (REPEAT)',
               'r': '; repair (scanbank), `(R359)`(3)(ii): the per-commit scan writes its own appended bank'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b749, to `(R359)`(3)(i) and (iii): from relay 921ac933 the hook refuses a git write by plain git (PLAINGIT) and records every shell call with its message’s request '
            'stamp, and the one-call tool reads that record before it writes; b749’s own writes after that commit run through the tool alone (relay data/b749_standing_v1290.txt, the (calls) and (plain) blocks).',
            'Dated note, b749, to `(R359)`(3)(ii): the act’s scan bank is written once at its step and the post-lock bank after the lock; the scan before each commit lands in '
            'data/b749_address_scan_commits.txt, an excluded kind of the root route, so the root’s dry run reads the committed banks with no restore (relay data/b749_standing_v1290.txt, the (scanbank) block).')
C1_CLASSES = (
    ('calls', 'one call of the tool per message (`(R359)`(3)(i), event (2), defects (d), (k))', 'the hook records each shell call with its message’s request stamp; commit.py refuses a call while another git write was allowed in the same message, the bare add counted. b748’s root message replayed, the second call refused after and not before', 'bank'),
    ('scanbank', 'the per-commit scan’s own bank (`(R359)`(3)(ii), defect (r))', 'the scan before each commit runs without --bank and appends to data/<act>_address_scan_commits.txt; the act’s scan bank, which the root names, unchanged across a commit. The route before passed --bank and b748’s gate commits carried the rewritten bank', 'bank'),
    ('plain', 'no commit without the scan (`(R359)`(3)(iii), defects (b), (d))', 'run() takes no scanner=False and the hook refuses a git write by plain git. be4a5a0d’s plain add and a plain commit allowed before, refused after; a scratch commit with the scan skipped committed before, refused after', 'bank'),
    ('reader', 'the record’s readers refuse a missing path (`(R359)`(3)(iv), defect (j))', 'relaypath.rows_of and grep_of refuse a file the repository does not hold, printing it, and print each read’s rows and count. The grep of CLUSTERS.md read NONE before, refused after; SPIRAL_MAP :264-:286 read with its 23 rows', 'bank'),
    ('carry', 'the carry row by row, the kept row by the tool (`(R359)`(3)(v), defects (c), (n), (o))', 'carry.py ruled prints each carried citation row and refuses (R4) a commit the ruling does not name; carry.py kept writes the KEPT row from the branch listing. b748’s carried sections refused 0 before, 3 after; port-b707 absent from the hand row, named in the tool’s', 'bank'),
    ('log', 'a prior act’s log by its step rows (`(R359)`(3)(vi), defects (g), (l))', 'tools/standing/actlog.py takes a prior act’s commits from its step bank, to its lock. b747’s gate commits 3 by grep (88f39b22 absent) before, 6 after; its step-rows commits 7 by grep with 0c118109 before, 3 without it after', 'bank'),
    ('retry', 'the remote-read retry (`(R359)`(3)(viii), events (3), (4))', 'each retry an event with two timings; a reader failing twice on one repository runs alone before the part is re-run', 8),
    ('refusals', 'the hook’s refusals and the gate before its bank (`(R359)`(3)(vii), (x), REPEAT)', 'the instances printed from b748’s refusal bank, thirteen lines, each recorded by a row; (q) printed', 10),
    ('version', 'the version (`(R359)`(3)(xi))', 'tools/standing/VERSION v1.29.0, landed by a commit of its own (%s) with its controls bank and the record’s dry over it, before the gate' % K.C1_STANDING, 'bank'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b748’s events bank (relay data/b748_events.txt) carries five rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank eighteen lettered rows, (a)-(r), each tagged in its own bracket (%s), (i) the navigator’s; its refusal bank thirteen lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R359)`(3), at tools/standing/ v1.29.0, each with a control on b748’s banks or the trail as it stands, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s; the rules relay data/b749_rules.txt):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what, where in C1_CLASSES:
        at_ = ('relay data/%s :%d' % (C1_V170, _c1_v170_line('### (%s) ' % k_))) if where == 'bank' else ('relay data/b749_rules.txt (%d), :%d' % (where, _c1_rules_line(where)))
        if k_ == 'version':
            at_ = 'relay data/%s :%d' % (C1_V170, _c1_v170_line('### (version) '))
        L += ['**(%s) %s** -- %s (%s).' % (k_, name, what, at_), '']
    L += ['**b748’s events (1)-(5):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b748_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, ''))]
    L += ['', '**b748’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b748_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b748’s refusals** (relay data/b748_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (five events, eighteen defects), as b748’s closing prints it (relay data/b748_closing.txt :5); '
          'no tag is read otherwise here; the CLAIM items %s.' % (nc, nl_, rep, n, n, ', '.join(claims) or 'none'), '',
          '*Filed at b749 on the author’s ruling `(R359)`(3): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b749.py) from '
          'b748’s events and defects banks read unedited, its refusal bank, the v1.29.0 controls bank and the rules; banked as relay `data/b749_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b748’s record; no sealed tool, face, trail or root-named bank of b748 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b749 -- THE CORRIGENDUM FOR b748, (R359)(3) (%s)' % utc(), '',
             '### the banks read unedited: data/b748_events.txt rows (1)-(5), data/b748_defects.txt 18 rows, data/b748_hook_refusals.txt 13 '
             'lines at %s; data/%s (the v1.29.0 controls); data/b749_rules.txt; the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 5, DEFECTS 18 ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE NAVIGATOR`S 1 ; DATED NOTES %d ; v1.29.0: ONE CALL OF THE TOOL PER MESSAGE, THE PER-COMMIT SCAN`S OWN BANK, '
               'NO COMMIT WITHOUT THE SCAN, THE RECORD`S READERS REFUSING A MISSING PATH, THE CARRY ROW BY ROW AND THE KEPT ROW BY THE TOOL, A PRIOR ACT`S LOG BY STEP ROWS, THE RETRY RULE, THE REFUSALS, '
               'THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b748 at its weight after its entry, and the corrigendum for b748, landed through b698's guarded
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
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.29.0', bank='data/' + C1_V170, rules='data/b749_rules.txt'),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b749, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b749, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b749's name.
# ### b749's own changes are marked "b749, Component 3". The runner overrides read the act's dispatch rows: (R359)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b749_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R358)(7), as b748 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """N1, b749 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b749: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b749, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R359)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b748, naming tools/standing/hook.py, unedited this act (its last edit b748`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b749, C4, defect (n) (the Edit tool): the step-zero bank writes each deleted ref's tip as "(was 7d34b587)" (data/b749_stepzero.txt :44-:45),
# ### b748's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b748-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b749, Component 3 (the Edit tool): b749's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b748-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b749_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b749_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b749, Component 6 (the Edit tool): b749's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b748's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b749, Component 4 (the Edit tool): b748's overrides of checks 1516 and 1659 (hook.py edited by b748's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b749 as it stands
# ### b749, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b749_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b749, Component 4 (the Edit tool): the corrigendum's events rows (1)-(5), b748's five (the template's range is a fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 6)) \
#⟪END⟫
# ### b749, Component 4 (the Edit tool): b748's override of checks 1476-1482 (one ERRATA entry at b748's (R358)(5)) removed -- (R359)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b749 as it stands
# ### b749, Component 3 (the Edit tool): G-BRANCHES-DELETED over b749's two repositories (relay, PLACE-papers) and five
# ### refs; the step-zero bank writes "KEPT as banked:" (data/b749_stepzero.txt :33), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b749, Component 4 (the Edit tool): G-RUNNER-READ's plant on b749's dispatch rows -- run 2's axiom lines carrying sorryAx (b748's
# ### plant read the lv rows' closure log, which b749 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b749, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b749, Component 6 (the Edit tool): the fold bank was b748's own route
# ### (tools/b748_fold.py); b749's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b749_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b748.py -> tools/acts/b749.py' in (rd('b749_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b749, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b749_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b749, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b749_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b749_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b749, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R359): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R359)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b749')
    return '### THE COUNTER ((R359) Component 5, the act`s events and defects together; relay data/b749_defects.txt, data/b749_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b748, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b749 (defect (d')): the order's
# ### state as b749 leaves it -- the carry from b748 said "as b748 left it ... not touched this act", where b749 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act; W-ORD-MECHANISM-ATTRIBUTION as b748 entered it (PLACE-papers 4ba38687); W-ORD-LI-ARITH and W-ORD-ZQ-FAMILY as they were entered;',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b749, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)
#⟪END⟫
# ### b749, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b748's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b749_author_answers.txt', 'b749_answer_check.txt', 'b749_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b749, Component 4's probe: v1.27.0's rdn (repair (7)) refuses a missing file, and _counter (record.tpl :2315) reads the events bank,
# ### which the close writes after the seal; read optional for the events bank alone, the defects bank still refused if missing
#⟪OVERRIDE record MARK 26666a71fb1e 1 REPAIR (reader)⟫
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
#⟪END⟫
# ### b749, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b748's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b749, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b748's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b749_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b749_registration_%s.txt' % __import__('b749_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b749, Component 4 (the Edit tool, before the face): b748's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b749, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b749's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b749, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R359)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b749 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b749_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b749: the controls' one route (N1)
#⟪END⟫
# ### b749, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b748's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b749 scorer reads; the needles set to the banks b749's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b749, (R359)(2)(iii): b748's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b749, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b749_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijk')))   # ### (a)-(k), entered before the lock, every one the seat's (data/b749_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b749_corrigendum.txt', 'data/b749_standing_v1290.txt', 'data/b749_tier3_plan.txt', 'data/b749_zenodo_call.txt',
                  'data/b749_line.txt', 'data/b749_rules.txt', 'data/b749_pathrefusal.txt',
                  'data/b749_reproduce.txt', 'data/b749_reproduce.json', 'data/b749_address_scan.txt', 'data/b749_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b749 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R359)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b749_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R359)(4): the sitting bank's rows by label -- a row opens `[A1] STATE`, `[C] STATE`, `[(7)] ...` at column 0, its fields indented two
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
        # ### (R359)(1)-(4) (b749's keys over b749's objects): the order by time and ancestry; v1.29.0's controls; the plan, [Z1] and the
        # ### call's banks; REGISTRY d1-1's dated note; the line bank; zq-b730 and the tag; v8 and v9; the address scan; the reproduction
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b748's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1290', K.STANDING_COMMIT, K.C1_STANDING), ('v1290_corr', K.C1_STANDING, K.C1_CORR),
                                 ('corr_plan', K.C1_CORR, K.C2_RELAY_ALL[0]), ('plan_z1', K.C2_RELAY_ALL[0], K.C2_RELAY_ALL[1]),
                                 ('z1_call', K.C2_RELAY_ALL[1], K.C2_RELAY_ALL[2]), ('call_c3', K.C2_RELAY_ALL[2], K.C3_RELAY[0]))),
        # ### b749 (R359)(1)-(2): the order within PLACE-papers by ancestry -- the weight and corrigendum, then REGISTRY d1-1's dated note
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('pre_c1', K.PRE_PP, K.C1_PP), ('c1_c2', K.C1_PP, K.C2_PP))),
        v1130=rd('b749_standing_v1290.txt'), v1281=None, plan=read(os.path.join(ROOT, *K.PLAN_BANK.split('/'))), print_=read(os.path.join(ROOT, *K.POSCONTROL_PLAN.split('/'))),
        controls=rd('b749_zenodo_call.txt'), notes=rd('b749_tier3_plan.txt'), rows_bank=rd('b749_line.txt'), routes=None, zanswers=rd('b749_author_answers.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        plan_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.PLAN_BANK))), print_at=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.POSCONTROL_PLAN))),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP, K.C2_PP)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP, K.C2_PP)),
        c3_blobs=dict((p_, _s(blob(ROOT, '%s:%s' % (K.C3_RELAY[0], p_)))) for p_ in ('data/b749_line.txt', 'data/b749_address_scan.txt')),
        readme=read(os.path.join(PP, 'README.md')), readme_pre=_s(blob(PP, '%s:README.md' % K.PRE_PP)),
        reg_at=_s(blob(PP, '%s:REGISTRY.md' % K.C2_PP)),
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
        drows=json.loads(rd('b749_dispatch_rows.json') or '[]'), reproduce=rd('b749_reproduce.txt'), reproducej=jl('b749_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b749_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b748 left them
        rebuild=None, rebuild_rows=json.loads(rd('b749_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               plan=_ct(ROOT, K.C2_RELAY_ALL[0]), z1=_ct(ROOT, K.C2_RELAY_ALL[1]), s2=_ct(ROOT, K.C2_RELAY), s2pp=_ct(PP, K.C2_PP),
               c3=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), s2=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY[0]),
                   s2pp=files_of(PP, K.C2_PP), c1pp_=files_of(PP, K.C1_PP), plan=files_of(ROOT, K.C2_RELAY_ALL[0]), z1=files_of(ROOT, K.C2_RELAY_ALL[1]),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b749's read-first bank's items by path, as its step zero wrote them (data/b749_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b748_closing.txt |', 'relay data/b748_events.txt |', 'relay data/b748_defects.txt |', 'relay data/b748_author_answers.txt |',
                     'relay data/b747_author_answers.txt |', 'relay data/b747_zenodo_readback.txt |', 'relay data/b747_zenodo_routes.txt |',
                     'PLACE-papers REGISTRY.md |', 'PLACE-papers README.md |', 'relay tools/standing/commit.py at v1.28.1 |', 'relay data/b748_ferry.txt |',
                     'relay data/b748_commands.txt |', 'relay data/b748_stepzero.txt |', 'relay tools/b747_zenodo.py |', 'relay data/b746_integration_draft.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R359)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'HELD DRAFT ((R359)(2))', 'LINE ((R359)(4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (142 = 142 + 0, data/b749_citation_check.txt), no miss; the
    check CLEAN; the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 142 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b749, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b748's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b749, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b748()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b749_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b748's figures, read at FINDINGS :14429 as Component 1 landed them (b748's closing head quoted)
    return landed(S, 0, ['b748 AT ITS WEIGHT', 'suite 112 of 116', 'relay 9475a886', '18 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b749's title in the ferry's Component 4 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## The Zenodo draft 23228113 at v1.2.0 discarded on the author’s word at [Z1], ',
                 'the deposit v1.1.2 and the concept read back unchanged; ',
                 'REGISTRY d1-1 noted; ',
                 'the add as a git write, the staged-set scan’s own bank and 4 repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R359)(1), (3): the generated entry for b748's five events and eighteen defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(5), the defects by the one lettering (a)-(r); every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 3, CLOSE 20 over 23, REPEAT 11); the repairs at tools/standing/ v1.29.0 by their controls
    bank; the corrigenda bank appended at row (69) and nothing before it changed; in Component 1's commits (the figures read from
    data/b749_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 18 and len(items) == j.get('items') == 23 and j.get('row') == 69 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 23 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 3 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 11 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.29.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 \
        and '  (69) ' in S['corrigenda'] and '  (70) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R359)(3) orders the rules bank data/b749_rules.txt, one row per repair, eleven rows (1)-(11); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here first committed with v1.29.0 (C1_RULES), in no other commit."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', S['rules'] or '')] == list(range(1, 12)) and 'data/b749_rules.txt' in S['files']['rules'] \
        and sorted(gs(ROOT, 'log', '--format=%H', '--', 'data/b749_rules.txt').split()) == sorted(gs(ROOT, 'rev-parse', K.C1_RULES).split()) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b749's keys, the report sections' own heads
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.29.0', 'REGISTERED -- THE PLAN AND THE CALL', 'REGISTERED -- THE DATED NOTE ON REGISTRY d1-1',
               'REGISTERED -- THE INTEGRATION LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b749: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b749, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b749_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b749, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail; REGISTRY: d1-1's dated note), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b749's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The plan, the item and the call**', '**The dated note**', '**The integration line**',
                 '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b749_corrigendum.txt', 'data/b749_standing_v1290.txt', 'data/b749_rules.txt', 'data/b749_tier3_plan.txt',
                 'data/b749_author_answers.txt', 'data/b749_zenodo_call.txt', 'data/b749_line.txt', 'data/b746_integration_draft.txt',
                 'data/b749_reproduce.txt', 'data/b749_address_scan.txt', 'data/b749_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the deposit line (REGISTRY d1-1) ; keystone A_Place_to_Stand (the monograph) ; stage CLUSTERED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()                   # ### b749: no navigator's row in the defects bank; every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R359)(1)-(2), N2 (the name the frozen run list carries): the PLACE-papers writes in their order -- the weight and corrigendum in a
    commit touching FINDINGS alone in one hunk, its first two added lines b748 at its weight ("*Appended 2026-11-09 by b749 to b748’s entry")
    and the corrigendum's heading ("## Corrigendum to b748’s record"), the corrigendum's body after them, removing none; then REGISTRY d1-1's
    dated note in a commit touching REGISTRY alone, one line added ("*Dated note, b749, 2026-11-09"), none removed, after the call's relay
    bank; the order in PLACE-papers by ancestry (the act's base, the weight and corrigendum, the note); the plans of b744 unedited at their
    step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    t_ = S['t']
    dd_ = S['disch_diff'] or {}
    adds_ = [[l for l in (dd_.get(h_) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()] for h_ in (K.C1_PP, K.C2_PP)]   # ### the added blank separator lines not counted
    rems_ = [[l for l in (dd_.get(h_) or '').split(NL) if l.startswith('-') and not l.startswith('---')] for h_ in (K.C1_PP, K.C2_PP)]
    hunks_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(adds_) == 2 and len(adds_[0]) >= 2 and len(hunks_) == 1 and adds_[0][0].startswith('+*Appended 2026-11-09 by b749 to b748’s entry') \
        and adds_[0][1].startswith('+## Corrigendum to b748’s record') and len(adds_[1]) == 1 and adds_[1][0].startswith('+*Dated note, b749, 2026-11-09') \
        and rems_ == [[], []]
    files_ = [S['reg_pp'].get(h_) for h_ in (K.C1_PP, K.C2_PP)]
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    return bool(one_) and files_ == [['FINDINGS.md'], ['REGISTRY.md']] and md_ \
        and all(t_.get(k_) for k_ in ('c1pp', 's2pp', 's2')) and t_['c1pp'] < t_['s2'] <= t_['s2pp'] \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b749_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R359)(1)-(4), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, v1.29.0, the weight and
    corrigendum (PLACE-papers, then relay), the plan, [Z1], the call's bank, REGISTRY d1-1's note (PLACE-papers), the line bank; by ancestry
    within the relay v9, v1.29.0, the corrigendum, the plan, [Z1], the call's bank, the line bank."""
    t_ = S['t']
    ks_ = ('stepzero', 'standing', 'c1pp', 'corr', 'plan', 'z1', 's2', 's2pp', 'c3')
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values())
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R359)(2)(i)-(iv), N2, N5 (the name the frozen run list carries): the plan, the item and the call -- the plan bank's foot (DIFFER 3,
    AGREE 3, the title verbatim, NO REQUEST SENT) in the plan's commit; [Z1] PASS with its time in the answers bank and its commit; the call
    bank: the re-read 5 AGREE and 0 DIFFER, the DELETE HTTP 204, the draft's id HTTP 404, the concept's record UNCHANGED YES, in that order,
    its requests GET, DELETE, GET, GET and no other method, the DELETE on 23228113; the plan's commit before [Z1]'s, [Z1]'s before the
    call bank's, the author's word before the call bank's first request; no token in either bank."""
    return _call_ok(S)


# ### the record section's INTEGRATION_LINE, the same bytes (the checks and the record are separate modules; G-COUNT-ROUTE-PRICED reads the line
# ### bank against it, and the record's entry ends with it)
_INTEG_LINE = 'INTEGRATION: cluster the deposit line (REGISTRY d1-1) ; keystone A_Place_to_Stand (the monograph) ; stage CLUSTERED'


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


def _call_ok(S):
    p_, c_, a_ = S['notes'] or '', S['controls'] or '', S['zanswers'] or ''
    t_ = S['t']
    pv_ = _vlast(p_)
    z_ = re.search(r"(?m)^\[Z1\] (PASS), the author's word at (\S+Z)", a_)
    feet_ = ['THE RE-READ: HTTP 200 ; ROWS 5: 5 AGREE, 0 DIFFER ; THE DELETE MAY RUN ON THE AUTHOR`S PASS.',
             'THE DELETE: HTTP 204 ; DONE (204 No Content).', 'THE DRAFT 23228113: HTTP 404 ; NOT FOUND, AS EXPECTED.',
             'THE CONCEPT`S RECORD: HTTP 200 ; LATEST v1.1.2, RECORD 21539167, 11 FILES ; ROWS 5: 5 AGREE, 0 DIFFER ; UNCHANGED YES.']
    ix_ = [c_.find('### ### **' + f_ + '**') for f_ in feet_]
    req_ = re.findall(r'(?m)^  (GET|DELETE|POST|PUT|PATCH) (https://zenodo\.org/\S+) : HTTP (\d+)', c_)
    head_ = re.search(r'(?m)^## THE RE-READ BEFORE THE DELETE, \(R359\)\(2\)\(iii\) \((\S+Z)\)', c_)
    tok_ = re.search(r'(?i)bearer\s+[A-Za-z0-9]{12,}|access_token=\w', p_ + c_ + a_)
    return pv_.startswith('THE PLAN: DIFFER 3 (:38, :39, :41), AGREE 3 (:36, :37, :40) ; THE TITLE VERBATIM ;') and pv_.endswith('; NO REQUEST SENT.') \
        and bool(z_) and all(i_ >= 0 for i_ in ix_) and ix_ == sorted(ix_) \
        and [l.strip() for l in c_.split(NL) if l.strip().startswith('### ### **')][-1:] == ['### ### **' + feet_[-1] + '**'] \
        and [r_[0] for r_ in req_] == ['GET', 'DELETE', 'GET', 'GET'] and req_[1][1].endswith('/deposit/depositions/23228113') and req_[1][2] == '204' \
        and 'data/b749_tier3_plan.txt' in S['files']['plan'] and 'data/b749_author_answers.txt' in S['files']['z1'] and 'data/b749_zenodo_call.txt' in S['files']['s2'] \
        and all(t_.get(k_) for k_ in ('plan', 'z1', 's2')) and t_['plan'] < t_['z1'] <= t_['s2'] \
        and bool(head_) and (_iso_epoch(z_.group(2)) or 9e18) <= (_iso_epoch(head_.group(1)) or 0) <= t_['s2'] and not tok_
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R359)(8) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b748 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b748's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
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
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.29.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1290') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b748's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R359)(2)(v), (4), N3, N5 (the name the frozen run list carries): REGISTRY d1-1's dated note -- the one PLACE-papers write touching
    REGISTRY alone, one line added and none removed, the note carrying "discarded at b749 on the author", "unchanged", "fresh draft" and
    "rubric", no sentence of it saying a thing was deposited, published or versioned; REGISTRY at HEAD its blob at that commit; README at HEAD
    its blob at the act's base. The line bank's foot COMPOSED and ALL AS READ, its line the act module's INTEGRATION_LINE, the cluster table
    read (rows above 0), the keystone's files carrying no row of the finding with their positive controls read; b746's integration draft
    carried unchanged (its md5 the worklist's); Component 3's commit carrying the line bank. The act's one Zenodo tool tools/b749_zenodo.py,
    reaching GET and DELETE alone."""
    r_ = S['rows_bank'] or ''
    v_ = _vlast(r_)
    dd_ = (S['disch_diff'] or {}).get(K.C2_PP) or ''
    nt_ = [l[1:] for l in dd_.split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    rm_ = [l for l in dd_.split(NL) if l.startswith('-') and not l.startswith('---')]
    n_ = nt_[0] if len(nt_) == 1 else ''
    say_ = [s_ for s_ in re.split(r'(?<=[.;])\s+', n_) if re.search(r'\b(?:deposited|published|versioned)\b', s_)]
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b749_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    zs_ = read(os.path.join(T, 'b749_zenodo.py')) or ''
    meth_ = sorted(set(re.findall(r"request\('([A-Z]+)'", zs_)))
    return S['reg_pp'].get(K.C2_PP) == ['REGISTRY.md'] and len(nt_) == 1 and not rm_ \
        and all(w_ in n_ for w_ in ('discarded at b749 on the author', 'unchanged', 'fresh draft', 'rubric', 'd1-1')) and not say_ \
        and (S['reg_now_pp'] or '').replace(chr(13), '') == (S['reg_at'] or '').replace(chr(13), '') \
        and bool(S['readme']) and (S['readme'] or '').replace(chr(13), '') == (S['readme_pre'] or '').replace(chr(13), '') \
        and v_.startswith('THE LINE: COMPOSED ; FROM REGISTRY d1-1 AND SPIRAL_MAP ; KEYSTONE A_Place_to_Stand ; STAGE CLUSTERED ;') and v_.endswith('; ALL AS READ.') \
        and ('      %s' % _INTEG_LINE) in r_ and re.search(r'its cluster rows ([1-9]\d*) \(the control: the table read, not empty\)', r_) is not None \
        and len(re.findall(r': 0 \(the positive control, rows naming "Place to Stand" by the same reader: [1-9]\d*\)', r_)) == 2 \
        and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and 'data/b749_line.txt' in set(S['files']['c3']) \
        and zt_ == ['b749_zenodo.py'] and meth_ == ['DELETE', 'GET']

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
    """standing clauses v9 (Component 7 of (R359): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b749_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b748's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R359-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b748's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R359) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b748's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R358)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 71bc497a',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 142 = 142 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b748-\w+) \((?:was )?[0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s C4 form: the Zenodo draft 23228113 at v1.2.0 discarded on the author`s word at [Z1], the deposit v1.1.2 and the concept read back unchanged; REGISTRY d1-1 noted; the add as a git write, the staged-set scan`s own bank and the repairs landed, counted from v1.29.0`s controls',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R359)(1), (3): the generated corrigendum for b748`s record, landed at FINDINGS :14431: its five events and eighteen defects, 23 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 3 CLOSE 20, REPEAT 11; v1.29.0`s repairs by data/b749_standing_v1290.txt; the corrigenda bank appended at row (69)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R359)(3)`s rules bank data/b749_rules.txt, eleven rows (1)-(11), committed with v1.29.0 (921ac933) alone',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b749's objects
    ('G-REGISTRATIONS-FIRST', '(R359)(1)-(2), N2: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (16654192), none removed; REGISTRY d1-1`s dated note in one commit touching REGISTRY alone (55cd38b3), one line added and none removed, after the call`s bank; the PLACE-papers order by ancestry',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'ancpp', lambda d: d.update(c1_c2=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b749_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R359)(1)-(4), N2: the act`s order by time -- step zero, v1.29.0, the weight and corrigendum, the plan, [Z1], the call`s bank, the d1-1 note, the line -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(plan_z1=False))),
    ('G-DERIVATION-GRADED', '(R359)(2)(i)-(iv), N2, N5: the plan bank`s foot (DIFFER 3, AGREE 3, the title, NO REQUEST SENT) at ec5eb768; [Z1] PASS with its time at 1858213d; the call bank at d7e52526 -- the re-read 5 AGREE 0 DIFFER, the DELETE HTTP 204 on 23228113, the draft`s id HTTP 404, the concept UNCHANGED YES, in that order, GET, DELETE, GET, GET and no other method; the plan before [Z1], [Z1] before the call; no token in a bank',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'controls', (S['controls'] or '').replace('THE DELETE: HTTP 204', 'THE DELETE: HTTP 500'))),
    ('G-OFFSET-POST-HOC', 'N5, (R359)(8): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 71bc497a, VERSION 9; v8 at HEAD its blob at 71bc497a; no v10; v9`s commit an ancestor of v1.29.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R359)(2)(v), (4), N3, N5: REGISTRY d1-1`s dated note at 55cd38b3, one line, carrying discarded, unchanged, a fresh draft and the rubric, no sentence saying a thing was deposited, published or versioned; README at its base blob; the line bank COMPOSED and ALL AS READ, its line the module`s, stage CLUSTERED, the keystone`s files read with their positive controls; b746`s integration draft at its md5; the one Zenodo tool reaching GET and DELETE alone',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'rows_bank', (S['rows_bank'] or '').replace('; ALL AS READ.**', '; NOT ALL AS READ.**'))),
    ('G-DIFFERS-ERRATA', '(R359)(1), (3): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at the act`s base, no differs or errata bank, the worklist naming no line or id; the weight line and the corrigendum in 16654192, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b749_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R359-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b748`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b748 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b748 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS, OPEN_TRAILS and REGISTRY`s d1-1 note, (R359)(1)-(2)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b748`s trail record on OPEN_TRAILS (:17990) and its root in the chain', lambda S: '### b748 — lane two, act one hundred and seventy-five, the discharges and the forms under (R358)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and REGISTRY): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b749 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b748's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b749: (R359)'s rows, written at step zero over b748's (scratch splice749.py). (1)'s line read by the ruling from the public relay at 71bc497a
    pub = _blob('D:/relay', '71bc497a', 'data/b748_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b748_closing.txt :1, the head line as the public relay carries it at 71bc497a', bool(pub) and pub[0] == at(cl, 1) and 'relay 9475a886' in pub[0] and 'PLACE-papers 7c4b8d2' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root d5c6554c036fb9e5', '4 prompts answered', 'scores 7 of 8 HELD', '18 defects'):
        add('ruling (1)', 'data/b748_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1), (3)', 'data/b748_closing.txt :5, the counter CLAIM 3, CLOSE 20, REPEAT 11 OF 23, DEFECTS 18, EVENTS 5', 'CLAIM 3, CLOSE 20, REPEAT 11 OF 23' in at(cl, 5) and 'DEFECTS 18, EVENTS 5' in at(cl, 5), at(cl, 5)[-60:], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, 71bc497a and 7c4b8d2', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('71bc497a') and gr(PP, 'rev-parse', K.PRE_PP).startswith('7c4b8d2'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    EF_ = 'D:/SIDE-explicit-formula'
    tg_ = (gr(EF_, 'rev-parse', 'v0.38') or '').strip()
    tp_ = (gr(EF_, 'rev-parse', 'v0.38^{}') or '').strip()
    add('ruling (6)', 'the tag v0.38 on SIDE-explicit-formula, tag object 21c6edaf, its peel 14ca5725, no tag beyond it', tg_.startswith('21c6edaf') and tp_.startswith('14ca5725'), '%s ; %s' % (tg_[:8], tp_[:8]), '1')
    em_ = (gr(EF_, 'rev-parse', 'main') or '').strip()
    add('ruling (6)', 'SIDE-explicit-formula main at 8fbab45, unmoved (no merge)', em_.startswith('8fbab45'), em_[:8], '1')
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (5)', 'zq-b730 past v0.38 at 1e658870, kept', zt_.startswith('1e658870'), zt_[:8], '1')
    rgl_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (2)(i), (2)(v), ferry (read first)', 'REGISTRY.md :83, row d1-1, the monograph`s deposit line: Zenodo v1.1.2 (ms v5.10.2), DOI 21539167, concept 19675355',
        at(rgl_, 83).startswith('| d1-1 | A Place to Stand (monograph)') and all(w_ in at(rgl_, 83) for w_ in ('Zenodo v1.1.2 (ms v5.10.2)', 'zenodo.21539167', 'concept 19675355')), at(rgl_, 83)[:60], '2')
    add('ruling (2)(v)', 'REGISTRY.md :983, the second d1-1 row (the version table), pointing to :83', at(rgl_, 983).startswith('| d1-1 | `REGISTRY.md:83`'), at(rgl_, 983)[:60], '2')
    for n_, r_ in ((177, '1.5c-21'), (178, '1.5c-22'), (179, '1.5c-23')):
        add('ruling (scope), (4)', 'REGISTRY.md :%d, row %s, an Epstein row' % (n_, r_), at(rgl_, n_).startswith('| %s | The Epstein instance' % r_), at(rgl_, n_)[:60], '3')
    rml_ = lines_of(os.path.join(PP, 'README.md'))
    add('ruling (2)(i), (4), ferry (read first)', 'README.md :164, the deposit note: the monograph at v5.10.2 / Zenodo v1.1.2, concept 19675355 (untouched this act, carried to b750)',
        at(rml_, 164).startswith('**Deposit note (`day1/`).**') and all(w_ in at(rml_, 164) for w_ in ('**v5.10.2**', 'Zenodo **v1.1.2**', 'zenodo.19675355')), at(rml_, 164)[:60], '2')
    sml_ = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (1), (3)(iv)', 'SPIRAL_MAP.md :264, the cluster table`s first line (the table :264-:286 the line bank read)', bool(at(sml_, 264).strip()), at(sml_, 264)[:60], '3')
    fi1_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :14301, b747 at its weight (b748`s Component 1)', at(fi1_, 14301).startswith('*Appended 2026-11-08 by b748 to b747’s entry'), at(fi1_, 14301)[:60], '1')
    add('ruling (1)', 'FINDINGS :14303, the corrigendum to b747`s record', at(fi1_, 14303).startswith('## Corrigendum to b747’s record'), at(fi1_, 14303)[:60], '1')
    add('ruling (1)', 'FINDINGS :14387, b748`s entry, §3 passed, 812 words, 46 cites, §4 482 words, 14 cites', at(fi1_, 14387).startswith('## THE_EPSTEIN_CONTROL_OBJECT §3 passed, 812 words, 46 cites, and §4 passed, 482 words, 14 cites'), at(fi1_, 14387)[:60], '1')
    ot1_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'OPEN_TRAILS :17990, b748`s trail record', at(ot1_, 17990).startswith('### b748 — lane two, act one hundred and seventy-five'), at(ot1_, 17990)[:60], '1')
    for c_, w_ in (('3b701058', ''), ('7c4b8d2', '')):
        add('ruling (1)', 'PLACE-papers %s, the commit (1) names' % c_, bool(gr(PP, 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')) and w_ in gr(PP, 'log', '-1', '--format=%s', c_), gr(PP, 'log', '-1', '--format=%s', c_)[:60], '1')
    for c_, v_ in (('bf83b65b', 'v1.28.0'), ('791341fd', 'v1.28.1')):
        add('ruling (1)', 'relay %s, tools/standing/ %s by a commit of its own' % (c_, v_), (_blob('D:/relay', c_, 'tools/standing/VERSION') or '').strip() == v_, (_blob('D:/relay', c_, 'tools/standing/VERSION') or '').strip(), '1')
    sv_ = lines_of(p('data', 'b748_standing_v1280.txt'))
    add('ruling (1)', 'data/b748_standing_v1280.txt :200, v1.28.0, CASES 36 ; AS WANTED 36', 'v1.28.0' in at(sv_, 200) and 'CASES 36 ; AS WANTED 36' in at(sv_, 200), at(sv_, 200)[:60], '1')
    sv1_ = lines_of(p('data', 'b748_standing_v1281.txt'))
    add('ruling (1)', 'data/b748_standing_v1281.txt :95, v1.28.1, CASES 19 ; AS WANTED 19', 'v1.28.1' in at(sv1_, 95) and 'CASES 19 ; AS WANTED 19' in at(sv1_, 95), at(sv1_, 95)[:60], '1')
    cr_ = lines_of(p('data', 'b748_corrigendum.txt'))
    add('ruling (1)', 'data/b748_corrigendum.txt :87, ITEMS 32, CLAIM 11, CLOSE 21, REPEAT 16; WITH THE CARRIED ITEM 33: CLAIM 11, CLOSE 22, REPEAT 16', 'ITEMS 32' in at(cr_, 87) and 'WITH THE CARRIED ITEM 33: CLAIM 11, CLOSE 22, REPEAT 16' in at(cr_, 87), at(cr_, 87)[:60], '1')
    s3_ = lines_of(p('data', 'b748_section3.txt'))
    add('ruling (1)', 'data/b748_section3.txt :197, [S3] PASSED WITH THE AUTHOR`S CLAUSE, 812 WORDS, 46 CITES, 3b701058', all(w_ in at(s3_, 197) for w_ in ('[S3] PASSED', '812 WORDS', '46 CITES', '3b701058')), at(s3_, 197)[:60], '1')
    s4_ = lines_of(p('data', 'b748_section4.txt'))
    add('ruling (1)', 'data/b748_section4.txt :104, [S4] PASSED WITH THE AUTHOR`S CLAUSE, 482 WORDS, 14 CITES', all(w_ in at(s4_, 104) for w_ in ('[S4] PASSED', '482 WORDS', '14 CITES')), at(s4_, 104)[:60], '1')
    ln_ = lines_of(p('data', 'b748_line.txt'))
    add('ruling (1), (3)(iv)', 'data/b748_line.txt :9, the INTEGRATION line, stage BANKED; :19 the cluster table SPIRAL_MAP :264-:286, 8 rows, none naming the instance',
        at(ln_, 9).lstrip().startswith('INTEGRATION: cluster the Epstein instance') and at(ln_, 9).rstrip().endswith('stage BANKED') and 'SPIRAL_MAP.md :264-:286' in at(ln_, 19) and 'cluster rows 8' in at(ln_, 19) and 'NONE' in at(ln_, 19), at(ln_, 19)[:60], '1')
    rp_ = lines_of(p('data', 'b748_reproduce.txt'))
    add('ruling (1)', 'data/b748_reproduce.txt :275, ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4', 'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4' in at(rp_, 275), at(rp_, 275)[:60], '1')
    for f_ in ('b748_checks.txt', 'b748_checks_postpush.txt'):
        ck_ = lines_of(p('data', f_))
        add('ruling (1)', 'data/%s :16, 116 run, 112 passing, the three declared failing' % f_,
            "ARMS RUN : 116. ### LIVE PASSING : 112. ### LIVE FAILING : 3 ['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH']" in at(ck_, 16), at(ck_, 16)[:60], '1')
    sc9_ = _jl('b748_scores_close.json')
    sc9_ = sc9_.get('scores') or sc9_
    held_ = sorted(k_ for k_, v_ in sc9_.items() if isinstance(v_, list) and v_[:1] == ['HELD'])
    ref_ = sorted(k_ for k_, v_ in sc9_.items() if isinstance(v_, list) and v_[:1] == ['REFUTED'])
    add('ruling (1), (3)(ix)', 'data/b748_scores_close.json, 7 of 8 HELD, N5 REFUTED, N3 HELD by the close', len(held_) == 7 and ref_ == ['N5'] and 'N3' in held_, 'HELD %d ; REFUTED %s' % (len(held_), ' '.join(ref_)), '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b748']]
    add('ruling (1)', 'data/act_roots.txt, b748`s root d5c6554c chained from b747`s 59db3794', len(ar9_) == 1 and ar9_[0][1].startswith('d5c6554c') and ar9_[0][2].startswith('59db3794'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    b3_ = rd(p('data', 'b748_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE through b748 (b748`s post-push part b3)', 'b748 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b748 AGREE' if 'b748 AGREE' in b3_ else 'ABSENT', '1')
    mv_ = rd(p('data', 'b748_mirror_verify.txt')) or ''
    add('ruling (1)', 'data/b748_mirror_verify.txt, CLEAN ON ALL THREE CLAUSES', 'CLEAN ON ALL THREE CLAUSES' in mv_, 'CLEAN' if 'CLEAN ON ALL THREE CLAUSES' in mv_ else 'ABSENT', '1')
    mi_ = lines_of(p('data', 'b748_mirror.txt'))
    add('ruling (1)', 'data/b748_mirror.txt :2 and :3, mirror-refresh-2026-11-08-b748, sha256 02a757ad, MANIFEST md5 27788e21',
        'mirror-refresh-2026-11-08-b748' in at(mi_, 2) and 'sha256 02a757ad' in at(mi_, 2) and 'md5 27788e21' in at(mi_, 3), at(mi_, 3)[:60], '1')
    aa_ = lines_of(p('data', 'b748_author_answers.txt'))
    add('ruling (1), (7), ferry (read first)', 'data/b748_author_answers.txt :45, the author`s word at the root: the synthesis sitting at b750, §5 after it, the attribution plan act after that',
        at(aa_, 45).startswith('Synthesis sitting at b750') and 'cQ(n)' in NL.join(aa_[44:48]), at(aa_, 45)[:60], '1')
    ab_ = lines_of(p('data', 'b747_author_answers.txt'))
    add('ruling (2), ferry (read first)', 'data/b747_author_answers.txt :29, the second root answer: discard in a Tier 3 act of its own, the three DIFFER rows and the title in its plan',
        at(ab_, 29).startswith('Discard (Tier 3 act)') and 'three DIFFER rows' in at(ab_, 29) and '23228113' in at(ab_, 29), at(ab_, 29)[:60], '2')
    zr_ = lines_of(p('data', 'b747_zenodo_readback.txt'))
    for n_, w_ in ((36, 'AGREES'), (37, 'AGREES'), (38, 'DIFFERS'), (39, 'DIFFERS'), (40, 'AGREES'), (41, 'DIFFERS')):
        add('ruling (2)(i), ferry (read first)', 'data/b747_zenodo_readback.txt :%d, a comparison row %s' % (n_, w_), (' %s ' % w_) in at(zr_, n_), at(zr_, n_)[:60], '2')
    add('ruling (2)(i)', 'data/b747_zenodo_readback.txt :37, state unsubmitted, submitted False', 'state unsubmitted, submitted False' in at(zr_, 37), at(zr_, 37)[-50:], '2')
    add('ruling (2)(i)', 'data/b747_zenodo_readback.txt :41, the draft`s title verbatim', 'A Place To Stand: the SIDE reduction of the Riemann Hypothesis to a single located clause' in at(zr_, 41), 'read', '2')
    add('ruling (2)(i), ferry (read first)', 'data/b747_zenodo_readback.txt :43, STATE unsubmitted, VERSION v1.2.0, 14 FILES, 6 ROWS: 3 AGREE, 3 DIFFER',
        all(w_ in at(zr_, 43) for w_ in ('THE DRAFT 23228113', 'STATE unsubmitted', 'VERSION v1.2.0', '14 FILES', 'ROWS 6: 3 AGREE, 3 DIFFER')), at(zr_, 43)[:60], '2')
    add('ferry (read first)', 'data/b747_zenodo_routes.txt present (the routes the record`s tooling reads)', os.path.exists(p('data', 'b747_zenodo_routes.txt')), 'present' if os.path.exists(p('data', 'b747_zenodo_routes.txt')) else 'ABSENT', '2')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.29.0's commit's parent once it lands, HEAD's blob before
    add('ferry', 'tools/standing/VERSION v1.28.1 entering the act', v0_ == 'v1.28.1', v0_, '1')
    for f_ in ('data/b748_relay_push-b748-closing_push_out.txt', 'tools/mirror_prevbuild.json', 'data/b748_address_scan_postlock.txt'):
        add('ruling (3)', '%s tracked and clean at step zero' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)) and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'clean', '0')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (3), ferry (read first)', 'events (1)-(5) and 18 defects (data/b748_events.txt, data/b748_defects.txt)',
        starts == list(range(1, 6)) and len(letters) == 18, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    ev = lines_of(p('data', 'b748_events.txt'))
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    for n_, k_, w_ in ((4, 1, "THE SEAT'S [CLOSE ; REPEAT b748"), (7, 2, "THE SEAT'S [CLOSE ; NEW]"), (10, 3, "THE SEAT'S [CLOSE ; REPEAT b745 (transient ls-remote)]"),
                       (11, 4, "THE SEAT'S [CLOSE ; REPEAT b745 (transient ls-remote)]"), (14, 5, "THE SEAT'S [CLAIM ; NEW]")):
        add('ruling (3), ferry (read first)', 'data/b748_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    add('ruling (3)(i)', 'data/b748_events.txt :7, (2) the relay add of the root banks and the root commit sent in one message', 'in one messag' in at(ev, 7), at(ev, 7)[:60], '1')
    add('ruling (3)(ix)', 'data/b748_events.txt :14, (5) N3, S1 and S2 PENDING in the scores written before the root', 'PENDING' in at(ev, 14), at(ev, 14)[:60], '1')
    df_ = lines_of(p('data', 'b748_defects.txt'))
    TAGS_ = (('a', 'CLOSE ; REPEAT b747 (c)'), ('b', 'CLOSE ; NEW'), ('c', 'CLAIM ; REPEAT b747 (d)'), ('d', 'CLOSE ; NEW'), ('e', 'CLOSE ; REPEAT b748 (a)'),
             ('f', 'CLOSE ; REPEAT b748 (e)'), ('g', 'CLOSE ; NEW'), ('h', 'CLOSE ; REPEAT b747 (k)'), ('i', 'CLAIM ; NEW'), ('j', 'CLOSE ; NEW'), ('k', 'CLOSE ; NEW'),
             ('l', 'CLOSE ; REPEAT b748 (g)'), ('m', 'CLOSE ; REPEAT b748 (e)'), ('n', 'CLOSE ; NEW'), ('o', 'CLOSE ; NEW'), ('p', 'CLOSE ; REPEAT b748 (m)'),
             ('q', 'CLOSE ; NEW'), ('r', 'CLOSE ; NEW'))
    for n_, (l_, t_) in zip(range(7, 25), TAGS_):
        nav_ = l_ == 'i'
        add('ruling (3), ferry (read first)', 'data/b748_defects.txt :%d, (%s) %s [%s]' % (n_, l_, "THE NAVIGATOR'S" if nav_ else "THE SEAT'S", t_),
            at(df_, n_).startswith("    (%s) THE %s [%s]" % (l_, "NAVIGATOR'S" if nav_ else "SEAT'S", t_)), at(df_, n_)[:60], '1')
    for c_ in ('be4a5a0d', 'cdb0d404', '0b8ad609', '5fa49fbc', 'bace7cfd', '9475a886', '9e3970df', '71bc497a'):
        add('ruling (3)', 'relay %s, a commit the events, the defects and the closing name' % c_, bool(gr('D:/relay', 'rev-parse', '--verify', '--quiet', c_ + '^{commit}')), gr('D:/relay', 'log', '-1', '--format=%s', c_)[:60], '1')
    hr_ = lines_of(p('data', 'b748_hook_refusals.txt'))
    add('ruling (3)(x)', 'data/b748_hook_refusals.txt, 11 refusals (:1-:11)', len([l_ for l_ in hr_ if l_.strip()]) >= 11, '%d lines' % len([l_ for l_ in hr_ if l_.strip()]), '1')
    TN_ = 'C:/Users/echo chamber/.claude/projects/D--/memory/feedback_b748_traps.md'
    add('ferry (read first)', 'the seat`s trap note on the staged-set scan, %s :11 (outside the tree, printed by path)' % TN_, at(lines_of(TN_), 11).startswith('- **The staged-set scan (commit.py v1.28.0) rewrites'), at(lines_of(TN_), 11)[:60], '1')
    cm_ = lines_of(p('tools', 'standing', 'commit.py'))
    for n_, w_ in ((26, '(iv) EVERY GIT WRITE THROUGH THE ONE-CALL TOOL'), (29, '(ii) THE SCAN OVER THE STAGED SET BEFORE EVERY COMMIT'), (38, 'v1.28.1, (R358)(3)(iv), b748 defect (k)'),
                   (277, 'def run_scan(act):'), (443, 'def write_route(key, verb, args, act=None):'), (495, '(scanner or run_scan)(act)')):
        add('ferry (read first)', 'tools/standing/commit.py :%d at v1.28.1, %s' % (n_, w_[:50]), w_ in at(cm_, n_), at(cm_, n_)[:60], '1')
    ig_ = lines_of(p('data', 'b746_integration_draft.txt'))
    add('ruling (4)', 'data/b746_integration_draft.txt :16-:26, the stages drafted as canon text, carried unchanged to b750', at(ig_, 16).startswith('## (B) THE STAGES') and at(ig_, 18).lstrip().startswith('BANKED'), at(ig_, 16)[:40], '3')
    add('ruling (4)', 'data/b746_integration_draft.txt :11, the line`s form', at(ig_, 11).lstrip().startswith('INTEGRATION: cluster <name>'), at(ig_, 11)[:40], '3')
    add('ruling (4)', 'data/b746_integration_draft.txt md5 %s, unchanged' % K.INTEGRATION_DRAFT_MD5[:12], __import__('hashlib').md5(open(p('data', 'b746_integration_draft.txt'), 'rb').read()).hexdigest() == K.INTEGRATION_DRAFT_MD5, 'md5', '3')
    add('ruling (1)', 'FINDINGS :%d, b748`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## '), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b747`s weight line and corrigendum (b748`s), the form b749`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), bool(at(fi, K.B711_WEIGHT)) and bool(at(fi, K.B711_CORRIGENDUM)), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b748`s trail record, its hand section' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b748 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (1)', 'OPEN_TRAILS :%d, b748`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('ruling (scope)', 'the census THE_KEYSTONE_CENSUS_v0_8_3.md at 36 kernels', '36' in NL.join(lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))[:40]), 'read', '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.28.1 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.28.1',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R359)(1): b748's export, the mirror's last
    add('ruling (1)', '%s, b748`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R359)(3), (6): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), (6)', 'the push-b748-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R359)(3), (6): act_current alone, then b748's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b748_relay_push-b748-closing_push_out.txt'])):   # ### b749: no terminal table carried (b748 left none)
        if c_ is K.STEPZERO:   # ### tools/mirror_prevbuild.json: a CRLF-only difference from HEAD's blob a94aa543, restored by checkout, nothing to commit
            add('ruling (3)', 'tools/mirror_prevbuild.json at HEAD`s blob a94aa543 (a CRLF-only difference restored at step zero, no commit)',
                gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json').startswith(gr('D:/relay', 'rev-parse', 'HEAD:tools/mirror_prevbuild.json')[:12]), 'blob %s' % gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json')[:8], '0')
        if not c_:
            add('ruling (3), (6)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3), (6)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3), (6)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (3), (6)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3), (6)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b749_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b749_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b749 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b748_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.29.0's controls and the rules, the plan's and the call's banks, the line bank, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R359)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R359)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R359)(8): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b749 ((R359)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R358)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b749 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SEVENTY-SIX, THE HELD DRAFT: b748 AT ITS WEIGHT AND ITS CORRIGENDUM; '
              'v1.29.0; THE ZENODO DRAFT 23228113 AT v1.2.0 DISCARDED ON THE AUTHOR`S WORD AT [Z1] AND THE RECORD READ BACK; REGISTRY d1-1 NOTED; THE INTEGRATION LINE, UNDER (R359).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b748's sections over b748's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.29.0: one call of the tool per message, the per-commit scan`s own bank, no commit without the scan, the record`s readers refusing a missing path, the carry row by row and the kept row by the tool, a prior act`s log by its step rows, each case failing before its repair and passing after', 'b749_standing_v1290.txt'),
                ('the eleven rules of (R359)(3)', 'b749_rules.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE HELD DRAFT ((R359)(2))', [
                ('the plan, banked and committed before any call: the three DIFFER rows, the three AGREE rows and the title verbatim', 'b749_tier3_plan.txt'),
                ('the re-read compared row by row, the one DELETE, the draft`s id and the concept`s record read back', 'b749_zenodo_call.txt'),
                ('the probe-path refusal printed before the lock gate', 'b749_pathrefusal.txt')]),
            ('THE LINE ((R359)(4))', [
                ('the INTEGRATION line from REGISTRY d1-1 and SPIRAL_MAP, stage CLUSTERED, the carried items named to b750', 'b749_line.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b749_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b748`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b749_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R358)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R359)(8)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b748 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b748-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the plan banked and committed before any API call, [Z1]`s answer banked before the delete, the re-read printed and compared before it and the read-backs after it, the tools` controls before their figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: REGISTRY d1-1`s dated note read for discarded, unchanged and a fresh draft and for any further sentence ; no sentence saying a thing was deposited, published or versioned ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b749_address_scan.txt, data/b749_address_scan_postlock.txt, data/b749_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no field of a published record touched ; the API calls three GETs and the one DELETE of the unpublished deposition 23228113 on the author`s word at [Z1], the token in the request header alone ; publish never called, the draft at v1.2.0 deleted unpublished ; no GitHub description written ; no door edited ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS (the trail), REGISTRY.md (one dated note to row d1-1) ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b749`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.29.0 by (R359)(3) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b748 unedited, act_current`s shared_edits empty ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R359)(4) AND (8)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the README :164 item, the 1.5c-21 dated note and the canon text of the stages carried to the synthesis sitting at b750 (relay data/b749_line.txt (C), data/b746_integration_draft.txt) ;',
    '        the root`s question, whether the sign of cQ(n) over n <= 3000 is computed at b750`s sitting as a banked instrument row or waits for the plan act, its answer in relay data/b749_author_answers.txt ; the d1-1 note`s further words for the author`s keep or strike (defect (j)) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b749_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b748 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b749: the standing repairs are v1.29.0's ((R359)(3), relay data/b749_standing_v1290.txt, read in the corrigendum section); the
    # ### carry's diffs here (b749 carried at step zero before the fold; its tools since are the templates and tools/acts/b749.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b748 left them; port-b707 at b712`s tip %s)' % (
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
    b749's form over b749's objects: the corrigendum's foot and v1.29.0's controls; the plan's foot, [Z1]'s word and the call bank's four
    feet; the line bank's foot; the rules bank's rows; the citation check; the reproduction run; the address scan; each by its own lines
    through _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1290.txt' % ACT, r'\*\*v1\.29\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.29.0`s controls')
    pl_ = _bfig('%s_tier3_plan.txt' % ACT, r'\*\*THE PLAN: DIFFER (\d+) \(([^)]*)\), AGREE (\d+) \(([^)]*)\) ; THE TITLE VERBATIM ;.*; (NO REQUEST SENT)\.\*\*', 'the plan`s foot')
    rr_ = _bfig('%s_zenodo_call.txt' % ACT, r'\*\*THE RE-READ: HTTP (\d+) ; ROWS (\d+): (\d+) AGREE, (\d+) DIFFER ;', 'the re-read`s foot')
    dl_ = _bfig('%s_zenodo_call.txt' % ACT, r'\*\*THE DELETE: HTTP (\d+) ; ([^*]+?)\.\*\*', 'the delete`s foot')
    dr_ = _bfig('%s_zenodo_call.txt' % ACT, r'\*\*THE DRAFT (\d+): HTTP (\d+) ; ([^*]+?)\.\*\*', 'the draft`s read-back')
    cp_ = _bfig('%s_zenodo_call.txt' % ACT, r'\*\*THE CONCEPT`S RECORD: HTTP (\d+) ; LATEST (v[\d.]+), RECORD (\d+), (\d+) FILES ; ROWS (\d+): (\d+) AGREE, (\d+) DIFFER ; UNCHANGED (YES|NO)\.\*\*', 'the concept`s read-back')
    z1_ = _bfig('%s_author_answers.txt' % ACT, r"(?m)^\[Z1\] (PASS|STRIKE), the author's word at (\S+Z)", 'the author`s word at [Z1]')
    ln_ = _bfig('%s_line.txt' % ACT, r'\*\*THE LINE: (COMPOSED) ; FROM REGISTRY d1-1 AND SPIRAL_MAP ; KEYSTONE (\S+) ; STAGE (\w+) ; THE CANON TEXT CARRIED, md5 ([0-9a-f]{12}) (EQUAL) ; THE README ITEM CARRIED ; THE 1\.5c-21 NOTE CARRIED ; (ALL AS READ)\.\*\*', 'the line bank`s foot')
    reps_ = [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', rdn('%s_rules.txt' % ACT))]   # ### the rules bank's rows
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b749: no order entered this act ((R359) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], rules_rows=reps_,
                repairs=len([c_ for c_ in v5[0].split(', ') if c_.strip('()') not in ('calls', 'scanbank', 'version')]),   # ### the repairs beside the two the title names, the version not a repair
                pl_differ=int(pl_[0]), pl_agree=int(pl_[2]),
                rr_status=rr_[0], rr_rows=int(rr_[1]), rr_agree=int(rr_[2]), rr_differ=int(rr_[3]),
                dl_status=dl_[0], dr_status=dr_[1], cp_status=cp_[0], cp_version=cp_[1], cp_record=cp_[2], cp_files=int(cp_[3]),
                cp_rows=int(cp_[4]), cp_agree=int(cp_[5]), cp_differ=int(cp_[6]), cp_unchanged=(cp_[7] == 'YES'),
                z1_state=z1_[0], z1_at=z1_[1],
                ln_keystone=ln_[1], ln_stage=ln_[2], ln_md5=ln_[3], ln_ok=(ln_[5] == 'ALL AS READ'),
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R359)(3): the kernel rows of one kind as banked (data/b749_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R359): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b749_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b749_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b749's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b749_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b749_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b749_standing_v1290.txt', '## THE CONTROLS', '### ### **v1.29.0: CONTROLS '))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, the call: in the call bank the re-read printed and compared before the delete, the read-backs after it; (bank, the re-read's head,
# ### the delete's foot, the read-back's words after it)
N2_SECTIONS = (('data/b749_zenodo_call.txt', '## THE RE-READ BEFORE THE DELETE', '### ### **THE DELETE: HTTP', 'THE CONCEPT`S RECORD'),)


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R359): the plan bank committed before any API call; [Z1]'s answer banked before the delete; in the call bank the re-read printed
    and compared before the delete and the read-backs after it; each tool's controls before its figures; the weight and corrigendum
    (FINDINGS alone) and the d1-1 note (REGISTRY alone); the (W) regeneration, the pre-lock comparison and the probe-path refusal before the
    lock gate. Step zero, v1.29.0, the weight and corrigendum, the corrigendum banks, the plan, [Z1], the call's bank, the d1-1 note and the
    line bank in that order by time; v1.29.0 an ancestor of the call's bank, and the call's bank of HEAD."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_RELAY_ALL[0]), (ROOT, K.C2_RELAY_ALL[1]),
              (ROOT, K.C2_RELAY_ALL[2]), (PP, K.C2_PP), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.C2_RELAY], capture_output=True).returncode == 0 \
        and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C2_RELAY, 'HEAD'], capture_output=True).returncode == 0
    dfiles_ = [sorted(x for x in g(PP, 'show', '--name-only', '--format=', h_).split() if x.strip()) for h_ in (K.C1_PP, K.C2_PP)]
    disch_ = dfiles_ == [['FINDINGS.md'], ['REGISTRY.md']]
    sect_ = True
    for b_, *w_ in N2_SECTIONS:
        sb_ = rd(os.path.join(ROOT, *b_.split('/'))) or ''   # ### the path is relay-relative ('data/...'), joined to the relay root
        ix_ = [sb_.find(x_) for x_ in w_[:2]]
        sect_ = sect_ and all(i_ >= 0 for i_ in ix_) and ix_ == sorted(ix_) and w_[2] in sb_[ix_[1]:]
    za_ = re.search(r"(?m)^\[Z1\] PASS, the author's word at (\S+Z)", rdn('%s_author_answers.txt' % ACT))
    zh_ = re.search(r'(?m)^## THE RE-READ BEFORE THE DELETE, \(R359\)\(2\)\(iii\) \((\S+Z)\)', rdn('%s_zenodo_call.txt' % ACT))
    zord_ = bool(za_ and zh_) and za_.group(1)[:19] <= zh_.group(1)[:19]   # ### the author's word before the call's first request
    route_ = disch_ and sect_ and zord_
    same_ = True
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the weight and corrigendum (PLACE-papers %s) FINDINGS alone and the d1-1 note (PLACE-papers %s) REGISTRY alone: %s; in the call bank (relay %s) the re-read before the delete and the read-backs after it: %s; the author`s word at [Z1] before the call`s first request: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.29.0, the weight and corrigendum, the corrigendum banks, the plan, [Z1], the call`s bank, the d1-1 note and the line bank in that order by time: %s (%s), v1.29.0 an ancestor of the call`s bank and that of HEAD: %s; the tools` controls before their figures: %s' % (
            K.C1_PP[:8], K.C2_PP[:8], disch_, ', '.join(b_ for b_, *_w in N2_SECTIONS), sect_, zord_, regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b749's objects; b748's in git at b748's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b749_standing_v1290.txt', ('ALL AS WANTED',)), ('b749_tier3_plan.txt', ('THE PLAN: DIFFER 3', 'NO REQUEST SENT')),
             ('b749_zenodo_call.txt', ('THE CONCEPT`S RECORD', 'UNCHANGED YES')),
             ('b749_line.txt', ('THE LINE: COMPOSED', 'ALL AS READ')),
             ('b749_corrigendum.txt', ('ITEMS',)), ('b749_citation_check.txt', ('THE CHECK CLEAN',)), ('b749_reproduce.txt', ('REPRODUCES',)), ('b749_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### the entry's last line, the INTEGRATION line, in b746's draft's form (relay data/b746_integration_draft.txt :11), read from REGISTRY and
# ### SPIRAL_MAP at PLACE-papers HEAD through relaypath (relay data/b749_line.txt): the deposit line, its keystone the monograph, CLUSTERED by
# ### the d1-1 dated note, no file of the keystone carrying the finding
INTEGRATION_LINE = 'INTEGRATION: cluster the deposit line (REGISTRY d1-1) ; keystone A_Place_to_Stand (the monograph) ; stage CLUSTERED'
FIXED_SENTENCES = ()   # ### b749: no fixed sentence ordered by (R359)


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
    """N3 (R359): no sentence says anything was deposited, published or versioned; the dated note on d1-1 says discarded, unchanged and a
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
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b749: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    nt_ = [l for l in (rd(os.path.join(PP, 'REGISTRY.md')) or '').replace(chr(13), '').split(NL) if l.startswith('*Dated note, b749,')]
    n_ = nt_[0] if len(nt_) == 1 else ''
    nsents_ = [x for x in re.split(r'(?<=[.;])\s+', n_.strip('*')) if x.strip()]
    three_ = ('discarded', 'unchanged', 'fresh draft')
    said_ = bool(n_) and all(w_ in n_ for w_ in three_) and 'rubric' in n_
    more_ = [x for x in nsents_ if not any(w_ in x for w_ in three_)]   # ### N3: "says discarded, unchanged and a fresh draft on the rubric's word, and no more"
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    dep_ = [x for x in nsents_ + sents if re.search(r'\b(?:deposited|published|versioned)\b', x) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents if re.search(r'\b(?:RH|GRH|h2|ζ)\b.*\b(?:holds|fails|proved|refuted|moved)\b', x) and not re.search(neg_, x)]
    lines_ = [l for l in text.split(NL) if l.strip()]
    rg_ = (rd(os.path.join(PP, 'REGISTRY.md')) or '').replace(chr(13), '').split(NL)
    sm_ = rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''
    integ_ = bool(lines_) and lines_[-1].strip() == INTEGRATION_LINE \
        and any(l.startswith('| d1-1 | A Place to Stand (monograph)') for l in rg_) and 'A_Place_to_Stand.md' in sm_
    fixed_ = []
    nouns_ = [w_ for w_ in ('23228113', 'v1.2.0', 'v1.1.2', '21539167', '19675355', '[Z1]', 'data/%s_tier3_plan.txt' % ACT, 'data/%s_zenodo_call.txt' % ACT,
                            'data/%s_line.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and said_ and not more_ and not dep_ and not first_ and not loc_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; REGISTRY d1-1`s dated note (PLACE-papers %s) saying discarded, unchanged and a fresh draft on the rubric`s word: %s, its sentences beyond those: %s; a sentence of the note or the entry saying a thing was deposited, published or versioned outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY d1-1 and SPIRAL_MAP`s keystone row read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), K.C2_PP[:8], said_, more_ or 'NONE', dep_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R359) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R359)(5))
# ### (R359)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R359)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
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
    # ### (R359) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b748's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b749, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b748's face
# ### read them; (R359)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
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
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R359)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R359)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b748 left them; the address scan's count from its bank (relay data/b749_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R359)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R359)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R359)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    ghe_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+release\b|/actions/newversion|/actions/publish|zenodo\.org/api|\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    # ### (R359)(2)(iii), N5: the one DELETE of 23228113 through tools/b749_zenodo.py, sent once and not --dry
    zdel_ = [r_['n'] for r_ in cmr_ if re.search(r'b749_zenodo\.py"?\s+delete\b', r_.get('cmd') or '') and '--dry' not in (r_.get('cmd') or '')]
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and len(zdel_) == 1
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b749_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the capture: %s; the DELETE of 23228113 by tools/b749_zenodo.py in the capture, not --dry (once): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b749 — lane two, act one hundred and seventy-six, the held draft under (R359): b748 at its weight and its corrigendum; '
            'v1.29.0; the Zenodo draft 23228113 at v1.2.0 %s; REGISTRY d1-1 noted; the integration line' % (
                'discarded on the author’s word at [Z1]' if _figs()['z1_state'] == 'PASS' else 'held, [Z1] struck'))
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects in the ferry's C4 form ("the Zenodo draft 23228113 at v1.2.0 <discarded on the author's word at
    [Z1] | held, [Z1] struck>, the deposit v1.1.2 and the concept read back <unchanged | DIFFERS printed>; REGISTRY d1-1 noted; the add as a
    git write, the staged-set scan's own bank and <r> repairs landed"); every figure from the banks ([Z1]'s word, the delete's and the
    read-backs' statuses, the concept's rows; v1.29.0's controls less (calls), (scanbank) and (version))."""
#⟪END⟫
#⟪SECTION record 31⟫
    ctl_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if 'calls' not in ctl_ or 'scanbank' not in ctl_:
        sys.exit('### v1.29.0`S CONTROLS DO NOT NAME (calls) AND (scanbank) -- NOTHING COMPOSED')
    if f['rules_rows'] != list(range(1, len(f['rules_rows']) + 1)) or len(f['rules_rows']) < 3:
        sys.exit('### THE RULES BANK`S ROWS ARE NOT (1)-(n) IN ORDER -- NOTHING COMPOSED')
    disc_ = f['z1_state'] == 'PASS' and f['dl_status'] == '204' and f['dr_status'] == '404'
    if f['z1_state'] == 'PASS' and not disc_:
        sys.exit('### [Z1] PASSED AND THE DELETE OR ITS READ-BACK NOT AS EXPECTED -- NOTHING COMPOSED')
    return ('## The Zenodo draft 23228113 at v1.2.0 %s, the deposit %s and the concept read back %s; REGISTRY d1-1 noted; '
            'the add as a git write, the staged-set scan’s own bank and %d repairs landed' % (
                'discarded on the author’s word at [Z1]' if disc_ else 'held, [Z1] struck', f['cp_version'],
                'unchanged' if f['cp_unchanged'] else 'DIFFERS printed', f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) REGISTRY d1-1`s dated note (PLACE-papers 55cd38b3) says discarded, unchanged and a fresh draft at the rubric`s stage, and says more: the call`s read-back, the README note untouched, no cell edited and "Nothing deposits", where N3 reads "and no more" (defect (j)); the further words for the author to keep or strike, no second ledger write made; (2) the eleven rules of relay data/b749_rules.txt, the seat`s reading of (R359)(3), each for the author`s strike; (3) the README :164 item, the 1.5c-21 dated note and the stages` canon text carried to b750 (relay data/b749_line.txt (C)); '
            +
            '(4) %s and the seat’s %s defect%s as lettered' % (
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b749: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R359)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b749's objects; b748's composer in git at
    b748's record tool). Its last line the INTEGRATION line ((R359)(4))."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R358)(2)(v)
    rg_ = (rd(os.path.join(PP, 'REGISTRY.md')) or '').replace(chr(13), '').split(NL)
    dn_ = [i_ + 1 for i_, l_ in enumerate(rg_) if l_.startswith('*Dated note, b749,')]
    d1_ = [i_ + 1 for i_, l_ in enumerate(rg_) if l_.startswith('| d1-1 |')]
    if len(dn_) != 1 or len(d1_) != 2:
        sys.exit('### THE LINES THE ENTRY CITES DO NOT READ AS EXPECTED (the dated note %s, the d1-1 rows %s) -- NOTHING COMPOSED' % (dn_, d1_))
    e = ['', _title(), '',
         'The held Zenodo draft 23228113 at v1.2.0 is discarded on the author’s word at [Z1] (%s): one GET re-read it and agreed with b747’s read-back, %d rows AGREE and %d DIFFER; one DELETE answered HTTP %s; the draft’s id now answers HTTP %s. The public record reads back at %s, record %s, %d files, %d of %d rows agreeing with REGISTRY d1-1 and README :164: %s. REGISTRY row d1-1 (:%d, :%d) carries the act’s dated note at :%d.' % (
             f['z1_at'], f['rr_agree'], f['rr_differ'], f['dl_status'], f['dr_status'], f['cp_version'], f['cp_record'], f['cp_files'], f['cp_agree'], f['cp_rows'],
             'unchanged' if f['cp_unchanged'] else 'DIFFERS printed', d1_[0], d1_[1], dn_[0]), '',
         '*Filed at b749 on the author’s ruling `(R359)`; %d question%s put before the root. Banks: relay '
         '`data/b749_corrigendum.txt`, `data/b749_standing_v1290.txt`, `data/b749_rules.txt`, `data/b749_tier3_plan.txt`, `data/b749_author_answers.txt`, `data/b749_zenodo_call.txt`, `data/b749_line.txt`, `data/b749_prelock.txt`, `data/b749_pathrefusal.txt`, '
         '`data/b749_reproduce.txt`, `data/b749_address_scan.txt`, `data/b749_touch.txt`, `data/b749_standing_figures.txt`, `data/b749_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R359)(1), (3); %s, %s, %s): b748 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b748’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b749_corrigendum.txt); tools/standing/ at %s by a commit of its own, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b749_standing_v1290.txt): the bare add a git write and one call of the tool per message, the per-commit scan’s own bank, no commit without the scan, the record’s readers refusing a missing path, the carry row by row and the kept row by the tool, a prior act’s log by its step rows; the rules, %d rows, in relay data/b749_rules.txt.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], len(f['rules_rows'])), '',
         '**The plan, the item and the call** ((R359)(2)(i)-(iv), N2, N5): the plan banked and committed at relay %s before any call, the %d DIFFER rows and %d AGREE rows of b747’s read-back and the draft’s title printed verbatim (relay data/b749_tier3_plan.txt); [Z1] put in b736’s form, the author’s word %s at %s, banked at relay %s (relay data/b749_author_answers.txt); the re-read HTTP %s, %d AGREE and %d DIFFER; the DELETE HTTP %s; the draft’s id HTTP %s; the concept’s record HTTP %s, %s (relay data/b749_zenodo_call.txt, relay %s). The token from the environment, in the request header alone, in no command line, bank or capture.' % (
             K.C2_RELAY_ALL[0][:8], f['pl_differ'], f['pl_agree'], f['z1_state'], f['z1_at'], K.C2_RELAY_ALL[1][:8], f['rr_status'], f['rr_agree'], f['rr_differ'],
             f['dl_status'], f['dr_status'], f['cp_status'], 'UNCHANGED' if f['cp_unchanged'] else 'DIFFERS', K.C2_RELAY_ALL[2][:8]), '',
         '**The dated note** ((R359)(2)(v), N3): REGISTRY :%d, to row d1-1, one PLACE-papers write (%s): the held draft at v1.2.0 discarded on the author’s word, the deposit at v1.1.2 and the concept unchanged, a fresh draft to be opened when the 1.5C paper reaches the rubric’s stage; the note also names the call’s read-back, the README note untouched and no cell edited (defect (j)). README :164 untouched.' % (
             dn_[0], K.C2_PP[:8]), '',
         '**The integration line** ((R359)(4)): this entry’s line read from REGISTRY d1-1 and SPIRAL_MAP through the record’s readers: the cluster the deposit line, the keystone %s (SPIRAL_MAP :268, the cluster table’s Methodology row), stage %s by the dated note, no file of the keystone carrying the finding (relay data/b749_line.txt); the stages’ canon text at relay data/b746_integration_draft.txt carried unchanged to b750 (md5 %s), with the README :164 item and the 1.5c-21 dated note.' % (
             f['ln_keystone'], f['ln_stage'], f['ln_md5']), '',
         '**The order of the act** (N2): %s at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the plan at relay %s, [Z1] at %s, the call’s bank at %s; the dated note at PLACE-papers %s; the line bank at relay %s; the per-commit scan to its own bank at every commit; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b749_prelock.txt, data/b749_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             f['ver'], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_RELAY_ALL[0][:8], K.C2_RELAY_ALL[1][:8], K.C2_RELAY_ALL[2][:8], K.C2_PP[:8], K.C3_RELAY[0][:8]), '',
         '**What this act is not**: nothing deposits; no new version; no draft published; no field of a published record touched; the API calls three GETs and the one DELETE of the unpublished deposition 23228113; no kernel’s main touched, no branch merged, no tag beyond v0.38, no Lean file written, no door edited.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b749_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b749_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b749_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b749 -- %s, %s, %s, %s -- against b748’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b749_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the plan and the call read one way: the plan printed what the draft was and what the one call would do before any request, and the call’s bank prints what the record is after it -- the draft’s id not found, the deposit and the concept as REGISTRY d1-1 names them.', '',
         '**Carried to:** %s, the synthesis sitting, per (R359)(7): the README :164 item, the 1.5c-21 dated note and the stages’ canon text; the root’s question on the sign of cQ(n) over n ≤ 3000, put once and answered in relay data/b749_author_answers.txt; the dated note’s further words for the author’s keep or strike; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b748():
    """b748's form over b748's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b749's objects; b748's composer in git at b748's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the plan, the item and the call; the d1-1 note; the line."""
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
             '**(R359) ratified.** Its components as the ferry orders them (relay data/b749_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b748’s weight), :%s (the corrigendum), :%s (the entry); REGISTRY.md, one dated note to row d1-1 (PLACE-papers %s); no order entered; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.C2_PP[:8]), '',
             '**The held draft:** the plan at relay %s before any call; [Z1] %s at %s; the re-read %d AGREE, %d DIFFER; the DELETE of 23228113 HTTP %s; the draft’s id HTTP %s; the concept’s record %s, record %s, %s (relay data/b749_tier3_plan.txt, data/b749_author_answers.txt, data/b749_zenodo_call.txt).' % (
                 K.C2_RELAY_ALL[0][:8], f['z1_state'], f['z1_at'], f['rr_agree'], f['rr_differ'], f['dl_status'], f['dr_status'], f['cp_version'], f['cp_record'],
                 'unchanged' if f['cp_unchanged'] else 'DIFFERS printed'), '',
             '**The integration line:** b749’s at the foot of its entry, cluster the deposit line, keystone %s, stage %s (relay data/b749_line.txt); the stages’ canon text at relay data/b746_integration_draft.txt, carried unchanged to the synthesis sitting at b750.' % (
                 f['ln_keystone'], f['ln_stage']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b749_standing_v1290.txt); the d1-1 note`s further words (defect (j)).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b749_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b749_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b749_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b749 `%s` (previous `%s`, b748’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b749_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b749_standing_v1290.txt); the standing '
             'report tool (relay data/b749_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b748 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b749_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b748’s %s, %s, %s, %s (relay data/b749_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b749_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b748():
    """b748's trail record over b748's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b748 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b748`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none; no kernel`s main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b748-closing, push-b748-preroot, push-b748-record; PLACE-papers push-b748-preroot, push-b748-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b749_stepzero.txt :29-:32).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: one dated note appended at the foot to row d1-1 (PLACE-papers 55cd38b3), no row added.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R359)(3): FINDINGS :14431.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R359)(3): row (69).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none: (R359) orders none.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R359) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b749_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.29.0`s controls, the plan, the call and its read-backs, the line, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none this act: no registered object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R359)(8)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R359)(3): tools/standing/ to v1.29.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b749_address_scan.txt (the address never printed).'),
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
    # ### b749: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b749_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b749_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1290', 'tier3_plan', 'zenodo_call', 'line', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b749_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b749_registration_%s.txt -- b749, THE HELD DRAFT: b748 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.29.0; "
                             "THE ZENODO DRAFT 23228113 AT v1.2.0 DISCARDED ON THE AUTHOR`S WORD AT [Z1] AND THE RECORD READ BACK; REGISTRY d1-1 NOTED; THE INTEGRATION LINE; NO DEPOSIT, NO LEAN, UNDER (R359)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b748's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b749: b748's lines read banks this
act does not write, and are not carried; the lines are b749's: tools/standing/ v1.29.0 by its controls (CERTIFIED), the plan and the call,
REGISTRY d1-1's dated note and the INTEGRATION line by their banks (REGISTERED), and the draft (HELD); no line stands on KERNEL (no Lean
this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b749's lines, each from the record tool's figures over b749's banks
    # ------------------------------------------------------------------ REGISTERED: (R359)(2)(i)-(iv), the plan and the call, read from their banks
    sz = seat('%s_zenodo_call.txt' % ACT, '**THE CONCEPT`S RECORD:')
    sk = sz   # ### (R358)(2)(ii): the name the template appends
    keys['PLAN'] = ('REGISTERED -- THE PLAN AND THE CALL: the plan banked before any call (DIFFER %d, AGREE %d, the title verbatim); [Z1] %s at %s; the re-read %d AGREE, %d DIFFER; the DELETE of 23228113 HTTP %s; the draft`s id HTTP %s; the concept`s record %s, record %s, %d files, %s. SOURCE %s.' % (
        f['pl_differ'], f['pl_agree'], f['z1_state'], f['z1_at'], f['rr_agree'], f['rr_differ'], f['dl_status'], f['dr_status'], f['cp_version'], f['cp_record'],
        f['cp_files'], 'UNCHANGED' if f['cp_unchanged'] else 'DIFFERS', sz['text']))
    snz = seat('%s_line.txt' % ACT, 'REGISTRY.md, the act`s dated note')
    keys['NOTE'] = ('REGISTERED -- THE DATED NOTE ON REGISTRY d1-1 at PLACE-papers %s: the held draft discarded on the author`s word, the deposit and the concept unchanged, a fresh draft at the rubric`s stage; README :164 untouched. SOURCE %s.' % (
        K.C2_PP[:8], snz['text']))
    seats.append(snz)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.29.0 ((R359)(3)), by its controls
    sw = seat('%s_standing_v1290.txt' % ACT, '**v1.29.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1290'] = ('CERTIFIED -- tools/standing/ v1.29.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the INTEGRATION line ((R359)(4))
    so = seat('%s_line.txt' % ACT, '**THE LINE: ')
    keys['LINE'] = ('REGISTERED -- THE INTEGRATION LINE from REGISTRY d1-1 and SPIRAL_MAP: cluster the deposit line, keystone %s, stage %s; the canon text carried, md5 %s; the README item and the 1.5c-21 note carried to b750. SOURCE %s.' % (
        f['ln_keystone'], f['ln_stage'], f['ln_md5'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R359)(6))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; the Zenodo draft 23228113 at v1.2.0 deleted on the author`s word at [Z1], the deposit v1.1.2 and the concept unchanged. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1290']), ('REGISTERED', ['PLAN', 'NOTE', 'LINE']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b749 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
