# -*- coding: utf-8 -*-
# b739 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R349)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R349)(2) repair it carries. Edited by the Edit tool. Carried at b739 by tools/b739_fold.py (`carry`) from tools/acts/b738.py,
# b738`s names substituted; the citation`s sections adopted from tools/b739_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b738`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b738`s carried till
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
# ### b739, Component 1 (the Edit tool): THE c1 ROUTE FOR b738'S WEIGHT LINE AND ITS CORRIGENDUM, (R349)(1)-(2). Carried from b738's
# ### override and rewritten here against b738's own banks: the closing's lines by needle, the events (7), the defects (19), the refusals
# ### (2), the v1.19.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '3f45857d'          # ### b738's closing commit
C1_REFUSAL_AT = '3f45857d'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-04'
C1_CORRIGENDA_LAST = 58
C1_V170 = 'b739_standing_v1190.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-04 by b739 to b738’s entry (:%d), under `(R349)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-OFFLINE-ZERO on R4, box A: SP1 REACHED'
C1_TRAIL_NEEDLE = '### b738 — lane two, act one hundred and sixty-five, the frame act under (R348)'
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
    for l in _c1_rd('b738_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b738_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b738_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b738_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b738_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b738_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b738_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b738_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 7 or 'N5' in held or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b738_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b738_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b738_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    gr, l_gr = _c1_fl('b738_offlinezero.txt', r'^### ### \*\*SP1 REACHED ; SP2 REACHED ; DISPATCHES (\d+) OF (\d+) ; LINES SP1 (\d+) AGAINST (\d+-\d+), S5a-S5b (\d+) AGAINST (\d+-\d+) ; zq_offline_of_box AXIOMS (propext, Classical\.choice, Quot\.sound) ; THE CONTRAPOSITIVE AXIOMS propext, Classical\.choice, Quot\.sound ; THE ORDER OPEN AT SP2\.\*\*$', 'the build`s grade')
    (rp1, rp2), l_rp = _c1_fl('b738_offlinezero.txt', r'^  S5c-S5d at 900-2500 \(the plan :136\): by that ratio (\d+)-(\d+) lines ;', 'the re-price')
    _nb, l_nb = _c1_fl('b738_offlinezero.txt', r'^  (S5c and S5d NOT BEGUN) ', 'S5c-S5d not begun')
    (va, vb), l_v = _c1_fl('b738_standing_v1180.txt', r'^### ### \*\*v1\.18\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*$', 'the v1.18.0 foot')
    _mv, l_mv = _c1_fl('b738_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'(mirror-refresh-2026-11-03-b738)\.zip ; ', 'the mirror`s archive')
    (n3r,), l_n3 = _c1_fl(c, r'^    \(N1\) HELD \(N2\) HELD \(N3\) (REFUTED) \(N4\) HELD \(N5\) REFUTED ;', 'the record-time scores')
    _aw, l_aw = _c1_fl('b738_author_answers.txt', r'="(Land, N5 REFUTED) \(Recommended\)"', 'the author`s answer')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 8)) or len(dr) != 19:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b738 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b738_closing.txt):* “%s” (data/b738_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b738_steps.json, the record and closing rows). As its rows read: `W-ORD-ZQ-OFFLINE-ZERO` built on R4, box A (relay data/b738_offlinezero.txt :%d): '
            'SP1 REACHED, zq_offline_of_box compiled at %s lines against %s; SP2 REACHED, S5a-S5b at %s lines against %s; the contrapositive compiled; axioms %s throughout; %s of %s dispatches; the order OPEN at SP2. '
            'S5c-S5d not begun (:%d), re-priced at %s-%s lines by the measured ratio (:%d), the incomplete gamma, complex Stirling and certified elementary values absent at the pin; no integral evaluated, no value of zqFn computed, '
            'no zero located in Lean, Li nonnegativity not refuted as a theorem. '
            'Standing tools v1.18.0, %s of %s (data/b738_standing_v1180.txt :%d); the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), '
            'G-AXIOM-CLAIM declared on the face; SCORES %d OF 8 HELD, N5 REFUTED on defect (m), the kernel clone’s add and commit sent in parallel, as the author accepted at the root (“%s”, data/b738_author_answers.txt :%d); '
            'the closing’s score line prints N3 %s (:%d), the reading at the record before the root prompt was banked, where the scores bank read at the close holds N3 HELD (data/b738_scores_close.json). '
            'The root %s over %s banks, chained from %s (data/b738_act_root.json; :%d); the post-push part standing-b2d stopped by the host for low memory while idle (events (6)) and re-run on the author’s word in the foreground (events (7)); '
            'the mirror %s at %s (data/b738_mirror_verify.txt :%d; :%d); %s prompts banked as put by the seat (:%d); %d events in data/b738_events.txt, rows (1)-(%d); %d defects, (a)–(s) '
            '(data/b738_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'The draft at v5; nothing deposited, no Zenodo description edited; the corrigendum for these rows follows, under `(R349)`(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, l_gr, gr[2], gr[3], gr[4], gr[5], gr[6], gr[0], gr[1],
                l_nb, '{:,}'.format(int(rp1)), '{:,}'.format(int(rp2)), l_rp,
                vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                len(held), _aw[0], l_aw, n3r, l_n3,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b738's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '00:19:27Z', 'defect (o)'), (2, 'READ', '03:29:42Z', 'event (3)')]
C1_UNROWED = []
C1_CORR_TITLE = ('## Corrigendum to b738’s record (relay data/b738_events.txt rows (1)-(7) and data/b738_defects.txt): seven events and nineteen defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the parallel git write the hook did not refuse at its head; the post-push phases read, the seal subject from its bank, the guarded last row, no background part, no sed, '
                 'at tools/standing/ v1.19.0, each controlled, under (R349)(2)')


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
    rl = _c1_git('show', '%s:data/b738_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b738_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.19.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(7)', sorted(ev) == list(range(1, 8))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 19', len(dr) == 19), ('the refusals 2, each answered as listed', len(rl) == 2 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.19.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.19.0
C1_EV_EXTRA = {2: '; repair (runs); rule (4) of data/b739_rules.txt', 3: '; repair (sed); rule (6) of data/b739_rules.txt, the instance REPEAT of class (19)', 4: '; repair (subjects); rule (3) of data/b739_rules.txt',
               5: '; repair (phases); rule (2) of data/b739_rules.txt, the finding printed and no guard moved', 6: '; repair (background); rule (5) of data/b739_rules.txt, REPEAT of b735’s reaped watch'}
C1_DF_EXTRA = {'m': '; repair (gitwrite); rule (1) of data/b739_rules.txt; N5 REFUTED on it', 'p': '; repair (sed); rule (6) of data/b739_rules.txt'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b739, to the counter (`(R349)`(1)): “CLAIM 0, CLOSE 26, REPEAT 9 OF 26” is relay data/b738_closing.txt :5, over the seven events and the nineteen defects together; over the defects alone the tags give CLAIM 0, CLOSE 19, REPEAT 7 of 19, the root prompt’s figure (data/b738_author_answers.txt :4). Both read from the same tags; this entry prints both and edits neither.',
            'Dated note, b739, to b738’s score line: relay data/b738_closing.txt :137 and its record print N3 REFUTED, the reading at the record, when the root prompt was not yet banked; the scores bank read at the close (data/b738_scores_close.json) holds N3 HELD, and the closing’s head line its “scores 7 of 8 HELD”. Both are b738’s; neither is edited.',
            'Dated note, b739, to b738’s defects (h) and (i): the line-keyed overrides moved by a template insert and b734’s checks render broken by b2d3afc0 have no repair in `(R349)`(2); no load path of b739 imports a past act’s checks render; they stay carried.')
C1_CLASSES = (
    ('gitwrite', 'the parallel git write the hook did not refuse (`(R349)`(2)(i), defect (m), N5; CLOSE ; NEW, the class of b736’s 05:22Z pair)', 'rule (1) of data/b739_rules.txt; Claude Code writes a message’s tool blocks to the transcript only after its tools have run, so v1.17.0’s sibling read had nothing to count; the hook now keys each allowed git write to the transcript’s last api-request line, written before the tools run, in a per-session ledger, and refuses a second write under the same request in any repository, kernel clones included, kind GITWRITE. b738’s 23:22:55Z pair on the kernel clone replayed: the commit passed before, GITWRITE after; a single add and the next message’s commit pass. The count over the session: b738 95 messages carrying a git write, one with two; b739 one write per message'),
    ('phases', 'the post-push chain phases against the pre-push (`(R349)`(2)(ii), events (5); CLOSE ; REPEAT of b737 events (2))', 'rule (2) of data/b739_rules.txt; tools/standing/phases.py puts each part’s two banks side by side. The finding, printed before any guard moves: the post-push read did the pre-push read’s work in 5 of 5 parts, one remote read in each of 38 repositories and the same reads at commit; the time grew in standing-b2b and standing-b2c alone and in every phase of both (ratios 1.80-3.33), the slowdown the host’s while those parts ran; `(R348)`(2)(vi)’s split landed, every pre-push chain phase under 450 s. No guard moved'),
    ('subjects', 'the seal subject against its bank (`(R349)`(2)(iii), events (4); CLOSE ; NEW)', 'rule (3) of data/b739_rules.txt; tools/standing/subjects.py reads the count before “files” in a seal subject against the seal bank and before “gates” in a lock subject against the lock gate, and composes both; the hook refuses a subject the check faults, kind SUBJECT. b738’s “85 files” replayed: passed before, SUBJECT after; regenerated reading 80; the lock subject’s “eight gates” passing, “seven” planted faulting'),
    ('runs', 'G-DERIVATION-GRADED’s last row on an empty run list (`(R349)`(2)(iv), events (2); CLOSE ; NEW)', 'rule (4) of data/b739_rules.txt; tools/standing/runs.py reads the last row behind a guard and names NO RUNS where the table and the worklist’s runs are both empty. b738’s predicate on b737’s state replayed: IndexError before, NO RUNS after; a matching table RUNS, a differing one DIFFERS'),
    ('background', 'the host’s stop of a background part (`(R349)`(2)(v), events (6); CLOSE ; REPEAT of b735’s reaped watch)', 'rule (5) of data/b739_rules.txt; the hook refuses a suite part or combine sent with run_in_background, kind BACKGROUND. b738’s 04:51Z standing-b2d call replayed: passed before, BACKGROUND after; the same in the foreground passing'),
    ('sed', 'sed and the Read with no offset (`(R349)`(2)(vi), defect (p), events (3); CLOSE ; REPEAT of classes (18) and (19))', 'rule (6) of data/b739_rules.txt; the hook refuses sed as a command word in any form, kind SED; a line is read by the Read tool with an offset and a limit or by tools/standing/peek.py search --lines. b738’s #354 lookup replayed: passed before, SED after; a grep and the reader passing; events (3)’s Read refused READ as v1.4.0 orders'),
    ('exercise', 'the exercise bank at closing (`(R349)`(2)(vii), `(R345)`(2)(viii))', 'rule (7) of data/b739_rules.txt; read against b738, whose closing commit 3f45857d carries data/b738_exercise.json and its ten part banks; the rule stands as ruled. A guard: no failing side'),
    ('version', 'the version (`(R349)`(2)(viii))', 'rule (8) of data/b739_rules.txt; tools/standing/VERSION v1.19.0, landed by a commit of its own (3c92170b) with its controls bank'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b738’s events bank (relay data/b738_events.txt) carries seven rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank nineteen lettered rows, (a)-(s), each tagged in its own bracket (%s); its refusal bank two lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R349)`(2), at tools/standing/ v1.19.0, each with a control on b738’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b738’s events (1)-(7):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( put and \d\d:\d\dZ answered)?( from [^:]*)?|post-push|pre-push and post-push)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b738_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b738’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b738_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b738’s refusals** (relay data/b738_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (seven events, nineteen defects), as b738’s closing prints it (relay data/b738_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims) or 'none'), '',
          '*Filed at b739 on the author’s ruling `(R349)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b739.py) from '
          'b738’s events and defects banks read unedited, its refusal bank, and the v1.19.0 controls bank; banked as relay `data/b739_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b738’s record; no sealed tool, face, trail or root-named bank of b738 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b739 -- THE CORRIGENDUM FOR b738, (R349)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b738_events.txt rows (1)-(7), data/b738_defects.txt 19 rows, data/b738_hook_refusals.txt 2 '
             'lines at %s; data/%s (the v1.19.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 7, DEFECTS 19 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.19.0: THE GIT WRITE BY THE MESSAGE`S REQUEST, THE POST-PUSH PHASES, THE SEAL AND LOCK SUBJECTS, '
               'THE GUARDED LAST ROW, NO BACKGROUND PART, NO SED, THE EXERCISE BANK, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b738 at its weight after its entry, and the corrigendum for b738, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.19.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b739, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b739 ran three
# ### ((R349)(4)(iii)-(iv), N1), rowed in data/b739_dispatch_rows.json. Replaced for b739 alone; the arms' names stand, their plants on b739's rows.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R348)(7), as b738 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R349)(3)(d), N1, b739: twelve dispatches allowed, eleven made; each dispatch row carrying free_mb, its run id the worklist's in order,
    read once after it by that id; the plant a dispatch row with no read refused."""
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b739: each dispatch read once after it by its run id
#⟪END⟫
# ### b739, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R349)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b738, naming tools/standing/hook.py, edited this act by v1.18.0`s commit alone for (R349)(2)(iii) (its blob at b2d3afc0 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b739, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b738's record has twelve
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 10)) \
#⟪END⟫
# ### b739, Component 4 (the Edit tool): b739's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b738's override of checks 526 -- no registration commit -- removed: b739
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b739_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b739, Component 6 (the Edit tool): b739's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b738's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b739, Component 4 (the Edit tool): b738's overrides of checks 1516 and 1659 (hook.py edited by b738's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b739 as it stands
# ### b739, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b739_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b739, Component 4 (the Edit tool): b738's override of checks 1476-1482 (one ERRATA entry at b738's (R348)(5)) removed -- (R349)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b739 as it stands
# ### b739, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b738's step-zero wording; b739's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b739, Component 4 (the Edit tool): G-RUNNER-READ's plant on b739's dispatch rows -- run 2's axiom lines carrying sorryAx (b738's
# ### plant read the lv rows' closure log, which b739 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b739, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b739, Component 6 (the Edit tool): the fold bank was b738's own route
# ### (tools/b738_fold.py); b739's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b739_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b738.py -> tools/acts/b739.py' in (rd('b739_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b739, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b739_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b739, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b739_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b739_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b739, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R349): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    rows = [l for n_ in ('b739_defects.txt', 'b739_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R349) Component 5, the act`s events and defects together; relay data/b739_defects.txt, data/b739_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b739, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b739's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-OFFLINE-ZERO priced at b739 and open,',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b739, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b738's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b739_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b739_registration_%s.txt' % __import__('b739_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b739, Component 4 (the Edit tool, before the face): b738's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b739, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b739's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b739, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R349)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b739 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b739_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b739: the build's one route
#⟪END⟫
# ### b739, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b738's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b739 scorer reads; the needles set to the banks b739's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b739, (R349)(2)(iii): b738's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b739, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b739_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrs')))   # ### (a)-(s), entered before the lock, every one the seat's (data/b739_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b739_corrigendum.txt', 'data/b739_standing_v1180.txt', 'data/b739_rules.txt', 'data/b739_split_replay.txt', 'data/b739_offlinezero.txt', 'data/b739_offlinezero_notes.txt',
                  'data/b739_dispatch_rows.json', 'data/b739_pathrefusal.txt',
                  'data/b739_reproduce.txt', 'data/b739_reproduce.json', 'data/b739_address_scan.txt', 'data/b739_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b739 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R349)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b739_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R349)(4): the sitting bank's rows by number -- a row opens `[n] STATE` at column 0, its fields indented two spaces as `KEY: value`;
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
        # ### (R349)(2)-(4) (b739's keys over b739's objects): the order by time and ancestry; v1.18.0's controls; the plan read as committed;
        # ### the build bank and its notes; zq-b730; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.C2_PLAN_FIRST, K.PLAN_BANK))) or None, _s(blob(ROOT, 'HEAD:' + K.PLAN_BANK)) or None),   # ### the plan at its last commit (b738's) and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_build', K.C1_CORR, K.C2_RELAY),
                                 ('plan_build', K.C2_PLAN_FIRST, K.C2_RELAY), ('sp1_sp2', K.C2_RELAY, K.C3_RELAY[0]))),
        v1130=rd('b739_standing_v1180.txt'), plan=rd('b738_offlinezero_plan.txt'), print_=rd('b739_offlinezero.txt'), rows_bank=rd('b739_offlinezero.txt'),
        notes=rd('b739_offlinezero_notes.txt'),
        plan_first_files=files_of(ROOT, K.C2_PLAN_FIRST), plan_files=files_of(ROOT, K.C2_RELAY), price_files=(),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..%s' % (K.ZQ_ENTERING, K.ZQ_TIP)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--contains', K.ZQ_FIRST).split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b739_dispatch_rows.json') or '[]'), reproduce=rd('b739_reproduce.txt'), reproducej=jl('b739_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b739_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b738 left them
        rebuild=None, rebuild_rows=json.loads(rd('b739_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.C2_PLAN_FIRST), zq_first=_ct(EF, K.ZQ_FIRST), sp1=_ct(EF, K.ZQ_SP1),
               zq_tip=_ct(EF, K.ZQ_TIP), sitting=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.C2_RELAY), sitting=files_of(ROOT, K.C3_RELAY[0]), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b739's read-first bank's items by path, as its step zero wrote them (data/b739_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b738_closing.txt |', 'relay data/b738_events.txt |', 'relay data/b738_defects.txt |', 'relay data/b738_offlinezero_plan.txt |', 'relay data/b738_offlinezero_box.txt |',
                     'relay data/b738_offlinezero_criteria.txt |', 'relay data/b735_explicitformula.txt |', 'relay data/b731_price_measured.txt |', 'relay data/b725_interference.txt |',
                     'relay data/b675_rules.txt |', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/ZQ/ |', 'PLACE-papers FINDINGS.md |', 'PLACE-papers OPEN_TRAILS.md |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R349)(1)-(2))', 'BUILD TO SP1 AND SP2 ((R349)(3))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (93 = 93 + 0, data/b739_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 93 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b738's figures, read at FINDINGS :13165 as Component 1 landed them
    return landed(S, 0, ['b738 AT ITS WEIGHT', 'suite 113 of 116', 'relay b87c1e24', '23 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b739's title in the ferry's Component 3 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-ZQ-OFFLINE-ZERO on R4, box A: SP1 REACHED, the conditional theorem compiled with the standard three, ', ' lines against 135-275; SP2 REACHED, ',
                 ' dispatches; the order OPEN at SP2; the controls-before-figures render, the chain split and ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R349)(1)-(2): the generated entry for b738's nine events and twenty-three defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(9), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 4, CLOSE 28 over 32, REPEAT 17); the repairs at tools/standing/ v1.18.0 by their controls
    bank; the corrigenda bank appended at row (58) and nothing before it changed; in Component 1's commits (the figures read from
    data/b739_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 23 and len(items) == j.get('items') == 32 and j.get('row') == 58 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 32 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 4 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 17 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.18.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 3 \
        and '  (58) ' in S['corrigenda'] and '  (59) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b739_rules.txt carries (R349)(2)'s eight rules, in v1.18.0's commit; data/b739_rules.txt (by form in (R349)(4)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b738's form, its names b739's); no author's word of b739 orders a row of the next act's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and '(1) FIGURES BEFORE CONTROLS' in r1 and '(8) THE VERSION' in r1 and 'data/b739_rules.txt' in S['files']['standing'] \
        and not os.path.exists(os.path.join(D, 'b739_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b739's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO ON R4, BOX A', 'CERTIFIED -- tools/standing/ v1.18.0', 'REGISTERED -- THE ORDER OPEN AT',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b739: eleven dispatches of the twelve (R349)(3)(d) allows -- each dispatch command in the capture a row, each row carrying free_mb and
    read once after it by its run id; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = bool(seq_) and all(
        sum(1 for x in seq_ if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) == 1
        and seq_.index(d) < next(i for i, x in enumerate(seq_) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run')))
        for d in seq_ if d.get('kind') == 'dispatch')   # ### N1: each dispatch read once after it by its run id
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b739_offlinezero\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b739, N1: eleven rows, eleven dispatch commands
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
# ### b739's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The build to SP1**', '**S5a-S5b to SP2**', '**The remainder, priced again**',
                 '**The git writes**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b739_corrigendum.txt', 'data/b739_standing_v1180.txt', 'data/b739_offlinezero.txt', 'data/b739_offlinezero_notes.txt', 'data/b739_dispatch_rows.json',
                 'data/b739_reproduce.txt', 'data/b739_address_scan.txt', 'data/b739_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b739: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R349)(3), N2 (the name the frozen run list carries): the plan bank read as committed -- its blob at HEAD its blob at its last commit
    3dab6492, its md5 the step zero print's, no commit of the act touching it; the plan's commit, v1.18.0's, the corrigendum's, SP1's bank and
    SP2's in that order by time and by ancestry within the relay; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('plan', 'standing', 'corr', 'print', 'sitting')
    return bool(reg) and reg == head and K.PLAN_BANK in S['plan_first_files'] and K.PLAN_BANK not in S['plan_files'] \
        and K.PLAN_MD5 in (S['notes'] or '') \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b739_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    zq-b730 of the one kernel written; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R349)(2)-(4), N2 (the name the frozen run list carries): (2) whole before (3) -- v1.18.0, the weight and corrigendum on PLACE-papers
    and the corrigendum banks before the first Lean commit on zq-b730; then SP1's commit, SP1's bank, the last Lean commit and SP2's bank,
    by the commits' times; the corrigendum an ancestor of SP1's bank."""
    t_ = S['t']
    return all(t_.get(k_) for k_ in ('c1pp', 'c1', 'standing', 'zq_first', 'sp1', 'print', 'zq_tip', 'sitting')) \
        and max(t_['standing'], t_['c1pp'], t_['c1']) < t_['zq_first'] <= t_['sp1'] < t_['print'] < t_['zq_tip'] < t_['sitting'] \
        and S['anc'].get('corr_build') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R349)(3), N1, N3 (the name the frozen run list carries): the build bank's dispatch table -- one row per dispatch, its run id the
    worklist's in order, each row's sha one of zq-b730's eleven commits and its free memory printed, each graded KERNEL or BREAKS; the
    lines measured per group and in all against the plan's estimates; SP1's statement and its open hypotheses named; the foot SP1 REACHED
    and SP2 REACHED with the standard three."""
    t = S['print_'] or ''
    rows = re.findall(r'^  (\d+) \| group (\S+)\s*\| (\w+) \| sha ([0-9a-f]{8}) \| run (\d+) \| free (\d+) MB \| (KERNEL|BREAKS),', t, re.M)
    v = _vlast(t)
    return [int(r[4]) for r in rows] == list(K.EF_RUNS) and [int(r[0]) for r in rows] == list(range(1, len(K.EF_RUNS) + 1)) \
        and all(any(c.startswith(r[3]) for c in K.ZQ_COMMITS) for r in rows) and rows[-1][6] == 'KERNEL' \
        and 'SP1 IN ALL: measured 206' in t and 'S5a-S5b IN ALL: measured 321' in t \
        and 'THE OPEN HYPOTHESES, NAMED: hcm and hfr' in t \
        and v.startswith('SP1 REACHED ; SP2 REACHED ; DISPATCHES 11 OF 12') and 'zq_offline_of_box AXIOMS propext, Classical.choice, Quot.sound' in v
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip
    locally and at origin; zq-b730's diff against its entering tip the seven OffZero modules and print_targets.txt alone, its eleven commits
    the worklist's in order; no tag and no other branch carrying the act's first Lean commit (no merge)."""
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
    arm list since b738's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R349)(3)(b)-(c), N3, N5 (the name the frozen run list carries): the remainder of S5 re-priced from S5a-S5b -- the ratio measured
    over the estimate and S5c-S5d's lines by it, S5c and S5d NOT BEGUN, no OffZero module beyond the seven; the price line in OPEN_TRAILS at
    :17400 unmoved; no sentence of the build bank or its notes a location or a failure stated as a theorem."""
    n_ = S['rows_bank'] or ''
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    sents = [s_ for t_ in (n_, S['notes'] or '') for s_ in re.split(r'(?<=[.;:])\s+', t_)]
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    return 'S5a-S5b`s ratio, measured over the estimate: 321 / 300-600 = 0.535-1.070' in n_ and 'S5c-S5d at 900-2500 (the plan :136): by that ratio 482-2675 lines' in n_ \
        and 'S5c and S5d NOT BEGUN' in n_ and not [f_ for f_ in S['zq_files'] if '/OffZero/' in f_ and f_ not in K.ZQ_FILES] \
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
    """standing clauses v9 (Component 7 of (R349): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b739_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b738's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R349-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b738's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R349) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b738's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R348)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 54cd4f92',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 93 = 93 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b738-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 form: W-ORD-ZQ-OFFLINE-ZERO planned, no build, the candidate off0 with its figures, the routes priced and R4 recommended with its lines, dispatches and absent objects, [76] and [77] passed at SIDE-effects main, the amendment regeneration and the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R349)(1)-(2): the generated corrigendum for b738`s record, landed at FINDINGS :13167: its nine events and twenty-three defects, 32 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 4 CLOSE 28, REPEAT 17; v1.18.0`s repairs by data/b739_standing_v1180.txt; the corrigenda bank appended at row (58)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b739_rules.txt carrying (R349)(2)`s eight rules in v1.18.0`s commit, no data/b739_rules.txt',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b739's objects
    ('G-REGISTRATIONS-FIRST', '(R349)(3), N2: the plan bank read as committed, its blob at HEAD its blob at 3dab6492 and its md5 printed beside the notes, no commit of the act touching it; the plan`s, v1.18.0`s, the corrigendum`s, SP1`s bank and SP2`s in that order by time and ancestry; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(sp1_sp2=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b739_address_scan.py run live over every commit of the act in the relay, PLACE-papers and zq-b730, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R349)(2)-(4), N2: (2) whole before (3) -- v1.18.0, the weight and corrigendum and their banks before the first Lean commit; then SP1, SP1`s bank, the last Lean commit and SP2`s bank by time; the corrigendum an ancestor of SP1`s bank',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_build=False))),
    ('G-DERIVATION-GRADED', '(R349)(3), N1, N3: the build bank`s dispatch table -- one row per dispatch, the worklist`s eleven runs in order, each sha a zq-b730 commit, free memory printed, KERNEL or BREAKS; the lines 206 and 321 against the estimates; the open hypotheses named; the foot SP1 REACHED, SP2 REACHED with the standard three',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'print_', (S['print_'] or '').replace('| run 41743136382 |', '| run 41743136383 |'))),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against b25fd82c the seven OffZero modules and print_targets.txt alone, its eleven commits the worklist`s; no tag and no other branch carrying them',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 54cd4f92, VERSION 9; v8 at HEAD its blob at 54cd4f92; no v10; v9`s commit an ancestor of v1.18.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R349)(3)(b)-(c), N3, N5: the remainder of S5 re-priced from S5a-S5b, 321 / 300-600 = 0.535-1.070, S5c-S5d 482-2675 lines by it; S5c and S5d NOT BEGUN, no OffZero module beyond the seven; the price line at OPEN_TRAILS :17400; no sentence a location',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'rows_bank', (S['rows_bank'] or '').replace('S5c and S5d NOT BEGUN', 'S5c BEGUN'))),
    ('G-DIFFERS-ERRATA', '(R349): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 0cfc46e, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b739_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R349-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b738`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 54cd4f92 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: twelve dispatches allowed by (R349)(3)(d), eleven made, each row carrying free_mb, each read once after it by its run id, the worklist`s runs in order; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: eleven dispatch commands in the capture, eleven rows, each read after it by its run id, each carrying free_mb; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b738 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b738`s [41] tip; the join kernel`s main and its one tag v0.1.0; zq-b730`s eleven commits read at G-OFFSET-POST-HOC',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers, FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b738`s trail record on OPEN_TRAILS (:17402) and its root in the chain', lambda S: '### b738 — lane two, act one hundred and sixty-four, the plan act under (R348)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers, FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b738`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b739 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b738's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b739: (R349)'s rows. (1)'s line read by the ruling from the public relay at 3f45857d
    pub = _blob('D:/relay', '3f45857d', 'data/b738_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b738_closing.txt :1, the head line as the public relay carries it at 3f45857d', bool(pub) and pub[0] == at(cl, 1) and 'relay ab6d923f' in pub[0] and 'PLACE-papers 42dba04' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 115 of 116', 'root f28b18c138ef6a63', '2 prompts answered', 'scores 7 of 8 HELD', '19 defects'):
        add('ruling (1)', 'data/b738_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'the closing`s counter CLAIM 0, CLOSE 26, REPEAT 9 OF 26 (events and defects), data/b738_closing.txt :5',
        'CLAIM 0, CLOSE 26, REPEAT 9 OF 26' in at(cl, 5), at(cl, 5)[-40:], '1')
    dfl_ = [l for l in lines_of(p('data', 'b738_defects.txt')) if re.match(r"^    \([a-z]'?\) ", l)]
    tg_ = (sum(1 for l in dfl_ if '[CLAIM' in l), sum(1 for l in dfl_ if '[CLOSE' in l), sum(1 for l in dfl_ if '; REPEAT' in l), len(dfl_))
    add('ruling (1)', 'data/b738_defects.txt, 19 lettered defects, their tags printed', tg_[3] == 19, 'CLAIM %d CLOSE %d REPEAT %d OF %d' % tg_, '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b738']]
    add('ruling (1)', 'data/act_roots.txt, b738`s root f28b18c1 chained from b737`s 706d369c', len(ar8_) == 1 and ar8_[0][1].startswith('f28b18c1') and ar8_[0][2].startswith('706d369c'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b738_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b659-b738 (b738`s post-push part b3)', 'b738 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b738 AGREE' if 'b738 AGREE' in b3_ else 'ABSENT', '1')
    b2d_ = rd(p('data', 'b738_checks_postpush_standing-b2d.txt')) or ''
    add('ruling (1)', 'the re-run of b2d on the author`s word, b636-b658 AGREE (b738`s post-push part b2d, events (7))', 'b636 AGREE' in b2d_ and 'b658 AGREE' in b2d_ and 'DISAGREE' not in b2d_,
        'b658 AGREE' if 'b658 AGREE' in b2d_ else 'ABSENT', '1')
    ob_ = lines_of(p('data', 'b738_offlinezero.txt'))
    add('ruling (1)', 'data/b738_offlinezero.txt :80, the grade line: SP1 and SP2 REACHED, 11 of 12 dispatches, 206 against 135-275, 321 against 300-600, the order open at SP2',
        all(w_ in at(ob_, 80) for w_ in ('SP1 REACHED ; SP2 REACHED ; DISPATCHES 11 OF 12', 'LINES SP1 206 AGAINST 135-275, S5a-S5b 321 AGAINST 300-600', 'propext, Classical.choice, Quot.sound', 'THE ORDER OPEN AT SP2')),
        at(ob_, 80)[:60], '1')
    add('ruling (1)', 'data/b738_offlinezero.txt :77-:78, S5c-S5d re-priced at 482-2675 lines, not begun, the three objects ABSENT at the pin',
        '482-2675 lines' in at(ob_, 77) and 'NOT BEGUN' in at(ob_, 78) and 'stay ABSENT at the pin' in at(ob_, 78), at(ob_, 78)[:60], '1')
    sv_ = lines_of(p('data', 'b738_standing_v1180.txt'))
    add('ruling (1)', 'data/b738_standing_v1180.txt :123, v1.18.0, 26 cases, 26 as wanted', 'CASES 26 ; AS WANTED 26' in at(sv_, 123), at(sv_, 123)[:60], '1')
    add('ruling (1)', 'tools/standing/VERSION v1.18.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.18.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
    sc8_ = _jl('b738_scores_close.json')
    held_ = sorted(k_ for k_, v_ in sc8_.items() if v_[:1] == ['HELD'])
    add('ruling (1)', 'data/b738_scores_close.json, 7 of 8 HELD, N5 REFUTED', len(held_) == 7 and sc8_.get('N5', [''])[0] == 'REFUTED', 'HELD %s' % ' '.join(held_), '1')
    add('ruling (1), the corrigendum', 'data/b738_closing.txt :137 prints (N3) REFUTED, the record-time reading, beside the close scores` N3 HELD (a b738 record line for (2))',
        '(N3) REFUTED' in at(cl, 137) and sc8_.get('N3', [''])[0] == 'HELD', at(cl, 137)[:60], '1')
    # ### (R349)(3): the five notes by their sitting rows, each note's md5 printed; the author's passes; b727's route and its confirmation form
    import hashlib as _hl
    si6_ = lines_of(p('data', 'b736_sitting.txt'))
    for row_, kern_, rec_, n_ in K.TIER3:
        nt_ = at(si6_, n_ + 5)[len('  DRAFT WRITTEN: '):]
        add('ruling (3)(a)', 'data/b736_sitting.txt :%d, [%d] PASS, BANKED ONLY, %s Zenodo record %s, the note at :%d' % (n_, row_, kern_, rec_, n_ + 5),
            at(si6_, n_).startswith('[%d] PASS, BANKED ONLY' % row_) and at(si6_, n_ + 1).strip() == 'FILE: %s Zenodo record %s' % (kern_, rec_)
            and at(si6_, n_ + 2).strip() == 'LINE: the end of the description' and at(si6_, n_ + 5).startswith('  DRAFT WRITTEN: CURRENCY.')
            and at(si6_, n_ + 7).strip() == 'THE AUTHOR`S WORD: Pass [%d]' % row_, 'note md5 %s ; %d characters' % (_hl.md5(nt_.encode('utf-8')).hexdigest(), len(nt_)), '2')
    aa6_ = lines_of(p('data', 'b736_author_answers.txt'))
    add('ruling (head)', 'data/b736_author_answers.txt :308, Pass [104]-[107] at 2026-11-03T01:38:25Z', all('="Pass [%d]"' % r_ in at(aa6_, 308) for r_ in (104, 105, 106, 107)), at(aa6_, 308)[:50], '2')
    add('ruling (head)', 'data/b736_author_answers.txt :317, Pass [108] at 2026-11-03T01:55:33Z', '="Pass [108]"' in at(aa6_, 317), at(aa6_, 317)[:50], '2')
    aa8_ = lines_of(p('data', 'b738_author_answers.txt'))
    add('ruling (head), (6)', 'data/b738_author_answers.txt :15, the next act "Tier 3 act [104]-[108]"', '="Tier 3 act [104]-[108]"' in at(aa8_, 15), at(aa8_, 15)[:50], '0')
    qh_ = [x_ for x_ in gr('D:/relay', 'grep', '-l', '-F', 'pass 19938009', '--', 'data').split() if not x_.startswith('data/b739_')]
    add('ruling (head)', 'the quoted word "pass 19938009, 19938005, 19938003, 19931797, 21520474 as banked" found as worded in a bank before b739', bool(qh_),
        ' '.join(qh_) or 'NOT FOUND AS WORDED: the passes it stands for banked at b736 (data/b736_author_answers.txt :308, :317)', '2')
    s27_ = lines_of(p('data', 'b727_sitting.txt'))
    add('ferry (read first), ruling (3)(c)-(d)', 'data/b727_sitting.txt [13]-[19] at :114-:168, seven PASS rows, each confirmed "other metadata True, files True, record DOI version True"',
        all(at(s27_, k_).startswith('[%d] PASS' % r_) for k_, r_ in zip(range(114, 169, 9), range(13, 20)))
        and sum(1 for l in s27_[113:175] if 'read back anonymously' in l and 'other metadata True, files True, record DOI version True' in l) == 7, at(s27_, 120)[:60], '2')
    rb7_ = _jl('b727_zenodo_readback.json')
    add('ferry (read first), ruling (3)(d)', 'data/b727_zenodo_readback.json, the confirmation form, present', bool(rb7_), '%d keys' % len(rb7_), '2')
    add('ruling (3)', 'record 21520474 ([108]) is the record b727 wrote at [18] (data/b727_sitting.txt :165): its description read before the edit', 'Zenodo 21520474 read back' in at(s27_, 165), at(s27_, 165)[:60], '2')
    rr_ = lines_of(p('data', 'b675_rules.txt'))
    add('ruling (2)(ii)', 'data/b675_rules.txt :9, rules row (2), the long phase splits the next pre-run (the 450 s the post-push phases passed)', at(rr_, 9).strip().startswith("(2) A PRE-RUN'S LONG PHASE SPLITS THE NEXT ONE"), at(rr_, 9)[:60], '1')
    for f_, w_ in (('b738_checks_standing-b2c.txt', 'pre-push'), ('b738_checks_postpush_standing-b2c.txt', 'post-push')):
        add('ruling (2)(ii)', 'data/%s, b2c`s %s phase table, the control instance' % (f_, w_), os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(7) and 19 defects (data/b738_events.txt, data/b738_defects.txt)',
        starts == list(range(1, 8)) and len(letters) == 19, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b738_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    df_ = (rd(p('data', 'b738_defects.txt')) or '').replace('’', "'")
    for l_, w_ in (('m', 'sent as two parallel calls in one message'), ('p', 'carried `sed -n`')):
        add('ferry (read first)', 'data/b738_defects.txt (%s)' % l_, ("    (%s) " % l_) in df_ and w_ in df_.split("    (%s) " % l_, 1)[-1].split(NL, 1)[0], 'read', '1')
    ev_ = (rd(p('data', 'b738_events.txt')) or '').split(NL)
    for n_, w_ in ((2, 'raised IndexError'), (3, 'REFUSED BY THE HOOK (READ)'), (4, '"the sealed tools\' hashes, 85 files"'), (5, 'its act-root chain phase 493 s'),
                   (6, 'stopped by the host for low memory'), (7, 'foreground, 247 s')):
        add('ferry (read first)', 'data/b738_events.txt (%d), %s' % (n_, w_), any(l.startswith('    (%d) ' % n_) and w_ in l for l in ev_), 'read', '1')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ruling (scope)', 'zq-b730 at 602cd401, b738`s tip, not touched this act', zt_.startswith('602cd401'), zt_[:8], '3')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :13241, b738`s entry', at(fd_, 13241).startswith('## W-ORD-ZQ-OFFLINE-ZERO on R4, box A: SP1 REACHED'), at(fd_, 13241)[:50], '0')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'OPEN_TRAILS :17456, b738`s trail record', at(ot_, 17456).startswith('### b738 '), at(ot_, 17456)[:50], '0')
    add('ferry (read first)', 'OPEN_TRAILS :17502-:17506, the trail`s hand section carrying the author`s word for b739', at(ot_, 17502).startswith('### b738 — the author') and '“Tier 3 act [104]-[108]”' in at(ot_, 17506),
        at(ot_, 17506)[:50], '0')
    for row_, kern_, rec_, n_ in K.TIER3:
        add('PATHS', '%s at D:/%s ([%d], Zenodo %s), read only' % (kern_, kern_, row_, rec_), os.path.isdir('D:/%s/.git' % kern_), 'present' if os.path.isdir('D:/%s/.git' % kern_) else 'ABSENT', '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    SP6_ = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf/scratchpad'
    for z_ in ('zqwork', 'zqwork2', 'zqwork3'):
        add('PATHS, b738 closing (c)', 'the damaged clone %s in place in b736`s scratchpad, not deleted' % z_, os.path.isdir(SP6_ + '/' + z_), 'present' if os.path.isdir(SP6_ + '/' + z_) else 'ABSENT', '0')
    add('ferry', 'tools/standing/ at v1.18.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.18.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R349)(4): b738's export, the mirror's last
    add('ruling (4)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-03-b738.zip, b738`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R349)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b738-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R349)(2), (4): act_current alone, then b738's step row 22 and its closing capture, each committed alone; tools/mirror_prevbuild.json's
    # ### LF form equal to HEAD's (2d637131), nothing to commit (b738's build rewrote it with CRLF endings, its content unchanged)
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b738_steps.json'),
                   (K.STEPZERO, 'data/b738_relay_push-b738-closing_push_out.txt')):
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
    add('ferry (read first)', 'data/b739_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b739_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b739 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b738_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.18.0's controls, the build to SP1 and SP2 with its notes and dispatch rows, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R349)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R349)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: zq-b730 of SIDE-explicit-formula alone, eleven commits under (R349)(3); no main's code, no merge, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b739 ((R349)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R348)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b739 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY-FIVE, THE FRAME ACT: b738 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON FIGURES BEFORE CONTROLS AND THE SENTENCE AGAINST ITS TABLE; '
              'W-ORD-ZQ-OFFLINE-ZERO BUILT ON R4, BOX A, TO SP1 AND SP2, UNDER (R349).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b738's sections over b738's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.18.0: figures before controls at the head, the sentence against its table, the in-place edit, the delete after a clean check, the close`s order, the split, the vacuous gate, the Lean reader, each case failing before its repair and passing after', 'b739_standing_v1180.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE BUILD TO SP1 AND SP2 ((R349)(3))', [
                ('W-ORD-ZQ-OFFLINE-ZERO on R4, box A: the dispatches, the lines against the estimates, the axioms, the statements, the re-price of S5c-S5d', 'b739_offlinezero.txt'),
                ('the notes beside the plan bank, each row found wrong with its reason', 'b739_offlinezero_notes.txt'),
                ('the probe-path refusal printed before the lock gate', 'b739_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b739_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b738`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b739_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R348)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; zq-b730 from ' + WL.ZQ_ENTERING[:8] + ' to ' + WL.ZQ_TIP[:8] + ', eleven commits, every Lean file of the act on it, off main, no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: of the twelve (R349)(3)(d) allows, each read by its run id) ; the rebuild-b721 branches of the wave 1 kernels as b738 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b738-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the plan bank`s md5 printed at step zero before any Lean file, no plan row rewritten, the build bank`s controls before its figures, the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate ;',
    '    N3: SP1 and SP2 each printed REACHED with its axioms ; no sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem ; the entry`s nouns the banks` ; N5: S5c and S5d not begun ; one parallel add and commit (defect (m)) ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b739_address_scan.txt, data/b739_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the description write under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; the deposit route untouched, publish never called, the draft held at v5 ; no Zenodo description written, [104]-[108] waiting on the author`s record numbers ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the price line, the trail) written ; no paper moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY or faces page byte ; data/act_roots.txt (b739`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.18.0 by (R349)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b738 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R349)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZQ-OFFLINE-ZERO OPEN at SP2 (relay data/b739_offlinezero.txt), S5c-S5d re-priced there and not begun, the numeric hypotheses hcm and hfr open ; [104]-[108] for a Tier 3 act on the author`s record numbers ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b739_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b738 left them; push-b738-sitting on b738`s 21 kernels, local; the build clone D:/zq-b738.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on any kernel`s main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b738`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b739: the standing repairs are v1.18.0's ((R349)(2), relay data/b739_standing_v1180.txt, read in the corrigendum section); the
    # ### carry's diffs here (b739 carried at step zero before the fold; its tools since are the templates and tools/acts/b739.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, the act`s one written branch; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b738 left them; port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], K.SITTING_TIPS['SIDE-explicit-formula'], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b739's form over b739's objects (b738's form in git at b738's record tool): the corrigendum's foot and v1.18.0's controls; the build bank's foot;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1180.txt' % ACT, r'\*\*v1\.18\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.18.0`s controls')
    bd = _bfig('%s_offlinezero.txt' % ACT, r'\*\*SP1 (REACHED|NOT REACHED) ; SP2 (REACHED|NOT REACHED|NOT BEGUN) ; DISPATCHES (\d+) OF (\d+) ; LINES SP1 (\d+) AGAINST (\d+-\d+), S5a-S5b (\d+) AGAINST (\d+-\d+) ; '
               r'zq_offline_of_box AXIOMS ([^;]+?) ; THE CONTRAPOSITIVE AXIOMS ([^;]+?) ; THE ORDER OPEN AT (SP\d)\.\*\*', 'the build bank`s foot')
    rp_ = re.search(r'S5c-S5d at (\d+-\d+) \(the plan :136\): by that ratio (\d+-\d+) lines ; by the midpoint ratio ([\d.]+), (\d+-\d+)', rdn('%s_offlinezero.txt' % ACT))
    if not rp_:
        sys.exit('### THE BUILD BANK CARRIES NO RE-PRICE LINE -- NOTHING COMPOSED')
    am = []
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
                bd_sp1g=bd[0], bd_sp2g=bd[1], bd_disp=int(bd[2]), bd_max=int(bd[3]), bd_sp1=int(bd[4]), bd_sp1est=bd[5], bd_sp2=int(bd[6]), bd_sp2est=bd[7],
                bd_ax=bd[8], bd_axc=bd[9], bd_open=bd[10], rp_est=rp_.group(1), rp_ratio=rp_.group(2), rp_mid=rp_.group(3), rp_midr=rp_.group(4), amend_n=len(am),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R349)(3): the kernel rows of one kind as banked (data/b739_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R349): no lean process runs on this host; the runner dispatches those of (R349)(3), twelve at most, each read by its run id, each
    row carrying free_mb. From the command bank (the seat's commands, read live from the capture by the `commands` route) and the dispatch
    rows beside the worklist's EF_RUNS."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    free_ = [r for r in _ef_kind(rows_, 'dispatch') + _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x) for x in K.EF_RUNS) and not free_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b739_commands.json): %s; dispatch commands in the capture: %s of the %d (R349)(3)(d) allows, the worklist`s runs %d, each read by its run id: %s; dispatch and read rows without free_mb: %s (relay data/b739_dispatch_rows.json)' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', K.MAX_DISPATCHES, len(K.EF_RUNS), reads_ == sorted(str(x) for x in K.EF_RUNS), len(free_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b739's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b739_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b739_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b739_offlinezero.txt', '## THE CONTROLS', '## THE DISPATCHES'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R349): the plan bank's md5 prints before any Lean file is written and no plan row is rewritten; every figure bank opens with its
    controls; the (W) regeneration, the pre-lock comparison and the probe-path refusal print before the lock gate. The step-zero bank (the
    md5's print), v1.18.0's, the corrigendum's, the first Lean commit, SP1's bank and SP2's in that order by time; the plan bank at HEAD
    its blob at its last commit, its md5 the step zero print's; no commit of the act touching it."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (ROOT, K.C1_CORR), (K.EF_DIR, K.ZQ_FIRST), (K.EF_DIR, K.ZQ_SP1), (ROOT, K.C2_RELAY),
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
        'the plan bank`s md5 %s printed at step zero (relay %s): %s; the plan bank its md5 and its blob at %s, a commit of the act touching it: %s -- %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked: %s; the probe-path refusal banked and clear: %s; step zero, v1.18.0, the corrigendum, the first Lean commit, SP1, SP1`s bank, SP2 and SP2`s bank in that order by time: %s (%s), SP1`s bank an ancestor of SP2`s: %s; the tools` controls before their figures: %s' % (
            K.PLAN_MD5[:8], K.CITATION_BANK, md5_, K.C2_PLAN_FIRST[:8], later_ or 'NONE', same_, regen_, bool(tz), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b739's objects; b738's in git at b738's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b739_standing_v1180.txt', ('ALL AS WANTED',)), ('b739_offlinezero.txt', ('SP1 REACHED', 'SP2 REACHED', 'AXIOMS propext, Classical.choice, Quot.sound', 'THE ORDER OPEN AT SP2')),
             ('b739_corrigendum.txt', ('ITEMS',)), ('b739_citation_check.txt', ('CITES CHECKED',)), ('b739_reproduce.txt', ('REPRODUCES',)), ('b739_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R349): every stop point prints REACHED or NOT with its axiom print where reached; the entry's nouns are the banks'; no sentence says
    a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem; no comparative sentence contradicts the table it cites
    (the citation check's comparative read); the root prompt's sentences about the entry are the composer's. From the banks' last lines, the
    build bank's axiom sections, the entry's sentences and the root prompt in the answers bank (standing.rootprompt.entry_unbacked)."""
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
    sp_ = all(re.search(r'^  \S+\s+%s\s+%s \(run \d+\)$' % (n_, re.escape(ax_)), bt_, re.M) for n_ in ('zq_offline_of_box', 'zq_lambda0_split', 'zq_thetaC_tail'))
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'   # ### b738 defect (k'): "Nothing here ... locates any zero" read as a location
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|locates? (?:a|any|one|the) zero|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    nouns_ = [w_ for w_ in ('SP1', 'SP2', 'zq_offline_of_box', str(f['bd_disp']), str(f['bd_sp1']), str(f['bd_sp2']), 'data/%s_offlinezero.txt' % ACT) if w_ not in text]
    cmp_ = re.search(r'COMPARATIVE[^\n]*CONTRADICTS (\d+)', rdn(K.CITATION_BANK))
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and sp_ and not loc_ and not nouns_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; SP1`s and SP2`s terminals printed with the standard three (relay data/b739_offlinezero.txt): %s; read from %s, a sentence saying a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem: %s; the build bank`s nouns absent from the entry: %s; the citation check`s comparative line: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), sp_, src, loc_ or 'NONE', nouns_ or 'NONE', cmp_.group(0) if cmp_ else 'NO COMPARATIVE SENTENCE IN THE ACT`S BANKS READ', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R349) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R349)(5))
# ### (R349)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R349) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b738's form, carried) -- read from git,
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
    # ### (R349)(3), (5), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-explicit-formula's zq-b730 at its tip; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b738 left them; the address scan's count from its bank (relay data/b739_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b739_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b739 — lane two, act one hundred and sixty-five, the frame act under (R349): b738 at its weight and its corrigendum; v1.18.0; '
            'W-ORD-ZQ-OFFLINE-ZERO built on R4, box A, to SP1 and SP2, the order open at SP2')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form; every figure from the banks (the build bank's foot, v1.18.0's
    controls)."""
#⟪END⟫
#⟪SECTION record 31⟫
    if (f['bd_sp1g'], f['bd_sp2g']) != ('REACHED', 'REACHED') or f['bd_ax'] != 'propext, Classical.choice, Quot.sound':
        sys.exit('### THE TITLE`S FORM IS THE REACHED ONE AND THE BANK READS %s, %s, %s -- NOTHING COMPOSED' % (f['bd_sp1g'], f['bd_sp2g'], f['bd_ax']))
    return ('## W-ORD-ZQ-OFFLINE-ZERO on R4, box A: SP1 REACHED, the conditional theorem compiled with the standard three, %d lines against %s; SP2 REACHED, %d lines against %s; '
            '%d dispatches; the order OPEN at %s; the controls-before-figures render, the chain split and %d repairs landed' % (
                f['bd_sp1'], f['bd_sp1est'], f['bd_sp2'], f['bd_sp2est'], f['bd_disp'], f['bd_open'], f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) SP1’s statement read with the point’s place hc : c ∈ boxA added to the ruling’s form, the minimum modulus wanting the point inside the box (relay data/b739_offlinezero_notes.txt (1)); (2) the lattice truncation of S5b built as the box |m|, |n| ≤ 14 rather than the plan’s Q(v) ≤ N form, the box holding every Q ≤ 112 and the bound θ(cc/2) ≤ 10 taken from the functional equation, not from Bound.lean :319 (notes (5)); (3) S5a’s terminal printed under the ASCII name zq_lambda0_split, the same statement as zq_Λ₀_split, the print step refusing a non-ASCII target (defect (n)); (4) past SP1 at six dispatches, fewer than the eight (R349)(3)(b) names, S5a-S5b begun and taken to SP2 within the twelve; '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R349)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b739's objects; b738's composer in git at
    b738's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R348)(2)(v)
    e = ['', _title(), '',
         'SP1 and SP2 are REACHED on zq-b730 of SIDE-explicit-formula at %s, off main and untagged, eleven commits from b25fd82c. SP1, the conditional theorem with no numeric step, compiles as zq_offline_of_box with %s: from a point of box A where ‖zqFn‖ is below m and m a lower bound for ‖zqFn‖ on the frontier of box A, a zero of the carrier off the line; %d lines against the estimate %s. SP2, S5a and S5b, compiles: zq_lambda0_split, Λ₀ split at t = 1 into lamM s + lamM (1 − s), and zq_thetaC_tail, the lattice truncation of θ − 1 on the box |m|, |n| ≤ 14 within 1e-14 for t ≥ 1, each with the same three axioms; %d lines against %s. %d of the 12 dispatches spent, each read by its run id. The order stays OPEN at %s: the two numeric hypotheses are open, and S5c-S5d are not begun, re-priced at %s lines by S5a-S5b’s ratio. The draft stands at v5, HELD.' % (
             K.ZQ_TIP[:8], f['bd_ax'], f['bd_sp1'], f['bd_sp1est'], f['bd_sp2'], f['bd_sp2est'], f['bd_disp'], f['bd_open'], f['rp_ratio']), '',
         '*Filed at b739 on the author’s ruling `(R349)`; %d question%s put before the root. Banks: relay '
         '`data/b739_corrigendum.txt`, `data/b739_standing_v1180.txt`, `data/b739_rules.txt`, `data/b739_split_replay.txt`, `data/b739_offlinezero.txt`, `data/b739_offlinezero_notes.txt`, `data/b739_dispatch_rows.json`, `data/b739_prelock.txt`, `data/b739_pathrefusal.txt`, '
         '`data/b739_reproduce.txt`, `data/b739_address_scan.txt`, `data/b739_touch.txt`, `data/b739_standing_figures.txt`, `data/b739_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R349)(1)-(2), %s, %s, %s): b738 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b738’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b739_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b739_standing_v1180.txt), the controls-before-figures render at their head.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): the plan bank’s md5 %s printed at step zero (relay %s) before any Lean file, equal to its blob at %s, no plan row rewritten and a row found wrong noted beside it (relay data/b739_offlinezero_notes.txt); tools/standing/ v1.18.0 at %s, the weight and the corrigendum at PLACE-papers %s and their banks at %s, (2) whole before (3); the first Lean commit %s on b25fd82c; SP1 at %s and its bank at %s; SP2 at %s and its bank at %s. The build bank opens with its controls before its figures. The (W) regeneration printed in the face, and the pre-lock comparison and the probe-path refusal banked, before the lock gate (relay data/b739_prelock.txt, data/b739_pathrefusal.txt). No lean process on this host; %d dispatches, each row carrying free_mb, each read by its run id (relay data/b739_dispatch_rows.json).' % (
             K.PLAN_MD5[:8], 'data/' + K.CITATION_BANK, K.C2_PLAN_FIRST[:8], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.ZQ_FIRST[:8], K.ZQ_SP1[:8], K.C2_RELAY[:8], K.ZQ_TIP[:8], K.C3_RELAY[0][:8], f['bd_disp']), '',
         '**The build to SP1** ((R349)(3)(a), N1, N3): S1 box A with rational corners (Box.lean, 47 lines), S2 zqFn DiffContOnCl on box A (Diff.lean, 32), S3 min_modulus_zero on Complex.norm_le_of_forall_mem_frontier_norm_le (Mathlib AbsMax.lean :405) applied to the reciprocal (MinModulus.lean, 41), S4 carrier_of_box (Carrier.lean, 45) and (e) the corollary (Main.lean, 41), each group one dispatch, S1 two (its first BREAKS, 3 errors); %d lines against %s, ratio 0.749-1.526. zq_offline_of_box (c : ℂ) (hc : c ∈ boxA) (m : ℝ) (hcm : ‖zqFn c‖ < m) (hfr : ∀ z ∈ frontier boxA, m ≤ ‖zqFn z‖) : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1 / 2, printed with %s (run 41736472780); its contrapositive zq_li_not_nonneg_of_box with %s, carrying the same hypotheses. The open hypotheses are named: hcm and hfr, the numerics of S5-S6; hc the point’s place, added to the ruling’s form, which binds c over all of ℂ where the minimum modulus speaks of a point of the box (relay data/b739_offlinezero_notes.txt (1)).' % (
             f['bd_sp1'], f['bd_sp1est'], f['bd_ax'], f['bd_axc']), '',
         '**S5a-S5b to SP2** ((R349)(3)(b)): begun at six dispatches, fewer than the eight the ruling names. S5a (Split.lean, 122 lines): zqPair.Λ₀ = mellin P.f_modif split at t = 1, zq_lambda0_split (s : ℂ) : zqPair.Λ₀ s = lamM s + lamM (1 − s), lamM the Mellin transform of θ − 1 on (1, ∞), in four dispatches, two BREAKS repaired and one KERNEL whose terminal zq_Λ₀_split the print step refused as non-ASCII (defect (n)), printed at the fourth under its ASCII name. S5b (Tail.lean, 199 lines): zq_thetaC_tail, for t ≥ 1 the norm of (θ − 1) less the truncation on the box |m|, |n| ≤ 14 below 1e-14, KERNEL on its first dispatch; the box holds every Q ≤ 112 and the bound’s constant θ(cc/2) ≤ 10 comes from the functional equation at x = 2 (notes (5)). %d lines against %s, ratio 0.535-1.070; both terminals with %s. No integral is evaluated and no value of zqFn computed.' % (
             f['bd_sp2'], f['bd_sp2est'], f['bd_ax']), '',
         '**The remainder, priced again** ((R349)(3)(b)-(c)): S5c-S5d at %s lines in the plan (:136), by S5a-S5b’s ratio %s, by its midpoint ratio %s %s; not begun this act. They build the incomplete gamma function and certified elementary values with |Γ(s)|⁻¹, absent at the Mathlib pin, and SP3’s rule (stop and re-price at three times the estimate) binds the act that takes them, on the author’s word about where they are built.' % (
             f['rp_est'], f['rp_ratio'], f['rp_mid'], f['rp_midr']), '',
         '**The git writes** (N5): one git write per message across parallel calls was broken once, S5a’s add and commit on the kernel clone sent as two parallel calls in one message (defect (m)); the commit holds the two files staged and nothing else, and stands.', '',
         '**What this act is not**: no deposit, no tag, no draft published, no merge, no kernel’s main touched; every Lean file of the act on zq-b730 alone. SP1 is a conditional theorem: its two numeric hypotheses are open, and no value of zqFn is certified. Nothing here proves RH or GRH, and no zero of Z_Q0 is located in Lean.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b739_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b739_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b739_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b739 -- %s, %s, %s, %s -- against b738’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b739_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the corrigendum and the build read one way: the plan bank was read by its md5 and not rewritten, its two wrong rows noted beside it, and the build’s bank prints its controls before its figures, as (2)(i) now requires of every figure bank.', '',
         '**Carried to:** %s, (R349)(6): W-ORD-ZQ-OFFLINE-ZERO OPEN at SP2, the numeric hypotheses hcm and hfr open and S5c-S5d at their re-price, on the author’s word about where the absent objects are built; the five Zenodo currency notes [104]-[108], to a Tier 3 act on the author’s record numbers; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds, and no zero is located in Lean.*', '']
    return _title(), NL.join(e)


def _finding_text_b738():
    """b738's form over b738's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b739's objects; b738's composer in git at b738's record tool): the open-orders line written from
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
             '**(R349) ratified.** Its components as the ferry orders them (relay data/b739_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b738’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** W-ORD-ZQ-OFFLINE-ZERO (priced at OPEN_TRAILS :%d) built on R4, box A, to SP1 and SP2 on zq-b730 at %s; it stays OPEN at %s, the numeric hypotheses open and S5c-S5d not begun.' % (K.PRICE_LINE, K.ZQ_TIP[:8], f['bd_open']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b739_standing_v1180.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The build:** SP1 %s, zq_offline_of_box with %s, %d lines against %s; SP2 %s, zq_lambda0_split and zq_thetaC_tail, %d lines against %s; %d dispatches of %d; S5c-S5d re-priced at %s lines, not begun (relay data/b739_offlinezero.txt, data/b739_offlinezero_notes.txt, data/b739_dispatch_rows.json).' % (
                 f['bd_sp1g'], f['bd_ax'], f['bd_sp1'], f['bd_sp1est'], f['bd_sp2g'], f['bd_sp2'], f['bd_sp2est'], f['bd_disp'], f['bd_max'], f['rp_ratio']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b739_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b739_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b739_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b739 `%s` (previous `%s`, b738’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b739_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b739_standing_v1180.txt); the standing '
             'report tool (relay data/b739_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** zq-b730 of SIDE-explicit-formula from %s to %s, eleven commits, seven Lean files under Schema/ZQ/OffZero and print_targets.txt, off main, untagged; no kernel’s main touched; %d dispatches; the %s branches as b738 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.ZQ_ENTERING[:8], K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b739_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b738’s %s, %s, %s, %s (relay data/b739_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b739_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b738():
    """b738's trail record over b738's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: eleven of the twelve (R349)(3)(d) allows; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725 and detect-b729 kept, unmoved; zq-b730 at the build`s tip; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b738 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b730-b735`s and this act`s seven; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R349)(5): relay push-b738-closing, push-b738-preroot, push-b738-record; PLACE-papers push-b738-preroot, push-b738-record; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: seven Lean files and print_targets.txt alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R349) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (e0e37fc8) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R349)(2): FINDINGS :13167.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R349)(2): row (58).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-OFFLINE-ZERO entered at b738 (OPEN_TRAILS :17400), open at SP2.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b739_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.18.0`s controls, the split`s replay, the build bank, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the build reads b738`s plan as committed (3dab6492), no registration of its own.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none named; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: the plan is b738`s (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### seven on zq-b730 (Box, Diff, MinModulus, Carrier, Main, Split, Tail), N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R349)(2): tools/standing/ to v1.18.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b739_address_scan.txt (the address never printed).'),
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
    # ### (R349)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b739_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b739_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1180', 'split_replay', 'offlinezero', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b739_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b739_registration_%s.txt -- b739, THE FRAME ACT: b738 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.18.0; W-ORD-ZQ-OFFLINE-ZERO BUILT ON R4, BOX A, TO SP1 AND SP2 ON zq-b730; "
                             "NO DEPOSIT, NO TAG, UNDER (R349)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b738's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b739: b738's lines read banks this
act does not write, and are not carried; the lines are b739's: the build to SP1 and SP2 (KERNEL, the axioms printed), tools/standing/ v1.18.0 by
its controls (CERTIFIED), the order open at SP2 with its re-price (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b739's lines, each from the record tool's figures over b739's banks
    # ------------------------------------------------------------------ KERNEL: (R349)(3), SP1 and SP2 on zq-b730, the axioms printed
    sz = seat('%s_offlinezero.txt' % ACT, '**SP1 ')
    sk = sz   # ### (R348)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO ON R4, BOX A: SP1 %s (zq_offline_of_box, %d lines against %s), SP2 %s (zq_lambda0_split, zq_thetaC_tail, %d lines against %s), each with %s, on zq-b730 at %s; %d dispatches of %d. SOURCE %s.' % (
        f['bd_sp1g'], f['bd_sp1'], f['bd_sp1est'], f['bd_sp2g'], f['bd_sp2'], f['bd_sp2est'], f['bd_ax'], K.ZQ_TIP[:8], f['bd_disp'], f['bd_max'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.18.0 ((R349)(2)), by its controls
    sw = seat('%s_standing_v1180.txt' % ACT, '**v1.18.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.18.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the order open at SP2, its remainder re-priced, from the build bank
    so = seat('%s_offlinezero.txt' % ACT, '  S5c-S5d at ')
    keys['ORD'] = ('REGISTERED -- THE ORDER OPEN AT %s: the numeric hypotheses hcm and hfr open; S5c-S5d at %s lines in the plan, %s by S5a-S5b`s ratio, not begun. SOURCE %s.' % (
        f['bd_open'], f['rp_est'], f['rp_ratio'], so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R349)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]   # ### b739's four lines
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b739 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
