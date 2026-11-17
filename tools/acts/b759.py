# -*- coding: utf-8 -*-
# b759 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R369)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R369)(2) repair it carries. Edited by the Edit tool. Carried at b759 by tools/b759_fold.py (`carry`) from tools/acts/b758.py,
# b758`s names substituted; the citation`s sections adopted from tools/b759_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b758`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b758`s carried till
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
# ### b759, Component 1: THE c1 ROUTE FOR b758'S SHORT CORRIGENDUM, (R369)(1), written by the Edit tool against b758's banks (72 events, 8
# ### defects, 1 refusal; no post-seal events bank at b758) and the findings after b758's lock, entered as this act's events from the seat's own
# ### closing message (data/b759_events.txt (17)-(21)); short, as (1) orders: the counts from the banks, no CLAIM item among them, the findings
# ### each with its time. (1) states b758's weight from its closing's head and orders no line of its own, so the weight route refuses; (10)
# ### carries OPEN_TRAILS' lines under one dated head, so the next route too. b758's route (tools/acts/b758.py :34-:241) carried by hand in
# ### place of the stub; nothing composed by the stub. The title under the title rule: no backtick (tools/standing/titlerule.py, v1.35.8).
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_NOTED = '2026-11-17'
C1_CORRIGENDA_LAST = 78
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b758_events.txt'), ('defects', 'b758_defects.txt'))
C1_EVENTS_N = 72
C1_DEFECTS = (8, 'h')
C1_REFUSALS = 1
C1_CLAIMS = ()                     # ### (R369)(1): "no CLAIM item among them"
C1_HEAD = ('b758 closed: relay c25f8b53, PLACE-papers 4ea4194; suite 111 of 116;', 'scores 7 of 8 HELD; 8 defects')   # ### data/b758_closing.txt :1, read by the state
C1_FINDINGS_BANK = 'b759_events.txt'
C1_FINDINGS_IDS = ('17', '18', '19', '20', '21')
C1_RULED = (('17', ('14:23:25Z', '680.2 s', 'background')), ('18', ('14:36:12Z', 'MEMORY HOLD', '2,457 MB')), ('19', ('16:37:20Z', 'UNRESOLVED', '16:37:56Z')),
            ('20', ('15:21:58Z', 'CEILING')), ('21', ('recut-b712-silence', 'DIFFER')))   # ### the closing message's "After the lock" list in its order
C1_CORR_TITLE = ('## Corrigendum to b758’s record, short (relay data/b758_events.txt rows (1)-(72) and data/b758_defects.txt (a)-(h)): its events and '
                 'defects by count from their banks, no CLAIM item among them, and the findings after the lock, entered as events with their times')
def _c1_rd(name, base=None):
    with open(os.path.join(base or D, name), encoding='utf-8') as fh:
        return fh.read().replace(chr(13), '')


def _c1_fl(name, pat, what, base=None):
    """the one line of a bank matching pat: (groups, line number); any other count exits, nothing composed."""
    hits = [(i, m) for i, l in enumerate(_c1_rd(name, base).split(NL), 1) for m in [re.search(pat, l)] if m]
    if len(hits) != 1:
        sys.exit('### %s: %d LINES OF %s MATCH %r, NOT ONE -- NOTHING COMPOSED' % (what, len(hits), name, pat))
    return hits[0][1].groups(), hits[0][0]


def _c1_rows(name):
    """[(id, owner, tag, column, text)] of a bank's rows in bank order: a row opens at four spaces with (id) and its lines after, at five
    spaces or more, are joined to it; a line at column 0 (a section head of an events bank) closes the row before it; an untagged row
    exits, nothing composed."""
    out, cur = [], None
    for l in _c1_rd(name).split(NL):
        if re.match(r"^    \(((?:[a-z]'*)|\d+)\) ", l):
            cur = [l.strip()]
            out.append(cur)
        elif cur is not None and l.startswith('     ') and l.strip():
            cur.append(l.strip())
        else:
            cur = None
    rows = []
    for r in out:
        m = C1_ROW.match(' '.join(r))
        if not m:
            sys.exit('### %s: AN UNTAGGED ROW %s -- NOTHING COMPOSED' % (name, ' '.join(r)[:60]))
        rows.append(m.groups())
    return rows


def _c1_tally(rows):
    return dict(claim=sum(1 for r in rows if r[2] == 'CLAIM'), close=sum(1 for r in rows if r[2] == 'CLOSE'),
                repeat=sum(1 for r in rows if not r[3].startswith('NEW')), total=len(rows))


def _c1_q(s):
    """a bank's own words for the ledger (b754's form, carried): markdown's marks escaped; a pair of backticks quoting a span read as quotes,
    every other backtick as an apostrophe; the template's placeholder brackets as angles."""
    s = s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_')
    s = re.sub(r'(^|[\s(\[])`([^`]{1,60}?)`', r'\1‘\2’', s)
    return (s.replace('`', '’')
            .replace('\u27ea', '\u2039').replace('\u27eb', '\u203a'))


def _c1_owner(o):
    return o.lower().replace("'s", '’s').replace("'", '’')


def _c1_col(c):
    if c == 'NEW':
        return 'NEW'
    c = c if c.startswith('REPEAT of ') else c.replace('REPEAT ', 'REPEAT of ', 1)
    return c.replace("'", '’').replace('`', '’')


def _c1_head(text):
    """a finding's head: its words before the first ", at " or the first full stop and space."""
    m = re.match(r"^(.*?)(?:, at |\. )", text)
    return m.group(1) if m else text[:120]


def _c1_time(text):
    """a finding's time: the first full date and time its row carries, as HH:MM:SSZ; None where the row carries none."""
    m = re.search(r'\d{4}-\d\d-\d\dT(\d\d:\d\d:\d\d)(?:\.\d+)?Z', text)
    return m.group(1) + 'Z' if m else None


def _c1_state():
    s = dict((k_, _c1_rows(n_)) for k_, n_ in C1_BANKS)
    ev, df = s['events'], s['defects']
    tot = _c1_tally(ev + df)
    cnt, l_cn = _c1_fl('b758_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    head = _c1_rd('b758_closing.txt').split(NL)[0]
    rf = [l for l in _c1_rd('b758_hook_refusals.txt').split(NL) if l.strip()]
    kinds = {}
    for l in rf:
        m = re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \| ([A-Z]+) \| ', l)
        kinds[m.group(1) if m else '?'] = kinds.get(m.group(1) if m else '?', 0) + 1
    cr_ = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    own = dict((r[0], r) for r in _c1_rows(C1_FINDINGS_BANK))
    fnd = [own.get(i_) for i_ in C1_FINDINGS_IDS]
    claims = [(k_, r) for k_, _n in C1_BANKS for r in s[k_] if r[2] == 'CLAIM']
    ruled = [(i_, w_) for i_, ws_ in C1_RULED for w_ in ws_ if not (own.get(i_) and w_ in own[i_][4])]
    bad = [k_ for k_, ok_ in (
        ('the closing`s head as (1) reads it', all(h_ in head for h_ in C1_HEAD)),
        ('the event rows (1)-(%d)' % C1_EVENTS_N, [int(r[0]) for r in ev] == list(range(1, C1_EVENTS_N + 1))),
        ('no post-seal events bank at b758', not os.path.exists(os.path.join(D, 'b758_events_postseal.txt'))),
        ('the defect rows %d, the last (%s)' % C1_DEFECTS, len(df) == C1_DEFECTS[0] and df[-1][0] == C1_DEFECTS[1]),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev)) == tuple(int(x) for x in cnt)),
        ('no CLAIM row', [(k_, r[0]) for k_, r in claims] == list(C1_CLAIMS)),
        ('the refusals %d, each by its kind' % C1_REFUSALS, len(rf) == C1_REFUSALS and '?' not in kinds),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the five findings, each with its date and time', all(fnd) and all(_c1_time(r[4]) for r in fnd)),
        ('the findings, each in its row: missing %s' % ruled, not ruled),
    ) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (the tally %s)' % (bad, tot))
    s.update(tally=tot, l_counter=l_cn, refusals=len(rf), kinds=kinds, findings=fnd, claims=claims)
    return s


def _c1_lines(s):
    t = s['tally']
    per = dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS)
    kinds = ', '.join('%s %d' % kv for kv in sorted(s['kinds'].items(), key=lambda kv: (-kv[1], kv[0])))
    pe, pd = per['events'], per['defects']
    ft = _c1_tally(s['findings'])
    L = ['*b758 closed at relay c25f8b53 and PLACE-papers 4ea4194, suite 111 of 116, scores 7 of 8 HELD (relay data/b758_closing.txt :1). '
         'Its events bank (relay data/b758_events.txt) carries %d rows, (1)-(%d): CLAIM %d, CLOSE %d, REPEAT %d; its defects bank (relay '
         'data/b758_defects.txt) %d lettered rows, (a)-(h): CLAIM %d, CLOSE %d, REPEAT %d. Together CLAIM %d, CLOSE %d, REPEAT %d of %d, as b758’s closing '
         'counter prints it (relay data/b758_closing.txt :%d). Rows (67)-(72) were appended after b758’s lock and before its root, and are counted. '
         'Its refusals bank %d line (relay data/b758_hook_refusals.txt), by kind %s. No post-seal events bank at b758. Each item is tagged in its own '
         'bracket; the tags are the banks’ own and this entry edits none of them. No CLAIM item stands among them, so none is printed in full.*' % (
             pe['total'], pe['total'], pe['claim'], pe['close'], pe['repeat'], pd['total'], pd['claim'], pd['close'], pd['repeat'],
             t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds), '']
    L += ['**The findings after b758’s lock**, entered as events of b759 from the seat’s closing message (transcript line 130938, '
          '2026-11-17T16:42:02Z), which gave them there and not in a bank, the events bank being among the banks the root hashes; each time read '
          'from the transcript’s record (relay data/b759_events.txt rows (17)-(21)), each on 2026-11-17: CLAIM %d, CLOSE %d, REPEAT %d of %d. %s.' % (
              ft['claim'], ft['close'], ft['repeat'], ft['total'],
              '; '.join('(%s) %s, %s [%s ; %s]' % (r[0], _c1_q(_c1_head(r[4])).replace("'", '’'), _c1_time(r[4]), r[2], _c1_col(r[3])) for r in s['findings'])), '']
    L += ['**N4 at b758** stands REFUTED, on the act module’s repair after the lock (relay f401a81e), made on the author’s word of 11:32:30Z, '
          'and on rows (67)-(72); it is not argued (`(R369)`(1)). **The repairs b758’s close carried** are ordered as standing changes under '
          '`(R369)`(4): the plant of G-DELETES-ONE-BRANCH reading every covering clause, the row writer’s phase for a repair commit, and the '
          'suite’s reader of the kernels face naming SIDE-dirichlet-mod-24 (b758 defect (f)), each with its control before its use.', '',
          '*Filed at b759 on the author’s ruling `(R369)`(1): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b759.py) from b758’s events, defects and refusals banks read unedited and b759’s events rows (17)-(21); '
          'banked as relay `data/b759_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b758’s record; no '
          'sealed tool, face, trail or root-named bank of b758 is edited. No weight line is written: `(R369)`(1) orders none.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    ft = _c1_tally(s['findings'])
    return (['b759 -- THE CORRIGENDUM FOR b758, SHORT, (R369)(1) (%s)' % utc(), '',
             '### the banks read unedited: data/b758_events.txt rows (1)-(%d), data/b758_defects.txt %d rows, data/b758_hook_refusals.txt %d line; no '
             'post-seal events bank at b758; data/b758_closing.txt :1 (the head) and :%d (the counter); data/%s rows (17)-(21) (the findings after the '
             'lock); the corrigenda bank`s last row (%d).' % (len(s['events']), len(s['defects']), s['refusals'], s['l_counter'], C1_FINDINGS_BANK, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEMS 0 ; THE FINDINGS AFTER THE LOCK %d: '
               'CLAIM %d, CLOSE %d, REPEAT %d ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['defects']), t['claim'], t['close'], t['repeat'], ft['total'], ft['claim'],
                   ft['close'], ft['repeat'], ln)])


def c1(*a):
    """`c1 corrigendum [dry|write]`: the short corrigendum for b758, landed through b698's guarded landing (the title rule of v1.35.8 in front of
    it); dry prints and writes nothing. (R369)(1) orders no weight line and (10) carries OPEN_TRAILS' lines: `c1 weight` and `c1 next` refuse."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        sys.exit('### (R369)(1) ORDERS NO WEIGHT LINE FOR b758 -- NOTHING COMPOSED')
    if route == 'next':
        sys.exit('### (R369)(10) CARRIES OPEN_TRAILS` LINES UNDER ONE DATED HEAD -- NOTHING COMPOSED HERE')
    if route == 'corrigendum':
        from b652_record import line_of
        s = _c1_state()
        text = NL + C1_CORR_TITLE + NL + NL + NL.join(_c1_lines(s)) + NL
        land([('FINDINGS.md', C1_CORR_TITLE, text)], '%s_corrigendum_landing.json' % ACT, 'corrigendum', entry=None, dry=dry)
        if dry:
            print(NL.join(_c1_bank(s, None)))
            return
        ln = line_of(R.FIND, C1_CORR_TITLE)
        t = s['tally']
        ft = _c1_tally(s['findings'])
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=t['claim'], close=t['close'], repeat=t['repeat'], items=t['total'],
                                                   by_bank=dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS),
                                                   claims=[], in_full=None,
                                                   findings=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_FINDINGS_IDS), claim=ft['claim'],
                                                                 close=ft['close'], repeat=ft['repeat'],
                                                                 times=dict((r[0], _c1_time(r[4])) for r in s['findings']),
                                                                 claims=[dict(id=r[0], owner=r[1], column=r[3]) for r in s['findings'] if r[2] == 'CLAIM']),
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   repairs=dict(ordered='(R369)(4)(ii), (iii), (iv)'),
                                                   weight_line=None, row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEMS 0 ; THE FINDINGS %d, CLAIM %d ; FINDINGS :%s' % (
            t['claim'], t['close'], t['total'], t['repeat'], ft['total'], ft['claim'], ln))
        return
    sys.exit('usage: fold.py record c1 corrigendum  [dry | write]')
#⟪END⟫
# ### b754, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b754, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b754's name.
# ### b754's own changes are marked "b754, Component 3". The runner overrides read the act's dispatch rows: (R364)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b754_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R363)(7), as b753 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """N1, b759 ((R369)(5), (11)): every dispatch of the act a row of the dispatch bank, its kernel named, its free memory read before the send at or
    above the hold; the run ids by kernel the worklist's, EF_RUNS in SIDE-explicit-formula within 3 and none in SIDE-dirichlet-mod-24
    (M24_RUNS empty, its cap 0: (11) touches no kernel beyond SIDE-explicit-formula's tree and the five branches of (3)), no dispatch row of another kernel; each read once after it by
    that id, the read's free memory at or above the hold; the plant a dispatch row with no kernel and no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    ef_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-explicit-formula']
    m4_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-dirichlet-mod-24']
    return bool(ds) and ef_ == list(K.EF_RUNS) and len(ef_) <= K.MAX_DISPATCHES and m4_ == list(K.M24_RUNS) and len(m4_) <= K.MAX_DISPATCHES_M24 \
        and len(ds) == len(ef_) + len(m4_) \
        and all(str(r.get('free_mb', '')).isdigit() and int(r.get('free_mb')) >= KS.HOLD for r in ds + rs) \
        and all(sum(1 for x in rs if str(x.get('run')) == str(d.get('run'))) == 1
                and rows.index(d) < next((i for i, x in enumerate(rows) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))), -1) for d in ds)
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b754: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): b754's override of the hook's blob (read at its v1.11.0 commit) retired -- v1.34.6 (relay
# ### eac02515) left tools/standing/hook.py unedited, so the template's line (its blob at the act's base 28255aea the working tree's) reads b755
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b758, naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base 28255aea the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b758-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b759_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b754, Component 6 (the Edit tool), carried: the step-zero bank words the row "THE --MERGED LISTING, PRINTED BEFORE THE DELETES"
# ### (data/b755_stepzero.txt :55); b758: "THE --MERGED LISTING, before the deletes" (data/b758_stepzero.txt :54); b759, before the lock:
# ### b759's bank words it "THE --MERGED LISTING (18:41Z)" and its deletes "THE DELETES, AFTER THE CHECK" (data/b759_stepzero.txt :60, :62)
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING (18:41Z)' in z and 'THE DELETES, AFTER THE CHECK' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's overrides of checks 1516 and 1659 (hook.py edited by b753's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b754 as it stands
# ### b754, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b759_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b756, Component 6 (the Edit tool): the corrigendum's json (data/b756_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 46, CLAIM 0, CLOSE 46, REPEAT 20, the CLAIM items 0, the corrigenda row (76); the rows stand in the bank by
# ### their banks (data/b756_corrigendum.txt); the template's row range read as the json's counts
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 80 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's override of checks 1476-1482 (one ERRATA entry at b753's (R363)(5)) removed -- (R364)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b754 as it stands
# ### G-BRANCHES-DELETED over b755's two repositories (relay, PLACE-papers) and five refs. b755, Component 6 (the Edit tool): b755's step
# ### zero names no kept branch in its own bank ("the kept branches and the tag read by the citation check's section 9", data/
# ### b755_stepzero.txt :60), where the template's needle ('port-b707', 'KEPT') and b754's (its kept row's wording) read the step-zero bank;
# ### read where b755 banks it, the citation check's row (data/b755_citation_check.txt :68, "port-b707 kept on SIDE-lv-conservation"), and
# ### its tip from the tree. b756, Component 6 (the Edit tool): the row is (R366)(8)'s at b756 ("no branch of any kernel merged, created,
# ### moved or deleted"), data/b756_citation_check.txt :60, "| ruling (8) | port-b707 kept on SIDE-lv-conservation | local |"; b755's
# ### "(9)" read no row and failed the arm at the a2 probe (19:11:41Z)
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
# ### b759, before the lock (the Edit tool): five refs at b759's step zero (the relay's push-b758-closing, -preroot and -record; PLACE-papers'
# ### -preroot and -record, data/b759_events.txt (9)); b759's citation check carries the kept row under (R369)(3), data/b759_citation_check.txt
# ### :56, "| ruling (3) | port-b707 kept on SIDE-lv-conservation | local |"
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and '| ruling (3) | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b759, before the lock (the Edit tool): G-DELETES-ONE-BRANCH over b759's deletes -- the five step-zero refs, each by the one-call tool's
# ### delete route, and (3)'s five kernel branches, each removed at its kernel's remote by (4)(i)'s route `<repo> rdelete <branch>`
# ### (data/b759_events.txt (24)), which the standing capture reader (tools/standing/delread.py v1.30.0, its TOOL_ARGS) does not read: the
# ### act's reader below reads them segment by segment as delread reads the delete route, wanted equal to the worklist's KERNEL_DELETES; every
# ### delete of either route read against the ruling's own delete clauses through the standing allowance reader; port-b707 undeleted at its tip
#⟪OVERRIDE checks MARK 61379f7e4609 2⟫
        and sorted(_rdeletes(S)) == sorted(b_ for b_, _t in K.KERNEL_DELETES) and not [b for b in got if b not in NAMED_PUSH] \
        and STW.deletes_read([('-', b) for b in got + _rdeletes(S)], S['ferry'], STW.words_of(ACTN))['ok'] \
        and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP \
#⟪END⟫
#⟪OVERRIDE checks MARK 23e17a97edcc 1⟫
    ('G-DELETES-ONE-BRANCH', '(⟪RUL⟫)(3): the command capture`s branch deletes, each one branch, no glob, no variable, nothing chained after; the five step-zero deletes by the tool`s delete route and the five kernel branches by (4)(i)`s rdelete route, each allowed by the ruling`s own delete clause read through tools/standing/allow.py, the kernel branches the worklist names and no other; port-b707 undeleted at its tip; the command bank`s count',
#⟪END⟫
# ### b759, before the lock: b758's override of the plant (plant_every_kept, after b758's lock on the author's word) retired -- v1.36.4
# ### (relay 4622b017, (R369)(4)(ii)) gave tools/standing/allow.py's plant_kept the reading of every covering clause, so the template's
# ### plant line reads b759 as it stands (data/b759_events.txt (25)); the reader of (4)(i)'s rdelete route put in its slot
#⟪OVERRIDE checks MARK 48a0f0acd92b 0⟫
def _rdeletes(S):
    """b759, (R369)(3), (4)(i): the kernel branches removed at a remote by the one-call tool's rdelete route, read from the command capture
    segment by segment as tools/standing/delread.py reads the delete route (gitwrite's RUNS_COMMIT over the segment's commands, quoted strings
    blanked; the words `<repo> rdelete <branch>` closing the segment); an interpreter program or an echo quoting the route reads none."""
    DR = __import__('standing.delread', fromlist=['segments'])
    out = []
    for r in S['cmds']:
        if r['tool'] not in ('Bash', 'PowerShell'):
            continue
        for seg in DR.segments(r['cmd']):
            if any(DR.GW.RUNS_COMMIT.match(c) for c in DR.GW.commands(seg)):
                m = re.search(r'\bcommit\.py[\'"]?\s+(\S+)\s+rdelete\s+(\S+)\s*$', seg.rstrip())
                if m:
                    out.append(m.group(2).strip('\'"'))
    return out


#⟪END⟫
# ### b755, Component 6 (the Edit tool): b754's overrides of the ledger adds and G-FINDINGS-APPEND-ONLY (its (R364)(5)[A] passes
# ### replacing seven FINDINGS lines one for one) retired -- b755 appends to FINDINGS alone (the weight line and the corrigendum at
# ### PLACE-papers dc89f3e7, 1 hunk, 0 lines removed; the entry at the record), so the template's appended() and its arm read b755 as it stands
# ### b754, Component 4 (the Edit tool): G-RUNNER-READ's plant on b754's dispatch rows -- run 2's axiom lines carrying sorryAx (b753's
# ### plant read the lv rows' closure log, which b754 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b754, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b754, Component 6 (the Edit tool): the fold bank was b753's own route
# ### (tools/b753_fold.py); b754's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b754_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b758.py -> tools/acts/b759.py' in (rd('b759_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b759_report.py' not in (S['sealj'].get('tools') or {})   # ### b759, before the lock: the carried stub set for the act, b758's body with the act's name
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b759_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:   # ### b759, before the lock: the carried stub set for the act, b758's body with the act's name
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b759')
    return '### THE COUNTER ((R369) Component 5, the act`s events and defects together; relay data/b759_defects.txt, data/b759_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-MECHANISM-ATTRIBUTION open on the author`s word, T0 and T1 entered beside it ((R369)(10)); W-ORD-WSC-KERNEL-CITES, W-ORD-LI-INDEX, W-ORD-CAPACITY-ATTRIBUTION, W-ORD-BIBLIOGRAPHY-LINK and W-ORD-EPSTEIN-SECTIONS-3-4 entered by name in (10)`s block, each priced by no build;',
    '        no W-ORD-RECUT order, (9) leaving no line; the orders before this act as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)   # ### b759, before the lock: the carried stub set, b758's body (b759's listing at 18:41Z, data/b759_stepzero.txt :60)
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b759_author_answers.txt', 'b759_answer_check.txt', 'b759_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b754, defect (m''), Component 4 before the gate (the Edit tool): record.tpl :194 bound DEFECT_ROW to b698's matcher of at most one
# ### prime, which v1.34.0's repair under (R364)(3)(viii) left; b754's letters run to (l''), and letters_of, the defects route, N4's count
# ### and, through b703's module, read_defect_row and _defect_short read 51 of the bank's 63. The one line bound, with b698's, b703's and
# ### b753's module bindings, to the matcher of any number of primes, as tools/standing/close.py :35 and closing.tpl :122 read
#⟪OVERRIDE record MARK 7606fc9891fa 1 REPAIR (reader)⟫
DEFECT_ROW = R.DEFECT_ROW = P3.DEFECT_ROW = P7.DEFECT_ROW = re.compile(r"^    \(([a-z]'*)\) ")   # ### b754 (m''): any number of primes
#⟪END⟫
# ### b754, Component 1 (the Edit tool), tools/standing/ v1.34.0, (R364)(3)(v) and (viii): b753's override of _counter's read (the events
# ### bank optional) retired -- the template's line now carries it, with the post-seal events bank read beside it and a letter of any number
# ### of primes (record.tpl's _counter)
# ### b754, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b753's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b754, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b753's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b759_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b759_registration_%s.txt' % __import__('b759_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b754, Component 4 (the Edit tool, before the face): b753's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b754, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b754's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 10`s EFNEW and EFEDIT.'),
#⟪END⟫
# ### b757, Component 6 (the Edit tool): the template's lines that read "none" of kernel writes, true of every act since b745 and not of this
# ### one, each replaced for b757 by its count and its source ((R367)(3)-(6), (9)); the template stays, the earlier acts' renders unchanged
#⟪OVERRIDE regspec MARK 254ae4810dcb 1⟫
    ('commits on any kernel`s main', 'EFMAINCOMMITS', 'EFMAINCOMMITS', 'commits', '### (R369)(5): SIDE-explicit-formula`s main moved from 630cba16 to the tip of push-b759-weil by the gated push`s default mode after the run`s success, (5)`s two commits; SIDE-dirichlet-mod-24`s remote main unmoved; MEASURED off git rev-list --count 630cba16..main.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 18c1a19a6cb6 1⟫
    ('scratch branches cut on a kernel', 0, 0, 'branches', '### none: the planted controls of (4)(i) in a scratch remote outside the kernels (data/b759_standing_v1363.txt).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK a2b9535083e6 1⟫
    ('push branches cut on a kernel for the push procedure', 1, 1, 'branches', '### push-b759-weil in SIDE-explicit-formula, made at main 630cba16 by the one-call tool and carried by the gated push, kept for the next act`s step zero ((R369)(3)).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 42ab3bdb112d 1⟫
    ('kernel merges made', 0, 0, 'merges', '### none: (5) merges nothing; main moved to the tip of push-b759-weil by the gated push, a fast-forward.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 63e5424dd90e 1⟫
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### N5: v0.41 where the run succeeded, its peel read back at the remote equal to main; v0.38 at 14ca5725, v0.39 at d1afb4fc, v0.40 at 630cba16 and v0.2.0 at e5ebdd15 unmoved; MEASURED off SIDE-explicit-formula`s tags past v0.40, SIDE-dirichlet-mod-24`s past v0.2.0, and the template`s other kernels as before.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 5381b10a2ae6 1⟫
    ef_tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() not in ('v0.37', 'v0.38', 'v0.39', 'v0.40')] + [t for t in _git(K.M24_DIR, 'tag', '--list').split(chr(10)) if t.strip() and t.strip() not in ('v0.1.0', 'v0.2.0')]   # ### b759: v0.38 b745`s, v0.39 and v0.40 b758`s, v0.2.0 b757`s; the tags past them
#⟪END⟫
#⟪OVERRIDE regspec MARK 100638d8d84e 1⟫
    ('kernel branches deleted', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### (R369)(3): ' + ', '.join(b_ for b_, _t in K.KERNEL_DELETES) + ', each removed at its kernel`s remote by (4)(i)`s route after its controls, one per message, each an ancestor of its remote`s main, read absent; port-b707, the pin, challenge and rebuild branches and the four held branches kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 51acd0ac8ef1 1⟫
    ('branches deleted beyond the step zero`s list', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### the five kernel branches of (R369)(3), removed at Component 2 after (4)(i)`s controls; port-b707 kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK b6204f4e0fa8 1⟫
    ('census editions written on main', 0, 0, 'editions', '### none: no new edition; the census v0.8.3 takes (R369)(8)`s one dated note at its end (relay data/b759_notes.json).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 0daf7a1cb287 1⟫
    ('papers moved, renamed or written beyond FINDINGS, OPEN_TRAILS and REGISTRY', 13, 13, 'papers', '### (R369)(8): the new file THE_EPSTEIN_CONTROL_OBJECT_v0_2.md beside v0.1, and one dated note each in FACES_LEDGER.md and THE_KEYSTONE_CENSUS_v0_8_3.md; (9): the fourteen lines in nine documents; (10): ERRATA.md`s two entries; each by one PLACE-papers commit a document; none moved or renamed, v0.1 unchanged.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 46160108b751 1⟫
    ('README edits', 0, 0, 'edits', '### none this act: no kernel`s README written.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 2d7a99569826 1⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 'OTBLOCK', 'OTBLOCK', 'lines', '### (R369)(10): the block under one dated head at the file`s end, no line moving -- b758`s root answer, W-ORD-MECHANISM-ATTRIBUTION`s condition read not met with T0 and T1 beside it, the five orders by name -- by one PLACE-papers commit; MEASURED off relay data/b759_errata.json`s trails row.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 44ff8bc9f5d4 1⟫
    ('faces ledger update blocks appended', 1, 1, 'blocks', '### (R369)(8): one UPDATE section at FACES_LEDGER`s end (:575-:585) in the form of b758`s at :565, no face entered (relay data/b759_notes.json).'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b759_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): G-SCORER-READS-BANKS's needles set to the banks b755's N1-N4 read (the command bank and the
# ### dispatch rows, N2's controls and first adds, the walk among the figure banks, the seal and step banks), the carried stub's refusal
# ### removed; the ledger exclusion unchanged. The arm stands in tools/standing/arms.py's RETIRED and is not in the run list; read so, its
# ### template line :971 would fire on N3's label of the landed entry (record.tpl :2444, a string naming FINDINGS.md), not edited here
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_walk.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b754, (R364)(2)(iii): b753's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b754, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b754_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): the corrigendum's foot carries b754's post-seal events beside its events and defects
# ### (data/b755_corrigendum.txt :47, "EVENTS 79, POST-SEAL 16, DEFECTS 70"); the template's reader wants the two side by side and refused
# ### the foot; read with the post-seal count optional, the seven groups in the template's order
#⟪OVERRIDE record MARK 909ece48c5e6 2⟫
    ci = _bfig('%s_corrigendum.txt' % ACT, r'\*\*ITEMS (\d+): EVENTS (\d+), (?:POST-SEAL \d+, )?DEFECTS (\d+) ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;.*THE ENTRY AT FINDINGS :(\d+)\.\*\*',
               'the corrigendum`s foot')
#⟪END⟫
# ### b754: b753's override of G-DIFFERS-ERRATA (two ERRATA entries at its sitting) retired; b754 writes no ERRATA entry ((R364)(6)), so
# ### the template's arm, ERRATA at HEAD byte-equal to its blob at the act's base, reads b754 as it stands
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'ab'))   # ### b759: the seat's rows of data/b759_defects.txt as the template's reader takes them, (a) and (b), each THE SEAT'S; set again at the seal where a row is added; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b759_misses.txt', 'data/b759_corrigendum.txt',                                                   # ### step zero and Component 1
                  'data/b759_standing_v1363.txt', 'data/b759_standing_v1364.txt', 'data/b759_standing_v1365.txt', 'data/b759_standing_v1366.txt',
                  'data/b759_standing_v1367.txt',                                                                         # ### Component 2, (4)'s four and the kernel route
                  'data/b759_kernel_bases.json', 'data/b759_presend.txt', 'data/b759_targets.json', 'data/b759_controls_control.txt', 'data/b759_controls.txt',
                  'data/b759_dispatch_rows.json', 'data/b759_outcomes.txt', 'data/b759_outcomes.json',                       # ### Component 3, (5)
                  'data/b759_c3table.txt', 'data/b759_costlaw.txt', 'data/b759_fields.txt', 'data/b759_fields.json',         # ### Component 4, (6) and (7)
                  'data/b759_compose.txt', 'data/b759_notes.json',                                                         # ### Component 5, (8)
                  'data/b759_corpus.txt', 'data/b759_corpus.json', 'data/b759_fields_corpus.txt', 'data/b759_fields_corpus.json',
                  'data/b759_errata.json', 'data/b759_reproduce.txt', 'data/b759_reproduce.json',                           # ### Component 6, (9), (10) and (11)
                  'data/b759_ceiling.txt', 'data/b759_author_answers.txt', 'data/b759_address_scan.txt', 'data/b759_touch.txt',   # ### b759, before the lock: the act's banks by its components, in place of b758's carried names; no amendments bank this act (none written); the template's standing banks follow
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b759_address_scan.py'), 'scan'], capture_output=True, text=True,
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


def _chain():
    """(R369)(1)-(11): the act's relay commits after step zero in their order, (key, commit) -- v9, then the worklist's CHAIN (the standing
    versions v1.36.3 to v1.36.7, the c1 route and the corrigendum banks, the act's tools each before its bank, the pre-send and the
    dispatches' rows, the outcomes, the table and the cost law, the fields, the document, the notes, the corpus, the errata and the ceiling),
    then the handoff page and the lock gate where each is made, in that order; read from the worklist at the call. A lock gate tool
    committed inside CHAIN before the handoff page is read at its place in CHAIN and not again after the handoff (N2's "each act tool
    commits before it runs" read there), as b758 read it."""
    c = [('v9', K.STANDING_COMMIT)] + list(K.CHAIN)
    in_ = set(h_[:8] for _k, h_ in K.CHAIN)
    c += [(k_, h_) for k_, h_ in (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT), ('lockgate', K.C1_LOCKGATE)) if h_ and h_[:8] not in in_]
    return c


def _anc_pairs():
    """the ancestry pairs of _chain, each commit beside the next; the pair from v9 keeps the name the surgery arm reads."""
    c = _chain()
    return [('v9_v1310', c[0][1], c[1][1])] + [('%s_%s' % (a[0], b[0]), a[1], b[1]) for a, b in zip(c[1:], c[2:])]


def _gens_state():
    """(R366)(3)-(5), N2: each tool of K.GENS by its name -- the bank in the working tree and its blob at its commit; the tool's first add
    (the oldest commit adding it) against the first of its commits; the files of each of its commits and of the bank's; their times."""
    out = {}
    for n_, tool_, gens_, data_, bank_ in K.GENS:
        out[n_] = dict(tool=tool_, data=data_, bank=rd(data_.split('/', 1)[1]), blob=_s(blob(ROOT, '%s:%s' % (bank_, data_))),
                       gen_first=[h_ for h_ in gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', tool_).split() if h_.strip()][-1:],
                       gen_full=gs(ROOT, 'rev-parse', gens_[0]).strip(),
                       gen_files=[files_of(ROOT, h_) for h_ in gens_], bank_files=files_of(ROOT, bank_),
                       t_gen=[_ct(ROOT, h_) for h_ in gens_], t_bank=_ct(ROOT, bank_))
    return out


def _gens_ok(S, names=None):
    """each generator first added by the first of its commits, every one of its commits carrying it and not its bank, the bank's commit
    carrying the bank and not the generator, every generator commit before the bank's, the bank at HEAD its blob there; (name, ok) each."""
    out = []
    for n_, d_ in sorted((S['gens'] or {}).items()):
        if names is not None and n_ not in names:
            continue
        gf_, bf_, tg_ = d_.get('gen_files') or [[]], d_.get('bank_files') or [], d_.get('t_gen') or [None]
        b_ = _txt(d_.get('bank'))
        out.append((n_, bool(b_) and b_ == _txt(d_.get('blob')) and bool(d_.get('gen_first')) and d_['gen_first'][0] == d_.get('gen_full')
                    and all(d_['tool'] in f_ and d_['data'] not in f_ for f_ in gf_) and d_['data'] in bf_ and d_['tool'] not in bf_
                    and all(tg_) and bool(d_.get('t_bank')) and max(tg_) < d_['t_bank']))
    return out


def _kernel_state():
    """b757, (R367)(3)-(7): the two kernels' refs as G-OFFSET-POST-HOC reads them, no remote read -- each local head, tracking ref and tag
    by its full name, (object, peel; '' where the ref is no tag), and for each kernel commit of the worklist the refs that contain it."""
    out = {}
    for kd_, nm_ in ((K.EF_DIR, 'ef'), (K.M24_DIR, 'm24')):
        refs_ = {}
        for l_ in gs(kd_, 'for-each-ref', '--format=%(refname) %(objectname) %(*objectname)').split(NL):
            p_ = l_.split()
            if p_:
                refs_[p_[0]] = (p_[1], p_[2] if len(p_) > 2 else '')
        out[nm_] = refs_
    out['contains'] = dict((k_, [r_ for r_ in gs(K.EF_DIR if kn_ == 'SIDE-explicit-formula' else K.M24_DIR, 'for-each-ref', '--contains', c_,
                                                 '--format=%(refname)').split() if r_.strip()]) for k_, kn_, c_, _b in K.KERNEL_COMMITS)
    return out
#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R366)(1)-(7) (b756's keys over b756's objects): the order by time and ancestry; the seven standing versions' controls; each tool
        # ### before its bank; the map, the notes, the orders, the put and the passed writes; the fault count, the placing and the README route;
        # ### zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b753's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in _anc_pairs()),
        # ### b756 (R366)(1), (3), (5): PLACE-papers by ancestry -- the act's base, each commit of the worklist's PP_CHAIN in its order, HEAD on the last
        ancpp=dict(('%s_%s' % (a_[0], b_[0]), subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a_[1], b_[1]]).returncode == 0)
                   for a_, b_ in zip([('pre', K.PRE_PP)] + list(K.PP_CHAIN), list(K.PP_CHAIN) + [('head', 'HEAD')])),
        pp_log=[l for l in gs(PP, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_PP).split() if l.strip()],
        # ### the seven standing versions ((R366)(1), (5)(i), (6)): each controls bank in the working tree and its blob at its own commit; the act's
        # ### relay commits under tools/standing/, oldest first
        stbanks=dict((v_, (rd(b_.split('/', 1)[1]), _s(blob(ROOT, '%s:%s' % (c_, b_))))) for v_, c_, b_, _n in K.STANDING_BANKS),
        st_commits=[h_ for h_ in gs(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()],
        r366_chain=_chain(),
        gens=_gens_state(),
        # ### b759, before the lock: the act's banks its arms read -- the notes of (8), the ceiling at HEAD and at the commit of its last
        # ### reading, the outcomes of (5), the corpus lines of (9), the errata of (10), the fields N and DEPOSITS; and the sha256 (16 hex) of
        # ### each PLACE-papers file's blob at the commit that wrote it, against which the banks' new_sha are read; b758's merge, statements and
        # ### moved-cites banks have no counterpart at this act and are not read
        notesj=jl('b759_notes.json'),
        ceiling=(rd('b759_ceiling.txt'), _s(blob(ROOT, '%s:data/b759_ceiling.txt' % K.C1_CEILING))),
        outc=jl('b759_outcomes.json'), corpusj=jl('b759_corpus.json'), errataj=jl('b759_errata.json'), fcorpj=jl('b759_fields_corpus.json'),
        compose=rd('b759_compose.txt'), corpus=rd('b759_corpus.txt'),
        pp_shas=dict(('%s:%s' % (c_[:8], f_), hashlib.sha256(blob(PP, '%s:%s' % (c_, f_)) or b'').hexdigest()[:16])
                     for _k, f_, c_ in K.C3_NOTES_PP + K.C3_CORPUS_PP + K.C3_ERRATA_PP + (('doc',) + K.C3_DOC_PP,)),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        pp_files=dict((k_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        numstat=dict((k_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        kst=_kernel_state(),   # ### b757: the two kernels' refs, tags and the kernel commits' containing refs (G-OFFSET-POST-HOC)
        drows=json.loads(rd('b759_dispatch_rows.json') or '[]'), reproduce=rd('b759_reproduce.txt'), reproducej=jl('b759_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b759_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b759_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [(k_, _ct(PP, h_)) for k_, h_ in K.PP_CHAIN]
               + [('c1', _ct(ROOT, K.C1_RELAY)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)), ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), lockgate=files_of(ROOT, K.C1_LOCKGATE) if K.C1_LOCKGATE else [], c2=[],   # ### b757: the lock gate set when made; no Component 2 relay bank of b756's kind
                   v9=files_of(ROOT, K.STANDING_COMMIT), handoff=files_of(ROOT, K.HANDOFF_COMMIT) if K.HANDOFF_COMMIT else [],
                   **dict([('rc_' + k_, files_of(ROOT, h_)) for k_, h_ in K.CHAIN] + [('pp_' + k_, files_of(PP, h_)) for k_, h_ in K.PP_CHAIN]),   # ### b756: each commit of the two chains by its key
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b755's read-first bank's items by path, the ferry's read-first list in its order (data/b755_readfirst_rows.json); b755 step zero: the
# ### carried stub replaced, one needle for each item of the ferry's list (:44) and for the act's own reads beside it
# ### b756 step zero: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b756_ferry.txt :46), in its order
# ### b757, Component 6: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b757_ferry.txt :41), in its
# ### order, as data/b757_readfirst.txt :14-:35 holds them
# ### b758, Component 5: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b758_ferry.txt :37), in its
# ### order, as data/b758_readfirst.txt :14-:26 holds them
# ### b759, before the lock: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b759_ferry.txt :43), in
# ### its order, as data/b759_readfirst.txt :16-:35 holds them
READFIRST_NEEDLES = (
    'relay data/b758_closing.txt |',
    'relay data/b758_defects.txt |',
    'relay data/b758_events.txt |',
    'relay data/b758_epstein_statements.txt |',
    'relay data/b758_presend.txt |',
    'relay data/b758_outcomes.txt |',
    'relay data/b718_derivation.txt |',
    'relay data/b721_derivation.txt |',
    'relay data/b753_registrations.txt |',
    'relay data/b755_walk.txt |',
    'relay data/b750_cq_sign.txt |',
    'relay data/b744_zetabox_plan.txt |',
    'relay data/b742_offlinezero.txt |',
    'relay tools/b718_abstract.py |',
    'relay tools/b750_cq_sign.py |',
    'relay tools/b758_controls.py |',
    'relay tools/b758_statements.py |',
    'relay tools/standing/allow.py |',
    'relay tools/push_gated.sh |',
    'PLACE-papers phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R369)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'STANDING CHANGES ((R369)(1), (3), (4), (6))', 'LANDING ((R369)(4))', 'THREE RESULTS ((R369)(5))', 'CEILING ((R369)(2))',
 'STATEMENTS FOR SECTIONS 6 TO 8 ((R369)(7))', 'NOTES OF (8) ((R369)(8))',
 'NAME AND ADDRESS (N5)', 'RESEARCH INSTRUMENTS NOT REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', 'TOUCH READ (standing clauses v9)')   # ### b758: closing 7's sections, the ferry's components in order
#⟪END⟫
#⟪SECTION checks 12⟫
    """b759: the citation check's bank: every cite checked, OK and misses summing (78 = 77 + 1, data/b759_citation_check.txt :147), the one
    miss the ruling's own, (7)'s cite of data/b744_zetabox_plan.txt :134 for a figure standing at :135 (:39, :85; data/b759_events.txt (11)),
    entered and not repaired; the ferry's paths 53, OK 43, NONE 1, the new file of (8) (:148); the check CLEAN (:149, halts 0: Lean paths and
    nouns 0, comparatives 0), as the step-zero bank enters it (data/b759_stepzero.txt :56-:57, after the read-first bank and the subject read,
    before the deletes); the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 1 and int(m.group(1)) == 78 \
        and 'data/b744_zetabox_plan.txt :134' in json.dumps(S['cit_misses'], ensure_ascii=False) \
        and '### ### **THE CHECK CLEAN** (halts 0: Lean paths and nouns 0, comparatives 0)' in c \
        and 'THE CITATION CHECK BANKED (' in (S['stepz'] or '') and 'CITES CHECKED 78 ; OK 77 ; MISSES 1 (:134, the ruling' in (S['stepz'] or '') \
        and 'NONE 1 (the new file of (8)) ; OWN 9 ; THE CHECK CLEAN' in (S['stepz'] or '') \
#⟪END⟫
# ### b754, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b753's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b754, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b759_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b759, (R369)(1): no weight line ordered (the c1 route refuses one; data/b759_corrigendum.txt's foot NO WEIGHT LINE), so the
    # ### record-lines bank holds none; b758 at its weight stands in the corrigendum's line, FINDINGS :15550 (PLACE-papers c71ebcd2, step 7),
    # ### read through the corrigendum's landing bank, its head through conv; a planted record-lines line is read in its place
    return landed(S if S['rl'] else dict(S, rl=jl('b759_corrigendum_landing.json')), 0,
                  ['b758’s record, short', 'data/b758_events.txt rows (1)-(72)', 'data/b758_defects.txt (a)-(h)', 'no CLAIM item among them'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b759's title by its objects, the ferry's ACT line (data/b759_ferry.txt :39) adjusted to what the act did (record 31's _title over the
# ### banks' feet, printed by scratch title759.py through tools/standing/fold.py load, writing nothing, 22:44Z: b758 at its weight; 4 of 4;
# ### landed at v0.41 = a3aad4cc; the table reproduced, 27 of 27; 52 fields (50 and N and DEPOSITS); 551 lines; 14 of 14; 1 dispatch);
# ### each needle composed with the typographic apostrophe, no backtick, conv(title) == title
TITLE_NEEDLES = ('## The Epstein document at v0.2 under (R369): b758’s close at its weight (b759_corrigendum)',
                 'four standing changes, 4 of 4 (b759_standing_v1363 to b759_standing_v1366)',
                 'the statement and four print lines landed at v0.41 = a3aad4cc (b759_presend, b759_outcomes)',
                 'the table of Appendix A reproduced, 27 of 27 cells by each route (b759_c3table)',
                 '52 fields filled (b759_fields)',
                 'the document entered at v0.2, 0 fields left, 551 lines (b759_compose, b759_notes)',
                 '14 of 14 corpus lines re-cut (b759_corpus)',
                 '1 dispatch (b759_dispatch_rows)')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R369)(1): the generated corrigendum for b758's record landed, short (its line in the json, FINDINGS :15550, the title at that line
    through conv): b758's 72 events and 8 defects by count from their banks, 80 items, CLAIM 0 and CLOSE 80, REPEAT 30, no CLAIM item
    among them as (1) says; the five findings after b758's lock entered as b759's events (17)-(21) (CLAIM 0, CLOSE 5, REPEAT 3), each with
    its time; no weight line; the corrigenda bank appended at row (79) and nothing before it changed; in Component 1's commits (the figures
    read from data/b759_corrigendum.json and the bank's foot, :13)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 79 and j.get('claim') == 0 == len(j.get('claims') or []) and j.get('close') == 80 and j.get('repeat') == 30 \
        and '### ### **ITEMS 80: EVENTS 72, DEFECTS 8 ; CLAIM 0, CLOSE 80 ; REPEAT 30 ; THE CLAIM ITEMS 0 ; THE FINDINGS AFTER THE LOCK 5: CLAIM 0, CLOSE 5, REPEAT 3 ; ' in (S['corrt'] or '') \
        and 'NO WEIGHT LINE ; THE ENTRY AT FINDINGS :15550.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('claims') or []) == [] and j.get('in_full') is None \
        and (j.get('findings') or {}).get('rows') == [str(n_) for n_ in range(17, 22)] \
        and [(j.get('findings') or {}).get(k_) for k_ in ('claim', 'close', 'repeat')] == [0, 5, 3] \
        and j.get('weight_line') is None \
        and '  (79) ' in S['corrigenda'] and '  (80) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R369) orders no rules bank for this act, nor did (R368) or (R367); the rule it works by is
    b756's, data/b756_rules.txt, its rows (a) to (c) in force from b757 by (R366)(2); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here b756's rows (a) to (c), lettered as (R366)(2) letters them, in b756's Component 1 commit (relay 0a151012) and no other, the working
    tree its blob at HEAD; no data/b759_rules.txt written (the worklist's C1_RULES None), as none was at b758 (its defect (e): the carry had
    shifted the bank's name to b757's, which no commit holds)."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and re.findall(r'(?m)^  \(([a-z])\) ', rd('b756_rules.txt') or '') == ['a', 'b', 'c'] \
        and not r1 and K.C1_RULES is None and not os.path.exists(os.path.join(D, 'b759_rules.txt')) \
        and _txt(rd('b756_rules.txt')) == _txt(blob(ROOT, 'HEAD:' + K.B756_RULES[0])) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', K.B756_RULES[0]).split()] == [K.B756_RULES[1][:8]] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b759's report lines (report sections 2-5): each key a phrase its line carries; the statement's line read by the words both tiers
# ### carry (KERNEL where landed, HELD where not), each tier read by the report's footing
REPORT_KEYS = (' -- THE STATEMENT',
               'CERTIFIED -- tools/standing/ v1.36.3 TO v1.36.7', 'CERTIFIED -- tools/b759_controls.py BY ITS OWN CONTROLS',
               'CERTIFIED -- THE TABLE OF APPENDIX A ', 'CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED',
               'REGISTERED -- THE DOCUMENT AT v0.2', 'REGISTERED -- WHERE ELSE (8) IS WRITTEN', 'REGISTERED -- THE FIELDS OF (7)',
               'REGISTERED -- THE CORPUS LINES OF (9)', 'REGISTERED -- ERRATA AND THE ORDERS OF (10)',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b759 ((R369)(10)): every runner dispatch of the act sent by tools/b759_controls.py's dispatch route, one command in the
    capture for each dispatch row (one to three, each in SIDE-explicit-formula, none in SIDE-dirichlet-mod-24), each read once after it by its
    run id, every dispatch and read row's free memory at or above the hold; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### b758: the act's own rows, each dispatch and its read; the order read by the loop above, by run id
    order = order and len(seq_) == 2 * len([r for r in rows if r.get('kind') == 'dispatch'])
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b759_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) + len(K.M24_RUNS) == len(cmds) \
        and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES == 3 and len(K.M24_RUNS) == K.MAX_DISPATCHES_M24 == 0 \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b759 step zero, (R369)(5): one to three dispatches in SIDE-explicit-formula ((5)'s), none in SIDE-dirichlet-mod-24 ((11))
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5, (R369)(8)-(11): PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the corrigendum and the entry; the new file of
    (8), phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md; REGISTRY: (8)'s row and dated note; FACES_LEDGER and the census: (8)'s
    notes; the documents of (9)'s fourteen lines; ERRATA: (10)'s two entries; OPEN_TRAILS: (10)'s block under one dated head, and the
    trail), the ledgers changed; v0.1 unchanged; no rename; no other paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b759's headings and banks, as its _finding_text (record 34) writes them (printed by scratch title759.py, 22:44Z); the last the
# ### INTEGRATION line's opening words (_integ_line)
ENTRY_NEEDLES = ('**b758 at its weight and the corrigendum**', '**The four standing changes**', '**The statement and the print lines**', '**The table of Appendix A**',
                 '**The fields**', '**The document**', '**The corpus lines**', '**ERRATA and the orders**', '**The research instruments reproduced**',
                 '**The ceiling**', '**The order of the act**', '**What this act is not**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b759_misses.txt', 'data/b759_corrigendum.txt', 'data/b759_standing_v1363.txt', 'data/b759_standing_v1367.txt', 'data/b759_presend.txt',
                 'data/b759_controls_control.txt', 'data/b759_controls.txt', 'data/b759_dispatch_rows.json', 'data/b759_outcomes.txt', 'data/b759_c3table.txt',
                 'data/b759_costlaw.txt', 'data/b759_fields.txt', 'data/b759_compose.txt', 'data/b759_notes.json', 'data/b759_corpus.txt', 'data/b759_errata.json',
                 'data/b759_reproduce.txt', 'data/b759_ceiling.txt', 'data/b759_events.txt', 'data/b759_address_scan.txt', 'data/b759_touch.txt',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: the statement: ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R369)(1), (8)-(10), N4, N5 (the name the frozen run list carries): PLACE-papers written by the worklist's PP_CHAIN in its order and
    by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone, the act's first on its base (no weight line,
    (1) ordering none); (8)'s document in one commit adding its one new file and removing nothing, v0.1 not in it; (8)'s three notes each in
    one commit touching its one file and removing no line; (9)'s nine documents each in one commit touching its one file, removing as many
    lines as it adds, one for each line its keys re-cut; (10)'s ERRATA and OPEN_TRAILS each in one commit removing no line; each file's blob
    at its commit the sha256 its bank wrote and read back (the compose bank's file, the notes, the corpus and the errata banks); the changed
    files since the base within PP_WRITTEN; by ancestry the base, each commit of the chain and HEAD; the earlier acts' registrations at HEAD
    their blobs."""
    pf_, ns_, sh_ = S['pp_files'] or {}, S['numstat'] or {}, S['pp_shas'] or {}
    pc_ = dict(K.PP_CHAIN)
    nj_ = dict((r_.get('item'), r_) for r_ in (S['notesj'] if isinstance(S['notesj'], list) else []) if isinstance(r_, dict))
    ej_ = dict((r_.get('item'), r_) for r_ in (S['errataj'] if isinstance(S['errataj'], list) else []) if isinstance(r_, dict))
    cj_ = S['corpusj'] if isinstance(S['corpusj'], dict) else {}
    cd_ = dict((d_.get('path'), d_) for d_ in (cj_.get('docs') or []) if isinstance(d_, dict))
    lines_ = dict((p_, len(set(r_.get('line') for r_ in (cj_.get('rows') or []) if r_.get('path') == p_))) for p_ in cd_)
    def sha_(c_, f_, w_):
        return bool(w_) and sh_.get('%s:%s' % (c_[:8], f_)) == w_
    cs_ = re.search(r'(?m)^  v0\.2: \d+ lines, \d+ bytes, sha256 ([0-9a-f]{16}) ;', S['compose'] or '')   # ### the compose bank's v0.2 line (:25), not v0.1's (:15)
    want_ = [('c1pp', ['FINDINGS.md'], '0', True), ('pp_doc', [K.C3_DOC_PP[0]], '0', bool(cs_) and sha_(K.C3_DOC_PP[1], K.C3_DOC_PP[0], cs_.group(1)))] \
        + [('pp_' + it_, [f_], '0', (nj_.get(it_) or {}).get('read_back') is True and sha_(c_, f_, (nj_.get(it_) or {}).get('new_sha'))) for it_, f_, c_ in K.C3_NOTES_PP] \
        + [(k_, [f_], str(lines_.get(f_, -1)), (cd_.get(f_) or {}).get('commit', '')[:8] == c_[:8] and bool((cd_.get(f_) or {}).get('confirmed'))
            and sha_(c_, f_, (cd_.get(f_) or {}).get('new_sha'))) for k_, (_ks, f_, c_) in zip([k_ for k_, _h in K.PP_CHAIN if re.match(r'pp_c\d+$', k_)], K.C3_CORPUS_PP)] \
        + [('pp_' + it_, [f_], '0', (ej_.get(it_) or {}).get('read_back') is True and sha_(c_, f_, (ej_.get(it_) or {}).get('new_sha'))) for it_, f_, c_ in K.C3_ERRATA_PP]
    rows_ = [(k_, sorted(pf_.get(k_) or []) == sorted(fs_) and bool(ns_.get(k_)) and all(x_ == rm_ for x_ in (ns_.get(k_) or [])[1::3])
              and (rm_ == '0' or (ns_.get(k_) or [])[0::3] == (ns_.get(k_) or [])[1::3]) and ok_) for k_, fs_, rm_, ok_ in want_]
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:len(K.PP_CHAIN)]] == [h_[:8] for _k, h_ in K.PP_CHAIN]
    return len(rows_) == len(K.PP_CHAIN) == 16 and set(k_ for k_, _o in rows_) == set(pc_) and all(o_ for _k, o_ in rows_) and order_ \
        and 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' not in S['pp_head_files'] \
        and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b759_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R369)(1)-(11), N2, N4 (the name the frozen run list carries): the act's order by time -- the worklist's TIME_ORDER, relay and
    PLACE-papers together (the act_current commit, step zero's banks, the c1 route, PLACE-papers' corrigendum and the corrigendum banks,
    the four standing changes of (4) and the kernel route before any kernel write, each act tool before its bank, the pre-send and the
    dispatch rows, the outcomes, the table and the cost law, the fields, the document, the notes, the corpus lines, the errata and the
    ceiling's readings), then the handoff page and the lock gate where made; by ancestry within the relay from v9 through each commit of
    _chain; each of the five standing versions' banks at HEAD its blob at its commit (v1.36.3 to v1.36.7), its foot ALL AS WANTED at the
    worklist's cases, VERSION and the bank in that commit's files; the act's commits under tools/standing/ those five and no other."""
    t_ = S['t']
    ks_ = list(K.TIME_ORDER) + [k_ for k_, _h in S['r366_chain'] if k_ in ('passed', 'handoff', 'lockgate') and k_ not in K.TIME_ORDER]
    sb_ = []
    for v_, c_, b_, n_ in K.STANDING_BANKS:
        bk_, bl_ = (S['stbanks'] or {}).get(v_, (None, None))
        m_ = re.match(r'^%s: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.$' % re.escape(v_), _vlast(_txt(bk_)))
        ck_ = [k_ for k_, h_ in K.CHAIN if h_ == c_]
        sb_.append(bool(bk_) and _txt(bk_) == _txt(bl_) and bool(m_) and int(m_.group(1)) == int(m_.group(2)) == n_ and len(ck_) == 1
                   and 'tools/standing/VERSION' in S['files'].get('rc_' + ck_[0], []) and b_ in S['files'].get('rc_' + ck_[0], []))
    st_ = [h_[:8] for h_ in S['st_commits'] or []] == [c_[:8] for _v, c_, _b, _n in K.STANDING_BANKS]
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and len(S['anc']) == len(S['r366_chain']) - 1 and all(v is True for v in S['anc'].values()) \
        and len(sb_) == len(K.STANDING_BANKS) == 5 and all(sb_) and st_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R369)(2), (5)-(10), N2, N3 (the name the frozen run list carries): each tool of K.GENS first added by a commit of its own, every one
    of its commits carrying it and not its bank, the bank's commit carrying the bank and not the tool and after every tool commit, the bank
    at HEAD its blob there (the pre-send reads with (5)'s salt check, the controls tool, the composer of the outcomes, (6)'s table, (7)'s
    cost law and fields, (8)'s document and notes, (9)'s corpus lines, (10)'s errata, the ceiling); no tool committed with its bank
    (GENS_WITH_BANK empty); the outcomes bank's foot the outcomes json's word for (5), its runs one to three; the ceiling at HEAD its blob
    at the commit of its last reading, two readings or more, nothing carried; the pre-send's, the tool controls', the table's, the cost
    law's and the reproduction run's feet as the entry reads them."""
    gk_ = _gens_ok(S)
    ce_ = S['ceiling'] or (None, None)
    cv_ = re.match(r'^THE CEILING: READINGS (\d+) ; THE LAST AT \S+, [\d.]+ h OF 16 ; NOTHING CARRIED ; DISPATCHES (\d+) OF 3\.$', _vlast(_txt(ce_[0])))
    ceil_ = bool(ce_[0]) and _txt(ce_[0]) == _txt(ce_[1]) and bool(cv_) and int(cv_.group(1)) >= 2
    ow_ = dict((r_.get('item'), r_.get('outcome') or 'NOT READ') for r_ in (S['outc'] if isinstance(S['outc'], list) else []) if isinstance(r_, dict))
    of_ = re.match(r'^THE OUTCOME OF \(5\): (.+?) ; RUNS READ (\d+) ; CONTROLS (\d+) OF (\d+)\.$', _vlast(_txt(rd('b759_outcomes.txt'))))
    out_ = bool(of_) and of_.group(1) == ow_.get('weil') and 1 <= int(of_.group(2)) <= 3 and of_.group(3) == of_.group(4)
    ps_ = _vlast(_txt(rd('b759_presend.txt')))
    feet_ = [('b759_controls_control.txt', 'THE TOOL`S CONTROLS: 17 OF 17 AS WANTED ; ALL AS WANTED.'),
             ('b759_c3table.txt', 'THE TABLE OF APPENDIX A: REPRODUCED ; ROUTE ONE AGREES 27 OF 27 ; ROUTE TWO AGREES 27 OF 27 ; (a) HOLDS ; (b) HOLDS ; THE PLANT FAILS AS WANTED.'),
             ('b759_costlaw.txt', 'F1 8.88 (THE QUOTIENT 8.88, AGREEING WITHIN ONE PART IN A HUNDRED, THE SENTENCE STANDS) ; F2 1.1 × 10^9 ; INSTRUMENTS :556 CARRYING BOTH HEIGHTS ; CONTROLS 5 OF 5.'),
             ('b759_reproduce.txt', 'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4 ; PLANTED CONTROLS AS WANTED 64 OF 64 ; 354 s.')]
    ft_ = [_vlast(_txt(rd(n_))) == w_ for n_, w_ in feet_] + [
        ps_.startswith('THE PRE-SEND READS AT a3aad4cc: DUPLICATES 0 ') and ' ; REFUSED BY THE FILTER 2 (:358, :359), THE TWO KNOWN YES ; ' in ps_
        and ' ; THE SALT CHECK PASSED ; ' in ps_ and ps_.endswith(' ; CONTROLS 16 OF 16.')]
    return len(gk_) == len(K.GENS) >= 8 and all(o_ for _n, o_ in gk_) and K.GENS_WITH_BANK == () and ceil_ and out_ and all(ft_)


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R369)(3), (5), (11) (the name the frozen run list carries): the two kernels as the act left them, read locally with no remote
    read -- SIDE-explicit-formula's main locally and at its tracking ref at (5)'s commit two a3aad4cc where (5) landed, else at the act's
    entering main 630cba16; v0.41's object 390506fc peeling to main where (5) landed and no v0.41 else; v0.39 peeling to d1afb4fc and v0.40
    to 630cba16, unmoved, no other tag past v0.38, v0.38's object 21c6edaf and peel 14ca5725; its four held branches at their entering tips
    locally and at origin, zq-b730 at 1e658870; push-b759-weil at a3aad4cc locally and at origin, kept for the next act's step zero; the four
    branches (3) removed at SIDE-explicit-formula's remote absent from its tracking refs, push-b757-mod24 from SIDE-dirichlet-mod-24's, each
    named in the worklist's KERNEL_DELETES; (5)'s two kernel commits on the remote main; SIDE-dirichlet-mod-24's main at e5ebdd15 at its
    tracking ref and locally, v0.2.0's object e5c84316 peeling to e5ebdd15, v0.1.0 at 597b0869 and no other tag; no sitting kernel."""
    ks_ = S['kst'] or {}
    ef_, m4_, ct_ = ks_.get('ef') or {}, ks_.get('m24') or {}, ks_.get('contains') or {}
    def h_(d_, r_):
        return (d_.get(r_) or ('', ''))[0]
    def p_(d_, r_):
        return (d_.get(r_) or ('', ''))[1]
    l5_ = (dict((r_.get('item'), r_.get('outcome')) for r_ in (S['outc'] if isinstance(S['outc'], list) else []) if isinstance(r_, dict)).get('weil') or '').startswith('LANDED')
    mn_ = h_(ef_, 'refs/heads/main')
    tg_ = sorted(r for r in ef_ if re.match(r'^refs/tags/v0\.(39|[4-9]\d)', r))
    gone_ = [b_ for b_, _t in K.KERNEL_DELETES if b_ != 'push-b757-mod24']
    ef_ok = mn_ == h_(ef_, 'refs/remotes/origin/main') and mn_ == (K.WEIL_TAG[2] if l5_ else K.EF_BASE) \
        and all(h_(ef_, 'refs/heads/' + b) == t == h_(ef_, 'refs/remotes/origin/' + b) for b, t in K.EF_BRANCHES) and K.ZQ_TIP == K.ZQ_ENTERING \
        and h_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[1] and p_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[2] \
        and tg_ == ['refs/tags/v0.39', 'refs/tags/v0.40'] + (['refs/tags/v0.41'] if l5_ else []) \
        and p_(ef_, 'refs/tags/v0.39') == K.LAND_BRANCH[1] and p_(ef_, 'refs/tags/v0.40') == K.COEFF_LAND_BRANCH[1] \
        and (not l5_ or (h_(ef_, 'refs/tags/v0.41') == K.WEIL_TAG[1] and p_(ef_, 'refs/tags/v0.41') == K.WEIL_TAG[2] == mn_)) \
        and h_(ef_, 'refs/heads/' + K.WEIL_BRANCH[0]) == K.WEIL_BRANCH[1] == h_(ef_, 'refs/remotes/origin/' + K.WEIL_BRANCH[0]) \
        and sorted(gone_) == sorted(b_ for b_, _t in (K.JOIN_BRANCH, K.COEFF_BRANCH, K.LAND_BRANCH, K.COEFF_LAND_BRANCH)) \
        and not [b_ for b_ in gone_ if 'refs/remotes/origin/' + b_ in ef_]
    kc_ = len(K.KERNEL_COMMITS) == 2 and all(b == 'main' and 'refs/remotes/origin/main' in ct_.get(k, []) for k, _kn, _c, b in K.KERNEL_COMMITS)
    m4_ok = h_(m4_, 'refs/remotes/origin/main').startswith(K.M24_MAIN) and h_(m4_, 'refs/heads/main')[:8] == K.M24_MAIN[:8] \
        and h_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[1]) and p_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[2]) \
        and p_(m4_, 'refs/tags/v0.1.0').startswith(K.M24_BASE) and sorted(r for r in m4_ if r.startswith('refs/tags/')) == ['refs/tags/v0.1.0', 'refs/tags/v0.2.0'] \
        and ('push-b757-mod24', 'e5ebdd15') in K.KERNEL_DELETES and 'refs/remotes/origin/push-b757-mod24' not in m4_
    return ef_ok and kc_ and m4_ok and not K.SITTING_TIPS

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.34.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1310') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b758's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R369)(7)-(10), N1, N3 (the name the frozen run list carries): the counts the entry and the root prompt carry, each read from its
    bank -- the notes bank's three items (REGISTRY's row and note, FACES_LEDGER's note, the census's note) in (8)'s order, each at its file
    and read back, the worklist's count 3; the corpus bank's fourteen keys of BLOCK D each RE-CUT, none left and no order entered, its nine
    documents each changed, committed alone and confirmed, the foot RE-CUT 14 OF 14 with one deposited copy, N in the fields' corpus bank
    equal to the count re-cut; the errata bank's two items, ERRATA's two entries and OPEN_TRAILS' block, each read back; the dispatches by
    their rows, one to three in SIDE-explicit-formula and none in SIDE-dirichlet-mod-24, each run the worklist's and read once after its
    dispatch; b746's draft unchanged; no Zenodo tool this act."""
    nr_ = S['notesj'] if isinstance(S['notesj'], list) else []
    notes_ = [r_.get('item') for r_ in nr_ if isinstance(r_, dict)] == [it_ for it_, _f, _c in K.C3_NOTES_PP] == ['reg', 'faces', 'census'] \
        and all(r_.get('file') == f_ and r_.get('read_back') is True for r_, (_i, f_, _c) in zip(nr_, K.C3_NOTES_PP)) and len(K.C3_NOTES_PP) == K.C3_NOTES_WRITTEN == 3
    cj_ = S['corpusj'] if isinstance(S['corpusj'], dict) else {}
    sm_ = cj_.get('summary') or {}
    keys_ = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8a', 'C8b', 'C9a', 'C9b', 'C11a', 'C11b', 'C10']
    docs_ = [d_ for d_ in (cj_.get('docs') or []) if isinstance(d_, dict)]
    sweep_ = [r_.get('key') for r_ in (cj_.get('rows') or [])] == keys_ and all(r_.get('state') == 'RE-CUT' for r_ in cj_.get('rows') or []) \
        and sorted(sm_.get('recut') or []) == sorted(keys_) and sm_.get('left') == [] and sm_.get('orders') == [] \
        and [d_.get('path') for d_ in docs_] == [f_ for _k, f_, _c in K.C3_CORPUS_PP] \
        and all(d_.get('changed') is True and (d_.get('commit') or '')[:8] == c_[:8] and bool(d_.get('confirmed')) for d_, (_k, _f, c_) in zip(docs_, K.C3_CORPUS_PP)) \
        and _vlast(_txt(S['corpus'])) == 'RE-CUT 14 OF 14 ; LEFT 0 ; ORDERS 0 ; DEPOSITED COPIES 1 ; CONTROLS 4 OF 4.' \
        and str((S['fcorpj'] or {}).get('N')) == str(len(sm_.get('recut') or [])) == '14'
    er_ = S['errataj'] if isinstance(S['errataj'], list) else []
    rep_ = [[r_.get('item') for r_ in er_ if isinstance(r_, dict)] == [it_ for it_, _f, _c in K.C3_ERRATA_PP] == ['errata', 'trails'],
            all(r_.get('read_back') is True for r_ in er_),
            ((er_[0] if er_ else {}).get('notes') or {}).get('entries') == ['E-2026-11-17-1', 'E-2026-11-17-2']]
    moved_ = True   # ### (carried name) no moved cites this act
    rows_ = S['drows'] or []
    ds_ = [r_ for r_ in rows_ if r_.get('kind') == 'dispatch']
    def _runs(kn_):
        return [int(r_.get('run')) for r_ in ds_ if r_.get('kernel') == kn_]
    rd1_ = all(sum(1 for x_ in rows_ if x_.get('kind') == 'read' and str(x_.get('run')) == str(d_.get('run'))) == 1
               and rows_.index(d_) < next(i_ for i_, x_ in enumerate(rows_) if x_.get('kind') == 'read' and str(x_.get('run')) == str(d_.get('run'))) for d_ in ds_)
    # ### b759 step zero: the dispatch term read against (R369)(5)'s cap and rewritten to it (1 to 3 in SIDE-explicit-formula, none in
    # ### SIDE-dirichlet-mod-24); before the lock: the notes, corpus and errata terms written for b759 in place of b758's, the carried names
    # ### sweep_ holding the corpus term and rep_ the errata term
    disp_ = _runs('SIDE-explicit-formula') == list(K.EF_RUNS) and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES == 3 \
        and _runs('SIDE-dirichlet-mod-24') == list(K.M24_RUNS) == [] and K.MAX_DISPATCHES_M24 == 0 and len(ds_) == len(K.EF_RUNS) and rd1_
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b759_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return notes_ and moved_ and sweep_ and all(rep_) and disp_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b759_steps.json', 'data/b759_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order, the tool's own list at the act's base 38024feb (I-109, entered at
    b753, and I-110 and I-111, entered at b756 on the author's pass, stand in no row of it, and this act changes no research tool). Not
    run at b757: the run computes at a field where (R367)(10) bars it, nothing computed at any field but the builds; the arm fails and is
    declared so on the face. Each row REPRODUCES,
    DIFFERS or NOT RUN; each run row's planted wrong figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more
    than 60 s or a dispatch or network read); the json's counts and the bank's foot the rows'; the tool at HEAD its blob at the act's base
    (unchanged this act) and the working tree's."""
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
    """standing clauses v9 (Component 6 of (R369): the close "as the standing clauses order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b759_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b758's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R369-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b758's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R369) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b758's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 38024feb; not run at b759, its rows computing at a field, which (R369)(10) bars, the builds apart; declared failing on the face',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 78 = 77 OK + 1 miss, the miss the ruling`s own cite of data/b744_zetabox_plan.txt :134 (events (11)), the check CLEAN (halts 0), as the step-zero bank enters it after the read-first bank and the subject read and before the deletes; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b758-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b759: the tip removed from "(was b19867ac, 12:56:12Z)" and the four after it (data/b759_stepzero.txt :66-:67); the carried plant wanted the tip closed by its paren and mutated nothing (the probe's VAC)
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s ACT line adjusted to what the act did: the Epstein document at v0.2 under (R369); b758 at its weight; the four standing changes; the statement and four print lines at v0.41; the table reproduced; the document entered; the corpus`s sentences re-cut; each object`s bank in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R369)(1): the generated corrigendum for b758`s record, short, landed at FINDINGS :15550: b758`s 72 events and 8 defects by count from their banks, 80 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 0 CLOSE 80, REPEAT 30, no CLAIM item among them; the five findings after b758`s lock entered as b759`s events (17)-(21), CLAIM 0 CLOSE 5 REPEAT 3, each with its time; no weight line; the corrigenda bank appended at row (79)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R366)(2), data/b756_rules.txt`s rows (a) to (c), in force from b757, in b756`s commit 0a151012 and no other, the working tree its blob at HEAD; no rules bank of b759`s, (R369) ordering none',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b759's objects
    ('G-REGISTRATIONS-FIRST', '(R369)(1), (8)-(10), N4, N5: PLACE-papers written by the worklist`s chain of sixteen in its order and by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone (c71ebcd2), no weight line; (8)`s new document in one commit removing nothing, v0.1 untouched; (8)`s three notes and (10)`s two writes each touching its one file and removing no line; (9)`s nine documents each touching its one file and removing a line for each line re-cut; each blob at its commit the sha its bank read back; the changed files within the act`s list; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('phase1.5/method/INSTRUMENTS.md'))),   # ### b759: a file outside the list (SPIRAL_MAP.md, the carried plant, is in b759's)
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b759_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R369)(1)-(10), N2, N4: the act`s order by time across the relay and PLACE-papers -- the act_current commit and step zero`s banks, the ceiling tool, the c1 route and the corrigendum, the four standing changes of (4) and the kernel route before any kernel write, each act tool before its bank, the pre-send and dispatch 1, the outcomes, the table and the cost law, the fields, the document and its three notes, the corpus lines, the errata, then the handoff page and the lock gate -- and by ancestry within the relay; each of the five standing versions` banks ALL AS WANTED at its cases in its own commit with VERSION moved; the act`s commits under tools/standing/ those five alone',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update({next(iter(d), 'none'): False}))),   # ### b759: the first pair of the chain's ancestry set False (b758's planted key stood in no state of b759's)
    ('G-DERIVATION-GRADED', '(R369)(2), (5)-(10), N2, N3: each of the act`s thirteen tools first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; no tool committed with its bank; the outcomes bank`s foot the outcomes json`s word for (5); the pre-send`s with the salt check, the tool controls`, the table`s, the cost law`s and the reproduction run`s feet; the ceiling at HEAD its blob at its last reading`s commit, two readings or more, nothing carried',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'ceiling', ((S['ceiling'] or (None, None))[0], 'planted'))),
    ('G-OFFSET-POST-HOC', 'N5, (R369)(3), (5), (11): the two kernels as the act left them -- SIDE-explicit-formula`s main locally and at origin at a3aad4cc where (5) landed, else at 630cba16; v0.41 peeling to main where (5) landed; v0.39 at d1afb4fc and v0.40 at 630cba16 unmoved, no other tag past v0.38, v0.38 peeling to 14ca5725; its four held branches at their tips; push-b759-weil at a3aad4cc at origin, kept; the four branches of (3) absent at origin; (5)`s two commits on main; SIDE-dirichlet-mod-24`s main at e5ebdd15 at origin, push-b757-mod24 absent there, v0.2.0 peeling to main, v0.1.0 at 597b0869 and no other tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'kst', lambda d: d['ef'].update({'refs/tags/v0.40': ('0' * 40, K.WEIL_TAG[2])}))),   # ### b759: v0.40's peel planted at main a3aad4cc, a tag moved
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R369)(7)-(10), N1, N3: the counts read from their banks -- the notes of (8) three, REGISTRY`s, FACES_LEDGER`s and the census`s, each at its file and read back; the corpus lines of (9) fourteen re-cut and none left, no order entered, nine documents each changed, committed alone and confirmed, one deposited copy, N 14; the errata of (10) two writes, ERRATA`s two entries and OPEN_TRAILS` block, each read back; the dispatches one to three in SIDE-explicit-formula and none elsewhere by their rows, each read once after it; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'notesj', lambda d: d.pop())),   # ### b759: the census's note dropped from the notes bank
    ('G-DIFFERS-ERRATA', '(R369)(1), (10): no DIFFERS entry; ERRATA.md at HEAD its base`s bytes followed by BLOCK E`s two entries alone, E-2026-11-17-1 and E-2026-11-17-2, in PLACE-papers ebbf080c, ERRATA the one file there, E-2026-11-06-1 not edited; no differs bank; the corrigendum in c71ebcd2, FINDINGS the one file there, its head at FINDINGS :15550; no weight line, (R369)(1) ordering none',
#⟪END⟫
# ### b759, before the lock: G-DIFFERS-ERRATA for (R369)(10), which orders ERRATA two entries -- the template's predicate (checks.tpl
# ### :1562-:1567) wants ERRATA.md byte-equal to its base and a weight line in FINDINGS, (R369)(1) ordering none; replaced whole here, in place
# ### of b758's two one-line overrides (its :1566 and :1567), carried and retired with it
#⟪OVERRIDE checks MARK dd4dd9cb3d4b 6⟫
    """(R369)(1), (10): no DIFFERS entry this act; ERRATA's two entries of BLOCK E and no other change -- ERRATA.md's working tree its
    bytes at the act's base followed by two entries alone (E-2026-11-17-1 and E-2026-11-17-2, appended at the file's end in PLACE-papers
    ebbf080c, ERRATA the one file there), E-2026-11-06-1 (:1039) and every line before them not edited; no differs bank and no errata text
    bank (the errata bank is data/b759_errata.json); the corrigendum at FINDINGS in Component 1's PLACE-papers commit, FINDINGS the one file
    there, its head at the worklist's CORR_LINE; no weight line, (R369)(1) ordering none."""
    pre_, now_ = S['errata_pp_pre'] or b'', S['errata_pp_now'] or b''
    new_ = _s(now_[len(pre_):]) if bool(pre_) and now_.startswith(pre_) else ''
    return bool(new_) and re.findall(r'(?m)^## (E-\d{4}-\d\d-\d\d-\d+) ', new_) == ['E-2026-11-17-1', 'E-2026-11-17-2'] \
        and not S['differs'] and not S['errata'] and (S['pp_files'] or {}).get('pp_errata') == ['ERRATA.md'] \
        and K.DIFFERS_LINE is None and K.WEIGHT_LINE is None and S['files']['c1pp'] == ['FINDINGS.md'] \
        and fline(S, K.CORR_LINE).startswith('## Corrigendum to b758')
#⟪END⟫
# ### b759, Component 5 (the Edit tool), defect (f): v1.36.2 taught the kernels face's writer to name SIDE-dirichlet-mod-24 (record.tpl :634)
# ### and not the suite's reader of the face (checks.tpl :611, its list without it), so G-KERNELS-UNTOUCHED's first clause (the face's
# ### kernels equal the kernels read) failed at the standing-a2 probe (05:51:52Z), 24 against 23; the reader takes the writer's own list, in
# ### the act's module for this act, the standing line carried to the next act's standing change (the misses read before the lock)
#⟪OVERRIDE checks MARK f8d771e18f03 1 REPAIR (face)⟫
        kern_face=(jl('b759_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns() + ['SIDE-faces-join', 'SIDE-dirichlet-mod-24'])),
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b759_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R369-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal to its blob at the act`s base e43f1369 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R369)(5), (11): every dispatch a row with its kernel and its free memory at or above the hold, the run ids the worklist`s, one to three in SIDE-explicit-formula and none in SIDE-dirichlet-mod-24, each read once after it by its id; the plant a dispatch with no kernel and no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4, (R369)(5), (11): one dispatch command in the capture for each dispatch row, one to three, each in SIDE-explicit-formula and read once after it, every row`s free memory at or above the hold; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no merge onto a kernel`s main this act beyond SIDE-explicit-formula`s, the holds lifted there alone by (R369)(5) (its main and tags read by G-OFFSET-POST-HOC): each repaired wave 1 kernel`s rebuild-b721 as b758 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at the worklist`s EF_MAIN, the landing`s tip, and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS: the corrigendum and the entry; the new document of (8), v0.1 unchanged; REGISTRY: (8)`s row and note; FACES_LEDGER and the census: (8)`s notes; the nine documents of (9)`s fourteen lines; ERRATA: (10)`s two entries; OPEN_TRAILS: (10)`s block and the trail; (R369)(1), (8)-(10)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    # ### b759, before the lock: the carried stub replaced -- b758's trail head as OPEN_TRAILS :18565 carries it (the Grep tool at PLACE-papers
    # ### HEAD b6e9f79c, 21:5xZ), in place of b757's carried head (b758's module, :1149)
    ('G-PRIOR-CLOSED-PUSHED', 'b758`s trail record on OPEN_TRAILS (:18565) and its root in the chain', lambda S: '### b758 — lane two, act one hundred and eighty-five, the landing under (R368)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS, REGISTRY, ERRATA, FACES_LEDGER, SPIRAL_MAP, the census, the new document of (8) and the eight other documents of (9)): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved; v0.38 to v0.41, push-b759-weil, the removed branches and SIDE-dirichlet-mod-24 read by G-OFFSET-POST-HOC) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: one to three by the dispatch rows, each in SIDE-explicit-formula; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b759 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b758's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b759: (R369)'s rows, written at step zero in place of b758's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch facts759.py, facts759b.py, facts759c.py, read-only). A place is
    # ### named by its role or its file name, never by a folder of the host (N5); the PLACE-papers lines these rows read stand at no place of
    # ### [Q]'s row (3) (the masking reader printed each whole). The relay tools the act changes are read at the act's start (K.PRE_RELAY), the
    # ### kernels at their commits and tags, so a later run reads the same text.
    import hashlib as _h
    EF_ = 'D:/SIDE-explicit-formula'
    MOD_ = 'D:/SIDE-dirichlet-mod-24'
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling SCOPE', 'relay main at the act`s start e43f1369, b758`s closing push, read back at the remote (or an ancestor of the remote`s main)',
        gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('e43f1369') and bool(rm) and gr('D:/relay', 'merge-base', 'e43f1369', rm).startswith('e43f1369'), 'remote main %s' % rm[:8], '0')
    npp_, tpp_ = gr(PP, 'rev-list', '--count', K.PRE_PP), gr(PP, 'tag', '--list').split()
    add('ruling SCOPE', 'PLACE-papers main at the act`s start 4ea41948: 2,184 commits and 2 tags there', gr(PP, 'rev-parse', K.PRE_PP).startswith('4ea41948') and npp_ == '2184' and len(tpp_) == 2,
        '%s ; %s commits ; %d tags' % (K.PRE_PP[:8], npp_, len(tpp_)), '0')
    tip_ = lambda r_, c_: (gr(EF_, 'rev-parse', '--verify', '--quiet', r_) or c_).startswith(c_)   # noqa: E731  ### a branch removed at (3) read as its commit
    TAGS_ = (('v0.38', '21c6edaf', '14ca5725'), ('v0.39', '69da6cd7', 'd1afb4fc'), ('v0.40', 'd86d8cf5', '630cba16'))
    BR5_ = (('push-b757-join', '6568e9c7'), ('push-b757-coeff', '596d1c9e'), ('push-b758-land', 'd1afb4fc'), ('push-b758-coeff', '630cba16'))
    add('ruling SCOPE, (3), (5), (11)', 'SIDE-explicit-formula: main 630cba16 at the act`s start; v0.38, v0.39 and v0.40 the tag objects 21c6edaf, 69da6cd7 and d86d8cf5 peeling to 14ca5725, d1afb4fc and 630cba16; push-b757-join 6568e9c7, push-b757-coeff 596d1c9e, push-b758-land d1afb4fc and push-b758-coeff 630cba16 at the remote, each an ancestor of 630cba16',
        K.EF_MAIN.startswith('630cba16') and all(gr(EF_, 'rev-parse', t_).startswith(o_) and gr(EF_, 'rev-parse', t_ + '^{commit}').startswith(c_) for t_, o_, c_ in TAGS_)
        and all(tip_('origin/' + b_, c_) and gr(EF_, 'merge-base', c_, K.EF_MAIN).startswith(c_) for b_, c_ in BR5_),
        'origin/main %s ; v0.40 peel %s' % (gr(EF_, 'rev-parse', '--short=8', 'origin/main'), gr(EF_, 'rev-parse', 'v0.40^{commit}')[:8]), '2')
    add('ruling SCOPE, (3), (11)', 'SIDE-dirichlet-mod-24: the remote`s main e5ebdd15 with v0.2.0, the tag object e5c84316, peeling to it; push-b757-mod24 at e5ebdd15',
        gr(MOD_, 'rev-parse', 'v0.2.0').startswith('e5c84316') and gr(MOD_, 'rev-parse', 'v0.2.0^{commit}').startswith('e5ebdd15') and gr(MOD_, 'rev-parse', 'origin/main').startswith('e5ebdd15')
        and (gr(MOD_, 'rev-parse', '--verify', '--quiet', 'origin/push-b757-mod24') or 'e5ebdd15').startswith('e5ebdd15'),
        'remote main %s ; v0.2.0 peel %s' % (gr(MOD_, 'rev-parse', '--short=8', 'origin/main'), gr(MOD_, 'rev-parse', 'v0.2.0^{commit}')[:8]), '2')
    mi_ = lines_of(p('data', 'b758_mirror.txt'))
    add('ruling SCOPE', 'data/b758_mirror.txt :3, b758`s mirror: MANIFEST md5 6104e9e8bc6ca155e2b7a4766c5031b4, 84 files with MANIFEST',
        'md5 6104e9e8bc6ca155e2b7a4766c5031b4' in at(mi_, 3) and 'files 84 + MANIFEST' in at(mi_, 3), at(mi_, 3)[:60], '0')
    # ### (R369)(1): b758 at its weight, from its closing bank's head line; (3): its carried list (f)
    add('ruling (1)', 'data/b758_closing.txt :1, the head line: relay c25f8b53, PLACE-papers 4ea4194, suite 111 of 116, scores 7 of 8 HELD, 8 defects',
        at(cl, 1).startswith('b758 closed: relay c25f8b53, PLACE-papers 4ea4194; suite 111 of 116;') and 'scores 7 of 8 HELD; 8 defects' in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (2), (3)', 'data/b758_closing.txt :969-:974, CARRIED FORWARD (f) and (g): the push-b758* branches left for this step zero, the kept branches by name (the five kernel branches of (3) among them), the closing push-out bank for this act to commit',
        at(cl, 969).lstrip().startswith('(f) Branches left for the next act`s step zero: the push-b758* branches of relay and PLACE-papers. KEPT, not for deletion:')
        and 'push-b757-join, push-b757-coeff, push-b758-land and push-b758-coeff of SIDE-explicit-formula standing at the remote;' in at(cl, 971)
        and 'push-b757-workflow and push-b757-mod24 of SIDE-dirichlet-mod-24' in at(cl, 972) and 'corrigendum-b723 of relay' in at(cl, 972)
        and at(cl, 974).lstrip().startswith('(g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.'), 'present', '0')
    # ### (R369)(4): the three standing lines the changes touch, at the act's start, and the two controls' subjects
    al_ = _blob('D:/relay', K.PRE_RELAY, 'tools/standing/allow.py').replace(chr(13), '').split(NL)
    b8_ = _blob('D:/relay', K.PRE_RELAY, 'tools/acts/b758.py').replace(chr(13), '').split(NL)
    add('ruling (4)(ii)', 'tools/standing/allow.py :110-:117 at the act`s start, plant_kept: the located delete clause`s first "deleted" read "kept", one clause alone; tools/acts/b758.py :362, plant_every_kept',
        at(al_, 110) == 'def plant_kept(ruling, must):' and at(al_, 117).strip() == "return flat.replace(c, DELETED.sub('kept', c, count=1), 1)" and 'def plant_every_kept' in at(b8_, 362),
        '%d ; %d lines' % (len(al_), len(b8_)), '2')
    rt_ = _blob('D:/relay', K.PRE_RELAY, 'tools/standing/fold/record.tpl').replace(chr(13), '').split(NL)
    add('ruling (4)(iii)', 'tools/standing/fold/record.tpl :312-:313 at the act`s start, the row writer refusing a phase outside STEP_PHASES; relay f401a81e, b758`s repair commit, tools/acts/b758.py alone',
        at(rt_, 312).strip() == 'if phase not in STEP_PHASES:' and at(rt_, 313).strip().startswith("sys.exit('### THE PHASE %r IS NOT ONE OF %s")
        and gr('D:/relay', 'show', '--name-only', '--format=', 'f401a81e').split() == ['tools/acts/b758.py'] and gr('D:/relay', 'log', '-1', '--format=%s', 'f401a81e').startswith('b758 repair:'),
        '%d lines' % len(rt_), '2')
    ct_ = _blob('D:/relay', K.PRE_RELAY, 'tools/standing/fold/checks.tpl').replace(chr(13), '').split(NL)
    kf_ = _jl('b758_kernels_face.json').get('kernels') or {}
    add('ruling (4)(iv)', 'tools/standing/fold/checks.tpl :611 at the act`s start, the suite`s reader of the kernels face: SIDE-faces-join added to the kernels read, SIDE-dirichlet-mod-24 not named; data/b758_kernels_face.json, 24 kernels with SIDE-dirichlet-mod-24',
        'kern_face=(jl(' in at(ct_, 611) and "+ ['SIDE-faces-join']" in at(ct_, 611) and 'SIDE-dirichlet-mod-24' not in at(ct_, 611) and len(kf_) == 24 and 'SIDE-dirichlet-mod-24' in kf_,
        'face kernels %d' % len(kf_), '2')
#⟪END⟫
#⟪SECTION citation 2⟫
    # ### b759: no row between the events bank's read and its numbers
#⟪END⟫
#⟪SECTION citation 3⟫
    # ### b759: no row between the events' numbers and the defects bank's read
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b759 step zero: (R369)(1)'s counts over b758's banks, written in place of b758's rows over b757's: its events (1)-(72) and its defects
    # ### (a)-(h), each row tagged by the reader's owner form, every one CLOSE and none CLAIM ("no CLAIM item among them", (R369)(1)); no
    # ### post-seal events bank at b758 (what the seat found after the lock stands in its closing message, entered as b759's events)
    add('ruling (1), ferry (read first)', 'b758`s events (1)-(72) and its 8 lettered defects (a)-(h), no post-seal events bank (data/b758_events.txt, data/b758_defects.txt)',
        starts == list(range(1, 73)) and letters == list('abcdefgh') and not os.path.exists(p('data', 'b758_events_postseal.txt')),
        'events %s ; letters %d (%s-%s) ; post-seal %s' % (starts[-1:], len(letters), letters[:1], letters[-1:], 'absent' if not os.path.exists(p('data', 'b758_events_postseal.txt')) else 'PRESENT'), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_ in (('data/b758_events.txt', ev, 72), ('data/b758_defects.txt', dl, 8)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_.group(2) for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        add('ruling (1), ferry (read first)', '%s: %d rows, each tagged by the reader`s owner form, CLOSE every one, no CLAIM item' % (f_, nr_),
            len(rr_) == nr_ and len(tg_) == nr_ and tg_.count('CLAIM') == 0 and tg_.count('CLOSE') == nr_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d' % (len(rr_), len(tg_), tg_.count('CLAIM'), tg_.count('CLOSE')), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'FINDINGS :%d, b758`s entry, the landing under (R368)' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## The landing under (R368): b757’s close by its four carried steps'),
        at(fi, K.B711_ENTRY)[:50], '1')
    add('ruling (1)', 'FINDINGS :%d, b758`s corrigendum to b757`s record, short, the form b759`s follows; no weight line there' % K.B711_CORRIGENDUM,
        at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b757’s record, short') and K.B711_WEIGHT is None, at(fi, K.B711_CORRIGENDUM)[:40], '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b758`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b758 — lane two, act one hundred and eighty-five, the landing under (R368)'), at(ot, K.B711_TRAIL)[:50], '1')
    add('ruling (1)', 'OPEN_TRAILS :%d, b758`s open-orders line; :18615, its scores line with N4 REFUTED' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**')
        and at(ot, 18615).startswith('**N1 HELD · N2 HELD · N3 HELD · N4 REFUTED · N5 HELD'), at(ot, K.TRAIL_ORDERS)[:50], '1')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula and SIDE-dirichlet-mod-24, the two kernels this act opens', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-dirichlet-mod-24/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.36.2 entering the act (read at the act`s start, so a run after (4)`s changes reads the same)', (_blob('D:/relay', K.PRE_RELAY, 'tools/standing/VERSION') or '').strip() == 'v1.36.2',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### b758's mirror the last built, by its file name and hash, the folder that holds it not printed (N5)
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    add('ruling SCOPE, (8)', 'b758`s mirror, the last built: %s (sha256 %s); this act`s mirror carries v0.2' % (os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest()[:8]), bool(mz_) and 'b758' in K.MIRROR_ZIP,
        '%d bytes' % len(mz_), '6')
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R369)(3), (5): the two kernels' clones before any kernel write, clean: SIDE-explicit-formula on push-b758-coeff as b758 left it (at
    # ### main's commit), later on push-b759-weil or main; SIDE-dirichlet-mod-24 on push-b757-mod24 (at its main's commit), or main
    kc2_ = [(os.path.basename(r_), gr(r_, 'rev-parse', '--abbrev-ref', 'HEAD'), gr(r_, 'status', '--porcelain', '-uno')) for r_ in (EF_, MOD_)]
    add('ruling (3), (5)', 'the two kernels` clones with nothing changed or staged: SIDE-explicit-formula on push-b758-coeff (or push-b759-weil or main), SIDE-dirichlet-mod-24 on push-b757-mod24 (or main)',
        kc2_[0][1] in ('push-b758-coeff', 'push-b759-weil', 'main') and kc2_[1][1] in ('push-b757-mod24', 'main') and not any(s_ for _n, _h2, s_ in kc2_),
        ' ; '.join('%s %s %s' % (n_, h_, 'clean' if not s_ else 'CHANGED') for n_, h_, s_ in kc2_), '0')
#⟪END⟫
#⟪SECTION citation 6⟫
    # ### (R369)(5): the statement's neighbours and the print lines, at 630cba16
    hs_ = _blob(EF_, '630cba16', 'SIDEExplicitFormula/H2Sign.lean').replace(chr(13), '').split(NL)
    hc_ = _blob(EF_, '630cba16', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean').replace(chr(13), '').split(NL)
    add('ruling (5)', 'at 630cba16: H2Sign.lean :15 opens ComplexOrder, :29-:30 h2_sign (0 ≤ poleTerm k - primeSum k + archTerm k over classK); Schema/Wide/HalfScaleControl.lean :26-:28 zq_arith_side_re_neg in namespace SIDEExplicitFormula.Schema.ZQ (:20-:22), its proof closing at :35, 39 lines',
        at(hs_, 15) == 'open scoped ComplexOrder' and at(hs_, 29) == 'def h2_sign : Prop :=' and at(hs_, 30).strip() == '∀ k : ℝ → ℂ, classK k → 0 ≤ poleTerm k - primeSum k + archTerm k'
        and at(hc_, 26) == 'theorem zq_arith_side_re_neg :' and at(hc_, 28).strip() == '(B321.poleTerm k - primeTermQ (fun n => cQ n) k + archTermQ k).re < 0 := by'
        and [at(hc_, n_) for n_ in (20, 21, 22)] == ['namespace SIDEExplicitFormula', 'namespace Schema', 'namespace ZQ'] and at(hc_, 35).strip() == 'exact hneg' and len(hc_) == 40 and hc_[-1] == '',
        '%d ; %d lines' % (len(hs_) - 1, len(hc_) - 1), '3')
    pt_ = [l_ for l_ in _blob(EF_, '630cba16', 'print_targets.txt').replace(chr(13), '').split(NL) if l_.strip()]
    N4_ = (('SIDEExplicitFormula.Schema.ZQ.rQ_one', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 56), ('SIDEExplicitFormula.Schema.ZQ.cQ_eq', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 71),
           ('SIDEExplicitFormula.Schema.detector', 'SIDEExplicitFormula/Schema/Detector.lean', 99), ('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'SIDEExplicitFormula/Seam.lean', 101))
    d4_ = [(n_, _decl_files(EF_, '630cba16', n_), _decl_line(_blob(EF_, '630cba16', f_), n_.split('.')[-1])) for n_, f_, _l in N4_]
    add('ruling (5)', 'print_targets.txt at 630cba16: 484 lines, none twice, zq_arith_side_re_neg`s among them and none of COMMIT ONE`s four; each of the four declared in one file at its line (LogDeriv.lean :56 and :71, Schema/Detector.lean :99, Seam.lean :101); zq_weil_positivity_fails declared nowhere',
        len(pt_) == 484 and len(set(pt_)) == 484 and 'SIDEExplicitFormula.Schema.ZQ.zq_arith_side_re_neg' in pt_ and not any(n_ in pt_ for n_, _f, _l in N4_)
        and all(fs_ == [f_] and l_ == w_ for (_n, fs_, l_), (_m, f_, w_) in zip(d4_, N4_)) and _decl_files(EF_, '630cba16', 'zq_weil_positivity_fails') == [],
        ' '.join('%s:%d' % (n_.split('.')[-1], l_) for n_, _f, l_ in d4_), '3')
    bm_ = _blob(EF_, '630cba16', '.github/workflows/build-module.yml').replace(chr(13), '').split(NL)
    add('ruling SCOPE, (5)', 'build-module.yml :86-:96 at 630cba16, the print step: print_targets.txt copied at :86, its filter at :91 (A-Z in both cases, digits, underscore, full stop and the prime), the axioms run at :96',
        at(bm_, 86).strip() == 'cp print_targets.txt out/print_targets.txt' and at(bm_, 91).strip().startswith('*[!A-Za-z0-9_.' + chr(92) + chr(39) + ']*) echo "print target refused: $n"')
        and at(bm_, 96).strip() == 'lake env lean out/Axioms.lean > out/axioms.txt 2>&1 || true', '%d lines' % (len(bm_) - 1), '3')
    ps_ = lines_of(p('data', 'b758_presend.txt'))
    add('ruling (5)', 'data/b758_presend.txt :4-:5, the pre-send reads of (R368)(4) this act carries: duplicates printed, 0 wanted; the filter`s refusals, two expected (:358 and :359)',
        at(ps_, 4).startswith('### duplicates printed, 0 wanted at the tip;') and at(ps_, 5).startswith('### refuses printed, two expected (:358 and :359'), 'present', '3')
    # ### (R369)(6): the three routes' tools and the registration they reproduce
    ab_ = lines_of(p('tools', 'b718_abstract.py'))
    cq_ = lines_of(p('tools', 'b750_cq_sign.py'))
    add('ruling (6)', 'tools/b718_abstract.py :53 a_of, :72 b_lattice, :91 pair_sum (I-105`s model); tools/b750_cq_sign.py :1-:7, the recursion of LogDeriv.lean :63-:65 at 14ca5725, its form_counts at :84 and recursion at :128',
        at(ab_, 53).startswith('def a_of(') and at(ab_, 72).startswith('def b_lattice(') and at(ab_, 91).startswith('def pair_sum(')
        and at(cq_, 1).startswith('"""b750, (R360)(2)[E]: THE SIGN OF cQ(n)') and 'LogDeriv.lean :63-:65' in at(cq_, 2) and at(cq_, 84).startswith('def form_counts(') and at(cq_, 128).startswith('def recursion('),
        '%d ; %d lines' % (len(ab_) - 1, len(cq_) - 1), '4')
    rg3_ = lines_of(p('data', 'b753_registrations.txt'))
    wk_ = lines_of(p('data', 'b755_walk.txt'))
    add('ruling SCOPE, (6)', 'data/b753_registrations.txt :14-:23, the coefficient law at class number 3 and its reason, the four minimal negative patterns at :20-:21; data/b755_walk.txt :234, H-C3-LAW 14 OF 14 HELD',
        at(rg3_, 14).startswith('Let D be a negative fundamental discriminant of class number 3') and '(1,1,1,1) at −6, (2,1,1) at −2, (4,1) at −2 and' in at(rg3_, 20)
        and at(wk_, 234).startswith('### ### **H-C3-LAW: 14 OF 14 HELD, REFUTED 0'), 'present', '4')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    add('ruling SCOPE, (6), (7), (10)', 'INSTRUMENTS :746 I-105 and :750 I-106, their heads; :766, the recursion`s reads; :556 carrying gamma prime 29.5517610986 and gamma 16.2902157204; :664 carrying the index 10034',
        at(ins_, 746).startswith('## I-105 — THE GROUP-RING MODEL OF b(n)') and at(ins_, 750).startswith('## I-106 — THE CLASS GROUP OF A NEGATIVE DISCRIMINANT')
        and at(ins_, 766).startswith('**Reads.** Nothing external: the recursion of SIDE-explicit-formula') and '29.5517610986' in at(ins_, 556) and '16.2902157204' in at(ins_, 556) and '10034' in at(ins_, 664),
        '%d lines' % (len(ins_) - 1), '4')
    # ### (R369)(7): the fields' banks. THE RULING CITES data/b744_zetabox_plan.txt :134 FOR 1.2972e11: that line carries zeta's figure, 4.3908e+09,
    # ### at gamma 14.1347251417; 1.2972e+11, at b741's gamma 16.29021572, stands at :135 (read at step zero) -- a MISS, raised in the seat's read
    zb_ = lines_of(p('data', 'b744_zetabox_plan.txt'))
    add('ruling (7)', 'data/b744_zetabox_plan.txt :134, the figure 1.2972e11 (e^(pi gamma/2) at b741`s gamma)', '1.2972e+11' in at(zb_, 134),
        'at :134 %r ; the figure at :%d' % (at(zb_, 134).strip()[:46], first(zb_, '1.2972e+11')), '4')
    on_ = lines_of(p('data', 'b740_offlinezero_notes.txt'))
    of_ = lines_of(p('data', 'b742_offlinezero.txt'))
    add('ruling (7)', 'data/b740_offlinezero_notes.txt :5, the figure 1.4608e10 (the true 1/|Gamma(cA)|); data/b742_offlinezero.txt :68, the md5 of the six generated modules at 14ca5725, two whole and four by their opening characters',
        '(1.4608e10)' in at(on_, 5) and 'At 14ca5725 the md5 of each generated module equals the generator' in at(of_, 68) and 'FrontierData c8e320f9db1a12622cc147555496cf11' in at(of_, 68)
        and 'NodesF d37bbfbb8c81165521b77de16022069a' in at(of_, 68) and all(('%s ' % m_) in at(of_, 68) for m_ in ('Nodes0', 'Nodes1', 'Nodes2', 'Nodes3')), 'present', '4')
    oc7_ = lines_of(p('data', 'b757_outcomes.txt'))
    add('ruling (7)', 'data/b757_outcomes.txt :90, units24_iso_signs`s axioms line, [propext]', at(oc7_, 90).split() == ['SIDEDirichletMod24.units24_iso_signs', '[propext]'], at(oc7_, 90).strip()[:60], '4')
    # ### (R369)(8): the document and the places its notes go
    v1p_ = os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md')
    v1b_ = open(v1p_, 'rb').read() if os.path.exists(v1p_) else b''
    ep_ = v1b_.decode('utf-8', 'replace').split(NL)
    add('ruling (8)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md: sha256 opening 8289b9539b21fd18, 37,472 bytes; its nine dated notes at :3 to :19 (the odd lines); section 1`s head at :21; :218 section 5`s last line; the heads of sections 6 to 9 at :220, :222, :224 and :226',
        _h.sha256(v1b_).hexdigest().startswith('8289b9539b21fd18') and len(v1b_) == 37472 and all(at(ep_, n_).startswith('*') for n_ in range(3, 20, 2)) and not any(at(ep_, n_).strip() for n_ in range(4, 20, 2))
        and at(ep_, 21).startswith('## 1. The object:') and at(ep_, 218).strip() and at(ep_, 220).startswith('## 6. The corollary and what it says') and at(ep_, 222).startswith('## 7. The cost law')
        and at(ep_, 224).startswith('## 8. Class number one') and at(ep_, 226).startswith('## 9. Back matter'), 'sha256 %s ; %d bytes' % (_h.sha256(v1b_).hexdigest()[:16], len(v1b_)), '5')
    v2r_ = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'
    add('ruling (8)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, the new file: absent at the act`s start, written by this act alone', not os.path.exists(os.path.join(PP, v2r_)) or bool(gr(PP, 'log', '--format=%h', K.PRE_PP + '..HEAD', '--', v2r_)),
        'absent' if not os.path.exists(os.path.join(PP, v2r_)) else 'written by %s' % gr(PP, 'log', '-1', '--format=%h', '--', v2r_), '5')
    rg2_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    kc_ = lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))
    # ### each line the file's last while PLACE-papers stands at the act's start; after this act's own writes the ends move by design
    at_start_ = gr(PP, 'rev-parse', 'HEAD') == gr(PP, 'rev-parse', K.PRE_PP)
    ends_ = not any(l_.strip() for L_, n_ in ((rg2_, 1252), (fl_, 573), (kc_, 1572)) for l_ in L_[n_:])
    add('ruling (8)', 'REGISTRY :179, the row 1.5c-23, and :1252, b758`s dated note; FACES_LEDGER.md :573, b758`s filing line; THE_KEYSTONE_CENSUS_v0_8_3.md :1572, b758`s note; the last three each its file`s end at the act`s start',
        at(rg2_, 179).startswith('| 1.5c-23 |') and at(rg2_, 1252).startswith("*Dated note, b758, 2026-11-17, under the author's ruling `(R368)`(8)")
        and at(fl_, 573).startswith('*The rows above are unedited. Filed by b758') and at(kc_, 1572).startswith("*Appended 2026-11-17 by b758 under the author's ruling `(R368)`(8):*")
        and (ends_ or not at_start_), '%d ; %d ; %d lines ; the ends %s' % (len(rg2_) - 1, len(fl_) - 1, len(kc_) - 1, 'read' if at_start_ else 'moved by this act'), '5')
    # ### (R369)(9): SPIRAL_MAP and the eight other documents of the fourteen lines, each present (the OLD of each line read at Component 6 by its tool)
    D9_ = [x_ for x_ in K.PP_EDITED if x_ not in ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md', 'ERRATA.md', 'FACES_LEDGER.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', v2r_)]
    add('ruling (9)', 'the nine documents of (9)`s fourteen lines (SPIRAL_MAP and the eight others), each present in PLACE-papers', len(D9_) == 9 and all(os.path.exists(os.path.join(PP, x_)) for x_ in D9_),
        '%d ; absent %s' % (len(D9_), [x_ for x_ in D9_ if not os.path.exists(os.path.join(PP, x_))] or 'none'), '6')
    # ### (R369)(10): ERRATA, OPEN_TRAILS and the orders' cites
    er_ = lines_of(os.path.join(PP, 'ERRATA.md'))
    add('ruling (10)', 'ERRATA :1039, E-2026-11-06-1 (not edited); :1047, E-2026-11-09-1, the form BLOCK E`s entries take', at(er_, 1039).startswith('## E-2026-11-06-1 — `(R345)`(6)')
        and at(er_, 1047).startswith('## E-2026-11-09-1 — '), 'present', '6')
    ix_ = lines_of(os.path.join(PP, 'phase1.5', 'proofs', 'INDEX_ARITY_AT_THE_CRITICAL_LINE.md'))
    ws_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines_v2_4_0.md'))
    add('ruling (10)', 'OPEN_TRAILS :17932, W-ORD-MECHANISM-ATTRIBUTION; INDEX_ARITY_AT_THE_CRITICAL_LINE.md :344 carrying 5938; Which_Structure_Confines_v2_4_0.md :203, the row at class number above one; BIBLIOGRAPHY.md present',
        'W-ORD-MECHANISM-ATTRIBUTION' in at(ot, 17932) and '5938' in at(ix_, 344) and at(ws_, 203).startswith('| for class number > 1 the coefficients are not multiplicative, so no Euler product exists |')
        and os.path.exists(os.path.join(PP, 'BIBLIOGRAPHY.md')), 'present', '6')
    add('ruling (11)', 'tools/research/reproduce.py, the reproduction the standing clauses order run in full', os.path.exists(p('tools', 'research', 'reproduce.py')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3)', 'the push-b758-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R369)(2): act_current alone, then b758's carried files, each alone, in the worklist's order (K.STEPZERO_CARRIED), each commit read for
    # ### its files; the third file the ruling names, tools/mirror_prevbuild.json, read against HEAD's blob with its CR line ends removed
    WANT_ = {'aeeacd60': ['data/b758_relay_push-b758-closing_push_out.txt'], '93c32f60': ['data/b759_address_scan_commits.txt']}
    if not K.ACT_CURRENT_COMMIT:
        add('ruling (2)', 'data/act_current.json -- TO BE COMMITTED at step zero', False, 'NOT COMMITTED', '0')
    else:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', K.ACT_CURRENT_COMMIT).split()
        add('ruling (2)', 'data/act_current.json committed alone at %s, an ancestor of HEAD' % K.ACT_CURRENT_COMMIT, nm_ == ['data/act_current.json']
            and gr('D:/relay', 'merge-base', K.ACT_CURRENT_COMMIT, 'HEAD').startswith(K.ACT_CURRENT_COMMIT), ' '.join(nm_)[:90], '0')
    for c_, s_, w_ in K.STEPZERO_CARRIED:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (2)', 'b758`s carried files, %s, committed alone at %s (step %d), an ancestor of HEAD' % (w_, c_, s_), sorted(nm_) == sorted(WANT_.get(c_, ['?']))
            and gr('D:/relay', 'merge-base', c_, 'HEAD').startswith(c_), '%d files' % len(nm_), '0')
    mpw_ = open(p('tools', 'mirror_prevbuild.json'), 'rb').read().replace(b'\r', b'') if os.path.exists(p('tools', 'mirror_prevbuild.json')) else b''
    mph_ = subprocess.run(['git', '-C', 'D:/relay', 'cat-file', '-p', 'HEAD:tools/mirror_prevbuild.json'], capture_output=True).stdout.replace(b'\r', b'')
    add('ruling (2)', 'tools/mirror_prevbuild.json, the third file the ruling names: its working copy equal to HEAD`s blob with the CR line ends removed, nothing to commit (an event of step zero)',
        bool(mpw_) and mpw_ == mph_, 'sha256 %s ; HEAD %s' % (_h.sha256(mpw_).hexdigest()[:8], _h.sha256(mph_).hexdigest()[:8]), '0')
    left_ = gr('D:/relay', 'status', '--porcelain', '--', 'data/b758_relay_push-b758-closing_push_out.txt')
    add('ruling (2)', 'the closing push-out bank b758 left uncommitted clean at HEAD after its commit', not left_, left_.replace(NL, ' | ') or 'clean', '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (11)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (2)', 'tools/mirror_prevbuild.json, the builder`s state file the mirror reads', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '0')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (2), ferry (read first)', 'data/b759_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b759_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b759_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with b758 at its weight and the seat's read of what the ruling misses, the four standing changes of
(4) and the kernel route counted apart (each by its controls bank), the statement and the print lines ((5)'s pre-send reads and salt check,
the controls tool's own controls, the dispatch and its read, the outcome), the table of Appendix A and the cost law, the fields, the
document (its composition and the notes of (8)), the corpus lines, the errata and orders of (10), the reproduction run of (11), the
ceiling's readings, the name and address scan, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the
line its pattern names (section_reading);
(R369)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section;
the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next
act ((R369)(11)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act, as (R369)(5) and (11) open them: SIDE-explicit-formula's tree on
push-b759-weil ((5)'s two commits, the four print lines and zq_weil_positivity_fails), main moved by the gated push's default mode after the
run's success alone, v0.41 cut at main's read-back, as relay data/b759_outcomes.txt reads it; its local main fast-forwarded to the landing by
the one-call tool; the five branches of (3) removed at the kernels' remotes by (4)(i)'s route (relay data/b759_events.txt (24), (39)).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for the act after b759 ((R369)(10) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R365)(2)(iv)(c): the outbound sentence from the one clause
# ### b759, before the lock: (5)'s outcome read from its bank at import, and the table's, the document's and the corpus's feet, for the title
# ### and the kernel lines (b758's two items, join and coeff, give way to (5)'s one, weil)
_OC5 = dict((r_.get('item'), r_) for r_ in (jl('b759_outcomes.json') or []) if isinstance(r_, dict))
_OW5 = lambda k_: (_OC5.get(k_) or {}).get('outcome') or 'NOT READ'
_LT5 = [(_OC5[k_].get('tag'), (_OC5[k_].get('peel') or '')[:8]) for k_ in ('weil',) if _OW5(k_).startswith('LANDED')]
_FT5 = lambda n_: ([l_ for l_ in (rd(n_) or '').split(NL) if l_.startswith('### ### **')] or [''])[-1]
TITLE_LINE = ('b759 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTY-SIX, THE EPSTEIN DOCUMENT AT v0.2: b758 AT ITS WEIGHT; '
              'FOUR STANDING CHANGES; %s; %s; %s; %s; UNDER (R369).**' % (
                  'ONE STATEMENT AND FOUR PRINT LINES LANDED AT v0.41' if _OW5('weil') == 'LANDED, COMPILED' else (
                      'FOUR PRINT LINES LANDED AT v0.41, THE STATEMENT NOT COMPILED' if _OW5('weil').startswith('LANDED') else 'NOTHING LANDED, MAIN AT v0.40'),
                  'THE APPENDIX’S TABLE REPRODUCED' if 'THE TABLE OF APPENDIX A: REPRODUCED ;' in _FT5('b759_c3table.txt') else 'THE APPENDIX’S TABLE NOT REPRODUCED',
                  'THE DOCUMENT ENTERED' if 'v0.2 COMPOSED:' in _FT5('b759_compose.txt') else 'THE DOCUMENT NOT ENTERED',
                  'THE CORPUS’S SENTENCES RE-CUT' if 'RE-CUT 14 OF 14 ;' in _FT5('b759_corpus.txt') else 'THE CORPUS’S SENTENCES RE-CUT IN PART'))   # ### the ferry`s ACT line (data/b759_ferry.txt :39) adjusted to what the act did
_K5_MAIN = ('moved to %s' % ' and then to '.join('%s, %s cut at its read-back' % (p_, t_) for t_, p_ in _LT5)) if _LT5 else 'unmoved, no tag cut'
_K5_DEL = ('the branches of (3) deleted at the kernels` remotes by (4)(i)`s route, one per message: ' + ', '.join(
    '%s (was %s)' % (b_, t_[:8]) for b_, t_ in WL.KERNEL_DELETES)) if WL.KERNEL_DELETES else 'the branches of (3) standing at the kernels` remotes'
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b758's sections over b758's objects not carried), headed as CLOSING_SECTIONS names them. A row
    of two reads its bank's verdict line by vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('b758 at its weight, as its closing record`s head line gives it ((R369)(1))', 'b758_closing.txt', r'(?m)^b758 closed: [^\n]*'),
                ('the seat`s read of what the ruling misses, made after (5)`s pre-send reads ((R369)(2)), its head', 'b759_misses.txt', r'(?m)^b759 -- [^\n]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE STANDING CHANGES ((R369)(4), and the kernel route counted apart)', [
                ('v1.36.3: (4)(i), the route that removes a named branch at a kernel`s remote, used for (3)`s five', 'b759_standing_v1363.txt'),
                ('v1.36.4: (4)(ii), the plant of G-DELETES-ONE-BRANCH reading kept every covering clause', 'b759_standing_v1364.txt'),
                ('v1.36.5: (4)(iii), the row writer taking the phase repair', 'b759_standing_v1365.txt'),
                ('v1.36.6: (4)(iv), the suite`s reader of the kernels face naming SIDE-dirichlet-mod-24, on :663', 'b759_standing_v1366.txt'),
                ('v1.36.7: the one-call tool opened for this act in SIDE-explicit-formula, before any kernel write, counted apart', 'b759_standing_v1367.txt')]),
            ('THE STATEMENT AND THE PRINT LINES ((R369)(5))', [
                ('the salt check and the pre-send reads at push-b759-weil`s tip, banked before the dispatch', 'b759_presend.txt'),
                ('tools/b759_controls.py by its own controls, committed before its opening dispatch', 'b759_controls_control.txt'),
                ('every dispatch and its read by run id, within the cap of 3', 'b759_controls.txt'),
                ('the outcome of (5), its sentence cut from the ruling for the outcome its run read, main and v0.41 read back', 'b759_outcomes.txt')]),
            ('THE TABLE AND THE FIELDS ((R369)(6), (7))', [
                ('the table of Appendix A by two routes and the proof`s general steps, the plant printed first', 'b759_c3table.txt'),
                ('F1 and F2, each from the banked figures', 'b759_costlaw.txt'),
                ('the fields filled from the banks and from no recall', 'b759_fields.txt'),
                ('N and DEPOSITS by the corpus route after (9)', 'b759_fields_corpus.txt')]),
            ('THE DOCUMENT ((R369)(8))', [
                ('v0.2 composed beside v0.1, its controls printed before its commit', 'b759_compose.txt'),
                ('REGISTRY`s row and note, FACES_LEDGER`s and the census`s notes, each read back and committed alone', 'b759_notes.json', r'"read_back": (?:true|false)')]),
            ('THE CORPUS LINES AND THE ERRATA ((R369)(9), (10))', [
                ('the fourteen lines of BLOCK D, each OLD once at its line and replaced by its NEW, one commit a document', 'b759_corpus.txt'),
                ('ERRATA`s two entries and OPEN_TRAILS` block, each read back and committed alone', 'b759_errata.json', r'"read_back": (?:true|false)')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED ((R369)(11), the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run in the foreground', 'b759_reproduce.txt')]),
            ('THE CEILING ((R369)(2))', [
                ('the readings against 16 hours from the delivery, banked by the committed tool', 'b759_ceiling.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b759_address_scan.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R365)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s tree alone, as (R369)(5) and (11) open it: main from ' + WL.EF_BASE[:8] + ' ' + _K5_MAIN + ', by the gated push`s default mode after the run`s success, never forced ; ' + WL.WEIL_BRANCH[0] + ' at ' + WL.WEIL_BRANCH[1][:8] + ' ((5)`s two commits, the four print lines and zq_weil_positivity_fails), pushed --scratch and read back, kept for the next act`s step zero ; ' + WL.ZQ_TAG[0] + ', v0.39 and v0.40 peeling as before ;',
    '    the local main of SIDE-explicit-formula fast-forwarded to the landing by the one-call tool, read back equal ; SIDE-dirichlet-mod-24`s main ' + WL.M24_MAIN + ' and ' + WL.M24_TAG[0] + ' peeling to ' + WL.M24_TAG[2][:8] + ', unmoved, nothing pushed there but the removal of (3) ;',
    '    the four held branches of SIDE-explicit-formula at their tips, zq-b730 at ' + WL.ZQ_TIP[:8] + ' unmoved ; ' + _K5_DEL + ' ; the rebuild-b721 branches of the wave 1 kernels as b759 found them ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches in SIDE-explicit-formula of the ' + str(WL.MAX_DISPATCHES) + ' (R369)(5) allows, each read by its run id from its artifact, the exit file governing (relay data/b759_dispatch_rows.json, data/b759_controls.txt) ; none in SIDE-dirichlet-mod-24 (' + str(len(WL.M24_RUNS)) + ' rows), which (R369)(11) leaves untouched but for the branch removal of (3) ;',   # ### b759 step zero: the dispatch line read against (R369)(5) and (11) and rewritten; the section's other lines are b758's and are rewritten before the close
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each record route, suite part and dispatch ;',
    '    the push-b758-* branches of relay and PLACE-papers deleted at step zero by name, one per message, the --merged listing printed before them as captured shell commands ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ v1.36.3 to v1.36.7, each a version commit of its own with its controls in its bank before its use, v1.36.7 before any kernel write ; each act tool committed before its run ; a kernel`s main moved after its run`s success alone ; the (W) regeneration and the pre-lock dry before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: v0.2 equal to the composition, the text block with its fields filled from the banks (relay data/b759_compose.txt) ; each line of (9) at the digest the corpus bank wrote ; each note of (8) and write of (10) read back at HEAD (relay data/b759_notes.json, data/b759_errata.json) ; no sentence of the act saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved ; a sentence of the act about a result at the control naming the side ; no sentence saying the mechanism catalogue has or has not met the zero ; the entry`s INTEGRATION line composed from the banks` feet ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; (6)`s route two at -23 and the reproduction run as (11) orders them ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed, the kernel`s commits and tag message among them (relay data/b759_address_scan.txt, data/b759_address_scan_postlock.txt, data/b759_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no anchor edited ; five orders entered by name in OPEN_TRAILS under (10), no W-ORD-RECUT order, (9) leaving no line ;',
    '    on PLACE-papers main FINDINGS (the corrigendum, the entry), the new file phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md beside v0.1, v0.1 unchanged, REGISTRY (the row 1.5c-24 and a note at the file`s end), FACES_LEDGER and the census (a note at each file`s end), the fourteen lines of (9) in nine documents, ERRATA (two entries at the file`s end), OPEN_TRAILS ((10)`s block under one dated head, and the trail) ; no other sentence of a paper`s body edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b759`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; no rules bank written this act ;',
    '    tools/standing/ v1.36.3, v1.36.4, v1.36.5, v1.36.6 and v1.36.7, five version commits each with its controls in its bank (relay data/b759_standing_v1363.txt to data/b759_standing_v1367.txt) ; ' + (('HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay ' + WL.HANDOFF_COMMIT[:8]) if WL.HANDOFF_COMMIT else 'HANDOFF.md not written: tools/standing/handoff.py refused the page, three needles not found -- REGISTRY :373 no heading after (8)`s row at :180, b759`s ferry no line opening its holds clause, b758`s ferry no THE ACT`S PLACE -- the page standing at b758`s (relay data/b759_handoff_halt.txt)') + ' ; act_current`s shared_edits as standing/carry.py shared reads them ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R369)(11) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one ((R369)(11)), its answer in relay data/b759_author_answers.txt ;',
    '        W-ORD-MECHANISM-ATTRIBUTION open on the author`s word with T0 and T1 beside it, and the five orders of (10), each priced by no build (relay data/b759_errata.json) ;',
    '        push-b759-weil kept for the next act`s step zero ; the two lines of print_targets.txt no print can reach by the workflow`s filter, named and not edited (relay data/b759_presend.txt) ;',
    '        the composer`s two listed cites in v0.2, v0.1`s own :31 at v0.2 :44 and data/b744_zetabox_plan.txt :138-:139 (relay data/b759_compose.txt, data/b759_misses.txt (9), (10)) ; the defects of relay data/b759_defects.txt for the next corrigendum ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; ' + WL.WEIL_BRANCH[0] + ' at ' + WL.WEIL_BRANCH[1][:8] + ', merged into main at v0.41, kept for the next act`s step zero; ' + ('the branches of (3) removed at the kernels` remotes (' + ', '.join(b_ for b_, _t in WL.KERNEL_DELETES) + ')' if WL.KERNEL_DELETES else 'the branches of (3) standing at the kernels` remotes') + ';',
    '        push-b757-workflow of SIDE-dirichlet-mod-24, a local branch of its clone, merged into its main at ' + WL.M24_MAIN + '; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b759 found them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main but SIDE-explicit-formula ((R369)(5)), SIDE-dirichlet-mod-24 touched by the removal of (3) alone ; '
          'SIDE-explicit-formula main %s (' + ', '.join('%s at %s' % (t_, p_) for t_, p_ in _LT5) + (' cut at main`s read-back' if _LT5 else 'unmoved, no tag cut') + '), v0.37 %s, v0.17 %s, v0.38 peeling to ' + WL.ZQ_TAG[2][:12] + ', v0.39 and v0.40 as b758 cut them, '
          + 'the held branches off main, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b759: five standing changes, v1.36.3 to v1.36.7, each read in the standing changes section; the carry's diffs here (b759 carried at
    # ### step zero before the fold; its tools since are the templates and tools/acts/b759.py)
#⟪END⟫
#⟪SECTION record 1⟫
    # ### b759 (R369)(3), (5): the kernels as the act left them, (5)'s branch and its two commits; what main moved to read from the outcomes
    # ### bank by the figures (f['oc']), not here
    # ### b759: the entering tag is v0.40, b758's, peeling to EF_BASE ((R369)'s SCOPE READ, data/b759_ferry.txt :3); the carry had left ZQ_TAG
    # ### (v0.38 peeling to 14ca5725) beside EF_BASE in this print, which no bank carries (23:19:5xZ)
    print('  kernels read: %d (SIDE-explicit-formula entering at main %s with v0.40 peeling to %s; (5)`s branch %s at %s from main %s, its commits %s; '
          'the five branches of (3) removed at the kernels` remotes, %s; SIDE-dirichlet-mod-24 at main %s with %s peeling to %s; no kernel beyond the two written)' % (
              len(ks), K.EF_BASE[:8], K.EF_BASE[:8], K.WEIL_BRANCH[0], K.WEIL_BRANCH[1][:8], K.EF_BASE[:8],
              ', '.join('%s %s' % (k_, c_[:8]) for k_, _kn, c_, _b in K.KERNEL_COMMITS), ', '.join(b_ for b_, _t in K.KERNEL_DELETES),
              K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8]))
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
    b759's form over b759's objects ((R369)(1)-(11)): the corrigendum's foot; the five standing versions' controls from their banks ((4)'s
    four and the kernel route); the pre-send reads' foot with the salt check; the outcome of (5) from the outcomes bank, its foot and its row's
    run, commit, tag, tag object and peel; the dispatch rows by kernel and the controls tool's banks; the ceiling's readings; (6)'s table and
    (7)'s cost law, fields and fields' corpus route; (8)'s composition and its three notes; (9)'s corpus lines; (10)'s ERRATA entries and
    OPEN_TRAILS block; (11)'s reproduction run; b758's scores close; the citation check; the address scan; each by its own lines through
    _bfig, which refuses where a bank does not carry its figure, the json banks read whole and refused where their rows are not the act's;
    the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    vs_ = [(v_,) + _bfig(b_.split('/', 1)[1], r'\*\*%s: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*' % re.escape(v_), '%s`s controls' % v_)
           for v_, _c, b_, _n in K.STANDING_BANKS]
    # ### b759, before the lock: (5)'s pre-send reads with the salt check and its outcome, the dispatches, the ceiling, (6)'s table, (7)'s
    # ### cost law, fields and corpus route, (8)'s composition and notes, (9)'s corpus lines, (10)'s errata, (11)'s reproduction run, b758's close
    ps_ = _bfig('%s_presend.txt' % ACT, r'\*\*THE PRE-SEND READS AT ([0-9a-f]{8}): DUPLICATES (\d+) \(OVER THE TARGETS (\d+)\) ; ANONYMOUS PAIRS (\d+) \(OF (\d+), (\d+) UNREAD\) ; '
                r'REFUSED BY THE FILTER (\d+) \(([^)]*)\), THE TWO KNOWN (YES|NO) ; TARGETS (\d+) MODULES FOR (\d+) NAMES, (\d+) REFUSED, MODULES REFUSED (\d+) ; THE SALT CHECK ([A-Z ]+?) ; '
                r'CONTROLS (\d+) OF (\d+)\.\*\*', 'the pre-send reads` foot')
    of_ = _bfig('%s_outcomes.txt' % ACT, r'\*\*THE OUTCOME OF \(5\): ([A-Z, ]+?) ; RUNS READ (\d+) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the outcome`s foot')
    oj_ = dict((r_.get('item'), r_) for r_ in (json.loads(rdn('%s_outcomes.json' % ACT)) or []))
    if sorted(oj_) != ['weil'] or oj_['weil'].get('outcome') != of_[0] or oj_['weil'].get('unfilled') or not oj_['weil'].get('sentence') \
            or (of_[0].startswith('LANDED') and not (oj_['weil'].get('tag') == 'v0.41' and oj_['weil'].get('peel') and oj_['weil'].get('tag_object'))):
        sys.exit('### data/%s_outcomes.json DOES NOT CARRY (5)`S ONE OUTCOME AS ITS FOOT GIVES IT, FILLED, WITH ITS TAG WHERE IT LANDED -- NOTHING COMPOSED' % ACT)
    dr_rows_ = json.loads(rdn('%s_dispatch_rows.json' % ACT)) or []
    dk_ = lambda kn_, kd_: [r_ for r_ in dr_rows_ if r_.get('kernel') == kn_ and r_.get('kind') == kd_]
    cc_ = _bfig('%s_controls_control.txt' % ACT, r'\*\*THE TOOL`S CONTROLS: (\d+) OF (\d+) AS WANTED ; ALL AS WANTED\.\*\*', 'the controls tool`s control bank')
    cb_ = _bfig('%s_controls.txt' % ACT, r'\*\*DISPATCHES (\d+) \(SIDE-explicit-formula (\d+) OF (\d+), SIDE-dirichlet-mod-24 (\d+) OF (\d+)\) ; READ KERNEL \(THE BUILD EXITING 0\) (\d+), '
                r'OF THEM WITH THE AXIOMS PRINT RUN (\d+) ; THE TOOL`S CONTROLS (\d+) OF (\d+)\.\*\*', 'the controls bank`s foot')
    ce_ = _bfig('%s_ceiling.txt' % ACT, r'\*\*THE CEILING: READINGS (\d+) ; THE LAST AT (\S+), ([\d.]+) h OF (\d+) ; (NOTHING CARRIED|[^;]+? CARRIED) ; DISPATCHES (\d+) OF (\d+)\.\*\*',
                'the ceiling`s readings')
    c3_ = _bfig('%s_c3table.txt' % ACT, r'\*\*THE TABLE OF APPENDIX A: (REPRODUCED|NOT REPRODUCED[^;]*) ; ROUTE ONE AGREES (\d+) OF (\d+) ; ROUTE TWO AGREES (\d+) OF (\d+) ; '
                r'\(a\) (HOLDS|FAILS) ; \(b\) (HOLDS|FAILS) ; THE PLANT ([A-Z ]+)\.\*\*', 'the table`s foot')
    cl_ = _bfig('%s_costlaw.txt' % ACT, r'\*\*F1 ([\d.]+) \(THE QUOTIENT ([\d.]+), ([^,]+), THE SENTENCE (STANDS|[A-Z ]+?)\) ; F2 ([^;]+?) ; INSTRUMENTS :556 CARRYING BOTH HEIGHTS ; '
                r'CONTROLS (\d+) OF (\d+)\.\*\*', 'the cost law`s foot')
    fd_ = _bfig('%s_fields.txt' % ACT, r'\*\*FIELDS FILLED (\d+) ; LEFT (\d+) \(([^)]*)\) ; AX CELLS (\d+) ; THE PIN (.+?) ; THE LAW (THEOREM|OBSERVED) ; REFUSALS (\d+) ; '
                r'CONTROLS (\d+) OF (\d+)\.\*\*', 'the fields` foot')
    fc_ = _bfig('%s_fields_corpus.txt' % ACT, r'\*\*N (\d+) ; DEPOSITS (FILLED|[A-Z ]+?) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the fields` corpus route`s foot')
    cp_ = _bfig('%s_compose.txt' % ACT, r'\*\*v0\.2 COMPOSED: (\d+) LINES ; BLOCK B (\d+) OF (\d+) ; CITES (\d+), CORRECTED (\d+), LISTED (\d+) ; 9\.9 ([A-Z -]+?) ; BRACKETS LEFT (\d+) ; '
                r'THE STEMS ([A-Z ]+?) ; v0\.1 ([A-Z]+) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the composition`s foot')
    cr_ = _bfig('%s_corpus.txt' % ACT, r'\*\*RE-CUT (\d+) OF (\d+) ; LEFT (\d+) ; ORDERS (\d+) ; DEPOSITED COPIES (\d+) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the corpus lines` foot')
    rp_ = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ; (\d+) s\.\*\*', 'the reproduction run`s foot')
    nr_ = jl('%s_notes.json' % ACT)
    if not isinstance(nr_, list) or [r_.get('item') for r_ in nr_] != ['reg', 'faces', 'census'] or not all(r_.get('read_back') is True for r_ in nr_):
        sys.exit('### data/%s_notes.json DOES NOT CARRY (8)`S THREE NOTES, EACH READ BACK -- NOTHING COMPOSED' % ACT)
    er_ = jl('%s_errata.json' % ACT)
    if not isinstance(er_, list) or [r_.get('item') for r_ in er_] != ['errata', 'trails'] or not all(r_.get('read_back') is True for r_ in er_):
        sys.exit('### data/%s_errata.json DOES NOT CARRY (10)`S TWO WRITES, EACH READ BACK -- NOTHING COMPOSED' % ACT)
    cj_ = jl('%s_corpus.json' % ACT)
    if not isinstance(cj_, dict) or len(cj_.get('rows') or []) != 14 or len(cj_.get('docs') or []) != len(K.C3_CORPUS_PP) or not (cj_.get('summary') or {}).get('sentence'):
        sys.exit('### data/%s_corpus.json DOES NOT CARRY (9)`S FOURTEEN LINES, ITS DOCUMENTS AND ITS SENTENCE -- NOTHING COMPOSED' % ACT)
    cps_ = re.search(r'(?m)^  (THE_EPSTEIN_CONTROL_OBJECT stands at v0\.2: .+)$', rdn('%s_compose.txt' % ACT))
    c6s_ = re.search(r'the sentence is "(The table of Appendix A reproduces[^"]+)"' if c3_[0] == 'REPRODUCED' else r'the sentence is "(The table of Appendix A did not reproduce[^"]+)"',
                     rdn('%s_ferry.txt' % ACT))
    if not cps_ or not c6s_:
        sys.exit('### THE SENTENCES OF (6) AND (8) ARE NOT READ FROM THE FERRY AND THE COMPOSITION BANKS -- NOTHING COMPOSED')
    b7c_ = jl('b758_scores_close.json') or {}
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b758: no order entered; W-ORD-SQUARES-AT-24 takes its price in (8)'s OPEN_TRAILS block
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                corr_findings=((co.get('findings') or {}).get('claim'), (co.get('findings') or {}).get('close'), (co.get('findings') or {}).get('repeat')),
                vers=[(v_, c_, int(n_), int(w_)) for v_, c_, n_, w_ in vs_],   # ### the five: (version, controls, cases, as wanted)
                changes=sum(1 for v_, _c, n_, w_ in vs_ if v_ in ('v1.36.3', 'v1.36.4', 'v1.36.5', 'v1.36.6') and int(n_) == int(w_)),   # ### (4)(i)-(iv), each landed with its controls
                ps_rev=ps_[0], ps_dup=int(ps_[1]), ps_anon=(int(ps_[3]), int(ps_[4]), int(ps_[5])), ps_refused=int(ps_[6]), ps_refused_lines=ps_[7], ps_known=ps_[8],
                ps_modules=int(ps_[9]), ps_names=int(ps_[10]), ps_names_refused=int(ps_[11]), ps_mod_refused=int(ps_[12]), ps_salt=ps_[13], ps_ctl=(int(ps_[14]), int(ps_[15])),
                oc=dict((k_, dict(outcome=oj_[k_].get('outcome'), run=oj_[k_].get('run'), sha=(oj_[k_].get('sha') or '')[:8], sentence=oj_[k_].get('sentence'),
                                  tag=oj_[k_].get('tag'), peel=(oj_[k_].get('peel') or '')[:8], tag_object=(oj_[k_].get('tag_object') or '')[:8], grade=oj_[k_].get('grade'),
                                  axiom_lines=((oj_[k_].get('runs') or [{}])[-1]).get('axiom_lines'))) for k_ in oj_),
                weil_word=oj_['weil'].get('outcome'), oc_ctl=(int(of_[2]), int(of_[3])), oc_runs=int(of_[1]),
                st_word='landed at v0.41' if of_[0] == 'LANDED, COMPILED' else ('did not compile' if of_[0].startswith('LANDED') else 'did not land'),
                pl_word='landed' if of_[0].startswith('LANDED') else 'not',
                close_word='at its weight' if rdn('b758_closing.txt', optional=True) and b7c_ else 'carried',
                b7_held=sum(1 for v_ in b7c_.values() if (v_ or [''])[0] == 'HELD'), b7_refuted=[k_ for k_, v_ in sorted(b7c_.items()) if (v_ or [''])[0] != 'HELD'],
                disp_ef=len(dk_('SIDE-explicit-formula', 'dispatch')), disp_m24=len(dk_('SIDE-dirichlet-mod-24', 'dispatch')),
                read_ef=len(dk_('SIDE-explicit-formula', 'read')), read_m24=len(dk_('SIDE-dirichlet-mod-24', 'read')),
                cc_ctl=(int(cc_[0]), int(cc_[1])), cb_kernel=int(cb_[5]), cb_printed=int(cb_[6]), cb_ctl=(int(cb_[7]), int(cb_[8])),
                ce_n=int(ce_[0]), ce_at=ce_[1], ce_sum=ce_[2], ce_ceiling=int(ce_[3]), ce_word=ce_[4], ce_disp=(int(ce_[5]), int(ce_[6])),
                c3_word=c3_[0], c3_one=(int(c3_[1]), int(c3_[2])), c3_two=(int(c3_[3]), int(c3_[4])), c3_a=c3_[5], c3_b=c3_[6], c3_plant=c3_[7],
                table_word='reproduced' if c3_[0] == 'REPRODUCED' else 'not, at %s' % c3_[0][len('NOT REPRODUCED'):].strip(' ,') or 'a cell',
                law_word='a theorem by written proof' if fd_[5] == 'THEOREM' else 'observed', c6_sentence=c6s_.group(1),
                cl_f1=cl_[0], cl_quot=cl_[1], cl_agree=cl_[2], cl_word=cl_[3], cl_f2=cl_[4], cl_ctl=(int(cl_[5]), int(cl_[6])),
                fd_filled=int(fd_[0]), fd_left=int(fd_[1]), fd_left_names=fd_[2], fd_ax=int(fd_[3]), fd_pin=fd_[4], fd_law=fd_[5], fd_refused=int(fd_[6]), fd_ctl=(int(fd_[7]), int(fd_[8])),
                fc_n=int(fc_[0]), fc_word=fc_[1], fc_ctl=(int(fc_[2]), int(fc_[3])),
                cp_lines=int(cp_[0]), cp_b=(int(cp_[1]), int(cp_[2])), cp_cites=int(cp_[3]), cp_corrected=int(cp_[4]), cp_listed=int(cp_[5]), cp_99=cp_[6], cp_left=int(cp_[7]),
                cp_stems=cp_[8], cp_v01=cp_[9], cp_ctl=(int(cp_[10]), int(cp_[11])), c8_sentence=cps_.group(1),
                doc_word=('entered at v0.2, %d fields left' % int(cp_[7])) if cp_[9] == 'UNCHANGED' else 'not entered',
                cr_recut=int(cr_[0]), cr_of=int(cr_[1]), cr_left=int(cr_[2]), cr_orders=int(cr_[3]), cr_deposits=int(cr_[4]), cr_ctl=(int(cr_[5]), int(cr_[6])),
                c9_sentence=(cj_.get('summary') or {}).get('sentence'), corpus_docs=[(d_.get('path'), (d_.get('commit') or '')[:8]) for d_ in cj_.get('docs') or []],
                rp_rows=int(rp_[0]), rp_repro=int(rp_[1]), rp_differs=int(rp_[2]), rp_notrun=int(rp_[3]), rp_ctl=(int(rp_[4]), int(rp_[5])), rp_secs=int(rp_[6]),
                notes=[(r_.get('item'), r_.get('file'), dict((it_, c_) for it_, _f, c_ in K.C3_NOTES_PP).get(r_.get('item'), '-'), len(r_.get('lines') or [])) for r_ in nr_],
                notes_written=len(nr_), notes_reg=(nr_[0].get('notes') or {}),
                errata=[(r_.get('item'), r_.get('file'), dict((it_, c_) for it_, _f, c_ in K.C3_ERRATA_PP).get(r_.get('item'), '-'), len(r_.get('lines') or []), r_.get('notes') or {}) for r_ in er_],
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R369): no lean process runs on this host; each build a runner dispatch read by its run id from the artifact, the exit file
    governing (each dispatch row with one read row of its run, the read's exit read); the dispatch counts within (5)'s and (11)'s, 3 in
    SIDE-explicit-formula and 0 in SIDE-dirichlet-mod-24, the worklist's EF_RUNS and M24_RUNS each the runs of its kernel's dispatch and
    read rows; each dispatch under the memory hold (free_mb at or above 2,560 MB) and the disk hold (each volume at or above 5,000 MB) as its
    row banks them, each read row carrying free_mb; each dispatch row naming the licence of step zero's banks; the dispatch commands in the
    capture as many as the dispatch rows and the sends refused; no suite part in the background. From the command bank (the seat's commands,
    read live from the capture by the `commands` route), the dispatch rows beside the worklist's runs, and the hook's refusal bank (a suite
    part sent in the background refused BACKGROUND)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    per_ = []
    # ### b759 step zero: read against (R369)(5)'s and (11)'s caps (3 in SIDE-explicit-formula, 0 in SIDE-dirichlet-mod-24): the loop's form holds
    # ### for both, the second kernel's rows and runs empty and its count 0 within its cap 0
    for kn_, runs_w_, cap_ in (('SIDE-explicit-formula', K.EF_RUNS, K.MAX_DISPATCHES), ('SIDE-dirichlet-mod-24', K.M24_RUNS, K.MAX_DISPATCHES_M24)):
        d_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'dispatch') if r.get('kernel') == kn_)
        r_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read') if r.get('kernel') == kn_)
        per_.append((kn_, len(d_), cap_, d_ == r_ == sorted(str(x) for x in runs_w_)))
    runs_ = all(o_ for _k, _n, _c, o_ in per_) and all(n_ <= c_ for _k, n_, c_, _o in per_)
    twice_ = sorted(set(x for x in reads_ if reads_.count(x) > 1))
    # ### the disk read of a dispatch row under either of tools/b758_controls.py's two keys: `disk_mb` (the send's route, :248, read before the
    # ### send) and `disk_mb_at_row` (the rowsent route, :277, the join's row alone, read at the row) -- defect (u): the reader read the second alone
    dk_ = lambda r: r.get('disk_mb') if r.get('disk_mb') is not None else r.get('disk_mb_at_row')
    dmin_ = lambda r: min(dk_(r).values()) if isinstance(dk_(r), dict) and dk_(r) else (dk_(r) if isinstance(dk_(r), int) else -1)
    free_ = [r.get('n') for r in _ef_kind(rows_, 'dispatch') if not isinstance(r.get('free_mb'), int) or r['free_mb'] < 2560 or dmin_(r) < 5000] \
        + [r.get('n') for r in _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    exits_ = ['%s %s exit %s %s' % (r.get('kernel', '')[5:], r.get('run'), r.get('build_exit'), r.get('verdict')) for r in _ef_kind(rows_, 'read')]
    unexit_ = [r.get('run') for r in _ef_kind(rows_, 'read') if str(r.get('build_exit') or '') == '']
    bg_ = [l for l in rdn('%s_hook_refusals.txt' % ACT).split(NL) if '| BACKGROUND |' in l]
    bgc_ = [r['n'] for r in ((cm.get('rows') or []) if cm else []) if r.get('bg') and re.search(r'fold\.py"? checks\b|_checks\.py', r.get('cmd') or '')]
    refused_ = _ef_kind(rows_, 'dispatch_refused')
    lic_ = [r for r in _ef_kind(rows_, 'dispatch') if not str((r.get('licence') or {}).get('commit') if isinstance(r.get('licence'), dict) else r.get('licence') or '').startswith(K.STEPZERO_BANKS[:8])]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(_ef_kind(rows_, 'dispatch')) + len(refused_) and runs_ and not twice_ \
        and not free_ and not unexit_ and not lic_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b759_commands.json): %s; dispatch commands in the capture: %s, against the dispatch rows %d and the sends refused by the host (no run) %d; by kernel, dispatches against (10)`s cap and the worklist`s runs each a dispatch row`s and a read row`s: %s; reads %d, a run read twice: %s; each read`s exit file: %s; a read with no exit read: %s; dispatch rows under the memory hold 2,560 MB or the disk hold 5,000 MB, or a row without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b759_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(_ef_kind(rows_, 'dispatch')), len(refused_),
            ', '.join('%s %d of %d, the runs %s' % (k_, n_, c_, o_) for k_, n_, c_, o_ in per_), len(reads_), ', '.join(twice_) or 'none', '; '.join(exits_),
            unexit_ or 'NONE', free_ or 'NONE', K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b758's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line);
# ### the controls tool's own controls stand in a bank of their own (data/b758_controls_control.txt), read by time against the opening dispatch
N2_CONTROLS = (('data/b759_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b759_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b759_standing_v1363.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.3: CONTROLS '),
               ('data/b759_standing_v1364.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.4: CONTROLS '),
               ('data/b759_standing_v1365.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.5: CONTROLS '),
               ('data/b759_standing_v1366.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.6: CONTROLS '),
               ('data/b759_standing_v1367.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.7: CONTROLS '),
               ('data/b759_presend.txt', '## THE CONTROLS', '## AT 630cba16'),
               ('data/b759_outcomes.txt', '## THE CONTROLS', '## (5) THE STATEMENT AND THE PRINT LINES'),
               ('data/b759_ceiling.txt', '## THE CONTROLS', '## THE READINGS, EACH APPENDED WHEN TAKEN'),
               ('data/b759_controls.txt', '## THE CONTROLS', '## SIDE-explicit-formula: '),
               ('data/b759_c3table.txt', '## THE PLANT, PRINTED BEFORE ANY USE OF THE RESULT', '## ROUTE ONE, THE GROUP-RING MODEL'),
               ('data/b759_costlaw.txt', '## THE CONTROLS', '## THE INPUTS, EACH READ FROM A BANK'),
               ('data/b759_fields.txt', '## THE CONTROLS', '## THE READS'),
               ('data/b759_fields_corpus.txt', '## THE CONTROLS', '## THE FIELDS'),
               ('data/b759_compose.txt', '## THE CONTROLS (planted)', '## THE COMPOSITION'),
               ('data/b759_corpus.txt', '## THE CONTROLS', '## THE FOURTEEN LINES'))
N2_CONTROLS_COEFF = ('data/b759_coeff.txt', '## THE CONTROLS', '## THE MERGE ON push-b759-coeff')   # ### (carried, inert: no coeff bank at b759)
N2_PUSHES = ('SIDE-explicit-formula_push-b759-weil',)   # ### the gated push's capture, data/b759_<kernel>_<branch>_push_out.txt: (5)'s branch and main's one move
N2_WORKFLOW = None   # ### b759: no move of a kernel's main ahead of a build


def _main_moves():
    """N2 (R368): each move of a kernel's main in the gated push's captures, (capture, time, tip, the run whose success licenses it or the
    workflow's exception, ok): a section of a capture opening at its stamped `capture on` line and carrying a ` -> main` line; its tip the
    section's `tip` field; licensed where a read row of the dispatch rows reads exit 0 for a dispatch at that tip, read before the section's
    time, or the tip is (6)(i)'s workflow commit."""
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    sha_ = dict((str(r.get('run')), r.get('sha') or '') for r in _ef_kind(rows_, 'dispatch'))
    ok_reads_ = [(sha_.get(str(r.get('run')), ''), _iso_epoch(r.get('free_at') or r.get('at') or '') or 0, r.get('run')) for r in _ef_kind(rows_, 'read')
                 if str(r.get('build_exit')) == '0']
    out_ = []
    for p_ in N2_PUSHES:
        t_ = rdn('%s_%s_push_out.txt' % (ACT, p_), optional=True) or ''   # ### b758: (5)'s capture absent where (5) was not begun
        for sec_ in re.split(r'(?m)^(?=push_gated: capture on )', t_):
            if not re.search(r'(?m)^\s+\S+\.\.\S+\s+\S+ -> main$|\[new branch\]\s+\S+ -> main$', sec_):
                continue
            ts_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', sec_)
            tip_ = re.search(r'; tip ([0-9a-f]{40})', sec_)
            te_ = _iso_epoch(ts_.group(1)) if ts_ else None
            tp_ = tip_.group(1) if tip_ else ''
            lic_ = [run_ for s_, e_, run_ in ok_reads_ if tp_ and s_.startswith(tp_[:8]) and te_ and e_ < te_]
            wf_ = bool(N2_WORKFLOW) and tp_.startswith(N2_WORKFLOW)
            out_.append((p_, ts_.group(1) if ts_ else 'unread', tp_[:8], 'the workflow of (6)(i)' if wf_ else (lic_[0] if lic_ else 'NONE'), bool(te_) and (wf_ or bool(lic_))))
    return out_
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
N2_SECTIONS = ()
N2_RIDERS = ('data/b759_steps.json', 'data/b759_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


def _hms_epoch(hms):
    """a step-zero time of day (HH:MM:SS, UTC) on the act's date, as an epoch; None where unread."""
    import calendar
    try:
        return calendar.timegm(time.strptime('%s %s' % (K.DATE, hms), '%Y-%m-%d %H:%M:%S'))
    except Exception:
        return None


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R369): "the step-zero reads, the chain read and the carry print before any write, a scratch file among the writes; each standing
    change lands with its controls before its use; each act tool commits before it runs; a kernel's main moves after its run's success and
    at no other time." Read: the chain read, the step-zero reads and the carry by the step-zero bank's times, in that order, before the
    act_current commit; the act's commits in the worklist's TIME_ORDER by time, relay and PLACE-papers together; each of the five standing
    changes (v1.36.3 to v1.36.7) a commit of its own moving VERSION with its controls bank, the act's commits under tools/standing/ those five
    and no other; the kernel route (v1.36.7) landing before any kernel write; each tool of K.GENS first added by a commit of its own carrying it
    and not its bank, the bank's commit not the tool; the controls tool's own controls banked AS WANTED after its commit and before its
    opening dispatch; each tool's controls before its figures; each move of a kernel's main in the gated push's captures after a read of
    its run exiting 0 at that tip; the (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate; the kernel
    route an ancestor of HEAD."""
    if rdn('%s_coeff.txt' % ACT, optional=True) and N2_CONTROLS_COEFF not in N2_CONTROLS:
        globals()['N2_CONTROLS'] = N2_CONTROLS + (N2_CONTROLS_COEFF,)   # ### (5)'s merge bank where (5) was begun
    ct_ = lambda r_, h_: int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0)
    keyed_ = dict([(k_, (ROOT, h_)) for k_, h_ in K.CHAIN] + [(k_, (PP, h_)) for k_, h_ in K.PP_CHAIN]
                  + [('actcur', (ROOT, K.ACT_CURRENT_COMMIT)), ('stepzero', (ROOT, K.STEPZERO_BANKS))]
                  + [(k_, (ROOT, h_)) for k_, h_ in (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT)) if h_])
    okeys_ = list(K.TIME_ORDER) + [k_ for k_ in ('passed', 'handoff') if k_ in keyed_ and k_ not in K.TIME_ORDER]
    chain_ = [keyed_[k_] for k_ in okeys_ if k_ in keyed_]
    tm_ = [ct_(r_, h_) for r_, h_ in chain_]
    order_ = len(chain_) == len(okeys_) and set(okeys_) == set(keyed_) and all(tm_) and tm_ == sorted(tm_)
    files_ = lambda h_: [x for x in g(ROOT, 'show', '--name-only', '--format=', h_).split() if x.strip() and x not in N2_RIDERS]
    # ### the step-zero reads, the chain read and the carry, each with its time in the step-zero bank, before the act_current commit
    sz_ = rdn('%s_stepzero.txt' % ACT)
    # ### b759's step-zero bank: the chain read at :7 ("THE CHAIN READ the first call after the delivery (18:12:47Z)"), the reads at :8
    # ### (18:13:42Z), the carry at :12 (18:14:05Z); the first match of each, the later chain reads after summaries standing below them
    szt_ = [(n_, re.search(p_, sz_, re.S)) for n_, p_ in (('the chain read', r'THE CHAIN READ[^(\n]*\((\d\d:\d\d:\d[\dx])Z'),
                                                          ('the step-zero reads', r'THE STEP-ZERO READS \((\d\d:\d\d:\d\d)Z'),
                                                          ('the carry', r'THE CARRY before any (?:other )?write of the relay: .*?(\d\d:\d\d:\d\d)Z'))]
    sze_ = [(n_, _hms_epoch(m_.group(1).replace('x', '0')) if m_ else None) for n_, m_ in szt_]
    stepzero_ = all(e_ for _n, e_ in sze_) and [e_ for _n, e_ in sze_] == sorted(e_ for _n, e_ in sze_) and sze_[-1][1] < tm_[0]
    # ### the standing changes: each of the five a commit of its own moving VERSION with its controls bank; the act's commits under
    # ### tools/standing/ those five and no other
    st_commits_ = [h_ for h_ in g(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()]
    st_rows_ = [(v_, c_, 'tools/standing/VERSION' in files_(c_) and b_ in files_(c_)) for v_, c_, b_, _n in K.STANDING_BANKS]
    standing_ = all(o_ for _v, _c, o_ in st_rows_) and [h_[:8] for h_ in st_commits_] == [c_[:8] for _v, c_, _b, _n in K.STANDING_BANKS]
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, 'HEAD'], capture_output=True).returncode == 0
    # ### each tool before its bank (K.GENS)
    gens_ok_ = []
    for n_, tool_, gens_, data_, bank_ in K.GENS:
        fa_ = _first_add(tool_)
        gens_ok_.append((n_, bool(fa_) and fa_ == g(ROOT, 'rev-parse', gens_[0]).strip() and all(tool_ in files_(h_) and data_ not in files_(h_) for h_ in gens_)
                         and data_ in files_(bank_) and tool_ not in files_(bank_) and max(ct_(ROOT, h_) for h_ in gens_) < ct_(ROOT, bank_)))
    gen_ = len(gens_ok_) == len(K.GENS) >= 6 and all(o_ for _n, o_ in gens_ok_)
    # ### the kernel route (v1.36.7, K.C1_STANDING) landed, with its controls bank, before any kernel write (the earliest of K.KERNEL_COMMITS)
    kd_ = {'SIDE-explicit-formula': K.EF_DIR, 'SIDE-dirichlet-mod-24': K.M24_DIR}
    kt_ = [(k_, c_, ct_(kd_[kn_], c_)) for k_, kn_, c_, _b in K.KERNEL_COMMITS]
    kw0_ = min([t_ for _k, _c, t_ in kt_ if t_] or [0])
    before_kw_ = all(t_ for _k, _c, t_ in kt_) and ct_(ROOT, K.C1_STANDING) < kw0_
    # ### the controls tool committed, then its own controls banked AS WANTED, then its opening dispatch (the dispatch rows' first 'at')
    cc_t_ = rdn('%s_controls_control.txt' % ACT)
    cc0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)\s*$', (cc_t_.split(NL) or [''])[0])
    d0_ = min([_iso_epoch(r.get('free_at') or '') or 0 for r in _ef_kind(jl('%s_dispatch_rows.json' % ACT) or [], 'dispatch')] or [0])
    cons_ = bool(cc0_) and ct_(ROOT, dict(K.CHAIN)['controls_gen']) < (_iso_epoch(cc0_.group(1)) or 0) < d0_ and 'CONTROLS: 17 OF 17 AS WANTED ; ALL AS WANTED' in cc_t_   # ### b759: the controls tool first committed at 9a5a7dc2 (step 17)
    # ### a kernel's main moved after its run's success and at no other time
    mm_ = _main_moves()
    rev_ = bool(mm_) and all(o_ for *_x, o_ in mm_)
    sect_ = stepzero_ and standing_ and gen_ and cons_ and rev_ and before_kw_
    route_ = sect_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT, optional=True)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the chain read, the step-zero reads and the carry printed before any write, in that order (%s, each by the step-zero bank, before the act_current commit %s): %s; the standing changes, each a commit of its own moving VERSION with its controls bank (%s), the act`s commits under tools/standing/ those five and no other (%s): %s; the kernel route (v1.36.7) before any kernel write (the first kernel commit %s): %s; each tool first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the tool (%s): %s; the controls tool committed (%s), its own controls banked AS WANTED (%s) before its opening dispatch: %s; each move of a kernel`s main after its run`s success at that tip (%s): %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; the act`s %d commits in the worklist`s order by time, relay and PLACE-papers together: %s (%s); the kernel route an ancestor of HEAD: %s; the tools` controls before their figures: %s' % (
            ', '.join('%s %s' % (n_, ('%sZ' % m_.group(1)) if m_ else 'unread') for n_, m_ in szt_), K.ACT_CURRENT_COMMIT, stepzero_,
            ', '.join('%s %s %s' % (v_, c_[:8], o_) for v_, c_, o_ in st_rows_), ' '.join(h_[:8] for h_ in st_commits_) or 'none', standing_,
            ([('%s %s' % (k_, c_)) for k_, c_, t_ in kt_ if t_ == kw0_] or ['unread'])[0], before_kw_,
            ', '.join('%s %s' % x_ for x_ in gens_ok_), gen_, dict(K.CHAIN)['controls_gen'][:8], cc0_.group(1) if cc0_ else 'unread', cons_,
            '; '.join('%s at %s tip %s licensed by %s %s' % x_ for x_ in mm_) or 'NONE', rev_,
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_,
            len(chain_), order_, ' '.join('%s %s@%d' % (k_, h_[:8], c_) for k_, (_r, h_), c_ in zip([k_ for k_ in okeys_ if k_ in keyed_], chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b757's objects): the banks whose grade prints at their end, (bank, the words the foot carries); the address scan written
# ### before the gate. The citation check's foot is its HALT (data/b757_citation_check.txt :149, the one Lean-path row read in the
# ### step-zero bank, defect (c)), read as banked; no reproduction bank ((R367)(10): nothing computed at any field, the builds apart)
# ### b758: (R368)'s N3 reads three clauses -- the writes of (8) equal to the ruling's text filled from the banks; no sentence of zeta, RH, GRH
# ### or Weil positivity on classK for zeta holding, failing or moving; the side named under (9). The novelty and navigator-figure matchers of
# ### (R367)'s N3 stand in neither (R368) nor data/standing_clauses_v9.txt (read 02:5xZ, 0 of each word): printed with their yields, graded by
# ### no clause. The graded feet: each bank's last line its grade, the outcome's words not fixed (the grade a result of the run)
# ### b759: (R369)'s N3 reads five clauses -- v0.2 equal to the text block with its fields filled and (6)'s outcome applied; each sentence
# ### replaced under (9) equal to its NEW; each sentence of (5), (6), (8) and (9) entered in a ledger equal to the ruling's text filled; no
# ### sentence of zeta, RH, GRH or Weil positivity on classK for zeta holding, failing or moving; the side named under (R368)(9); and no
# ### sentence saying the mechanism catalogue has or has not met the zero. The act's own sentences are its banks', the entry's and its
# ### PLACE-papers writes' (v0.2, the fourteen NEWs, the notes and errata lines), each matcher over all three. The graded feet: each bank
# ### closing on a `### ### **` line; the table's and the composition's banks close otherwise and are read by _figs at their own lines
N3_GRADED = (('b759_corrigendum.txt', ('ITEMS 80', 'NO WEIGHT LINE', 'THE ENTRY AT FINDINGS :15550')),
             ('b759_standing_v1363.txt', ('v1.36.3: CONTROLS', 'ALL AS WANTED')), ('b759_standing_v1364.txt', ('v1.36.4: CONTROLS', 'ALL AS WANTED')),
             ('b759_standing_v1365.txt', ('v1.36.5: CONTROLS', 'ALL AS WANTED')), ('b759_standing_v1366.txt', ('v1.36.6: CONTROLS', 'ALL AS WANTED')),
             ('b759_standing_v1367.txt', ('v1.36.7: CONTROLS', 'ALL AS WANTED')),
             ('b759_presend.txt', ('THE PRE-SEND READS AT a3aad4cc: DUPLICATES 0', 'REFUSED BY THE FILTER 2 (:358, :359)', 'THE SALT CHECK PASSED', 'CONTROLS 16 OF 16')),
             ('b759_controls_control.txt', ('THE TOOL`S CONTROLS: 17 OF 17 AS WANTED',)),
             ('b759_controls.txt', ('**DISPATCHES ', 'THE TOOL`S CONTROLS 17 OF 17')),
             ('b759_outcomes.txt', ('THE OUTCOME OF (5): ', 'CONTROLS 8 OF 8')),
             ('b759_ceiling.txt', ('THE CEILING: READINGS ', ' h OF 16 ; ')),
             ('b759_costlaw.txt', ('F1 ', 'CONTROLS 5 OF 5')), ('b759_fields.txt', ('FIELDS FILLED ', 'CONTROLS 7 OF 7')),
             ('b759_fields_corpus.txt', ('N 14 ; DEPOSITS ', 'CONTROLS 7 OF 7')), ('b759_corpus.txt', ('RE-CUT ', 'CONTROLS 4 OF 4')),
             ('b759_reproduce.txt', ('ROWS ', 'PLANTED CONTROLS AS WANTED ')),
             ('b759_citation_check.txt', ('### ### **THE CHECK ', '** (halts ')), ('b759_address_scan.txt', ('PREVIOUS ADDRESS',)))
N3_GRADED_COEFF = ('b759_coeff.txt', ('THE MERGE: ', 'THE FIVE NAMES LINES '))   # ### (carried, inert: no coeff bank at b759)
# ### N3 (R367): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word; the centre
# ### matcher over the clause's own words, "anything of zeta, RH, GRH or Weil positivity on classK for zeta" (data/b757_ferry.txt :51): zeta
# ### (the symbol, Riemann's, or a zeta function not the Epstein's), RH, GRH and Weil positivity on classK -- b756's bare `classK` not carried,
# ### the clause naming classK only inside Weil positivity for zeta, and (R367)(7)'s outcome a test function in classK at the control; the
# ### side matcher over (R367)'s "no sentence about the control speaks of positivity without naming the side"
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
# ### b759: "Weil positivity on classK" read as the clause's "for zeta" unless its sentence places it at the control -- (5)'s ruled sentence
# ### opens "Weil positivity on classK fails at the control on the arithmetic side of its explicit formula", a statement about the Epstein
# ### function, and N3's side clause asks that very sentence to name its side; one control of each kind in record 20 (the planted zeta
# ### sentence caught, (5)'s sentence passed)
N3_LOC = (r'(?:\b(?:RH|GRH)\b|ζ|\bRiemann(?:`s|\'s)? zeta\b|(?<!Epstein )\bzeta function\b|\bWeil positivity on classK\b(?![^.;]*\bat the control\b)).*'
          r'\b(?:holds|hold|fails|fail|proved|refuted|moved)\b')
# ### b759, N3's last clause: "no sentence says the mechanism catalogue has or has not met the zero" -- a negation does not pass it
N3_CAT = r'\bcatalogue\b[^.;]*\b(?:has|have|had)(?: not)? met\b'
N3_SIDE = r'\bpositivity\b'
N3_BANKS = ('stepzero', 'misses', 'corrigendum', 'presend', 'controls_control', 'controls', 'outcomes', 'ceiling', 'c3table', 'costlaw', 'fields',
            'fields_corpus', 'compose', 'corpus', 'reproduce', 'standing_v1363', 'standing_v1364', 'standing_v1365', 'standing_v1366', 'standing_v1367',
            'events', 'defects')
N3_BANKS_OPTIONAL = ('coeff',)   # ### (carried, inert: no coeff bank at b759)
# ### N3 (R367): no figure of the navigator's workspace printed as a banked figure -- the ruling's one figure of the navigator's reading that
# ### no bank of the act computed, (7)'s price "as the navigator read it, 250 to 550 lines and 4 to 8 dispatches" ((R367)(2), (7)), banked
# ### in the price table as the navigator's beside the seat's own: in the act's own sentences and the entry's, each occurrence wants the
# ### navigator named in its sentence
N3_NAV_FIGS = r'\b250(?: to |-)550\b|\b4(?: to |-)8 dispatches\b'
# ### N3 (R367): each write of (9) equal to the ruling's text with its fields filled from the banks -- each line the notes bank names read at
# ### PLACE-papers HEAD by its digest, and each outcome sentence the bank's item names (data/b757_outcomes.json) standing whole in that note
# ### b759, (R369)(8) and (10): the notes bank's three (REGISTRY's row and note; FACES_LEDGER's and the census's, each "made of the document's
# ### own dated head and the sentences of (5) and (8) that came true") and the errata bank's two (ERRATA's two entries; OPEN_TRAILS' block with
# ### the six orders by name); the papers they write since the act's base: lines added, none removed
N3_NOTES = ('reg', 'faces', 'census', 'errata', 'trails')
N3_ORDERS = ('W-ORD-MECHANISM-ATTRIBUTION', 'W-ORD-WSC-KERNEL-CITES', 'W-ORD-LI-INDEX', 'W-ORD-CAPACITY-ATTRIBUTION', 'W-ORD-BIBLIOGRAPHY-LINK',
             'W-ORD-EPSTEIN-SECTIONS-3-4')
N3_V02 = ('phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md', '804a5c96244c5a3f')   # ### (8): the document, and the composition's digest the compose bank prints
N3_V01 = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'   # ### (8): not edited, byte-equal before and after (N4)
N3_PAPERS = (N3_V02[0], 'FACES_LEDGER.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'REGISTRY.md', 'ERRATA.md')
# ### b759: a hit of the matchers over the act's PLACE-papers writes passes only by a hand verdict pinned here by path, line and the sentence's
# ### digest (sha256, 16 hex), each read at b759 before the lock (scratch n3units759.py, read-only, 1,040 units, 1 hit); the words not quoted
N3_HAND = {(N3_V02[0], 317, '205b3041882dca7b'): 'hand-read: the centre matcher`s verb is transitive there, its subject the product and its object the '
                                                   'zeros; the sentence names the statement that for zeta is RH and says of zeta nothing holds, fails or moved'}
N3_CONTROL = r'\b(?:control|Epstein|zq_\w+)\b|x\^2 \+ xy \+ 6y\^2'   # ### a sentence about the control: the control named, the Epstein function, a zq_ name, the form
N3_SIDE_NAMED = r'\b(?:arithmetic|spectral|zero|prime-power) side\b'
import hashlib as _hs   # noqa: E402  ### the notes' digests, sha256 of each line (16 hex), as tools/b757_notes.py writes them; _hs, not _h, which record.tpl :2633 binds to its height formatter (defect (t))


def _side_bad(x):
    """N3 (R367): a sentence about the control that speaks of positivity and names no side of the explicit formula."""
    return bool(re.search(N3_SIDE, x, re.I) and re.search(N3_CONTROL, x) and not re.search(N3_SIDE_NAMED, x))


# ### (R368)(9), THE SIDE RULE NARROWED, from b757 defect (v): "A sentence the act writes about a result names the side where it speaks of
# ### positivity at the control. A line that reports a dated record in that record's own words is outside the rule, and the matcher is taught
# ### the difference by the line's head." The head: the line opens with the record's file and line and the report's separator,
# ### `<file>.md :<n> -- ` or `<file>.lean :<n> -- ` (b757's sweep bank's form, :151-:183, and the statements bank's of (7)); such a line is
# ### read by no side matcher, every other matcher reading it as before. b757's sweep bank is not rewritten.
N3_DATED_HEAD = r'^\s*(?:PLACE-papers )?[\w./-]+\.(?:md|lean) :\d+(?:-:?\d+)? -- '


def _dated_line(l_):
    """(R368)(9): the line's head a dated record's file and line, the report's separator after it."""
    return bool(re.match(N3_DATED_HEAD, l_ or ''))


def _side_sentences(t):
    """(R368)(9): the act's own sentences for the side matcher alone -- _own_sentences over the bank with each line headed by a dated record
    (_dated_line) left out."""
    return _own_sentences(NL.join(l_ for l_ in (t or '').replace(chr(13), '').split(NL) if not _dated_line(l_)))


def _nav_bad(x):
    """N3 (R367): a sentence printing (7)'s price as the navigator read it with no navigator named in it."""
    return bool(re.search(N3_NAV_FIGS, x) and not re.search(r'\bnavigator', x))


def _nav_units(t):
    """N3 (R367), the navigator's figures: a bank's own sentences as _own_sentences cuts them, each table row (a line carrying ' | ', the
    price table's form) read whole and apart -- defect (w): the cut at a row's semicolon parted (7)'s figures from the navigator named
    before it in the same row (data/b757_price.txt :23), and the scores dry of 14:39:47Z read that row's second half as a figure unnamed."""
    ls_ = (t or '').replace(chr(13), '').split(NL)
    rows_ = [l_.strip() for l_ in ls_ if ' | ' in l_ and not l_.startswith('### ')]
    return _own_sentences(NL.join(l_ for l_ in ls_ if ' | ' not in l_)) + rows_


def _own_sentences(t):
    """the act's own sentences of a bank: the quote rows (`  :n "...`) and the quoted spans dropped, the `### ` lines dropped. A quotation
    wrapped over lines is dropped to its closing mark: an opening mark left unmatched on its line opens it, and the lines after it are read
    as the quotation's until a closing mark (data/b755_defects.txt (q): the line-at-a-time drop kept the literature bank's T7.a, a source's
    own words wrapped over three lines, and N3 read them as the bank's)."""
    ls, open_ = [], False
    for l in (t or '').replace(chr(13), '').split(NL):
        if not l.strip() or l.startswith('### '):
            continue
        s_ = l
        if open_:
            m_ = re.search(r'["”]', s_)
            if not m_:
                continue
            s_, open_ = '\x00' + s_[m_.end():], False
        s_ = re.sub(r'“[^”\n]*”', '\x00', re.sub(r'"[^"\n]*"', '\x00', s_))
        m_ = re.search(r'["“]', s_)
        if m_:
            s_, open_ = s_[:m_.start()] + '\x00', True
        if re.match(r'^\s+:\d+(?:-:\d+)? ["“]', l):
            continue
        ls.append(s_.replace('\x00', '"…"').strip())
    return [x for x in re.split(r'(?<=[.;])\s+', ' '.join(ls)) if x.strip()]


def _integ_line(f):
    """the entry's last line, the ferry's INTEGRATION line (data/b759_ferry.txt :51) composed from the banks' feet through _figs, adjusted to
    what the act did: the statement and the print lines by the outcome's foot; the table by its foot and the law by the fields'; the
    document by the composition's foot; the corpus lines by theirs; the standing changes by (4)'s four versions' controls; the dispatches by
    the dispatch rows."""
    return ("INTEGRATION: the statement: %s; the print lines: %s; the table: %s; the law: %s; the document: %s; the corpus lines: %d of 14; "
            "the standing changes: %d of 4; dispatches %d" % (
                f['st_word'], f['pl_word'], f['table_word'], f['law_word'], f['doc_word'], f['cr_recut'], f['changes'], f['disp_ef'] + f['disp_m24']))


N3_KEYS = {}   # ### (carried name, unread at b759)


def _true_sentences():
    """the sentences of (5) and (8) that came true, from their banks: (5)'s where the outcome LANDED (data/b759_outcomes.json), (8)'s the
    compose bank's (its line opening two spaces and "THE_EPSTEIN_CONTROL_OBJECT stands at v0.2: ")."""
    s5_ = [r_.get('sentence') for r_ in (json.loads(rdn('%s_outcomes.json' % ACT)) or []) if str(r_.get('outcome') or '').startswith('LANDED') and r_.get('sentence')]
    m8_ = re.search(r'(?m)^  (THE_EPSTEIN_CONTROL_OBJECT stands at v0\.2: .+)$', rdn('%s_compose.txt' % ACT))
    return s5_, ([m8_.group(1)] if m8_ else [])


def _notes_rows():
    """N3 (R369): each write of (8) and (10) at PLACE-papers HEAD against the ruling's text with its fields filled from the banks -- the notes
    bank's lines (reg, faces, census), each [line, text], read equal at HEAD: FACES_LEDGER's and the census's carrying the sentences of (5)
    and (8) that came true, each whole; REGISTRY's carrying v0.41, its peel and "The tags confer no deposit."; the errata bank's lines (errata,
    trails), each [line, sha256 16 hex, length], read by digest and length at HEAD: ERRATA's carrying its two entries, OPEN_TRAILS' the six
    orders by name; (item, lines, equal). And the papers of (8) and (10) since the act's base: lines added, none removed."""
    s5_, s8_ = _true_sentences()
    want_ = {'reg': ['v0.41', K.WEIL_TAG[2][:8], 'The tags confer no deposit.'], 'faces': s5_ + s8_, 'census': s5_ + s8_,
             'errata': ['E-2026-11-17-1', 'E-2026-11-17-2'], 'trails': list(N3_ORDERS)}
    rows_in_ = dict((r_.get('item'), r_) for r_ in (jl('%s_notes.json' % ACT) or []) + (jl('%s_errata.json' % ACT) or []) if isinstance(r_, dict))
    rows_ = []
    for k_ in N3_NOTES:
        it_ = rows_in_.get(k_) or {}
        txt_ = (_show(PP, 'HEAD', it_.get('file') or '-') or '').replace(chr(13), '').split(NL)
        ls_ = list(it_.get('lines') or [])
        got_ = [txt_[x_[0] - 1] if 0 < (x_[0] or 0) <= len(txt_) else '\x00' for x_ in ls_]
        if k_ in ('errata', 'trails'):
            eq_ = all(_hs.sha256(t_.encode('utf-8')).hexdigest()[:16] == x_[1] and len(t_) == x_[2] for t_, x_ in zip(got_, ls_))
        else:
            eq_ = all(t_ == x_[1] for t_, x_ in zip(got_, ls_))
        body_ = NL.join(got_)
        rows_.append((k_, len(got_), bool(ls_) and eq_ and bool(want_[k_]) and all(w_ in body_ for w_ in want_[k_])
                      and (k_ not in ('faces', 'census') or (len(s5_) == 1 and len(s8_) == 1))))
    rm_ = []
    for p_ in N3_PAPERS + ('OPEN_TRAILS.md',):
        ns_ = g(PP, 'diff', '--numstat', K.PRE_PP, 'HEAD', '--', p_).split()
        if not ns_ or ns_[1] != '0':
            rm_.append('%s %s' % (p_, ns_[:2] or 'UNCHANGED'))
    return rows_, rm_


def _pp_n3():
    """N3 (R369) over the act's PLACE-papers writes: v0.2 at HEAD by the composition's digest (the compose bank's, N3_V02); v0.1 unchanged
    since the act's base; each corpus line of (9) at HEAD by the digest the corpus bank wrote (after_sha), its row RE-CUT; and the act's own
    sentences there -- v0.2's line by line, each NEW of the text bank's BLOCK D, each line the notes and errata banks name -- cut at . ; ?
    before a space, for the centre matcher (outside a negation), the catalogue matcher and the side matcher; a hit named by path, line and
    the sentence's digest, never by its words, passing only by a hand verdict of N3_HAND. Returns (v0.2 equal, v0.1 unchanged, the corpus
    rows (key, ok), units read, hits (place, digest, kinds, verdict or None))."""
    raw_ = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + N3_V02[0]], capture_output=True).stdout
    v02_ = bool(raw_) and _hs.sha256(raw_).hexdigest()[:16] == N3_V02[1]
    v01_ = g(PP, 'diff', '--numstat', K.PRE_PP, 'HEAD', '--', N3_V01).strip() == '' and bool(_show(PP, 'HEAD', N3_V01))
    cut_ = lambda l_: [x_ for x_ in re.split(r'(?<=[.;?])\s+', (l_ or '').strip()) if x_.strip()]
    crows_ = []
    for r_ in (jl('%s_corpus.json' % ACT) or {}).get('rows') or []:
        t_ = (_show(PP, 'HEAD', r_.get('path') or '-') or '').replace(chr(13), '').split(NL)
        l_ = t_[r_['line'] - 1] if 0 < (r_.get('line') or 0) <= len(t_) else '\x00'
        crows_.append((r_.get('key'), r_.get('state') == 'RE-CUT' and _hs.sha256(l_.encode('utf-8')).hexdigest()[:16] == str(r_.get('after_sha') or '')[:16]))
    units_ = []
    for i_, l_ in enumerate(raw_.decode('utf-8', 'replace').replace(chr(13), '').split(NL), 1):
        units_ += [((N3_V02[0], i_), x_) for x_ in cut_(l_)]
    tx_ = rdn('%s_text.txt' % ACT).replace(chr(13), '').split(NL)
    for i_, l_ in enumerate(tx_):
        m_ = re.match(r'^@@ (C\w+) \| ', l_)
        nw_ = [x_ for x_ in tx_[i_ + 1:i_ + 6] if x_.startswith('NEW: ')][:1] if m_ else []
        if nw_:
            units_ += [(('data/%s_text.txt NEW' % ACT, m_.group(1)), x_) for x_ in cut_(nw_[0][5:])]
    for r_ in (jl('%s_notes.json' % ACT) or []) + (jl('%s_errata.json' % ACT) or []):
        t_ = (_show(PP, 'HEAD', r_.get('file') or '-') or '').replace(chr(13), '').split(NL)
        for x_ in r_.get('lines') or []:
            if 0 < (x_[0] or 0) <= len(t_):
                units_ += [((r_.get('file'), x_[0]), y_) for y_ in cut_(t_[x_[0] - 1])]
    hits_ = []
    for (p_, n_), x_ in units_:
        kinds_ = [k_ for k_, bad_ in (('centre', bool(re.search(N3_LOC, x_)) and not re.search(N3_NEG, x_)), ('catalogue', bool(re.search(N3_CAT, x_))),
                                      ('side', _side_bad(x_))) if bad_]
        if kinds_:
            d_ = _hs.sha256(x_.encode('utf-8')).hexdigest()[:16]
            hits_.append(('%s :%s' % (p_, n_), d_, '+'.join(kinds_), N3_HAND.get((p_, n_, d_))))
    return v02_, v01_, crows_, len(units_), hits_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R369): "v0.2 equals the text block with its fields filled from the banks and (6)'s outcome applied; each sentence replaced under
    (9) equals its NEW; each sentence of (5), (6), (8) and (9) entered in a ledger equals this ruling's text with its fields filled; no
    sentence of the act says that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; a sentence the act
    writes about a result at the control names the side, under (R368)(9); no sentence says the mechanism catalogue has or has not met the
    zero." Read: v0.2 at PLACE-papers HEAD by the composition's digest and v0.1 unchanged; each corpus line at HEAD by the digest the corpus
    bank wrote; the notes and errata banks' lines at HEAD, the sentences of (5) and (8) whole in FACES_LEDGER's and the census's; the four
    sentences whole in the entry, the FINDINGS ledger; no line of the papers of (8) and (10) removed since the act's base; the centre, side
    and catalogue matchers over the act's own sentences -- its banks', the entry's and its PLACE-papers writes' -- a PLACE-papers hit
    passing by a pinned hand verdict alone; each bank's foot carrying its grade; each matcher's control caught; the entry's last line the
    ferry's INTEGRATION line composed from the banks; the banks' nouns in the entry; the root prompt's sentences about the entry the
    composer's ((R369)(11), "composed from the banks"). The novelty and navigator-figure matchers printed with their yields and graded by
    no clause."""
    if rdn('%s_coeff.txt' % ACT, optional=True) and N3_GRADED_COEFF not in N3_GRADED:
        globals()['N3_GRADED'] = N3_GRADED + (N3_GRADED_COEFF,)   # ### (5)'s merge bank where (5) was begun
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b754: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    # ### N3 over the act's own sentences (the banks' quote rows and quoted spans dropped) and the entry's, each matcher with its control
    nsents_, navs_, nsides_ = [], [], []
    for b_ in N3_BANKS + N3_BANKS_OPTIONAL:
        t_ = rdn('%s_%s.txt' % (ACT, b_), optional=b_ in N3_BANKS_OPTIONAL) or ''
        nsents_ += _own_sentences(t_)
        nsides_ += _side_sentences(t_)   # ### (R368)(9): the lines headed by a dated record left out of the side matcher alone
        navs_ += _nav_units(t_)   # ### defect (w): the navigator's figures read with each table row whole
    neg_ = N3_NEG
    row_n_ = '  (7) navigator  AS THE NAVIGATOR READ IT: 250-550 lines and 4-8 dispatches; hours (x) | lines 250-550 | dispatches 4-8\n'
    row_x_ = '  (7) wide  THE WIDE DIRECTION: 250-550 lines and 4-8 dispatches; hours (x) | lines 250-550 | dispatches 4-8\n'
    ctl3_ = dict(lit=bool(re.search(N3_LIT, 'The join is a new result.', re.I)), loc=bool(re.search(N3_LOC, 'RH holds at every height.')),
                 loc_k=bool(re.search(N3_LOC, 'Weil positivity on classK holds.')), loc_e=not re.search(N3_LOC, 'The Epstein zeta function holds no zero there.'),
                 # ### b759: (5)'s ruled sentence, its head as the ruling writes it, passed; the same words for zeta caught
                 loc_w=not re.search(N3_LOC, 'Weil positivity on classK fails at the control on the arithmetic side of its explicit formula, in the form h2_sign has for zeta.')
                 and bool(re.search(N3_LOC, 'Weil positivity on classK fails for zeta, in the form h2_sign has.')),
                 # ### b759: the catalogue clause, either way caught, a negation not passing it; a sentence of the order left open passed
                 cat=bool(re.search(N3_CAT, 'The mechanism catalogue has met the zero.')) and bool(re.search(N3_CAT, 'The catalogue has not met the zero.'))
                 and not re.search(N3_CAT, 'The order stays open on the author`s word, T0 and T1 entered beside it.'),
                 loc_c=not re.search(N3_LOC, 'There is a test function in classK, and the direction that gives it holds for every configuration.'),
                 neg=bool(re.search(neg_, 'RH is not proved.')),
                 side=_side_bad('Weil positivity fails at the control.') and not _side_bad('Positivity of the arithmetic side fails at the control.'),
                 # ### (R368)(9), one control of each kind: a sentence the act writes about a result, caught; a line reporting a dated record in its
                 # ### own words under the record's head (b757's sweep bank :159's form), passed
                 side_result=any(_side_bad(x_) for x_ in _side_sentences('  THE LANDING: the control`s positivity fails at v0.40.\n')),
                 side_dated=not any(_side_bad(x_) for x_ in _side_sentences(
                     '  FINDINGS.md :12999 -- SAYS IT ; A DATED RECORD -- TAKES MOVED BY NO RULE -- hand-read: b736`s discharge: the control`s positivity '
                     'failure held numerically at b726`s two windows, stated by no declaration then; true of its act\n      sha256 92c4460ac53deb3b\n')),
                 quote=not any(re.search(N3_LIT, x_, re.I) for x_ in _own_sentences('  T9.a  X (:1): "Many zeros are listed here, as far as\n        we know, for the first time." The bank reads on.\n'))
                 and 'The bank reads on.' in ' '.join(_own_sentences('  T9.a  X (:1): "Many zeros are listed here, as far as\n        we know, for the first time." The bank reads on.\n')),
                 nav=_nav_bad('The wide direction took 250 to 550 lines.') and not _nav_bad('The navigator read 250 to 550 lines and 4 to 8 dispatches.')
                 and not _nav_bad('The wide direction took 1250 to 5500 lines.'),
                 nav_row=any(_nav_bad(x_) for x_ in _own_sentences(row_n_)) and not any(_nav_bad(x_) for x_ in _nav_units(row_n_))
                 and any(_nav_bad(x_) for x_ in _nav_units(row_x_)))
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    side_ = [x[:80] for x in sents + nsides_ if _side_bad(x)]   # ### (R368)(9): the banks' sentences with the dated records' lines left out
    cat_ = [x[:80] for x in sents + nsents_ if re.search(N3_CAT, x)]   # ### b759: the catalogue clause, a negation not passing it
    # ### the writes of (8) and (10) against the ruling's text; no line of a paper removed; the PLACE-papers writes; the navigator's figures
    notes_, removed_ = _notes_rows()
    v02_, v01_, crows_, ppn_, pph_ = _pp_n3()
    ppbad_ = [h_ for h_ in pph_ if not h_[3]]
    s5_, s8_ = _true_sentences()
    led_ = [(k_, bool(s_) and (s_ in text or conv(s_) in text)) for k_, s_ in (('(5)', (s5_ or [''])[0]), ('(6)', f['c6_sentence']), ('(8)', (s8_ or [''])[0]),
                                                                               ('(9)', f['c9_sentence']))]
    navfig_ = [x[:80] for x in navs_ + sents if _nav_bad(x)]
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    nouns_ = [w_ for w_ in ('v0.38', 'v0.39', 'v0.40', 'v0.41', 'v0.2.0', 'push-b759-weil', 'a3aad4cc', '390506fc', 'v1.36.3', 'v1.36.4', 'v1.36.5', 'v1.36.6',
                            'v1.36.7', 'data/%s_presend.txt' % ACT, 'data/%s_outcomes.txt' % ACT, 'data/%s_c3table.txt' % ACT, 'data/%s_costlaw.txt' % ACT,
                            'data/%s_fields.txt' % ACT, 'data/%s_compose.txt' % ACT, 'data/%s_notes.json' % ACT, 'data/%s_corpus.txt' % ACT,
                            'data/%s_errata.json' % ACT, 'data/%s_reproduce.txt' % ACT, 'data/%s_ceiling.txt' % ACT, 'data/%s_corrigendum.txt' % ACT,
                            'E-2026-11-17-1', 'E-2026-11-17-2', 'W-ORD-MECHANISM-ATTRIBUTION') if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    # ### b759: (R369)'s five clauses and the carried ones beside them; more_, first_ and navfig_ printed, graded by no clause of (R369)
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not loc_ and not side_ and not cat_ and len(notes_) == 5 \
        and all(o_ for _k, _n, o_ in notes_) and not removed_ and v02_ and v01_ and len(crows_) == 14 and all(o_ for _k, o_ in crows_) \
        and not ppbad_ and all(o_ for _k, o_ in led_) and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence and (7)`s classK sentence passed, (5)`s ruled sentence passed and its words for zeta caught, the catalogue clause caught either way and a sentence of the open order passed, a negation read, a sentence of positivity at the control naming no side caught and one naming the arithmetic side passed, a quotation wrapped over two lines dropped and the text after it kept, a navigator`s price caught where no navigator is named, passed where one is, and a longer number passed, a table row naming the navigator before its semicolon caught by the sentence cut and passed read whole, and a row naming none caught): %s; '
        'v0.2 at PLACE-papers HEAD by the composition`s digest %s (relay data/%s_compose.txt): %s; v0.1 unchanged since the act`s base: %s; the fourteen corpus lines at HEAD, each by the digest the corpus bank wrote and RE-CUT (relay data/%s_corpus.json): %d of %d; the sentences of (5), (6), (8) and (9) whole in the entry, the FINDINGS ledger: %s; '
        'each write of (8) and (10) at PLACE-papers HEAD, the notes bank`s lines equal and the errata bank`s by digest, FACES_LEDGER`s and the census`s carrying the sentences of (5) and (8), REGISTRY`s v0.41 and its closing sentence, ERRATA`s two entries and OPEN_TRAILS` six orders (relay data/%s_notes.json, data/%s_errata.json): %s, %d lines; the papers of (8) and (10) since the act`s base with a line removed: %s; '
        'over %d of the act`s own sentences in its banks and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation (graded by no clause of (R369)): %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant (graded by no clause of (R369)): %s; a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; a sentence about a result at the control speaking of positivity with no side named, the lines a dated record heads left out ((R368)(9)): %s; a sentence saying the mechanism catalogue has or has not met the zero: %s; '
        'over %d units of the act`s PLACE-papers writes (v0.2 line by line, the fourteen NEWs, the notes and errata lines), the hits of the three matchers by place and digest, the words not quoted: %s, passed by no hand verdict: %s; '
        'a sentence printing a navigator`s price with no navigator named (graded by no clause of (R369)): %s; the entry`s last line (R369)`s INTEGRATION line composed from the banks (%s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            N3_V02[1], ACT, v02_, v01_, ACT, sum(1 for _k, o_ in crows_ if o_), len(crows_), ', '.join('%s %s' % x_ for x_ in led_),
            ACT, ACT, ', '.join('(%s) %d %s' % x_ for x_ in notes_), sum(n_ for _k, n_, _o in notes_), removed_ or 'NONE',
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', side_ or 'NONE', cat_ or 'NONE',
            ppn_, '; '.join('%s %s %s%s' % (p_, d_, k_, (' HAND: %s' % v_) if v_ else '') for p_, d_, k_, v_ in pph_) or 'NONE', ppbad_ or 'NONE',
            navfig_ or 'NONE', il_, integ_, nouns_ or 'NONE', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R364) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R364)(5))
# ### (R364)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### v1.30.0, (R360)(3)(viii), b749 events (12): the lock's time printed from the one reader's epoch; b753's module left lock_iso unset and
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
    # ### (R364) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b753's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b754, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b753's face
# ### read them; (R364)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
# ### 14ca572, main unmoved, the tags containing v0.37 exactly v0.37 and v0.38, v0.38 peeling to 14ca5725
# ### b758, (R368)(4), (5), N5: SIDE-explicit-formula's main and tags against b757's face moved by the outcomes alone -- main at the last
# ### LANDED item's peel (8fbab45d where none landed), the tags b757's face read and each LANDED item's tag at its peel, no other; the tags
# ### containing v0.37 among v0.37, v0.38 and those; v0.38 peeling to 14ca5725
#⟪OVERRIDE record MARK 82a559f5c96c 2⟫
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    _land5 = [r_ for r_ in (json.loads(rdn('%s_outcomes.json' % ACT, optional=True) or '[]') or []) if str(r_.get('outcome') or '').startswith('LANDED') and r_.get('tag') and r_.get('peel')]   # ### b759: "LANDED, COMPILED"
    _new5 = dict((r_['tag'], r_['peel'][:7]) for r_ in _land5)
    _main5 = _land5[-1]['peel'] if _land5 else K.EF_BASE
    tag_one = _ef_now[0] == _main5[:7] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **_new5)
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main.startswith(_main5[:8]) and set(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) <= set(['v0.37', 'v0.38', 'v0.39', 'v0.40'] + list(_new5)) \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') and ch_ok \
        and bool(prev) and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main and tags against b758`s face moved by the outcome of (R369)(5) alone (main at the landed tag`s peel, 630cba16 where none landed; the landed tag v0.41 at its peel; v0.38, v0.39 and v0.40 as before; read in full in N5`s kernel clause below), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R369)(11), N5: "no kernel touched beyond SIDE-explicit-formula's tree and the five branches of (3)" -- every ref of every kernel
    # ### carrying a commit made after the act's opening commit is a fault but the act's own: in SIDE-explicit-formula a push-b759-* branch, its
    # ### main at the landed tag's peel and the landed tag; SIDE-dirichlet-mod-24 none (b758's (6)(i) exception for its local main not
    # ### carried); a listed branch of the face's list excepted as before; no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b756 found them; the address scan's count from its bank. The outcome's word opens LANDED (b759's tool
    # ### banks "LANDED, COMPILED")
    ocr5_ = json.loads(rdn('%s_outcomes.json' % ACT)) or []
    land5_ = [r_ for r_ in ocr5_ if str(r_.get('outcome') or '').startswith('LANDED')]
    main5_ = (land5_[-1].get('peel') if land5_ else K.EF_BASE) or ''
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R354)(2)(v): the face's branch list
    own_k_ = ('SIDE-explicit-formula',)
    lean_w, own_r = [], []
    kps_ = list(dict.fromkeys(list(K.KERNEL_PATHS) + [K.M24_DIR]))
    for kp in kps_:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                if kn in own_k_ and (r_[0].startswith('refs/heads/push-b759-')
                                     or (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/main' and bool(land5_) and r_[1].startswith(main5_[:8]))
                                     or (kn == 'SIDE-explicit-formula' and r_[0] in ['refs/tags/%s' % x_.get('tag') for x_ in land5_])):
                    own_r.append('%s %s %s' % (kn, r_[0][len('refs/heads/'):], r_[1][:8]))
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    own_r = sorted(set(own_r))
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### N5 (R369): "v0.38, v0.39, v0.40 and v0.2.0 peel as before at the close; v0.41's peel is read back equal to main".
    # ### SIDE-dirichlet-mod-24: v0.2.0 peeling to e5ebdd15 by its tag object, the local main there as b758 left it. SIDE-explicit-formula:
    # ### the tag the outcomes bank gives LANDED, its gated push's capture reading main back at the remote equal to the tag's commit and the
    # ### tag's peel local and remote equal to it, the commit the outcome's peel; the tags v0.39*, v0.40* and v0.41* v0.39 and v0.40 and those
    # ### landed, v0.39 at d1afb4fc and v0.40 at 630cba16; v0.38 at 14ca5725; the branch the act pushed read back at the remote in its capture
    m24_loc_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % K.M24_TAG[0]).strip()
    m24_main_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'main').strip()
    m24_ok = m24_loc_.startswith(K.M24_TAG[2]) and m24_main_ == m24_loc_ \
        and g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s' % K.M24_TAG[0]).strip().startswith(K.M24_TAG[1])
    br5_ = {'weil': K.WEIL_BRANCH[0]}
    efl_ = []
    for r_ in land5_:
        c_ = rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, br5_.get(r_.get('item'), '-')), optional=True) or ''
        rb_ = re.findall(r'(?m)^push_gated: main read back at the remote: ([0-9a-f]{40})$', c_)
        pl_ = re.findall(r'(?m)^push_gated: tag %s peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$' % re.escape(r_.get('tag') or '-'), c_)
        loc_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % (r_.get('tag') or '-')).strip()
        efl_.append((r_.get('tag'), loc_[:8] or 'NONE', bool(loc_) and loc_.startswith((r_.get('peel') or '-')[:8]) and rb_[-1:] == [loc_] and pl_[-1:] == [(loc_, loc_)]))
    ef_new_tags_ = sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--list', 'v0.39*', 'v0.40*', 'v0.41*').split() if t_.strip())
    v038_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip()
    v039_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.39^{commit}').strip()
    v040_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.40^{commit}').strip()
    pushed5_ = [(K.WEIL_BRANCH[0], K.WEIL_BRANCH[1])]
    ef_rb_ = [(b_, bool(re.search(r'(?m)^push_gated: branch %s read back at the remote: %s' % (re.escape(b_), t_ or '-'),
                                  rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, b_), optional=True) or ''))) for b_, t_ in pushed5_]
    efb_ok = ef_new_tags_ == sorted(['v0.39', 'v0.40'] + [t_ for t_, _l, _o in efl_]) and all(o_ for _t, _l, o_ in efl_) and v038_.startswith('14ca5725') \
        and v039_.startswith('d1afb4fc') and v040_.startswith('630cba16') and all(o_ for _b, o_ in ef_rb_)
    # ### N5: a repository edit read by the taught reader (tools/b757_ghcalls.py over this act's capture, unedited): no captured command runs
    # ### gh repo edit, and no tool the capture runs sends one ((R368) orders no description)
    gho_ = __import__('b758_ghcalls').over(ACT)
    ghr_ = (gho_ or {}).get('direct')
    ghs_ = (gho_ or {}).get('sends') or {}
    gh_ok = gho_ is not None and not ghr_ and not ghs_
    # ### v1.30.0, (R360)(3)(vi), b749 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R364)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and gh_ok and not zdel_ and m24_ok and efb_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b759_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel, the act`s own apart (a push-b759-* branch, main at the landed tag`s peel %s and the landed tag in SIDE-explicit-formula), or a .lean file in a kernel`s tree (%d kernels read): %s; the act`s own refs read: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; SIDE-dirichlet-mod-24`s tag %s peeling locally to %s, its local main %s: %s; SIDE-explicit-formula: the tags v0.39*, v0.40* and v0.41* %s, each landed tag at its outcome`s peel with main read back at the remote equal to it and its peel local and remote equal (%s), v0.38 at %s, v0.39 at %s, v0.40 at %s, the branch the act pushed read back at the remote in its capture %s: %s; '
            'gh repo edit run by a captured command (the carried reader): %s; gh repo edit sent from inside a tool, read by its rows bank (the taught reader, tools/b758_ghcalls.py): %s, none wanted: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (main5_[:8], len(kps_), lean_w or 'NONE', ', '.join(own_r) or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                K.M24_TAG[0], m24_loc_[:8] or 'NONE', m24_main_[:8] or 'NONE', m24_ok,
                ef_new_tags_ or 'NONE', '; '.join('%s at %s %s' % x_ for x_ in efl_) or 'none landed', v038_[:8] or 'NONE', v039_[:8] or 'NONE', v040_[:8] or 'NONE', ef_rb_, efb_ok,
                'UNREAD (no command bank)' if gho_ is None else (ghr_ or 'NONE'), '; '.join('tools/%s.py %s' % (s_, v_) for s_, v_ in ghs_.items()) or ('UNREAD (no command bank)' if gho_ is None else 'NONE'), gh_ok,   # ### defect (x): NONE printed unread
                ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b759, before the lock: the ruling's ordinal and title (the ferry's ACT line, data/b759_ferry.txt :39) adjusted to what the act did
    # ### (data/b759_outcomes.txt: LANDED, COMPILED; data/b759_c3table.txt: REPRODUCED; data/b759_compose.txt: v0.2 COMPOSED;
    # ### data/b759_corpus.txt: RE-CUT 14 OF 14); the apostrophe typographic, (R368)(3)
    return ('### b759 — lane two, act one hundred and eighty-six, the Epstein document at v0.2 under (R369): b758 at its weight; a short corrigendum; '
            'four standing changes; one statement and four print lines landed at v0.41; the appendix’s table reproduced; the document entered; '
            'the corpus’s sentences re-cut')
#⟪END⟫
#⟪SECTION record 29⟫
# ### b756: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict
# ### b759, before the lock: the guard over (R369)(1)-(11)'s feet


def _guard(f):
    """the composer's refusals before any sentence, where the banks' feet disagree with one another (never on a verdict): the five standing
    versions in the worklist's order with the worklist's cases, each all as wanted; the pre-send reads' controls all as wanted; the dispatches
    by kernel within (R369)(5)'s and (11)'s caps (3 and 0), each dispatch read once, the controls bank's count the rows'; the ceiling's
    dispatches the rows'; the table's two routes each over the same cells; the fields' corpus route's N the corpus lines re-cut; the corpus's
    lines re-cut and left summing to its fourteen; (8)'s three notes and (10)'s two writes; the reproduction run's rows summing."""
    if [v_ for v_, _c, _n, _w in f['vers']] != [v_ for v_, _c, _b, _n in K.STANDING_BANKS] or any(n_ != w_ for _v, _c, n_, w_ in f['vers']) \
            or [n_ for _v, _c, n_, _w in f['vers']] != [n_ for _v, _c, _b, n_ in K.STANDING_BANKS] or len(f['vers']) != 5:
        sys.exit('### THE STANDING VERSIONS ARE NOT THE WORKLIST`S FIVE, EACH ALL AS WANTED -- NOTHING COMPOSED')
    if f['ps_ctl'][0] != f['ps_ctl'][1] or f['cc_ctl'][0] != f['cc_ctl'][1] or f['cb_ctl'][0] != f['cb_ctl'][1] or f['oc_ctl'][0] != f['oc_ctl'][1]:
        sys.exit('### A CONTROL OF THE PRE-SEND READS, THE CONTROLS TOOL OR THE OUTCOME IS NOT AS WANTED -- NOTHING COMPOSED')
    if f['disp_ef'] > K.MAX_DISPATCHES or f['disp_m24'] > K.MAX_DISPATCHES_M24 or f['disp_ef'] != f['read_ef'] or f['disp_m24'] != f['read_m24'] \
            or f['cb_kernel'] != f['read_ef'] + f['read_m24'] or f['oc_runs'] != f['read_ef']:
        sys.exit('### THE DISPATCH ROWS ARE OVER (5)`S CAPS, NOT EACH READ ONCE, OR NOT THE CONTROLS AND OUTCOME BANKS` COUNT -- NOTHING COMPOSED')
    if f['ce_disp'][0] > f['disp_ef'] + f['disp_m24'] or f['ce_disp'][1] != K.MAX_DISPATCHES:
        sys.exit('### THE CEILING`S DISPATCHES ARE NOT THE ROWS` -- NOTHING COMPOSED')
    if f['c3_one'][1] != f['c3_two'][1] or (f['c3_word'] == 'REPRODUCED') != (f['c3_one'][0] == f['c3_one'][1] == f['c3_two'][0] and f['c3_a'] == f['c3_b'] == 'HOLDS'):
        sys.exit('### THE TABLE`S ROUTES DISAGREE WITH ITS WORD -- NOTHING COMPOSED')
    if f['fc_n'] != f['cr_recut'] or f['cr_recut'] + f['cr_left'] != f['cr_of'] != 14 or f['cr_orders'] != f['cr_left']:
        sys.exit('### THE CORPUS LINES` COUNTS DISAGREE WITH THE FIELDS` N OR WITH THEIR FOURTEEN -- NOTHING COMPOSED')
    if f['notes_written'] != 3 or any(n_ < 1 for _k, _f, _c, n_ in f['notes']) or len(f['errata']) != 2:
        sys.exit('### THE NOTES OF (8) ARE NOT THREE WRITES AND THE WRITES OF (10) NOT TWO, EACH WITH LINES -- NOTHING COMPOSED')
    if f['rp_repro'] + f['rp_differs'] + f['rp_notrun'] != f['rp_rows'] or f['rp_ctl'][0] != f['rp_ctl'][1]:
        sys.exit('### THE REPRODUCTION RUN`S ROWS DO NOT SUM -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects (the ferry's ACT line, data/b759_ferry.txt :39, adjusted to what the act did): b758's close at its
    weight (b759_corrigendum); the four standing changes (b759_standing_v1363 to b759_standing_v1366); the statement and the four print lines
    (b759_presend, b759_outcomes); the table of Appendix A (b759_c3table); the fields (b759_fields); the document and its notes (b759_compose,
    b759_notes); the corpus lines (b759_corpus); the dispatches (b759_dispatch_rows). Each object's name in the heading, for the line reader;
    every figure from the banks' feet, in digits; the apostrophe typographic and no backtick, (R368)(3)'s rule, which tools/standing/titlerule.py
    refuses at the landing."""
#⟪END⟫
#⟪SECTION record 31⟫
    _guard(f)
    w_ = f['oc']['weil']
    sw_ = ('the statement and four print lines landed at %s = %s' % (w_['tag'], w_['peel'])) if f['weil_word'] == 'LANDED, COMPILED' else (
        ('four print lines landed at %s = %s, the statement not compiled' % (w_['tag'], w_['peel'])) if f['weil_word'].startswith('LANDED') else 'nothing landed in SIDE-explicit-formula')
    return ('## The Epstein document at v0.2 under (R369): b758’s close %s (b759_corrigendum); four standing changes, %d of 4 (b759_standing_v1363 to b759_standing_v1366); '
            '%s (b759_presend, b759_outcomes); the table of Appendix A %s, %d of %d cells by each route (b759_c3table); %d fields filled (b759_fields); '
            'the document %s, %d lines (b759_compose, b759_notes); %d of 14 corpus lines re-cut (b759_corpus); %d dispatch%s (b759_dispatch_rows)' % (
                f['close_word'], f['changes'], sw_, f['table_word'], f['c3_one'][0], f['c3_one'][1], f['fd_filled'] + 2 * (f['fc_word'] == 'FILLED'),
                f['doc_word'], f['cp_lines'], f['cr_recut'], f['disp_ef'] + f['disp_m24'], '' if f['disp_ef'] + f['disp_m24'] == 1 else 'es'))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    # ### b759: the seat's read of what (R369) misses (data/b759_misses.txt :3-:11, its second printing :25-:32), each item with what the act
    # ### found at it, and the act's own
    return ('(1) (7)`s cite of data/b744_zetabox_plan.txt :134 for 1.2972e11, which stands at :135, F1 reading :135`s figure, %s against the quotient %s (relay data/b759_misses.txt :3, data/b759_costlaw.txt); '
            '(2) (2)`s commit of tools/mirror_prevbuild.json, its working copy differing from HEAD`s blob by carriage returns alone, nothing carried (relay data/b759_misses.txt :4-:5, data/b759_events.txt (5)); '
            '(3) h2_sign_iff_rh among (5)`s print lines, compiled at FINDINGS :901 and :4595, the act writing its axioms line alone (relay data/b759_misses.txt :6-:7); '
            '(4) (5)`s one step read with Complex.zero_re beside Complex.le_def, the theorem opening ComplexOrder for itself alone (relay data/b759_misses.txt :8-:9, data/b759_presend.txt); '
            '(5) the clones’ local branches of (3)`s five names, none removed in a clone (relay data/b759_misses.txt :10-:11); '
            '(6) the kernel route, v1.36.7, a standing change (4) does not name, counted apart from its four (relay data/b759_misses.txt :27, data/b759_standing_v1367.txt); '
            '(7) (4)(iv)`s reader made on checks.tpl :663, not :611 (relay data/b759_misses.txt :28, data/b759_standing_v1366.txt); '
            '(8) the text block`s AX legend "std 3" where (7) writes "the standard three", the fields carrying (7)`s words (relay data/b759_misses.txt :29); '
            '(9) section 7`s three cites of the zeta-box plan corrected by the composer to their figures’ lines and one listed (relay data/b759_misses.txt :30, data/b759_compose.txt); '
            '(10) v0.2 :44`s cite of the document`s own v0.1 :31 listed and left as v0.1 wrote it (relay data/b759_misses.txt :31); '
            '(11) FACES_LEDGER`s note written as an UPDATE section in b758`s form at :565 (relay data/b759_misses.txt :32, data/b759_notes.json); '
            '(12) %s and the seat’s %s defect%s as lettered' % (f['cl_f1'], f['cl_quot'],
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b754: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
        # ### b754, defect (d''): a letter with any number of primes, as (R364)(3)(viii) set for the standing readers (counter.py, record.tpl`s
        # ### _counter); the carried `[a-z]'?` dropped (a''), (b'') and (c'') and printed REPEAT 72 of 107 beside CLOSE 110
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'*|\d+)\) ", l)]
    return sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l)), len(rows)


def _runs3(act=ACT):
    """v9 row (83): "a class that repeats in three acts running is the next act's opening component" -- each row of the act's defects bank
    tagged REPEAT <the previous act> (<letter>) whose row in the previous act's defects bank is itself tagged REPEAT <the act before> (...):
    a list of (this act's letter, 'b<n-2> (x) -> b<n-1> (y) -> b<n> (z)'). A REPEAT naming an older act, a class, or no letter, is not a run
    of three."""
    n = int(act[1:])
    p1, p2 = 'b%d' % (n - 1), 'b%d' % (n - 2)
    tag = re.compile(r"^    \(([a-z]'*)\) THE (?:SEAT|NAVIGATOR)'S \[(?:CLAIM|CLOSE) ; REPEAT (b\d+) \(([a-z]'*)\)\]")   # ### b754, defect (d''): any number of primes; the carried `'?` missed (a'') -> b753 (b) -> b752 (b)
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R369)(8)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b759's objects; b758's composer in git at
    b758's record tool). Its last line (R369)'s INTEGRATION line, composed from the banks' feet (_integ_line)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    # ### b758 touch read: the comparative read's own line in the citation bank (banks, words, rows), cited by its line; step zero records none
    cl_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    sc_ = dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)   # ### version -> its commit
    sv_ = dict((x_[0], (x_[2], x_[3])) for x_ in f['vers'])   # ### version -> (cases, as wanted)
    vw_ = lambda v_: '%s at relay %s, controls %d of %d' % (v_, sc_[v_][:8], sv_[v_][1], sv_[v_][0])   # ### a standing version as the entry names it
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)   # ### the order line's commits by key, PLACE-papers and relay (the worklist's chains)
    w5_ = f['oc']['weil']
    nl_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_ in f['notes'])
    el_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_, _x in f['errata'])
    true5_ = [s_ for s_ in (w5_['sentence'], f['c6_sentence'], f['c8_sentence'], f['c9_sentence']) if s_]
    lp5_ = ('Main moved to the tip %s by the gated push`s default mode after the run`s success, v0.41 cut at main`s read-back (tag object %s) and its peel read back at '
            'the remote equal to main (relay data/b759_SIDE-explicit-formula_push-b759-weil_push_out.txt); the kernel`s local main fast-forwarded to it by the one-call tool, '
            'read back equal.' % (w5_['peel'], w5_['tag_object'])) if f['weil_word'].startswith('LANDED') else 'Main stands at %s, no tag cut.' % K.EF_BASE[:8]
    e = ['', _title(), '',
         ' '.join(true5_) + (
             ' Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from them (relay data/b759_outcomes.txt, data/b759_c3table.txt, '
             'data/b759_compose.txt, data/b759_corpus.txt); every build a runner dispatch read by its run id, %d in SIDE-explicit-formula of the 3 (5) allows and '
             'none elsewhere (relay data/b759_dispatch_rows.json); no lean process on this host.' % f['disp_ef']), '',
         '*Filed at b759 on the author’s ruling `(R369)`; %d question%s put before the root%s. Banks: relay '
         '`data/b759_misses.txt`, `data/b759_corrigendum.txt`, `data/b759_standing_v1363.txt` to `data/b759_standing_v1367.txt`, `data/b759_presend.txt`, '
         '`data/b759_controls_control.txt`, `data/b759_controls.txt`, `data/b759_dispatch_rows.json`, `data/b759_outcomes.txt`, the gated push`s capture '
         '`data/b759_SIDE-explicit-formula_push-b759-weil_push_out.txt`, `data/b759_c3table.txt`, `data/b759_costlaw.txt`, `data/b759_fields.txt`, '
         '`data/b759_fields_corpus.txt`, `data/b759_compose.txt`, `data/b759_notes.json`, `data/b759_corpus.txt`, `data/b759_errata.json`, `data/b759_reproduce.txt`, '
         '`data/b759_ceiling.txt`, `data/b759_author_answers.txt`, `data/b759_events.txt`, `data/b759_defects.txt`, `data/b759_prelock.txt`, `data/b759_pathrefusal.txt`, '
         '`data/b759_address_scan.txt`, `data/b759_touch.txt`, `data/b759_standing_figures.txt`, `data/b759_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b758 at its weight and the corrigendum** ((R369)(1)): b758 closed at relay c25f8b53 and PLACE-papers 4ea41948, its scores %d of 8 HELD (%s), as its closing record`s head line gives it (relay data/b758_closing.txt, data/b758_scores_close.json); N4 stays REFUTED on the plant`s repair after its lock and is not argued. '
         'The corrigendum of b758’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- no CLAIM item among them; '
         'what the seat found after b758`s lock entered as this act`s events (17) to (21) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b759_corrigendum.txt, route %s, banks %s; PLACE-papers %s). The version at the close %s.' % (
             f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted',
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'],
             f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], f['corr_line'], f['corr_row'], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['ver']), '',
         '**The four standing changes** ((R369)(4)), each a commit of its own moving VERSION, its planted controls printed before its use: (i) the route that removes a named branch at a kernel`s remote, refused for main, for a kept name and for a tip that is no ancestor of the remote`s main, read back absent, %s (relay data/b759_standing_v1363.txt); '
         '(ii) the plant of G-DELETES-ONE-BRANCH reading kept each clause that covers a named ref, (R368) replayed with its clauses (2) and (5) both read, %s (relay data/b759_standing_v1364.txt); '
         '(iii) the row writer taking the phase repair, b758`s repair commit f401a81e replayed, %s (relay data/b759_standing_v1365.txt); '
         '(iv) the suite`s reader of the kernels face naming SIDE-dirichlet-mod-24, made on checks.tpl :663 where the ruling named :611, b758`s face read as 24 kernels, %s (relay data/b759_standing_v1366.txt). '
         'The changes: %d of 4. The kernel route, the one-call tool opened for this act in SIDE-explicit-formula before its first kernel write, a standing change (4) does not name, %s, counted apart (relay data/b759_standing_v1367.txt). '
         'The branches of (3): at the relay and PLACE-papers the five push-b758-* branches by the tool`s route after the merged listing; at the kernels’ remotes %s, each by (i)`s route after its controls, each an ancestor of its remote`s main; each read absent after, one a message (relay data/b759_stepzero.txt, data/b759_events.txt (13), (24)); no clone`s branch removed; push-b759-weil kept for the next act`s step zero.' % (
             vw_('v1.36.3'), vw_('v1.36.4'), vw_('v1.36.5'), vw_('v1.36.6'), f['changes'], vw_('v1.36.7'), ', '.join('%s (was %s)' % (b_, t_[:8]) for b_, t_ in K.KERNEL_DELETES)), '',
         '**The statement and the print lines** ((R369)(5)): push-b759-weil made at main %s; commit one %s, the four lines rQ_one, cQ_eq, detector and h2_sign_iff_rh after print_targets.txt :484, none of them there before; commit two %s, zq_weil_positivity_fails with its docstring in Schema/Wide/HalfScaleControl.lean :37-:51 after zq_arith_side_re_neg, no line above it moved, ComplexOrder opened for it alone, and its line at print_targets.txt :489. '
         'The salt check printed before the send, h2_sign`s body taken into the control`s names under a negation equal to the statement, no binder before its colon: %s; the pre-send reads at %s: duplicates %d; refused by the filter %d (%s), the two known; anonymous pairs %d of %d (%d unread); %d modules for %d names, %d refused; controls %d of %d (relay data/b759_presend.txt). '
         'The dispatch and the read by tools/b759_controls.py, carried from b758`s and set for this act`s one item and its cap, committed before its opening dispatch, its own controls %d of %d (relay data/b759_controls_control.txt); dispatch 1 of 3 at the branch`s tip, run %s: the exit file 0, 0 error lines, %s axioms lines each within the standard three, the five new names among them, no line naming sorryAx (relay data/b759_controls.txt, data/b759_outcomes.txt). '
         'The grade read against the clause from the compiled statement before it was written anywhere: %s, binding no premise. %s' % (
             K.EF_BASE[:8], K.KERNEL_COMMITS[0][2][:8], K.KERNEL_COMMITS[1][2][:8], f['ps_salt'].lower(), f['ps_rev'], f['ps_dup'], f['ps_refused'], f['ps_refused_lines'],
             f['ps_anon'][0], f['ps_anon'][1], f['ps_anon'][2], f['ps_modules'], f['ps_names'], f['ps_names_refused'], f['ps_ctl'][0], f['ps_ctl'][1],
             f['cc_ctl'][0], f['cc_ctl'][1], w5_['run'], w5_['axiom_lines'], w5_['grade'], lp5_), '',
         '**The table of Appendix A** ((R369)(6)), a reproduction and no registered prediction, by tools/b759_c3table.py committed before its run: the plant printed first, the wanted table with beta at (3,2) read -2 reported unequal by each route at that cell and no other, %s; route one, the group-ring model of INSTRUMENTS I-105, %d of %d cells agreeing; route two, the form`s own count at -23 by the recursion of tools/b750_cq_sign.py, the primes 2, 3, 13 and 29 read as wanted and b(n) = c(n)/log n exact at each instance, %d of %d; route three, (a) the closed form of Step 4 for e from 1 to 24, %s, and (b) over every pattern of at most 8 prime factors counted with multiplicity, beta negative at none of the patterns containing none of (4,1), (3,2), (2,1,1) and (1,1,1,1), %s: %s, the law entering as %s (relay data/b759_c3table.txt).' % (
             f['c3_plant'].lower(), f['c3_one'][0], f['c3_one'][1], f['c3_two'][0], f['c3_two'][1], f['c3_a'].lower(), f['c3_b'].lower(), f['c3_word'], f['law_word']), '',
         '**The fields** ((R369)(7)), filled by tools/b759_fields.py from the banks and from no recall: %d filled, then N and DEPOSITS by its corpus route after (9), N %d and DEPOSITS %s; the pin %s, read equal to the run`s built ref; %d AX cells, each the axioms line of its name from the run that printed it, units24_iso_signs from b757`s; BLOCK F`s texts by (5)`s outcome and the law and the appendix by (6)`s; the six module md5s at 14ca5725 agreeing with data/b742_offlinezero.txt :68; HISTORY, v0.1 :3-:19 byte for byte; controls %d of %d and the route`s %d of %d (relay data/b759_fields.txt, data/b759_fields_corpus.txt). '
         'F1 and F2 by tools/b759_costlaw.py committed before its run: F1 = %s beside the quotient of the two banked figures, %s, %s, the sentence %s, its first figure read at data/b744_zetabox_plan.txt :135 where (7) cites :134; F2 = %s, INSTRUMENTS :556 carrying both heights; controls %d of %d (relay data/b759_costlaw.txt).' % (
             f['fd_filled'], f['fc_n'], f['fc_word'].lower(), f['fd_pin'], f['fd_ax'], f['fd_ctl'][0], f['fd_ctl'][1], f['fc_ctl'][0], f['fc_ctl'][1],
             f['cl_f1'], f['cl_quot'], f['cl_agree'].lower(), f['cl_word'].lower(), f['cl_f2'], f['cl_ctl'][0], f['cl_ctl'][1]), '',
         '**The document** ((R369)(8)): phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md composed by tools/b759_compose.py, committed before its run, beside v0.1, which is not edited: %d lines; BLOCK B %d of %d, each OLD once in v0.1 at its line; %d cites read, %d corrected where the name or figure stands once, %d listed where it does not; section 9.9 %s; brackets left %d; the banned stems %s; v0.1 %s, its sha256 equal before and after; controls %d of %d (relay data/b759_compose.txt); one PLACE-papers commit, %s. '
         'Written where else it is by tools/b759_notes.py, each note read back equal and committed alone: %s (relay data/b759_notes.json) -- REGISTRY`s row %s at :%s after 1.5c-23, its status "REVIEW; entered at v0.2 by b759; not deposited", no cell blank and no grade conferred, and a dated note at the file`s end giving v0.41 with its tag object and peel and closing "The tags confer no deposit."; FACES_LEDGER`s and the census`s each made of the document`s own dated head and the sentences of (5) and (8) that came true.' % (
             f['cp_lines'], f['cp_b'][0], f['cp_b'][1], f['cp_cites'], f['cp_corrected'], f['cp_listed'], f['cp_99'].lower(), f['cp_left'], f['cp_stems'].lower(), f['cp_v01'].lower(),
             f['cp_ctl'][0], f['cp_ctl'][1], K.C3_DOC_PP[1][:8], nl_, f['notes_reg'].get('id', '-'), f['notes_reg'].get('row_line', '-')), '',
         '**The corpus lines** ((R369)(9)): the hold on a paper`s sentences lifted for the fourteen lines of BLOCK D alone; each OLD read once at its line and replaced by its NEW by tools/b759_corpus.py, committed before its run, one PLACE-papers commit a document through the one-call tool, each confirmed at HEAD: %s; re-cut %d of %d, left %d, orders %d; REGISTRY`s deposit pins read for the nine documents, one deposited copy, A Place to Stand at REGISTRY :83, not read and not touched, C4 and C5 standing there as deposited; controls %d of %d (relay data/b759_corpus.txt, data/b759_corpus.json).' % (
             '; '.join('%s at %s' % (p_, c_) for p_, c_ in f['corpus_docs']), f['cr_recut'], f['cr_of'], f['cr_left'], f['cr_orders'], f['cr_ctl'][0], f['cr_ctl'][1]), '',
         '**ERRATA and the orders** ((R369)(10)), by tools/b759_errata.py committed before its run, each write read back equal and committed alone: %s (relay data/b759_errata.json) -- ERRATA`s entries %s at the file`s end in the form of E-2026-11-09-1, E-2026-11-06-1 not edited; OPEN_TRAILS’ block under one dated head after b758`s trail, no line moving: b758`s root answer; W-ORD-MECHANISM-ATTRIBUTION`s condition as the navigator read it, not met, T0 and T1 entered beside it and the order left open on the author`s word; the five orders W-ORD-WSC-KERNEL-CITES, W-ORD-LI-INDEX, W-ORD-CAPACITY-ATTRIBUTION, W-ORD-BIBLIOGRAPHY-LINK and W-ORD-EPSTEIN-SECTIONS-3-4 entered by name, each priced by no build; no order of a re-cut left, (9) leaving no line.' % (
             el_, ', '.join(((dict((r_[0], r_[4]) for r_ in f['errata']).get('errata')) or {}).get('entries') or [])), '',
         '**The research instruments reproduced** ((R369)(11), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (I-56, I-57, I-61 and I-107, as at b755), the planted controls %d of %d as wanted, %d s (relay data/b759_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The ceiling** ((R369)(2)): %d reading%s against 16 hours from the delivery, each before the work of a component began, the last at %s, %s h, %s, dispatches %d of %d (relay data/b759_ceiling.txt). The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b759_misses.txt).' % (
             f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower(), f['ce_disp'][0], f['ce_disp'][1]), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b759_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; each standing change a commit of its own moving VERSION with its controls bank, before its use; each act tool committed before it ran; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after its run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b759_prelock.txt, data/b759_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero'))), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula`s tree and the five branches of (3); no push forced; no tag moved, v0.38, v0.39, v0.40 and v0.2.0 among them; no toolchain or Mathlib pin moved; no sentence of any paper edited beyond (8)`s new file and (9)`s fourteen lines, v0.1 byte-equal before and after; no ledger row edited; no lean process on this host; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b759_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b759_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b759 -- %s, %s, %s, %s -- against b758’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b759_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b759_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the control now stands in one document read from its coefficients and from its zeros -- on its arithmetic side the failure of positivity compiled at v0.41 beside the statement it negates, the coefficient law at class number 3 by written proof with its table reproduced by two routes, and the corpus`s sentences about it re-cut to what is proved, compiled and observed; each is a statement about the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R369)(11), as the author answers the one question at the root: the same re-cut, map before write, for the keystone the author names, Which Structure Confines standing nearest with three of this act`s orders on it; or the class-number-3 law priced for a kernel; or W-ORD-BIBLIOGRAPHY-LINK; or another the author names. W-ORD-MECHANISM-ATTRIBUTION and the five orders of (10) open; push-b759-weil kept; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b758_body():
    """b755's paragraphs over b755's objects, kept for the record and not called (b756, Component 6): held as text, their names b755's
    locals, which the gate's report dry (tools/standing/reportdry.py unbound) read as live unbound globals beside _finding_text's own (defect (j))."""
    return r"""
    e = [
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b759_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b759_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b759_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b759_zeros_from_primes_59.txt, data/b759_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b759 on the author’s ruling `(R369)` and its two amendment rows (relay data/b759_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b759_corrigendum.txt`, `data/b759_carried_faults.txt`, `data/b759_standing_v1346.txt`, `data/b759_walk.txt`, `data/b759_coeffs_controls.json`, `data/b759_literature.txt`, '
         '`data/b759_cand_a.txt` to `data/b759_cand_l_plant.txt`, `data/b759_candidates.txt`, `data/b759_ceiling.txt`, `data/b759_registrations.txt`, `data/b759_roots_59.txt`, '
         '`data/b759_list_59.txt`, `data/b759_list_59_controls.txt`, `data/b759_zeros_from_primes_59.txt`, `data/b759_recur_59.txt`, `data/b759_recur_control.txt`, '
         '`data/b759_census_from_primes.txt`, `data/b759_l16.json`, `data/b759_put_1.json`, `data/b759_put_2.json`, `data/b759_author_answers.txt`, `data/b759_events.txt`, '
         '`data/b759_defects.txt`, `data/b759_prelock.txt`, `data/b759_pathrefusal.txt`, `data/b759_reproduce.txt`, `data/b759_address_scan.txt`, `data/b759_touch.txt`, '
         '`data/b759_standing_figures.txt`, `data/b759_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R369)(1), (2); relay %s, %s, PLACE-papers %s): b758 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b758’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b759_corrigendum.txt). Its three repairs: the lock gate carried as tools/b759_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b759_standing_v1346.txt; the amendment row 1). '
         'The open items of b758`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b759_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R369)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b759_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b759_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b759_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b759_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R369)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b759_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b759_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R369)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b759_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes’ phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b759_candidates.txt, data/b759_cand_a.txt to data/b759_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R369)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b759_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b759_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b759_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b759_zeros_from_primes_59.txt, data/b759_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b759_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b759_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R369)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b759_defects.txt (l)); its generator committed at relay %s before its run (relay data/b759_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R369)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b759_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R369)(8)): the price table at step zero from banked timings where a bank held one (relay data/b759_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b759_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b759_stepzero.txt); step zero from %s (data/act_current.json) through b758`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]’s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b759_prelock.txt, data/b759_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b759_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b759_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b759_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b758: [U3] in force, the counter's line as it prints (its event in data/b758_events.txt (22))
         '**The standing arms**: the four figures at b759 -- %s, %s, %s, %s -- against b758’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b759_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b759_citation_check.txt, data/b759_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R369)(8), as the author answers the one question at the root: the clearing act as b759 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]’s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b759 with the clearing act after it; defects (b), (e) and the tools’ (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)
"""


def _finding_text_b758():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b759's objects): the ledger writes; b758 at its weight; the standing changes and the branches of (3); the
    outcome of (5); the dispatches; the table, the fields, the document, the corpus lines and the errata of (6) to (10); the reproduction
    run; the ceiling; the open-orders line from tools/standing/orders.py's output over the trail at HEAD; the standing versions; the kernels."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    _r, _n, sh = seal_hashes()
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    # ### the open orders read through the orders tool with the trail at HEAD, (9)'s block among them (no status line written by this record)
    w5_ = f['oc']['weil']
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    nl_ = '; '.join('%s at %s' % (f_, c_[:8]) for _k, f_, c_, _n in f['notes'])
    el_ = '; '.join('%s at %s' % (f_, c_[:8]) for _k, f_, c_, _n, _x in f['errata'])
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R369) ratified.** Its components as the ferry orders them (relay data/b759_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b758), :%s (the entry); phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md at %s, v0.1 beside it unchanged; (8)`s notes, %s; (9)`s fourteen lines in nine documents; (10)`s writes, %s, OPEN_TRAILS.md`s block under one dated head; this record.' % (
                 f['corr_line'], fj.get('entry_line'), K.C3_DOC_PP[1][:8], nl_, el_), '',
             '**b758 at its weight** ((R369)(1)): closed at relay c25f8b53 and PLACE-papers 4ea41948, the scores %d of 8 HELD (%s), N4 not argued; the corrigendum short, no CLAIM item, no weight line (relay data/b758_scores_close.json, data/b759_corrigendum.txt).' % (
                 f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted'), '',
             '**The standing changes** ((R369)(4)): %d of 4, v1.36.3 to v1.36.6, each with its controls before its use; the kernel route v1.36.7 counted apart; the branches of (3) removed, five at the relay and PLACE-papers and %s at the kernels’ remotes (relay data/b759_standing_v1363.txt to data/b759_standing_v1367.txt).' % (
                 f['changes'], ', '.join(b_ for b_, _t in K.KERNEL_DELETES)), '',
             '**The statement and the print lines** ((R369)(5)): %s, run %s%s, the grade %s; the salt check %s (relay data/b759_presend.txt, data/b759_outcomes.txt).' % (
                 f['weil_word'].lower(), w5_['run'], (', %s = %s' % (w5_['tag'], w5_['peel'])) if f['weil_word'].startswith('LANDED') else '', w5_['grade'], f['ps_salt'].lower()), '',
             '**The dispatches:** SIDE-explicit-formula %d of the 3 (5) allows, none elsewhere, each read by its run id, the exit file governing (relay data/b759_dispatch_rows.json).' % (
                 f['disp_ef']), '',
             '**The table, the fields and the document** ((R369)(6)-(8)): the table %s, %d of %d by each route, the plant %s, the law %s; %d fields filled and N and DEPOSITS by the corpus route, F1 %s, F2 %s; v0.2 %d lines, %d fields left, v0.1 %s (relay data/b759_c3table.txt, data/b759_fields.txt, data/b759_compose.txt).' % (
                 f['table_word'], f['c3_one'][0], f['c3_one'][1], f['c3_plant'].lower(), f['law_word'], f['fd_filled'], f['cl_f1'], f['cl_f2'], f['cp_lines'], f['cp_left'], f['cp_v01'].lower()), '',
             '**The corpus lines and the errata** ((R369)(9), (10)): %d of 14 re-cut, %d left, %d orders, one deposited copy not touched; ERRATA`s two entries and OPEN_TRAILS’ block, W-ORD-MECHANISM-ATTRIBUTION left open and five orders entered (relay data/b759_corpus.txt, data/b759_errata.json).' % (
                 f['cr_recut'], f['cr_left'], f['cr_orders']), '',
             '**The reproduction run** ((R369)(11)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b759_reproduce.txt).' % (
                 f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
             '**The ceiling:** %d reading%s, the last at %s, %s h of 16, %s (relay data/b759_ceiling.txt).' % (f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower()), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s (relay data/b759_standing_v1363.txt to data/b759_standing_v1367.txt); %s.' % (
                 '; '.join('%s %d of %d' % (v_, w_, n_) for v_, _c, n_, w_ in f['vers']),
                 ('HANDOFF.md regenerated once by tools/standing/handoff.py before the gate, at relay %s' % K.HANDOFF_COMMIT[:8]) if K.HANDOFF_COMMIT else
                 'HANDOFF.md not regenerated: tools/standing/handoff.py refused the page, three needles not found -- REGISTRY :373 no heading after the row of (R369)(8) at :180, b759’s ferry no line opening its holds clause, b758’s ferry no THE ACT’S PLACE -- and the page stands at b758’s (relay data/b759_handoff_halt.txt)'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b759_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b759_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b759 `%s` (previous `%s`, b758’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b759_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b759_standing_v1367.txt); the standing '
             'report tool (relay data/b759_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    lt5_ = [w5_] if f['weil_word'].startswith('LANDED') else []
    rows_ += ['**The kernels:** SIDE-explicit-formula`s main at %s (entering at %s), %s; %s at %s, kept; v0.38, v0.39 and v0.40 unmoved; zq-b730 at %s, unmoved; the branches of (3) removed at the remotes, %s; SIDE-dirichlet-mod-24`s main at %s, %s at %s; no kernel beyond SIDE-explicit-formula`s tree and the five branches of (3) touched; the %s branches as b759 found them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  (lt5_[-1]['peel'] if lt5_ else K.EF_BASE[:8]), K.EF_BASE[:8], ', '.join('%s at %s' % (x_['tag'], x_['peel']) for x_ in lt5_) or 'no tag cut', K.WEIL_BRANCH[0], K.WEIL_BRANCH[1][:8],
                  K.ZQ_TIP[:8], ', '.join(b_ for b_, _t in K.KERNEL_DELETES), K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root with the two ledgers’ cuts beside it (the ferry`s Component 5), HANDOFF.md among its files, its file named in the closing by its name, bytes and hash and its folder by role (relay data/b759_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b758’s %s, %s, %s, %s (relay data/b759_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b759_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b758():
    """b753's trail record over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: at most 3 in SIDE-explicit-formula and none in SIDE-dirichlet-mod-24 ((R369)(5), (11)); MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: every run read by its id from its artifact, the exit file governing (data/b759_dispatch_rows.json); MEASURED off the worklist`s EF_RUNS and M24_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b759*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved, push-b759-weil made beside them; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('kernel branches removed at a kernel`s remote', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### (R369)(3): push-b757-join, push-b757-coeff, push-b758-land and push-b758-coeff at SIDE-explicit-formula and push-b757-mod24 at SIDE-dirichlet-mod-24, each by (4)(i)`s route after its controls, one per message, each an ancestor of its remote`s main, read absent; the four held branches of b725 to b730 kept.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b759 found them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b759*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act, the four unmoved; MEASURED off each branch against main.'),
    ('Lean files changed on SIDE-explicit-formula`s main', 'EFMAINLEAN', 'EFMAINLEAN', 'files', '### (R369)(5): Schema/Wide/HalfScaleControl.lean, zq_weil_positivity_fails after zq_arith_side_re_neg, main moved after the run`s success; SIDE-dirichlet-mod-24`s remote main unmoved; MEASURED off git diff --name-only from 630cba16 to main.'),
    ('tags cut at main`s read-back', 'EFTAGS', 'EFTAGS', 'tags', '### (R369)(5): v0.41 where the run succeeded, its peel read back at the remote equal to main; v0.38, v0.39, v0.40 and v0.2.0 unmoved; MEASURED off SIDE-explicit-formula`s tag v0.41.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b758-closing, push-b758-preroot, push-b758-record; PLACE-papers push-b758-preroot, push-b758-record; each by name, through the one-call tool, one per message, after the --merged listing and the citation check (data/b759_stepzero.txt :60-:65).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: (R369)(5), the workflow not widened for the two lines its filter refuses.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 1, 1, 'rows', '### (R369)(8): the row 1.5c-24 at :180 after 1.5c-23, its status "REVIEW; entered at v0.2 by b759; not deposited", no cell blank, no grade conferred, and one dated note at the file`s end (relay data/b759_notes.json).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none: (8)`s row inserted and its note appended, no line moving; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R369)(1): FINDINGS :15550 (relay data/b759_corrigendum.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R369)(1): row (79).'),
    ('ERRATA entries filed', 2, 2, 'entries', '### (R369)(10): E-2026-11-17-1 and E-2026-11-17-2 at the file`s end in the form of E-2026-11-09-1, E-2026-11-06-1 not edited (relay data/b759_errata.json).'),
    ('outcome sentences composed from the banks', 'OUTCOMES', 'OUTCOMES', 'sentences', '### (R369)(5): the ruling`s for the outcome its run read, its fields filled from the banks (relay data/b759_outcomes.txt); MEASURED off the outcomes bank`s rows read LANDED or BROKE.'),
    ('notes of (8) written, each by one PLACE-papers commit', 'NOTESN', 'NOTESN', 'notes', '### (R369)(8): REGISTRY`s row and note, FACES_LEDGER`s and the census`s notes, each read back against its bytes; MEASURED off relay data/b759_notes.json.'),
    ('corpus lines re-cut, one PLACE-papers commit a document', 'CORPUSN', 'CORPUSN', 'lines', '### (R369)(9): the fourteen lines of BLOCK D in nine documents, each OLD once at its line, each confirmed at HEAD; MEASURED off relay data/b759_corpus.txt`s foot.'),
    ('standing changes of (4) landed, each with its planted control', 4, 4, 'changes', '### (R369)(4)(i)-(iv): v1.36.3 to v1.36.6 (relay data/b759_standing_v1363.txt to data/b759_standing_v1366.txt); the kernel route v1.36.7 counted apart.'),
    ('orders entered with the trail', 5, 5, 'orders', '### (R369)(10): W-ORD-WSC-KERNEL-CITES, W-ORD-LI-INDEX, W-ORD-CAPACITY-ATTRIBUTION, W-ORD-BIBLIOGRAPHY-LINK and W-ORD-EPSTEIN-SECTIONS-3-4 in (10)`s block, each priced by no build; W-ORD-MECHANISM-ATTRIBUTION open beside them.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py`s full run at b759 as (R369)(11) orders it, in the foreground; MEASURED off data/b759_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### the tools` runs over the record and the runner`s prints, (6)`s route two at -23 and the reproduction run as (R369)(11) orders them: the five standing versions` controls, the pre-send reads, the controls tool`s controls and its run, the outcome, the table, the cost law, the fields, the document, the corpus lines, the reproduction, the ceiling, the probe-path refusal, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### none: (R369) registers no test, (6) a reproduction and no registered prediction, and no data/b759_registrations.txt is written; MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2): no registered object this act, nothing computed at any field; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: (5)`s two commits add no module; MEASURED off push-b759-weil against main 630cba16.'),
    ('Lean files edited by the act`s own commits', 'EFEDIT', 'EFEDIT', 'files', '### (R369)(5): Schema/Wide/HalfScaleControl.lean, one theorem with its docstring after zq_arith_side_re_neg, no line above it moved (a3aad4cc); commit one print_targets.txt alone; MEASURED off push-b759-weil against main 630cba16.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R369)(4) and the kernel route: tools/standing/ v1.36.3 to v1.36.7, each by a version commit of its own with its controls in its bank (data/b759_standing_v1363.txt to data/b759_standing_v1367.txt); MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b759_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, the dispatches and the artifact downloads, and the gh reads under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b759: no registered object and no figure bank ((R369) registers no test; (6) a reproduction)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    # ### b759 step zero: the runs' count read against (R369)(5) (SIDE-explicit-formula's alone, at most 3, M24_RUNS empty)
                    EFRUNS=len(K.EF_RUNS) + len(K.M24_RUNS),
                    # ### b759: main's Lean past the entering main, the tag of (5), the outcome rows ("LANDED, COMPILED" read by its head), the
                    # ### notes read back, the corpus lines re-cut, the OPEN_TRAILS block's lines
                    EFMAINLEAN=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, 'main').split() if f_.endswith('.lean')),
                    EFTAGS=sum(1 for t_ in ('v0.41',) if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/' + t_)),
                    OUTCOMES=jcount('b759_outcomes.json', lambda j: len([r_ for r_ in j if str(r_.get('outcome') or '').startswith(('LANDED', 'BROKE'))])),
                    NOTESN=jcount('b759_notes.json', lambda j: len([r_ for r_ in j if r_.get('read_back') is True])),
                    CORPUSN=tfirst('b759_corpus.txt', r'\*\*RE-CUT (\d+) OF 14 ;'),
                    EFMAINCOMMITS=int(_git(K.EF_DIR, 'rev-list', '--count', '%s..main' % K.EF_BASE) or 0),
                    OTBLOCK=jcount('b759_errata.json', lambda j: len(([r_ for r_ in j if r_.get('item') == 'trails'] or [{}])[0].get('lines') or [])),
                    REPROWS=jcount('b759_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b759_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    # ### b759: the modules (5)'s branch adds past main 630cba16, and the Lean files its commits edit ((R369)(5))
                    EFNEW=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=A', K.EF_BASE, K.WEIL_BRANCH[1]).split() if f_.endswith('.lean')),
                    EFEDIT=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=M', K.EF_BASE, K.WEIL_BRANCH[1]).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1363', 'standing_v1364', 'standing_v1365', 'standing_v1366', 'standing_v1367',
                                               'presend', 'controls_control', 'controls', 'outcomes', 'c3table', 'costlaw', 'fields', 'fields_corpus', 'compose',
                                               'corpus', 'reproduce', 'ceiling', 'pathrefusal', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b759_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b759_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFEDIT', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE', 'EFMAINLEAN', 'EFTAGS', 'OUTCOMES', 'NOTESN', 'CORPUSN', 'EFMAINCOMMITS', 'OTBLOCK',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b759_registration_%s.txt -- b759, THE EPSTEIN DOCUMENT AT v0.2: b758 AT ITS WEIGHT; FOUR STANDING CHANGES; ONE STATEMENT "
                             "AND FOUR PRINT LINES BY THEIR OUTCOME (data/b759_outcomes.txt); THE TABLE OF APPENDIX A REPRODUCED; THE DOCUMENT ENTERED; THE "
                             "CORPUS LINES RE-CUT; NO DEPOSIT, UNDER (R369)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b758's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b759: b758's lines read banks this
act does not write, and are not carried; the lines are b759's: the statement and the four print lines from the runner read by run id where they
landed (KERNEL); tools/standing/ v1.36.3 to v1.36.7, the controls tool, the table of Appendix A with its planted error and the reproduction run
by their controls (CERTIFIED); the document, its notes, the fields, the corpus lines and the errata (REGISTERED); what did not land, and the
draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b759's lines, each from the record tool's figures over b759's banks (REC._figs), the record's guard first
    REC._guard(f)
    w_ = f['oc']['weil']
    # ------------------------------------------------------------------ KERNEL or HELD: (R369)(5), the statement and the print lines, read by its run id (the name the template appends)
    sk = seat('%s_outcomes.txt' % ACT, '## (5) THE STATEMENT AND THE PRINT LINES')
    keys['WEIL'] = (('KERNEL -- THE STATEMENT AND THE FOUR PRINT LINES LANDED: zq_weil_positivity_fails with rQ_one, cQ_eq, detector and h2_sign_iff_rh, %s cut at main`s read-back = %s (tag object %s), run %s at %s, %s axioms lines each within the standard three, no sorryAx; the grade %s, binding no premise, read against the clause from the compiled statement. SOURCE %s.' % (
        w_['tag'], w_['peel'], (w_['tag_object'] or '-')[:8], w_['run'], K.WEIL_BRANCH[1][:8], w_['axiom_lines'], w_['grade'], sk['text'])) if f['weil_word'] == 'LANDED, COMPILED' else (
        'HELD -- THE STATEMENT, NOT LANDED AS ORDERED: %s, run %s. SOURCE %s.' % (f['weil_word'].lower(), w_['run'] or '-', sk['text'])))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.36.3 to v1.36.7 ((R369)(4) and the kernel route), by their controls
    sv = seat('%s_standing_v1367.txt' % ACT, '**v1.36.7: CONTROLS ')
    keys['VERSIONS'] = ('CERTIFIED -- tools/standing/ v1.36.3 TO v1.36.7, each by a commit of its own moving VERSION, its controls all as wanted, (4)`s four and the kernel route counted apart: %s. SOURCE %s.' % (
        '; '.join('%s at relay %s, %d of %d' % (v_, dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)[v_][:8], wv_, n_) for v_, _c, n_, wv_ in f['vers']), sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: (R369)(6), the table of Appendix A with its planted error
    st = seat('%s_c3table.txt' % ACT, '**THE TABLE OF APPENDIX A: ')
    keys['TABLE'] = ('CERTIFIED -- THE TABLE OF APPENDIX A %s, A REPRODUCTION AND NO REGISTERED PREDICTION: the plant printed first, beta at (3,2) read -2 reported unequal by each route at that cell alone, %s; route one, the group-ring model, %d of %d; route two, the form`s own count at -23, %d of %d; (a) %s and (b) %s; the law %s. SOURCE %s.' % (
        f['table_word'].upper(), f['c3_plant'].lower(), f['c3_one'][0], f['c3_one'][1], f['c3_two'][0], f['c3_two'][1], f['c3_a'].lower(), f['c3_b'].lower(), f['law_word'], st['text']))
    seats.append(st)
    # ------------------------------------------------------------------ CERTIFIED: (R369)(11), the reproduction run
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED: tools/research/reproduce.py`s full run in the foreground, rows %d, reproducing %d, differing %d, not run %d, the planted controls %d of %d as wanted, %d s. SOURCE %s.' % (
        f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs'], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ CERTIFIED: the dispatch and read tool by its own controls (the name the template appends)
    sw = seat('%s_controls_control.txt' % ACT, '**THE TOOL`S CONTROLS: ')
    keys['CONTROLS'] = ('CERTIFIED -- tools/b759_controls.py BY ITS OWN CONTROLS: %d of %d as wanted, committed before its opening dispatch; every run read by its id, the exit file governing, %d dispatch%s in SIDE-explicit-formula of 3 and none elsewhere. SOURCE %s.' % (
        f['cc_ctl'][0], f['cc_ctl'][1], f['disp_ef'], '' if f['disp_ef'] == 1 else 'es', sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: (R369)(8), the document and its notes, each by one PLACE-papers commit
    sd = seat('%s_compose.txt' % ACT, 'v0.2 COMPOSED:')
    keys['DOCUMENT'] = ('REGISTERED -- THE DOCUMENT AT v0.2: phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md beside v0.1 (%s), %d lines, BLOCK B %d of %d, %d cites read, %d corrected, %d listed, brackets left %d, the stems %s; one PLACE-papers commit, %s; its controls %d of %d. SOURCE %s.' % (
        f['cp_v01'].lower(), f['cp_lines'], f['cp_b'][0], f['cp_b'][1], f['cp_cites'], f['cp_corrected'], f['cp_listed'], f['cp_left'], f['cp_stems'].lower(), K.C3_DOC_PP[1][:8],
        f['cp_ctl'][0], f['cp_ctl'][1], sd['text']))
    seats.append(sd)
    sa = seat('%s_notes.json' % ACT, '"read_back"')
    keys['NOTES'] = ('REGISTERED -- WHERE ELSE (8) IS WRITTEN: %d PLACE-papers commits (%s), each by the tool of the notes at relay %s, committed before its run, each read back equal and committed alone. SOURCE %s.' % (
        len(f['notes']), ', '.join('%s %s' % (f_, c_[:8]) for _k, f_, c_, _n in f['notes']), K.C3_NOTES_GEN[:8], sa['text']))
    seats.append(sa)
    # ------------------------------------------------------------------ REGISTERED: (R369)(7), the fields
    sf = seat('%s_fields.txt' % ACT, '**FIELDS FILLED ')
    keys['FIELDS'] = ('REGISTERED -- THE FIELDS OF (7): %d filled from the banks and N and DEPOSITS by the corpus route, the pin %s, %d AX cells, F1 %s beside the quotient %s (%s), F2 %s; controls %d of %d, %d of %d and %d of %d. SOURCE %s.' % (
        f['fd_filled'], f['fd_pin'], f['fd_ax'], f['cl_f1'], f['cl_quot'], f['cl_word'].lower(), f['cl_f2'], f['fd_ctl'][0], f['fd_ctl'][1], f['fc_ctl'][0], f['fc_ctl'][1],
        f['cl_ctl'][0], f['cl_ctl'][1], sf['text']))
    seats.append(sf)
    # ------------------------------------------------------------------ REGISTERED: (R369)(9) and (10), the corpus lines and the errata
    sc = seat('%s_corpus.txt' % ACT, '**RE-CUT ')
    keys['CORPUS'] = ('REGISTERED -- THE CORPUS LINES OF (9): re-cut %d of %d, left %d, orders %d, one PLACE-papers commit a document, the one deposited copy not touched; controls %d of %d. SOURCE %s.' % (
        f['cr_recut'], f['cr_of'], f['cr_left'], f['cr_orders'], f['cr_ctl'][0], f['cr_ctl'][1], sc['text']))
    seats.append(sc)
    se = seat('%s_errata.json' % ACT, '"read_back"')
    keys['ERRATA'] = ('REGISTERED -- ERRATA AND THE ORDERS OF (10): %s, each read back equal and committed alone; W-ORD-MECHANISM-ATTRIBUTION open on the author`s word and five orders entered by name. SOURCE %s.' % (
        ', '.join('%s %s' % (f_, c_[:8]) for _k, f_, c_, _n, _x in f['errata']), se['text']))
    seats.append(se)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R369)(11)) (the name the template appends)
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    land_ = ['WEIL'] if f['weil_word'] == 'LANDED, COMPILED' else []   # ### b759: the line`s tier by its outcome
    order = [('KERNEL', land_), ('CERTIFIED', ['VERSIONS', 'CONTROLS', 'TABLE', 'REPRO']), ('REGISTERED', ['DOCUMENT', 'NOTES', 'FIELDS', 'CORPUS', 'ERRATA']),
             ('HELD', [k_ for k_ in ('WEIL',) if k_ not in land_] + ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b754 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
