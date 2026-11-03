# -*- coding: utf-8 -*-
# b738 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R348)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R348)(2) repair it carries. Edited by the Edit tool. Carried at b738 by tools/b738_fold.py (`carry`) from tools/acts/b737.py,
# b737`s names substituted; the citation`s sections adopted from tools/b738_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b737`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b737`s carried till
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
# ### b738, Component 1 (the Edit tool): THE c1 ROUTE FOR b737'S WEIGHT LINE AND ITS CORRIGENDUM, (R348)(1)-(2). Carried from b737's
# ### override and rewritten here against b737's own banks: the closing's lines by needle, the events (9), the defects (23), the refusals
# ### (11), the v1.18.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_PREV_CLOSE = '54cd4f92'          # ### b737's closing commit
C1_REFUSAL_AT = '54cd4f92'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-03'
C1_CORRIGENDA_LAST = 57
C1_V170 = 'b738_standing_v1180.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-03 by b738 to b737’s entry (:%d), under `(R348)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-OFFLINE-ZERO planned, no build: candidate off0'
C1_TRAIL_NEEDLE = '### b737 — lane two, act one hundred and sixty-four, the plan act under (R347)'
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
    for l in _c1_rd('b737_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b737_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b737_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b737_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b737_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b737_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b737_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b737_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 7 or 'N2' in held or 'scores %d of 8 HELD' % len(held) not in head:
        sys.exit('### data/b737_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b737_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b737_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (s_r, s_p, s_s, s_c), l_st = _c1_fl('b737_sitting.txt', r'^### ### \*\*THE SITTING OF ONE KERNEL: (\d+) ROWS ; PASS (\d+) \(\[76\], \[77\], \[25\]-\[29\]\) ; STRUCK (\d+) ; CARRIED (\d+) ; WRITES: README\.md 2 \(21b6328c, db0575c6\), the description 1 ;', 'the sitting')
    pl, l_pl = _c1_fl('b737_offlinezero_plan.txt', r'^### ### \*\*THE PLAN: CANDIDATE off0 AT beta - 1/2 = (0\.4532604748), gamma = (16\.29021572) ; BOX A, MARGIN (0\.357096) SAMPLED ; (3) ROUTES PRICED \(R1, R2, R4\), R3 NOT A ROUTE ; R4 RECOMMENDED AT (1496)-(3820) LINES, (9)-(22) DISPATCHES ; (7) MATHLIB OBJECTS ABSENT ; (0) DISPATCHES THIS ACT\.\*\*$', 'the plan')
    _bx, l_bx = _c1_fl('b737_offlinezero_box.txt', r'^  ## BOX A .*: \[0\.853260, 1\.053260\] x \[16\.190216, 16\.390216\]$', 'box A')
    (va, vb), l_v = _c1_fl('b737_standing_v1170.txt', r'^### ### \*\*v1\.17\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*$', 'the v1.17.0 foot')
    _mv, l_mv = _c1_fl('b737_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz,), l_mz = _c1_fl(c, r'(mirror-refresh-2026-11-03-b737)\.zip', 'the mirror`s archive')
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 10)) or len(dr) != 23:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    return (C1_WEIGHT_HEAD + ' -- b737 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b737_closing.txt):* “%s” (data/b737_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b737_steps.json, the record and closing rows). As its rows read: `W-ORD-ZQ-OFFLINE-ZERO` PLANNED, no build (relay data/b737_offlinezero_plan.txt :%d): '
            'the candidate off0 at β − 1/2 = %s, γ = %s; box A the square [0.853260, 1.053260] × [16.190216, 16.390216] (data/b737_offlinezero_box.txt :%d), margin %s sampled; %s routes priced (R1, R2, R4), R3 not a route; '
            'R4, the minimum modulus on Complex.norm_le_of_forall_mem_frontier_norm_le (AbsMax.lean :405) applied to zqFn⁻¹, recommended at %s-%s lines and %s-%s dispatches; %s Mathlib objects absent at the pin; '
            'four stop points SP1-SP4; %s dispatches, no Lean file. The sitting of one kernel %s rows, PASS %s ([76], [77], [25]-[29]), STRUCK %s, CARRIED %s, README.md written twice and the description once at SIDE-effects main (data/b737_sitting.txt :%d). '
            'Standing tools v1.17.0, %s of %s (data/b737_standing_v1170.txt :%d); the sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), '
            'G-AXIOM-CLAIM and G-BRANCHES-BANKED declared on the face, G-RUNNER-GATE vacuous with no dispatch; SCORES %d OF 8 HELD, N2 REFUTED on defect (q), the two plan banks printing their figures before their controls, as the author accepted at the root. '
            'The root %s over %s banks, chained from %s (data/b737_act_root.json; :%d); the mirror %s at %s (data/b737_mirror_verify.txt :%d; :%d); %s prompts banked as put by the seat (:%d); %d events in data/b737_events.txt, rows (1)-(%d); %d defects, (a)–(w) '
            '(data/b737_defects.txt). The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'The draft at v5; nothing deposited, no Zenodo description edited; the corrigendum for these rows follows, under `(R348)`(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, l_pl, pl[0], pl[1], l_bx, pl[2], pl[3], '{:,}'.format(int(pl[4])), '{:,}'.format(int(pl[5])), pl[6], pl[7], pl[8], pl[9],
                s_r, s_p, s_s, s_c, l_st, vb, va, l_v, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                len(held), K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, l_mv, l_mz, np_, l_an, len(ev), max(ev), len(dr),
                cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b737's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '14:28:39Z', 'defect (b)'), (2, 'READ', '14:28:39Z', 'defect (b)'), (3, 'READ', '14:29:14Z', 'defect (b)'), (4, 'ORDER', '14:32:32Z', 'defect (d)'), (5, 'PIPE', '14:46:26Z', 'defect (j)'),
               (6, 'READ', '14:50:10Z', 'defect (k)'), (7, 'READ', '14:51:39Z', 'defect (k)'), (8, 'READ', '15:33:20Z', 'defect (m)'), (9, 'PIPE', '15:38:24Z', 'defect (p)'), (10, 'REDIR', '16:07:30Z', 'defect (s)'),
               (11, 'PIPE', '20:01:09Z', 'event (8)')]
C1_UNROWED = []
C1_CORR_TITLE = ('## Corrigendum to b737’s record (relay data/b737_events.txt rows (1)-(9) and data/b737_defects.txt): nine events and twenty-three defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the figures before their controls at its head; the sentence against its own table, the in-place edit, the delete before the check, the dry route after the lock, the long chain phases, the vacuous runner gate, '
                 'at tools/standing/ v1.18.0, each controlled, under (R348)(2)')


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
    rl = _c1_git('show', '%s:data/b737_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b737_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.18.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(9)', sorted(ev) == list(range(1, 10))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 23', len(dr) == 23), ('the refusals 11, each answered as listed', len(rl) == 11 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.18.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.18.0
C1_EV_EXTRA = {1: '; repair (order); rule (5) of data/b738_rules.txt, a REPEAT of (R346)(3)(vi)', 2: '; repair (split); rule (6)', 5: '; repair (split); rule (6)', 7: '; repair (split); rule (6)', 9: '; repair (split); rule (6)'}
C1_DF_EXTRA = {'d': '; repair (deletes); rule (4) of data/b738_rules.txt', 'q': '; repair (figbank); rule (1) of data/b738_rules.txt; N2 REFUTED on it',
               'u': '; repair (inplace); rule (3) of data/b738_rules.txt', 'v': '; repair (comparative); rule (2) of data/b738_rules.txt'}
C1_REFUSED_LATE = None
C1_NOTES = ('Dated note, b738, to the counter (`(R348)`(1)): the ruling’s “CLAIM 4, CLOSE 28, REPEAT 17 of 32” is relay data/b737_closing.txt :5, over the nine events and the twenty-three defects together; over the defects alone the tags give CLAIM 4, CLOSE 19, REPEAT 12 of 23. Both read from the same tags; this entry prints both and edits neither.',
            'Dated note, b738, to b737’s defect (r): the (W) regeneration’s reach, “carried to the next standing version” there, is not among `(R348)`(2)’s repairs and v1.18.0 does not repair it; it stays carried.',
            'Dated note, b738, to b737’s defect (h): the third pack loss has no repair in `(R348)`(2); zqwork, zqwork2 and zqwork3 stand in place and no figure of b738 rests on a read of any of them.')
C1_CLASSES = (
    ('figbank', 'figures before their controls (`(R348)`(2)(i), defect (q); CLOSE ; NEW)', 'rule (1) of data/b738_rules.txt; tools/standing/figbank.py reads a bank’s order and its writer refuses a figure bank whose controls block is absent or follows its figures, writing nothing. b737’s two plan banks, data/b737_offlinezero_criteria.txt and data/b737_offlinezero_box.txt, replayed: no reader before, REFUSED after (the first figure at :6 and :5, no controls block); b736’s sitting bank holds, no figure line'),
    ('comparative', 'the sentence against its own table (`(R348)`(2)(ii), defect (v); CLAIM ; NEW)', 'rule (2) of data/b738_rules.txt; the citation check reads each comparative sentence an act names against the table it cites and prints AGREES or CONTRADICTS, a CONTRADICTS or an unread word halting the check. The plan’s :23 “trails off12” replayed: no read before, CONTRADICTS after (off0 0.57396, off12 0.50702); `(R347)`(3)(a)’s “at the lowest height” AGREES on b725’s 69 rows'),
    ('inplace', 'the in-place edit by the shell (`(R348)`(2)(iii), defect (u); CLOSE ; REPEAT of class (18))', 'rule (3) of data/b738_rules.txt; the hook refuses sed and perl with -i or --in-place, and Set-Content, Add-Content and Clear-Content, kind INPLACE. b737’s 16:08:45Z `sed -i` replayed: passed before, INPLACE after; Set-Content read first as REDIR, its earlier kind'),
    ('deletes', 'the branch delete before the citation check (`(R348)`(2)(iv), defect (d); CLOSE ; NEW)', 'rule (4) of data/b738_rules.txt; the citation check banks `clean`, and the hook’s ORDER and tools/standing/deletes.py each refuse a delete until it stands CLEAN. A check banked HALTED, in a constructed relay: let the delete by before, held after; b737’s 14:32Z order, the delete before any check, held by both, a guard'),
    ('order', 'the dry route after the lock (`(R348)`(2)(v), event (1); CLOSE ; NEW)', 'rule (5) of data/b738_rules.txt; a close step before the lock [6] refuses, writing nothing, once data/<act>_lockgate.json stands. b737’s 17:22:02Z `record rootdry` replayed: the step guard before did not read the lock, the membrane refusing alone; REFUSED by the step after; a step before the lock runs'),
    ('split', 'the long chain phases (`(R348)`(2)(vi), events (2), (5), (7), (9); CLOSE ; (2) NEW, the three after it REPEAT of b737 (2) and (4))', 'rule (6) of data/b738_rules.txt; under b675’s rules row (2) the suite runs ten parts: standing-a in two (G-NO-SORRY-MAIN’s first half banked, then joined) and the chain’s first half in four quarters. The four phases over 450 s (471, 656, 462, 456 s) replayed under the new parts at 119, 201, 155, 165, 183 and 249 s, the longest 249 (data/b738_split_replay.txt); the pre-lock comparison reads each act by its own parts'),
    ('vacuous', 'G-RUNNER-GATE with no dispatch (`(R348)`(2)(vii), b736, b737; CLOSE)', 'rule (7) of data/b738_rules.txt, the rule written; the arm prints VACUOUS by name and is counted neither way, b737’s combined bank naming it on its VACUOUS line. A guard: no failing side'),
    ('leanpath', 'the Lean-path reader (`(R348)`(2)(viii), b738’s step-zero defect (e))', 'rule (8) of data/b738_rules.txt; the reader’s window ends at a closed parenthesis and cites the nearest identifier, Mathlib at its pin among the trees. The ruling’s paths replayed: 4 halts before, 0 after; v1.12.0’s control 5 of 5; tools/standing/VERSION v1.18.0'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b737’s events bank (relay data/b737_events.txt) carries nine rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-three lettered rows, (a)-(w), each tagged in its own bracket (%s); its refusal bank eleven lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R348)`(2), at tools/standing/ v1.18.0, each with a control on b737’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b737’s events (1)-(9):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE SCORE|THE RUNNER|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at )?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( put and \d\d:\d\dZ answered)?( from [^:]*)?|post-push|pre-push and post-push)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b737_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b737’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b737_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b737’s refusals** (relay data/b737_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (nine events, twenty-three defects), as b737’s closing prints it (relay data/b737_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b738 on the author’s ruling `(R348)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b738.py) from '
          'b737’s events and defects banks read unedited, its refusal bank, and the v1.18.0 controls bank; banked as relay `data/b738_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b737’s record; no sealed tool, face, trail or root-named bank of b737 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b738 -- THE CORRIGENDUM FOR b737, (R348)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b737_events.txt rows (1)-(9), data/b737_defects.txt 23 rows, data/b737_hook_refusals.txt 11 '
             'lines at %s; data/%s (the v1.18.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 9, DEFECTS 23 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.18.0: FIGURES BEFORE CONTROLS, THE SENTENCE AGAINST ITS TABLE, THE IN-PLACE EDIT, THE DELETE AFTER A CLEAN CHECK, '
               'THE CLOSE`S ORDER, THE SPLIT, THE VACUOUS GATE, THE LEAN READER ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b737 at its weight after its entry, and the corrigendum for b737, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.18.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b738, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b738 ran three
# ### ((R348)(4)(iii)-(iv), N1), rowed in data/b738_dispatch_rows.json. Replaced for b738 alone; the arms' names stand, their plants on b738's rows.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R347)(7), as b737 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R348)(3), N1, b738: two print dispatches allowed, none made; no row and no run; VACUOUS on the read of a run, the plant a planted row refused."""
    rows = S['drows'] or []
    return not rows and not K.EF_RUNS and K.MAX_DISPATCHES == 2
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b738: no push, the print ran at the branch's standing tip
#⟪END⟫
# ### b738, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R348)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit by (R348)(2)(iii), naming tools/standing/hook.py, edited this act by v1.17.0`s commit alone (its blob at b3bad7b6 the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b738, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b737's record has twelve
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 11)) \
#⟪END⟫
# ### b738, Component 4 (the Edit tool): b738's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b737's override of checks 526 -- no registration commit -- removed: b738
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b738_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b738, Component 6 (the Edit tool): b738's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b737's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b738, Component 4 (the Edit tool): b737's overrides of checks 1516 and 1659 (hook.py edited by b737's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b738 as it stands
# ### b738, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b738_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b738, Component 4 (the Edit tool): b737's override of checks 1476-1482 (one ERRATA entry at b737's (R347)(5)) removed -- (R348)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b738 as it stands
# ### b738, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b737's step-zero wording; b738's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked:' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b738, Component 4 (the Edit tool): G-RUNNER-READ's plant on b738's dispatch rows -- run 2's axiom lines carrying sorryAx (b737's
# ### plant read the lv rows' closure log, which b738 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b738, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b738, Component 6 (the Edit tool): the fold bank was b737's own route
# ### (tools/b737_fold.py); b738's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b738_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b737.py -> tools/acts/b738.py' in (rd('b738_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b738, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b738_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b738, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b738_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b738_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b738, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R348): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    rows = [l for n_ in ('b738_defects.txt', 'b738_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R348) Component 5, the act`s events and defects together; relay data/b738_defects.txt, data/b738_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b738, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b738's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-OFFLINE-ZERO priced at b738 and open,',
    '        and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b738, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b737's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b738_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b738_registration_%s.txt' % __import__('b738_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b738, Component 4 (the Edit tool, before the face): b737's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b738, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b738's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b738, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R348)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b738 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b738_ef\.py dispatch\b', re.M)   # ### b738: the build's one route
#⟪END⟫
# ### b738, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b737's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b738 scorer reads; the needles set to the banks b738's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b738, (R348)(2)(iii): b737's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b738, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b738_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrstuvw')))   # ### (a)-(w), entered before the lock, every one the seat's (data/b738_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b738_corrigendum.txt', 'data/b738_standing_v1170.txt', 'data/b738_offlinezero_plan.txt', 'data/b738_offlinezero_criteria.txt', 'data/b738_offlinezero_box.txt',
                  'data/b738_sitting.txt', 'data/b738_amendments.json', 'data/b738_pathrefusal.txt',
                  'data/b738_reproduce.txt', 'data/b738_reproduce.json', 'data/b738_address_scan.txt', 'data/b738_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b738 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R348)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b738_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _sitting_rows(t):
    """(R348)(4): the sitting bank's rows by number -- a row opens `[n] STATE` at column 0, its fields indented two spaces as `KEY: value`;
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
        # ### (R348)(2)-(4) (b738's keys over b738's objects): the order by time and ancestry; v1.17.0's controls; the plan, its prints and the price line;
        # ### the sitting of one kernel; the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.C2_RELAY, K.PLAN_BANK))) or None, _s(blob(ROOT, 'HEAD:' + K.PLAN_BANK)) or None),   # ### the plan at its last commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_plan', K.C1_CORR, K.C2_PLAN_FIRST),
                                 ('plan_last', K.C2_PLAN_FIRST, K.C2_RELAY), ('plan_sitting', K.C2_RELAY, K.C3_RELAY[0]))),
        v1130=rd('b738_standing_v1170.txt'), plan=rd('b738_offlinezero_plan.txt'), print_=rd('b738_sitting.txt'), rows_bank=rd('b738_offlinezero_plan.txt'),
        sittingj=_sitting_rows(rd('b738_sitting.txt')), amendj=jl('b738_amendments.json'),
        plan_first_files=files_of(ROOT, K.C2_PLAN_FIRST), plan_files=files_of(ROOT, K.C2_RELAY), price_files=files_of(PP, K.C2_PP),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        sit_files=dict((k_, gs('D:/' + k_, 'diff', '--name-only', K.SITTING_BASE, K.SITTING_TIPS[k_]).split()) for k_ in K.SITTING_TIPS),
        sit_main=dict((k_, gs('D:/' + k_, 'rev-parse', 'refs/heads/main').strip()) for k_ in K.SITTING_TIPS),
        sit_origin=dict((k_, gs('D:/' + k_, 'rev-parse', 'refs/remotes/origin/main').strip()) for k_ in K.SITTING_TIPS),
        sit_log=dict((k_, [l for l in gs('D:/' + k_, 'rev-list', '--reverse', '%s..%s' % (K.SITTING_BASE, K.SITTING_TIPS[k_])).split() if l.strip()]) for k_ in K.SITTING_TIPS),
        sit_tags=dict((k_, [t for t in gs('D:/' + k_, 'tag', '--contains', K.SITTING_COMMITS[0]).split(NL) if t.strip()]) for k_ in K.SITTING_TIPS),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b738_dispatch_rows.json') or '[]'), reproduce=rd('b738_reproduce.txt'), reproducej=jl('b738_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b738_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b737 left them
        rebuild=None, rebuild_rows=json.loads(rd('b738_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               print=_ct(ROOT, K.PRINT_COMMIT), plan=_ct(ROOT, K.C2_PLAN_FIRST), price=_ct(PP, K.C2_PP), first_item=_ct('D:/SIDE-effects', K.SITTING_COMMITS[0]),
               second_item=_ct('D:/SIDE-effects', K.SITTING_COMMITS[1]), sitting=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.PRINT_COMMIT),
                   count=files_of(ROOT, K.C2_PLAN_FIRST), sitting=files_of(ROOT, K.C3_RELAY[0]), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b738's read-first bank's items by path, as its step zero wrote them (data/b738_readfirst.txt)
READFIRST_NEEDLES = ('relay data/b737_closing.txt |', 'relay data/b737_events.txt |', 'relay data/b737_defects.txt |', 'relay data/b737_sitting.txt |', 'relay data/b725_interference.txt |',
                     'relay data/b725_registration_2026-10-30.txt |', 'relay data/b730_continuation_plan.txt |', 'relay data/b730_continuation.txt |', 'relay data/b731_price_measured.txt |',
                     'relay data/b735_explicitformula.txt |', 'PLACE-papers OPEN_TRAILS.md |', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/ZQ/EF/Main.lean |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R348)(1)-(2))', 'PLAN AND THE SITTING ((R348)(3)-(4))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (77 = 77 + 0, data/b738_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 77 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b737's figures, read at FINDINGS :13031 as Component 1 landed them
    return landed(S, 0, ['b737 AT ITS WEIGHT', 'suite 113 of 116', 'relay 68e793fa', '38 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b738's title in the ferry's Component 3 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-ZQ-OFFLINE-ZERO planned, no build: candidate off0 at β − 1/2 = 0.4532604748, γ = 16.29021572; ', ' routes priced, R4 recommended at ', ' Mathlib objects absent; [76], [77] passed at SIDE-effects main; ', 'the amendment regeneration and ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R348)(1)-(2): the generated entry for b737's ten events and thirty-eight defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(10), the defects by the one lettering; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 7, CLOSE 41 over 48, REPEAT 22); the repairs at tools/standing/ v1.17.0 by their controls
    bank; the corrigenda bank appended at row (57) and nothing before it changed; in Component 1's commits (the figures read from
    data/b738_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 38 and len(items) == j.get('items') == 48 and j.get('row') == 57 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 48 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 7 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 22 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.17.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 3 \
        and '  (57) ' in S['corrigenda'] and '  (58) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules bank data/b738_rules.txt carries (R348)(2)'s eight rules, in v1.17.0's commit; data/b738_rules.txt (by form in (R348)(5)'s (W)) is
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b737's form, its names b738's); no author's word of b738 orders a row of the next act's, so that bank does not exist."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and '(1) THE AMENDMENT ROW' in r1 and '(8) THE VERSION' in r1 and 'data/b738_rules.txt' in S['files']['standing'] \
        and not os.path.exists(os.path.join(D, 'b738_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b738's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO PLANNED', 'CERTIFIED -- tools/standing/ v1.17.0', 'REGISTERED -- THE PLAN',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b738: no dispatch this act -- no dispatch command in the capture, no row; VACUOUS on every row's read; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### N1: no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b738_ef\.py"? dispatch\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 2
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b738, N1: no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
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
# ### b738's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The candidate**', '**The box and the routes**', '**The price and the recommendation**',
                 '**The consequence, priced and not stated**', '**The sitting of one kernel**', '**The amendment rows**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b738_corrigendum.txt', 'data/b738_standing_v1170.txt', 'data/b738_offlinezero_plan.txt', 'data/b738_sitting.txt', 'data/b738_amendments.json',
                 'data/b738_reproduce.txt', 'data/b738_address_scan.txt', 'data/b738_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b738: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R348)(3), N2 (the name the frozen run list carries): the plan bank commits with the prints it cites (the criteria and the box banks
    in its first commit, none later), after v1.17.0's and the corrigendum's commits and before the sitting's bank, in that order by time and
    by ancestry within the relay; the plan at HEAD its text at its last commit, the prints at HEAD their blobs at the first; the earlier acts'
    registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('standing', 'corr', 'plan', 'print', 'sitting')
    prints_ = ('data/b738_offlinezero_criteria.txt', 'data/b738_offlinezero_box.txt')
    return all(p_ in S['plan_first_files'] for p_ in prints_ + (K.PLAN_BANK,)) and K.PLAN_BANK in S['plan_files'] and bool(reg) and reg == head \
        and not [p_ for p_ in prints_ if p_ in S['plan_files']] \
        and all(_s(blob(ROOT, '%s:%s' % (K.C2_PLAN_FIRST, p_))) == _s(blob(ROOT, 'HEAD:' + p_)) for p_ in prints_) \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b738_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    the kernels the sitting wrote; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R348)(2)-(5), N2 (the name the frozen run list carries): (2) whole before (3) -- v1.17.0, the weight and corrigendum on PLACE-papers
    and the corrigendum banks before the plan's first commit; the price line on PLACE-papers by a commit of its own, OPEN_TRAILS alone, after
    the plan's first commit; the two SIDE-effects writes after the plan's last commit and before the sitting's bank, by the commits' times."""
    t_ = S['t']
    return K.REGISTRATIONS in S['files']['reg'] and all(t_.get(k_) for k_ in ('c1pp', 'c1', 'standing', 'plan', 'price', 'print', 'first_item', 'second_item', 'sitting')) \
        and max(t_['standing'], t_['c1pp'], t_['c1']) < t_['plan'] < t_['price'] and t_['plan'] <= t_['print'] < t_['first_item'] < t_['second_item'] < t_['sitting'] \
        and S['price_files'] == ['OPEN_TRAILS.md'] and S['anc'].get('corr_plan') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R348)(4), N3 (the name the frozen run list carries): the sitting of one kernel -- [76], [77] and [25]-[29] each a row of the sitting's
    bank with the author's word and its time beside it, no other row; no PASS without its confirmation; the writes README.md twice
    (21b6328c, [76]; db0575c6, [28]) and the description once ([77]); the bank's foot the rows'; [28]'s words verbatim; the amendment rows
    the words of [76] and [28], each in the sitting's row by its time."""
    R = S['sittingj'] or {}
    want = ['76', '77', '25', '26', '27', '28', '29']
    miss = [k for k in want if k not in R or not (R[k].get('word') or '').strip() or not (R[k].get('at') or '').strip()]
    st = lambda k: (R.get(k) or {}).get('state') or ''
    v = _vlast(S['print_'] or '')
    am = (S['amendj'] or {}).get('rows') or []
    return not miss and sorted(R) == sorted(want) and all(st(k).startswith('PASS') for k in want) \
        and all(r.get('confirm') for r in R.values()) \
        and (R['76'].get('confirm') or '').startswith('SIDE-effects ' + K.SITTING_COMMITS[0]) and (R['28'].get('confirm') or '').startswith('SIDE-effects ' + K.SITTING_COMMITS[1]) \
        and (R['77'].get('confirm') or '').startswith('gh read back') \
        and 'THE SITTING OF ONE KERNEL: 7 ROWS ; PASS 7' in v and 'STRUCK 0 ; CARRIED 0' in v \
        and R['28'].get('word', '').startswith('Pass [28] with one write: at main :50 and :57, “Genuine content, 0 sorry.” becomes “0 sorry at 78bbcff.”') \
        and len(am) == 2 and all(any(a.get('words') == r.get('word') and a.get('at') == r.get('at') for r in R.values()) for a in am)
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip locally and at origin; zq-b730's diff against its entering tip empty, no Lean file this act;
    SIDE-effects, the one kernel (4) names, at its main's tip locally and at origin, its two commits since 78bbcff the sitting's, its diff README.md alone, no tag on either."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and not S['zq_files'] and sorted(K.SITTING_TIPS) == ['SIDE-effects'] \
        and all(S['sit_files'].get(k_) == ['README.md'] and S['sit_main'].get(k_, '').startswith(h_) and S['sit_origin'].get(k_) == S['sit_main'].get(k_)
                and S['sit_log'].get(k_) == list(K.SITTING_COMMITS) and not S['sit_tags'].get(k_) for k_, h_ in K.SITTING_TIPS.items())

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.17.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b737's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R348)(3), N2, N3 (the name the frozen run list carries): the plan bank's foot -- the candidate off0, box A, three routes priced, R3 not
    a route, R4 recommended at its lines and dispatches, seven Mathlib objects absent, no dispatch; its (a)-(e) present, the criteria
    printed before the candidate's name; the price line in OPEN_TRAILS at :17400, planned and not built; no sentence of the plan, its prints
    or the price line a location or a failure stated as a theorem."""
    n_ = S['rows_bank'] or ''
    v = _vlast(n_)
    heads = [h for h in ('## (a) ', '## (b) ', '## (c) ', '## (d) ', '## (e) ') if h in n_]
    a_ = n_.find('## (a) ')
    crit_first = a_ >= 0 and 0 <= n_.find('  criterion ', a_) < n_.find('  the nearest other zero of Z_Q0', a_) < n_.find('THE CANDIDATE: off0', a_)
    pl = [l for l in (S['ot'] or '').split(NL) if l.startswith('**`W-ORD-ZQ-OFFLINE-ZERO` PRICED at b738, `(R348)`(3), planned and not built:**')]
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'
    sents = [s_ for t_ in (n_, rd('b738_offlinezero_criteria.txt') or '', rd('b738_offlinezero_box.txt') or '') + tuple(pl) for s_ in re.split(r'(?<=[.;])\s+', t_)]
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    return v.startswith('THE PLAN: CANDIDATE off0 AT beta - 1/2 = 0.4532604748, gamma = 16.29021572') and '3 ROUTES PRICED (R1, R2, R4), R3 NOT A ROUTE' in v \
        and 'R4 RECOMMENDED AT 1496-3820 LINES, 9-22 DISPATCHES' in v and '7 MATHLIB OBJECTS ABSENT' in v and '0 DISPATCHES THIS ACT' in v \
        and len(heads) == 5 and crit_first and len(pl) == 1 and oline(S, K.PRICE_LINE) == pl[0] and not loc_


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
    """standing clauses v9 (Component 7 of (R348): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b738_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b737's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R348-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b737's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R348) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b737's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R347)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 77 = 77 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b737-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 form: W-ORD-ZQ-OFFLINE-ZERO planned, no build, the candidate off0 with its figures, the routes priced and R4 recommended with its lines, dispatches and absent objects, [76] and [77] passed at SIDE-effects main, the amendment regeneration and the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R348)(1)-(2): the generated corrigendum for b737`s record, landed at FINDINGS :13033: its ten events and thirty-eight defects, 48 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 7 CLOSE 41, REPEAT 22; v1.17.0`s repairs by data/b738_standing_v1170.txt; the corrigenda bank appended at row (57)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); data/b738_rules.txt carrying (R348)(2)`s eight rules in v1.17.0`s commit, no data/b738_rules.txt',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b738's objects
    ('G-REGISTRATIONS-FIRST', '(R348)(3), N2: the plan bank`s first commit carrying the criteria and box prints it cites, none later; v1.17.0`s, the corrigendum`s, the plan`s, its second and the sitting bank`s in that order by time and ancestry; the plan at HEAD its text at 3dab6492, the prints at 310a681f; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(plan_sitting=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b738_address_scan.py run live over every commit of the act in the relay, PLACE-papers and the kernels the sitting wrote, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R348)(2)-(5), N2: (2) whole before (3) -- v1.17.0, the weight and corrigendum and their banks before the plan`s first commit; the price line by a commit of its own, OPEN_TRAILS alone, after it; the two SIDE-effects writes after the plan`s last commit and before the sitting`s bank',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_plan=False))),
    ('G-DERIVATION-GRADED', '(R348)(4), N3: the sitting of one kernel -- [76], [77], [25]-[29] each a row with the author`s word and its time, PASS 7, no other row; [76]`s write 21b6328c, [28]`s db0575c6, [77] read back by gh; the foot the rows`; [28]`s words verbatim; the two amendment rows the words of [76] and [28]',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'sittingj', lambda d: d.pop('28', None))),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against its entering tip empty, no Lean file this act; SIDE-effects at db0575c6 locally and at origin, its two commits since 78bbcff the sitting`s, README.md alone, no tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 58f2c295, VERSION 9; v8 at HEAD its blob at 58f2c295; no v10; v9`s commit an ancestor of v1.17.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R348)(3), N2, N3: the plan bank`s foot -- candidate off0, three routes priced, R3 not a route, R4 at 1496-3820 lines and 9-22 dispatches, 7 Mathlib objects absent, 0 dispatches; (a)-(e) present, the criteria before the name; the price line at OPEN_TRAILS :17400; no sentence a location',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'rows_bank', (S['rows_bank'] or '').replace('R4 RECOMMENDED AT', 'R1 RECOMMENDED AT'))),
    ('G-DIFFERS-ERRATA', '(R348): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 9842f1d3, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b738_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R348-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b737`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 58f2c295 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: two print dispatches allowed by (R348)(3), none made, no row and no run; VACUOUS on the rows` read, the plant a planted dispatch refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture and no row, the order and memory reads VACUOUS; no b721-b738 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b737 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b737`s [41] tip; the join kernel`s main and its one tag v0.1.0; SIDE-effects` two README commits read at G-OFFSET-POST-HOC',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers, FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b737`s trail record on OPEN_TRAILS (:17341) and its root in the chain', lambda S: '### b737 — lane two, act one hundred and sixty-three, the second sitting under (R347)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers, FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b737`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b738, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R348)(3): a main at its sitting tip, its tags unmoved, is not a move against b737's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b738: (R348)'s rows. (1)'s line read by the ruling from the public relay at 54cd4f92
    pub = _blob('D:/relay', '54cd4f92', 'data/b737_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b737_closing.txt :1, the head line as the public relay carries it at 54cd4f92', bool(pub) and pub[0] == at(cl, 1) and 'relay b87c1e24' in pub[0] and 'PLACE-papers e0e37fc' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 113 of 116', 'root 706d369cad76e1fd', '9 prompts answered', 'scores 7 of 8 HELD', '23 defects'):
        add('ruling (1)', 'data/b737_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'the closing`s counter CLAIM 4, CLOSE 28, REPEAT 17 OF 32 (events and defects), data/b737_closing.txt :5',
        'CLAIM 4, CLOSE 28, REPEAT 17 OF 32' in at(cl, 5), at(cl, 5)[-40:], '1')
    dfl_ = [l for l in lines_of(p('data', 'b737_defects.txt')) if re.match(r"^    \([a-z]'?\) ", l)]
    tg_ = (sum(1 for l in dfl_ if '[CLAIM' in l), sum(1 for l in dfl_ if '[CLOSE' in l), sum(1 for l in dfl_ if '; REPEAT' in l), len(dfl_))
    add('ruling (1)', 'data/b737_defects.txt, the defects alone CLAIM 4, CLOSE 19, REPEAT 12 of 23', tg_ == (4, 19, 12, 23), 'CLAIM %d CLOSE %d REPEAT %d OF %d' % tg_, '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b737']]
    add('ruling (1)', 'data/act_roots.txt, b737`s root 706d369c chained from b736`s 0c6cc62f', len(ar8_) == 1 and ar8_[0][1].startswith('706d369c') and ar8_[0][2].startswith('0c6cc62f'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b737_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b737 (b737`s post-push part b3)', 'b737 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b737 AGREE' if 'b737 AGREE' in b3_ else 'ABSENT', '1')
    pl_ = lines_of(p('data', 'b737_offlinezero_plan.txt'))
    add('ruling (1)', 'data/b737_offlinezero_plan.txt :148, off0 at 0.4532604748 / 16.29021572, R4 at 1496-3820 lines, 9-22 dispatches, 7 objects absent, 0 dispatches',
        all(w_ in at(pl_, 148) for w_ in ('0.4532604748', '16.29021572', 'R3 NOT A ROUTE', '1496-3820 LINES', '9-22 DISPATCHES', '7 MATHLIB OBJECTS ABSENT', '0 DISPATCHES THIS ACT')), at(pl_, 148)[:60], '1')
    bx_ = lines_of(p('data', 'b737_offlinezero_box.txt'))
    add('ruling (1)', 'data/b737_offlinezero_box.txt :5, box A [0.853260, 1.053260] x [16.190216, 16.390216]', '[0.853260, 1.053260] x [16.190216, 16.390216]' in at(bx_, 5), at(bx_, 5)[:60], '1')
    add('ruling (1)', 'data/b737_offlinezero_box.txt :9, the margin 0.357096 sampled', '0.357096 (THE MARGIN, sampled)' in at(bx_, 9), at(bx_, 9)[:60], '1')
    si_ = lines_of(p('data', 'b737_sitting.txt'))
    add('ruling (1)', 'data/b737_sitting.txt :95, 7 rows, PASS 7, README.md 2 writes, the description 1', 'PASS 7' in at(si_, 95) and 'README.md 2' in at(si_, 95) and 'the description 1' in at(si_, 95), at(si_, 95)[:60], '1')
    sv_ = lines_of(p('data', 'b737_standing_v1170.txt'))
    add('ruling (1)', 'data/b737_standing_v1170.txt :110, v1.17.0, 25 cases, 25 as wanted', 'CASES 25 ; AS WANTED 25' in at(sv_, 110), at(sv_, 110)[:60], '1')
    add('ruling (1)', 'tools/standing/VERSION v1.17.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.17.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
    # ### (R348)(3): the plan bank's md5 printed, the working bytes against the plan's last commit (3dab6492): no plan row rewritten
    import hashlib as _hl
    pw_ = open(p('data', 'b737_offlinezero_plan.txt'), 'rb').read() if os.path.exists(p('data', 'b737_offlinezero_plan.txt')) else b''
    pc_ = _blob('D:/relay', '3dab6492', 'data/b737_offlinezero_plan.txt').encode('utf-8')
    add('ruling (3)', 'data/b737_offlinezero_plan.txt, its md5 %s, as committed at 3dab6492' % _hl.md5(pw_).hexdigest(), bool(pw_) and pw_ == pc_,
        'md5 %s ; %d lines' % (_hl.md5(pw_).hexdigest(), len(pl_)), '1')
    # ### (R348)(2)(ii), (4): THE COMPARATIVE-SENTENCE READ at step zero, the seat's, on the two control instances the ruling names, before
    # ### Component 1 lands the reader in tools/standing/; each sentence against the table it cites, AGREES or CONTRADICTS printed
    def _cmp(word, mine, other):
        lead = mine > other
        return 'AGREES' if (word == 'leads') == lead else 'CONTRADICTS'
    z_ = [float(x_) for x_ in at(pl_, 16).split()[-3:]]
    l_ = [float(x_) for x_ in at(pl_, 17).split()[-3:]]
    v1_ = _cmp('trails', z_[0], z_[1])
    add('ruling (2)(ii)', 'data/b737_offlinezero_plan.txt :23, "it trails off12 on the distance to zeta_K`s zeros" against its table :16 (%s against %s): %s, the control wanting CONTRADICTS' % (z_[0], z_[1], v1_),
        'trails off12 on the distance to zeta_K' in at(pl_, 23) and v1_ == 'CONTRADICTS', v1_, '1')
    v2_ = _cmp('trails', l_[0], l_[1])
    add('ruling (2)(ii)', 'data/b737_offlinezero_plan.txt :23-:24, "and off12 on the distance to L(psi)`s" against its table :17 (%s against %s): %s' % (l_[0], l_[1], v2_),
        'off12 on the distance to L(psi)' in at(pl_, 24) and v2_ == 'AGREES', v2_, '1')
    in_ = lines_of(p('data', 'b725_interference.txt'))
    rows_ = [l.split() for l in in_[31:] if re.match(r'^  off\d+ ', l)]
    low_ = min(rows_, key=lambda r_: float(r_[2])) if rows_ else ['']
    fr_ = rd(p('data', 'b737_ferry.txt')) or ''
    v3_ = 'AGREES' if low_[0] == 'off0' else 'CONTRADICTS'
    add('ruling (2)(ii)', '(R347)(3)(a), "the lowest", against data/b725_interference.txt :32-, the least gamma of %d off-line rows %s: %s, the control wanting AGREES' % (len(rows_), low_[0], v3_),
        'the order\'s phrase "the lowest"' in fr_ and len(rows_) == 69 and v3_ == 'AGREES', v3_, '1')
    ef_ = lines_of(p('data', 'b735_explicitformula.txt'))
    add('ferry (read first)', 'data/b735_explicitformula.txt :184-:185, zq_li_nonneg_imp_online_instance an implication', 'zq_li_nonneg_imp_online_instance' in at(ef_, 184) and 'ρ.re = 1 / 2' in at(ef_, 185), at(ef_, 185)[:60], '1')
    pm_ = lines_of(p('data', 'b731_price_measured.txt'))
    add('ferry (read first)', 'data/b731_price_measured.txt :17-:19, 835 / 786 / 340 measured', '835' in at(pm_, 17) and '786' in at(pm_, 18) and '340' in at(pm_, 19), at(pm_, 17)[:50], '1')
    rr_ = lines_of(p('data', 'b675_rules.txt'))
    add('ferry (read first), ruling (2)(vi)', 'data/b675_rules.txt :9, rules row (2), the long phase splits the next pre-run', at(rr_, 9).strip().startswith("(2) A PRE-RUN'S LONG PHASE SPLITS THE NEXT ONE"), at(rr_, 9)[:60], '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(9) and 23 defects (data/b737_events.txt, data/b737_defects.txt)',
        starts == list(range(1, 10)) and len(letters) == 23, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b737_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    df_ = (rd(p('data', 'b737_defects.txt')) or '').replace('’', "'")
    for l_, w_ in (('d', 'a branch delete sent before the citation check'), ('q', 'prints no controls block before its figures'), ('u', 'sed -i'), ('v', 'trails off12 on the distance')):
        add('ferry (read first)', 'data/b737_defects.txt (%s)' % l_, ("    (%s) " % l_) in df_ and w_ in df_.split("    (%s) " % l_, 1)[-1].split(NL, 1)[0], 'read', '1')
    ev_ = (rd(p('data', 'b737_events.txt')) or '').split(NL)
    for n_, w_ in ((1, 'record rootdry'), (2, '471 s'), (5, '656 s'), (7, '462 s'), (9, '456 s')):
        add('ferry (read first)', 'data/b737_events.txt (%d), %s' % (n_, w_), any(l.startswith('    (%d) ' % n_) and w_ in l for l in ev_), 'read', '1')
    EF_ = 'D:/SIDE-explicit-formula'
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ferry (read first), ruling (3)', 'zq-b730 at b25fd82c', zt_.startswith('b25fd82c'), zt_[:8], '3')
    for f_, n_, w_ in (('EF/Main.lean', 205, 'theorem zq_li_nonneg_imp_online_instance'), ('Zeros.lean', 24, 'theorem zq_differentiableAt'),
                       ('Zeros.lean', 65, 'theorem zq_conj'), ('Zeros.lean', 145, 'theorem mem_C'), ('Zeros.lean', 319, 'def zqZeroConfig'),
                       ('Continuation.lean', 147, 'theorem zqFn_holomorphic'), ('FEPair.lean', 127, 'theorem thetaC_feq'), ('FEPair.lean', 158, 'def zqPair'),
                       ('Theta.lean', 81, 'theorem thetaU_eq'), ('Theta.lean', 124, 'theorem thetaU_inversion'), ('Bound.lean', 319, 'theorem zq_three_halves_lt')):
        ln_ = gr(EF_, 'show', 'b25fd82c:SIDEExplicitFormula/Schema/ZQ/' + f_).split(NL)
        add('ferry (read first)', 'SIDEExplicitFormula/Schema/ZQ/%s :%d at b25fd82c, %s' % (f_, n_, w_.split()[-1]), at(ln_, n_).startswith(w_), at(ln_, n_)[:60], '2')
    ML_ = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
    ml_ = gr(ML_, 'rev-parse', 'HEAD')
    add('ferry (read first)', 'Mathlib at de5ce8a9', ml_.startswith('de5ce8a9'), ml_[:12], '3')
    for f_, n_, w_ in (('Analysis/Complex/AbsMax.lean', 405, 'theorem norm_le_of_forall_mem_frontier_norm_le'),
                       ('Analysis/Complex/ReImTopology.lean', 199, 'theorem frontier_reProdIm'),
                       ('NumberTheory/LSeries/AbstractFuncEq.lean', 376, 'def Λ₀ : ℂ → E := mellin P.f_modif')):
        ln_ = gr(ML_, 'show', 'HEAD:Mathlib/' + f_).split(NL)
        add('ferry (read first)', 'Mathlib/%s :%d at the pin, %s' % (f_, n_, w_.split()[1]), at(ln_, n_).startswith(w_), at(ln_, n_)[:60], '2')
    ri_ = gr(ML_, 'show', 'HEAD:Mathlib/Analysis/Complex/ReImTopology.lean').split(NL)
    add('ferry (read first)', 'Mathlib/Analysis/Complex/ReImTopology.lean :192-:199, closure, interior and frontier of a reProdIm', any('closure_reProdIm' in at(ri_, k_) for k_ in range(185, 193)) and 'interior_reProdIm' in ' '.join(at(ri_, k_) for k_ in range(192, 199)),
        at(ri_, 196)[:60], '2')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ruling (1)', 'FINDINGS :13121, b737`s entry', 'W-ORD-ZQ-OFFLINE-ZERO planned, no build' in at(fd_, 13121), at(fd_, 13121)[:50], '0')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (3)', 'OPEN_TRAILS :17400, W-ORD-ZQ-OFFLINE-ZERO PRICED at b737', 'W-ORD-ZQ-OFFLINE-ZERO` PRICED at b737' in at(ot_, 17400), at(ot_, 17400)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    SP6_ = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-62df-4f5e-a436-7e99b58f5dbf/scratchpad'
    for z_ in ('zqwork', 'zqwork2', 'zqwork3'):
        add('PATHS, b737 closing (c)', 'the damaged clone %s in place in b736`s scratchpad, not deleted' % z_, os.path.isdir(SP6_ + '/' + z_), 'present' if os.path.isdir(SP6_ + '/' + z_) else 'ABSENT', '0')
    add('ferry', 'tools/standing/ at v1.17.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.17.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R348)(4): b737's export, the mirror's last
    add('ruling (4)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-03-b737.zip, b737`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R348)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b737-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R348)(2), (4): act_current alone, then b737's step row 22 and its closing capture, each committed alone; tools/mirror_prevbuild.json's
    # ### LF form equal to HEAD's (2d637131), nothing to commit (b737's build rewrote it with CRLF endings, its content unchanged)
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b737_steps.json'),
                   (K.STEPZERO, 'data/b737_relay_push-b737-closing_push_out.txt')):
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
    add('ferry (read first)', 'data/b738_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b738_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b738 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b737_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.17.0's controls, the plan and the sitting of one kernel, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R348)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R348)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: README.md alone on SIDE-effects, twice, on the author's numbers under (R348)(4); no Lean file, no main's code, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b738 ((R348)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R347)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b738 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY-FOUR, THE PLAN ACT: b737 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE FACE THAT DID NOT FOLLOW THE AMENDMENT; '
              'W-ORD-ZQ-OFFLINE-ZERO`S CANDIDATE, BOX, ROUTES AND PRICE, NO BUILD; [76] AND [77] REDRAFTED AT MAIN, UNDER (R348).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b737's sections over b737's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.17.0: the amendment regeneration at the head, the parallel git write, the locked bank, the clone`s snapshot, the root prompt`s promise, the post-seal list, the empty remote read, each case failing before its repair and passing after', 'b738_standing_v1170.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE PLAN AND THE SITTING ((R348)(3)-(4))', [
                ('W-ORD-ZQ-OFFLINE-ZERO`s plan: the candidate by printed criteria, the box, the routes priced from statements, the recommendation with its reason, the stop points; no build', 'b738_offlinezero_plan.txt'),
                ('the sitting of one kernel: [76], [77], [25]-[29] at SIDE-effects main, the author`s word beside each', 'b738_sitting.txt'),
                ('the probe-path refusal printed before the lock gate', 'b738_pathrefusal.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b738_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b737`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b738_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R347)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no branch moved ; README.md alone on SIDE-effects` main, two commits ending at ' + WL.SITTING_TIPS['SIDE-effects'] + ', on the author`s numbers under (R348)(4), push-b738-sitting left local, no tag ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none of the two prints (R348)(3) allows) ; the rebuild-b721 branches of the wave 1 kernels as b737 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b737-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the plan committed with the prints it cites, its order printed by ancestry, the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate, the plan tool`s banks carrying no controls block before their figures (defect (q)) ;',
    '    N3: the candidate`s criteria printed before its name ; no sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem ; the entry`s nouns the banks` ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b738_address_scan.txt, data/b738_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the description write under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; the deposit route untouched, publish never called, the draft held at v5 ; no Zenodo description written, [104]-[108] waiting on the author`s record numbers ; SIDE-effects` GitHub description written by the route b727 used, read back ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the price line, the trail) written ; no paper moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY or faces page byte ; data/act_roots.txt (b738`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.17.0 by (R348)(2) ; the hook in D:/.claude/settings.json widened to Edit|Write|NotebookEdit by (R348)(2)(iii) ; the per-act tools of b698-b737 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R348)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: W-ORD-ZQ-OFFLINE-ZERO OPEN at its price (OPEN_TRAILS :17400), the plan bank relay data/b738_offlinezero_plan.txt with R4 and its four stop points ; [104]-[108] for a Tier 3 act on the author`s record numbers ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b738_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b737 left them; push-b737-sitting on b737`s 21 kernels and push-b738-sitting on SIDE-effects, local.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main but SIDE-effects` two README.md commits, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b737`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b738: the standing repairs are v1.17.0's ((R348)(2), relay data/b738_standing_v1170.txt, read in the corrigendum section); the
    # ### carry's diffs here (b738 carried at step zero before the fold; its tools since are the templates and tools/acts/b738.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; README.md alone on SIDE-effects` main at %s, the sitting of one kernel; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b737 left them; port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], K.SITTING_TIPS['SIDE-effects'], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b738's form over b738's objects (b737's form in git at b737's record tool): the corrigendum's foot and v1.17.0's controls; the plan's and the sitting's feet, the amendment rows;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1170.txt' % ACT, r'\*\*v1\.17\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.17.0`s controls')
    pl = _bfig('%s_offlinezero_plan.txt' % ACT, r'\*\*THE PLAN: CANDIDATE (\w+) AT beta - 1/2 = ([\d.]+), gamma = ([\d.]+) ; BOX (\w), MARGIN ([\d.]+) SAMPLED ; (\d+) ROUTES PRICED '
               r'\(([^)]*)\), R3 NOT A ROUTE ; (R\d) RECOMMENDED AT (\d+)-(\d+) LINES, (\d+-\d+) DISPATCHES ; (\d+) MATHLIB OBJECTS ABSENT ; (\d+) DISPATCHES THIS ACT\.\*\*', 'the plan`s foot')
    sf = _bfig('%s_sitting.txt' % ACT, r'\*\*THE SITTING OF ONE KERNEL: (\d+) ROWS ; PASS (\d+) \(([^)]*)\) ; STRUCK (\d+) ; CARRIED (\d+) ; WRITES: README\.md (\d+) \(([^)]*)\), '
               r'the description (\d+) ; SIDE-effects main ([0-9a-f]+)\.\*\*', 'the sitting`s foot')
    am = jl('%s_amendments.json' % ACT).get('rows') or []
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
                pl_name=pl[0], pl_d=pl[1], pl_g=pl[2], pl_box=pl[3], pl_margin=pl[4], pl_n=int(pl[5]), pl_routes=pl[6], pl_route=pl[7],
                pl_lo='{:,}'.format(int(pl[8])), pl_hi='{:,}'.format(int(pl[9])), pl_disp=pl[10], pl_absent=int(pl[11]), pl_disp_act=int(pl[12]),
                sit_rows=int(sf[0]), sit_p=int(sf[1]), sit_pass=sf[2], sit_s=int(sf[3]), sit_c=int(sf[4]), sit_readme=int(sf[5]), sit_commits=sf[6],
                sit_desc=int(sf[7]), sit_main=sf[8], sit_word=('passed' if int(sf[1]) == int(sf[0]) else 'carried' if int(sf[4]) else 'struck'), amend_n=len(am),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R348)(3): the kernel rows of one kind as banked (data/b738_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R348): no lean process runs on this host; the runner dispatches those of (R348)(3), two at most, each a print, each read by its
    run id, each row carrying free_mb -- none made. From the command bank (the seat's commands, read live from the capture by the `commands`
    route) and the worklist's EF_RUNS, empty."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b738_commands.json): %s; dispatch commands in the capture: %s of the %d (R348)(3) allows, the worklist`s runs %d, rows read %s, VACUOUS on a row`s free memory: no dispatch row exists' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', K.MAX_DISPATCHES, len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b738's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b738_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b738_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b738_offlinezero_criteria.txt', '## THE CONTROLS FIRST', '## (a) THE CANDIDATES'),   # ### defect (q): no controls block, read as it stands
               ('data/b738_offlinezero_box.txt', '## THE CONTROLS FIRST', '## (b) THE BOX'))
N2_REGEN = '### THE (W) REGENERATION ((R348)(2)(i))'   # ### the regeneration printed in the face, before the lock gate


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R348): the plan bank commits after the prints it cites, the order printed by ancestry; each tool's controls print before its
    figures; the (W) regeneration, the pre-lock comparison and the probe-path refusal print before the lock gate. v1.17.0's, the weight and
    corrigendum's, the plan's with its prints, the price line's, the plan's second, the two SIDE-effects writes and the sitting bank's in
    that order by time; the prints in the plan's first commit and none after it; the plan's first commit an ancestor of its second."""
    chain_ = [(ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_PLAN_FIRST), (PP, K.C2_PP), (ROOT, K.C2_RELAY),
              ('D:/SIDE-effects', K.SITTING_COMMITS[0]), ('D:/SIDE-effects', K.SITTING_COMMITS[1]), (ROOT, K.C3_RELAY[0])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C2_PLAN_FIRST, K.C2_RELAY], capture_output=True).returncode == 0
    prints_ = ('data/b738_offlinezero_criteria.txt', 'data/b738_offlinezero_box.txt')
    first_ = g(ROOT, 'show', '--name-only', '--format=', K.C2_PLAN_FIRST).split()
    later_ = [h_ for h_ in g(ROOT, 'log', '--format=%H', '%s..HEAD' % K.C2_PLAN_FIRST, '--', *prints_).split() if h_.strip()]
    same_ = all(p_ in first_ for p_ in prints_ + (K.PLAN_BANK,)) and not later_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = same_ and regen_ and bool(tz) and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the plan bank and the prints it cites (%s) in its first commit %s, a commit touching the prints after it: %s -- %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked: %s; the probe-path refusal banked and clear: %s; v1.17.0, the weight and corrigendum, their banks, the plan, the price line, the plan`s second commit, the two SIDE-effects writes and the sitting`s bank in that order by time: %s (%s), the plan`s first commit an ancestor of its second: %s; the tools` controls before their figures: %s' % (
            ', '.join(os.path.basename(p_) for p_ in prints_), K.C2_PLAN_FIRST[:8], later_ or 'NONE', same_, regen_, bool(tz), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b738's objects; b737's in git at b737's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b738_standing_v1170.txt', ('ALL AS WANTED',)), ('b738_offlinezero_plan.txt', ('THE PLAN: CANDIDATE off0',)), ('b738_sitting.txt', ('THE SITTING OF ONE KERNEL:',)),
             ('b738_corrigendum.txt', ('ITEMS',)), ('b738_citation_check.txt', ('CITES CHECKED',)), ('b738_reproduce.txt', ('REPRODUCES',)), ('b738_address_scan.txt', ('PREVIOUS ADDRESS',)))


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R348): the candidate's criteria print before its name; no sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity
    fails as a theorem; the entry's nouns are the banks'; the root prompt's sentences about the entry are the composer's. From the banks' last
    lines, the plan's (a), the entry's sentences and the root prompt in the answers bank (standing.rootprompt.entry_unbacked)."""
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
    pt_ = rdn('%s_offlinezero_plan.txt' % ACT)
    a_ = pt_.find('## (a) ')
    crit_ = a_ >= 0 and 0 <= pt_.find('  criterion ', a_) < pt_.find('  the nearest other zero of Z_Q0', a_) < pt_.find('THE CANDIDATE: off0', a_)
    neg_ = r'\b(?:NOT|not|no|No|never|until|Until|nothing|Nothing|none|None)\b'   # ### b737 defect (k'): "Nothing here ... locates any zero" read as a location
    loc_ = [s_ for s_ in sents if re.search(r'located in Lean|locates? (?:a|any|one|the) zero|positivity fails|nonnegativity fails', s_) and not re.search(neg_, s_)]
    nouns_ = [w_ for w_ in (f['pl_name'], f['pl_d'], f['pl_g'], f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], 'data/%s_offlinezero_plan.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok = all(o for _n, o in graded) and crit_ and not loc_ and not nouns_ and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the candidate`s criteria printed before its name (relay data/b738_offlinezero_plan.txt (a)): %s; read from %s, a sentence saying a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem: %s; the plan`s nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), crit_, src, loc_ or 'NONE', nouns_ or 'NONE', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R348) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R348)(5))
# ### (R348)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R348) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b737's form, carried) -- read from git,
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
    # ### (R348)(4)-(6), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-effects' main or its push-b738-sitting at db0575c6; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b737 left them; the address scan's count from its bank (relay data/b738_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b738_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than the sitting`s main and push-b738-sitting at the sitting`s tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b738 — lane two, act one hundred and sixty-four, the plan act under (R348): b737 at its weight and its corrigendum; v1.17.0; '
            'W-ORD-ZQ-OFFLINE-ZERO planned, no build; [76] and [77] at SIDE-effects main')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form; every figure from the banks (the plan's and the sitting's feet,
    v1.17.0's controls less the amendment regeneration's own)."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## W-ORD-ZQ-OFFLINE-ZERO planned, no build: candidate %s at β − 1/2 = %s, γ = %s; %d routes priced, %s recommended at %s-%s lines, %s dispatches, '
            '%d Mathlib objects absent; [76], [77] %s at SIDE-effects main; the amendment regeneration and %d repairs landed' % (
                f['pl_name'], f['pl_d'], f['pl_g'], f['pl_n'], f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], f['pl_absent'], f['sit_word'], f['repairs'] - 1))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the candidate read from b725’s table by the printed criteria, off0 confirmed where the navigator named it, the order’s “the lowest” not the reason; (2) R3 read as not a route, no off-line segment carrying a real-valued restriction whose sign change marks the zero, and R4 the route the seat found in Mathlib at the pin (AbsMax.lean :405); (3) the line prices read from statements against the measured ratios of b730-b735, every sampled figure a float of a sample and not a bound; (4) “Pass [76] + Milestones” read as widening [76] to the Milestones section of the same README.md, and [28] as one write the author’s words name, each banked as an amendment row with no new path (relay data/b738_amendments.json); '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)) or '(R348)(6)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b738's objects; b737's composer in git at
    b737's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R347)(2)(v)
    e = ['', _title(), '',
         'W-ORD-ZQ-OFFLINE-ZERO is planned and not built: the candidate %s, β − 1/2 = %s and γ = %s, chosen from b725’s table by printed criteria; box %s around it, its least sampled |Z_Q0| on the boundary %s; %d routes priced from statements (%s), R3 not a route; %s recommended at %s-%s lines and %s dispatches, %d Mathlib objects absent at the pin. No dispatch was made (%d of the 2 allowed) and no Lean file written. [76] and [77] were redrafted at SIDE-effects main and passed on the author’s word, with [25]-[29] after them: %d rows, PASS %d; README.md written twice (%s), the description once. The draft stands at v5, HELD.' % (
             f['pl_name'], f['pl_d'], f['pl_g'], f['pl_box'], f['pl_margin'], f['pl_n'], f['pl_routes'], f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], f['pl_absent'],
             f['pl_disp_act'], f['sit_rows'], f['sit_p'], f['sit_commits']), '',
         '*Filed at b738 on the author’s ruling `(R348)`, its (4) read with %d amendment row%s from the author’s words; %d question%s put before the root. Banks: relay '
         '`data/b738_corrigendum.txt`, `data/b738_standing_v1170.txt`, `data/b738_offlinezero_plan.txt`, `data/b738_offlinezero_criteria.txt`, `data/b738_offlinezero_box.txt`, `data/b738_sitting.txt`, `data/b738_amendments.json`, `data/b738_prelock.txt`, `data/b738_pathrefusal.txt`, '
         '`data/b738_reproduce.txt`, `data/b738_address_scan.txt`, `data/b738_touch.txt`, `data/b738_standing_figures.txt`, `data/b738_report.txt`.*' % (f['amend_n'], '' if f['amend_n'] == 1 else 's', n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R348)(1)-(2), %s, %s, %s): b737 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b737’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b738_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b738_standing_v1170.txt), the amendment regeneration at their head.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): tools/standing/ v1.17.0 at %s, the weight and the corrigendum at PLACE-papers %s and their banks at %s, all before the plan’s first commit %s, which carries the criteria and box prints it cites; the price line at PLACE-papers %s by a commit of its own, OPEN_TRAILS alone; the plan’s second commit %s; then SIDE-effects %s and %s; the sitting’s bank at %s. The (W) regeneration printed in the face, and the pre-lock comparison and the probe-path refusal banked, before the lock gate (relay data/b738_prelock.txt, data/b738_pathrefusal.txt). The plan’s two figure banks open on their figures with no controls block before them, the controls standing inside the rows (defect (q)). No lean process on this host and no dispatch: the runner arms read VACUOUS, no row existing to read.' % (
             K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_PP[:8], K.C2_RELAY[:8], K.SITTING_COMMITS[0][:8], K.SITTING_COMMITS[1][:8], K.C3_RELAY[0][:8]), '',
         '**The candidate** ((R348)(3)(a), N3): the three leading rows of relay data/b725_interference.txt :32-:34, off0, off12 and off52, each printed on β − 1/2, γ, the bits b725 took, the nearest other zero of Z_Q0, the nearest zero of ζ_K and of L(ψ) on the line and |Z_Q0′| before the name; %s leads on β − 1/2 (%s), on the distance to its nearest other zero (its reflection, 0.906521), on the evaluation’s cost at the least height (γ = %s) and on the bits; it trails off52 on the distance to ζ_K’s zeros (0.573960 against 0.575992) and off12 on the distance to L(ψ)’s (0.498714 against 0.559635), each clear of box A (relay data/b738_offlinezero_criteria.txt :8-:9, :13-:14, :18-:19). The plan’s (a) reads “trails off12 on the distance to zeta_K’s zeros (0.574 against 0.507)”, its own figures saying off0 leads off12 there (defect (v)).' % (f['pl_name'], f['pl_d'], f['pl_g']), '',
         '**The box and the routes** ((R348)(3)(b)-(c)): box %s, the square of half-side 0.1 centred on %s, [0.853260, 1.053260] × [16.190216, 16.390216], off0 the one listed zero inside, its least |Z_Q0| on 160 boundary samples %s (sampled, not a bound); box B, its right edge at Re s = 3/2, priced and not taken (relay data/b738_offlinezero_box.txt). R1, the argument principle with a Lipschitz bound, and R2, Rouché with f the finite truncation, each compile the count; R4, the minimum modulus through Complex.norm_le_of_forall_mem_frontier_norm_le (Mathlib AbsMax.lean :405) applied to the reciprocal, compiles the existence the order asks; R3, a sign change, is not a route, no segment through an off-line zero carrying a real-valued restriction. Every route shares the certified evaluation of zqFn on the box, Λ₀ wanted to some 5e-12 where |Γ(s)| is near 7e-11.' % (f['pl_box'], f['pl_name'], f['pl_margin']), '',
         '**The price and the recommendation** ((R348)(3)(d)): %s at 1,635-4,175 lines from statements, %s-%s by explicitFormula’s measured ratio 0.915, the envelope of the five measured ratios 455-16,408, %s dispatches; R1 2,374-5,943 and R2 2,191-5,577 by the same ratio; the %d Mathlib objects absent at the pin named (the argument principle, Rouché, the winding number, the incomplete gamma function, complex Stirling with explicit error, the K-Bessel function, certified interval evaluation), three on R4’s path. The reason: the order’s condition is an existence and R4 proves exactly that with the one complex-analytic step Mathlib carries by name. Four stop points, the first a conditional theorem with no numeric step (relay data/b738_offlinezero_plan.txt (d)). The price line at OPEN_TRAILS :%d.' % (
             f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], f['pl_absent'], K.PRICE_LINE), '',
         '**The consequence, priced and not stated** ((R348)(3)(e)): a declaration of ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1/2 with the standard three axioms would give, through zq_li_nonneg_imp_online_instance (Schema/ZQ/EF/Main.lean :205, zq-b730 at b25fd82c), the negation of ∀ n, 0 ≤ Wide.liCoeff zqZeroConfig n, at 5-15 lines. The plan prices that sentence and does not state it. Until a build compiles the condition, no sentence says a zero of Z_Q0 is located in Lean or that Li nonnegativity fails as a theorem; the off-line zeros stand at b725’s numerical location, HELD.', '',
         '**The sitting of one kernel** ((R348)(4), N3): SIDE-effects read at main 78bbcff, the statements standing there listed and side_exclusion named retired in Structural.lean’s ledger; the door paragraph and the description redrafted from that read and put one item at a time with current and drafted words, file, line and grade. [76] passed with the Milestones section by the author’s word and written at %s; [77] passed and written by gh, read back; [25] and [29] fell with [76] and [77]; [26] and [27] stand, true at main; [28] passed with the author’s own words, “0 sorry at 78bbcff.” at :50 and :57, written at %s, the second write of this act to README.md. %d rows, PASS %d, STRUCK %d, CARRIED %d; the open-premise paragraph and the retirement record kept whole; README.md alone on the kernel, no Lean file, no tag (relay data/b738_sitting.txt). The Milestones line written at %s dropped “0 axioms”, a fact true at main and still printed in the README’s Status section (defect (o)).' % (
             K.SITTING_COMMITS[0][:8], K.SITTING_COMMITS[1][:8], f['sit_rows'], f['sit_p'], f['sit_s'], f['sit_c'], K.SITTING_COMMITS[0][:8]), '',
         '**The amendment rows** ((R348)(2)(i), N5): %d rows, the words of [76] and [28], each widening (4)’s door paragraph within the README.md it names and adding no path; the face’s (W) row and N5’s write clause regenerated from the ruling and the rows before the lock, the regeneration printed in the face (relay data/b738_amendments.json).' % f['amend_n'], '',
         '**What this act is not**: no deposit, no tag, no draft published, no Lean file written, no merge, no dispatch. A plan prices a build and proves nothing; a README sentence removed removes a claim from a door. Nothing here proves RH or GRH or locates any zero.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b738_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b738_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b738_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b738 -- %s, %s, %s, %s -- against b737’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b738_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the plan and the sitting read one way: the plan prices the one declaration that would turn two HELD rows into a kernel and states neither, and SIDE-effects’ door now says what compiles at its main and no further; a grade word is out of both.', '',
         '**Carried to:** %s, (R348)(7): W-ORD-ZQ-OFFLINE-ZERO OPEN at its price, the build on the plan’s route by the author’s word; the five Zenodo currency notes [104]-[108], to a Tier 3 act on the author’s record numbers; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the damaged clones zqwork, zqwork2 and zqwork3 in place, the cause not established; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b737():
    """b737's form over b737's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b738's objects; b737's composer in git at b737's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD, W-ORD-ZQ-DERIVES closed at b737 and W-ORD-ZQ-OFFLINE-ZERO open at its price (:17400)."""
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
             '**(R348) ratified.** Its components as the ferry orders them (relay data/b738_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b737’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders:** W-ORD-ZQ-OFFLINE-ZERO priced at OPEN_TRAILS :%d by PLACE-papers %s, a commit of its own, planned and not built; it stays OPEN at its price.' % (K.PRICE_LINE, K.C2_PP[:8]), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b738_standing_v1170.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The plan:** candidate %s (β − 1/2 = %s, γ = %s), box %s, margin %s sampled; %d routes priced, %s recommended at %s-%s lines, %s dispatches, %d Mathlib objects absent; %d dispatches this act (relay data/b738_offlinezero_plan.txt).' % (
                 f['pl_name'], f['pl_d'], f['pl_g'], f['pl_box'], f['pl_margin'], f['pl_n'], f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], f['pl_absent'], f['pl_disp_act']), '',
             '**The sitting:** SIDE-effects at main, %d rows, PASS %d, STRUCK %d, CARRIED %d; README.md %d writes (%s), the description %d; %d amendment rows (relay data/b738_sitting.txt, data/b738_amendments.json).' % (
                 f['sit_rows'], f['sit_p'], f['sit_s'], f['sit_c'], f['sit_readme'], f['sit_commits'], f['sit_desc'], f['amend_n']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b738_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b738_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b738_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b738 `%s` (previous `%s`, b737’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b738_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b738_standing_v1170.txt); the standing '
             'report tool (relay data/b738_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** README.md alone on SIDE-effects’ main at %s, two commits, no Lean file and no main’s code, no tag; push-b738-sitting left local; zq-b730 of SIDE-explicit-formula unmoved at %s; %d dispatches; the %s branches as b737 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.SITTING_TIPS['SIDE-effects'], K.ZQ_TIP[:8], len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b738_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b737’s %s, %s, %s, %s (relay data/b738_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b738_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b737():
    """b737's trail record over b737's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none of the two prints (R348)(3) allows; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b737 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b735`s, none at b737 or this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R348)(5): relay push-b737-closing, push-b737-preroot, push-b737-record; PLACE-papers push-b737-preroot, push-b737-record; each local, by name, each after its --merged listing.'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: README.md alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R348) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (9b12ec5a) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R348)(2): FINDINGS :13033.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R348)(2): row (57).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-OFFLINE-ZERO priced by (R348)(3)`s own commit (OPEN_TRAILS :17400), entered at b737.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b738_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.17.0`s controls, the plan`s criteria and box prints, the plan, the sitting`s bank, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the plan committed with the prints it cites (310a681f), (R348)(3)(d) ordering the plan after its prints, not alone.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: the plan registers no figure beyond its prints; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none: the prints commit with the plan (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none, N5; MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R348)(2): tools/standing/ to v1.17.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b738_address_scan.txt (the address never printed).'),
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
    # ### (R348)(3): no figure bank of a registered object: the print is the plan's source and precedes it (N2)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b738_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b738_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1170', 'offlinezero_criteria', 'offlinezero_box', 'offlinezero_plan', 'sitting', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b738_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b738_registration_%s.txt -- b738, THE PLAN ACT: b737 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.17.0; W-ORD-ZQ-OFFLINE-ZERO PLANNED, NO BUILD; [76] AND [77] AT SIDE-effects MAIN; "
                             "NO DEPOSIT, NO TAG, UNDER (R348)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b737's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b738: b737's lines read banks this
act does not write, and are not carried; the lines are b738's: the plan (KERNEL, its price at the pin; nothing built), tools/standing/ v1.17.0 by
its controls (CERTIFIED), the plan's candidate and the sitting of one kernel (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b738's lines, each from the record tool's figures over b738's banks
    # ------------------------------------------------------------------ KERNEL: (R348)(3), the plan's price at the pin, nothing built
    sz = seat('%s_offlinezero_plan.txt' % ACT, '**THE PLAN: CANDIDATE ')
    sk = sz   # ### (R347)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- W-ORD-ZQ-OFFLINE-ZERO PLANNED, NO BUILD: %s recommended at %s-%s lines and %s dispatches over zq-b730 at %s, %d Mathlib objects absent at the pin; no Lean file and no dispatch this act. SOURCE %s.' % (
        f['pl_route'], f['pl_lo'], f['pl_hi'], f['pl_disp'], K.ZQ_TIP[:8], f['pl_absent'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.17.0 ((R348)(2)), by its controls
    sw = seat('%s_standing_v1170.txt' % ACT, '**v1.17.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.17.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the plan's candidate and the sitting, read from their banks
    so = seat('%s_sitting.txt' % ACT, '**THE SITTING OF ONE KERNEL: ')
    keys['ORD'] = ('REGISTERED -- THE PLAN`S CANDIDATE %s at beta - 1/2 = %s, gamma = %s, box %s, margin %s sampled, not a bound; THE SITTING OF ONE KERNEL: %d rows, PASS %d, STRUCK %d, CARRIED %d, each on the author`s word, SIDE-effects main %s. SOURCE %s.' % (
        f['pl_name'], f['pl_d'], f['pl_g'], f['pl_box'], f['pl_margin'], f['sit_rows'], f['sit_p'], f['sit_s'], f['sit_c'], f['sit_main'], so['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R348)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b738 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
