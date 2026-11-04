# -*- coding: utf-8 -*-
# b740 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R350)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R350)(2) repair it carries. Edited by the Edit tool. Carried at b740 by tools/b740_fold.py (`carry`) from tools/acts/b739.py,
# b739`s names substituted; the citation`s sections adopted from tools/b740_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b739`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b739`s carried till
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
# ### b740, Component 1 (the Edit tool): THE c1 ROUTE FOR b739'S WEIGHT LINE AND ITS CORRIGENDUM, (R350)(1)-(2). Carried from b739's
# ### override and rewritten here against b739's own banks: the closing's lines by needle, the events (3), the defects (21), the refusals
# ### (9), the v1.20.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = 'c961e9d7'          # ### b739's closing commit
C1_REFUSAL_AT = 'c961e9d7'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-04'
C1_CORRIGENDA_LAST = 59
C1_V170 = 'b740_standing_v1200.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-04 by b740 to b739’s entry (:%d), under `(R350)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The Tier 3 act for [104]-[108]: '
C1_TRAIL_NEEDLE = '### b739 — lane two, act one hundred and sixty-six, the Tier 3 act under (R349)'
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
    for l in _c1_rd('b739_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b739_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b739_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b739_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b739_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b739_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b739_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b739_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8 or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b739_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b739_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b739_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    gr, l_gr = _c1_fl('b739_tier3.txt', r'^### ### \*\*TIER 3: (\d+) OF FIVE NOTES WRITTEN AND READ BACK ; STOPPED (\w+) ; NOT RUN (\d+) ; (NO NEW VERSION, NO FILE, NO OTHER FIELD)\.\*\*$', 'the Tier 3 grade')
    _am, l_am = _c1_fl('b739_tier3.txt', r'^  (APPENDED, ON THE AUTHOR`S WORD) \(data/b739_amendments\.json rows 1-2\)', 'the [108] amendment')
    (va, vb), l_v = _c1_fl('b739_standing_v1190.txt', r'^### ### \*\*v1\.19\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*$', 'the v1.19.0 foot')
    (vac,), l_vac = _c1_fl('b739_arms_prerun.txt', r"^  ### ### \*\*VACUOUS, THE PLANT MUTATED NOTHING, COUNTED NEITHER PASSING NOR FAILING : 1 \['(G-[A-Z-]+)'\]\.\*\*$", 'the vacuous arm')
    _mv, l_mv = _c1_fl('b739_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'(mirror-refresh-2026-11-04-b739)\.zip ; ', 'the mirror`s archive')
    (n3r,), l_n3 = _c1_fl(c, r'^    \(N1\) HELD \(N2\) HELD \(N3\) (REFUTED) \(N4\) HELD \(N5\) HELD ;', 'the record-time scores')
    _aw, l_aw = _c1_fl('b739_author_answers.txt', r'="(Land as composed) \(Recommended\)"', 'the author`s answer')
    _nx, l_nx = _c1_fl('b739_author_answers.txt', r'="(S5c-S5d in the tree) \(Recommended\)"', 'the next act')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != [1, 2, 3] or len(dr) != 21:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b739 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b739_closing.txt):* “%s” (data/b739_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b739_steps.json, the record and closing rows). As its rows read: the Tier 3 act for [104]-[108] (relay data/b739_tier3.txt :%d): '
            '%s of five currency notes written to Zenodo records 19938009, 19938005, 19938003, 19931797 and 21520474, each read back anonymously, stopped %s, not run %s, %s; '
            '[108] by the author’s amendment, sentences (4) and (5) appended after b727’s [18] note (:%d, data/b739_amendments.json rows 1-2). '
            'Standing tools v1.19.0, %s of %s (data/b739_standing_v1190.txt :%d); the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), '
            'G-AXIOM-CLAIM and G-PUBLISH-UNCALLED declared on the face, G-ENTRY-TITLE-FORM failing on its own first needle (events (3)), the one arm more %s VACUOUS at the plant run, counted neither passing nor failing (data/b739_arms_prerun.txt :%d); SCORES %d OF 8 HELD, as the author accepted at the root (“%s”, data/b739_author_answers.txt :%d); '
            'the closing’s score line prints N3 %s (:%d), the reading at the record before the root prompt was banked, where the scores bank read at the close holds N3 HELD (data/b739_scores_close.json). '
            'The root %s over %s banks, chained from %s (data/b739_act_root.json; :%d); '
            'the mirror %s at %s (data/b739_mirror_verify.txt :%d; :%d); %s prompts banked as put by the seat (:%d); the author’s word at the root: b740 is “%s” (data/b739_author_answers.txt :%d); '
            '%d events in data/b739_events.txt, rows (1)-(%d); %d defects, (a)–(u) '
            '(data/b739_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d, the ruling’s figure. '
            'The draft at v5; nothing deposited, no new Zenodo version; the corrigendum for these rows follows, under `(R350)`(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, l_gr, gr[0], gr[1].lower(), gr[2], gr[3].lower(), l_am,
                vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, vac, l_vac,
                len(held), _aw[0], l_aw, n3r, l_n3,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, _nx[0], l_nx, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b739's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '05:49:30Z', 'defect (a)'), (2, 'READ', '06:03:22Z', 'defect (g)'), (3, 'READ', '06:14:39Z', 'defect (h)'), (4, 'ENV', '06:21:26Z', 'defect (i)'),
               (5, 'READ', '06:52:09Z', 'defect (m)'), (6, 'PIPE', '07:49:24Z', 'defect (n)'), (7, 'REDIR', '08:09:06Z', 'defect (s)'), (8, 'SUBJECT', '10:04:30Z', 'event (1)'),
               (9, 'ENV', '10:29:07Z', 'event (2)')]
C1_UNROWED = []
C1_CORR_TITLE = ('## Corrigendum to b739’s record (relay data/b739_events.txt rows (1)-(3) and data/b739_defects.txt): three events and twenty-one defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the arm that could not pass at its head; the composer the one route to a seal or lock subject, the shell assignment, the deposit route read by its state, the miss with the check clean, '
                 'at tools/standing/ v1.20.0, each controlled, under (R350)(2)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.20.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b739_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if at[:5] not in src and at not in src and ('REFUSED BY THE HOOK (%s' % kind) not in src and 'refused by the hook' not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b739_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.20.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(3)', sorted(ev) == [1, 2, 3]), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 21', len(dr) == 21), ('the refusals 9, each answered as listed', len(rl) == 9 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.20.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.20.0
C1_EV_EXTRA = {1: '; repair (subjects); rule (2) of data/b740_rules.txt', 2: '; repair (assign); rule (3) of data/b740_rules.txt, REPEAT, the class met again at b740 step zero (f)',
               3: '; repair (needles); rule (1) of data/b740_rules.txt, the arm that could not pass'}
C1_DF_EXTRA = {'i': '; repair (assign); rule (3) of data/b740_rules.txt, the class (R350)(2)(iii) names', 'q': '; repair (publish); rule (4) of data/b740_rules.txt, METADATA EDIT, NO NEW VERSION by name'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b740, to the counter (`(R350)`(1)): “CLAIM 6, CLOSE 18, REPEAT 17 OF 24” is relay data/b739_closing.txt :5, over the three events and the twenty-one defects together; over the defects alone the tags give CLAIM 6, CLOSE 15, REPEAT 14 of 21, the ruling’s figure. Both read from the same tags; this entry prints both and edits neither.',
            'Dated note, b740, to b739’s score line: relay data/b739_closing.txt :139 and the trail’s score line (OPEN_TRAILS :17550) print N3 REFUTED, the reading at the record, when the root prompt was not yet banked; the scores bank read at the close (data/b739_scores_close.json) holds 8 of 8 HELD, and the closing’s head line its “scores 8 of 8 HELD”. The class of b738’s closing :137; both are b739’s; neither is edited.',
            'Dated note, b740, to b739’s worklist: tools/b738_worklist.py and tools/b739_worklist.py carried TRAIL_ORDERS 17410, TRAIL_RESOLVED 17442 and TRAIL_RETIRED 17428, b737’s trail lines, under each act’s own names; b740’s worklist reads b739’s (17516, 17546, 17532). No closing figure of b739 read those three names; none is edited.',
            'Dated note, b740, to b739’s citation check (`(R350)`(2)(v)): its one miss (data/b739_citation_check.txt :104) is the ruling’s quoted word “pass 19938009, 19938005, 19938003, 19931797, 21520474 as banked”, found as worded in no bank; the check stayed CLEAN because CLEAN counts halts alone (Lean paths, typed nouns, comparatives, :105 “halts 0”), and the miss was entered by the fact clause before the component citing it ran (data/b739_stepzero.txt :15-:17), the passes it stands for banked at b736. b739’s events bank carries no row for it; this note is its row.')
C1_CLASSES = (
    ('needles', 'the arm that could not pass (`(R350)`(2)(i), events (3); CLOSE ; REPEAT of b727 events (14))', 'rule (1) of data/b740_rules.txt; G-ENTRY-TITLE-FORM folded the title’s opening article and searched for its needles unfolded, so “## The Tier 3 act for [104]-[108]: ” could not stand in the folded title; tools/standing/armnorm.py folds needle and target alike, names every needle the fold would change as CANNOT PASS before the lock, and runs the act’s needles against its composed title at the pre-lock dry. b739’s entry replayed: FAIL before, PASS after; its old phrase CANNOT PASS; b740’s needles CANNOT PASS NONE'),
    ('subjects', 'the seal subject typed with the previous act’s count (`(R350)`(2)(ii), events (1); CLOSE ; REPEAT of b738 events (4))', 'rule (2) of data/b740_rules.txt; v1.19.0 read the count and not the typing: b739’s “85 files” was refused for its 85, and the same words with 83 would have run. tools/standing/subjects.py now refuses any seal or lock subject not opening with the composer’s words read from the bank, kind SUBJECT at the hook. Replayed: the typed 83 ran before and is refused after; b739’s composed subject c1776793 passes'),
    ('assign', 'the shell assignment at the pre-root push (`(R350)`(2)(iii), events (2); CLOSE ; REPEAT of b739 (i))', 'rule (3) of data/b740_rules.txt; row (20); the hook’s ENV kind refused it as it refused b739 (i); every ENV refusal of b739 and b740 printed by instance, three, each nothing run, the third b740’s own at step zero (defect (f)); b739 events (2)’s command judged ENV now. No route changed: the rule held, the seat broke it'),
    ('publish', 'G-PUBLISH-UNCALLED declared on the face for a Tier 3 act (`(R350)`(2)(iv), (R338)’s “publish not called” repair)', 'rule (4) of data/b740_rules.txt; from b728 the clause read “metadata edits on published records are permitted where a ruling names them by record” and the arm still read the word; tools/standing/publishstate.py reads each tool as UNCALLED, METADATA EDIT, NO NEW VERSION or PUBLISH, and the arm passes on the first two by name. b739’s and b727’s deposit-route tools: FAIL before, METADATA EDIT, NO NEW VERSION after; b733’s UNCALLED; a planted new version and a planted publish with no edit PUBLISH'),
    ('miss', 'the citation check’s one miss with the check clean (`(R350)`(2)(v), data/b739_citation_check.txt :104)', 'rule (5) of data/b740_rules.txt; the miss named with why the check stayed clean, in the dated note below. A guard: no failing side'),
    ('version', 'the version (`(R350)`(2)(vi))', 'rule (6) of data/b740_rules.txt; tools/standing/VERSION v1.20.0, landed by a commit of its own (63424433) with its controls bank'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b739’s events bank (relay data/b739_events.txt) carries three rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-one lettered rows, (a)-(u), each tagged in its own bracket (%s); its refusal bank nine lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R350)`(2), at tools/standing/ v1.20.0, each with a control on b739’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b739’s events (1)-(3):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( put and \d\d:\d\dZ answered)?( from [^:]*)?|post-push|pre-push and post-push)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b739_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b739’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b739_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b739’s refusals** (relay data/b739_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (three events, twenty-one defects), as b739’s closing prints it (relay data/b739_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims) or 'none'), '',
          '*Filed at b740 on the author’s ruling `(R350)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b740.py) from '
          'b739’s events and defects banks read unedited, its refusal bank, and the v1.20.0 controls bank; banked as relay `data/b740_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b739’s record; no sealed tool, face, trail or root-named bank of b739 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b740 -- THE CORRIGENDUM FOR b739, (R350)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b739_events.txt rows (1)-(3), data/b739_defects.txt 21 rows, data/b739_hook_refusals.txt 9 '
             'lines at %s; data/%s (the v1.20.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 3, DEFECTS 21 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.20.0: THE ARM THAT COULD NOT PASS, THE COMPOSER THE ONE ROUTE TO A SEAL OR LOCK SUBJECT, '
               'THE SHELL ASSIGNMENT, THE DEPOSIT ROUTE BY ITS STATE, THE MISS WITH THE CHECK CLEAN, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b739 at its weight after its entry, and the corrigendum for b739, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.20.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b740, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b740 ran three
# ### ((R350)(4)(iii)-(iv), N1), rowed in data/b740_dispatch_rows.json. Replaced for b740 alone; the arms' names stand, their plants on b740's rows.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R349)(7), as b739 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R350)(3)(d), N1, b740 (b738's form): twelve dispatches allowed, three made; each dispatch row carrying free_mb, its run id the
    worklist's in order, read once after it by that id; the plant a dispatch row with no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    return len(ds) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 12 and [r.get('run') for r in ds] == list(K.EF_RUNS) \
        and all(isinstance(r.get('free_mb'), int) for r in ds + rs) \
        and all(sum(1 for x in rs if str(x.get('run')) == str(d.get('run'))) == 1
                and rows.index(d) < next(i for i, x in enumerate(rows) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) for d in ds)
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b740: each dispatch read once after it by its run id (three this act)
#⟪END⟫
# ### b740, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R350)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b739, naming tools/standing/hook.py, unedited this act (its last commit b739`s 3c92170b; its blob at v1.20.0`s 63424433 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b740, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b739's record has twelve
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 4)) \
#⟪END⟫
# ### b740, Component 4 (the Edit tool): b740's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b739's override of checks 526 -- no registration commit -- removed: b740
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b740_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b740, Component 6 (the Edit tool): b740's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b739's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b740, Component 4 (the Edit tool): b739's overrides of checks 1516 and 1659 (hook.py edited by b739's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b740 as it stands
# ### b740, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b740_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b740, Component 4 (the Edit tool): b739's override of checks 1476-1482 (one ERRATA entry at b739's (R349)(5)) removed -- (R350)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b740 as it stands
# ### b740, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b739's step-zero wording; b740's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b740, Component 4 (the Edit tool): G-RUNNER-READ's plant on b740's dispatch rows -- run 2's axiom lines carrying sorryAx (b739's
# ### plant read the lv rows' closure log, which b740 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='planted', run=1)))),
#⟪END⟫
# ### b740, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b740, Component 6 (the Edit tool): the fold bank was b739's own route
# ### (tools/b739_fold.py); b740's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b740_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b739.py -> tools/acts/b740.py' in (rd('b740_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b740, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b740_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b740, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b740_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b740_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b740, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R350): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    rows = [l for n_ in ('b740_defects.txt', 'b740_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R350) Component 5, the act`s events and defects together; relay data/b740_defects.txt, data/b740_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b739, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b740 (defect (d')): the order's
# ### state as b740 leaves it -- the carry from b739 said "as b739 left it ... not touched this act", where b740 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-OFFLINE-ZERO open at SP2, S5c-S5d built this act to (d8) zqFn_centre_le, SP3 NOT REACHED at (c7) lamM_centre_encl,',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b740, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b739's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b740, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b739's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b740_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b740_registration_%s.txt' % __import__('b740_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b740, Component 4 (the Edit tool, before the face): b739's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b740, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b740's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b740, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R350)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b740 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b740_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b740: the build's one route
#⟪END⟫
# ### b740, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b739's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b740 scorer reads; the needles set to the banks b740's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b740, (R350)(2)(iii): b739's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b740, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b740_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrstuvwxyz')))   # ### (a)-(z) as entered before the lock, every one the seat's (data/b740_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b740_corrigendum.txt', 'data/b740_standing_v1200.txt', 'data/b740_rules.txt', 'data/b740_s5cd_statements.txt', 'data/b740_offlinezero.txt',
                  'data/b740_offlinezero_notes.txt', 'data/b740_dispatch_rows.json', 'data/b740_pathrefusal.txt',
                  'data/b740_reproduce.txt', 'data/b740_reproduce.json', 'data/b740_address_scan.txt', 'data/b740_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b740 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R350)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b740_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R350)(4): the sitting bank's rows by number -- a row opens `[n] STATE` at column 0, its fields indented two spaces as `KEY: value`;
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
        # ### (R350)(2)-(4) (b740's keys over b740's objects): the order by time and ancestry; v1.20.0's controls; the statements read as
        # ### committed; the build bank and its notes; zq-b730; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.C2_RELAY, K.STATEMENTS_BANK))) or None, _s(blob(ROOT, 'HEAD:' + K.STATEMENTS_BANK)) or None),   # ### the statements at Component 2's commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_build', K.C1_CORR, K.C2_RELAY),
                                 ('stmt_build', K.C2_RELAY, K.C3_RELAY[0]))),
        v1130=rd('b740_standing_v1200.txt'), plan=rd('b737_offlinezero_plan.txt'), print_=rd('b740_offlinezero.txt'), rows_bank=rd('b740_s5cd_statements.txt'),
        notes=rd('b740_offlinezero_notes.txt'),
        plan_first_files=files_of(ROOT, K.C2_RELAY), plan_files=files_of(ROOT, K.C3_RELAY[0]), price_files=(),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..%s' % (K.ZQ_ENTERING, K.ZQ_TIP)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--contains', K.ZQ_FIRST).split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b740_dispatch_rows.json') or '[]'), reproduce=rd('b740_reproduce.txt'), reproducej=jl('b740_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b740_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b739 left them
        rebuild=None, rebuild_rows=json.loads(rd('b740_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.C2_RELAY), zq_first=_ct(EF, K.ZQ_FIRST),
               zq_tip=_ct(EF, K.ZQ_TIP), sitting=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.C2_RELAY), sitting=files_of(ROOT, K.C3_RELAY[0]), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b740's read-first bank's items by path, as its step zero wrote them (data/b740_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b739_closing.txt |', 'relay data/b739_events.txt |', 'relay data/b739_citation_check.txt |', 'relay data/b727_events.txt |',
                     'relay data/b737_offlinezero_plan.txt |', 'relay data/b738_offlinezero.txt |', 'relay data/b738_offlinezero_notes.txt |', 'relay data/b731_price_measured.txt |',
                     'SIDE-explicit-formula zq-b730 at 602cd401 |', 'relay data/b739_defects.txt |', 'relay data/b739_checks.txt |', 'PLACE-papers FINDINGS.md :13281-:13351',
                     'relay tools/b740_worklist.py whole;')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R350)(1)-(2))', 'BUILD TO SP3 ((R350)(3))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (123 = 123 + 0, data/b740_citation_check.txt); the check CLEAN;
    the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 123 and '### ### **THE CHECK CLEAN**' in c \
#⟪END⟫
# ### b740, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b739's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b740, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b739()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b740_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b739's figures, read at FINDINGS :13387 as Component 1 landed them
    return landed(S, 0, ['b739 AT ITS WEIGHT', 'suite 112 of 116', 'relay a5b5f216', '21 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b740's title in the ferry's Component 4 form (the record tool's _title over the banks); the opening phrase lowercase after "## " as the
# ### ferry orders, read by tools/standing/armnorm.py cannot_pass before the lock ((R350)(2)(i))
TITLE_NEEDLES = ('## W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d in the tree: ', ' dispatches, ', ' lines against 482-2,675; the order OPEN at ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R350)(1)-(2): the generated entry for b739's three events and twenty-one defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(3), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 6, CLOSE 18 over 24, REPEAT 17); the repairs at tools/standing/ v1.20.0 by their controls
    bank; the corrigenda bank appended at row (60) and nothing before it changed; in Component 1's commits (the figures read from
    data/b740_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 21 and len(items) == j.get('items') == 24 and j.get('row') == 60 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 24 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 6 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 17 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.20.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 4 \
        and '  (60) ' in S['corrigenda'] and '  (61) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b740_rules.txt carries (R350)(2)'s six rules, in its own commit 744cb044; data/b741_rules.txt (by form in (R350)(4)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b739's form, its names b740's); no author's word of b740 orders a row of the next act's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and "(1) AN ARM'S SEARCH PHRASE IS READ UNDER THE NORMALISATION" in r1 and '(6) THE VERSION' in r1 and S['files']['rules'] == ['data/b740_rules.txt'] \
        and not os.path.exists(os.path.join(D, 'b741_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b740's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO S5c-S5d AT BOX A`S CENTRE', 'CERTIFIED -- tools/standing/ v1.20.0', 'REGISTERED -- THE ORDER OPEN AT',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b740: three dispatches of the twelve (R350)(3)(d) allows -- each dispatch command in the capture a row, each row carrying free_mb and
    read once after it by its run id; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = bool(seq_) and all(
        sum(1 for x in seq_ if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) == 1
        and seq_.index(d) < next(i for i, x in enumerate(seq_) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run')))
        for d in seq_ if d.get('kind') == 'dispatch')   # ### N1: each dispatch read once after it by its run id
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b740_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b740, N1: three rows, three dispatch commands
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
# ### b740's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The statements before any Lean**', '**The build to SP3**', '**The enclosure not built**',
                 '**The git writes**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b740_corrigendum.txt', 'data/b740_standing_v1200.txt', 'data/b740_s5cd_statements.txt', 'data/b740_offlinezero.txt', 'data/b740_offlinezero_notes.txt',
                 'data/b740_reproduce.txt', 'data/b740_address_scan.txt', 'data/b740_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b740: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R350)(3)(a), N2 (the name the frozen run list carries): the statements bank read as committed -- its blob at HEAD its blob at
    Component 2's commit a9c206b9, that commit carrying it and Component 3's not; its fifteen rows (c1)-(c7), (d1)-(d8), each with its route,
    its reason and its neighbour or ABSENT; the plan bank's md5 the step zero print's, printed in the build bank; v1.20.0's commit, the
    corrigendum's, the statements' and the build bank's in that order by time and by ancestry; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('standing', 'corr', 'plan', 'print')
    body_ = (reg or '').split('## SP3 AS THESE ROWS DEFINE IT')[0]
    rows_ = re.split(r'(?m)^(?=\([cd][1-8]\) (?:GENERAL|CENTRE)\b)', body_)[1:]
    ids_ = [r_[1:3] for r_ in rows_]
    return bool(reg) and reg == head and K.STATEMENTS_BANK in S['plan_first_files'] and K.STATEMENTS_BANK not in S['plan_files'] \
        and ids_ == ['c%d' % i for i in range(1, 8)] + ['d%d' % i for i in range(1, 9)] \
        and all('reason' in r_ and 'neighbour' in r_ for r_ in rows_) \
        and 'data/b737_offlinezero_plan.txt md5 %s ; step zero`s %s ; equal True' % (K.PLAN_MD5, K.PLAN_MD5) in (S['print_'] or '') \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b740_address_scan.py run live over every commit of the act (relay and
    PLACE-papers; fields, messages and added lines; zq-b730's three Lean commits scanned at each commit by the seat), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R350)(2)-(3), N2 (the name the frozen run list carries): (2) whole before (3) -- v1.20.0, the weight and corrigendum on PLACE-papers
    and the corrigendum banks before the statements bank; the statements before the first Lean commit on zq-b730 ((R350)(3)(a)); the last
    Lean commit before the build bank, by the commits' times; the corrigendum an ancestor of the statements, the statements of the build bank."""
    t_ = S['t']
    return all(t_.get(k_) for k_ in ('c1pp', 'c1', 'standing', 'plan', 'zq_first', 'zq_tip', 'print')) \
        and max(t_['standing'], t_['c1pp'], t_['c1']) < t_['plan'] < t_['zq_first'] <= t_['zq_tip'] < t_['print'] \
        and S['anc'].get('corr_build') is True and S['anc'].get('stmt_build') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R350)(3)(b)-(d), N1, N3 (the name the frozen run list carries): the build bank's dispatch table -- one row per dispatch, its run id
    the worklist's in order, each row's sha one of zq-b730's three commits and its free memory printed, each graded KERNEL or BREAKS, the
    last KERNEL; the lines measured per group and in all against 482-2,675 and the three-times rule; every built name of the statements on
    the standard three by the last KERNEL run, (c4) and (c7) NOT BUILT; the foot SP3 NOT REACHED at (c7), the order OPEN at SP2."""
    t = S['print_'] or ''
    rows = re.findall(r'^  (\d+) \| group (\S+)\s*\| (\w+) \| sha ([0-9a-f]{8}) \| run (\d+) \| free (\d+) MB \| (KERNEL|BREAKS),', t, re.M)
    v = _vlast(t)
    std = 'propext, Classical.choice, Quot.sound (run %d)' % K.EF_RUNS[-1]
    built = re.findall(r'^  S5[cd] \(([cd]\d)\) (\w+)\s+(.*)$', t, re.M)
    return bool(rows) and [int(r[4]) for r in rows] == list(K.EF_RUNS) and [int(r[0]) for r in rows] == list(range(1, len(K.EF_RUNS) + 1)) \
        and all(any(c.startswith(r[3]) for c in K.ZQ_COMMITS) for r in rows) and rows[-1][6] == 'KERNEL' \
        and 'S5c-S5d IN ALL: measured 578 ; the estimate 900-2500' in t and 'SP3`S RULE: three times the estimate, 7500 lines ; measured 578 ; within' in t \
        and len(built) == 15 and sorted(n_ for _r, n_, a_ in built if a_.startswith('NOT BUILT')) == ['incGamma1_add_one', 'lamM_centre_encl'] \
        and all(a_ == std for _r, _n, a_ in built if not a_.startswith('NOT BUILT')) \
        and v.startswith('SP3 NOT REACHED AT (c7) lamM_centre_encl ; DISPATCHES 3 OF 12 ; LINES 578') and v.endswith('THE ORDER OPEN AT SP2.')
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip
    locally and at origin; zq-b730's diff against its entering tip 602cd401 the two modules IncGamma and Elem and print_targets.txt alone,
    its three commits the worklist's in order; no tag and no other branch carrying the act's first Lean commit (no merge)."""
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
    arm list since b739's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R350)(3)(b)-(d), N3, N5 (the name the frozen run list carries): SP3's three-times rule kept and S6 not begun -- 578 lines within 7,500,
    no OffZero module beyond IncGamma and Elem among zq-b730's files and no S6 file; (c7)'s ABSENT route and the reason it is NOT BUILT in the
    notes; the price line in OPEN_TRAILS at :17400 unmoved; no sentence of the build bank, its notes or the statements a location of a zero or
    a failure stated as a theorem."""
    t = S['print_'] or ''
    n_ = S['notes'] or ''
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    sents = [s_ for t_ in (t, n_, S['rows_bank'] or '') for s_ in re.split(r'(?<=[.;:])\s+', t_)]
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    return 'SP3`S RULE: three times the estimate, 7500 lines ; measured 578 ; within' in t \
        and not [f_ for f_ in S['zq_files'] if f_ not in K.ZQ_FILES] and not [f_ for f_ in S['zq_files'] if 'S6' in f_ or '/Main' in f_] \
        and '(6) (c7) lamM_centre_encl is NOT BUILT' in n_ and 'the quadrature route is ABSENT in the statements bank' in n_ \
        and 'W-ORD-ZQ-OFFLINE-ZERO' in oline(S, K.PRICE_LINE) and not loc_


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
    """standing clauses v9 (Component 7 of (R350): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b740_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b739's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R350-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b739's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R350) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b739's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R349)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 3f45857d',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 123 = 123 OK + 0 misses, the check CLEAN; the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b739-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 form: W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d in the tree, SP3 graded, the dispatches and the lines against 482-2,675, the order OPEN at its SP, the arm control and the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R350)(1)-(2): the generated corrigendum for b739`s record, landed at FINDINGS :13389: its three events and twenty-one defects, 24 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 6 CLOSE 18, REPEAT 17; v1.20.0`s repairs by data/b740_standing_v1200.txt; the corrigenda bank appended at row (60)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b740_rules.txt carrying (R350)(2)`s rules in its own commit 744cb044, no data/b741_rules.txt',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b740's objects
    ('G-REGISTRATIONS-FIRST', '(R350)(3)(a), N2: the statements bank read as committed, its blob at HEAD its blob at a9c206b9, fifteen rows (c1)-(c7), (d1)-(d8) each with its reason and neighbour; the plan`s md5 the step zero print`s in the build bank; v1.20.0`s, the corrigendum`s, the statements` and the build bank`s commits in that order by time and ancestry; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(stmt_build=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b740_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R350)(2)-(3), N2: (2) whole before (3) -- v1.20.0, the weight and corrigendum and their banks before the statements; the statements before the first Lean commit; the last Lean commit before the build bank, by time; the corrigendum an ancestor of the statements, the statements of the build bank',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_build=False))),
    ('G-DERIVATION-GRADED', '(R350)(3)(b)-(d), N1, N3: the build bank`s dispatch table -- the worklist`s three runs in order, each sha a zq-b730 commit, free memory printed, KERNEL or BREAKS, the last KERNEL; 578 lines against 482-2,675 within 7,500; every built name on the standard three, (c4) and (c7) NOT BUILT; the foot SP3 NOT REACHED at (c7), OPEN at SP2',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'print_', (S['print_'] or '').replace('| run 41859346843 |', '| run 41859346844 |'))),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against 602cd401 IncGamma, Elem and print_targets.txt alone, its three commits the worklist`s; no tag and no other branch carrying them',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 3f45857d, VERSION 9; v8 at HEAD its blob at 3f45857d; no v10; v9`s commit an ancestor of v1.20.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R350)(3)(b)-(d), N3, N5: SP3`s three-times rule kept (578 within 7,500) and S6 not begun, no OffZero module beyond IncGamma and Elem; (c7)`s ABSENT route and its NOT BUILT reason in the notes; the price line at OPEN_TRAILS :17400; no sentence a location',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'notes', (S['notes'] or '') + NL + '(10) A zero is located in Lean at the centre.')),
    ('G-DIFFERS-ERRATA', '(R350): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 454f2167, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b740_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R350-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b739`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 3f45857d (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: twelve dispatches allowed by (R350)(3)(d), three made, each row carrying free_mb, each read after it by its run id, the worklist`s runs in order; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: three dispatch commands in the capture, three rows, each read after it by its run id, each carrying free_mb; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b739 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0; zq-b730`s three commits read at G-OFFSET-POST-HOC',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers, FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b739`s trail record on OPEN_TRAILS (:17508) and its root in the chain', lambda S: '### b739 — lane two, act one hundred and sixty-six, the Tier 3 act under (R349)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers, FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b739`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: three of the twelve; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b740 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b739's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b740: (R350)'s rows, set at step zero by the Edit route (scratch splice740.py). (1)'s line read by the ruling from the public relay at c961e9d7
    pub = _blob('D:/relay', 'c961e9d7', 'data/b739_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b739_closing.txt :1, the head line as the public relay carries it at c961e9d7', bool(pub) and pub[0] == at(cl, 1) and 'relay a5b5f216' in pub[0] and 'PLACE-papers 5b89b86' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root 407e3f98c4ae10e8', '4 prompts answered', 'scores 8 of 8 HELD', '21 defects'):
        add('ruling (1)', 'data/b739_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    dfl_ = [l for l in lines_of(p('data', 'b739_defects.txt')) if re.match(r"^    \([a-z]'?\) ", l)]
    tg_ = (sum(1 for l in dfl_ if '[CLAIM' in l), sum(1 for l in dfl_ if '[CLOSE' in l), sum(1 for l in dfl_ if '; REPEAT' in l), len(dfl_))
    add('ruling (1)', 'the counter CLAIM 6, CLOSE 15, REPEAT 14 of 21: data/b739_defects.txt`s 21 lettered defects, their tags', tg_ == (6, 15, 14, 21), 'CLAIM %d CLOSE %d REPEAT %d OF %d' % tg_, '1')
    add('ruling (1)', 'data/b739_closing.txt :5, the closing`s counter over events and defects together, CLAIM 6, CLOSE 18, REPEAT 17 OF 24 (the 21 defects and events (1)-(3), each CLOSE ; REPEAT)',
        'CLAIM 6, CLOSE 18, REPEAT 17 OF 24' in at(cl, 5), at(cl, 5)[-40:], '1')
    t3_ = lines_of(p('data', 'b739_tier3.txt'))
    add('ruling (1)', 'data/b739_tier3.txt :53, five of five written and read back, no new version, no file, no other field',
        'TIER 3: 5 OF FIVE NOTES WRITTEN AND READ BACK' in at(t3_, 53) and 'NO NEW VERSION, NO FILE, NO OTHER FIELD' in at(t3_, 53), at(t3_, 53)[:60], '1')
    add('ruling (1)', 'data/b739_tier3.txt :46, [108]`s sentences (4)-(5) appended on the author`s word, the amendment rows data/b739_amendments.json',
        'APPENDED, ON THE AUTHOR`S WORD (data/b739_amendments.json rows 1-2)' in at(t3_, 46) and bool(_jl('b739_amendments.json')), at(t3_, 46)[:60], '1')
    sv_ = lines_of(p('data', 'b739_standing_v1190.txt'))
    add('ruling (1)', 'data/b739_standing_v1190.txt :105, v1.19.0, 17 cases, 17 as wanted', 'CASES 17 ; AS WANTED 17' in at(sv_, 105), at(sv_, 105)[:60], '1')
    ck_ = lines_of(p('data', 'b739_checks.txt'))
    add('ruling (1)', 'data/b739_checks.txt :16, 116 run, 112 passing, failing G-AXIOM-CLAIM, G-PUBLISH-UNCALLED, G-ENTRY-TITLE-FORM',
        "ARMS RUN : 116. ### LIVE PASSING : 112. ### LIVE FAILING : 3 ['G-AXIOM-CLAIM', 'G-PUBLISH-UNCALLED', 'G-ENTRY-TITLE-FORM']" in at(ck_, 16), at(ck_, 16)[:60], '1')
    add('ruling (1)', 'data/b739_checks.txt :18, G-RUNNER-GATE VACUOUS', "VACUOUS, THE PLANT MUTATED NOTHING, COUNTED NEITHER PASSING NOR FAILING : 1 ['G-RUNNER-GATE']" in at(ck_, 18), at(ck_, 18)[:60], '1')
    sc9_ = _jl('b739_scores_close.json')
    held_ = sorted(k_ for k_, v_ in sc9_.items() if v_[:1] == ['HELD'])
    add('ruling (1)', 'data/b739_scores_close.json, 8 of 8 HELD', len(held_) == 8, 'HELD %s' % ' '.join(held_), '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar9_ = [x for x in ar_ if x[:1] == ['b739']]
    add('ruling (1)', 'data/act_roots.txt, b739`s root 407e3f98 chained from b738`s f28b18c1', len(ar9_) == 1 and ar9_[0][1].startswith('407e3f98') and ar9_[0][2].startswith('f28b18c1'), ' '.join(x_[:8] for x_ in (ar9_[0] if ar9_ else [])), '1')
    add('ruling (1)', 'data/b739_closing.txt :125, the root over 105 banks', 'BANKS 105 ; CLEAN AND EQUAL AT HEAD 105' in at(cl, 125), at(cl, 125)[:60], '1')
    b3_ = rd(p('data', 'b739_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE through b739 (b739`s post-push part b3)', 'b739 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b739 AGREE' if 'b739 AGREE' in b3_ else 'ABSENT', '1')
    for q_ in ('a1', 'a2', 'c', 'b1', 'b2a', 'b2b', 'b2c', 'b2d'):
        t_ = rd(p('data', 'b739_checks_postpush_standing-%s.txt' % q_)) or ''
        add('ruling (1)', 'b739`s post-push part %s, no DISAGREE (the chain b624-b739)' % q_, bool(t_) and 'DISAGREE' not in t_, 'present' if t_ else 'ABSENT', '1')
    add('ruling (1)', 'data/b739_closing.txt :127, the mirror mirror-refresh-2026-11-04-b739 CLEAN', 'mirror-refresh-2026-11-04-b739.zip' in at(cl, 127) and 'CLEAN ON ALL THREE CLAUSES' in at(cl, 127), at(cl, 127)[:60], '1')
    aa9_ = lines_of(p('data', 'b739_author_answers.txt'))
    add('ruling (1), (head)', 'data/b739_author_answers.txt :29, the next act "S5c-S5d in the tree"', '="S5c-S5d in the tree (Recommended)"' in at(aa9_, 29), at(aa9_, 29)[:50], '1')
    add('ruling (1), (5)', 'data/b739_closing.txt :308, the draft held at v5 unpublished', 'the draft held at v5 unpublished' in at(cl, 308), at(cl, 308)[:60], '1')
    v0_ = _blob('D:/relay', K.C1_STANDING + '^', 'tools/standing/VERSION').strip()   # ### entering the act: v1.20.0's commit's parent (the live file moved at C1_STANDING)
    add('ruling (1)', 'tools/standing/VERSION v1.19.0 entering the act', v0_ == 'v1.19.0', v0_, '1')
    # ### (R350)(2): the corrigendum's sources
    cc9_ = lines_of(p('data', 'b739_citation_check.txt'))
    add('ruling (2)(v)', 'data/b739_citation_check.txt :104, 91 cites, 90 OK, 1 miss; :105 THE CHECK CLEAN',
        'CITES CHECKED 91 ; OK 90 ; MISSES 1' in at(cc9_, 104) and 'THE CHECK CLEAN' in at(cc9_, 105), at(cc9_, 104)[:60], '1')
    e27_ = (rd(p('data', 'b727_events.txt')) or '').split(NL)
    add('ruling (2)(i), ferry (read first)', 'data/b727_events.txt (14), G-ENTRY-TITLE-FORM failing on its first needle', any(l.startswith('    (14) ') and 'G-ENTRY-TITLE-FORM' in l for l in e27_), 'read', '1')
    # ### (R350)(3): the plan and b738's build bank as committed, md5s printed; their rows
    import hashlib as _hl
    for f_, m_ in ((K.PLAN_BANK, K.PLAN_MD5), (K.PREV_BUILD_BANK, K.PREV_BUILD_MD5)):
        b_ = open(p(*f_.split('/')), 'rb').read() if os.path.exists(p(*f_.split('/'))) else b''
        add('ruling (3)', '%s as committed, md5 %s' % (f_, m_), _hl.md5(b_).hexdigest() == m_ and not gr('D:/relay', 'status', '--porcelain', '--', f_), 'md5 %s' % _hl.md5(b_).hexdigest(), '2')
    pl_ = lines_of(p('data', 'b737_offlinezero_plan.txt'))
    for n_, w_ in ((91, 'S5c each term`s integral'.replace('`', "'")), (93, 'S5d the elementary values'), (96, 'S6  P'), (120, 'THE MATHLIB OBJECTS ABSENT AT THE PIN'),
                   (136, 'SP3 after S5c-S5d at the centre alone'), (142, 'The order')):
        add('ruling (3), ferry (read first)', 'data/b737_offlinezero_plan.txt :%d, %s' % (n_, w_), w_ in at(pl_, n_), at(pl_, n_)[:60], '2')
    ob_ = lines_of(p('data', 'b738_offlinezero.txt'))
    add('ruling (3), ferry (read first)', 'data/b738_offlinezero.txt :80, the grade line: SP1 and SP2 REACHED, 11 of 12 dispatches, the order open at SP2',
        all(w_ in at(ob_, 80) for w_ in ('SP1 REACHED ; SP2 REACHED ; DISPATCHES 11 OF 12', 'THE ORDER OPEN AT SP2')), at(ob_, 80)[:60], '2')
    add('ruling (3)(b)', 'data/b738_offlinezero.txt :77, S5c-S5d re-priced at 482-2675 lines by the measured ratio', '482-2675 lines' in at(ob_, 77), at(ob_, 77)[:60], '2')
    add('ferry (read first)', 'data/b738_offlinezero.txt :70-:71, zq_Λ₀_split, lamM_eq, zq_thetaC_tail, thetaTr', 'zq_Λ₀_split' in at(ob_, 70) and 'lamM_eq' in at(ob_, 70) and 'zq_thetaC_tail' in at(ob_, 71) and 'thetaTr' in at(ob_, 71),
        at(ob_, 71)[:60], '2')
    on_ = lines_of(p('data', 'b738_offlinezero_notes.txt'))
    add('ferry (read first)', 'data/b738_offlinezero_notes.txt :20, (5), the truncation built as the box |m|, |n| <= 14', at(on_, 20).strip().startswith('(5)') and '|m|, |n| <= 14' in at(on_, 20), at(on_, 20)[:60], '2')
    add('ferry (read first)', 'data/b731_price_measured.txt, I-10`s form', 'I-10`s form' in (rd(p('data', 'b731_price_measured.txt')) or ''), 'present', '2')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(3) and 21 defects (data/b739_events.txt, data/b739_defects.txt)',
        starts == [1, 2, 3] and len(letters) == 21, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b739_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    ev_ = (rd(p('data', 'b739_events.txt')) or '').split(NL)
    for n_, w_ in ((1, 'REFUSED BY THE HOOK (SUBJECT)'), (2, 'REFUSED BY THE HOOK (ENV)'), (3, 'G-ENTRY-TITLE-FORM fails LIVE')):
        add('ferry (read first), ruling (2)', 'data/b739_events.txt (%d), %s' % (n_, w_), any(l.startswith('    (%d) ' % n_) and w_ in l for l in ev_), 'read', '1')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (3)', 'zq-b730 at 602cd401, the tip b738 left, read back', zt_.startswith('602cd401') or zt_.startswith(K.ZQ_TIP[:8]), zt_[:8], '3')
    zf_ = gr(EF_, 'ls-tree', '-r', '--name-only', K.ZQ_ENTERING, '--', 'SIDEExplicitFormula/Schema/ZQ').split()
    for f_ in ('OffZero/Split.lean', 'OffZero/Tail.lean', 'OffZero/Box.lean', 'OffZero/Main.lean', 'Bound.lean', 'Theta.lean', 'FEPair.lean', 'Continuation.lean'):
        add('PATHS, ferry (read first)', 'SIDEExplicitFormula/Schema/ZQ/%s at zq-b730 602cd401, printed from the tree' % f_, 'SIDEExplicitFormula/Schema/ZQ/' + f_ in zf_, 'present' if 'SIDEExplicitFormula/Schema/ZQ/' + f_ in zf_ else 'ABSENT', '3')
    for f_, n_, w_ in (('OffZero/Split.lean', 31, 'theorem lamM_eq'), ('OffZero/Split.lean', 99, 'theorem zq_Λ₀_split'), ('Bound.lean', 319, 'theorem zq_three_halves_lt'),
                       ('Continuation.lean', 122, 'def zqFn'), ('OffZero/Box.lean', 31, 'def boxA'), ('Theta.lean', 20, 'def thetaU')):
        bl_ = _blob(EF_, K.ZQ_ENTERING, 'SIDEExplicitFormula/Schema/ZQ/' + f_).replace(chr(13), '').split(NL)
        add('ferry (read first)', 'SIDEExplicitFormula/Schema/ZQ/%s :%d, %s' % (f_, n_, w_), at(bl_, n_).startswith(w_), at(bl_, n_)[:60], '3')
    ta_ = _blob(EF_, K.ZQ_ENTERING, 'SIDEExplicitFormula/Schema/ZQ/OffZero/Tail.lean')
    for w_ in ('def thetaTr', 'theorem zq_thetaC_tail'):
        add('ferry (read first)', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Tail.lean carries %s' % w_, w_ in ta_, 'present' if w_ in ta_ else 'ABSENT', '3')
    ML_ = EF_ + '/.lake/packages/mathlib'
    mh_ = (gr(ML_, 'rev-parse', 'HEAD') or '').strip()
    add('PATHS', 'Mathlib at the pin de5ce8a9 (the kernel`s .lake/packages/mathlib)', mh_.startswith('de5ce8a9'), mh_[:8], '3')
    for f_, n_, w_ in (('Mathlib/Analysis/Complex/Exponential.lean', 517, 'nonrec theorem exp_bound {x : ℝ}'), ('Mathlib/Analysis/Complex/Exponential.lean', 377, 'theorem exp_bound {x : ℂ}'),
                       ('Mathlib/Analysis/Complex/Trigonometric.lean', 873, 'theorem cos_bound {x : ℝ}'), ('Mathlib/Analysis/Complex/Trigonometric.lean', 876, 'theorem sin_bound {x : ℝ}'),
                       ('Mathlib/Analysis/Complex/ExponentialBounds.lean', 71, 'theorem log_two_near_10'), ('Mathlib/Analysis/Real/Pi/Bounds.lean', 190, 'theorem pi_gt_d20'),
                       ('Mathlib/Analysis/Real/Pi/Bounds.lean', 206, 'theorem pi_lt_d20'), ('Mathlib/Analysis/SpecialFunctions/Gamma/Beta.lean', 398, 'theorem Gamma_mul_Gamma_one_sub (z : ℂ)'),
                       ('Mathlib/Analysis/SpecialFunctions/Gamma/Beta.lean', 559, 'theorem Gamma_mul_Gamma_add_half (s : ℂ)'), ('Mathlib/Analysis/SpecialFunctions/Gamma/Basic.lean', 356, 'theorem Gamma_conj'),
                       ('Mathlib/Analysis/SpecialFunctions/ImproperIntegrals.lean', 57, 'theorem integral_exp_neg_Ioi'), ('Mathlib/Analysis/SpecialFunctions/Pow/Real.lean', 337, 'theorem norm_cpow_eq_rpow_re_of_pos')):
        bl_ = _blob(ML_, 'HEAD', f_).replace(chr(13), '').split(NL)
        add('ferry (read first), PATHS', '%s :%d, %s, printed from the tree' % (f_, n_, w_), at(bl_, n_).startswith(w_), at(bl_, n_)[:60], '3')
    st_ = _blob(ML_, 'HEAD', 'Mathlib/Analysis/SpecialFunctions/Stirling.lean')
    add('ferry (read first)', 'Mathlib/Analysis/SpecialFunctions/Stirling.lean, the factorial`s Stirling (no complex Stirling with explicit error)', 'stirlingSeq' in st_, 'present, stirlingSeq' if 'stirlingSeq' in st_ else 'ABSENT', '3')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :13351, b739`s entry', at(fd_, 13351).startswith('## The Tier 3 act for [104]-[108]'), at(fd_, 13351)[:50], '0')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'OPEN_TRAILS :17508, b739`s trail record', at(ot_, 17508).startswith('### b739 '), at(ot_, 17508)[:50], '0')
    add('ferry (read first)', 'OPEN_TRAILS :17554-:17558, the trail`s hand section carrying the author`s word for b740', at(ot_, 17554).startswith('### b739 — the author') and '“S5c-S5d in the tree (Recommended)”' in at(ot_, 17558),
        at(ot_, 17558)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    SP6_ = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf/scratchpad'
    for z_ in ('zqwork', 'zqwork2', 'zqwork3'):
        add('PATHS, b739 closing (c)', 'the damaged clone %s in place in b736`s scratchpad, not deleted' % z_, os.path.isdir(SP6_ + '/' + z_), 'present' if os.path.isdir(SP6_ + '/' + z_) else 'ABSENT', '0')
    add('ferry', 'tools/standing/ at v1.19.0 entering the act (tools/standing/VERSION at v1.20.0`s commit`s parent)', _blob('D:/relay', K.C1_STANDING + '^', 'tools/standing/VERSION').strip() == 'v1.19.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R350)(4): b739's export, the mirror's last
    add('ruling (4)', '%s, b739`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R350)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b739-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R350)(2), (4): act_current alone, then b739's step row 19 and its closing capture, each committed alone; tools/mirror_prevbuild.json's
    # ### LF form equal to HEAD's (2d637131), nothing to commit (b739's build rewrote it with CRLF endings, its content unchanged)
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b739_steps.json'),
                   (K.STEPZERO, 'data/b739_relay_push-b739-closing_push_out.txt')):
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
    add('ferry (read first)', 'data/b740_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b740_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b740 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b739_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.20.0's controls, the build to SP3 with its statements, notes and dispatch rows, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R350)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R350)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: zq-b730 of SIDE-explicit-formula alone, three commits under (R350)(3); no main's code, no merge, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b740 ((R350)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R349)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b740 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY-SEVEN, THE NUMERICS ACT: b739 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE ARM THAT COULD NOT PASS; '
              'W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d STATED AND BUILT IN THE TREE AT THE CENTRE OF BOX A TO SP3, UNDER (R350).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b739's sections over b739's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.20.0: the arm that could not pass at the head, the composer the one route to a seal or lock subject, the shell assignment, the deposit route by its state, the miss with the check clean, the version, each case failing before its repair and passing after', 'b740_standing_v1200.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE BUILD TO SP3 ((R350)(3))', [
                ('the statements of S5c and S5d, each with its route, reason and neighbour or ABSENT, committed before any Lean file', 'b740_s5cd_statements.txt', r'(?m)^## SP3 AS THESE ROWS DEFINE IT.*'),
                ('W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d at the centre of box A: the dispatches, the lines against 482-2,675 and the three-times rule, the axioms of every row, the grade', 'b740_offlinezero.txt'),
                ('the notes beside the build bank, each with its reason', 'b740_offlinezero_notes.txt', r'(?m)^\(6\) \(c7\) lamM_centre_encl is NOT BUILT[^\n]*'),
                ('the probe-path refusal printed before the lock gate', 'b740_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b740_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b739`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b740_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R349)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; zq-b730 from ' + WL.ZQ_ENTERING[:8] + ' to ' + WL.ZQ_TIP[:8] + ', three commits, every Lean file of the act on it, off main, no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: of the twelve (R350)(3)(d) allows, each read by its run id) ; the rebuild-b721 branches of the wave 1 kernels as b739 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b739-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the plan bank`s md5 printed at step zero before any Lean file, the statements committed before any Lean file, the build bank`s controls before its figures, the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate ;',
    '    N3: SP3 graded NOT REACHED at (c7) with every built row`s axioms ; no sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem ; a value at one point is a value ; the entry`s nouns the banks` ; N5: S6 not begun ; one git write per message ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b740_address_scan.txt, data/b740_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads, the three workflow dispatches and their artifact downloads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo field touched ; the deposit route untouched, the draft held at v5 unpublished ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the price line, the trail) written ; no paper moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY or faces page byte ; data/act_roots.txt (b740`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.20.0 by (R350)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b739 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R350)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZQ-OFFLINE-ZERO OPEN at SP2 (relay data/b740_offlinezero.txt), SP3 NOT REACHED at (c7) lamM_centre_encl, its quadrature route ABSENT, (c4) not built, S6 not begun ; the wave 1 deposit ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b740_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b739 left them; push-b739-sitting on b739`s 21 kernels, local; the build clone D:/zq-b738.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on any kernel`s main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b739`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b740: the standing repairs are v1.20.0's ((R350)(2), relay data/b740_standing_v1200.txt, read in the corrigendum section); the
    # ### carry's diffs here (b740 carried at step zero before the fold; its tools since are the templates and tools/acts/b740.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, the act`s one written branch; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b739 left them; port-b707 at b712`s tip %s)' % (
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
    b740's form over b740's objects (b738's build form, in git at b738's record tool): the corrigendum's foot and v1.20.0's controls; the
    build bank's foot and its lines; the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which
    refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1200.txt' % ACT, r'\*\*v1\.20\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.20.0`s controls')
    bd = _bfig('%s_offlinezero.txt' % ACT, r'\*\*SP3 (REACHED|NOT REACHED AT \([cd]\d\) \w+|STOPPED BY THE THREE-TIMES RULE AT \d+ LINES) ; DISPATCHES (\d+) OF (\d+) ; LINES (\d+) AGAINST ([\d,]+-[\d,]+) '
               r'\(THE CEILING (\d+)\) ; ROWS COMPILED (\d+) OF (\d+), NAMES (\d+) OF (\d+) ; THE ORDER OPEN AT (SP\d)\.\*\*', 'the build bank`s foot')
    gl_ = re.findall(r'^  (S5[cd]) \S+ measured (\d+) ; the estimate (\d+-\d+) ;', rdn('%s_offlinezero.txt' % ACT), re.M)
    if len(gl_) != 2:
        sys.exit('### THE BUILD BANK CARRIES NOT TWO GROUP LINES -- NOTHING COMPOSED')
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
                bd_sp3g=bd[0], bd_disp=int(bd[1]), bd_max=int(bd[2]), bd_lines=int(bd[3]), bd_est=bd[4], bd_ceil=int(bd[5]),
                bd_rows=int(bd[6]), bd_rowsof=int(bd[7]), bd_names=int(bd[8]), bd_namesof=int(bd[9]), bd_open=bd[10],
                bd_groups=[(g_, int(n_), e_) for g_, n_, e_ in gl_], amend_n=len(am),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R350)(3): the kernel rows of one kind as banked (data/b740_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R350): no lean process runs on this host; the runner dispatches those of (R350)(3), twelve at most, each read by its run id, each
    row carrying free_mb; no suite part in the background. From the command bank (the seat's commands, read live from the capture by the
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
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and runs_ and not free_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b740_commands.json): %s; dispatch commands in the capture: %s of the %d (R350)(3)(d) allows, the worklist`s runs %d, each read by its run id: %s (reads %d, run %s read twice, defect (t)); dispatch and read rows without free_mb: %s (relay data/b740_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b740's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b740_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b740_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b740_standing_v1200.txt', '## THE CONTROLS', '### the instances read at their commits'),
               ('data/b740_offlinezero.txt', '## THE CONTROLS', '## THE DISPATCHES'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R350): the plan bank's md5 prints before any Lean file is written and the statements bank is committed before any Lean file
    ((R350)(3)(a)); every figure bank opens with its controls; the (W) regeneration, the pre-lock comparison and the probe-path refusal
    print before the lock gate. Step zero (the md5's print), v1.20.0's commit, the corrigendum's, the statements', the first Lean commit,
    the last and the build bank's in that order by time, the statements an ancestor of the build bank; the plan bank at HEAD its blob at its
    last commit, its md5 the step zero print's; no commit of the act touching it."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (ROOT, K.C1_CORR), (ROOT, K.C2_RELAY), (K.EF_DIR, K.ZQ_FIRST),
              (K.EF_DIR, K.ZQ_TIP), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C2_RELAY, K.C3_RELAY[0]], capture_output=True).returncode == 0
    md5_ = K.PLAN_MD5 in rdn(K.CITATION_BANK)
    later_ = [h_ for h_ in g(ROOT, 'log', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', K.PLAN_BANK).split() if h_.strip()]
    same_ = md5_ and _s_md5(os.path.join(ROOT, *K.PLAN_BANK.split('/'))) == K.PLAN_MD5 \
        and rdn(K.PLAN_BANK[len('data/'):]) == g(ROOT, 'show', '%s:%s' % (K.C2_PLAN_FIRST, K.PLAN_BANK)).replace(chr(13), '') and not later_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = same_ and regen_ and bool(tz) and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the plan bank`s md5 %s printed at step zero (relay %s): %s; the plan bank its md5 and its blob at %s, a commit of the act touching it: %s -- %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked: %s; the probe-path refusal banked and clear: %s; step zero, v1.20.0, the corrigendum, the statements, the first Lean commit, the last and the build bank in that order by time: %s (%s), the statements an ancestor of the build bank: %s; the tools` controls before their figures: %s' % (
            K.PLAN_MD5[:8], K.CITATION_BANK, md5_, K.C2_PLAN_FIRST[:8], later_ or 'NONE', same_, regen_, bool(tz), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b740's objects; b739's in git at b739's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b740_standing_v1200.txt', ('ALL AS WANTED',)), ('b740_offlinezero.txt', ('SP3 NOT REACHED AT (c7) lamM_centre_encl', 'DISPATCHES 3 OF 12', 'THE ORDER OPEN AT SP2')),
             ('b740_corrigendum.txt', ('ITEMS',)), ('b740_citation_check.txt', ('THE CHECK CLEAN',)), ('b740_reproduce.txt', ('REPRODUCES',)), ('b740_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R350): SP3 prints REACHED, NOT REACHED or STOPPED, and every built name its axiom print; the entry's nouns are the banks'; no
    sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem; a value at one point is a value; no
    comparative sentence contradicts the table it cites (the citation check's comparative read); the root prompt's sentences about the entry
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
    built_ = re.findall(r'^  S5[cd] \(([cd]\d)\) (\w+)\s+(.*)$', bt_, re.M)
    sp_ = len(built_) == 15 and all(a_ == '%s (run %d)' % (ax_, K.EF_RUNS[-1]) or a_ == 'NOT BUILT (run None)' for _r, _n, a_ in built_) \
        and re.search(r'\*\*SP3 (REACHED|NOT REACHED AT|STOPPED)', bt_) is not None
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'   # ### b739 defect (k'): "Nothing here ... locates any zero" read as a location
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|locates? (?:a|any|one|the) zero|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    nouns_ = [w_ for w_ in ('SP3', 'lamM_centre_encl', 'zqFn_centre_le', str(f['bd_disp']), str(f['bd_lines']), 'data/%s_offlinezero.txt' % ACT, 'data/%s_s5cd_statements.txt' % ACT) if w_ not in text]
    cmp_ = re.search(r'COMPARATIVE[^\n]*CONTRADICTS (\d+)', rdn(K.CITATION_BANK))
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and sp_ and not loc_ and not nouns_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; SP3 graded and every built name of the statements printed with the standard three, (c4) and (c7) NOT BUILT (relay data/b740_offlinezero.txt): %s; read from %s, a sentence saying a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem: %s; the build bank`s nouns absent from the entry: %s; the citation check`s comparative line: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), sp_, src, loc_ or 'NONE', nouns_ or 'NONE', cmp_.group(0) if cmp_ else 'NO COMPARATIVE SENTENCE IN THE ACT`S BANKS READ', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))   # ### the entry`s nouns the banks`: SP3, the open row and the built terminal, the figures, the two banks
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R350) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R350)(5))
# ### (R350)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R350) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b739's form, carried) -- read from git,
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
    # ### (R350)(3), (5), N5: no ref of any kernel carrying a commit made after the act's opening commit (no kernel touched); no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b739 left them; the address scan's count from its bank (relay data/b740_address_scan.txt), the suite's arm recounting it live;
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
    # ### (R350)(3)(c), N5: no Zenodo write, no GitHub description, no release, no new version in the capture; no zenodo route of the act's
    ghe_ = [r_['n'] for r_ in (jl('%s_commands.json' % ACT).get('rows') or []) if re.search(r'\bgh\s+repo\s+edit\b|\bgh\s+release\b|/actions/newversion|zenodo\.org/api', r_.get('cmd') or '')]
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b740_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit, release, a new version or a Zenodo route in the capture: %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghe_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b740 — lane two, act one hundred and sixty-seven, the numerics act under (R350): b739 at its weight and its corrigendum; v1.20.0; '
            'W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d in the tree at box A`s centre, SP3 graded, the order open at SP2')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form; every figure from the banks (the build bank's foot, v1.20.0's
    controls)."""
#⟪END⟫
#⟪SECTION record 31⟫
    if f['bd_sp3g'] != 'NOT REACHED AT (c7) lamM_centre_encl' or (f['bd_rows'], f['bd_rowsof']) != (12, 14):
        sys.exit('### THE TITLE`S FORM IS THE NOT-REACHED-AT-(c7) ONE AND THE BANK READS %s, ROWS %s OF %s -- NOTHING COMPOSED' % (f['bd_sp3g'], f['bd_rows'], f['bd_rowsof']))
    return ('## W-ORD-ZQ-OFFLINE-ZERO, S5c-S5d in the tree: the incomplete gamma and the certified elementary values stated and compiled to (d8) zqFn_centre_le, %s of %s rows, (c4) and (c7) not; '
            'SP3 NOT REACHED at (c7) lamM_centre_encl; %s dispatches, %s lines against 482-2,675; the order OPEN at %s; the arm control and %d repairs landed' % (
                f['bd_rows'], f['bd_rowsof'], f['bd_disp'], f['bd_lines'], f['bd_open'], f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) SP3’s P and ε, which (R350)(3)(b) asks as rationals without naming them, taken in the statements bank before any Lean as P = 0 and ε = 1/10, so that only an upper bound on ‖(Gamma c)⁻¹‖ is wanted (relay data/b740_s5cd_statements.txt :14-:20); (2) (c7) lamM_centre_encl not built within the twelve: its quadrature route, chosen in the statements bank, has no neighbour at the pin, and the series route needs Gamma(cA) and π past twenty digits (relay data/b740_offlinezero_notes.txt (6)); (c4) incGamma1_add_one not built with it, (c7) its one use (notes (5)); (3) S5c’s tail bounded by the decaying tail_le (Tail.lean :99), not by zq_thetaC_tail, whose bound is not integrable against t^(w−1) for Re w ≤ 1 (notes (2)); (4) the clone D:/zq-b738 reused, not cloned afresh, its snapshot before and after in the dispatch rows (notes (1)); '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R350)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b740's objects; b739's composer in git at
    b739's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot, not the seat's row quoting b739's (defect (a'))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R349)(2)(v)
    e = ['', _title(), '',
         'S5c and S5d of W-ORD-ZQ-OFFLINE-ZERO are stated and built on zq-b730 of SIDE-explicit-formula at %s, off main and untagged, three commits from %s, at the centre of box A, cA = 95326/100000 + (16290216/1000000)i. %s of %s rows of the statements bank compile, %s of %s printed names, each with propext, Classical.choice and Quot.sound (run %d); the last, zqFn_centre_le, bounds ‖zqFn cA‖ by 13103/10000 · 16012218800 · δ for any δ bounding ‖lamM cA + lamM (1 − cA) − 1/(cA (1 − cA))‖. That one enclosure, (c7) lamM_centre_encl, is not built, and (c4) with it, so SP3 is NOT REACHED at (c7): no value of zqFn cA is certified and no ε is printed as reached. %s lines against %s by the measured ratio, within the three-times ceiling of %s; %s of the %s dispatches spent, each read by its run id. The order stays OPEN at %s; S6 is not begun. The draft stands at v5, HELD.' % (
             K.ZQ_TIP[:8], K.ZQ_ENTERING[:8], f['bd_rows'], f['bd_rowsof'], f['bd_names'], f['bd_namesof'], K.EF_RUNS[-1], f['bd_lines'], f['bd_est'], f['bd_ceil'], f['bd_disp'], f['bd_max'], f['bd_open']), '',
         '*Filed at b740 on the author’s ruling `(R350)`; %d question%s put before the root. Banks: relay '
         '`data/b740_corrigendum.txt`, `data/b740_standing_v1200.txt`, `data/b740_rules.txt`, `data/b740_s5cd_statements.txt`, `data/b740_offlinezero.txt`, `data/b740_offlinezero_notes.txt`, `data/b740_dispatch_rows.json`, `data/b740_prelock.txt`, `data/b740_pathrefusal.txt`, '
         '`data/b740_reproduce.txt`, `data/b740_address_scan.txt`, `data/b740_touch.txt`, `data/b740_standing_figures.txt`, `data/b740_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R350)(1)-(2), %s, %s, %s): b739 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b739’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b740_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b740_standing_v1200.txt); the arm that could not pass at their head, '
         'an arm’s search phrase read under its target’s fold (tools/standing/armnorm.py), every arm’s positive control printed before the lock.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): the plan bank’s md5 %s printed at step zero before any Lean file and again among the build bank’s controls, equal to its blob at %s; tools/standing/ v1.20.0 at %s, the weight and the corrigendum at PLACE-papers %s and their banks at %s, (2) whole before (3); the statements at %s before the first Lean commit %s on %s; the last Lean commit %s, then the build bank at %s. The build bank opens with its controls before its figures. The (W) regeneration printed in the face, and the pre-lock comparison and the probe-path refusal banked, before the lock gate (relay data/b740_prelock.txt, data/b740_pathrefusal.txt). No lean process on this host; %s dispatches, each row carrying free_mb, each read by its run id, the first read twice, a void row at the download root standing before its read at the artifact (defect (t); relay data/b740_dispatch_rows.json).' % (
             K.PLAN_MD5[:8], K.C2_PLAN_FIRST[:8], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_RELAY[:8], K.ZQ_FIRST[:8], K.ZQ_ENTERING[:8], K.ZQ_TIP[:8], K.C3_RELAY[0][:8], f['bd_disp']), '',
         '**The statements before any Lean** ((R350)(3)(a)): fifteen rows, (c1)-(c7) for S5c and (d1)-(d8) for S5d, nine general and six at the centre, each with its route and its Mathlib or kernel neighbour, ABSENT twice ((c1)’s object, its nearest named; (c7)’s route), and fourteen with a reason: row (d7) carries none (defect (b’)), and row (d6) carries its route in a clause without the word (defect (z)). The precision taken there: ε = 1/10 with P = 0, so δ ≤ 1/(10 K). Its forecast of K, about ninefold high by (d5) at N = 64, stands as committed; the constants computed after give 16012218800, 1.096 times the true 1/|Gamma(cA)| (notes (4), defect (r)), so δ ≤ 4.77e-12 is the figure (notes (3)).', '',
         '**The build to SP3** ((R350)(3)(b)-(d), N1, N3): S5c in IncGamma.lean, 227 lines against 400-1000: incGamma1 on [1, ∞), its integrability (c2) and norm bound (c3), the truncation remainder of lamM (c5) and the shell bound (c6), the tail by tail_le (notes (2)); its first dispatch BREAKS on one congr goal at :153, fixed at :155. S5d in Elem.lean, 351 lines against 500-1500: certified exp, cos, sin and log on rational intervals (d1)-(d3), the real-base power (d4), the upper bound on ‖(Gamma c)⁻¹‖ by GammaSeq at N (d5) and at the centre, 16012218800 (d6), the base power at the centre (d7), and zqFn_centre_le (d8); its first dispatch BREAKS on two trailing ring calls after the goal closed, its second KERNEL. %s lines in all against %s, the ceiling %s; ROWS COMPILED %s OF %s, NAMES %s OF %s (relay data/b740_offlinezero.txt). No integral is evaluated and no value of zqFn computed in Lean.' % (
             f['bd_lines'], f['bd_est'], f['bd_ceil'], f['bd_rows'], f['bd_rowsof'], f['bd_names'], f['bd_namesof']), '',
         '**The enclosure not built** ((R350)(3)(b)-(c)): (c7) lamM_centre_encl, the one enclosure SP3 wants, needs each incomplete gamma at small a and |Im w| about 16.3 certified to about 1e-13; its quadrature route has no neighbour at the pin and the series route needs Gamma(cA) and π past twenty digits; it is not built within the twelve (notes (6)), nor (c4), its one use (notes (5)). S6 is not begun.', '',
         '**The git writes** (N5): one git write per message, add and commit in separate messages, across the relay, PLACE-papers and the kernel clone D:/zq-b738; the act read by the suite’s arm over the capture.', '',
         '**What this act is not**: no deposit, no new version, no Zenodo field, no GitHub description; no tag, no draft published, no merge, no kernel’s main touched; every Lean file of the act on zq-b730 alone. SP3 is not reached: zqFn_centre_le reduces SP3’s value to one enclosure, and no value of zqFn at the centre is certified. Nothing here proves RH or GRH, and no zero of Z_Q0 is located in Lean.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b740_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b740_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b740_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b740 -- %s, %s, %s, %s -- against b739’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b740_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the corrigendum and the build read one way: the arm that could not pass was repaired by reading its phrase under its target’s fold, and the statements were read by the arm that grades them, which found row (d6) without the word its route asks (defect (z)); each bank is read as committed, its wrong sentences noted beside it.', '',
         '**Carried to:** %s, (R350)(6), the act the author names: W-ORD-ZQ-OFFLINE-ZERO OPEN at SP2, SP3 NOT REACHED at (c7) lamM_centre_encl, its route to be priced, and (c4) with it; S6 not begun; the wave 1 deposit; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds, and no zero is located in Lean.*', '']
    return _title(), NL.join(e)


def _finding_text_b739():
    """b739's form over b739's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b740's objects; b739's composer in git at b739's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD, W-ORD-ZQ-DERIVES closed at b736 and W-ORD-ZQ-OFFLINE-ZERO open at SP2."""
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
             '**(R350) ratified.** Its components as the ferry orders them (relay data/b740_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b739’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** W-ORD-ZQ-OFFLINE-ZERO (priced at OPEN_TRAILS :%d) built in the tree to S5c-S5d at box A’s centre on zq-b730 at %s; SP3 %s; it stays OPEN at %s, S6 not begun.' % (K.PRICE_LINE, K.ZQ_TIP[:8], f['bd_sp3g'], f['bd_open']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b740_standing_v1200.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The build:** SP3 %s; rows compiled %s of %s, names %s of %s, each with the standard three (run %d); %s lines against %s, the ceiling %s; %s dispatches of %s (relay data/b740_s5cd_statements.txt, data/b740_offlinezero.txt, data/b740_offlinezero_notes.txt, data/b740_dispatch_rows.json).' % (
                 f['bd_sp3g'], f['bd_rows'], f['bd_rowsof'], f['bd_names'], f['bd_namesof'], K.EF_RUNS[-1], f['bd_lines'], f['bd_est'], f['bd_ceil'], f['bd_disp'], f['bd_max']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b740_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b740_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b740_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b740 `%s` (previous `%s`, b739’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b740_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b740_standing_v1200.txt); the standing '
             'report tool (relay data/b740_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** zq-b730 of SIDE-explicit-formula from %s to %s, three commits, two Lean files under Schema/ZQ/OffZero (IncGamma, Elem) and print_targets.txt, off main, untagged; no kernel’s main touched; %d dispatches; the %s branches as b739 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.ZQ_ENTERING[:8], K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b740_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b739’s %s, %s, %s, %s (relay data/b740_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b740_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b739():
    """b739's trail record over b739's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: three of the twelve (R350)(3)(d) allows; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725 and detect-b729 kept, unmoved; zq-b730 at the build`s tip; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b739 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b730-b738`s and this act`s two (IncGamma, Elem); MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R350)(5): relay push-b739-closing, push-b739-preroot, push-b739-record; PLACE-papers push-b739-preroot, push-b739-record; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: two Lean files and print_targets.txt alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R350) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (454f2167) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R350)(2): FINDINGS :13389.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R350)(2): row (60).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-OFFLINE-ZERO entered at b737 (OPEN_TRAILS :17400), open at SP2.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b740_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.20.0`s controls, the build bank, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none alone: the statements bank committed at a9c206b9 with the worklist`s one line, before any Lean file (N2).'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none named; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: the build bank first committed at 218029c8, after the statements (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### two on zq-b730 (IncGamma, Elem), N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R350)(2): tools/standing/ to v1.20.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b740_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, the gh reads, the three workflow dispatches and their artifact downloads under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### (R350)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b740_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b740_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1200', 'offlinezero', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b740_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b740_registration_%s.txt -- b740, THE NUMERICS ACT: b739 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.20.0; W-ORD-ZQ-OFFLINE-ZERO S5c-S5d BUILT IN THE TREE AT BOX A`S CENTRE TO SP3; "
                             "NO DEPOSIT, NO NEW VERSION, NO MERGE, NO TAG, UNDER (R350)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b739's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b740: b739's lines read banks this
act does not write, and are not carried; the lines are b740's: S5c-S5d built at box A's centre and SP3 graded (KERNEL, the rows and
names compiled), tools/standing/ v1.20.0 by its controls (CERTIFIED), the order open at SP2 with (c7) not built (REGISTERED), and the
draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b740's lines, each from the record tool's figures over b740's banks
    # ------------------------------------------------------------------ KERNEL: (R350)(3), S5c-S5d on zq-b730 at box A's centre, SP3 graded
    sz = seat('%s_offlinezero.txt' % ACT, '**SP3 ')
    sk = sz   # ### (R349)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO S5c-S5d AT BOX A`S CENTRE: SP3 %s; rows compiled %s of %s, names %s of %s; %s lines against %s (the ceiling %s); on zq-b730 at %s; %s dispatches of %s. SOURCE %s.' % (
        f['bd_sp3g'], f['bd_rows'], f['bd_rowsof'], f['bd_names'], f['bd_namesof'], f['bd_lines'], f['bd_est'], f['bd_ceil'], K.ZQ_TIP[:8], f['bd_disp'], f['bd_max'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.20.0 ((R350)(2)), by its controls
    sw = seat('%s_standing_v1200.txt' % ACT, '**v1.20.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.20.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the order open, from the notes beside the build bank
    so = seat('%s_offlinezero_notes.txt' % ACT, '(6) (c7) lamM_centre_encl is NOT BUILT')
    seats.append(so)
    keys['ORD'] = ('REGISTERED -- THE ORDER OPEN AT %s: (c7) lamM_centre_encl not built, its quadrature route ABSENT in the statements bank; S6 not begun. SOURCE %s.' % (
        f['bd_open'], so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R350)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]   # ### b740's four lines
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b740 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
