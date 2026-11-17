# -*- coding: utf-8 -*-
# b758 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R368)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R368)(2) repair it carries. Edited by the Edit tool. Carried at b758 by tools/b758_fold.py (`carry`) from tools/acts/b757.py,
# b757`s names substituted; the citation`s sections adopted from tools/b758_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b757`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b757`s carried till
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
# ### b758, Component 1: THE c1 ROUTE FOR b757'S SHORT CORRIGENDUM, (R368)(1), written by the Edit tool against b757's banks (46 events, 28
# ### defects, 7 refusals; no post-seal events bank at b757 by its ferry's Component 6) and the findings after b757's lock entered as this act's
# ### events from the author's relay in the delivery (data/b758_events.txt (23)-(32)); short, as (1) orders: the counts from the banks, the
# ### CLAIM item (v) in full, the findings each with its time. (1) orders no weight line, where (R367)(1) ordered b756's, so the weight route is
# ### retired; (8) carries OPEN_TRAILS' lines, so the next route too. The carried stub (tools/standing/carry.py v1.34.0) removed by the Edit tool;
# ### nothing composed by it. The title under (R368)(3): no backtick (tools/standing/titlerule.py refuses one at the landing, v1.35.8).
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_NOTED = '2026-11-17'
C1_CORRIGENDA_LAST = 77
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b757_events.txt'), ('defects', 'b757_defects.txt'))
C1_EVENTS_N = 46
C1_DEFECTS = (28, "b'")
C1_REFUSALS = 7
C1_CLAIMS = (('events', '13'), ('defects', 'v'))   # ### b756's finding entered as b757's (data/b757_events.txt :88) and the ruled (v) (:35); b758 events (9)
C1_RULED_CLAIM = ('defects', 'v')
C1_FINDINGS_BANK = 'b758_events.txt'
C1_FINDINGS_IDS = tuple(str(i_) for i_ in range(23, 33))
C1_RULED = (('23', ('19:35:51Z', 'PIPE')), ('24', ('mirror_prevbuild.json', 'CARRIAGE RETURNS', 'RESTORED BY THE TOOL')), ('25', ('19:43:30',)),
            ('26', ('20:16:36',)), ('27', ('21:26:01',)), ('28', ('514.8 s',)), ('29', ('G-TRAIL-CARRIES-SEAL', 'UNDECLARED')),
            ('30', ('--quiet', 'REFUSED AND RESENT')), ('31', ('21:55:35Z', 'TWO BACKTICKS')), ('32', ('23:19:16Z', 'PIPE')))   # ### (R368)(1)'s list in its order, the PIPE at 23:19:16Z from the author's words before the ruling
C1_CORR_TITLE = ('## Corrigendum to b757’s record, short (relay data/b757_events.txt rows (1)-(46) and data/b757_defects.txt (a)-(b’)): its events and '
                 'defects by count from their banks, its CLAIM item (v) in full, and the findings after the lock, entered as events with their times')
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
    cnt, l_cn = _c1_fl('b757_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    rf = [l for l in _c1_rd('b757_hook_refusals.txt').split(NL) if l.strip()]
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
        ('the event rows (1)-(%d)' % C1_EVENTS_N, [int(r[0]) for r in ev] == list(range(1, C1_EVENTS_N + 1))),
        ('no post-seal events bank at b757', not os.path.exists(os.path.join(D, 'b757_events_postseal.txt'))),
        ('the defect rows %d, the last (%s)' % C1_DEFECTS, len(df) == C1_DEFECTS[0] and df[-1][0] == C1_DEFECTS[1]),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev)) == tuple(int(x) for x in cnt)),
        ('the CLAIM rows events (13) and defects (v)', [(k_, r[0]) for k_, r in claims] == list(C1_CLAIMS)),
        ('the refusals %d, each by its kind' % C1_REFUSALS, len(rf) == C1_REFUSALS and '?' not in kinds),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the ten findings, each with its date and time', all(fnd) and all(_c1_time(r[4]) for r in fnd)),
        ('the ruled findings, each in its row: missing %s' % ruled, not ruled),
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
    L = ['*b757’s events bank (relay data/b757_events.txt) carries %d rows, (1)-(%d): CLAIM %d, CLOSE %d, REPEAT %d; its defects bank (relay '
         'data/b757_defects.txt) %d lettered rows, (a)-(b’): CLAIM %d, CLOSE %d, REPEAT %d. Together CLAIM %d, CLOSE %d, REPEAT %d of %d, as b757’s closing '
         'counter prints it (relay data/b757_closing.txt :%d, the closing record written at b758 by b757’s sealed tools under `(R368)`(1)). Its refusals '
         'bank %d lines (relay data/b757_hook_refusals.txt), by kind %s, the seventh committed at b758’s step zero (relay 41ff314d). No post-seal events '
         'bank at b757, by its ferry’s Component 6. Each item is tagged in its own bracket; the tags are the banks’ own and this entry edits none of them.*' % (
             pe['total'], pe['total'], pe['claim'], pe['close'], pe['repeat'], pd['total'], pd['claim'], pd['close'], pd['repeat'],
             t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds), '']
    L += ['**The CLAIM item (v), in full:**', '']
    for k_, (i_, o_, tg_, col_, tx_) in [(k_, r) for k_, r in s['claims'] if (k_, r[0]) == C1_RULED_CLAIM]:
        L += ['**(%s)** %s (relay data/%s, row (%s); %s; %s; %s).' % (i_, _c1_q(tx_).replace("'", '’'), dict(C1_BANKS)[k_], i_, _c1_owner(o_), tg_, _c1_col(col_)), '']
    L += ['b757’s other CLAIM row, events (13), is one of b756’s findings after its lock that b757 entered as its own events; it stands in full in '
          'b757’s corrigendum (FINDINGS :%d) and is counted here.' % K.B711_CORRIGENDUM, '']
    L += ['**The findings after b757’s lock**, entered as events of b758 from the author’s relay in `(R368)`(1) and the author’s words before the ruling '
          '(the delivery at transcript line 112358, 2026-11-16T23:21:58Z; relay data/b758_events.txt rows (23)-(32)), each with its time on 2026-11-16: '
          'CLAIM %d, CLOSE %d, REPEAT %d of %d. %s.' % (
              ft['claim'], ft['close'], ft['repeat'], ft['total'],
              '; '.join('(%s) %s, %s [%s ; %s]' % (r[0], _c1_q(_c1_head(r[4])).replace("'", '’'), _c1_time(r[4]), r[2], _c1_col(r[3])) for r in s['findings'])), '']
    L += ['**The repairs:** the reader of tools/standing/act.py :82 at v1.35.6 (relay ac6a0a77) under `(R368)`(1); b757’s four carried steps, [22] to '
          '[25], run at b758 under v1.35.7 (relay 248cacb8), the bound of the author’s amendment of (1) (relay data/b758_amendments.json row 1): b757 '
          'closed at 7 of 8 HELD, N3 REFUTED on (v) as ruled (relay data/b757_scores_close.json, 401d3bda); the composer at v1.35.8 (relay ed0d3f33) under '
          '`(R368)`(3); G-TRAIL-CARRIES-SEAL ordered under `(R368)`(6).', '',
          '*Filed at b758 on the author’s ruling `(R368)`(1): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b758.py) from b757’s events, defects and refusals banks read unedited and b758’s events rows (23)-(32); '
          'banked as relay `data/b758_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b757’s record; no '
          'sealed tool, face, trail or root-named bank of b757 is edited. No weight line is written: `(R368)`(1) orders none.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    ft = _c1_tally(s['findings'])
    return (['b758 -- THE CORRIGENDUM FOR b757, SHORT, (R368)(1) (%s)' % utc(), '',
             '### the banks read unedited: data/b757_events.txt rows (1)-(%d), data/b757_defects.txt %d rows, data/b757_hook_refusals.txt %d lines; no '
             'post-seal events bank at b757; data/b757_closing.txt :%d (the counter); data/%s rows (23)-(32) (the findings after the lock); the '
             'corrigenda bank`s last row (%d).' % (len(s['events']), len(s['defects']), s['refusals'], s['l_counter'], C1_FINDINGS_BANK, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEM IN FULL 1 ; THE FINDINGS AFTER THE LOCK %d: '
               'CLAIM %d, CLOSE %d, REPEAT %d ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['defects']), t['claim'], t['close'], t['repeat'], ft['total'], ft['claim'],
                   ft['close'], ft['repeat'], ln)])


def c1(*a):
    """`c1 corrigendum [dry|write]`: the short corrigendum for b757, landed through b698's guarded landing (the title rule of v1.35.8 in front of
    it); dry prints and writes nothing. (R368)(1) orders no weight line and (8) carries OPEN_TRAILS' lines: `c1 weight` and `c1 next` refuse."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        sys.exit('### (R368)(1) ORDERS NO WEIGHT LINE FOR b757 ((R367)(1) ordered b756`s) -- NOTHING COMPOSED')
    if route == 'next':
        sys.exit('### (R368)(8) CARRIES OPEN_TRAILS` LINES UNDER ONE DATED HEAD -- NOTHING COMPOSED HERE')
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
                                                   claims=[dict(bank=dict(C1_BANKS)[k_], id=r[0], owner=r[1], column=r[3]) for k_, r in s['claims']],
                                                   in_full=dict(bank=dict(C1_BANKS)[C1_RULED_CLAIM[0]], id=C1_RULED_CLAIM[1]),
                                                   findings=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_FINDINGS_IDS), claim=ft['claim'],
                                                                 close=ft['close'], repeat=ft['repeat'],
                                                                 times=dict((r[0], _c1_time(r[4])) for r in s['findings']),
                                                                 claims=[dict(id=r[0], owner=r[1], column=r[3]) for r in s['findings'] if r[2] == 'CLAIM']),
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   repairs=dict(reader='v1.35.6 ac6a0a77', bound='v1.35.7 248cacb8', composer='v1.35.8 ed0d3f33',
                                                                trail_arm='(R368)(6)'),
                                                   weight_line=None, row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEM IN FULL (v) ; THE FINDINGS %d, CLAIM %d ; FINDINGS :%s' % (
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
    """N1, b758 ((R368)(10)): every dispatch of the act a row of the dispatch bank, its kernel named, its free memory read before the send at or
    above the hold; the run ids by kernel the worklist's, EF_RUNS in SIDE-explicit-formula within 4 and none in SIDE-dirichlet-mod-24
    (M24_RUNS empty, its cap 0: (6)(i) moves that kernel's local main alone), no dispatch row of another kernel; each read once after it by
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
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b757, naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base 28255aea the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b757-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b758_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b754, Component 6 (the Edit tool), carried: the step-zero bank words the row "THE --MERGED LISTING, PRINTED BEFORE THE DELETES"
# ### (data/b755_stepzero.txt :55)
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's overrides of checks 1516 and 1659 (hook.py edited by b753's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b754 as it stands
# ### b754, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b758_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b756, Component 6 (the Edit tool): the corrigendum's json (data/b756_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 46, CLAIM 0, CLOSE 46, REPEAT 20, the CLAIM items 0, the corrigenda row (76); the rows stand in the bank by
# ### their banks (data/b756_corrigendum.txt); the template's row range read as the json's counts
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 48 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
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
# ### b757, Component 6 (the Edit tool): b757's citation check carries the kept row under (R367)(4) and (10) ("the four branches stand as
# ### they stood"; "no kernel touched beyond SIDE-explicit-formula and SIDE-dirichlet-mod-24"), data/b757_citation_check.txt :74, "| ruling
# ### (4), (10) | port-b707 kept on SIDE-lv-conservation | local |"; b756's "(8)" read no row and failed the arm at the standing-a2 probe (12:11Z)
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and '| ruling (4), (10) | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b757, Component 6 (the Edit tool): G-DELETES-ONE-BRANCH's allowance read over the step-zero deletes alone -- (R367)(2)'s "The
# ### push-b756-* branches are deleted by the tool's route" (data/b757_ferry.txt :11); the two control branches of (R367)(3), "a commit in
# ### each of the two kernels on a scratch branch, read back and then deleted by the tool's route" (:13), name no branch in the ruling, so
# ### they are read from the live control's bank, which names each by its commit's subject (data/b757_standing_v1354_live.txt :22, :25),
# ### and are wanted deleted, the two and no other; (R367) writes no kept clause and names no port-b707, so the kept term reads port-b707
# ### undeleted and at its tip in the tree in place of a clause the ruling does not carry (scratch dels757.py, 11:5xZ: 7 deletes, OUTSIDE
# ### the two controls, the kept clause '')
#⟪OVERRIDE checks MARK 61379f7e4609 2⟫
        and (_ctl := sorted(set(re.findall(r'on (push-b758-control-[a-z0-9]+)[ ,]', rd('b758_standing_v1354_live.txt') or '')))) == ['push-b758-control-ef', 'push-b758-control-mod24'] \
        and sorted(b for b in got if b in _ctl) == _ctl and STW.deletes_read([('-', b) for b in got if b not in _ctl], S['ferry'], STW.words_of(ACTN))['ok'] \
        and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP \
#⟪END⟫
#⟪OVERRIDE checks MARK 23e17a97edcc 1⟫
    ('G-DELETES-ONE-BRANCH', '(⟪PRUL⟫)(2), (3): the command capture`s branch deletes, each one branch, no glob, no variable, nothing chained after; the step-zero deletes each allowed by the ruling`s own delete clause read through tools/standing/allow.py, the two control branches of (3) the live control`s bank names, deleted and no other; port-b707 undeleted at its tip; the command bank`s count',
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
                                                                          or (bool(S['report_tool']) and 'tools/acts/b757.py -> tools/acts/b758.py' in (rd('b758_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and (_ for _ in ()).throw(SystemExit('### b758`s a probe`s needle (OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED'))   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 1 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    raise SystemExit('### b758`s a probe`s needle (OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 8 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b758')
    return '### THE COUNTER ((R368) Component 5, the act`s events and defects together; relay data/b758_defects.txt, data/b758_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-SQUARES-AT-24 entered in (9)`s block ((R368)(6)); W-ORD-MECHANISM-ATTRIBUTION open, T0 and T1 compiled on push-b758-coeff, its condition read by the navigator at the next ruling ((R368)(5)); W-ORD-KEIPER-FACE, W-ORD-EXPLICIT-FORMULA-C1, W-ORD-E2-SEPARATION, W-ORD-BESSEL-BOUND-TIGHTEN and W-ORD-B518-FLOAT CARRIED in (9)`s block;',
    '        W-ORD-LI-ARITH, W-ORD-ZQ-FAMILY, W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    raise SystemExit('### b758`s a probe`s needle (OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 1 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b758_author_answers.txt', 'b758_answer_check.txt', 'b758_events.txt'))   # noqa: E731,E702
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
REG = os.path.join(ROOT, 'data', 'b758_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b758_registration_%s.txt' % __import__('b758_worklist').DATE)   # ### the gate imports no worklist of its own
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
    ('commits on any kernel`s main', 2, 2, 'commits', '### (R368)(6): SIDE-dirichlet-mod-24`s main moved from 597b0869 to the workflow 22282733 and then to the module e5ebdd15 after its run`s success, each read back at the remote; SIDE-explicit-formula`s main unmoved at 8fbab45d.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 18c1a19a6cb6 1⟫
    ('scratch branches cut on a kernel', 2, 2, 'branches', '### (R368)(3)`s live control: push-b758-control-ef and push-b758-control-mod24, a commit on each read back, each deleted by the tool`s route (data/b758_standing_v1354_live.txt).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK a2b9535083e6 1⟫
    ('push branches cut on a kernel for the push procedure', 4, 4, 'branches', '### push-b758-join and push-b758-coeff in SIDE-explicit-formula, push-b758-workflow and push-b758-mod24 in SIDE-dirichlet-mod-24, each made by the one-call tool and carried by the gated push, standing at the close.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 42ab3bdb112d 1⟫
    ('kernel merges made', 4, 4, 'merges', '### (R368)(4): detect-b729, keiper-b725, c2-b725 and zq-b730 into push-b758-join, one at a time without fast-forward (0a0672bc, 12d60407, 36ad7bb7, 0cc23db8); no branch merged into a main.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 63e5424dd90e 1⟫
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### N5: one, v0.2.0 in SIDE-dirichlet-mod-24 (object e5c84316, peel e5ebdd15 read back at the remote equal to main); v0.38 unmoved at 14ca5725, no v0.39 and no v0.40; MEASURED off SIDE-explicit-formula`s tags past v0.38, SIDE-dirichlet-mod-24`s past v0.1.0, and the template`s other kernels as before.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 5381b10a2ae6 1⟫
    ef_tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() not in ('v0.37', 'v0.38')] + [t for t in _git(K.M24_DIR, 'tag', '--list').split(chr(10)) if t.strip() and t.strip() != 'v0.1.0']   # ### b757: v0.38 b745`s; SIDE-dirichlet-mod-24`s tags past v0.1.0
#⟪END⟫
#⟪OVERRIDE regspec MARK 100638d8d84e 1⟫
    ('kernel branches deleted', 2, 2, 'branches', '### the two control branches of (R368)(3), each by the tool`s route after its read-back; port-b707, the pin, challenge and rebuild branches and the four held branches kept; the four push-b758-* branches standing.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 51acd0ac8ef1 1⟫
    ('branches deleted beyond the step zero`s list', 2, 2, 'branches', '### the two control branches, deleted as (R368)(3) orders; port-b707 kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK b6204f4e0fa8 1⟫
    ('census editions written on main', 0, 0, 'editions', '### none: no new edition; the census v0.8.3 takes (R368)(9)(c)`s one note at its end (PLACE-papers 9c0896c5).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 0daf7a1cb287 1⟫
    ('papers moved, renamed or written beyond FINDINGS, OPEN_TRAILS and REGISTRY', 3, 3, 'papers', '### (R368)(9)(a)-(c): one dated note each in THE_EPSTEIN_CONTROL_OBJECT_v0_1.md, FACES_LEDGER.md and THE_KEYSTONE_CENSUS_v0_8_3.md, by one PLACE-papers commit each; none moved or renamed, no sentence edited.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 46160108b751 1⟫
    ('README edits', 1, 1, 'edits', '### (R368)(4)(iii): [B1] on push-b758-join (6568e9c7), not on any main; SIDE-dirichlet-mod-24`s README not written; [B3] carried whole.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 2d7a99569826 1⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 18, 18, 'lines', '### (R368)(1), (9)(e): the dated block at the file`s end, the line of (1), the order lines, W-ORD-SQUARES-AT-24 and [L22], by PLACE-papers b14256c2 (git diff --numstat b6860142 b14256c2 -- OPEN_TRAILS.md: 18 added, 0 removed).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 44ff8bc9f5d4 1⟫
    ('faces ledger update blocks appended', 1, 1, 'blocks', '### (R368)(9)(b): one UPDATE section at FACES_LEDGER`s end (PLACE-papers c7dfe43c), no face entered.'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b758_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): G-SCORER-READS-BANKS's needles set to the banks b755's N1-N4 read (the command bank and the
# ### dispatch rows, N2's controls and first adds, the walk among the figure banks, the seal and step banks), the carried stub's refusal
# ### removed; the ledger exclusion unchanged. The arm stands in tools/standing/arms.py's RETIRED and is not in the run list; read so, its
# ### template line :971 would fire on N3's label of the landed entry (record.tpl :2444, a string naming FINDINGS.md), not edited here
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    raise SystemExit('### b758`s a probe`s needle (OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0), ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED: written for the act before use -- NOTHING COMPOSED')
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### b757: the seat's rows of data/b757_defects.txt as the template's reader takes them, (a) to (z), each THE SEAT'S, as the face's (xiii) reads them at the seal; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b758_corrigendum.txt', 'data/b758_price.txt', 'data/b758_standing_v1354.txt', 'data/b758_standing_v1354_live.txt',
                  'data/b758_controls_control.txt', 'data/b758_controls.txt', 'data/b758_join.txt', 'data/b758_join_targets.json', 'data/b758_dispatch_rows.json',
                  'data/b758_ceiling.txt', 'data/b758_ceiling.json', 'data/b758_outcomes.txt', 'data/b758_outcomes.json',
                  'data/b758_cut.txt', 'data/b758_standing_v1355.txt', 'data/b758_ghcalls.txt', 'data/b758_registry_line.txt', 'data/b758_doors.txt', 'data/b758_doors_rows.json',
                  'data/b758_notes.json', 'data/b758_notes_moved.txt', 'data/b758_sweep.txt', 'data/b758_sweep.json', 'data/b758_author_answers.txt',
                  'data/b758_address_scan.txt', 'data/b758_touch.txt',   # ### b757, Component 6: the act's banks by its components, in place of b756's carried names; no amendments, rules or reproduce bank this act (the run computes at fields, which (R367)(10) bars)
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b758_address_scan.py'), 'scan'], capture_output=True, text=True,
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
    """(R367)(1)-(9): the act's relay commits after step zero in their order, (key, commit) -- v9, then the worklist's CHAIN (the c1 route,
    the corrigendum banks, v1.35.4 and its live control, the controls tool and its repairs, the join's tools and bank, the composer of the
    outcomes and its banks, the ceiling, (8)(iv)'s tool, the doors, the gh-call reader, v1.35.5, the sweep, the cut, the tool of the notes and
    its bank), then the handoff page and the lock gate where each is made, in that order; read from the worklist at the call."""
    c = [('v9', K.STANDING_COMMIT)] + list(K.CHAIN)
    c += [(k_, h_) for k_, h_ in (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT), ('lockgate', K.C1_LOCKGATE)) if h_]
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
        # ### b757, Component 6: the act's banks its arms read -- the notes of (9), the ceiling after Component 3 at HEAD and at its commit, the
        # ### doors; b756's map, orders, put, passed-writes and fault banks have no counterpart at this act and are not read
        notesj=jl('b758_notes.json'),
        ceiling=(rd('b758_ceiling.txt'), _s(blob(ROOT, '%s:data/b758_ceiling.txt' % K.C1_CEILING))),
        doors=rd('b758_doors.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        pp_files=dict((k_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        numstat=dict((k_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        kst=_kernel_state(),   # ### b757: the two kernels' refs, tags and the kernel commits' containing refs (G-OFFSET-POST-HOC)
        drows=json.loads(rd('b758_dispatch_rows.json') or '[]'), reproduce=rd('b758_reproduce.txt'), reproducej=jl('b758_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b758_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b758_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
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
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): statement READFIRST_NEEDLES; it carried an act ordinal or the read-first needles
READFIRST_NEEDLES = __import__('standing.carry', fromlist=['Carried']).Carried('b758`s READFIRST_NEEDLES')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R368)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'ROUTE FOR KERNEL WRITES ((R368)(3))', 'BUILDS ((R368)(4)-(7))', 'REPAIRS OF (8) ((R368)(8))', 'NOTES OF (9) ((R368)(9))',
 'NAME AND ADDRESS (N5)', 'RESEARCH INSTRUMENTS NOT REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', 'TOUCH READ (standing clauses v9)')   # ### b757: closing 7's sections, the ferry's components in order
#⟪END⟫
#⟪SECTION checks 12⟫
    """b758: the citation check's bank: every cite checked, OK and misses summing (94 = 94 + 0, data/b758_citation_check.txt :154), no
    miss; the check HALTED on one Lean-path row (:156, halts 1: Lean paths and nouns 1, comparatives 0), as the step-zero bank enters it
    (data/b758_stepzero.txt :58-:60, after the act_current commit and the subject read), the halt row read there by hand before the deletes
    (:95-:101; defect (c), events (5)); the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 94 \
        and '### ### **THE CHECK HALTED** (halts 1: Lean paths and nouns 1, comparatives 0)' in c \
        and 'THE CITATION CHECK BANKED (' in (S['stepz'] or '') and 'CITES CHECKED 94 ; OK 94 ; MISSES 0 ;' in (S['stepz'] or '') \
        and '## THE ONE HALT ROW OF THE CITATION CHECK, READ' in (S['stepz'] or '') and "h2_sign_cfg_imp_online against every path of a clause of 5" in (S['stepz'] or '') \
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
                    MISSES=tfirst('b758_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b756's figures, read at FINDINGS :15414 as Component 1 landed them (b756's closing head quoted, data/b756_closing.txt :1, PLACE-papers 810ec2da)
    return landed(S, 0, ['b757 AT ITS WEIGHT', 'suite 110 of 116', '48bf6d77facceaf4', '4 prompts answered', 'scores 8 of 8 HELD', '11 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b757's title by its objects, the ferry's Component 6 order (data/b757_ferry.txt :49) adjusted to what the act did (record 31's _title
# ### over the banks' feet, printed by scratch title757.py through tools/standing/fold.py load, writing nothing: the join broken at the import,
# ### no tag cut; T0 and T1 compiled on push-b757-coeff; the module under v0.2.0; the wide direction compiled; 8 dispatches, 6 and 2; the
# ### repairs 5 landed; the notes of (9) 5 written)
TITLE_NEEDLES = ('## The build under (R368): the join of SIDE-explicit-formula`s four held branches broken at SIDEExplicitFormula.Schema.ZQ.OffZero.Time :18, no tag cut (b758_join, b758_outcomes)',
                 'T0 compiled at 89eb71b6 and T1 compiled at e52f9060 on push-b758-coeff', 'the modulus-24 module compiled under v0.2.0',
                 'the one direction over the wider strip compiled at 596d1c9e (b758_outcomes)',
                 '8 dispatches, 6 in SIDE-explicit-formula and 2 in SIDE-dirichlet-mod-24 (b758_dispatch_rows)',
                 'the five repairs, 5 landed (b758_cut, b758_standing_v1355, b758_ghcalls, b758_registry_line, b758_doors)',
                 'the notes of (9), 5 written (b758_notes)')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R368)(1): the generated corrigendum for b757's record landed, short (its line in the json, FINDINGS :15416, the title at that line
    through conv): b757's 37 events and 11 defects by count from their banks, 48 items, CLAIM 1 and CLOSE 47, REPEAT 33, its one CLAIM item
    in full (b757 events (10), THE TOOLS', NEW); the seven findings the seat printed after b757's lock entered as events (7)-(13) (CLAIM 1,
    CLOSE 6, REPEAT 5) with the navigator's correction to (F6) (G-RUNNER-GATE); no repair in Component 1's corrigendum ((R368) orders (F5)-(F7)
    under (8)); the corrigenda bank appended at row (77) and nothing before it changed; in Component 1's commits (the figures read from
    data/b758_corrigendum.json and the bank's foot)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 77 and j.get('claim') == 1 == len(j.get('claims') or []) and j.get('close') == 47 and j.get('repeat') == 33 \
        and '### ### **ITEMS 48: EVENTS 37, DEFECTS 11 ; CLAIM 1, CLOSE 47 ; REPEAT 33 ; THE CLAIM ITEMS IN FULL 1 ; THE SEVEN FINDINGS 7: CLAIM 1, CLOSE 6, REPEAT 5 ; ' in (S['corrt'] or '') \
        and 'THE CORRECTION TO (F6) ENTERED ; THE ENTRY AT FINDINGS :15416.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and [(c_.get('bank'), c_.get('id'), c_.get('column')) for c_ in (j.get('claims') or [])] == [('b757_events.txt', '10', 'NEW')] \
        and (j.get('findings') or {}).get('rows') == ['7', '8', '9', '10', '11', '12', '13'] \
        and [(j.get('findings') or {}).get(k_) for k_ in ('claim', 'close', 'repeat')] == [1, 6, 5] \
        and (j.get('correction') or {}).get('f6') == 'G-RUNNER-GATE' \
        and '  (77) ' in S['corrigenda'] and '  (78) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R368) orders no rules bank for this act; the rule it works by is b757's, data/b757_rules.txt,
    its rows (a) to (c) in force from b758 by (R367)(2); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here b757's rows (a) to (c), lettered as (R367)(2) letters them, in b757's Component 1 commit (relay 0a151012) and no other, the working
    tree its blob at HEAD; no data/b758_rules.txt written (the worklist's C1_RULES None)."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and re.findall(r'(?m)^  \(([a-z])\) ', rd('b757_rules.txt') or '') == ['a', 'b', 'c'] \
        and not r1 and K.C1_RULES is None and not os.path.exists(os.path.join(D, 'b758_rules.txt')) \
        and _txt(rd('b757_rules.txt')) == _txt(blob(ROOT, 'HEAD:' + K.B756_RULES[0])) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', K.B756_RULES[0]).split()] == [K.B756_RULES[1][:8]] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b757's report lines (report sections 2-5): each key a phrase its line opens with
REPORT_KEYS = ('KERNEL -- T0 AND T1 ON push-b758-coeff', 'KERNEL -- THE MODULUS-24 MODULE IN SIDE-dirichlet-mod-24', 'KERNEL -- THE ONE DIRECTION OVER THE WIDER STRIP ON',
               'CERTIFIED -- tools/standing/ v1.35.4 AND v1.35.5', 'CERTIFIED -- tools/b758_controls.py BY ITS OWN CONTROLS',
               'REGISTERED -- THE NOTES OF (9)', 'REGISTERED -- THE FIVE REPAIRS OF (8), EACH WITH ITS CONTROL',
               'HELD -- THE JOIN OF THE FOUR BRANCHES, BROKEN', 'HELD -- THE REPRODUCTION RUN, NOT RUN',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b758 ((R368)(10)): every runner dispatch of the act sent by tools/b758_controls.py's dispatch route, one command in the
    capture for each dispatch row (8: 6 in SIDE-explicit-formula of 14, 2 in SIDE-dirichlet-mod-24 of 4), each read once after it by its run
    id, every dispatch and read row's free memory at or above the hold; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### b757: the act's own rows, 8 dispatches and 8 reads; the order read by the loop above, by run id
    order = order and len(seq_) == 2 * len([r for r in rows if r.get('kind') == 'dispatch'])
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b758_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) + len(K.M24_RUNS) == len(cmds) \
        and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES == 4 and len(K.M24_RUNS) == K.MAX_DISPATCHES_M24 == 0 \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b758 step zero, (R368)(10): one to four dispatches in SIDE-explicit-formula ((4)'s and (5)'s), none in SIDE-dirichlet-mod-24
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5, (R368)(10): PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry;
    OPEN_TRAILS: (9)'s block under one dated head, (1)'s line among it, and the trail; REGISTRY: (8)(iv)'s line in place and (9)(d)'s note;
    FACES_LEDGER: (9)(b)'s UPDATE section; the Epstein document and the census: (9)(a)'s and (9)(c)'s notes), the ledgers changed; no rename;
    no other paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b757's headings and banks, as its _finding_text (record 34) writes them; the last the INTEGRATION line's opening words (_integ_line)
ENTRY_NEEDLES = ('**The weight and the corrigendum**', '**The route for kernel writes**', '**The join**', '**T0 and T1**', '**The modulus-24 module**',
                 '**The one direction over the wider strip**', '**The five repairs**', '**The notes of (9)**', '**The order of the act**', '**What this act is not**',
                 '**The research instruments not reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b758_price.txt', 'data/b758_corrigendum.txt', 'data/b758_standing_v1354.txt', 'data/b758_standing_v1354_live.txt', 'data/b758_controls_control.txt',
                 'data/b758_controls.txt', 'data/b758_dispatch_rows.json', 'data/b758_join.txt', 'data/b758_outcomes.txt', 'data/b758_ceiling.txt',
                 'data/b758_registry_line.txt', 'data/b758_doors.txt', 'data/b758_ghcalls.txt', 'data/b758_standing_v1355.txt', 'data/b758_sweep.txt', 'data/b758_cut.txt',
                 'data/b758_notes.json', 'data/b758_notes_moved.txt', 'data/b758_events.txt', 'data/b758_address_scan.txt', 'data/b758_touch.txt',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: the join: ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R368)(1), (8)(iv), (9), N5 (the name the frozen run list carries): PLACE-papers written by the worklist's PP_CHAIN in its order and
    by nothing else before the record -- the weight line and the corrigendum in one commit touching FINDINGS alone, the act's first on its
    base ((1)'s dated line stands in (9)'s block in OPEN_TRAILS); REGISTRY's header at :13 replaced in place under (8)(iv), one line added and
    one removed, the registry-line bank's foot reading LINE 13 REPLACED and LINES MOVED 0; the five notes of (9) each touching its one file,
    the notes bank's confirm naming each commit with none removed; every commit but (8)(iv)'s removing no line; the changed files since the
    base within PP_WRITTEN; by ancestry the base, each commit of the chain and HEAD; the earlier acts' registrations at HEAD their blobs."""
    pf_, ns_ = S['pp_files'] or {}, S['numstat'] or {}
    nj_ = (S['notesj'] or {}).get('items') or {}
    pc_ = dict(K.PP_CHAIN)
    want_ = [('c1pp', ['FINDINGS.md'], None, '0'), ('pp_registry', ['REGISTRY.md'], None, '1')] \
        + [('pp_' + lab_.strip('()'), [fn_], (nj_.get(lab_.strip('()')) or {}).get('confirm') or '-', '0') for lab_, fn_, _h in K.C3_NOTES_PP]
    rows_ = [(k_, sorted(pf_.get(k_) or []) == sorted(fs_) and bool(ns_.get(k_)) and all(x_ == rm_ for x_ in (ns_.get(k_) or [])[1::3])
              and (c_ is None or (c_.startswith('PLACE-papers %s at ' % pc_.get(k_, '-')[:8]) and 'none removed' in c_))) for k_, fs_, c_, rm_ in want_]
    rg_ = '### ### **(8)(iv): CONTROLS 2 OF 2 AS WANTED ; LINE 13 REPLACED ; LINES MOVED 0 ; ' in (rd('b758_registry_line.txt') or '')
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:len(K.PP_CHAIN)]] == [h_[:8] for _k, h_ in K.PP_CHAIN]
    return len(rows_) == len(K.PP_CHAIN) == 7 and set(k_ for k_, _o in rows_) == set(pc_) and all(o_ for _k, o_ in rows_) and order_ and rg_ \
        and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b758_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R368)(1)-(9), N2, N4 (the name the frozen run list carries): the act's order by time -- the worklist's TIME_ORDER, relay and
    PLACE-papers together (the act_current commit, step zero's banks, the c1 route, PLACE-papers' weight and corrigendum, the corrigendum
    banks, v1.35.4 and its live control before any kernel write, the controls tool before its opening dispatch, the join's tools and bank, the
    composer of the outcomes and its banks, the ceiling's tool and bank, (8)(iv)'s tool and its write, the doors and the gh-call reader,
    v1.35.5, the sweep's tool and bank, the cut's tool and bank, the tool of the notes, its five writes and its bank), then the lock gate and
    the handoff page where made; by ancestry within the relay from v9 through each commit of _chain; each of the two standing versions'
    banks at HEAD its blob at its commit, its foot ALL AS WANTED at the worklist's cases, VERSION and the bank in that commit's files; the
    act's commits under tools/standing/ those two and no other."""
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
        and len(sb_) == len(K.STANDING_BANKS) == 2 and all(sb_) and st_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R368)(3)-(9), N2, N3 (the name the frozen run list carries): each tool of K.GENS first added by a commit of its own, every one of
    its commits carrying it and not its bank, the bank's commit carrying the bank and not the tool and after every tool commit, the bank at
    HEAD its blob there (ten: the controls tool, the join, the composer of the outcomes, the ceiling, (8)(iv)'s tool, the doors, the gh-call
    reader, the sweep, the cut, the tool of the notes); no tool committed with its bank (GENS_WITH_BANK empty; the controls tool's control
    bank in its first commit, defect (i)); the outcomes bank's foot the five outcomes as the entry reads them; the ceiling after Component 3
    at HEAD its blob at its commit, nothing carried; the join's, the cut's, the sweep's, the gh-call reader's and the doors' feet as the
    report seats them."""
    gk_ = _gens_ok(S)
    ce_ = S['ceiling'] or (None, None)
    ceil_ = bool(ce_[0]) and _txt(ce_[0]) == _txt(ce_[1]) and _vlast(_txt(ce_[0])).startswith('THE CEILING AFTER COMPONENT 3: ') and ', NOTHING CARRIED ;' in _vlast(_txt(ce_[0]))
    feet_ = [('b758_outcomes.txt', 'THE OUTCOMES: JOIN BROKE ; T0 COMPILED ; T1 COMPILED ; MOD24 COMPILED ; WIDE COMPILED.'),
             ('b758_join.txt', 'THE JOIN: MERGES AS ORDERED ; THE UNION DIFFERENCES 0 ; TARGETS 93 MODULES FOR 419 NAMES, 0 REFUSED ; CONTROLS 8 OF 8.'),
             ('b758_cut.txt', '(8)(i): CONTROLS 4 OF 4 AS WANTED ; ON b757`S BANK WHOLE THE CUT CHECK PASSES, ON THE PLANTED SECOND RESULT FAILS.'),
             ('b758_ghcalls.txt', '(8)(iii): CONTROLS AS WANTED ; OVER b757`S BANKS THE CARRIED READER NONE, THE TAUGHT READER 2.'),
             ('b758_doors.txt', '(8)(v): CONTROLS AS WANTED ; SENT 2 OF 2 (EDIT CALLS 2) ; READ BACK EQUAL TO THE PASSED TEXT 2 OF 2 (PLACE-papers, SIDE-kernel).')]
    ft_ = [_vlast(_txt(rd(n_))) == w_ for n_, w_ in feet_] + [_vlast(_txt(rd('b758_sweep.txt'))).startswith('THE SWEEP: CONTROLS 9 OF 9 AS WANTED ; LINES SAYING ONE OF THE THREE STATEMENTS 24: ')]
    return len(gk_) == len(K.GENS) == 10 and all(o_ for _n, o_ in gk_) and K.GENS_WITH_BANK == () and ceil_ and all(ft_)


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R368)(3)-(7), (10) (the name the frozen run list carries): the kernels this act wrote, read at the two it opens and no remote
    read -- SIDE-explicit-formula's main at EF_BASE 8fbab45d locally and at its tracking ref (unmoved: the join broke, (4)'s failing
    outcome); its four held branches at their entering tips locally and at origin, zq-b730 at 1e658870 (its move the route the seat lacks,
    events (17)-(18)); push-b758-join at 6568e9c7 and push-b758-coeff at 596d1c9e, each equal to its tracking ref; each kernel commit of the
    worklist on its branch, the two live controls' scratch commits on no ref (their branches deleted by the tool's route); v0.38's object
    21c6edaf and peel 14ca5725 and no tag past it (no v0.39, no v0.40); SIDE-dirichlet-mod-24's main at e5ebdd15 at its tracking ref (its
    local main at the entering 597b0869 or at e5ebdd15: the gated push moves the remote's main from a push-* branch), v0.2.0's object e5c84316
    peeling to e5ebdd15, v0.1.0 at 597b0869 and no other tag; no sitting kernel."""
    ks_ = S['kst'] or {}
    ef_, m4_, ct_ = ks_.get('ef') or {}, ks_.get('m24') or {}, ks_.get('contains') or {}
    def h_(d_, r_):
        return (d_.get(r_) or ('', ''))[0]
    def p_(d_, r_):
        return (d_.get(r_) or ('', ''))[1]
    ef_ok = h_(ef_, 'refs/heads/main') == h_(ef_, 'refs/remotes/origin/main') == K.EF_BASE == K.EF_MAIN \
        and all(h_(ef_, 'refs/heads/' + b) == t == h_(ef_, 'refs/remotes/origin/' + b) for b, t in K.EF_BRANCHES) and K.ZQ_TIP == K.ZQ_ENTERING \
        and all(h_(ef_, 'refs/heads/' + b).startswith(t) and h_(ef_, 'refs/remotes/origin/' + b) == h_(ef_, 'refs/heads/' + b) for b, t in (K.JOIN_BRANCH, K.COEFF_BRANCH)) \
        and h_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[1] and p_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[2] \
        and not [r for r in ef_ if re.match(r'^refs/tags/v0\.(39|[4-9]\d)', r)]
    kc_ = all(((('refs/heads/%s' % b) in ct_.get(k, [])) if b and b != 'main' else (('refs/remotes/origin/main' in ct_.get(k, [])) if b == 'main' else ct_.get(k) == []))
              for k, _kn, _c, b in K.KERNEL_COMMITS) and len(K.KERNEL_COMMITS) == 16
    m4_ok = h_(m4_, 'refs/remotes/origin/main').startswith(K.M24_MAIN) and h_(m4_, 'refs/heads/main')[:8] in (K.M24_BASE[:8], K.M24_MAIN[:8]) \
        and h_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[1]) and p_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[2]) \
        and p_(m4_, 'refs/tags/v0.1.0').startswith(K.M24_BASE) and sorted(r for r in m4_ if r.startswith('refs/tags/')) == ['refs/tags/v0.1.0', 'refs/tags/v0.2.0']
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
    arm list since b757's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R368)(8)-(10), N1, N3 (the name the frozen run list carries): the counts the entry and the root prompt carry, each read from its
    bank -- the notes bank's five items (a) to (e) in the ruling's order, each at its file and confirmed at its PLACE-papers commit with none
    removed, the worklist's count 5; the cites (a)'s insertion moves, 134 lines and 231 cites, none edited; the sweep's 24 lines, none
    unread; the five repairs each by its foot ((i) the cut, (ii) v1.35.5, (iii) the gh-call reader, (iv) REGISTRY's line, (v) the doors, the
    two descriptions sent and each read back equal); the dispatches by their rows, 6 in SIDE-explicit-formula of 14 and 2 in
    SIDE-dirichlet-mod-24 of 4, each run the worklist's and read once after its dispatch; b746's draft unchanged; no Zenodo tool this act."""
    nj_ = (S['notesj'] or {}).get('items') or {}
    notes_ = list(nj_) == ['a', 'b', 'c', 'd', 'e'] and all(
        (nj_.get(it_.strip('()')) or {}).get('file') == f_ and (nj_[it_.strip('()')].get('confirm') or '').startswith('PLACE-papers %s at ' % c_[:8])
        and 'none removed' in nj_[it_.strip('()')]['confirm'] for it_, f_, c_ in K.C3_NOTES_PP) and len(K.C3_NOTES_PP) == K.C3_NOTES_WRITTEN == 5
    moved_ = _vlast(_txt(rd('b758_notes_moved.txt'))) == 'THE CITES THE INSERTION MOVES: LINES 134 (PLACE-papers 11, relay 123) ; CITES MOVED 231 ; NONE EDITED, EACH PRINTED.'
    sweep_ = ' ; LINES SAYING ONE OF THE THREE STATEMENTS 24: ' in _vlast(_txt(rd('b758_sweep.txt'))) and ' ; NOT YET READ 0 ; ' in _vlast(_txt(rd('b758_sweep.txt')))
    rep_ = [_vlast(_txt(rd('b758_cut.txt'))).startswith('(8)(i): CONTROLS 4 OF 4 AS WANTED ;'),
            _vlast(_txt(rd('b758_standing_v1355.txt'))).endswith(' ; CASES 6 ; AS WANTED 6 ; ALL AS WANTED.'),
            _vlast(_txt(rd('b758_ghcalls.txt'))).endswith('THE CARRIED READER NONE, THE TAUGHT READER 2.'),
            _vlast(_txt(rd('b758_registry_line.txt'))).startswith('(8)(iv): CONTROLS 2 OF 2 AS WANTED ; LINE 13 REPLACED ; LINES MOVED 0 ;'),
            ' ; SENT 2 OF 2 (EDIT CALLS 2) ; READ BACK EQUAL TO THE PASSED TEXT 2 OF 2 ' in _vlast(_txt(S['doors']))]
    rows_ = S['drows'] or []
    ds_ = [r_ for r_ in rows_ if r_.get('kind') == 'dispatch']
    def _runs(kn_):
        return [int(r_.get('run')) for r_ in ds_ if r_.get('kernel') == kn_]
    rd1_ = all(sum(1 for x_ in rows_ if x_.get('kind') == 'read' and str(x_.get('run')) == str(d_.get('run'))) == 1
               and rows_.index(d_) < next(i_ for i_, x_ in enumerate(rows_) if x_.get('kind') == 'read' and str(x_.get('run')) == str(d_.get('run'))) for d_ in ds_)
    # ### b758 step zero: the dispatch term read against (R368)(10)'s caps and rewritten to them (1 to 4 in SIDE-explicit-formula, none in
    # ### SIDE-dirichlet-mod-24); the notes, moved-cites, sweep and repairs terms above are b757's and are rewritten for (R368)(7)-(9) at Component 5
    disp_ = _runs('SIDE-explicit-formula') == list(K.EF_RUNS) and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES == 4 \
        and _runs('SIDE-dirichlet-mod-24') == list(K.M24_RUNS) == [] and K.MAX_DISPATCHES_M24 == 0 and len(ds_) == len(K.EF_RUNS) and rd1_
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b758_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return notes_ and moved_ and sweep_ and all(rep_) and disp_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b758_steps.json', 'data/b758_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

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
    """standing clauses v9 (Component 6 of (R368): the close "as the standing clauses order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b758_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b757's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R368-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b757's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R368) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b757's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 38024feb; not run at b758, its rows computing at a field, which (R368)(10) bars, the builds apart; declared failing on the face',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 94 = 94 OK + 0 misses, the check HALTED on one Lean-path row (halts 1) and the halt read by hand in the step-zero bank before the deletes (defect (c)), as that bank enters it after the act_current commit and the subject read; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b757-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b758: the tip removed from "(was b19867ac, 12:56:12Z)" and the four after it (data/b758_stepzero.txt :66-:67); the carried plant wanted the tip closed by its paren and mutated nothing (the probe's VAC)
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 6 order adjusted to what the act did: the build under (R368); the join broken at the import, no tag cut; T0 and T1 compiled on push-b758-coeff at their commits; the modulus-24 module compiled under v0.2.0; the wide direction compiled at 596d1c9e; 8 dispatches, 6 and 2; the five repairs, 5 landed; the notes of (9), 5 written; each object`s bank in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R368)(1): the generated corrigendum for b757`s record, short, landed at FINDINGS :15416: b757`s 37 events and 11 defects by count from their banks, 48 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 1 CLOSE 47, REPEAT 33, its one CLAIM item in full; the seven findings the seat printed after b757`s lock entered as events (7)-(13), CLAIM 1 CLOSE 6 REPEAT 5, with the navigator`s correction to (F6); the corrigenda bank appended at row (77)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R367)(2), data/b757_rules.txt`s rows (a) to (c), in force from b758, in b757`s commit 0a151012 and no other, the working tree its blob at HEAD; no rules bank of b758`s, (R368) ordering none',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b758's objects
    ('G-REGISTRATIONS-FIRST', '(R368)(1), (8)(iv), (9), N5: PLACE-papers written by the worklist`s chain in its order and by nothing else before the record -- the weight line and the corrigendum in one commit touching FINDINGS alone (810ec2da), the act`s first on its base; REGISTRY`s header replaced in place under (8)(iv), one line for one (3e85e952), the registry-line bank reading LINES MOVED 0; the five notes of (9) each touching its one file (e88282c4, c7dfe43c, 9c0896c5, c45be6e0, b14256c2), the notes bank`s confirm naming each with none removed; the changed files within the act`s list; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('SPIRAL_MAP.md'))),   # ### b758: a file outside the list (REGISTRY.md, b757's plant, is in b758's)
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b758_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R368)(1)-(9), N2, N4: the act`s order by time across the relay and PLACE-papers -- the act_current commit and step zero`s banks, the c1 route, the weight and corrigendum, v1.35.4 and its live control before any kernel write, the controls tool before its opening dispatch, the join`s tools before its bank, the composer of the outcomes before its banks, the ceiling, (8)(iv)`s tool before its write, the doors and the gh-call reader, v1.35.5, the sweep, the cut, the tool of the notes before its five writes and its bank, then the lock gate and the handoff page -- and by ancestry within the relay; each of the two standing versions` banks ALL AS WANTED at its cases in its own commit with VERSION moved; the act`s commits under tools/standing/ those two alone',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update({next(iter(d), 'none'): False}))),   # ### b758: the first pair of the chain's ancestry set False (b757's planted key stood in no state of b758's)
    ('G-DERIVATION-GRADED', '(R368)(3)-(9), N2, N3: each of the act`s ten tools first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; no tool committed with its bank; the outcomes bank`s foot JOIN BROKE, T0, T1, MOD24 and WIDE COMPILED; the join`s, the cut`s, the sweep`s, the gh-call reader`s and the doors` feet; the ceiling after Component 3 at HEAD its blob, nothing carried',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'ceiling', ((S['ceiling'] or (None, None))[0], 'planted'))),
    ('G-OFFSET-POST-HOC', 'N5, (R368)(3)-(7), (10): the two kernels as the build left them -- SIDE-explicit-formula`s main at 8fbab45d locally and at origin (the join broke), its four held branches at their tips, push-b758-join at 6568e9c7 and push-b758-coeff at 596d1c9e each equal to origin, each kernel commit on its branch and the two live controls on none, v0.38 peeling to 14ca5725 and no tag past it; SIDE-dirichlet-mod-24`s main at e5ebdd15 at origin, v0.2.0 peeling to it, v0.1.0 at 597b0869 and no other tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'kst', lambda d: d['ef'].update({'refs/tags/v0.39': ('0' * 40, K.EF_BASE)}))),   # ### b758: a v0.39 planted beside v0.38
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R368)(8)-(10), N1, N3: the counts read from their banks -- the notes of (9) five, (a) to (e), each at its file and confirmed at its commit with none removed; the cites the insertion moves 134 lines and 231 cites, none edited; the sweep`s 24 lines, none unread; the five repairs each by its foot, the two descriptions sent and read back equal; the dispatches 6 of 14 and 2 of 4 by their rows, each read once after it; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'notesj', lambda d: (d.get('items') or {}).pop('e', None))),   # ### b758: the trail's note (e) dropped from the notes bank
    ('G-DIFFERS-ERRATA', '(R368)(1), (10): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line and the corrigendum in 810ec2da, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b758_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R368-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal to its blob at the act`s base 38024feb (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R368)(10): every dispatch a row with its kernel and its free memory at or above the hold, the run ids the worklist`s, 6 in SIDE-explicit-formula of 14 and 2 in SIDE-dirichlet-mod-24 of 4, each read once after it by its id; the plant a dispatch with no kernel and no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4, (R368)(10): one dispatch command in the capture for each dispatch row, 8 (6 and 2, within 14 and 4), each read once after it, every row`s free memory at or above the hold; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no merge onto a kernel`s main this act (the join`s four merges on push-b758-join, off main, read by G-OFFSET-POST-HOC): each repaired wave 1 kernel`s rebuild-b721 as b757 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b758 found it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: (9)`s block with (1)`s line, and the trail; REGISTRY: (8)(iv)`s line and (9)(d)`s note; FACES_LEDGER: (9)(b)`s section; the Epstein document and the census: (9)(a)`s and (c)`s notes; (R368)(1), (8)(iv), (9), (10)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    (_ for _ in ()).throw(SystemExit('### b758`s a block reading an act ordinal or the read-first needles (SECTION checks 60) IS A CARRIED STUB (tools/standing/carry.py v1.34.0), ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED: written for the act before use -- NOTHING COMPOSED')),
    ('G-PRIOR-CLOSED-PUSHED', 'b757`s trail record on OPEN_TRAILS (:18422) and its root in the chain', lambda S: '### b757 — lane two, act one hundred and eighty-three, the clearing act under (R367)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS, REGISTRY, FACES_LEDGER, and the Epstein document and the census of (9)(a) and (c)): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved; v0.38, the two push-b758 branches and SIDE-dirichlet-mod-24 read by G-OFFSET-POST-HOC) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: 8 by the dispatch rows, 6 in SIDE-explicit-formula and 2 in SIDE-dirichlet-mod-24; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b758, (R368)(1): Component 1's PLACE-papers commit carries the weight line and the corrigendum in FINDINGS alone (810ec2da); (1)'s
# ### dated line stands in (9)'s block in OPEN_TRAILS (b14256c2)
#⟪OVERRIDE checks MARK e92df47c9946 1⟫
        and K.DIFFERS_LINE is None and K.ERRATA_LINE is None and K.ERRATA_ID is None and S['files']['c1pp'] == ['FINDINGS.md'] \
#⟪END⟫
# ### (carried; b758 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b757's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b758: (R368)'s rows, written at step zero in place of b757's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch facts758.py, read-only). A place is named by its role or its
    # ### file name, never by a folder of the host (N5); the PLACE-papers lines these rows read stand at no place of [Q]'s row (3) (the masking
    # ### reader printed each whole). b757 left no closing bank (it stopped at [22]): `cl` reads empty and no row reads it. The relay tools the
    # ### act repairs are read at the act's start (K.PRE_RELAY), and the kernel at its commits, so a later run reads the same text.
    import hashlib as _h
    EF_ = 'D:/SIDE-explicit-formula'
    MOD_ = 'D:/SIDE-dirichlet-mod-24'
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling SCOPE', 'relay main at the act`s start ff65ccdb, b757`s record push, read back at the remote (or an ancestor of the remote`s main)',
        gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('ff65ccdb') and bool(rm) and gr('D:/relay', 'merge-base', 'ff65ccdb', rm).startswith('ff65ccdb'), 'remote main %s' % rm[:8], '0')
    npp_, tpp_ = gr(PP, 'rev-list', '--count', K.PRE_PP), gr(PP, 'tag', '--list').split()
    add('ruling SCOPE', 'PLACE-papers main at the act`s start b8c0bd73: 2,176 commits and 2 tags there', gr(PP, 'rev-parse', K.PRE_PP).startswith('b8c0bd73') and npp_ == '2176' and len(tpp_) == 2,
        '%s ; %s commits ; %d tags' % (K.PRE_PP[:8], npp_, len(tpp_)), '0')
    tip_ = lambda r_, c_: (gr(EF_, 'rev-parse', '--verify', '--quiet', r_) or c_).startswith(c_)   # noqa: E731  ### a branch deleted after (5) read as its commit
    add('ruling SCOPE, (4), (5), (10)', 'SIDE-explicit-formula: main 8fbab45d at the act`s start; push-b757-join at 6568e9c7 and push-b757-coeff at 596d1c9e at the remote; v0.38 the tag object 21c6edaf peeling to 14ca5725',
        gr(EF_, 'rev-parse', K.EF_BASE).startswith('8fbab45d') and tip_('origin/push-b757-join', '6568e9c7') and tip_('origin/push-b757-coeff', '596d1c9e')
        and gr(EF_, 'rev-parse', 'v0.38').startswith('21c6edaf') and gr(EF_, 'rev-parse', 'v0.38^{commit}').startswith('14ca5725'),
        'main %s ; v0.38 peel %s' % (gr(EF_, 'rev-parse', '--short=8', 'origin/main'), gr(EF_, 'rev-parse', 'v0.38^{commit}')[:8]), '2')
    add('ruling SCOPE, (6)(i), (10)', 'SIDE-dirichlet-mod-24: the remote`s main e5ebdd15 with v0.2.0, the tag object e5c84316, peeling to it; the local main at 597b0869 (or moved to e5ebdd15), an ancestor of the remote`s',
        gr(MOD_, 'rev-parse', 'v0.2.0').startswith('e5c84316') and gr(MOD_, 'rev-parse', 'v0.2.0^{commit}').startswith('e5ebdd15') and gr(MOD_, 'rev-parse', 'origin/main').startswith('e5ebdd15')
        and gr(MOD_, 'merge-base', '597b0869', 'e5ebdd15').startswith('597b0869') and gr(MOD_, 'rev-parse', 'main')[:8] in ('597b0869', 'e5ebdd15'),
        'local main %s ; remote main %s ; v0.2.0 peel %s' % (gr(MOD_, 'rev-parse', '--short=8', 'main'), gr(MOD_, 'rev-parse', '--short=8', 'origin/main'), gr(MOD_, 'rev-parse', 'v0.2.0^{commit}')[:8]), '4')
    add('ruling SCOPE', 'SIDEDirichletMod24/Units.lean :61 at e5ebdd15, units24_iso_signs', _decl_line(_blob(MOD_, 'e5ebdd15', 'SIDEDirichletMod24/Units.lean'), 'units24_iso_signs') == 61, 'present', '4')
    # ### (R368)(1): b757 at its weight and its close
    aw_ = lines_of(p('data', 'b757_author_words.txt'))
    add('ruling (1)', 'data/b757_author_words.txt :2-:3, the author`s word of 2026-11-16T23:02:40Z: stop at [22], carry the rest',
        '2026-11-16T23:02:40Z' in at(aw_, 2) and at(aw_, 3).rstrip() == 'Stop at [22], carry the rest (Recommended)', at(aw_, 3)[:44], '1')
    oc_ = lines_of(p('data', 'b757_outcomes.txt'))
    add('ruling (1), (5)', 'data/b757_outcomes.txt :132, the outcomes` foot (the join broke; T0, T1, the modulus-24 module and the wide direction compiled); :30, :71-:72, :124-:125, the five names of (5), each within the standard three',
        at(oc_, 132).rstrip() == '### ### **THE OUTCOMES: JOIN BROKE ; T0 COMPILED ; T1 COMPILED ; MOD24 COMPILED ; WIDE COMPILED.**'
        and all(at(oc_, n_).split()[:1] == ['SIDEExplicitFormula.Schema.%s' % q_] and at(oc_, n_).rstrip().endswith('[propext, Classical.choice, Quot.sound]')
                for n_, q_ in ((30, 'ZQ.zq_coeff_not_multiplicative'), (71, 'ZQ.cQ_forty_eight'), (72, 'ZQ.cQ_not_nonneg'), (124, 'Wide.wide_detector'), (125, 'ZQ.zq_arith_side_re_neg'))),
        '%d lines' % (len(oc_) - 1), '1')
    ac_ = _blob('D:/relay', K.PRE_RELAY, 'tools/standing/act.py').replace(chr(13), '').split(NL)
    rc_ = _blob('D:/relay', K.PRE_RELAY, 'tools/b652_record.py').replace(chr(13), '').split(NL)
    add('ruling (1)', 'tools/standing/act.py :82 at the act`s start, landed_entry comparing the FINDINGS line with the bank`s head unconverted; tools/b652_record.py :34-:36, conv, THE ONE CONVERSION',
        "lines[i].rstrip() != (fj.get('head') or fj.get('title') or '').rstrip()" in at(ac_, 82) and at(rc_, 34) == 'def conv(t):' and 'THE ONE CONVERSION' in at(rc_, 35)
        and 'Every landing and every look-up of a landed line goes through this function.' in at(rc_, 36), '%d ; %d lines' % (len(ac_), len(rc_)), '1')
    add('ruling (1)', 'OPEN_TRAILS :18553, b757`s scores line: N3 REFUTED, S1 and S2 PENDING, the readings (1) closes from the banks', 'N3 REFUTED' in at(ot, 18553) and 'S1 PENDING · S2 PENDING' in at(ot, 18553),
        at(ot, 18553)[:60], '1')
    e7_ = lines_of(p('data', 'b757_events.txt'))
    add('ruling (6), SCOPE', 'data/b757_events.txt :141-:142 and :399-:400, the two routes the seat lacked at b757: a push of a commit to a named branch (zq-b730) and a fast-forward of a kernel`s local main',
        'THE ROUTE IT LACKS is a push of' in at(e7_, 141) and "push-b757-coeff's tip to refs/heads/zq-b730, never forced, read back." in at(e7_, 142)
        and "THE ROUTE IT LACKS is a fast-forward of a kernel's local main to its remote's main," in at(e7_, 399) and at(e7_, 400).lstrip().startswith('read back, the class (18) named for zq-b730.'),
        'present', '4')
    # ### (R368)(4): the join landed
    tm_ = _blob(EF_, '6568e9c7', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Time.lean').replace(chr(13), '').split(NL)
    sm_ = _blob(EF_, '6568e9c7', 'SIDEExplicitFormula/Schema/ZQ/OffZero/Sums.lean').replace(chr(13), '').split(NL)
    DEF_ = 'def sRe (r wr wi : ℚ) : ℕ → ℚ'
    su_ = [k_ + 1 for k_, l_ in enumerate(tm_) if re.search(r'\bsRe\b', l_)]
    add('ruling (4), SCOPE', 'at 6568e9c7: Schema/ZQ/OffZero/Time.lean :18 and Sums.lean :134, each `def sRe`, Time`s in namespace SIDEExplicitFormula.Schema.ZQ.OffZero (:12-:15); Time`s uses of the name at :18, :20, :25, :26',
        at(tm_, 18) == DEF_ and at(sm_, 134) == DEF_ and [at(tm_, n_) for n_ in (12, 13, 14, 15)] == ['namespace SIDEExplicitFormula', 'namespace Schema', 'namespace ZQ', 'namespace OffZero'] and su_ == [18, 20, 25, 26],
        'uses %s' % su_, '2')
    bm_ = _blob(EF_, '6568e9c7', '.github/workflows/build-module.yml').replace(chr(13), '').split(NL)
    pt_ = _blob(EF_, '6568e9c7', 'print_targets.txt').replace(chr(13), '').split(NL)
    add('ruling (4), SCOPE', 'build-module.yml :86-:95, the print step, its filter at :91 passing A-Z in both cases, digits, underscore, full stop and the prime; print_targets.txt :358-:359 at 6568e9c7, each name carrying the Greek capital lambda; 419 lines',
        at(bm_, 86).strip() == 'cp print_targets.txt out/print_targets.txt' and at(bm_, 91).strip().startswith('*[!A-Za-z0-9_.' + chr(92) + chr(39) + ']*) echo "print target refused: $n"')
        and at(pt_, 358) == 'SIDEExplicitFormula.Schema.ZQ.zqPair_\u039b_one_sub' and at(pt_, 359) == 'SIDEExplicitFormula.Schema.ZQ.zqPair_\u039b_eq_of_re' and len([l_ for l_ in pt_ if l_.strip()]) == 419,
        '%d lines in print_targets.txt' % len([l_ for l_ in pt_ if l_.strip()]), '2')
    # ### (R368)(5): the three results landed
    mf_ = gr(EF_, 'diff', '--name-only', '1e658870', '596d1c9e').split()
    add('ruling (5), (6)(ii)', 'push-b757-coeff`s tip 596d1c9e forks from 6568e9c7 at zq-b730`s tip 1e658870, zq-b730 standing there; past that tip it changes four Lean files and print_targets.txt, 443 lines at 596d1c9e',
        gr(EF_, 'merge-base', '6568e9c7', '596d1c9e').startswith('1e658870') and gr(EF_, 'rev-parse', 'zq-b730').startswith('1e658870')
        and mf_ == ['SIDEExplicitFormula/Schema/Wide/HalfScale.lean', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean',
                    'SIDEExplicitFormula/Schema/ZQ/Mechanism/NoEuler.lean', 'print_targets.txt']
        and len([l_ for l_ in _blob(EF_, '596d1c9e', 'print_targets.txt').split(NL) if l_.strip()]) == 443, '%d files' % len(mf_), '3')
    # ### (R368)(7): the fourteen names, each at its file and line at 596d1c9e
    D7_ = (('zq_offline_zero', 'SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 32), ('zq_count_instance', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean', 194),
           ('zq_explicitFormula', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean', 25), ('zq_explicit_formula_instance', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean', 198),
           ('zq_premises', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean', 190), ('rQ_one', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 56),
           ('zq_coeff_not_multiplicative', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/NoEuler.lean', 99), ('cQ_eq', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 71),
           ('cQ_four', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 240), ('cQ_six', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 247),
           ('cQ_forty_eight', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 281), ('cQ_not_nonneg', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 291),
           ('wide_detector', 'SIDEExplicitFormula/Schema/Wide/HalfScale.lean', 277), ('zq_arith_side_re_neg', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean', 26))
    d7_ = [(n_, _decl_files(EF_, '596d1c9e', n_), _decl_line(_blob(EF_, '596d1c9e', f_), n_)) for n_, f_, _l in D7_]
    add('ruling (7), (5)', 'the fourteen names of (7) at 596d1c9e, each declared in one file at the line read at step zero (the statements bank`s source where (5) does not land)',
        len(D7_) == 14 and all(fs_ == [f_] and l_ == w_ for (_n, fs_, l_), (_m, f_, w_) in zip(d7_, D7_)), ' '.join('%s:%d' % (n_, l_) for n_, _f, l_ in d7_)[:90], '5')
    # ### (R368)(6): G-TRAIL-CARRIES-SEAL at the act's start
    ck_ = _blob('D:/relay', K.PRE_RELAY, 'tools/standing/fold/checks.tpl').replace(chr(13), '').split(NL)
    add('ruling (6)', 'tools/standing/fold/checks.tpl :1853 at the act`s start, G-TRAIL-CARRIES-SEAL reading the worklist`s K.SEALED, not the trail bank',
        at(ck_, 1853).lstrip().startswith("('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),"),
        at(ck_, 1853).strip()[:50], '4')
    # ### (R368)(7), (8): the places in PLACE-papers
    ep_ = lines_of(os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'))
    add('ruling (7), (8)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md: its latest dated note b757`s at :17; the heads of §6 to §8 at :218, :220 and :222, §9 at :224',
        at(ep_, 17).startswith('*Dated note, 2026-11-16, b757, under the author’s ruling `(R367)`(9)(a):') and at(ep_, 218).startswith('## 6. The corollary and what it says')
        and at(ep_, 220).startswith('## 7. The cost law') and at(ep_, 222).startswith('## 8. Class number one') and at(ep_, 224).startswith('## 9. Back matter'), '%d lines' % (len(ep_) - 1), '5')
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    kc_ = lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))
    rg2_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (8)', 'each file`s end where (8)`s notes go: FACES_LEDGER.md :563 (b757`s filing line), THE_KEYSTONE_CENSUS_v0_8_3.md :1570 (b757`s note), REGISTRY :1250 (b757`s dated note), OPEN_TRAILS :18555 (b757`s Next line)',
        at(fl_, 563).startswith('*The rows above are unedited. Filed by b757') and at(kc_, 1570).startswith("*Appended 2026-11-16 by b757 under the author's ruling `(R367)`(9)(c):*")
        and at(rg2_, 1250).startswith("*Dated note, b757, 2026-11-16, under the author's ruling `(R367)`(9)(d),") and at(ot, 18555).startswith('**Next:** the act after this one, as the author answers at the root')
        and not any(l_.strip() for L_, n_ in ((fl_, 563), (kc_, 1570), (rg2_, 1250), (ot, 18555)) for l_ in L_[n_:]),
        '%d ; %d ; %d ; %d lines' % (len(fl_) - 1, len(kc_) - 1, len(rg2_) - 1, len(ot) - 1), '5')
    add('ruling (8)', 'REGISTRY :177-:179, the rows 1.5c-21 to 1.5c-23, and :924, SIDE-explicit-formula`s kernel row', at(rg2_, 177).startswith('| 1.5c-21 |') and at(rg2_, 178).startswith('| 1.5c-22 |')
        and at(rg2_, 179).startswith('| 1.5c-23 |') and at(rg2_, 924).startswith('| **`SIDE-explicit-formula`**'), 'present', '5')
    add('ruling (8)', 'OPEN_TRAILS :18503, W-ORD-SQUARES-AT-24 entered at b757 under (R367)(6), the order (8) prices', at(ot, 18503).startswith('`W-ORD-SQUARES-AT-24` ENTERED under `(R367)`(6)'), at(ot, 18503)[:40], '5')
    mv_ = lines_of(p('data', 'b757_notes_moved.txt'))
    add('ruling (8)', 'data/b757_notes_moved.txt :140, the cites b757`s Epstein note moved: 134 lines, 123 of them the relay`s, none edited',
        at(mv_, 140).rstrip() == '### ### **THE CITES THE INSERTION MOVES: LINES 134 (PLACE-papers 11, relay 123) ; CITES MOVED 231 ; NONE EDITED, EACH PRINTED.**', at(mv_, 140)[:60], '5')
#⟪END⟫
#⟪SECTION citation 2⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 3⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b758 step zero: (R368)(1)'s counts over b757's banks, written in place of b757's rows over b756's; each tag read as the bank tags it,
    # ### an owner of more than one word read whole; no post-seal events bank and no closing bank at b757 (it stopped at [22]); one CLAIM row in
    # ### each bank: events (13), THE TOOL'S, b756's post-lock finding entered by b757, and defects (v), the item (R368)(1) names in full
    add('ruling (1), ferry (read first)', 'b757`s events (1)-(46) and its 28 lettered defects (a)-(b`), no post-seal events bank (data/b757_events.txt, data/b757_defects.txt)',
        starts == list(range(1, 47)) and len(letters) == 28 and letters[-1] == "b'" and not os.path.exists(p('data', 'b757_events_postseal.txt')),
        'events %s ; letters %d (%s-%s) ; post-seal %s' % (starts[-1:], len(letters), letters[:1], letters[-1:], 'absent' if not os.path.exists(p('data', 'b757_events_postseal.txt')) else 'PRESENT'), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_, nt_, ncl_, ncs_ in (('data/b757_events.txt', ev, 46, 46, 1, 45), ('data/b757_defects.txt', dl, 28, 28, 1, 27)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_.group(2) for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        add('ruling (1), ferry (read first)', '%s: %d rows, %d tagged by the reader`s owner form; CLAIM %d, CLOSE %d' % (f_, nr_, nt_, ncl_, ncs_),
            len(rr_) == nr_ and len(tg_) == nt_ and tg_.count('CLAIM') == ncl_ and tg_.count('CLOSE') == ncs_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d' % (len(rr_), len(tg_), tg_.count('CLAIM'), tg_.count('CLOSE')), '1')
    add('ruling (1), (9)', 'the CLAIM rows: data/b757_defects.txt :35, (v) THE SEAT`S [CLAIM ; NEW], the item (1) names, in full; data/b757_events.txt :88, (13) THE TOOL`S [CLAIM ; NEW], b756`s post-lock finding entered by b757',
        at(dl, 35).startswith("    (v) THE SEAT'S [CLAIM ; NEW]: Component 6, (R367)(9)'s sweep:") and at(ev, 88).startswith("    (13) THE TOOL'S [CLAIM ; NEW]:"), 'defects :35 ; events :88', '1')
    add('ruling (2), (4)', 'data/b757_defects.txt :25, (l), the two reads before the join`s send; :38, (y), the flag reader that printed STOP and did not stop',
        at(dl, 25).startswith("    (l) THE SEAT'S [CLOSE ; NEW]: Component 2: TWO READS BEFORE THE JOIN'S SEND") and at(dl, 38).startswith("    (y) THE SEAT'S [CLOSE ; NEW]: A ROUTE RUN AFTER THE FLAG READ PRINTED STOP."),
        'present', '0')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'FINDINGS :%d, b757`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## The build under (R367): the join of SIDE-explicit-formula’s four held branches broken at SIDEExplicitFormula.Schema.ZQ.OffZero.Time :18, no tag cut'),
        at(fi, K.B711_ENTRY)[:50], '1')
    add('ruling (1)', 'FINDINGS :%d and :%d, b756`s weight line and corrigendum (b757`s), the form b758`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM),
        at(fi, K.B711_WEIGHT).startswith('*Appended 2026-11-16 by b757 to b756’s entry (:15370)') and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b756’s record, short'), at(fi, K.B711_WEIGHT)[:40], '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b757`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b757 — lane two, act one hundred and eighty-four, the build under (R367)'), at(ot, K.B711_TRAIL)[:50], '1')
    add('ruling (1)', 'OPEN_TRAILS :%d, b757`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '1')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula and SIDE-dirichlet-mod-24, the two kernels this act opens', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-dirichlet-mod-24/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.35.5 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.35.5',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### (R368) SCOPE: no mirror built at b757; b756's the last, by its file name and hash, the folder that holds it not printed (N5)
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    m7_ = sorted(f_ for f_ in os.listdir(os.path.dirname(K.MIRROR_ZIP)) if f_.startswith('mirror-refresh') and 'b757' in f_) if os.path.isdir(os.path.dirname(K.MIRROR_ZIP)) else ['UNREAD']
    add('ruling SCOPE, (1)', 'no mirror built at b757: none named for it beside b756`s %s (sha256 %s), the last built' % (os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest()[:8]), bool(mz_) and m7_ == [],
        'b757 zips %d' % len(m7_), '1')
    # ### PATHS: the clones at the paths the worklist holds, counted; one absent printed by its name alone
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R368)(4), (6)(i): the two kernels' clones before any kernel write, clean; SIDE-dirichlet-mod-24 left at b757 on push-b757-mod24, whose tree is the remote main's
    kc2_ = [(os.path.basename(r_), gr(r_, 'rev-parse', '--abbrev-ref', 'HEAD'), gr(r_, 'status', '--porcelain')) for r_ in ('D:/SIDE-explicit-formula', 'D:/SIDE-dirichlet-mod-24')]
    add('ruling (4), (6)(i)', 'the two kernels` clones with nothing changed or staged before any kernel write: SIDE-explicit-formula on main, SIDE-dirichlet-mod-24 on push-b757-mod24 as b757 left it',
        [h_ for _n, h_, _s in kc2_] == ['main', 'push-b757-mod24'] and not any(s_ for _n, _h, s_ in kc2_), ' ; '.join('%s %s %s' % (n_, h_, 'clean' if not s_ else 'CHANGED') for n_, h_, s_ in kc2_), '0')
#⟪END⟫
#⟪SECTION citation 6⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (2)', 'the push-b757-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R368)(2): act_current alone, then b757's carried files, each group alone, in the worklist's order (K.STEPZERO_CARRIED); each commit
    # ### read for its files: the files named, or for the two suite groups each file a b757 bank of its kind, at the count the commit's words give
    KIND_ = {'a44f2c06': (27, r'data/b757_(checks_postpush|chain_half_\w+_checks_postpush|lsr_postpush)'), '59a3244b': (11, r'data/b757_exercise')}
    WANT_ = {'b8ea1f01': ['data/b757_PLACE-papers_push-b757-record_push_out.txt', 'data/b757_relay_push-b757-record_push_out.txt'],
             '776cf191': ['data/b757_put_3.json'], '9869af85': ['data/b757_author_words.txt'], '2672f85d': ['data/b757_address_scan_commits.txt'],
             '41ff314d': ['data/b757_hook_refusals.txt']}
    if not K.ACT_CURRENT_COMMIT:
        add('ruling (2)', 'data/act_current.json -- TO BE COMMITTED at step zero', False, 'NOT COMMITTED', '0')
    else:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', K.ACT_CURRENT_COMMIT).split()
        add('ruling (2)', 'data/act_current.json committed alone at %s, an ancestor of HEAD' % K.ACT_CURRENT_COMMIT, nm_ == ['data/act_current.json']
            and gr('D:/relay', 'merge-base', K.ACT_CURRENT_COMMIT, 'HEAD').startswith(K.ACT_CURRENT_COMMIT), ' '.join(nm_)[:90], '0')
    for c_, s_, w_ in K.STEPZERO_CARRIED:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        ok_ = sorted(nm_) == sorted(WANT_[c_]) if c_ in WANT_ else (c_ in KIND_ and len(nm_) == KIND_[c_][0] and all(re.match(KIND_[c_][1], f_) for f_ in nm_))
        add('ruling (2)', 'b757`s carried files, %s, committed alone at %s (step %d), an ancestor of HEAD' % (w_, c_, s_), ok_ and gr('D:/relay', 'merge-base', c_, 'HEAD').startswith(c_),
            '%d files' % len(nm_), '0')
    left_ = gr('D:/relay', 'status', '--porcelain', '--', *(f_ for fs_ in WANT_.values() for f_ in fs_))
    add('ruling (2)', 'the files b757 left uncommitted clean at HEAD after their commits (each scan and refusal of b758 appended to b758`s own banks)', not left_, left_.replace(NL, ' | ') or 'clean', '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (5), (10)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (10)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (1)', 'tools/mirror_prevbuild.json, the builder`s state file [23] reads', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '1')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (2), ferry (read first)', 'data/b758_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b758_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b758_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 5) are the corrigendum with b757's close and the seat's read of what the ruling misses, the seven standing changes (the
reader's repair, the bound, the title rule, the kernel route, the two routes of (6), the arm and the face, each by its controls bank), the
landing ((4)'s pre-send reads, its branch, the controls tool's own controls, every dispatch and its read, the outcomes), the three results
((5)'s merge and union), the ceiling's readings, the statements bank of (7), the notes of (8) (the five confirms and the moved cites), the
name and address scan, the reproduction not run (declared on the face), the touch read of v9 and the standing arms, each row by its bank's
verdict line or by the line its pattern names (section_reading);
(R368)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section;
the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next
act ((R368)(10)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act, as (R368)(10) opens them: SIDE-explicit-formula's tree on push-b758-land
((4)'s one commit, the rename) and push-b758-coeff ((5)'s merge of 596d1c9e, print_targets.txt the union), main moved by the gated push's
default mode after each run's success alone, each tag cut at main's read-back, as relay data/b758_outcomes.txt reads them; the two local mains
fast-forwarded by (6)(i)'s route, SIDE-dirichlet-mod-24's to e5ebdd15 and SIDE-explicit-formula's to each landing (relay data/b758_events.txt
(38), (47)).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for the act after b758 ((R368)(10) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R365)(2)(iv)(c): the outbound sentence from the one clause
# ### b758, Component 5: (4)'s and (5)'s outcomes read from their bank at import, for the title and the kernel lines
_OC5 = dict((r_.get('item'), r_) for r_ in (jl('b758_outcomes.json') or []) if isinstance(r_, dict))
_OW5 = lambda k_: (_OC5.get(k_) or {}).get('outcome') or 'NOT READ'
_LT5 = [(_OC5[k_].get('tag'), (_OC5[k_].get('peel') or '')[:8]) for k_ in ('join', 'coeff') if _OW5(k_) == 'LANDED']
TITLE_LINE = ('b758 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTY-FIVE, THE LANDING: b757 CLOSED BY ITS CARRIED STEPS; %s; %s; '
              'TWO ROUTES; %s; UNDER (R368).**' % (
                  'THE JOIN LANDED AT v0.39' if _OW5('join') == 'LANDED' else 'THE JOIN BROKEN, NO TAG CUT',
                  'T0, T1 AND THE WIDE DIRECTION LANDED AT v0.40' if _OW5('coeff') == 'LANDED' else (
                      'T0, T1 AND THE WIDE DIRECTION ON THEIR BRANCH' if _OW5('coeff') == 'BROKE' else 'T0, T1 AND THE WIDE DIRECTION NOT MERGED'),
                  'THE STATEMENTS BANKED' if rd('b758_epstein_statements.txt') else 'THE STATEMENTS CARRIED'))   # ### the ferry`s ACT line (data/b758_ferry.txt :33) adjusted to what the act did
_K5_MAIN = ('moved to %s' % ' and then to '.join('%s, %s cut at its read-back' % (p_, t_) for t_, p_ in _LT5)) if _LT5 else 'unmoved, no tag cut'
_K5_DEL = ('the merged kernel branches deleted at the remote after v0.40 by the tool`s route, one per message: ' + ', '.join(
    '%s (was %s)' % (b_, t_[:8]) for b_, t_ in WL.KERNEL_DELETES)) if WL.KERNEL_DELETES else 'push-b757-join, push-b757-coeff, push-b758-land and push-b758-coeff standing at the remote'
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b757's sections over b757's objects not carried), headed as CLOSING_SECTIONS names them. A row
    of two reads its bank's verdict line by vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('b757`s close under v1.35.7, steps [22] to [25], its closing record`s head line ((R368)(1), amended)', 'b757_closing.txt', r'(?m)^b757 closed: [^\n]*'),
                ('the seat`s read of what the ruling misses, made after (4)`s pre-send reads ((R368)(2)), its head', 'b758_misses.txt', r'(?m)^b758 -- [^\n]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE STANDING CHANGES ((R368)(1), (3), (4), (6))', [
                ('v1.35.6: the reader behind the FINDINGS line passing the head through the landing`s one conversion ((R368)(1))', 'b758_standing_v1356.txt'),
                ('v1.35.7: the readers behind N2, N4, N5 and S3 bounded at the next act`s opening commit ((R368)(1), amended)', 'b758_standing_v1357.txt'),
                ('v1.35.8: the title rule, a backtick refused in an entry`s title and a bank`s head ((R368)(3))', 'b758_standing_v1358.txt'),
                ('v1.35.9: the one-call tool opened for this act in SIDE-explicit-formula, before any kernel write', 'b758_standing_v1359.txt'),
                ('v1.36.0: (6)(i), the fast-forward of a kernel`s local main to its remote`s main', 'b758_standing_v1360.txt'),
                ('v1.36.1: (6)(ii), the push of a named commit to a named non-main branch, built for the acts after', 'b758_standing_v1361.txt'),
                ('v1.36.2: G-TRAIL-CARRIES-SEAL reading the trail bank, and the kernels face naming SIDE-dirichlet-mod-24', 'b758_standing_v1362.txt')]),
            ('THE LANDING ((R368)(4))', [
                ('the two pre-send reads at the landing`s tip, banked before the dispatch', 'b758_presend.txt'),
                ('push-b758-land at push-b757-join`s tip, its one commit the rename', 'b758_land.txt'),
                ('tools/b758_controls.py by its own controls, committed before its opening dispatch', 'b758_controls_control.txt'),
                ('every dispatch and its read by run id, within the cap of 4', 'b758_controls.txt'),
                ('the outcomes of (4) and (5), each sentence cut from the ruling for the outcome its run read', 'b758_outcomes.txt')]),
            ('THE THREE RESULTS ((R368)(5))', [
                ('push-b758-coeff at main, 596d1c9e merged without fast-forward, print_targets.txt the union read against the tree', 'b758_coeff.txt')]),
            ('THE CEILING ((R368)(2))', [
                ('the readings against 16 hours from the delivery, banked by the committed tool', 'b758_ceiling.txt')]),
            ('THE STATEMENTS FOR SECTIONS 6 TO 8 ((R368)(7))', [
                ('the fourteen names, each statement, docstring and axioms line with its run, and the heads of sections 6 to 8', 'b758_epstein_statements.txt')]),
            ('THE NOTES OF (8) ((R368)(8))', [
                ('the five notes (a) to (e), each cut from the outcomes bank and read against the ruling`s text, one PLACE-papers commit each', 'b758_notes.json', r'"confirm": "[^"]*"'),
                ('the relay lines whose cites b757`s Epstein note moved, read by the citation tool`s helpers, none edited', 'b758_moved_cites.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b758_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS NOT REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run not run: its rows compute at a field, which (R368)(10) bars; the arm declared failing on the face', 'b758_registration_%s.txt' % WL.DATE, r'(?m)^### `G-RESEARCH-REPRODUCES`[^\n]*')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R365)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s tree alone, as (R368)(10) opens it: main from ' + WL.EF_BASE[:8] + ' ' + _K5_MAIN + ', by the gated push`s default mode after each run`s success, never forced ; ' + WL.LAND_BRANCH[0] + ' at ' + WL.LAND_BRANCH[1][:8] + ' ((4)`s one commit, sRe renamed in Schema/ZQ/OffZero/Time.lean) and ' + WL.COEFF_LAND_BRANCH[0] + ' at ' + (WL.COEFF_LAND_BRANCH[1] or '-')[:8] + ' ((5)`s merge of 596d1c9e, print_targets.txt the union), each pushed --scratch and read back ; ' + WL.ZQ_TAG[0] + ' peeling to ' + WL.ZQ_TAG[2][:8] + ', unmoved ;',
    '    the local mains by (6)(i)`s route alone: SIDE-dirichlet-mod-24`s from ' + WL.M24_BASE + ' to its remote`s ' + WL.M24_MAIN + ', ' + WL.M24_TAG[0] + ' peeling to ' + WL.M24_TAG[2][:8] + ', unmoved, nothing pushed there ; SIDE-explicit-formula`s to each landing ;',
    '    the four held branches of SIDE-explicit-formula at their tips, zq-b730 at ' + WL.ZQ_TIP[:8] + ' unmoved ; ' + _K5_DEL + ' ; the rebuild-b721 branches of the wave 1 kernels as b758 found them ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches in SIDE-explicit-formula of the ' + str(WL.MAX_DISPATCHES) + ' (R368)(10) allows, each read by its run id from its artifact, the exit file governing (relay data/b758_dispatch_rows.json, data/b758_controls.txt) ; none in SIDE-dirichlet-mod-24 (' + str(len(WL.M24_RUNS)) + ' rows), whose local main alone (6)(i) moves ;',   # ### b758 step zero: the dispatch line read against (R368)(10) and rewritten; the section's other lines are b757's and are rewritten at Component 5
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each record route, suite part and dispatch ;',
    '    the push-b757-* branches of relay and PLACE-papers deleted at step zero by name, one per message, the --merged listing printed before them as captured shell commands ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ v1.35.6 to v1.36.2, each a version commit of its own with its controls in its bank before its use, v1.35.9 before any kernel write ; each act tool committed before its run ; a kernel`s main moved after its run`s success alone ; the (W) regeneration and the pre-lock dry before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: each note of (8) equal to the ruling`s text with its fields filled from the banks (relay data/b758_notes.json) ; no sentence of any paper above a note edited ; no sentence of the act saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved ; a sentence of the act about a result at the control naming the side, the side matcher narrowed under (9) ; the entry`s INTEGRATION line composed from the banks` feet ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; nothing computed at any field ((R368)(10) ; the reproduction not run, declared on the face) ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed, the kernel`s commits and tag messages among them (relay data/b758_address_scan.txt, data/b758_address_scan_postlock.txt, data/b758_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no anchor edited ; no order entered, W-ORD-SQUARES-AT-24 taking its price in (8)`s block of OPEN_TRAILS ;',
    '    on PLACE-papers main FINDINGS (the corrigendum, the entry), OPEN_TRAILS ((8)`s block under one dated head, and the trail), REGISTRY ((8)(d)`s note at the file`s end), FACES_LEDGER ((8)(b)`s note at the file`s end), the Epstein document ((8)(a)`s note after its latest dated note) and the census ((8)(c)`s note at the file`s end) ; no sentence of a paper`s body edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b758`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; no rules bank written this act ;',
    '    tools/standing/ v1.35.6, v1.35.7, v1.35.8, v1.35.9, v1.36.0, v1.36.1 and v1.36.2, seven version commits each with its controls in its bank (relay data/b758_standing_v1356.txt to data/b758_standing_v1362.txt) ; HANDOFF.md written once by tools/standing/handoff.py before the gate ; act_current`s shared_edits as standing/carry.py shared reads them ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R368)(10) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one ((R368)(10)), its answer in relay data/b758_author_answers.txt ;',
    '        the statements bank of (7) for the navigator`s draft of sections 6 to 8, rQ_one and cQ_eq standing with no axioms line in the runs read (relay data/b758_epstein_statements.txt, data/b758_misses.txt (2)) ;',
    '        the route of (6)(ii) built and unused, zq-b730 at ' + WL.ZQ_TIP[:8] + ' ; the two lines of print_targets.txt no print can reach by the workflow`s filter, named and not edited (relay data/b758_presend.txt) ;',
    '        the relay lines whose cites b757`s Epstein note moved, printed and none edited (relay data/b758_moved_cites.txt) ; the reproduction not run at this act ; the defects of relay data/b758_defects.txt for the next corrigendum ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; ' + ('the merged kernel branches deleted by name after v0.40 (' + ', '.join(b_ for b_, _t in WL.KERNEL_DELETES) + ')' if WL.KERNEL_DELETES else WL.JOIN_BRANCH[0] + ', ' + WL.COEFF_BRANCH[0] + ', ' + WL.LAND_BRANCH[0] + ' and ' + WL.COEFF_LAND_BRANCH[0] + ' of SIDE-explicit-formula standing at the remote') + ';',
    '        push-b757-workflow and push-b757-mod24 of SIDE-dirichlet-mod-24, each merged into its main at ' + WL.M24_MAIN + '; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b758 found them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main but SIDE-explicit-formula ((R368)(4), (5)), SIDE-dirichlet-mod-24`s local main fast-forwarded to its remote`s ' + WL.M24_MAIN + ' ((R368)(6)(i)) ; '
          'SIDE-explicit-formula main %s (' + ', '.join('%s at %s' % (t_, p_) for t_, p_ in _LT5) + (' cut at main`s read-back' if _LT5 else 'unmoved, no tag cut') + '), v0.37 %s, v0.17 %s, v0.38 peeling to ' + WL.ZQ_TAG[2][:12] + ', '
          + 'the held branches off main, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b758: seven standing changes, v1.35.6 to v1.36.2, each read in the standing changes section; the carry's diffs here (b758 carried at
    # ### step zero before the fold; its tools since are the templates and tools/acts/b758.py)
#⟪END⟫
#⟪SECTION record 1⟫
    # ### b758 (R368)(4)-(6): the kernels as the act left them, the landing and the merge by their branches; what each moved read from the
    # ### outcomes bank by the figures (f['oc']), not here
    print('  kernels read: %d (SIDE-explicit-formula entering at main %s with %s peeling to %s; (4)`s branch %s at %s from %s`s tip %s; (5)`s branch %s%s; '
          'SIDE-dirichlet-mod-24 at main %s with %s peeling to %s, its local main fast-forwarded under (6)(i); no kernel beyond the two written)' % (
              len(ks), K.EF_BASE[:8], K.ZQ_TAG[0], K.ZQ_TAG[2][:8], K.LAND_BRANCH[0], (K.LAND_BRANCH[1] or '-')[:8], K.JOIN_BRANCH[0], K.JOIN_BRANCH[1][:8],
              K.COEFF_LAND_BRANCH[0], ' at %s' % K.COEFF_LAND_BRANCH[1][:8] if K.COEFF_LAND_BRANCH[1] else ', not made', K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8]))
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
    b758's form over b758's objects ((R368)(1)-(9)): the corrigendum's foot; the seven standing versions' controls from their banks (the
    reader's repair, the bound, the title rule, the kernel route, the two routes of (6), the arm and the face); the pre-send reads' foot and the
    landing's; the merge's foot where (5) was begun; the outcomes of (4) and (5) from the outcomes bank, its foot and each row's run, commit,
    tag and peel; the dispatch rows by kernel and the controls tool's banks; the ceiling's readings; the statements bank of (7); the notes'
    bank (the five writes of (8) and their confirms) and the moved cites' foot; b757's close by its closing record and scores close; the
    citation check; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the
    counter from the act's defects and events banks; nothing typed. No reproduction bank: (R368)(10) bars any computation at a field."""
#⟪END⟫
#⟪SECTION record 4⟫
    vs_ = [(v_,) + _bfig(b_.split('/', 1)[1], r'\*\*%s: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*' % re.escape(v_), '%s`s controls' % v_)
           for v_, _c, b_, _n in K.STANDING_BANKS]
    # ### b758, Component 5: (4)'s two banks, (5)'s merge where (5) was begun, the outcomes of (4) and (5), the dispatches, the ceiling, (7)'s
    # ### statements, (8)'s writes and the moved cites, b757's close
    ps_ = _bfig('%s_presend.txt' % ACT, r'\*\*THE PRE-SEND READS AT ([0-9a-f]{8}): DUPLICATES (\d+) \(OVER THE TARGETS (\d+)\) ; ANONYMOUS PAIRS (\d+) \(OF (\d+), (\d+) UNREAD\) ; '
                r'REFUSED BY THE FILTER (\d+) \(([^)]*)\) ; TARGETS (\d+) MODULES FOR (\d+) NAMES, (\d+) REFUSED, MODULES REFUSED (\d+) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the pre-send reads` foot')
    la_ = _bfig('%s_land.txt' % ACT, r'\*\*THE LANDING`S BRANCH: (AS ORDERED|NOT AS ORDERED) ; TARGETS (\d+) MODULES FOR (\d+) NAMES, (\d+) REFUSED ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the landing`s foot')
    cf_ = _bfig('%s_coeff.txt' % ACT, r'\*\*THE MERGE: (AS ORDERED|NOT AS ORDERED) ; THE UNION (AS \(5\) ORDERS|NOT AS \(5\) ORDERS) ; TARGETS (\d+) MODULES FOR (\d+) NAMES, (\d+) REFUSED ; '
                r'THE FIVE NAMES LINES (\d) OF 5 ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the merge`s foot') if rdn('%s_coeff.txt' % ACT, optional=True) else None
    of_ = _bfig('%s_outcomes.txt' % ACT, r'\*\*THE OUTCOMES: JOIN (LANDED|BROKE) ; THE THREE (LANDED|BROKE|NOT READ) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the outcomes` foot')
    oj_ = dict((r_.get('item'), r_) for r_ in (json.loads(rdn('%s_outcomes.json' % ACT)) or []))
    if sorted(oj_) != ['coeff', 'join'] or [oj_[k_].get('outcome') for k_ in ('join', 'coeff')] != list(of_[:2]) or any(oj_[k_].get('unfilled') for k_ in oj_) \
            or (of_[0] == 'BROKE' and of_[1] != 'NOT READ') or (cf_ is None) != (of_[1] == 'NOT READ'):
        sys.exit('### data/%s_outcomes.json DOES NOT CARRY THE TWO OUTCOMES OF ITS FOOT, EACH FILLED, (5) BEGUN AFTER (4)`S LANDING ALONE -- NOTHING COMPOSED' % ACT)
    dr_rows_ = json.loads(rdn('%s_dispatch_rows.json' % ACT)) or []
    dk_ = lambda kn_, kd_: [r_ for r_ in dr_rows_ if r_.get('kernel') == kn_ and r_.get('kind') == kd_]
    cc_ = _bfig('%s_controls_control.txt' % ACT, r'\*\*THE TOOL`S CONTROLS: (\d+) OF (\d+) AS WANTED ; ALL AS WANTED\.\*\*', 'the controls tool`s control bank')
    cb_ = _bfig('%s_controls.txt' % ACT, r'\*\*DISPATCHES (\d+) \(SIDE-explicit-formula (\d+) OF (\d+), SIDE-dirichlet-mod-24 (\d+) OF (\d+)\) ; READ KERNEL \(THE BUILD EXITING 0\) (\d+), '
                r'OF THEM WITH THE AXIOMS PRINT RUN (\d+) ; THE TOOL`S CONTROLS (\d+) OF (\d+)\.\*\*', 'the controls bank`s foot')
    ce_ = _bfig('%s_ceiling.txt' % ACT, r'\*\*THE CEILING: READINGS (\d+) ; THE LAST AT (\S+), ([\d.]+) h OF (\d+) ; (NOTHING CARRIED|\(7\) THEN \(6\)\(ii\) CARRIED) ; DISPATCHES (\d+) OF (\d+)\.\*\*',
                'the ceiling`s readings')
    st_ = _bfig('%s_epstein_statements.txt' % ACT, r'\*\*THE STATEMENTS BANK: AT ([0-9a-f]{8}) ; NAMES (\d+), FOUND ONE DECLARATION (\d+) ; NO AXIOMS LINE (\d+) ; SECTIONS (\d) OF 3 ; '
                r'CONTROLS (\d+) OF (\d+)\.\*\*', 'the statements bank`s foot')
    nj_ = jl('%s_notes.json' % ACT).get('items') or {}
    if sorted(nj_) != ['a', 'b', 'c', 'd', 'e'] or not all(re.match(r'PLACE-papers [0-9a-f]{8} at \S+, \S+ alone, \d+ lines added, none removed$', nj_[k_].get('confirm') or '') for k_ in nj_):
        sys.exit('### data/%s_notes.json DOES NOT CARRY THE FIVE WRITES OF (8) AND THEIR CONFIRMS -- NOTHING COMPOSED' % ACT)
    mv_ = _bfig('%s_moved_cites.txt' % ACT, r'\*\*THE MOVED CITES READ: RELAY LINES (\d+) ; CITES (\d+) ; RESOLVING (\d+) ; NOT RESOLVING (\d+) \(MOVED BY TWO (\d+) ; NO TEXT LINE THEN (\d+) ; '
                r'ELSEWHERE (\d+) ; GONE (\d+)\) ; RELAY LINES NOT AS COUNTED (\d+) ; NONE EDITED, EACH PRINTED\.\*\*', 'the moved cites` foot')
    b7c_ = jl('b757_scores_close.json') or {}
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b758: no order entered; W-ORD-SQUARES-AT-24 takes its price in (8)'s OPEN_TRAILS block
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                corr_findings=((co.get('findings') or {}).get('claim'), (co.get('findings') or {}).get('close'), (co.get('findings') or {}).get('repeat')),
                vers=[(v_, c_, int(n_), int(w_)) for v_, c_, n_, w_ in vs_],   # ### the seven: (version, controls, cases, as wanted)
                routes=sum(1 for v_, _c, n_, w_ in vs_ if v_ in ('v1.36.0', 'v1.36.1') and int(n_) == int(w_)),   # ### (6)(i) and (6)(ii), each landed with its controls
                ps_rev=ps_[0], ps_dup=int(ps_[1]), ps_anon=(int(ps_[3]), int(ps_[4]), int(ps_[5])), ps_refused=int(ps_[6]), ps_refused_lines=ps_[7],
                ps_modules=int(ps_[8]), ps_names=int(ps_[9]), ps_ctl=(int(ps_[12]), int(ps_[13])),
                la_word=la_[0], la_modules=int(la_[1]), la_names=int(la_[2]), la_refused=int(la_[3]), la_ctl=(int(la_[4]), int(la_[5])),
                cf=None if cf_ is None else dict(merge=cf_[0], union=cf_[1], modules=int(cf_[2]), names=int(cf_[3]), refused=int(cf_[4]), five=int(cf_[5]),
                                                  ctl=(int(cf_[6]), int(cf_[7]))),
                oc=dict((k_, dict(outcome=oj_[k_].get('outcome'), run=oj_[k_].get('run'), sha=(oj_[k_].get('sha') or '')[:8], sentence=oj_[k_].get('sentence'),
                                  tag=oj_[k_].get('tag'), peel=(oj_[k_].get('peel') or '')[:8], fields=oj_[k_].get('fields'), five=oj_[k_].get('five'))) for k_ in oj_),
                join_word='landed at v0.39' if of_[0] == 'LANDED' else 'broke', three_word='landed at v0.40' if of_[1] == 'LANDED' else 'on their branch',
                oc_ctl=(int(of_[2]), int(of_[3])),
                close_word='written' if rdn('b757_closing.txt', optional=True) and b7c_ else 'carried',
                b7_held=sum(1 for v_ in b7c_.values() if (v_ or [''])[0] == 'HELD'), b7_refuted=[k_ for k_, v_ in sorted(b7c_.items()) if (v_ or [''])[0] != 'HELD'],
                disp_ef=len(dk_('SIDE-explicit-formula', 'dispatch')), disp_m24=len(dk_('SIDE-dirichlet-mod-24', 'dispatch')),
                read_ef=len(dk_('SIDE-explicit-formula', 'read')), read_m24=len(dk_('SIDE-dirichlet-mod-24', 'read')),
                cc_ctl=(int(cc_[0]), int(cc_[1])), cb_kernel=int(cb_[5]), cb_printed=int(cb_[6]), cb_ctl=(int(cb_[7]), int(cb_[8])),
                ce_n=int(ce_[0]), ce_at=ce_[1], ce_sum=ce_[2], ce_ceiling=int(ce_[3]), ce_word=ce_[4], ce_disp=(int(ce_[5]), int(ce_[6])),
                st_rev=st_[0], st_names=int(st_[1]), st_found=int(st_[2]), st_noax=int(st_[3]), st_sections=int(st_[4]), st_ctl=(int(st_[5]), int(st_[6])),
                notes=[(k_, nj_[k_].get('file'), nj_[k_].get('confirm'), int(re.search(r', (\d+) lines added,', nj_[k_]['confirm']).group(1))) for k_ in ('a', 'b', 'c', 'd', 'e')],
                notes_written=len(nj_),
                mv_lines=int(mv_[0]), mv_cites=int(mv_[1]), mv_resolving=int(mv_[2]), mv_not=int(mv_[3]), mv_two=int(mv_[4]), mv_notext=int(mv_[5]),
                mv_elsewhere=int(mv_[6]), mv_gone=int(mv_[7]), mv_uncounted=int(mv_[8]),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R368): no lean process runs on this host; each build a runner dispatch read by its run id from the artifact, the exit file
    governing (each dispatch row with one read row of its run, the read's exit read); the dispatch counts within (10)'s, 14 in
    SIDE-explicit-formula and 4 in SIDE-dirichlet-mod-24, the worklist's EF_RUNS and M24_RUNS each the runs of its kernel's dispatch and
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
    # ### b758 step zero: read against (R368)(10)'s caps (4 in SIDE-explicit-formula, 0 in SIDE-dirichlet-mod-24): the loop's form holds for both,
    # ### the second kernel's rows and runs empty and its count 0 within its cap 0
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
        'the seat`s commands running lean or lake on this host (relay data/b758_commands.json): %s; dispatch commands in the capture: %s, against the dispatch rows %d and the sends refused by the host (no run) %d; by kernel, dispatches against (10)`s cap and the worklist`s runs each a dispatch row`s and a read row`s: %s; reads %d, a run read twice: %s; each read`s exit file: %s; a read with no exit read: %s; dispatch rows under the memory hold 2,560 MB or the disk hold 5,000 MB, or a row without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b758_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(_ef_kind(rows_, 'dispatch')), len(refused_),
            ', '.join('%s %d of %d, the runs %s' % (k_, n_, c_, o_) for k_, n_, c_, o_ in per_), len(reads_), ', '.join(twice_) or 'none', '; '.join(exits_),
            unexit_ or 'NONE', free_ or 'NONE', K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b758's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line);
# ### the controls tool's own controls stand in a bank of their own (data/b758_controls_control.txt), read by time against the opening dispatch
N2_CONTROLS = (('data/b758_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b758_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b758_standing_v1356.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.35.6: CONTROLS '),
               ('data/b758_standing_v1357.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.35.7: CONTROLS '),
               ('data/b758_standing_v1358.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.35.8: CONTROLS '),
               ('data/b758_standing_v1359.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.35.9: CONTROLS '),
               ('data/b758_standing_v1360.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.0: CONTROLS '),
               ('data/b758_standing_v1361.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.1: CONTROLS '),
               ('data/b758_standing_v1362.txt', '### THE COMPILE CONTROL, BEFORE ANY CASE', '### ### **v1.36.2: CONTROLS '),
               ('data/b758_presend.txt', '## THE CONTROLS', '## AT 6568e9c7'),
               ('data/b758_land.txt', '## THE CONTROLS', '## THE BRANCH push-b758-land, ITS ONE COMMIT'),
               ('data/b758_outcomes.txt', '## THE CONTROLS', '## (4) THE JOIN LANDED'),
               ('data/b758_ceiling.txt', '## THE CONTROLS', '## THE READINGS, EACH APPENDED WHEN TAKEN'),
               ('data/b758_epstein_statements.txt', '## THE CONTROLS', '## THE RUNS READ FOR THE AXIOMS LINES'),
               ('data/b758_moved_cites.txt', '## THE CONTROLS', '### the rows: '),
               ('data/b758_controls.txt', '## THE CONTROLS', '## SIDE-explicit-formula: '))
N2_CONTROLS_COEFF = ('data/b758_coeff.txt', '## THE CONTROLS', '## THE MERGE ON push-b758-coeff')   # ### where (5) was begun
N2_PUSHES = ('SIDE-explicit-formula_push-b758-land', 'SIDE-explicit-formula_push-b758-coeff')   # ### the gated push's captures, data/b758_<kernel>_<branch>_push_out.txt
N2_WORKFLOW = None   # ### b758: no move of a kernel's main ahead of a build; (6)(i)'s fast-forward moves a local main to its remote's, no push


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
N2_RIDERS = ('data/b758_steps.json', 'data/b758_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


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
    """N2 (R368): "the step-zero reads and the carry print before any write; each standing change lands with its controls before its use;
    each act tool commits before it runs; a kernel's main moves after its run's success and at no other time." Read: the chain read, the
    step-zero reads and the carry by the step-zero bank's times, in that order, before the act_current commit (the chain read's time banked
    to the ten seconds, 2x read as 20); the act's commits in the worklist's TIME_ORDER by time, relay and PLACE-papers together; each of the
    seven standing changes a commit of its own moving VERSION with its controls bank, the act's commits under tools/standing/ those seven and
    no other; the kernel route (v1.35.9) landing before any kernel write; each tool of K.GENS first added by a commit of its own carrying it
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
    # ### b758's step-zero bank: the chain read at :8 (23:22:2xZ, to the ten seconds), the reads at :12 (23:24:49Z-...), the carry at :16-:17
    # ### (refused first at 23:25:44Z, nothing written; its first write after it)
    szt_ = [(n_, re.search(p_, sz_, re.S)) for n_, p_ in (('the chain read', r'THE CHAIN READ \((\d\d:\d\d:\d[\dx])Z'),
                                                          ('the step-zero reads', r'THE STEP-ZERO READS \((\d\d:\d\d:\d\d)Z'),
                                                          ('the carry', r'THE CARRY before any (?:other )?write of the relay: .*?(\d\d:\d\d:\d\d)Z'))]
    sze_ = [(n_, _hms_epoch(m_.group(1).replace('x', '0')) if m_ else None) for n_, m_ in szt_]
    stepzero_ = all(e_ for _n, e_ in sze_) and [e_ for _n, e_ in sze_] == sorted(e_ for _n, e_ in sze_) and sze_[-1][1] < tm_[0]
    # ### the standing changes: each of the seven a commit of its own moving VERSION with its controls bank; the act's commits under
    # ### tools/standing/ those seven and no other
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
    # ### the kernel route (v1.35.9, K.C1_STANDING) landed, with its controls bank, before any kernel write (the earliest of K.KERNEL_COMMITS)
    kd_ = {'SIDE-explicit-formula': K.EF_DIR, 'SIDE-dirichlet-mod-24': K.M24_DIR}
    kt_ = [(k_, c_, ct_(kd_[kn_], c_)) for k_, kn_, c_, _b in K.KERNEL_COMMITS]
    kw0_ = min([t_ for _k, _c, t_ in kt_ if t_] or [0])
    before_kw_ = all(t_ for _k, _c, t_ in kt_) and ct_(ROOT, K.C1_STANDING) < kw0_
    # ### the controls tool committed, then its own controls banked AS WANTED, then its opening dispatch (the dispatch rows' first 'at')
    cc_t_ = rdn('%s_controls_control.txt' % ACT)
    cc0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)\s*$', (cc_t_.split(NL) or [''])[0])
    d0_ = min([_iso_epoch(r.get('free_at') or '') or 0 for r in _ef_kind(jl('%s_dispatch_rows.json' % ACT) or [], 'dispatch')] or [0])
    cons_ = bool(cc0_) and ct_(ROOT, dict(K.CHAIN)['controls_gen']) < (_iso_epoch(cc0_.group(1)) or 0) < d0_ and 'CONTROLS: 16 OF 16 AS WANTED ; ALL AS WANTED' in cc_t_
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
        'the chain read, the step-zero reads and the carry printed before any write, in that order (%s, each by the step-zero bank, before the act_current commit %s): %s; the standing changes, each a commit of its own moving VERSION with its controls bank (%s), the act`s commits under tools/standing/ those seven and no other (%s): %s; the kernel route (v1.35.9) before any kernel write (the first kernel commit %s): %s; each tool first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the tool (%s): %s; the controls tool committed (%s), its own controls banked AS WANTED (%s) before its opening dispatch: %s; each move of a kernel`s main after its run`s success at that tip (%s): %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; the act`s %d commits in the worklist`s order by time, relay and PLACE-papers together: %s (%s); the kernel route an ancestor of HEAD: %s; the tools` controls before their figures: %s' % (
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
N3_GRADED = (('b758_corrigendum.txt', ('ITEMS 74', 'THE ENTRY AT FINDINGS :15484')),
             ('b758_standing_v1356.txt', ('v1.35.6: CONTROLS', 'ALL AS WANTED')), ('b758_standing_v1357.txt', ('v1.35.7: CONTROLS', 'ALL AS WANTED')),
             ('b758_standing_v1358.txt', ('v1.35.8: CONTROLS', 'ALL AS WANTED')), ('b758_standing_v1359.txt', ('v1.35.9: CONTROLS', 'ALL AS WANTED')),
             ('b758_standing_v1360.txt', ('v1.36.0: CONTROLS', 'ALL AS WANTED')), ('b758_standing_v1361.txt', ('v1.36.1: CONTROLS', 'ALL AS WANTED')),
             ('b758_standing_v1362.txt', ('v1.36.2: CONTROLS', 'ALL AS WANTED')),
             ('b758_presend.txt', ('THE PRE-SEND READS AT d1afb4fc: DUPLICATES 0', 'REFUSED BY THE FILTER 2 (:358, :359)', 'CONTROLS 11 OF 11')),
             ('b758_land.txt', ('THE LANDING`S BRANCH: AS ORDERED', 'CONTROLS 6 OF 6')),
             ('b758_controls_control.txt', ('THE TOOL`S CONTROLS: 16 OF 16 AS WANTED',)),
             ('b758_controls.txt', ('**DISPATCHES ', 'THE TOOL`S CONTROLS 16 OF 16')),
             ('b758_outcomes.txt', ('THE OUTCOMES: JOIN ', ' ; THE THREE ', 'CONTROLS 7 OF 7')),
             ('b758_ceiling.txt', ('THE CEILING: READINGS ', ' h OF 16 ; ')),
             ('b758_epstein_statements.txt', ('THE STATEMENTS BANK: AT ', 'NAMES 14, ')),
             ('b758_moved_cites.txt', ('THE MOVED CITES READ: RELAY LINES 123', 'NONE EDITED, EACH PRINTED')),
             ('b758_citation_check.txt', ('### ### **THE CHECK ', '** (halts ')), ('b758_address_scan.txt', ('PREVIOUS ADDRESS',)))
N3_GRADED_COEFF = ('b758_coeff.txt', ('THE MERGE: ', 'THE FIVE NAMES LINES '))   # ### where (5) was begun
# ### N3 (R367): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word; the centre
# ### matcher over the clause's own words, "anything of zeta, RH, GRH or Weil positivity on classK for zeta" (data/b757_ferry.txt :51): zeta
# ### (the symbol, Riemann's, or a zeta function not the Epstein's), RH, GRH and Weil positivity on classK -- b756's bare `classK` not carried,
# ### the clause naming classK only inside Weil positivity for zeta, and (R367)(7)'s outcome a test function in classK at the control; the
# ### side matcher over (R367)'s "no sentence about the control speaks of positivity without naming the side"
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
N3_LOC = (r'(?:\b(?:RH|GRH)\b|ζ|\bRiemann(?:`s|\'s)? zeta\b|(?<!Epstein )\bzeta function\b|\bWeil positivity on classK\b).*'
          r'\b(?:holds|hold|fails|fail|proved|refuted|moved)\b')
N3_SIDE = r'\bpositivity\b'
N3_BANKS = ('stepzero', 'misses', 'corrigendum', 'presend', 'land', 'controls_control', 'controls', 'outcomes', 'ceiling', 'epstein_statements',
            'moved_cites', 'standing_v1356', 'standing_v1357', 'standing_v1358', 'standing_v1359', 'standing_v1360', 'standing_v1361', 'standing_v1362',
            'events', 'defects')
N3_BANKS_OPTIONAL = ('coeff',)   # ### (5)'s merge bank, read where (5) was begun
# ### N3 (R367): no figure of the navigator's workspace printed as a banked figure -- the ruling's one figure of the navigator's reading that
# ### no bank of the act computed, (7)'s price "as the navigator read it, 250 to 550 lines and 4 to 8 dispatches" ((R367)(2), (7)), banked
# ### in the price table as the navigator's beside the seat's own: in the act's own sentences and the entry's, each occurrence wants the
# ### navigator named in its sentence
N3_NAV_FIGS = r'\b250(?: to |-)550\b|\b4(?: to |-)8 dispatches\b'
# ### N3 (R367): each write of (9) equal to the ruling's text with its fields filled from the banks -- each line the notes bank names read at
# ### PLACE-papers HEAD by its digest, and each outcome sentence the bank's item names (data/b757_outcomes.json) standing whole in that note
# ### b758, (R368)(8): (a) to (d) each "made of the document's own dated head and the sentences of (4) and (5) that came true" (None: the
# ### outcomes bank's items LANDED or BROKE, (4) then (5)); (e), OPEN_TRAILS' block, none
N3_NOTES = (('a', None), ('b', None), ('c', None), ('d', None), ('e', ()))
N3_PAPERS = ('phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'FACES_LEDGER.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'REGISTRY.md')
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
    """the entry's last line, the ferry's INTEGRATION line (data/b758_ferry.txt :44) composed from the banks' feet through _figs, adjusted to
    what the act did: b757's close by its closing record and scores close; the join and the three results by the outcomes bank's foot; the
    routes of (6) by their two standing versions' controls; the dispatches by the dispatch rows; the notes of (8) by the notes bank's five
    confirms."""
    return ("INTEGRATION: b757's close: %s; the join: %s; the three results: %s; the routes: %d of 2; dispatches %d; the notes of (8): %d written" % (
        f['close_word'], f['join_word'], f['three_word'], f['routes'], f['disp_ef'] + f['disp_m24'], f['notes_written']))


N3_KEYS = {}   # ### b758: the notes bank's sentence keys are the outcomes bank's items (join, coeff)


def _notes_rows():
    """N3 (R368): each write of (8) at PLACE-papers HEAD against the ruling's text with its fields filled from the banks: each line the notes
    bank names, read from its file at HEAD, carrying the bank's digest (sha256 of the line, 16 hex); the bank's sentence keys for (a) to (d)
    the outcomes bank's items that came true (LANDED or BROKE), (e) none; each such sentence (data/b758_outcomes.json) standing whole in the
    note's lines; (item, lines, equal). And the papers of (8) and OPEN_TRAILS since the act's base: lines added, none removed (no sentence
    above a note edited)."""
    nj_ = jl('%s_notes.json' % ACT).get('items') or {}
    ocr_ = json.loads(rdn('%s_outcomes.json' % ACT)) or []
    oc_ = dict((r_.get('item'), r_.get('sentence') or '\x00') for r_ in ocr_)
    true_ = tuple(r_.get('item') for r_ in ocr_ if r_.get('outcome') in ('LANDED', 'BROKE'))
    rows_ = []
    for k_, want_ in N3_NOTES:
        want_ = true_ if want_ is None else want_
        it_ = nj_.get(k_) or {}
        txt_ = (_show(PP, 'HEAD', it_.get('file') or '-') or '').replace(chr(13), '').split(NL)
        ls_ = [x_ for x_ in it_.get('lines') or []]
        got_ = [txt_[x_['line'] - 1] if 0 < (x_.get('line') or 0) <= len(txt_) else '\x00' for x_ in ls_]
        dig_ = all(_hs.sha256(t_.encode('utf-8')).hexdigest()[:16] == x_.get('digest') for t_, x_ in zip(got_, ls_))
        keys_ = sorted(N3_KEYS.get(s_, s_) for s_ in (it_.get('sentences') or {}))
        body_ = NL.join(got_)
        rows_.append((k_, len(got_), bool(ls_) and dig_ and keys_ == sorted(want_) and all(oc_.get(w_, '\x00') in body_ for w_ in want_)))
    rm_ = []
    for p_ in N3_PAPERS + ('OPEN_TRAILS.md',):
        ns_ = g(PP, 'diff', '--numstat', K.PRE_PP, 'HEAD', '--', p_).split()
        if not ns_ or ns_[1] != '0':
            rm_.append('%s %s' % (p_, ns_[:2] or 'UNCHANGED'))
    return rows_, rm_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R368): "each sentence written under (8) equals this ruling's text with its fields filled from the banks; no sentence of the act says
    that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; a sentence the act writes about a result at the
    control names the side, under (9)." Read: each line the notes bank names at PLACE-papers HEAD by its digest, each sentence of (4) and (5)
    that came true standing whole in (a) to (d); no line of the papers of (8) or OPEN_TRAILS removed since the act's base; the centre matcher
    over the act's own sentences and the entry's, outside a negation; the side matcher with the dated records' lines left out (9); each
    bank's foot carrying its grade; each matcher's control caught; the entry's last line the ferry's INTEGRATION line composed from the banks;
    the banks' nouns in the entry; the root prompt's sentences about the entry the composer's ((R368)(10), "composed from the banks"). The
    novelty and navigator-figure matchers of (R367) printed with their yields and graded by no clause."""
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
    # ### the writes of (9) against the ruling's text; no line of a paper removed; the navigator's figures
    notes_, removed_ = _notes_rows()
    navfig_ = [x[:80] for x in navs_ + sents if _nav_bad(x)]
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    nouns_ = [w_ for w_ in ('v0.38', 'v0.2.0', 'push-b758-land', 'd1afb4fc', 'v1.35.6', 'v1.35.7', 'v1.35.8', 'v1.35.9', 'v1.36.0', 'v1.36.1', 'v1.36.2',
                            'data/%s_presend.txt' % ACT, 'data/%s_land.txt' % ACT, 'data/%s_outcomes.txt' % ACT, 'data/%s_notes.json' % ACT,
                            'data/%s_ceiling.txt' % ACT, 'data/%s_epstein_statements.txt' % ACT, 'data/%s_moved_cites.txt' % ACT,
                            'data/%s_corrigendum.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    # ### b758: (R368)'s three clauses and the carried ones beside them; more_, first_ and navfig_ printed, graded by no clause of (R368)
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not loc_ and not side_ and len(notes_) == 5 \
        and all(o_ for _k, _n, o_ in notes_) and not removed_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence and (7)`s classK sentence passed, a negation read, a sentence of positivity at the control naming no side caught and one naming the arithmetic side passed, a quotation wrapped over two lines dropped and the text after it kept, (7)`s price as the navigator read it caught where no navigator is named, passed where one is, and a longer number passed, a table row naming the navigator before its semicolon caught by the sentence cut and passed read whole, and a row naming none caught): %s; each write of (8) at PLACE-papers HEAD, each line by the notes bank`s digest and each sentence of (4) and (5) that came true standing whole in its note (relay data/%s_notes.json, data/%s_outcomes.json): %s, %d lines; the papers of (8) and OPEN_TRAILS since the act`s base with a line removed: %s; over %d of the act`s own sentences and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation (graded by no clause of (R368)): %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant (graded by no clause of (R368)): %s; a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; a sentence about a result at the control speaking of positivity with no side named, the lines a dated record heads left out ((R368)(9)): %s; a sentence printing (R367)`s navigator`s price with no navigator named (graded by no clause of (R368)): %s; the entry`s last line (R368)`s INTEGRATION line composed from the banks (%s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            ACT, ACT, ', '.join('(%s) %d %s' % x_ for x_ in notes_), sum(n_ for _k, n_, _o in notes_), removed_ or 'NONE',
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', side_ or 'NONE', navfig_ or 'NONE',
            il_, integ_, nouns_ or 'NONE', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
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
    _land5 = [r_ for r_ in (json.loads(rdn('%s_outcomes.json' % ACT, optional=True) or '[]') or []) if r_.get('outcome') == 'LANDED' and r_.get('tag') and r_.get('peel')]
    _new5 = dict((r_['tag'], r_['peel'][:7]) for r_ in _land5)
    _main5 = _land5[-1]['peel'] if _land5 else K.EF_BASE
    tag_one = _ef_now[0] == _main5[:7] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **_new5)
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main.startswith(_main5[:8]) and set(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) <= set(['v0.37', 'v0.38'] + list(_new5)) \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') and ch_ok \
        and bool(prev) and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main and tags against b757`s face moved by the outcomes of (R368)(4) and (5) alone (main at the last landed tag`s peel, 8fbab45d where none landed; each landed tag at its peel; v0.38 at 14ca5725; read in full in N5`s kernel clause below), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R368)(10), N5: "no kernel touched beyond SIDE-explicit-formula's tree and the two local mains of (6)(i)" -- every ref of every kernel
    # ### carrying a commit made after the act's opening commit is a fault but the act's own: in SIDE-explicit-formula a push-b758-* branch, its
    # ### main at the last landed tag's peel and the landed tags; SIDE-dirichlet-mod-24's local main (6)(i) moved to a commit of b757's, before
    # ### the start; a listed branch of the face's list excepted as before; no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b756 found them; the address scan's count from its bank
    ocr5_ = json.loads(rdn('%s_outcomes.json' % ACT)) or []
    land5_ = [r_ for r_ in ocr5_ if r_.get('outcome') == 'LANDED']
    main5_ = (land5_[-1].get('peel') if land5_ else K.EF_BASE) or ''
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R354)(2)(v): the face's branch list
    own_k_ = ('SIDE-explicit-formula', 'SIDE-dirichlet-mod-24')
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
                if kn in own_k_ and (r_[0].startswith('refs/heads/push-b758-') or (kn == 'SIDE-dirichlet-mod-24' and r_[0] == 'refs/heads/main')
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
    # ### N5 (R368): "v0.38's peel reads 14ca5725 and v0.2.0's reads e5ebdd15 at the close; each new tag's peel is read back equal to main".
    # ### SIDE-dirichlet-mod-24: v0.2.0 peeling to e5ebdd15 by its tag object, the local main there by (6)(i)'s route. SIDE-explicit-formula:
    # ### each tag the outcomes bank gives LANDED, its gated push's capture reading main back at the remote equal to the tag's commit and the
    # ### tag's peel local and remote equal to it, the commit the outcome's peel; no tag v0.39* or v0.40* beyond those; v0.38 at 14ca5725; each
    # ### branch the act pushed read back at the remote in its capture
    m24_loc_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % K.M24_TAG[0]).strip()
    m24_main_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'main').strip()
    m24_ok = m24_loc_.startswith(K.M24_TAG[2]) and m24_main_ == m24_loc_ \
        and g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s' % K.M24_TAG[0]).strip().startswith(K.M24_TAG[1])
    br5_ = {'join': K.LAND_BRANCH[0], 'coeff': K.COEFF_LAND_BRANCH[0]}
    efl_ = []
    for r_ in land5_:
        c_ = rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, br5_.get(r_.get('item'), '-')), optional=True) or ''
        rb_ = re.findall(r'(?m)^push_gated: main read back at the remote: ([0-9a-f]{40})$', c_)
        pl_ = re.findall(r'(?m)^push_gated: tag %s peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$' % re.escape(r_.get('tag') or '-'), c_)
        loc_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % (r_.get('tag') or '-')).strip()
        efl_.append((r_.get('tag'), loc_[:8] or 'NONE', bool(loc_) and loc_.startswith((r_.get('peel') or '-')[:8]) and rb_[-1:] == [loc_] and pl_[-1:] == [(loc_, loc_)]))
    ef_new_tags_ = sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--list', 'v0.39*', 'v0.40*').split() if t_.strip())
    v038_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip()
    pushed5_ = [(K.LAND_BRANCH[0], K.LAND_BRANCH[1])] + ([(K.COEFF_LAND_BRANCH[0], K.COEFF_LAND_BRANCH[1])] if K.COEFF_LAND_BRANCH[1] else [])
    ef_rb_ = [(b_, bool(re.search(r'(?m)^push_gated: branch %s read back at the remote: %s' % (re.escape(b_), t_ or '-'),
                                  rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, b_), optional=True) or ''))) for b_, t_ in pushed5_]
    efb_ok = ef_new_tags_ == sorted(t_ for t_, _l, _o in efl_) and all(o_ for _t, _l, o_ in efl_) and v038_.startswith('14ca5725') and all(o_ for _b, o_ in ef_rb_)
    # ### N5: a repository edit read by the taught reader (tools/b757_ghcalls.py over this act's capture, unedited): no captured command runs
    # ### gh repo edit, and no tool the capture runs sends one ((R368) orders no description)
    gho_ = __import__('b757_ghcalls').over(ACT)
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
            'the address scan (relay data/b758_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel, the act`s own apart (a push-b758-* branch, main at the last landed tag`s peel %s and the landed tags in SIDE-explicit-formula, SIDE-dirichlet-mod-24`s local main), or a .lean file in a kernel`s tree (%d kernels read): %s; the act`s own refs read: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; SIDE-dirichlet-mod-24`s tag %s peeling locally to %s, its local main %s: %s; SIDE-explicit-formula: the tags v0.39* and v0.40* %s, each landed tag at its outcome`s peel with main read back at the remote equal to it and its peel local and remote equal (%s), v0.38 at %s, each branch the act pushed read back at the remote in its capture %s: %s; '
            'gh repo edit run by a captured command (the carried reader): %s; gh repo edit sent from inside a tool, read by its rows bank (the taught reader, tools/b757_ghcalls.py): %s, none wanted: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (main5_[:8], len(kps_), lean_w or 'NONE', ', '.join(own_r) or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                K.M24_TAG[0], m24_loc_[:8] or 'NONE', m24_main_[:8] or 'NONE', m24_ok,
                ef_new_tags_ or 'NONE', '; '.join('%s at %s %s' % x_ for x_ in efl_) or 'none landed', v038_[:8] or 'NONE', ef_rb_, efb_ok,
                'UNREAD (no command bank)' if gho_ is None else (ghr_ or 'NONE'), '; '.join('tools/%s.py %s' % (s_, v_) for s_, v_ in ghs_.items()) or ('UNREAD (no command bank)' if gho_ is None else 'NONE'), gh_ok,   # ### defect (x): NONE printed unread
                ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    raise SystemExit('### b758`s a block reading an act ordinal or the read-first needles (SECTION record 28) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 3 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION record 29⟫
# ### b756: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict
# ### b758, Component 5: the guard over (R368)(1)-(9)'s feet


def _guard(f):
    """the composer's refusals before any sentence, where the banks' feet disagree with one another (never on a verdict): the seven standing
    versions in the worklist's order with the worklist's cases, each all as wanted; the pre-send reads and the landing at the same targets;
    the dispatches by kernel within (10)'s caps, each dispatch read once, the controls bank's count the rows'; the five notes each a confirm
    with lines added; the moved cites' classes summing to the cites not resolving, and those with the resolving to the cites; the ceiling's
    dispatches the rows'."""
    if [v_ for v_, _c, _n, _w in f['vers']] != [v_ for v_, _c, _b, _n in K.STANDING_BANKS] or any(n_ != w_ for _v, _c, n_, w_ in f['vers']) \
            or [n_ for _v, _c, n_, _w in f['vers']] != [n_ for _v, _c, _b, n_ in K.STANDING_BANKS]:
        sys.exit('### THE STANDING VERSIONS ARE NOT THE WORKLIST`S SEVEN, EACH ALL AS WANTED -- NOTHING COMPOSED')
    if (f['ps_modules'], f['ps_names']) != (f['la_modules'], f['la_names']) or f['la_refused'] != 0 or f['ps_ctl'][0] != f['ps_ctl'][1] or f['la_ctl'][0] != f['la_ctl'][1]:
        sys.exit('### THE PRE-SEND READS AND THE LANDING DISAGREE ON THE TARGETS, OR A CONTROL IS NOT AS WANTED -- NOTHING COMPOSED')
    if f['disp_ef'] > K.MAX_DISPATCHES or f['disp_m24'] > K.MAX_DISPATCHES_M24 or f['disp_ef'] != f['read_ef'] or f['disp_m24'] != f['read_m24'] \
            or f['cb_kernel'] != f['read_ef'] + f['read_m24']:
        sys.exit('### THE DISPATCH ROWS ARE OVER (10)`S CAPS, NOT EACH READ ONCE, OR NOT THE CONTROLS BANK`S COUNT -- NOTHING COMPOSED')
    if f['notes_written'] != 5 or any(n_ < 1 for _k, _f, _c, n_ in f['notes']):
        sys.exit('### THE NOTES OF (8) ARE NOT FIVE WRITES, EACH WITH LINES ADDED -- NOTHING COMPOSED')
    if f['mv_two'] + f['mv_notext'] + f['mv_elsewhere'] + f['mv_gone'] != f['mv_not'] or f['mv_resolving'] + f['mv_not'] != f['mv_cites']:
        sys.exit('### THE MOVED CITES` CLASSES DO NOT SUM -- NOTHING COMPOSED')
    if f['ce_disp'][0] > f['disp_ef'] + f['disp_m24'] or f['ce_disp'][1] != K.MAX_DISPATCHES:
        sys.exit('### THE CEILING`S DISPATCHES ARE NOT THE ROWS` -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects (the ferry's Component 5, data/b758_ferry.txt :44, "the entry's title composed under (3)"): b757's
    close (b758_corrigendum); the join (b758_presend, b758_land, b758_outcomes); T0, T1 and the wide direction (b758_coeff, b758_outcomes);
    the two routes of (6) (b758_standing_v1360, b758_standing_v1361); the statements of (7) (b758_epstein_statements); the dispatches
    (b758_dispatch_rows); the notes of (8) (b758_notes). Each object's name in the heading, for the line reader; every figure from the banks'
    feet, in digits; the apostrophe typographic and no backtick, (R368)(3)'s rule, which tools/standing/titlerule.py refuses at the landing."""
#⟪END⟫
#⟪SECTION record 31⟫
    _guard(f)
    oc_ = f['oc']
    j_, c_ = oc_['join'], oc_['coeff']
    jw_ = ('landed at %s = %s' % (j_['tag'], j_['peel'])) if j_['outcome'] == 'LANDED' else ('broken in run %s, no tag cut' % j_['run'])
    cw_ = ('landed at %s = %s' % (c_['tag'], c_['peel'])) if c_['outcome'] == 'LANDED' else (
        ('broken in run %s, standing on their branch at 596d1c9e' % c_['run']) if c_['outcome'] == 'BROKE' else 'not begun, standing on their branch at 596d1c9e')
    return ('## The landing under (R368): b757’s close by its four carried steps, %s (b758_corrigendum); the join of SIDE-explicit-formula’s four held '
            'branches %s (b758_presend, b758_land, b758_outcomes); T0, T1 and the one direction over the wider strip %s (b758_coeff, b758_outcomes); '
            'the two routes of (6), %d of 2 (b758_standing_v1360, b758_standing_v1361); the statements for sections 6 to 8 banked at %s '
            '(b758_epstein_statements); %d dispatches (b758_dispatch_rows); the notes of (8), %d written (b758_notes)' % (
                f['close_word'], jw_, cw_, f['routes'], f['st_rev'], f['disp_ef'] + f['disp_m24'], f['notes_written']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    # ### b758: the seat's read of what (R368) misses (data/b758_misses.txt), each item with what the act found at it, and the act's own
    cft_ = rdn('%s_coeff.txt' % ACT, optional=True) or ''
    cfm_ = re.search(r'print_targets\.txt at ([0-9a-f]{8}): (\d+) lines ; the union of its parents [0-9a-f]{8} and [0-9a-f]{8}: (\d+) ; outside the union (\d+) .*? ; '
                     r'left out (\d+), ', cft_)
    c4_ = ('(4) (5)`s removal of the union`s lines naming no declaration of the merged tree: the union %s lines, left out %s, the file at %s carrying %s, '
           'b757 (m) read as names outside a one-module target, each in the tree (relay data/b758_misses.txt :7-:8, data/b758_coeff.txt); ' % (
               cfm_.group(3), cfm_.group(5), cfm_.group(1), cfm_.group(2))) if cfm_ else '(4) (5) not begun, the join having broken (relay data/b758_outcomes.txt); '
    return ('(1) (1)`s "one CLAIM item (v)" where b757`s banks hold two, defects (v) and events (13), the corrigendum giving (v) in full and counting both (relay data/b758_misses.txt :3-:4, data/b758_corrigendum.txt); '
            '(2) b757`s scores close under v1.35.6 reading this act`s commits, tools and banks as b757`s and refuting N2, N4, N5 and S3, which step [9] read HELD; the author`s amendment of (R368)(1) bounding the readers at the next act`s opening commit, v1.35.7 (relay data/b758_events.txt (14), (15), data/b758_standing_v1357.txt); '
            '(3) (7)`s fourteen names, %d with no axioms line in the runs read: rQ_one and cQ_eq stand in no print_targets.txt at any tip read (relay data/b758_misses.txt :5-:6, data/b758_epstein_statements.txt); ' % f['st_noax']
            + c4_ +
            '(5) Component 5`s work begun before Component 3 and before the ceiling`s first reading, the reading when taken carrying nothing (relay data/b758_defects.txt (b), data/b758_ceiling.txt); and (8)`s read of the %d cites b757`s Epstein note moved: %d resolving, %d moved by two lines, %d naming no text line then, none edited (relay data/b758_moved_cites.txt); ' % (
                f['mv_cites'], f['mv_resolving'], f['mv_two'], f['mv_notext'])
            +
            '(6) %s and the seat’s %s defect%s as lettered' % (
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R368)(8)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b758's objects; b757's composer in git at
    b757's record tool). Its last line (R368)'s INTEGRATION line, composed from the banks' feet (_integ_line)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    sc_ = dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)   # ### version -> its commit
    sv_ = dict((x_[0], (x_[2], x_[3])) for x_ in f['vers'])   # ### version -> (cases, as wanted)
    vw_ = lambda v_: '%s at relay %s, controls %d of %d' % (v_, sc_[v_][:8], sv_[v_][1], sv_[v_][0])   # ### a standing version as the entry names it
    nl_ = '; '.join('(%s) %s, %d line%s added' % (k_, (c_ or '').split(' at ')[0], n_, '' if n_ == 1 else 's') for k_, _f, c_, n_ in f['notes'])
    oc_ = f['oc']
    j5_, c5_, cf5_ = oc_['join'], oc_['coeff'], f['cf'] or {}
    true5_ = [oc_[k_]['sentence'] for k_ in ('join', 'coeff') if oc_[k_]['outcome'] in ('LANDED', 'BROKE')]
    cft5_ = rdn('%s_coeff.txt' % ACT, optional=True) or ''
    cfm5_ = re.search(r'print_targets\.txt at ([0-9a-f]{8}): (\d+) lines ; the union of its parents [0-9a-f]{8} and [0-9a-f]{8}: (\d+) ; outside the union (\d+) .*? ; '
                      r'left out (\d+), ', cft5_)
    jp5_ = ('One dispatch at the tip, run %s: the build exited 0 at the dispatched commit with 0 error lines, the print ran and read %s axioms lines, each within '
            'the standard three, the two lines the filter refuses standing unprinted by name, no line naming sorryAx; main moved to the tip by the gated push`s '
            'default mode and %s cut at main`s read-back, %s, its peel read back at the remote equal to main (relay data/b758_outcomes.txt, '
            'data/b758_SIDE-explicit-formula_push-b758-land_push_out.txt); SIDE-explicit-formula`s local main fast-forwarded to it by (6)(i)`s route.' % (
                j5_['run'], (j5_['fields'] or {}).get('n', '-'), j5_['tag'], j5_['peel'])) if j5_['outcome'] == 'LANDED' else (
        'One dispatch at the tip, run %s, broke: main stands at %s and no tag was cut (relay data/b758_outcomes.txt).' % (j5_['run'], K.EF_BASE[:8]))
    if c5_['outcome'] == 'NOT READ':
        cp5_ = '(5) not begun, the join having broken: T0, T1 and the wide direction stand compiled on push-b757-coeff at 596d1c9e, as b757 left them.'
    else:
        cp5_ = ('push-b758-coeff made at main %s after (4)`s success and 596d1c9e merged into it without fast-forward at %s, print_targets.txt alone conflicted '
                'and resolved as the union of both sides, %s lines each once, %s left out as naming no declaration of the merged tree (relay data/b758_coeff.txt: '
                'the merge %s, the union %s, %d modules for %d names, %d refused, the five names lines %d of 5, controls %d of %d). ' % (
                    j5_['peel'], K.COEFF_LAND_BRANCH[1][:8], cfm5_.group(3) if cfm5_ else '-', cfm5_.group(5) if cfm5_ else '-', cf5_.get('merge', '-').lower(),
                    cf5_.get('union', '-').lower(), cf5_.get('modules', 0), cf5_.get('names', 0), cf5_.get('refused', 0), cf5_.get('five', 0),
                    (cf5_.get('ctl') or (0, 0))[0], (cf5_.get('ctl') or (0, 0))[1])) + ((
                    'One dispatch at the merged tip, run %s: as (4), and among the printed lines zq_coeff_not_multiplicative, cQ_forty_eight, cQ_not_nonneg, '
                    'wide_detector and zq_arith_side_re_neg, each within the standard three; main moved to the merged tip and %s cut at main`s read-back, %s, '
                    'its peel read back at the remote equal to main (relay data/b758_outcomes.txt, data/b758_SIDE-explicit-formula_push-b758-coeff_push_out.txt); '
                    'the local main fast-forwarded to it. The holds "no kernel`s main touched" and "no branch merged" lifted for SIDE-explicit-formula in this act '
                    'alone; the merged kernel branches deleted at the remote after %s was read back, each by name through the one-call tool: %s; the four held '
                    'branches of b725 to b730 kept.' % (c5_['run'], c5_['tag'], c5_['peel'], c5_['tag'], ', '.join('%s (was %s)' % (b_, t_[:8]) for b_, t_ in K.KERNEL_DELETES) or 'none'))
                    if c5_['outcome'] == 'LANDED' else
                    'One dispatch at the merged tip, run %s, broke: T0, T1 and the wide direction stand compiled on push-b757-coeff at 596d1c9e, and main stands at %s (relay data/b758_outcomes.txt).' % (
                        c5_['run'], j5_['tag']))
    e = ['', _title(), '',
         ' '.join(true5_) + (
             ' Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from them (relay data/b758_outcomes.txt); every build a '
             'runner dispatch read by its run id, %d in SIDE-explicit-formula of the 4 (10) allows and none elsewhere (relay data/b758_dispatch_rows.json); '
             'no lean process on this host; nothing computed at any field.' % f['disp_ef']), '',
         '*Filed at b758 on the author’s ruling `(R368)` and its one amendment row, (1) amended on the author’s word (relay data/b758_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b758_misses.txt`, `data/b758_corrigendum.txt`, `data/b758_standing_v1356.txt` to `data/b758_standing_v1362.txt`, `data/b758_presend.txt`, `data/b758_land.txt`, '
         '`data/b758_controls_control.txt`, `data/b758_controls.txt`, `data/b758_dispatch_rows.json`, `data/b758_outcomes.txt`, `data/b758_coeff.txt`, `data/b758_ceiling.txt`, '
         '`data/b758_epstein_statements.txt`, `data/b758_notes.json`, `data/b758_moved_cites.txt`, the gated push`s captures '
         '`data/b758_SIDE-explicit-formula_push-b758-land_push_out.txt` and `data/b758_SIDE-explicit-formula_push-b758-coeff_push_out.txt`, '
         '`data/b758_author_answers.txt`, `data/b758_events.txt`, `data/b758_defects.txt`, `data/b758_prelock.txt`, `data/b758_pathrefusal.txt`, '
         '`data/b758_address_scan.txt`, `data/b758_touch.txt`, `data/b758_standing_figures.txt`, `data/b758_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b757’s close and the corrigendum** ((R368)(1), amended, and (3)): the reader behind the FINDINGS line passing the head through the landing`s one conversion, %s (relay data/b758_standing_v1356.txt); '
         'b757`s scores close under it read this act`s commits, tools and banks as b757`s, the question put and the author`s answer, "Bound the readers, then close", with the amendment of (1) (relay data/b758_events.txt (14), (15)); '
         'the bound at this act`s opening commit, %s (relay data/b758_standing_v1357.txt); then b757`s four carried steps under it: [22] the scores close, %d of 8 HELD, %s, v0.38`s peel read at the remote; [23] the mirror; [24] the scores line; [25] the closing record (relay data/b757_scores_close.json, data/b757_closing.txt, committed at %s). '
         'The corrigendum of b757’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its CLAIM item (v) in full, '
         'and the findings after b757`s lock entered as events from the author`s relay in the delivery, CLAIM %s, CLOSE %s, %s repeats, at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b758_corrigendum.txt, route %s, banks %s; PLACE-papers %s). '
         'The title rule, an entry`s title and a bank`s head composed with the typographic apostrophe and the composer refusing a backtick in either, %s (relay data/b758_standing_v1358.txt). The version at the close %s.' % (
             vw_('v1.35.6'), vw_('v1.35.7'), f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', K.B757_CLOSE[:8],
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'],
             f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], f['corr_line'], f['corr_row'], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], vw_('v1.35.8'), f['ver']), '',
         '**The kernel route and the dispatches** ((R368)(4), (5)): the one-call tool opened for this act in SIDE-explicit-formula before any kernel write, print_targets.txt named for (5)`s merge, %s (relay data/b758_standing_v1359.txt). '
         'The dispatch and the read by tools/b758_controls.py, carried from b757`s tool and set for this act`s two items and caps, committed before its opening dispatch, its own controls %d of %d as wanted (relay data/b758_controls_control.txt); %d runs read with the build exiting 0, the axioms print run in %d, its controls %d of %d (relay data/b758_controls.txt). '
         'The pushes by tools/push_gated.sh as it stands, its branch mode with --scratch for each push-b758-* branch and its default mode for main and each tag, each read back.' % (
             vw_('v1.35.9'), f['cc_ctl'][0], f['cc_ctl'][1], f['cb_kernel'], f['cb_printed'], f['cb_ctl'][0], f['cb_ctl'][1]), '',
         '**The join** ((R368)(4)): push-b758-land made at push-b757-join`s tip %s, its one commit %s renaming sRe to timeSRe in Schema/ZQ/OffZero/Time.lean with its uses in that file, Sums.lean keeping its name, no statement`s meaning changed (relay data/b758_land.txt: the branch %s, %d modules for %d names, %d refused, controls %d of %d). '
         'The two pre-send reads at that tip, banked before the dispatch (relay data/b758_presend.txt): each fully qualified declaration name in one module, duplicates %d; each line of print_targets.txt against the workflow`s filter, %d refused (%s), named as lines no print can reach by this workflow, the file not edited for them and the workflow not widened; anonymous pairs %d of %d (%d unread); controls %d of %d. '
         '%s' % (
             K.JOIN_BRANCH[1][:8], K.LAND_BRANCH[1][:8], f['la_word'].lower(), f['la_modules'], f['la_names'], f['la_refused'], f['la_ctl'][0], f['la_ctl'][1],
             f['ps_dup'], f['ps_refused'], f['ps_refused_lines'], f['ps_anon'][0], f['ps_anon'][1], f['ps_anon'][2], f['ps_ctl'][0], f['ps_ctl'][1], jp5_), '',
         '**T0, T1 and the wide direction** ((R368)(5)): %s' % cp5_, '',
         '**The two routes, the arm and the face** ((R368)(6)): (i) a fast-forward of a kernel`s local main to its remote`s main, refused where the local main is not an ancestor of the remote`s, read back, %s, its control a refusal on a planted divergent main in a scratch clone (relay data/b758_standing_v1360.txt); used for SIDE-dirichlet-mod-24`s local main and for SIDE-explicit-formula`s after each landing (relay data/b758_events.txt (38), (47)); '
         '(ii) a push of a named commit to a named non-main branch of a kernel, not forced, refused where the branch`s remote tip is not an ancestor, read back, %s, its control a refusal on a planted non-ancestor (relay data/b758_standing_v1361.txt), built for the acts after, zq-b730 staying at %s; '
         'G-TRAIL-CARRIES-SEAL reading the tools` names from the trail bank, its control b756`s trail and b757`s, and the kernels face naming SIDE-dirichlet-mod-24, %s (relay data/b758_standing_v1362.txt). The routes: %d of 2.' % (
             vw_('v1.36.0'), vw_('v1.36.1'), K.ZQ_TIP[:8], vw_('v1.36.2'), f['routes']), '',
         '**The statements for sections 6 to 8** ((R368)(7)), banked and not written: the fourteen names at %s, %d of them found as one declaration, each with its file and line, its statement as written and its docstring, and its axioms line with the run that printed it, %d with no axioms line in the runs read; the heads of sections 6 to 8 of THE_EPSTEIN_CONTROL_OBJECT_v0_1.md by path, line range and the head line`s digest, %d of 3; controls %d of %d (relay data/b758_epstein_statements.txt, tools/b758_statements.py at %s). The navigator drafts the sections from that bank; they enter the document in the act the author names.' % (
             f['st_rev'], f['st_found'], f['st_noax'], f['st_sections'], f['st_ctl'][0], f['st_ctl'][1], K.STATEMENTS_GEN[:8]), '',
         '**The notes of (8)**: five PLACE-papers commits through the one-call tool with its scan, each composed by tools/b758_notes.py (relay %s, committed before its run) of the document`s own dated head and the sentences of (4) and (5) that came true, read from the outcomes bank and matched against the ruling`s template for the outcome: %s; no sentence above a note edited (relay data/b758_notes.json). '
         'The %d relay lines whose cites b757`s Epstein note moved, read by the citation tool`s helpers against the document at HEAD: %d cites, %d resolving, %d moved by two lines, %d naming no text line at b757`s write, %d elsewhere, %d gone, %d relay line%s not as b757 counted, each printed and none edited (relay data/b758_moved_cites.txt). '
         'OPEN_TRAILS` block: b757`s root answer; the two lines the seat resolved at b757 standing as written, the author having struck neither; W-ORD-SQUARES-AT-24 taking its price as the ruling gives it, the navigator`s, from no build.' % (
             K.C3_NOTES_GEN[:8], nl_, f['mv_lines'], f['mv_cites'], f['mv_resolving'], f['mv_two'], f['mv_notext'], f['mv_elsewhere'], f['mv_gone'], f['mv_uncounted'],
             '' if f['mv_uncounted'] == 1 else 's'), '',
         '**The side rule, narrowed** ((R368)(9)): N3`s side matcher reads the act`s sentences with each line headed by a dated record`s file and line and the report`s separator left out, every other matcher reading them as before; one control of each kind, a sentence of the act`s about a result caught and a line in b757`s sweep bank`s form passed; read against b757`s sweep bank, not rewritten (relay data/b758_events.txt (41)).', '',
         '**The ceiling** ((R368)(2)): %d reading%s against 16 hours from the delivery, the last at %s, %s h, %s (relay data/b758_ceiling.txt); the first taken after Component 5`s work had begun (relay data/b758_defects.txt (b)). The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b758_misses.txt).' % (
             f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower()), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b758_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; each standing change a commit of its own moving VERSION with its controls bank, before its use; each act tool committed before it ran; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after its run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b758_prelock.txt, data/b758_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero'))), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula`s tree and the two local mains of (6)(i); no push forced; no tag moved, v0.38 and v0.2.0 among them; no toolchain or Mathlib pin moved; no sentence of any paper edited, each write of (8) a note beside the text; no anchor edited; nothing computed at any field; no lean process on this host; no ledger row edited beyond the corrigendum, this entry, the trail and the notes of (8); the draft held at v5.', '',
         '**The research instruments not reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run calls rows that compute at a field, the Epstein control`s and the class groups at -23 and -15 among them, which (R368)(10) bars, nothing computed at any field; neither the run nor a part of it was run, and the arm fails at the gate, declared so on the face.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b758_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b758_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b758 -- %s, %s, %s, %s -- against b757’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b758_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b758_citation_check.txt, data/b758_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the control read from its coefficients and from its zeros now stands on one main where the tags give it -- the coefficient law at the fields of class number 2 and the Epstein instance with its located zero beside the halved coefficients that fail multiplicativity at 2 and 3 and the coefficient at 48 with its sign; whether the located zero and the failed multiplicativity are one fact told from two sides is the navigator`s reading to make in the sections the statements bank feeds, promoting nothing; none is a finding about zeta.', '',
         '**Carried to:** %s, per (R368)(10), as the author answers the one question at the root: sections 6 to 8 entered from the navigator`s draft with the author`s word; or the written proof of the class-number-3 coefficient law with the four carried orders priced beside it; or another the author names. W-ORD-KEIPER-FACE and the two lines the seat resolved at b757 stand as written; W-ORD-SQUARES-AT-24 priced as the ruling gives it; the route of (6)(ii) built and unused; the reproduction run, not run at this act; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH, GRH or Weil positivity on classK holds or fails, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b757_body():
    """b755's paragraphs over b755's objects, kept for the record and not called (b756, Component 6): held as text, their names b755's
    locals, which the gate's report dry (tools/standing/reportdry.py unbound) read as live unbound globals beside _finding_text's own (defect (j))."""
    return r"""
    e = [
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b758_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b758_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b758_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b758_zeros_from_primes_59.txt, data/b758_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b758 on the author’s ruling `(R368)` and its two amendment rows (relay data/b758_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b758_corrigendum.txt`, `data/b758_carried_faults.txt`, `data/b758_standing_v1346.txt`, `data/b758_walk.txt`, `data/b758_coeffs_controls.json`, `data/b758_literature.txt`, '
         '`data/b758_cand_a.txt` to `data/b758_cand_l_plant.txt`, `data/b758_candidates.txt`, `data/b758_ceiling.txt`, `data/b758_registrations.txt`, `data/b758_roots_59.txt`, '
         '`data/b758_list_59.txt`, `data/b758_list_59_controls.txt`, `data/b758_zeros_from_primes_59.txt`, `data/b758_recur_59.txt`, `data/b758_recur_control.txt`, '
         '`data/b758_census_from_primes.txt`, `data/b758_l16.json`, `data/b758_put_1.json`, `data/b758_put_2.json`, `data/b758_author_answers.txt`, `data/b758_events.txt`, '
         '`data/b758_defects.txt`, `data/b758_prelock.txt`, `data/b758_pathrefusal.txt`, `data/b758_reproduce.txt`, `data/b758_address_scan.txt`, `data/b758_touch.txt`, '
         '`data/b758_standing_figures.txt`, `data/b758_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R368)(1), (2); relay %s, %s, PLACE-papers %s): b757 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b757’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b758_corrigendum.txt). Its three repairs: the lock gate carried as tools/b758_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b758_standing_v1346.txt; the amendment row 1). '
         'The open items of b757`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b758_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R368)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b758_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b758_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b758_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b758_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R368)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b758_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b758_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R368)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b758_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes’ phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b758_candidates.txt, data/b758_cand_a.txt to data/b758_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R368)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b758_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b758_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b758_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b758_zeros_from_primes_59.txt, data/b758_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b758_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b758_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R368)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b758_defects.txt (l)); its generator committed at relay %s before its run (relay data/b758_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R368)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b758_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R368)(8)): the price table at step zero from banked timings where a bank held one (relay data/b758_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b758_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b758_stepzero.txt); step zero from %s (data/act_current.json) through b757`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]’s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b758_prelock.txt, data/b758_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b758_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b758_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b758_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b757: [U3] in force, the counter's line as it prints (its event in data/b757_events.txt (22))
         '**The standing arms**: the four figures at b758 -- %s, %s, %s, %s -- against b757’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b758_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b758_citation_check.txt, data/b758_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R368)(8), as the author answers the one question at the root: the clearing act as b758 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]’s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b758 with the clearing act after it; defects (b), (e) and the tools’ (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH, GRH or Weil positivity on classK holds or fails, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)
"""


def _finding_text_b757():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b758's objects): the ledger writes; b757's close; the outcomes of (4) and (5); the dispatches; the routes of
    (6); the statements of (7); the ceiling; the open-orders line from tools/standing/orders.py's output over the trail at HEAD; the standing
    versions; the kernels."""
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
    oc_ = f['oc']
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    nl_ = '; '.join('(%s) %s' % (k_, (c_ or '').split(' at ')[0]) for k_, _f, c_, _n in f['notes'])
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R368) ratified.** Its components as the ferry orders them (relay data/b758_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b757), :%s (the entry); the five notes of (8), %s, OPEN_TRAILS.md`s block among them under one dated head; no sentence of a paper edited; this record.' % (
                 f['corr_line'], fj.get('entry_line'), nl_), '',
             '**b757’s close** ((R368)(1), amended): steps [22] to [25] under v1.35.7, the scores %d of 8 HELD (%s), the mirror and the closing record (relay data/b757_scores_close.json, data/b757_closing.txt, committed at %s).' % (
                 f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', K.B757_CLOSE[:8]), '',
             '**The outcomes** ((R368)(4), (5)): the join %s, run %s%s; the three results %s%s (relay data/b758_outcomes.txt).' % (
                 f['join_word'], oc_['join']['run'], (' = %s' % oc_['join']['peel']) if oc_['join']['outcome'] == 'LANDED' else '',
                 f['three_word'], (', run %s = %s' % (oc_['coeff']['run'], oc_['coeff']['peel'])) if oc_['coeff']['outcome'] == 'LANDED' else (
                     (', run %s' % oc_['coeff']['run']) if oc_['coeff']['outcome'] == 'BROKE' else ', (5) not begun')), '',
             '**The dispatches:** SIDE-explicit-formula %d of the 4 (10) allows, none elsewhere, each read by its run id, the exit file governing (relay data/b758_dispatch_rows.json).' % (
                 f['disp_ef']), '',
             '**The routes** ((R368)(6)): %d of 2 -- (i) the fast-forward of a kernel`s local main, used; (ii) the push to a named non-main branch, built and unused; the arm and the face beside them (relay data/b758_standing_v1360.txt to data/b758_standing_v1362.txt).' % f['routes'], '',
             '**The statements** ((R368)(7)): the fourteen names at %s, %d with no axioms line in the runs read; sections 6 to 8 by their heads, %d of 3 (relay data/b758_epstein_statements.txt).' % (
                 f['st_rev'], f['st_noax'], f['st_sections']), '',
             '**The ceiling:** %d reading%s, the last at %s, %s h of 16, %s (relay data/b758_ceiling.txt).' % (f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower()), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s (relay data/b758_standing_v1356.txt to data/b758_standing_v1362.txt); HANDOFF.md regenerated once by tools/standing/handoff.py before the gate, at relay %s.' % (
                 '; '.join('%s %d of %d' % (v_, w_, n_) for v_, _c, n_, w_ in f['vers']), (K.HANDOFF_COMMIT or 'NOT MADE')[:8]), '',
             '**The instruments not reproduced:** the run not run at this act, its rows computing at a field, which (R368)(10) bars; G-RESEARCH-REPRODUCES declared failing on the face.', '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b758_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b758_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b758 `%s` (previous `%s`, b757’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b758_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b758_standing_v1362.txt); the standing '
             'report tool (relay data/b758_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    lt5_ = [oc_[k_] for k_ in ('join', 'coeff') if oc_[k_]['outcome'] == 'LANDED']
    rows_ += ['**The kernels:** SIDE-explicit-formula`s main at %s (entering at %s), %s; %s at %s and %s at %s, %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24`s local main at %s by (6)(i), %s at %s; no kernel beyond SIDE-explicit-formula`s tree and the two local mains touched; the %s branches as b758 found them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  (lt5_[-1]['peel'] if lt5_ else K.EF_BASE[:8]), K.EF_BASE[:8], ', '.join('%s at %s' % (x_['tag'], x_['peel']) for x_ in lt5_) or 'no tag cut', K.LAND_BRANCH[0], K.LAND_BRANCH[1][:8],
                  K.COEFF_LAND_BRANCH[0], (K.COEFF_LAND_BRANCH[1] or '-')[:8], ('deleted at the remote after v0.40, with push-b757-join and push-b757-coeff' if K.KERNEL_DELETES else 'standing at the remote'),
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root with the two ledgers’ cuts beside it (the ferry`s Component 5), HANDOFF.md among its files, its file named in the closing by its name, bytes and hash and its folder by role (relay data/b758_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b757’s %s, %s, %s, %s (relay data/b758_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b758_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b757():
    """b753's trail record over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: at most 14 in SIDE-explicit-formula and 4 in SIDE-dirichlet-mod-24 ((R368)(10)), 6 and 2 sent; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: every run read by its id from its artifact, the exit file governing (data/b758_dispatch_rows.json); MEASURED off the worklist`s EF_RUNS and M24_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b757*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved, the join and push-b758-coeff made beside them; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b758 found them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b757*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act, the four unmoved; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 2, 2, 'files', '### (R368)(6)(ii): SIDE-dirichlet-mod-24`s main moved to e5ebdd15 after run 43836415096`s success, SIDEDirichletMod24/Units.lean added and the root import SIDEDirichletMod24.lean edited (git diff --name-status 597b0869 e5ebdd15); SIDE-explicit-formula`s main unmoved at 8fbab45d.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b757-closing, push-b757-preroot, push-b757-record; PLACE-papers push-b757-preroot, push-b757-record; each local, by name, through the one-call tool, after the --merged listing (data/b758_stepzero.txt :62-:69).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 1, 1, 'files', '### (R368)(6)(i): .github/workflows/build-module.yml in SIDE-dirichlet-mod-24 at 22282733, a file and no Lean, main moved to it ahead of its control dispatch.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY`s header replaced in place under (R368)(8)(iv) (PLACE-papers 3e85e952) and one dated note appended at its end under (9)(d) (c45be6e0), no row.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### (R368)(8)(iv): the header at :13, the one line replaced in place, no line moving; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R368)(1): FINDINGS :15416 (relay data/b758_corrigendum.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R368)(1): row (77).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R368) orders none).'),
    ('outcome sentences composed from the banks', 5, 5, 'sentences', '### (R368)(4)-(7): the join`s, T0`s, T1`s, the modulus-24 module`s and the wide direction`s, each the ruling`s for the outcome its bank reads, its fields filled from the banks (relay data/b758_outcomes.txt).'),
    ('notes of (9) written, each by one PLACE-papers commit', 5, 5, 'notes', '### (R368)(9)(a)-(e): PLACE-papers e88282c4, c7dfe43c, 9c0896c5, c45be6e0 and b14256c2, 2, 14, 2, 2 and 18 lines added and none removed, each confirmed against its bytes (relay data/b758_notes.json).'),
    ('cites moved by (9)(a)`s insertion, printed before the write', 231, 231, 'cites', '### (R368)(9)(a): on 134 lines, 11 in PLACE-papers and 123 in the relay, none edited, an upper bound as the reader counts (relay data/b758_notes_moved.txt).'),
    ('lines saying one of the three statements, read by the sweep', 24, 24, 'lines', '### (R368)(9) by (R367)(2)(b): 0 overtaken, 1 as the record reads, 23 a dated record, 0 unread (relay data/b758_sweep.txt).'),
    ('repairs of (8) landed, each with its control', 5, 5, 'repairs', '### (R368)(8)(i)-(v) (relay data/b758_cut.txt, data/b758_standing_v1355.txt, data/b758_ghcalls.txt, data/b758_registry_line.txt, data/b758_doors.txt).'),
    ('repository descriptions sent and read back equal', 2, 2, 'descriptions', '### (R368)(8)(v): PLACE-papers and SIDE-kernel, by tools/b758_doors.py (relay data/b758_doors.txt).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-SQUARES-AT-24 entered in (9)(e)`s block before the seal (PLACE-papers b14256c2), not with the trail.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: not run at b758, the run computing at a field where (R368)(10) bars it; MEASURED off data/b758_reproduce.json, absent.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### the tools` runs over the record and the runner`s prints, none at a field ((R368)(10)): the price, the two standing versions` controls and the live control, the controls tool`s controls and its runs, the join, the outcomes, the ceiling, the header line, the doors, the gh-call reader, the sweep, the cut, the moved cites, the probe-path refusal, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### none: (R368)(5) registers no test on either statement, a theorem taking a compile outcome and no verdict, and no data/b758_registrations.txt is written; MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2): no registered object this act, nothing computed at any field but the builds; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### five added: Schema/ZQ/Mechanism/NoEuler.lean and CoeffSign.lean (T0, T1) and Schema/Wide/HalfScale.lean and HalfScaleControl.lean ((7)) on push-b758-coeff, SIDEDirichletMod24/Units.lean ((6)); MEASURED off push-b758-coeff against zq-b730`s tip and SIDE-dirichlet-mod-24`s main against its base.'),
    ('Lean files edited on the join branch', 'EFEDIT', 'EFEDIT', 'files', '### (R368)(4)(i), (ii): Schema/EpsteinZQ.lean`s two docstrings and KeiperTwo.lean`s alternatives, each its own commit (6f2d7e26, e90ae384), no statement changed; MEASURED off the join branch`s commits after its fourth merge.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R368)(3), (8)(ii): tools/standing/ v1.35.4 and v1.35.5, each by a version commit of its own with its controls in its bank (data/b758_standing_v1354.txt, data/b758_standing_v1355.txt); MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b758_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, the dispatches and the artifact downloads, the gh reads and the two description writes under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b757: no registered object and no figure bank ((R367)(5): no test registered on either statement)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    # ### b758 step zero: the runs' count read against (R368)(10) (SIDE-explicit-formula's alone, M24_RUNS empty); EFNEW and EFEDIT below
                    # ### are b757's and are rewritten for (4) and (5) at Component 5
                    EFRUNS=len(K.EF_RUNS) + len(K.M24_RUNS),
                    REPROWS=jcount('b758_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b758_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    # ### b757: the modules this act added, on push-b757-coeff past zq-b730's tip and on SIDE-dirichlet-mod-24's main past its base
                    EFNEW=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=A', K.ZQ_TIP, K.COEFF_BRANCH[1]).split() if f_.endswith('.lean'))
                    + sum(1 for f_ in _git(K.M24_DIR, 'diff', '--name-only', '--diff-filter=A', K.M24_BASE, K.M24_MAIN).split() if f_.endswith('.lean')),
                    # ### b757: the Lean files the join branch's own commits edit after its fourth merge ((R367)(4)(i), (ii))
                    EFEDIT=len(set(f_ for c_ in _git(K.EF_DIR, 'rev-list', '--no-merges', '%s..%s' % (dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS)['merge4'], K.JOIN_BRANCH[1])).split()
                                   for f_ in _git(K.EF_DIR, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split() if f_.endswith('.lean'))),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('price', 'standing_v1354', 'standing_v1354_live', 'controls_control', 'controls', 'join', 'outcomes', 'ceiling',
                                               'registry_line', 'doors', 'ghcalls', 'standing_v1355', 'sweep', 'cut', 'notes_moved', 'pathrefusal', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b758_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b758_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFEDIT', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b758_registration_%s.txt -- b758, THE BUILD: b757 AT ITS WEIGHT AND ITS CORRIGENDUM; THE ROUTE FOR KERNEL WRITES, v1.35.4; "
                             "THE JOIN BROKE AT THE IMPORT, MAIN UNMOVED; T0 AND T1 COMPILED ON push-b758-coeff; THE MODULUS-24 MODULE COMPILED AT v0.2.0; "
                             "THE WIDE DIRECTION COMPILED; FIVE REPAIRS, v1.35.5; THE NOTES OF (9); NO DEPOSIT, UNDER (R368)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b757's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b758: b757's lines read banks this
act does not write, and are not carried; the lines are b758's: T0 and T1, the modulus-24 module and the wide direction, each from its runner
read by run id (KERNEL); tools/standing/ v1.35.4 and v1.35.5 and the controls tool by their controls (CERTIFIED); the notes of (9), the five
repairs and the two descriptions (REGISTERED); the join broken at the import, the reproduction run not run, and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b757's lines, each from the record tool's figures over b757's banks (REC._figs), the record's guard first
    REC._guard(f)
    ch_, oc_ = dict(K.CHAIN), f['oc']
    # ------------------------------------------------------------------ KERNEL: (R367)(5), T0 and T1 on push-b757-coeff, each read by its run id
    s5 = seat('%s_outcomes.txt' % ACT, '## (5) T0 ')
    keys['T0T1'] = ('KERNEL -- T0 AND T1 ON %s, BUILT PAST zq-b730`S TIP THE JOIN HAVING FAILED: T0 %s at %s in %s lines against the stop 360, run %s, its %s names each within the standard three; T1 %s at %s in %s lines against the stop 1,350, run %s, its %s names each within the standard three; no main moved, no v0.40. SOURCE %s.' % (
        K.COEFF_BRANCH[0], f['t0_word'], oc_['T0']['sha'], oc_['T0']['lines'], oc_['T0']['run'], oc_['T0']['names'], f['t1_word'], oc_['T1']['sha'], oc_['T1']['lines'],
        oc_['T1']['run'], oc_['T1']['names'], s5['text']))
    seats.append(s5)
    # ------------------------------------------------------------------ KERNEL: (R367)(6), the modulus-24 module, read by its run id
    s6 = seat('%s_outcomes.txt' % ACT, '## (6) THE MODULUS-24 MODULE')
    keys['MOD24'] = ('KERNEL -- THE MODULUS-24 MODULE IN SIDE-dirichlet-mod-24: %s in run %s, its %s names; main moved to %s after that run`s success and %s cut at the read-back (object %s), its peel read back at the remote equal to main. SOURCE %s.' % (
        f['m24_word'], oc_['mod24']['run'], oc_['mod24']['names'], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[1][:8], s6['text']))
    seats.append(s6)
    # ------------------------------------------------------------------ KERNEL: (R367)(7), the wide direction, read by its run id (the name the template appends)
    sk = seat('%s_outcomes.txt' % ACT, '## (7) THE ONE DIRECTION OVER THE WIDER STRIP')
    keys['WIDE'] = ('KERNEL -- THE ONE DIRECTION OVER THE WIDER STRIP ON %s AT %s: %s in %s lines and one dispatch, against the navigator`s price of 250 to 550 lines and 4 to 8 dispatches, run %s, its %s names each within the standard three; no main moved and no tag cut by it. SOURCE %s.' % (
        K.COEFF_BRANCH[0], oc_['wide']['sha'], f['wide_word'], oc_['wide']['lines'], oc_['wide']['run'], oc_['wide']['names'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.35.4 and v1.35.5 ((R367)(3), (8)(ii)), by their controls
    sv = seat('%s_standing_v1355.txt' % ACT, '**v1.35.5: CONTROLS ')
    keys['VERSIONS'] = ('CERTIFIED -- tools/standing/ v1.35.4 AND v1.35.5, each by a commit of its own moving VERSION, its controls all as wanted: %s; the live commit in each kernel %d of %d. SOURCE %s.' % (
        '; '.join('%s at relay %s, %d of %d' % (v_, dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)[v_][:8], w_, n_) for v_, _c, n_, w_ in f['vers']), f['live'][0], f['live'][1], sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: (R367)(3), the dispatch and read tool by its own controls (the name the template appends)
    sw = seat('%s_controls_control.txt' % ACT, '**THE TOOL`S CONTROLS: ')
    keys['CONTROLS'] = ('CERTIFIED -- tools/b758_controls.py BY ITS OWN CONTROLS: 14 of 14 as wanted, committed at relay %s before its opening dispatch; every run read by its id, the exit file governing, %d dispatches in SIDE-explicit-formula of 14 and %d in SIDE-dirichlet-mod-24 of 4. SOURCE %s.' % (
        ch_['controls_gen'][:8], f['disp_ef'], f['disp_m24'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: (R367)(9), the notes, each by one PLACE-papers commit
    sa = seat('%s_notes.json' % ACT, '"confirm"')
    keys['NOTES'] = ('REGISTERED -- THE NOTES OF (9): five PLACE-papers commits (%s), %d lines added and none removed, each composed from the outcomes bank by the tool of the notes at relay %s, committed before its run, and matched whole against the ruling`s template for its outcome. SOURCE %s.' % (
        ', '.join((c_ or '').split(' at ')[0].replace('PLACE-papers ', '') for _k, _f, c_, _n in f['notes']), f['notes_written'], K.C3_NOTES_GEN[:8], sa['text']))
    seats.append(sa)
    # ------------------------------------------------------------------ REGISTERED: (R367)(8), the five repairs, each by its control
    sr = seat('%s_cut.txt' % ACT, '**(8)(i): CONTROLS ')
    keys['REPAIRS'] = ('REGISTERED -- THE FIVE REPAIRS OF (8), EACH WITH ITS CONTROL: %d landed of 5 -- (i) the cut, on b757`s bank whole the check %s, on the planted second result it %s; (ii) the closing`s one count, v1.35.5; (iii) N5`s reader, %d sends over b757`s banks where the carried reader read %s; (iv) REGISTRY`s header at :%d, %d lines moved, PLACE-papers %s; (v) the two descriptions, %d of %d read back equal. SOURCE %s.' % (
        f['repairs'], f['cu_whole'].lower(), f['cu_plant'].lower(), f['gh_taught'], f['gh_carried'].lower(), f['rg_line'], f['rg_moved'], dict(K.PP_CHAIN)['pp_registry'][:8],
        f['ds_equal'][0], f['ds_equal'][1], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: (R367)(4), the join, broken at the import
    sj = seat('%s_outcomes.txt' % ACT, '## (4) THE JOIN')
    keys['JOIN'] = ('HELD -- THE JOIN OF THE FOUR BRANCHES, BROKEN: run %s at %s built every module and its axioms print failed at the import, OffZero.Time and OffZero.Sums declaring sRe in one namespace; main standing at %s, no v0.39, the four branches as they stood; the two files outside (10)`s (W) list. SOURCE %s.' % (
        oc_['join']['run'], K.JOIN_BRANCH[1][:8], K.EF_BASE[:8], sj['text']))
    seats.append(sj)
    # ------------------------------------------------------------------ HELD: the reproduction run, not run ((R367)(10))
    s7 = seat('%s_ferry.txt' % ACT, 'nothing computed at any field, the builds apart')
    keys['REPRO'] = ('HELD -- THE REPRODUCTION RUN, NOT RUN: its rows compute at a field, which (R368)(10) bars, the builds apart; neither the run nor a part of it run; G-RESEARCH-REPRODUCES declared failing on the face. SOURCE %s.' % s7['text'])
    seats.append(s7)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R367)(10))
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['T0T1', 'MOD24', 'WIDE']), ('CERTIFIED', ['VERSIONS', 'CONTROLS']), ('REGISTERED', ['NOTES', 'REPAIRS']), ('HELD', ['JOIN', 'REPRO', 'HELD'])]
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
