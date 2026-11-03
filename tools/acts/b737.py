# -*- coding: utf-8 -*-
# b737 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R347)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R347)(2) repair it carries. Edited by the Edit tool. Carried at b737 by tools/b737_fold.py (`carry`) from tools/acts/b736.py,
# b736`s names substituted; the citation`s sections adopted from tools/b737_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b736`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b736`s carried till
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
# ### b737, Component 1 (the Edit tool): THE c1 ROUTE FOR b736'S WEIGHT LINE AND ITS CORRIGENDUM, (R347)(1)-(2). Carried from b736's
# ### override and rewritten here against b736's own banks: the closing's lines by needle, the events (10), the defects (38), the refusals
# ### (15), the v1.17.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '58f2c295'          # ### b736's closing commit
C1_REFUSAL_AT = '58f2c295'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-03'
C1_CORRIGENDA_LAST = 56
C1_V170 = 'b737_standing_v1170.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-03 by b737 to b736’s entry (:%d), under `(R347)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-DERIVES discharged on the three premise-free forms'
C1_TRAIL_NEEDLE = '### b736 — lane two, act one hundred and sixty-three, the second sitting under (R346)'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


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
    for l in _c1_rd('b736_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b736_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b736_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b736_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b736_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b736_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b736_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b736_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 7 or 'N5' in held or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b736_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b736_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b736_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (s_r, s_c, s_p, s_rp, s_s), l_st = _c1_fl('b736_sitting.txt', r'^### ### \*\*THE SITTING: (\d+) ROWS ; CARRIED (\d+) ; PASS (\d+) ; REPLACED (\d+) ; STRUCK (\d+)\.\*\*$', 'the sitting')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 11)) or len(dr) != 38:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b736 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b736_closing.txt):* “%s” (data/b736_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b736_steps.json, the record and closing rows). As its rows read: `W-ORD-ZQ-DERIVES` DISCHARGED on the three premise-free forms at PLACE-papers 89393bca; '
            'the second sitting %s rows, PASS %s, CARRIED %s ([76], [77], [25]-[29]), REPLACED %s ([111] by (A1)), STRUCK %s ([19]) (data/b736_sitting.txt :%d); the five Zenodo currency notes [104]-[108] banked for a Tier 3 act on the author’s record numbers; '
            '`W-ORD-ZQ-OFFLINE-ZERO` ENTERED in OPEN_TRAILS, priced at the act that takes it. Standing tools v1.16.0, 25 of 25; the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), '
            'G-AXIOM-CLAIM declared on the face, G-RULE-POSTSEAL-READ on a refused read, G-RUNNER-GATE vacuous with no dispatch; SCORES %d OF 8 HELD, N5 REFUTED on two clauses as the author accepted at the root: the face’s (W) row not naming the three files the author’s amendment of `(R346)`(4) widened, '
            'and two messages carrying add and commit together (22:22Z; 05:22Z as parallel calls). '
            'The root %s over %s banks, chained from %s (data/b736_act_root.json; :%d), the chain AGREE b624-b736; the mirror CLEAN; %s prompts banked as put by the seat (:%d); %d events in data/b736_events.txt, rows (1)-(%d); %d defects, (a)–(z) and (a’)–(l’) '
            '(data/b736_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone, as the ruling quotes it, CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'The draft at v5; nothing deposited, no Zenodo description edited; the corrigendum for these rows follows, under `(R347)`(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, s_r, s_p, s_c, s_rp, s_s, l_st, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                len(held), K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b736's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '20:49:14Z', 'b736 corrigendum'), (2, 'READ', '22:21:11Z', "defect (c)"), (3, 'PIPE', '22:21:13Z', 'defect (d)'), (4, 'READ', '22:22:40Z', 'defect (e)'), (5, 'READ', '22:22:40Z', 'defect (e)'),
               (6, 'READ', '22:29:15Z', 'defect (f)'), (7, 'PIPE', '22:35:58Z', 'defect (n)'), (8, 'PIPE', '22:35:58Z', 'defect (n)'), (9, 'READ', '22:40:51Z', 'defect (o)'), (10, 'PIPE', '23:07:53Z', 'defect (u)'),
               (11, 'PIPE', '02:04:56Z', "defect (d')"), (12, 'READ', '02:06:16Z', "defect (e')"), (13, 'PIPE', '02:19:17Z', "defect (g')"), (14, 'REDIR', '02:25:42Z', "defect (g')"), (15, 'POSTSEAL', '05:20:50Z', 'event (8)')]
C1_UNROWED = []
C1_CORR_TITLE = ('## Corrigendum to b736’s record (relay data/b736_events.txt rows (1)-(10) and data/b736_defects.txt): ten events and thirty-eight defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the face that did not follow the amendment at its head; the parallel add and commit, the locked bank, the clone’s snapshot, the root prompt’s promise, the post-seal list and the empty remote read, '
                 'at tools/standing/ v1.17.0, each controlled, under (R347)(2)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.7.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b736_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        if row == 'b736 corrigendum':
            if at not in _c1_rd('b736_corrigendum.txt'):
                bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if at[:5] not in src and at not in src and ('REFUSED BY THE HOOK (%s' % kind) not in src and 'refused by the hook' not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b736_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.17.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(10)', sorted(ev) == list(range(1, 11))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 38', len(dr) == 38), ('the refusals 15, each answered as listed', len(rl) == 15 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.17.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl_) == (int(cc), int(cd)))) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; counter %d, %d)' % (bad, bad_ref, nc, nl_))
    s['v170_foot'] = foot[0]
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
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’').replace('`', '’')


# ### the repairs each event is met by at v1.16.0
C1_EV_EXTRA = {1: '; repair (amend); rule (1) of data/b737_rules.txt', 2: '; repair (gitwrite); rule (2)', 3: '; repair (locked); rule (3)', 5: '; repair (promise); rule (5)',
               7: '; repair (gitwrite); rule (2)', 8: '; carried here as REPEAT of b732 event (11), the arm’s second failure, as `(R347)`(2)(vi) orders; repair (postseal); rule (6)',
               9: '; repair (emptyread), a guard; rule (7)'}
C1_DF_EXTRA = {'b': '; repair (gitwrite); rule (2) of data/b737_rules.txt', 'm': '; repair (snapshot); rule (4) of data/b737_rules.txt; the cause not established, and a third loss at this act'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b737, to the counter (`(R347)`(1)): the ruling’s “CLAIM 5, CLOSE 33, REPEAT 18 of 38” counts the thirty-eight defects alone; relay data/b736_closing.txt :5 prints CLAIM 7, CLOSE 41, REPEAT 22 OF 48 over the ten events and the defects together. Both read from the same tags; this entry prints both and edits neither.',
            'Dated note, b737, to OPEN_TRAILS :17361: the hand section’s CLAIM 6, CLOSE 38; REPEAT 20 of 44 is an earlier figure, read before the last four items landed; the closing’s :5 is the last figure.',
            'Dated note, b737, to relay data/b736_hook_refusals.txt :1: the refusal at 2026-11-02T20:49:14Z is b735’s late Read, entered at b736 as b735’s event (relay data/b736_corrigendum.txt); it is no item of b736’s 48.')
C1_CLASSES = (
    ('amend', 'the face that did not follow the amendment (`(R347)`(2)(i), event (1); CLAIM ; NEW)', 'rule (1) of data/b737_rules.txt; standing.amend regenerates the (W) row and N5’s write clause from the ruling plus the act’s amendment rows (data/<act>_amendments.json), read through the scorer’s own reader. b736’s amendment of `(R346)`(4) replayed: the route before read the ruling alone and found the face lacking nothing; the route after names the three doors with their repository, and a face carrying the regenerated row lacks none'),
    ('gitwrite', 'the parallel add and commit (`(R347)`(2)(ii), events (2), (7), defect (b); CLAIM ; REPEAT of b736 (b))', 'rule (2) of data/b737_rules.txt; the hook counts git writes per message from the session’s transcript, across parallel calls, and refuses the second. b736’s 05:22:31Z message replayed: the route before judged each call alone and refused none; the route after refuses the commit, the add standing; the chained form of 22:22Z refused by the command alone'),
    ('locked', 'the post-lock letter written and removed (`(R347)`(2)(iii), event (3); CLOSE ; NEW)', 'rule (3) of data/b737_rules.txt; the hook judges the Edit, Write and NotebookEdit tools and refuses a write to a tracked bank or tool of the act after its lock and before its closing, the events bank and the post-lock banks exempt. The 04:03:27Z Edit replayed: the matcher before never saw it; the route after refuses it'),
    ('snapshot', 'the pack loss (`(R347)`(2)(iv), defect (m); CLAIM ; REPEAT of b735 (p))', 'rule (4) of data/b737_rules.txt; standing.scratchfsck snapshot prints the fsck, the disk’s free space and the process listing, and standing.dispatchrows refuses a read, dispatch or clone row naming a clone without one before and after. The cause is not established. THE CONTROL DOES NOT READ CLEAN: zqwork3, clean at b736, lost its pack and info directories, objects/ last written 2026-11-03T03:54:09Z, about six hours after zqwork2’s loss as zqwork2’s was after zqwork’s; C: read 4389 MB free; a third instance, found by this reader and lettered in this act’s defects. zqwork, zqwork2 and zqwork3 stand in place'),
    ('promise', 'the root prompt’s promise (`(R347)`(2)(v), event (5); CLOSE ; NEW)', 'rule (5) of data/b737_rules.txt; standing.rootprompt compose_checked lets a clause about the entry stand only as a span the sealed composer’s entry carries or as procedure. b736’s recommended option replayed: passed before, refused after on “named in the entry and the events bank;”, and composing once regenerated without it'),
    ('postseal', 'the post-seal shell read of FINDINGS.md (`(R347)`(2)(vi), event (8); CLOSE ; REPEAT of b732 event (11))', 'rule (6) of data/b737_rules.txt; `hook.py excludes` prints the rule as the arm holds it, read first after the seal; b736’s 05:20:50Z `git grep` is a read the arm counts. A guard: no failing side'),
    ('emptyread', 'the chain part that got no answer (`(R347)`(2)(vii), event (9); CLOSE ; NEW)', 'rule (7) of data/b737_rules.txt; three repositories read empty make the row UNREAD, not AGREE. A guard: the route stood at b736, its part re-run alone and banked AGREE, and the instance shows it held'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b736’s events bank (relay data/b736_events.txt) carries ten rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank thirty-eight lettered rows, (a)-(z) and (a’)-(l’), each tagged in its own bracket (%s); its refusal bank fifteen lines at %s, '
         'each recorded by a row, the first b735’s. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R347)`(2), at tools/standing/ v1.17.0, each with a control on b736’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b736’s events (1)-(10):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( put and \d\d:\d\dZ answered)?( from [^:]*)?|post-push|pre-push and post-push)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b736_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b736’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b736_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b736’s refusals** (relay data/b736_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (ten events, thirty-eight defects), as b736’s closing prints it (relay data/b736_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b737 on the author’s ruling `(R347)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b737.py) from '
          'b736’s events and defects banks read unedited, its refusal bank, and the v1.17.0 controls bank; banked as relay `data/b737_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b736’s record; no sealed tool, face, trail or root-named bank of b736 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b737 -- THE CORRIGENDUM FOR b736, (R347)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b736_events.txt rows (1)-(10), data/b736_defects.txt 38 rows, data/b736_hook_refusals.txt 15 '
             'lines at %s; data/%s (the v1.17.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 10, DEFECTS 38 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.17.0: THE AMENDMENT REGENERATION, THE PARALLEL GIT WRITE, THE LOCKED BANK, THE CLONE`S SNAPSHOT, THE ENTRY`S PROMISE, '
               'THE POST-SEAL LIST, THE EMPTY REMOTE READ ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


C1_DISCHARGE_HEAD = '**`W-ORD-ZQ-DERIVES` DISCHARGED at b737, `(R347)`(2), on the navigator’s read:**'
C1_DISCHARGE = (C1_DISCHARGE_HEAD + ' the three premise-free forms are the instance’s theorems in the sense the order’s line meant (relay data/b730_ferry.txt :13), the bundle’s h filled by zq_premises: zq_count_instance at '
                'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean :194, zq_explicit_formula_instance at :198, zq_li_nonneg_imp_online_instance at :205, branch zq-b730 at b25fd82c, run 41483457057.' + NL + NL
                + '**Two conditions beside the read:** (a) what zqZeroConfig’s carrier is, is fixed by the compiled zeros field of zq_premises and by nothing in the ruling, and the sentence “the zeros of Z_Q0” means that carrier; '
                '(b) the grade is a reading of binders and confers nothing: no deposit, no tag, no line on any main; the branch zq-b730 stays a branch until the author’s word on a merge, which the ruling does not give.' + NL + NL
                + '**What did not compile:** no declaration locates a zero of Z_Q0 off the line, and no declaration states that Li nonnegativity fails for zqZeroConfig (relay data/b736_explicitformula.txt :212). The off-line zeros stand HELD at b725’s 69 to height 445 '
                'and the positivity failure HELD at b726’s two windows. The supportable sentence: “the count and the explicit formula compiled premise-free for an object whose off-line zeros are numerically located.”' + NL + NL
                + 'Dated note, b737, to `(R346)`(6): its sentence is withdrawn by `(R347)`(2), the sentence above standing in its place.')


C1_OFFZERO_HEAD = '**`W-ORD-ZQ-OFFLINE-ZERO` PRICED at b737, `(R347)`(3), planned and not built:**'
C1_OFFZERO = (C1_OFFZERO_HEAD + ' the candidate off0, β − 1/2 = 0.4532604748, γ = 16.29021572, chosen by the criteria printed at relay data/b737_offlinezero_plan.txt (a); box A, the square of half-side 0.1 centred on it, '
              'its least sampled |Z_Q0| on the boundary 0.357 (b). Routes R1 (the argument principle with a Lipschitz bound), R2 (Rouché) and R4 (the minimum modulus through Mathlib’s Complex.norm_le_of_forall_mem_frontier_norm_le, AbsMax.lean :405) priced; R3 (a sign change) not a route, no off-line segment carrying a real-valued restriction. '
              'R4 recommended: 1,635-4,175 lines from statements, 1,496-3,820 by explicitFormula’s measured ratio 0.915, the envelope of the five measured ratios 455-16,408; 9-22 dispatches; seven Mathlib objects absent at the pin (the argument principle, Rouché, the winding number, the incomplete gamma, complex Stirling with explicit error, the K-Bessel function, certified interval evaluation), three of them on R4’s path. '
              'The price driver every route shares: zqFn certified on the box to 0.1, Λ₀ to some 5e-12 at that height. Four stop points, the first a conditional theorem with no numeric step. '
              'No dispatch at b737; no Lean file. Until a build compiles the condition, no sentence says a zero is located in Lean or that positivity fails as a theorem.')


def c1(*a):
    """`c1 weight|corrigendum|discharge|offzero [dry|write]`: b736 at its weight after its entry, and the corrigendum for b736, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.17.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    if route == 'discharge':
        land([('OPEN_TRAILS.md', C1_DISCHARGE_HEAD, NL + C1_DISCHARGE + NL)], '%s_discharge_landing.json' % ACT, 'discharge', entry=None, dry=dry)
        return
    if route == 'offzero':
        land([('OPEN_TRAILS.md', C1_OFFZERO_HEAD, NL + C1_OFFZERO + NL)], '%s_offzero_landing.json' % ACT, 'offzero', entry=None, dry=dry)
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum | discharge | offzero  [dry | write]')
#⟪END⟫
# ### b737, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b737 ran three
# ### ((R347)(4)(iii)-(iv), N1), rowed in data/b737_dispatch_rows.json. Replaced for b737 alone; the arms' names stand, their plants on b737's rows.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R346)(7), as b736 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R347), N1, b737: no dispatch this act; no row and no run; VACUOUS on the read of a run, the plant a planted row refused."""
    rows = S['drows'] or []
    return not rows and not K.EF_RUNS and K.MAX_DISPATCHES == 0
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b737: no push, the print ran at the branch's standing tip
#⟪END⟫
# ### b737, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R347)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, unedited this act (its blob at 59e3efa8 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b737, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b736's record has twelve
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 9)) \
#⟪END⟫
# ### b737, Component 4 (the Edit tool): b737's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b736's override of checks 526 -- no registration commit -- removed: b737
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b737_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b737, Component 6 (the Edit tool): b737's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b736's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b737, Component 4 (the Edit tool): b736's overrides of checks 1516 and 1659 (hook.py edited by b736's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b737 as it stands
# ### b737, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b737_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b737, Component 4 (the Edit tool): b736's override of checks 1476-1482 (one ERRATA entry at b736's (R346)(5)) removed -- (R347)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b737 as it stands
# ### b737, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b736's step-zero wording; b737's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b737, Component 4 (the Edit tool): G-RUNNER-READ's plant on b737's dispatch rows -- run 2's axiom lines carrying sorryAx (b736's
# ### plant read the lv rows' closure log, which b737 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b737, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b737, Component 6 (the Edit tool): the fold bank was b736's own route
# ### (tools/b736_fold.py); b737's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b737_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b736.py -> tools/acts/b737.py' in (rd('b737_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b737, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b737_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b737, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b737_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b737_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b737, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R347): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    rows = [l for n_ in ('b737_defects.txt', 'b737_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R347) Component 5, the act`s events and defects together; relay data/b737_defects.txt, data/b737_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b737, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b737's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-DERIVES discharged at b737, W-ORD-ZQ-OFFLINE-ZERO entered at b737,',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b737, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b736's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b737_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b737_registration_%s.txt' % __import__('b737_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b737, Component 4 (the Edit tool, before the face): b736's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b737, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b737's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b737, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R347)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b737 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b737_ef\.py dispatch\b', re.M)   # ### b737: the build's one route
#⟪END⟫
# ### b737, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b736's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b737 scorer reads; the needles set to the banks b737's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b737, (R347)(2)(iii): b736's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b737, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b737_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrstuvwxyz') + ("a'", "b'", "c'", "d'", "e'", "f'", "g'", "h'", "i'", "j'", "k'", "l'")))   # ### (a)-(z) and (a')-(l'), entered before the lock, every one the seat's (data/b737_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b737_corrigendum.txt', 'data/b737_standing_v1160.txt', 'data/b737_discharge.txt', 'data/b737_sitting.txt', 'data/b737_sitting.json', 'data/b737_author_words.txt', 'data/b737_pathrefusal.txt',
                  'data/b737_reproduce.txt', 'data/b737_reproduce.json', 'data/b737_address_scan.txt', 'data/b737_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b737 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R347)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b737_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R347)(2)-(3) (b737's keys over b737's objects): the order by time and ancestry; v1.15.0's controls; the build's bank, the plan and the dispatch rows;
        # ### the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the plan at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('plan_standing', K.REG_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_print', K.C1_CORR, K.PRINT_COMMIT))),
        v1130=rd('b737_standing_v1160.txt'), plan=rd('b732_phase2_frontdoors.txt'), print_=rd('b737_sitting.txt'), rows_bank=rd('b737_discharge.txt'), sittingj=jl('b737_sitting.json'),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        sit_files=dict((k_, gs('D:/' + k_, 'diff', '--name-only', jl('b737_kernel_bases.json').get(k_), K.SITTING_TIPS[k_]).split()) for k_ in K.SITTING_TIPS),
        sit_main=dict((k_, gs('D:/' + k_, 'rev-parse', 'refs/heads/main').strip()) for k_ in K.SITTING_TIPS),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b737_dispatch_rows.json') or '[]'), reproduce=rd('b737_reproduce.txt'), reproducej=jl('b737_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b737_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b736 left them
        rebuild=None, rebuild_rows=json.loads(rd('b737_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.REG_COMMIT), discharge=_ct(PP, K.C1_DISCHARGE_PP), first_item=_ct(PP, K.SITTING_PP[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.PRINT_COMMIT), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b737's read-first bank's items by path, as its step zero wrote them (data/b737_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b736_closing.txt |', 'relay data/b736_events.txt |', 'relay data/b736_defects.txt |', 'relay data/b736_explicitformula.txt |', 'relay data/b730_ferry.txt |', 'relay data/b732_phase2_frontdoors.txt |',
                     'relay data/b732_phase2_doors.txt |', 'relay data/b725_interference.txt |', 'relay data/b726_frontdoors.txt |', 'relay data/b727_sitting.txt |', 'relay tools/e0_rule.py |', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/EpsteinZQ.lean |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R347)(1)-(2))', 'DISCHARGE AND THE SITTING ((R347)(2), (4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (85 = 85 + 0, data/b737_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 85 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b736's figures, read at FINDINGS :12909 as Component 1 landed them
    return landed(S, 0, ['b736 AT ITS WEIGHT', 'suite 115 of 116', 'relay d20a7119', '26 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b737's title in the ferry's Component 3 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-ZQ-DERIVES discharged on the three premise-free forms, the landed lines INTERFACES; the second sitting: ', ' carried of 111; W-ORD-ZQ-OFFLINE-ZERO entered, priced at the act that takes it; ', 'the vacuous-pass arm and ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R347)(1)-(3): the generated entry for b736's eight events and twenty-six defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(8), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 2, CLOSE 32 over 34, REPEAT 12); the repairs at tools/standing/ v1.16.0 by their controls
    bank; the corrigenda bank appended at row (56) and nothing before it changed; in Component 1's commits (the figures read from
    data/b737_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 26 and len(items) == j.get('items') == 34 and j.get('row') == 56 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 34 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 2 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 12 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.16.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 4 \
        and '  (56) ' in S['corrigenda'] and '  (57) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b737_rules.txt carries (R347)(3)'s five rules; data/b737_rules.txt (by form in (R347)(5)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b736's form, its names b737's); no author's word of b737 orders a row of the next act's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and 'THE SCORE ROUTES` DRY FORM RUNS BEFORE THE GATE CLEARS' in r1.replace("'", '`') and 'READS THE PROOF TERM' in r1 and not os.path.exists(os.path.join(D, 'b737_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b737's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- W-ORD-ZQ-DERIVES DISCHARGED', 'CERTIFIED -- tools/standing/ v1.16.0', 'REGISTERED -- THE SITTING',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b737: no dispatch this act -- no dispatch command in the capture, no row; VACUOUS on every row's read; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### N1: no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b737_ef\.py"? dispatch\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b737, N1: no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (the ledgers and the doors the passed items name), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b737's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The discharge**', '**The sitting**', '**The doors at main**', '**The order entered**', '**The Zenodo drafts**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b737_corrigendum.txt', 'data/b737_standing_v1160.txt', 'data/b737_discharge.txt', 'data/b737_sitting.txt', 'data/b737_author_words.txt',
                 'data/b737_reproduce.txt', 'data/b737_address_scan.txt', 'data/b737_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b737: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R347)(3)-(4), N2 (the name the frozen run list carries): the agenda's commit first, then v1.16.0's, the corrigendum's and the sitting's bank, in that order by time and by ancestry within the relay;
    the agenda at HEAD its text at its commit; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('plan', 'standing', 'corr', 'print')
    return K.REGISTRATIONS in S['files']['reg'] and bool(reg) and reg == head \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b737_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    the kernels the sitting wrote; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R347)(3)-(5), N2 (the name the frozen run list carries): the weight and corrigendum, then the discharge by a commit of its own, before the first sitting item on PLACE-papers by the commits' times; v1.16.0 before that item ((3) whole before (4)); the sitting's bank after it."""
    t_ = S['t']
    return K.REGISTRATIONS in S['files']['reg'] and all(t_.get(k_) for k_ in ('c1pp', 'discharge', 'first_item', 'standing', 'print')) \
        and t_['c1pp'] < t_['discharge'] < t_['first_item'] and t_['standing'] < t_['first_item'] < t_['print'] and S['anc'].get('corr_print') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R347)(4), N3 (the name the frozen run list carries): every item of the agenda, 1 to 111, and (A1), (A2), (B), (C) a row of the sitting's bank with the author's word beside it; no PASS without its confirmation or its banked state; [19] STRUCK; [25]-[29], [76], [77] CARRIED; the bank's foot the rows'; the words the bank names."""
    R = S['sittingj'] or {}
    want = [str(n) for n in range(1, 112)] + ['A1', 'A2', 'B', 'C']
    miss = [k for k in want if k not in R or not (R[k].get('word') or '').strip()]
    st = lambda k: (R.get(k) or {}).get('state') or ''
    v = _vlast(S['print_'] or '')
    return not miss and st('19').startswith('STRUCK') and all(st(str(n)).startswith('CARRIED') for n in (25, 26, 27, 28, 29, 76, 77)) \
        and st('111').startswith('REPLACED') and ('THE SITTING: %d ROWS' % len(R)) in v and len(R) == 117 \
        and all(r.get('confirm') or not r.get('state', '').startswith('PASS') for r in R.values()) \
        and 'BEGINPass [78]' in (rd('b737_author_words.txt') or '') and 'BEGINPass [109]' in (rd('b737_author_words.txt') or '')
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 as amended (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip locally and at origin; zq-b730's diff against its entering tip empty, no Lean file this act;
    each of the 21 kernels the sitting wrote at its main's tip, its diff from its base README.md alone."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and not S['zq_files'] and len(K.SITTING_TIPS) == 21 and all(S['sit_files'].get(k_) == ['README.md'] and S['sit_main'].get(k_, '').startswith(h_) for k_, h_ in K.SITTING_TIPS.items())

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.16.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b736's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R347)(2), (4)(C), N2, N3 (the name the frozen run list carries): the agenda unmoved at its commit's md5; the discharge's bank at its foot; W-ORD-ZQ-OFFLINE-ZERO entered in OPEN_TRAILS, priced and not built, its price the plan act's, no sentence of its entry a location."""
    n_ = S['rows_bank'] or ''
    import hashlib as _hl
    return _hl.md5(raw(os.path.join(ROOT, *K.REGISTRATIONS.split('/')))).hexdigest() == K.PLAN_MD5 and 'W-ORD-ZQ-DERIVES DISCHARGED BY A COMMIT OF ITS OWN' in _vlast(n_) \
        and 'ENTERED at b737, `(R347)`(4)(C), priced and not built' in S['ot'] and 'The price: the seat’s estimate from statements in a plan bank at the act that takes it, not this one.' in S['ot']


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
    """standing clauses v9 (Component 7 of (R347): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b737_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b736's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R347-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b736's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R347) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b736's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R346)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 85 = 85 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b736-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 3 form: W-ORD-ZQ-DERIVES discharged, the landed lines INTERFACES, the sitting`s counts of 111, W-ORD-ZQ-OFFLINE-ZERO entered, the vacuous-pass arm and the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R347)(1)-(3): the generated corrigendum for b736`s record, landed at FINDINGS :12911: its eight events and twenty-six defects, 34 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 2 CLOSE 32, REPEAT 12; v1.16.0`s repairs by data/b737_standing_v1160.txt; the corrigenda bank appended at row (56)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b737_rules.txt carrying (R347)(3)`s five rules, no data/b737_rules.txt',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b737's objects
    ('G-REGISTRATIONS-FIRST', '(R347)(3)-(4), N2: the agenda`s commit, v1.16.0`s, the corrigendum`s and the sitting bank`s in that order by time and ancestry; the agenda at HEAD its text at 2822aa73; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_print=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b737_address_scan.py run live over every commit of the act in the relay, PLACE-papers and the kernels the sitting wrote, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R347)(3)-(5), N2: the weight and corrigendum, then the discharge by a commit of its own, before the first sitting item by time; v1.16.0 before that item; the sitting`s bank after it',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_print=False))),
    ('G-DERIVATION-GRADED', '(R347)(4), N3: every item 1-111 and (A1), (A2), (B), (C) a row with the author`s word; [19] STRUCK, [25]-[29], [76], [77] CARRIED, [111] REPLACED; the bank`s foot the rows`; the author`s words at [78] and [109] verbatim',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'sittingj', lambda d: d.pop('19', None))),
    ('G-OFFSET-POST-HOC', 'N5 as amended: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against its entering tip empty, no Lean file this act; each of the 21 kernels at its main`s tip, its diff from its base README.md alone',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at d4e0ea02, VERSION 9; v8 at HEAD its blob at d4e0ea02; no v10; v9`s commit an ancestor of v1.16.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R347)(2), (4)(C), N2, N3: the agenda unmoved at its commit`s md5; the discharge`s bank at its foot; W-ORD-ZQ-OFFLINE-ZERO entered in OPEN_TRAILS, priced and not built, its price the plan act`s',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'rows_bank', (S['rows_bank'] or '').replace('W-ORD-ZQ-DERIVES DISCHARGED', 'W-ORD-ZQ-DERIVES CARRIED'))),
    ('G-DIFFERS-ERRATA', '(R347): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in dadfdf07, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b737_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R347-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b736`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at d4e0ea02 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no dispatch this act, no row and no run; VACUOUS on the rows` read, the plant a planted dispatch refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture and no row, the order and memory reads VACUOUS; no b721-b736 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b736 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b736`s [41] tip; the join kernel`s main and its one tag v0.1.0; the 21 kernels` README commits read at G-OFFSET-POST-HOC',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers and the doors the passed items name); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b736`s trail record on OPEN_TRAILS (:17283) and its root in the chain', lambda S: '### b736 — lane two, act one hundred and sixty-two, the build act under (R346)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers and the doors the passed items name): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b736`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b737, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R347)(3): a main at its sitting tip, its tags unmoved, is not a move against b736's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b737: (R347)'s rows. (1)'s line read by the ruling from the public relay at 58f2c295
    pub = _blob('D:/relay', '58f2c295', 'data/b736_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b736_closing.txt :1, the head line as the public relay carries it at 58f2c295', bool(pub) and pub[0] == at(cl, 1) and 'relay 68e793fa' in pub[0] and 'PLACE-papers 9b12ec5' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 113 of 116', 'root 0c6cc62f2193ba6a', '63 prompts answered', 'scores 7 of 8 HELD', '38 defects'):
        add('ruling (1)', 'data/b736_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'the closing`s counter CLAIM 7, CLOSE 41, REPEAT 22 OF 48 (events and defects), data/b736_closing.txt :5; the ruling`s CLAIM 5, CLOSE 33, REPEAT 18 of 38 the defects alone',
        'CLAIM 7, CLOSE 41, REPEAT 22 OF 48' in at(cl, 5), at(cl, 5)[-40:], '1')
    dfl_ = [l for l in lines_of(p('data', 'b736_defects.txt')) if re.match(r"^    \([a-z]'?\) ", l)]
    tg_ = (sum(1 for l in dfl_ if '[CLAIM' in l), sum(1 for l in dfl_ if '[CLOSE' in l), sum(1 for l in dfl_ if '; REPEAT' in l), len(dfl_))
    add('ruling (1)', 'data/b736_defects.txt, the defects alone CLAIM 5, CLOSE 33, REPEAT 18 of 38', tg_ == (5, 33, 18, 38), 'CLAIM %d CLOSE %d REPEAT %d OF %d' % tg_, '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b736']]
    add('ruling (1)', 'data/act_roots.txt, b736`s root 0c6cc62f chained from b735`s 879dfce5', len(ar8_) == 1 and ar8_[0][1].startswith('0c6cc62f') and ar8_[0][2].startswith('879dfce5'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b736_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b736 (b736`s post-push part b3)', 'b736 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b736 AGREE' if 'b736 AGREE' in b3_ else 'ABSENT', '1')
    si_ = lines_of(p('data', 'b736_sitting.txt'))
    add('ruling (1)', 'data/b736_sitting.txt :1175, 117 rows, CARRIED 7, PASS 108, REPLACED 1, STRUCK 1', 'THE SITTING: 117 ROWS ; CARRIED 7 ; PASS 108 ; REPLACED 1 ; STRUCK 1.' in at(si_, 1175), at(si_, 1175)[:60], '1')
    for n_ in (76, 77, 25, 26, 27, 28, 29):
        add('ruling (1), (4)', 'data/b736_sitting.txt, the row [%d] CARRIED' % n_, any(l.startswith('[%d] CARRIED' % n_) for l in si_), 'read', '1')
    in_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (3)(a)', 'data/b725_interference.txt :31, the table`s head', at(in_, 31).strip().startswith('name    beta - 1/2') and 'gamma' in at(in_, 31), at(in_, 31)[:60], '1')
    add('ruling (3)(a)', 'data/b725_interference.txt :32, off0 at 0.4532604748, 16.290216, 200 bits', at(in_, 32).split()[:3] == ['off0', '0.4532604748', '16.290216'] and ' 200 ' in at(in_, 32), at(in_, 32)[:60], '1')
    rg5_ = lines_of(p('data', 'b725_registration_2026-10-30.txt'))
    add('ferry (read first)', 'data/b725_registration_2026-10-30.txt :159, H-INTERFERENCE at Q0`s 69 off-line zeros to height 445', '69 certified off-line zeros to height 445' in at(rg5_, 159), at(rg5_, 159)[:60], '1')
    ef_ = lines_of(p('data', 'b735_explicitformula.txt'))
    add('ruling (3)(e)', 'data/b735_explicitformula.txt :184-:185, zq_li_nonneg_imp_online_instance an implication', 'zq_li_nonneg_imp_online_instance' in at(ef_, 184) and 'ρ.re = 1 / 2' in at(ef_, 185), at(ef_, 185)[:60], '1')
    add('ruling (3)(e)', 'data/b735_explicitformula.txt :212, nothing locates any zero', 'nothing here locates any zero' in at(ef_, 212), at(ef_, 212)[:60], '1')
    pm_ = lines_of(p('data', 'b731_price_measured.txt'))
    add('ruling (3)(d)', 'data/b731_price_measured.txt :17-:19, 835 / 786 / 340 measured', '835' in at(pm_, 17) and '786' in at(pm_, 18) and '340' in at(pm_, 19), at(pm_, 17)[:50], '1')
    add('ruling (3)(d)', 'data/b735_explicitformula.txt :201, 1949 lines against the 2130', '1949 lines' in at(ef_, 201) and '2130' in at(ef_, 201), at(ef_, 201)[:60], '1')
    ct_ = lines_of(p('data', 'b730_continuation.txt'))
    add('ruling (3)(c)', 'data/b730_continuation.txt :55, the continuation field CLOSED at 835 lines', 'THE continuation FIELD CLOSED' in at(ct_, 55) and 'LINES 835' in at(ct_, 55), at(ct_, 55)[:60], '1')
    add('ruling (3)(c)', 'data/b730_continuation_plan.txt', os.path.exists(p('data', 'b730_continuation_plan.txt')), 'present', '0')
    add('ruling (1)', 'tools/standing/VERSION v1.16.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.16.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(10) and 38 defects (data/b736_events.txt, data/b736_defects.txt)',
        starts == list(range(1, 11)) and len(letters) == 38, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b736_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    df_ = rd(p('data', 'b736_defects.txt')) or ''
    for l_, w_ in (('b', 'add and commit chained'), ("i'", 'author`s words were banked'), ('m', 'zqwork2'), ('r', 'ORCID')):
        add('ferry (read first)', 'data/b736_defects.txt (%s)' % l_, ("    (%s) " % l_) in df_ and w_.replace('`', "'") in df_.replace('’', "'"), 'read', '1')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ferry (read first)', 'zq-b730 at b25fd82c', zt_.startswith('b25fd82c'), zt_[:8], '3')
    mn_ = gr(EF_, 'show', 'b25fd82c:SIDEExplicitFormula/Schema/ZQ/EF/Main.lean').split(NL)
    add('ruling (3)(e)', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean :205 at b25fd82c', at(mn_, 205).startswith('theorem zq_li_nonneg_imp_online_instance'), at(mn_, 205)[:60], '2')
    ml_ = gr('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'rev-parse', 'HEAD')
    add('ferry (read first)', 'Mathlib at de5ce8a9', ml_.startswith('de5ce8a9'), ml_[:12], '3')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :12989, b736`s entry', 'W-ORD-ZQ-DERIVES discharged' in at(fd_, 12989), at(fd_, 12989)[:50], '0')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (3)', 'OPEN_TRAILS :17339, W-ORD-ZQ-OFFLINE-ZERO ENTERED at b736', 'W-ORD-ZQ-OFFLINE-ZERO' in at(ot_, 17339) and 'ENTERED at b736' in at(ot_, 17339), at(ot_, 17339)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    se_ = (gr('D:/SIDE-effects', 'rev-parse', 'main') or '').strip()
    add('ruling (4)', 'SIDE-effects at main, its commit printed', bool(se_), se_[:8] or 'ABSENT', '0')
    add('ferry', 'tools/standing/ at v1.16.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.16.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R347)(4): b736's export, the mirror's last
    add('ruling (4)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-02-b736.zip, b736`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R347)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b736-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R347)(5): act_current alone, then b736's step row 24, its closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b736_steps.json'),
                   (K.STEPZERO, 'data/b736_relay_push-b736-closing_push_out.txt'), (K.STEPZERO_PREVBUILD, 'tools/mirror_prevbuild.json')):
        if not c_:
            add('ruling (2)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (2)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (4)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (4)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b737_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b737_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b737 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b736_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.16.0's controls, the discharge and the sitting, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R347)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R347)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: README.md alone on the 21 kernels the passed numbers name, by the author's word amending (R347)(4); no Lean file, no main's code, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b737 ((R347)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R346)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b737 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY-THREE, THE SECOND SITTING: b736 AT ITS WEIGHT; W-ORD-ZQ-DERIVES DISCHARGED ON THE NAVIGATOR`S READ; THE CORRIGENDUM OPENING ON THE VACUOUS PASS AND THE PRIVATE LEXICON; '
              'THE SITTING OVER data/b732_phase2_frontdoors.txt WITH THREE ITEMS AT ITS HEAD, UNDER (R347).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b736's sections over b736's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.16.0: the proof-head arm at the head, the private lexicon landed, the refused read, the clone`s fsck, the reaped watch, the score routes` dry form, the counter, each case failing before its repair and passing after', 'b737_standing_v1160.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE DISCHARGE AND THE SITTING ((R347)(2), (4))', [
                ('W-ORD-ZQ-DERIVES discharged by a commit of its own, its two conditions and what did not compile beside it', 'b737_discharge.txt'),
                ('one row per item of the agenda and the three at its head, the author`s word beside each', 'b737_sitting.txt'),
                ('the probe-path refusal printed before the lock gate', 'b737_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b737_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b736`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b737_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R346)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no branch moved ; README.md alone on ' + str(len(WL.SITTING_TIPS)) + ' kernels` mains by the author`s word amending (R347)(4), push-b737-sitting left local on each, no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none) ; the rebuild-b721 branches of the wave 1 kernels as b736 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b736-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the discharge committed before any sitting item, the tools` controls before their figures, the pre-lock comparison and the probe-path refusal before the lock gate ;',
    '    N3: no sitting item written without the author`s number printed in the bank ; no sentence says an off-line zero is located in Lean or positivity fails as a theorem ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b737_address_scan.txt, data/b737_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the description writes under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; the deposit route untouched, publish never called, the draft held at v5 ; no Zenodo description written, the 8 records` drafts banked for a Tier 3 act on the author`s number ; GitHub descriptions written by the route b727 used, each read back ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS (the discharge, (C), the trail) and the doors the passed items name written ; no paper moved or renamed, THE_FINDINGS_AS_THEY_STAND at a new v0.7 beside v0.6 ;',
    '    no FOUNDATIONS, REGISTRY or faces page byte ; data/act_roots.txt (b737`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.16.0 and tools/e0_rule.py by (R347)(3) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b736 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R347)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZQ-OFFLINE-ZERO (OPEN_TRAILS), the plan bank at its price, the note that the plan may pick a better-isolated zero than the lowest ; the items carried by number, relay data/b737_sitting.txt ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b737_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b736 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main but the sitting`s README.md commits, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b736`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b737: the standing repairs are v1.16.0's ((R347)(3), relay data/b737_standing_v1160.txt, read in the corrigendum section); the
    # ### carry's diffs here (b737 carried at step zero before the fold; its tools since are the templates and tools/acts/b737.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; README.md alone on the sitting`s 21 kernels` mains; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b736 left them; port-b707 at b712`s tip %s)' % (
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
    b737's form over b737's objects (b736's form in git at b736's record tool): the corrigendum's foot and v1.16.0's controls; the discharge's and the sitting's feet;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1160.txt' % ACT, r'\*\*v1\.16\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.16.0`s controls')
    _bfig('%s_discharge.txt' % ACT, r'\*\*(W-ORD-ZQ-DERIVES DISCHARGED BY A COMMIT OF ITS OWN) ;', 'the discharge`s foot')
    sf = _bfig('%s_sitting.txt' % ACT, r'\*\*THE SITTING: (\d+) ROWS ; CARRIED (\d+) ; PASS (\d+) ; REPLACED (\d+) ; STRUCK (\d+)\.\*\*', 'the sitting`s foot')
    sj = jl('%s_sitting.json' % ACT)
    sn = [v_ for k_, v_ in sj.items() if k_.isdigit()]
    sc_ = lambda w_: sum(1 for v_ in sn if v_['state'].startswith(w_))
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], repairs=len(v5[0].split(', ')),
                sit_rows=int(sf[0]), sit_n=len(sn), sit_p=sc_('PASS'), sit_r=sc_('REPLACED'), sit_s=sc_('STRUCK'), sit_c=sc_('CARRIED'),
                sit_bank=sum(1 for v_ in sn if 'BANKED ONLY' in v_['state'] or re.search(r'as \[10[4-8]\]', v_['state'])), sit_desc=sum(1 for v_ in sj.values() if (v_.get('confirm') or '').startswith('gh ')),
                sit_kc=sum(1 for v_ in sj.values() if (v_.get('confirm') or '').startswith('SIDE-')), sit_pp=sum(1 for v_ in sj.values() if (v_.get('confirm') or '').startswith('PLACE-papers')),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R347)(3): the kernel rows of one kind as banked (data/b737_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R347): no lean process runs on this host and no dispatch is made. From the command bank (the seat's commands, read live from the
    capture by the `commands` route) and the worklist's EF_RUNS, empty."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b737_commands.json): %s; dispatch commands in the capture: %s, the worklist`s runs %d, rows read %s, VACUOUS on a row`s free memory: no dispatch row exists' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b737's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b737_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b737_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R347): the discharge commits before any sitting item, controls before figures: the agenda's commit, v1.16.0's, the weight and corrigendum's, the discharge's, the first item's and the sitting bank's in that order by time;
    the pre-lock comparison and the probe-path refusal printed before the lock gate; each tool's controls before its figures."""
    chain_ = [(ROOT, K.REG_COMMIT), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (PP, K.C1_DISCHARGE_PP), (PP, K.SITTING_PP[0]), (ROOT, K.PRINT_COMMIT)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, K.PRINT_COMMIT], capture_output=True).returncode == 0
    plan_ = K.REGISTRATIONS[len('data/'):]
    same_ = _s_md5(os.path.join(ROOT, *K.REGISTRATIONS.split('/'))) == K.PLAN_MD5 and rdn(plan_) == g(ROOT, 'show', '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS)).replace(chr(13), '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = same_ and bool(tz) and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the agenda its md5 %s and its blob at %s: %s; the pre-lock comparison banked: %s; the probe-path refusal banked and clear: %s; the agenda, v1.16.0, the weight and corrigendum, the discharge, the first sitting item and the sitting`s bank in that order by time: %s (%s), the agenda an ancestor of the bank: %s; the tools` controls before their figures: %s' % (
            K.PLAN_MD5[:8], K.REG_COMMIT, same_, bool(tz), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b737's objects; b736's in git at b736's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b737_standing_v1160.txt', ('ALL AS WANTED',)), ('b737_discharge.txt', ('W-ORD-ZQ-DERIVES DISCHARGED',)), ('b737_sitting.txt', ('THE SITTING:',)),
             ('b737_corrigendum.txt', ('ITEMS',)), ('b737_citation_check.txt', ('CITES CHECKED',)), ('b737_reproduce.txt', ('REPRODUCES',)), ('b737_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R347): no sitting item written without the author's number printed in the bank; no sentence says an off-line zero is located in Lean or positivity fails as a theorem; no sentence calls the instance more than DERIVES on the three forms. From the banks' last
    lines, the sitting's rows and the entry's sentences."""
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
    rows_ = jl('%s_sitting.json' % ACT)
    no_word = [k_ for k_, v_ in rows_.items() if not (v_.get('word') or '').strip()]
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'   # ### defect (k'): "Nothing here ... locates any zero" read as a location
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|locates? (?:a|any|one) zero|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    more_ = [s_ for s_ in sents if re.search(r'\binstance\b[^.;]*\b(?:PROVED|proved|CLOSED|VERIFIED|verified)\b', s_) and not re.search(neg_, s_)]
    ok = all(o for _n, o in graded) and bool(rows_) and not no_word and not loc_ and not more_
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the sitting`s %d rows, a row without the author`s word: %s; read from %s, a sentence saying an off-line zero is located in Lean or positivity fails as a theorem: %s; a sentence calling the instance more than DERIVES on the three forms: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), len(rows_), no_word or 'NONE', src, loc_ or 'NONE', more_ or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R347) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R347)(5))
# ### (R347)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R347) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b736's form, carried) -- read from git,
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
    # ### (R347)(4)-(5), N5 as amended: every ref of every kernel carrying a commit made after the act's opening commit is a sitting kernel's main or its push-b737-sitting; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b736 left them; the address scan's count from its bank (relay data/b737_address_scan.txt), the suite's arm recounting it live
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
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b737_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than the sitting`s main and push-b737-sitting at the sitting`s tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b737 — lane two, act one hundred and sixty-three, the second sitting under (R347): b736 at its weight and its corrigendum; v1.16.0; '
            'W-ORD-ZQ-DERIVES discharged on the navigator’s read; the agenda of 111 items by the author’s number')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 5 form; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## W-ORD-ZQ-DERIVES discharged on the three premise-free forms, the landed lines INTERFACES; the second sitting: %d items passed, %d replaced, %d struck, %d carried of %d; W-ORD-ZQ-OFFLINE-ZERO entered, priced at the act that takes it; the vacuous-pass arm and %d repairs landed' % (
        f['sit_p'], f['sit_r'], f['sit_s'], f['sit_c'], f['sit_n'], f['repairs'] - 1))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) Part A’s followers read as passing with the Part B paragraph they name, each row printing “as [n]”, the author’s number being the Part B item’s; (2) a README’s removals taken at whole sentences, whole list items and whole italic lines, a fence or table emptied falling whole and a head emptied falling, each diff in relay data/b737_sitting_diffs/; (3) the descriptions’ route read as gh repo edit, b727’s, each read back; [101] no write, the draft equal to the line; (4) SIDE-effects drafted and not written, no passed row naming a change to it; '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R347)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b737's objects; b736's composer in git at
    b736's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R346)(2)(v)
    e = ['', _title(), '',
         'W-ORD-ZQ-DERIVES is discharged by `(R347)`(2) on the navigator’s read of three premise-free forms, the landed lines at Schema/EpsteinZQ.lean :153, :157 and :164 reading INTERFACES on h as they stood. The second sitting exhausted its agenda: of %d items %d passed, %d replaced by (A1), %d struck unread and %d carried by number, each on the author’s word printed in the bank; the writes %d README commits over 21 kernels, %d GitHub descriptions and %d PLACE-papers items, one git write to each, and (A1)’s :685 repaired forward by a commit of its own (defect (r)). W-ORD-ZQ-OFFLINE-ZERO is entered and priced at the act that takes it. The draft stands at v5, HELD.' % (
             f['sit_n'], f['sit_p'], f['sit_r'], f['sit_s'], f['sit_c'], f['sit_kc'], f['sit_desc'], f['sit_pp']), '',
         '*Filed at b737 on the author’s ruling `(R347)`, amended at (4) by the author’s word; %d question%s put before the root. Banks: relay '
         '`data/b737_corrigendum.txt`, `data/b737_standing_v1160.txt`, `data/b737_discharge.txt`, `data/b737_sitting.txt`, `data/b737_author_words.txt`, `data/b737_prelock.txt`, `data/b737_pathrefusal.txt`, '
         '`data/b737_reproduce.txt`, `data/b737_address_scan.txt`, `data/b737_touch.txt`, `data/b737_standing_figures.txt`, `data/b737_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R347)(1), (3), %s, %s, %s): b736 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b736’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b737_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b737_standing_v1160.txt), the proof-head arm at their head.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): v1.16.0 at %s, then the weight and the corrigendum at PLACE-papers %s, then the discharge by a commit of its own at %s, all before the first sitting item at %s; the agenda’s md5 %s equal to its blob at %s; the sitting’s bank at %s; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b737_prelock.txt, data/b737_pathrefusal.txt). No lean process on this host and no dispatch: the runner arms read VACUOUS, no row existing to read.' % (K.C1_STANDING[:8], K.C1_PP[:8], K.C1_DISCHARGE_PP[:8], K.SITTING_PP[0][:8], K.PLAN_MD5[:8], K.REG_COMMIT[:8], K.PRINT_COMMIT[:8]), '',
         '**The discharge** ((R347)(2), N3): the three forms are zq_count_instance, zq_explicit_formula_instance and zq_li_nonneg_imp_online_instance at Schema/ZQ/EF/Main.lean :194, :198 and :205, branch zq-b730 at b25fd82c, run %s, the order’s meaning read by the navigator at relay data/b730_ferry.txt :13. Two conditions stand beside it: what zqZeroConfig’s carrier is, is fixed by the compiled zeros field of zq_premises; the grade is a reading of binders and confers nothing, the branch stays a branch. No declaration locates a zero of Z_Q0 off the line and none states that Li nonnegativity fails for zqZeroConfig; the off-line zeros stand HELD at b725’s 69 to height 445 and the positivity failure HELD at b726’s two windows. (R346)(6)’s sentence is withdrawn, its dated note in the trail (OPEN_TRAILS at PLACE-papers %s; relay data/b737_discharge.txt).' % (K.ZQ_RUN, K.C1_DISCHARGE_PP[:8]), '',
         '**The sitting** ((R347)(4) as amended, N3): (A1), (A2), (B) and (C) put before the agenda, then its items in their order, each with current words and drafted words, its file, line and grade; the author’s number read before any write and printed in the row; one git write per passed item. [19], the private kernel, struck unread; [111] replaced by (A1) by the author’s word; [76] and [77] carried for a redraft at main, [25]-[29] with them. [68], [92], [98] and [109] amended by the author’s words, and six further lines out by the author’s word at [72], [78], [80], [82], [92] and [96] (relay data/b737_sitting.txt, the words at data/b737_author_words.txt, each README’s removals at data/b737_sitting_diffs/).', '',
         '**The doors at main** (N5 as amended): the agenda’s drafts were read at the census pin and each was checked at main before it was put, the drafts standing wrong or short there amended or carried. README.md alone on the 21 kernels, no Lean file and no main’s code, no tag; two repairs by further commits on the author’s numbers, [60R] and [66R], the plan’s fragments and an empty fence, each found before its kernel’s push and each in the seat’s defects. PLACE-papers: (A1) and (A2), the findings paper at v0.7 by the repair the author passed, (B) at Which_Structure_Confines v2.4.0, (C), [109] and [110] at STORMER.md.', '',
         '**The order entered** ((R347)(4)(C)): W-ORD-ZQ-OFFLINE-ZERO in OPEN_TRAILS at PLACE-papers %s, priced and not built: its object, condition, consequence, price and trigger as (C) words them. The price is the plan act’s. Until a declaration compiles, no sentence says a zero is located in Lean or that positivity fails as a theorem.' % K.SITTING_PP[4][:8], '',
         '**The Zenodo drafts**: %d records’ drafts ruled by number and banked only, carried to a Tier 3 act on the author’s number; no Zenodo description edited.' % f['sit_bank'], '',
         '**What this act is not**: no deposit, no tag, no draft published, no Lean file written, no merge. A README sentence removed removes a claim from a door; it proves nothing. Nothing here proves RH or GRH or locates any zero.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b737_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b737_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b737_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b737 -- %s, %s, %s, %s -- against b736’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b737_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the discharge and the sitting read one way: the grade says what the statements bind, and the doors now say what compiled and no further, so the kernels’ front pages and the ledger are counted off one reading.', '',
         '**Carried to:** %s, (R347)(7): W-ORD-ZQ-OFFLINE-ZERO’s plan bank; items [76], [77] and [25]-[29], by number; the Zenodo drafts, to a Tier 3 act on the author’s number; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b736():
    """b736's form over b736's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b737's objects; b736's composer in git at b736's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD, W-ORD-ZQ-DERIVES closed by its own commit and W-ORD-ZQ-OFFLINE-ZERO entered by (C)."""
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
             '**(R347) ratified.** Its components as the ferry orders them (relay data/b737_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b736’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** the discharge of W-ORD-ZQ-DERIVES at PLACE-papers %s, the entry of W-ORD-ZQ-OFFLINE-ZERO at %s, each by its own commit, read above.' % (K.C1_DISCHARGE_PP[:8], K.SITTING_PP[4][:8]), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b737_standing_v1160.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The sitting:** of %d items %d passed, %d replaced by (A1), %d struck unread, %d carried by number; %d rows with (A1), (A2), (B), (C), [60R] and [66R]; %d README commits over 21 kernels, %d descriptions read back, %d PLACE-papers items (relay data/b737_sitting.txt, data/b737_author_words.txt).' % (
                 f['sit_n'], f['sit_p'], f['sit_r'], f['sit_s'], f['sit_c'], f['sit_rows'], f['sit_kc'], f['sit_desc'], f['sit_pp']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b737_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b737_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b737_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b737 `%s` (previous `%s`, b736’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b737_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b737_standing_v1160.txt); the standing '
             'report tool (relay data/b737_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** README.md alone on the 21 kernels’ mains, no Lean file and no main’s code, no tag; push-b737-sitting left local on each; zq-b730 of SIDE-explicit-formula unmoved at %s; %d dispatches; the %s branches as b736 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b737_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b736’s %s, %s, %s, %s (relay data/b737_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b737_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b736():
    """b736's trail record over b736's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b736 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b736`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R347)(5): relay push-b736-closing, push-b736-preroot, push-b736-record; PLACE-papers push-b736-preroot, push-b736-record; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: README.md alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R347) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (e28e6ed9) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R347)(3): FINDINGS :12911.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R347)(3): row (56).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-OFFLINE-ZERO entered by (R347)(4)(C)`s own commit, W-ORD-ZQ-DERIVES discharged by its own.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b737_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.16.0`s controls, the sitting`s bank, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the agenda committed at b732, its md5 read here.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: the agenda registers no figure; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: the agenda precedes the sitting`s bank by (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none, N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R347)(3): tools/standing/ to v1.16.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b737_address_scan.txt (the address never printed).'),
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
    # ### (R347)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b737_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b737_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1160', 'sitting', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b737_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b737_registration_%s.txt -- b737, THE SECOND SITTING: b736 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.16.0; W-ORD-ZQ-DERIVES DISCHARGED; THE AGENDA OF 111 ITEMS BY THE AUTHOR`S NUMBER; "
                             "NO DEPOSIT, NO TAG, UNDER (R347)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b736's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b737: b736's lines read banks this
act does not write, and are not carried; the lines are b737's: the discharge (KERNEL), tools/standing/ v1.16.0 by its controls (CERTIFIED), the sitting
(REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b737's lines, each from the record tool's figures over b737's banks
    # ------------------------------------------------------------------ KERNEL: (R347)(2), the discharge
    sz = seat('%s_discharge.txt' % ACT, '**W-ORD-ZQ-DERIVES DISCHARGED')
    sk = sz   # ### (R346)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- W-ORD-ZQ-DERIVES DISCHARGED on the three premise-free forms at Main.lean :194, :198, :205 on zq-b730 at %s, run %s, the landed lines INTERFACES; no Lean file this act. SOURCE %s.' % (K.ZQ_TIP[:8], K.ZQ_RUN, sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.16.0 ((R347)(3)), by its controls
    sw = seat('%s_standing_v1160.txt' % ACT, '**v1.16.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.16.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the sitting, read from its bank
    so = seat('%s_sitting.txt' % ACT, '**THE SITTING: ')
    keys['ORD'] = ('REGISTERED -- THE SITTING: of %d items %d passed, %d replaced, %d struck, %d carried, each on the author`s word; the agenda committed at b732, md5 %s. SOURCE %s.' % (f['sit_n'], f['sit_p'], f['sit_r'], f['sit_s'], f['sit_c'], K.PLAN_MD5[:8], so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R347)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b737 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
