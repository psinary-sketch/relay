# -*- coding: utf-8 -*-
# b755 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R365)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R365)(2) repair it carries. Edited by the Edit tool. Carried at b755 by tools/b755_fold.py (`carry`) from tools/acts/b754.py,
# b754`s names substituted; the citation`s sections adopted from tools/b755_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b754`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b754`s carried till
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
# ### b755, Component 1: THE c1 ROUTE FOR b754'S WEIGHT LINE AND ITS SHORT CORRIGENDUM, (R365)(1), (2), written by the Edit tool against b754's
# ### banks (79 events, 16 post-seal events, 70 defects, 21 refusals), the v1.34.6 controls (relay eac02515) and the carried faults bank; short, as
# ### (2) orders: the counts from the banks, the CLAIM items in full, the three repairs. The carried stub (tools/standing/carry.py v1.34.0) removed
# ### by the Edit tool; nothing composed by it.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_PREV_CLOSE = '28255aea'          # ### b754's closing step-row commit, the public relay's main at step zero ((R365)(1))
C1_CLOSING_COMMIT = '8b957792'      # ### b754's closing commit (its closing row, data/b754_steps.json)
C1_PP_RECORD = '0545f368'           # ### b754's PLACE-papers record commit (its pp record row)
C1_NOTED = '2026-11-14'
C1_CORRIGENDA_LAST = 74
C1_STANDING = 'eac02515'            # ### v1.34.6's own commit ((R365)(2)(iii), with the amendment row 1's two phases)
C1_LOCKGATE = '9a2e55b6'            # ### tools/b755_lockgate.py carried and committed before it runs ((R365)(2)(i))
C1_V1346 = 'b755_standing_v1346.txt'
C1_FAULTS = 'b755_carried_faults.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-14 by b755 to b754’s entry (:%d), under `(R365)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The sitting under (R364): the reference layer’s four anchors'
C1_TRAIL_NEEDLE = '### b754 — lane two, act one hundred and eighty-one, the sitting under (R364)'
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b754_events.txt'), ('postseal', 'b754_events_postseal.txt'), ('defects', 'b754_defects.txt'))
C1_RULES = ((1, r'^  \(1\) \(S1\), '), (5, r'^  \(5\) \(S5\), '), (6, r'^  \(6\) \[Q\] \(1\), '), (9, r'^  \(9\) \[Q\] \(4\), '),
            (10, r'^  \(10\) \[U1\], '), (11, r'^  \(11\) \[U2\], '), (12, r'^  \(12\) \[U3\], '))
C1_CORR_TITLE = ('## Corrigendum to b754’s record, short (relay data/b754_events.txt rows (1)-(79), data/b754_events_postseal.txt rows (80)-(95) and '
                 'data/b754_defects.txt (a)-(s’’)): its events and defects by count from their banks, the thirteen CLAIM items in full, and the three '
                 'repairs of `(R365)`(2), the lock gate, no post-seal events bank and the mirror’s folder by role')


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
    return subprocess.run(['git', '-C', repo or ROOT] + list(a), capture_output=True, text=True, encoding='utf-8')


def _c1_rows(name):
    """[(id, owner, tag, column, text)] of a bank's rows in bank order: a row opens at four spaces with (id) and its lines after, at five
    spaces or more, are joined to it -- b754's post-seal row (92) carries its tag across two lines (data/b755_carried_faults.txt (20)), which
    the standing counter's one-line reader refuses; an untagged row exits, nothing composed."""
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
    """a bank's own words for the ledger (b754's form): markdown's marks escaped; a pair of backticks quoting a span (the first after a space or
    a bracket, or at the line's head) read as quotes, every other backtick as an apostrophe; the template's placeholder brackets as angles."""
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


def _c1_weight():
    head = _c1_rd('b754_closing.txt').split(NL)[0]
    pub = _c1_git('show', '%s:data/b754_closing.txt' % C1_PREV_CLOSE).stdout.replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b754_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    on_main = _c1_git('merge-base', '--is-ancestor', C1_PREV_CLOSE, 'origin/main').returncode == 0
    steps = json.load(open(os.path.join(D, 'b754_steps.json'), encoding='utf-8')).get('rows') or []
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    prec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'pp']
    if not on_main or C1_CLOSING_COMMIT not in clo or C1_PP_RECORD not in prec:
        sys.exit('### %s on the pushed main %s ; closing %s ; pp record %s -- NOTHING COMPOSED' % (C1_PREV_CLOSE, on_main, clo, prec))
    for n_, pat_ in C1_RULES:
        _c1_fl('b754_rules.txt', pat_, 'the rules bank`s row (%d)' % n_)
    return (C1_WEIGHT_HEAD + ' -- b754 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b754_closing.txt):* “%s” (data/b754_closing.txt :1, the public relay '
            'at %s). Its closing commit %s and its step-row commit %s stand on the relay’s pushed main, PLACE-papers at its record %s, and the rules of '
            'data/b754_rules.txt bind b755 as `(R365)`(1) reads them: the sourcing rules, rows (1) to (5); the quoting rule, rows (6) to (9), read by N5; '
            '[U3], row (12); [U1] and [U2], rows (10) and (11), not in force at this act.') % (head, C1_PREV_CLOSE, C1_CLOSING_COMMIT, C1_PREV_CLOSE, C1_PP_RECORD[:7])


def _c1_state():
    s = dict((k_, _c1_rows(n_)) for k_, n_ in C1_BANKS)
    ev, ps, df = s['events'], s['postseal'], s['defects']
    tot = _c1_tally(ev + ps + df)
    cnt, l_cn = _c1_fl('b754_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    rf = [l for l in _c1_rd('b754_hook_refusals.txt').split(NL) if l.strip()]
    kinds = {}
    for l in rf:
        m = re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \| ([A-Z]+) \| ', l)
        kinds[m.group(1) if m else '?'] = kinds.get(m.group(1) if m else '?', 0) + 1
    foot = [l for l in _c1_rd(C1_V1346).split(NL) if l.startswith('### ### **v1.34.6: CONTROLS')]
    vm = re.search(r'CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED', foot[0]) if len(foot) == 1 else None
    ff = [l for l in _c1_rd(C1_FAULTS).split(NL) if l.startswith('### ### **THE CARRIED FAULTS : ')]
    fm = re.search(r'(\d+) ROWS FROM (\d+) ITEMS .*; REPAIRED HERE 0 ;', ff[0]) if len(ff) == 1 else None
    cr_ = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    lg = _c1_git('log', '-1', '--format=%H', C1_LOCKGATE, '--', 'tools/b755_lockgate.py').stdout.strip()
    st = _c1_git('log', '-1', '--format=%H', C1_STANDING, '--', 'tools/standing/VERSION').stdout.strip()
    ver = _c1_git('show', '%s:tools/standing/VERSION' % C1_STANDING).stdout.strip()
    bad = [k_ for k_, ok_ in (
        ('the event rows (1)-(79)', [int(r[0]) for r in ev] == list(range(1, 80))),
        ('the post-seal rows (80)-(95)', [int(r[0]) for r in ps] == list(range(80, 96))),
        ('the defect rows 70, the last (s``)', len(df) == 70 and df[-1][0] == "s''"),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev) + len(ps)) == tuple(int(x) for x in cnt)),
        ('the CLAIM items thirteen', tot['claim'] == 13),
        ('the refusals 21, each by its kind', len(rf) == 21 and '?' not in kinds),
        ('v1.34.6 ALL AS WANTED', bool(vm) and vm.group(1) == vm.group(2)),
        ('the carried faults banked, none repaired', bool(fm)),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the lock gate committed at %s' % C1_LOCKGATE, lg.startswith(C1_LOCKGATE)),
        ('v1.34.6 at %s moving VERSION' % C1_STANDING, st.startswith(C1_STANDING) and ver == 'v1.34.6')) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (the tally %s)' % (bad, tot))
    s.update(tally=tot, l_counter=l_cn, refusals=len(rf), kinds=kinds, v1346=(vm.group(1), vm.group(2)), faults=(fm.group(1), fm.group(2)))
    return s


def _c1_lines(s):
    t = s['tally']
    per = dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS)
    claims = [(k_, r) for k_, _n in C1_BANKS for r in s[k_] if r[2] == 'CLAIM']
    kinds = ', '.join('%s %d' % kv for kv in sorted(s['kinds'].items(), key=lambda kv: (-kv[1], kv[0])))
    pe, pp_, pd = per['events'], per['postseal'], per['defects']
    L = ['*b754’s events bank (relay data/b754_events.txt) carries %d rows, (1)-(79): CLAIM %d, CLOSE %d, REPEAT %d; its post-seal events bank (relay '
         'data/b754_events_postseal.txt) %d, (80)-(95): CLAIM %d, CLOSE %d, REPEAT %d; its defects bank (relay data/b754_defects.txt) %d lettered rows, '
         '(a)-(s’’): CLAIM %d, CLOSE %d, REPEAT %d. Together CLAIM %d, CLOSE %d, REPEAT %d of %d, as b754’s closing counter prints it (relay '
         'data/b754_closing.txt :%d). Its refusals bank %d lines (relay data/b754_hook_refusals.txt), by kind %s. Each item is tagged in its own bracket; '
         'the tags are the banks’ own and this entry edits none of them.*' % (
             pe['total'], pe['claim'], pe['close'], pe['repeat'], pp_['total'], pp_['claim'], pp_['close'], pp_['repeat'],
             pd['total'], pd['claim'], pd['close'], pd['repeat'], t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds), '']
    L += ['**The %d CLAIM items, in full:**' % len(claims), '']
    for k_, (i_, o_, tg_, col_, tx_) in claims:
        lab = '(%s)' % i_.replace("'", '’')
        L += ['**%s** %s (relay data/%s, %s %s; %s; %s; %s).' % (lab, _c1_q(tx_).replace("'", '’'), dict(C1_BANKS)[k_], 'letter' if k_ == 'defects' else 'row', lab,
                                                                 _c1_owner(o_), tg_, _c1_col(col_)), '']
    L += ['**The three repairs of `(R365)`(2):**', '',
          '**(i) The lock gate.** tools/b755_lockgate.py, carried from tools/b754_lockgate.py by the carry tool (relay data/b755_carry_lockgate.txt) and '
          'committed before it runs (relay %s), reads the handoff census’s STOPPED line as that gate’s pass; the page it counted is regenerated from the banks '
          'and the count has no reader. It runs at this act’s lock.' % C1_LOCKGATE, '',
          '**(ii) No post-seal events bank at this act.** The closing, the counter and the record each read that bank as optional (relay '
          'tools/standing/fold/closing.tpl :277-:280, tools/standing/counter.py :41-:43, tools/standing/fold/record.tpl :2314), so it is read as absent with '
          'no standing change; what the seat finds after the lock is printed with its times in the closing message and carried to the next corrigendum. The '
          'cause was the navigator’s: `(R364)`(3)(v) ordered a bank that no route could write.', '',
          '**(iii) The mirror’s folder by role.** tools/standing/ v1.34.6 (relay %s), one standing change with VERSION moved: the mirror bank, its json and '
          'the span line name the export by its file name and its folder by role, so the closing prints the file’s name with its bytes and hash and not the '
          'folder that holds it; inside the same change, by the author’s amendment row 1, the one-call tool’s act phases gain component 5 and component 6. '
          'Its controls %s of %s cases as wanted, each failing on v1.34.5 and passing on v1.34.6, or a guard of the new route alone (relay data/%s), landed '
          'before the gate.' % (C1_STANDING, s['v1346'][1], s['v1346'][0], C1_V1346), '',
          '**The carried faults:** the open items of b754’s closing message, %s rows from %s of its items, banked as relay data/%s, each with its place; '
          'none is repaired here.' % (s['faults'][0], s['faults'][1], C1_FAULTS), '',
          '*Filed at b755 on the author’s ruling `(R365)`(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b755.py) from b754’s events, post-seal events, defects and refusals banks read unedited, the v1.34.6 controls '
          'bank and the carried faults bank; banked as relay `data/b755_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row '
          '(%d). It answers b754’s record; no sealed tool, face, trail or root-named bank of b754 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    return (['b755 -- THE CORRIGENDUM FOR b754, SHORT, (R365)(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b754_events.txt rows (1)-(79), data/b754_events_postseal.txt rows (80)-(95), data/b754_defects.txt %d rows, '
             'data/b754_hook_refusals.txt %d lines; data/%s (the v1.34.6 controls); data/%s (the carried faults); the corrigenda bank`s last row (%d).' % (
                 len(s['defects']), s['refusals'], C1_V1346, C1_FAULTS, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, POST-SEAL %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEMS IN FULL %d ; THE REPAIRS 3: '
               'THE LOCK GATE AT %s, NO POST-SEAL EVENTS BANK, v1.34.6 AT %s (%s OF %s AS WANTED) ; THE CARRIED FAULTS %s ROWS ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['postseal']), len(s['defects']), t['claim'], t['close'], t['repeat'], t['claim'],
                   C1_LOCKGATE, C1_STANDING, s['v1346'][1], s['v1346'][0], s['faults'][0], ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b754 at its weight after its entry, and the short corrigendum for b754, landed through b698's guarded
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
        t = s['tally']
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=t['claim'], close=t['close'], repeat=t['repeat'], items=t['total'],
                                                   by_bank=dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS),
                                                   claims=[dict(bank=dict(C1_BANKS)[k_], id=r[0], owner=r[1], column=r[3]) for k_, _n in C1_BANKS for r in s[k_] if r[2] == 'CLAIM'],
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   repairs=dict(lockgate=C1_LOCKGATE, postseal='read as absent, no standing change', standing=C1_STANDING,
                                                                version='v1.34.6', bank='data/' + C1_V1346, cases=list(s['v1346'])),
                                                   faults=dict(bank='data/' + C1_FAULTS, rows=s['faults'][0], items=s['faults'][1]), row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEMS %d ; FINDINGS :%s' % (t['claim'], t['close'], t['total'], t['repeat'], t['claim'], ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
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
    """N1, b754 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b754: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): b754's override of the hook's blob (read at its v1.11.0 commit) retired -- v1.34.6 (relay
# ### eac02515) left tools/standing/hook.py unedited, so the template's line (its blob at the act's base 28255aea the working tree's) reads b755
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b754, naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base 28255aea the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b754-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b755_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
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
        and 'data/b755_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b755, Component 6 (the Edit tool): the corrigendum's json (data/b755_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 165, CLAIM 13, CLOSE 152, REPEAT 119, the CLAIM items 13, the corrigenda row (75); the rows stand in
# ### the bank by their banks (data/b755_corrigendum.txt); the template's row range read as the json's counts
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 165 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's override of checks 1476-1482 (one ERRATA entry at b753's (R363)(5)) removed -- (R364)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b754 as it stands
# ### G-BRANCHES-DELETED over b755's two repositories (relay, PLACE-papers) and five refs. b755, Component 6 (the Edit tool): b755's step
# ### zero names no kept branch in its own bank ("the kept branches and the tag read by the citation check's section 9", data/
# ### b755_stepzero.txt :60), where the template's needle ('port-b707', 'KEPT') and b754's (its kept row's wording) read the step-zero bank;
# ### read where b755 banks it, the citation check's row (data/b755_citation_check.txt :68, "port-b707 kept on SIDE-lv-conservation"), and
# ### its tip from the tree
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and '| ruling (9) | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
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
                                                                          or (bool(S['report_tool']) and 'tools/acts/b754.py -> tools/acts/b755.py' in (rd('b755_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b755_report.py' not in (S['sealj'].get('tools') or {})   # ### b755, Component 6: the carried stub set for the act, b754's body with the act's name
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b755_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:   # ### b755, Component 6: the carried stub set for the act, b754's body with the act's name
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b755')
    return '### THE COUNTER ((R365) Component 5, the act`s events and defects together; relay data/b755_defects.txt, data/b755_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act ((R365)(9)); W-ORD-MECHANISM-ATTRIBUTION open, its plan passed at b752`s [P1] (relay data/b752_attribution_plan.txt), its build T0 then T1 one of the two acts the root`s question offers as b756;',
    '        W-ORD-LI-ARITH, W-ORD-ZQ-FAMILY, W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)   # ### b755, Component 6: the carried stub set, b754's body; b755's listing `branch --merged main --list` (data/b755_stepzero.txt :55) meets it
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b755_author_answers.txt', 'b755_answer_check.txt', 'b755_events.txt'))   # noqa: E731,E702
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
REG = os.path.join(ROOT, 'data', 'b755_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b755_registration_%s.txt' % __import__('b755_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b754, Component 4 (the Edit tool, before the face): b753's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b754, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b754's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b755_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abefghijklmnop'))   # ### b755: the seat's rows of data/b755_defects.txt as the template's reader takes them (THE SEAT'S); (c) THE TOOL'S and (d) THE TOOLS' fall outside its three actors and are read by the counter, not by this floor; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b755_corrigendum.txt', 'data/b755_standing_v1346.txt', 'data/b755_carried_faults.txt', 'data/b755_walk.txt', 'data/b755_literature.txt',
                  'data/b755_cand_a.txt', 'data/b755_cand_h.txt', 'data/b755_cand_c.txt', 'data/b755_cand_j.txt', 'data/b755_cand_k.txt', 'data/b755_cand_l.txt',
                  'data/b755_candidates.txt', 'data/b755_registrations.txt', 'data/b755_ceiling.txt', 'data/b755_roots_59.txt', 'data/b755_list_59.txt',
                  'data/b755_list_59_controls.txt', 'data/b755_zeros_from_primes_59.txt', 'data/b755_recur_59.txt', 'data/b755_recur_control.txt',
                  'data/b755_census_from_primes.txt', 'data/b755_l16.json', 'data/b755_put_1.json', 'data/b755_put_2.json', 'data/b755_amendments.json',
                  'data/b755_author_answers.txt', 'data/b755_pathrefusal.txt', 'data/b755_reproduce.txt', 'data/b755_reproduce.json', 'data/b755_address_scan.txt', 'data/b755_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b755_address_scan.py'), 'scan'], capture_output=True, text=True,
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
    """(R365)(1)-(8) and the amendment rows: the act's relay commits after step zero in their order, (key, commit) -- v9, v1.34.6, the
    lock gate carried, the corrigendum banks, the walk's generator and its bank, the literature bank, the candidates' generators and banks
    in their order, the candidates bank with the prior clause, the ceiling after Component 3, each rule alone, the list of roots at -59, the
    engine, the list with the two verdicts, the census's generator and its bank, [L16]'s generator, its write bank and the handoff page where
    each is made; read from the worklist at the call."""
    c = [('v9', K.STANDING_COMMIT), ('standing', K.C1_STANDING), ('lockgate', K.C1_LOCKGATE), ('corr', K.C1_CORR), ('c2first', K.C2_PLAN_FIRST),
         ('walk', K.C2_RELAY), ('literature', K.C3_LITERATURE)]
    c += [('c3_%d' % i_, h_) for i_, h_ in enumerate(K.C3_RELAY[1:-2], 1)]   # ### the candidates' five commits between the literature and the candidates bank
    c += [('candidates', K.C3_CANDIDATES), ('ceiling', K.C1_CEILING), ('rule_zeros', K.C4_RULE_ZEROS), ('rule_recur', K.C4_RULE_RECUR),
          ('roots', K.C4_ROOTS), ('engine', K.C4_ENGINE), ('list', K.C4_LIST), ('census_gen', K.C5_GEN), ('census', K.C5_RELAY), ('l16_gen', K.L16_GEN)]
    c += [(k_, h_) for k_, h_ in (('l16', K.L16_BANK), ('handoff', K.HANDOFF_COMMIT)) if h_]
    return c


def _anc_pairs():
    """the ancestry pairs of _chain, each commit beside the next; the pair from v9 keeps the name the surgery arm reads."""
    c = _chain()
    return [('v9_v1310', c[0][1], c[1][1])] + [('%s_%s' % (a[0], b[0]), a[1], b[1]) for a, b in zip(c[1:], c[2:])]


def _gens_state():
    """(R365)(3)-(7), N2: each generator of K.GENS by its name -- the bank in the working tree and its blob at its commit; the generator's
    first add (the oldest commit adding it) against the first of its commits; the files of each of its commits and of the bank's; their
    times. A generator later given a mode of its own (tools/b755_zlist.py's verdict mode at 2b4a3942) is read at the commits before each bank."""
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
#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R365)(1)-(9) (b755's keys over b755's objects): the order by time and ancestry; v1.34.6's controls; the walk against the
        # ### registration at its blob; each generator before its bank; the literature, the candidates, the prior clause and the two rules; the
        # ### roots, the engine, the list and the verdicts; the census; [L16]; zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b753's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in _anc_pairs()),
        # ### b755 (R365)(1), (7): PLACE-papers by ancestry -- the weight and corrigendum on the act's base, [L16]'s line on them, HEAD on that
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('pre_c1', K.PRE_PP, K.C1_PP), ('c1_l16', K.C1_PP, K.L16_PP), ('l16_head', K.L16_PP, 'HEAD'))),
        pp_log=[l for l in gs(PP, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_PP).split() if l.strip()],
        v1346=rd('b755_standing_v1346.txt'), v1346_blob=_s(blob(ROOT, '%s:data/b755_standing_v1346.txt' % K.C1_STANDING)),
        r365_chain=_chain(),
        gens=_gens_state(),
        # ### the walk ((R365)(3)): the registration read at its blob, the bank and its controls json at their commit
        reg_walk=(_s(blob(ROOT, '%s:%s' % (K.REG_WALK[1], K.REG_WALK[0]))) or None, _s(blob(ROOT, 'HEAD:' + K.REG_WALK[0])) or None, rd(K.REG_WALK[0].split('/', 1)[1])),
        walk=rd('b755_walk.txt'), walk_blob=_s(blob(ROOT, '%s:data/b755_walk.txt' % K.C2_RELAY)), walk_ctl=jl('b755_coeffs_controls.json'),
        # ### the literature, the candidates and the prior clause ((R365)(4), (5)(i)); the ceiling after Component 3
        lit=rd('b755_literature.txt'), lit_blob=_s(blob(ROOT, '%s:data/b755_literature.txt' % K.C3_LITERATURE)),
        cands=rd('b755_candidates.txt'), cands_blob=_s(blob(ROOT, '%s:data/b755_candidates.txt' % K.C3_CANDIDATES)),
        ceiling=(rd('b755_ceiling.txt'), _s(blob(ROOT, '%s:data/b755_ceiling.txt' % K.C1_CEILING))),
        # ### the two rules ((R365)(5)(ii), (iii)): the registrations bank at each commit and at HEAD; the list of roots, the list, the verdicts
        regs=dict((k_, _s(blob(ROOT, '%s:data/b755_registrations.txt' % h_))) for k_, h_ in (('prior', K.C3_CANDIDATES), ('zeros', K.C4_RULE_ZEROS), ('recur', K.C4_RULE_RECUR), ('head', 'HEAD'))),
        regs_now=rd('b755_registrations.txt'),
        roots=rd('b755_roots_59.txt'), roots_blob=_s(blob(ROOT, '%s:data/b755_roots_59.txt' % K.C4_ROOTS)),
        list59=rd('b755_list_59.txt'), list59_ctl=rd('b755_list_59_controls.txt'),
        zfp=rd('b755_zeros_from_primes_59.txt'), recur=rd('b755_recur_59.txt'), recur_ctl=rd('b755_recur_control.txt'),
        census=rd('b755_census_from_primes.txt'), l16j=jl('b755_l16.json'),
        putj=jl('b755_put_2.json'), zanswers=rd('b755_author_answers.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP, K.L16_PP)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP, K.L16_PP)),
        numstat=dict((h_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for h_ in (K.C1_PP, K.L16_PP)),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_TIP, 'refs/heads/' + K.ZQ_BRANCH).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..refs/heads/%s' % (K.ZQ_TIP, K.ZQ_BRANCH)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        zq_tag=(gs(EF, 'rev-parse', 'refs/tags/' + K.ZQ_TAG[0]).strip(), gs(EF, 'rev-parse', K.ZQ_TAG[0] + '^{commit}').strip(),
                gs(EF, 'cat-file', '-p', 'refs/tags/' + K.ZQ_TAG[0])),
        ef_tags_entering=sorted(t for t in gs(EF, 'tag', '--points-at', K.ZQ_ENTERING).split(NL) if t.strip()),
        ef_since=[l for l in gs(EF, 'log', '--all', '--format=%H %ct').split(NL) if l.strip() and int(l.split()[1]) >= (_ct(ROOT, K.ACT_CURRENT_COMMIT) or 0)],   # ### any EF commit since the act opened (none: no Lean file written)
        box_src=_s(blob(EF, '%s:SIDEExplicitFormula/Schema/ZetaBox/Box.lean' % K.ZQ_TIP)),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b755_dispatch_rows.json') or '[]'), reproduce=rd('b755_reproduce.txt'), reproducej=jl('b755_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b755_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b755_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [('c1', _ct(ROOT, K.C1_RELAY)), ('c1pp', _ct(PP, K.C1_PP)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)),
                                                              ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT)), ('l16pp', _ct(PP, K.L16_PP))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), lockgate=files_of(ROOT, K.C1_LOCKGATE), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), ceiling=files_of(ROOT, K.C1_CEILING), literature=files_of(ROOT, K.C3_LITERATURE),
                   candidates=files_of(ROOT, K.C3_CANDIDATES), rule_zeros=files_of(ROOT, K.C4_RULE_ZEROS), rule_recur=files_of(ROOT, K.C4_RULE_RECUR),
                   roots=files_of(ROOT, K.C4_ROOTS), engine=files_of(ROOT, K.C4_ENGINE), list=files_of(ROOT, K.C4_LIST), census=files_of(ROOT, K.C5_RELAY),
                   handoff=files_of(ROOT, K.HANDOFF_COMMIT) if K.HANDOFF_COMMIT else [], l16pp=files_of(PP, K.L16_PP), c1pp_=files_of(PP, K.C1_PP),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b755's read-first bank's items by path, the ferry's read-first list in its order (data/b755_readfirst_rows.json); b755 step zero: the
# ### carried stub replaced, one needle for each item of the ferry's list (:44) and for the act's own reads beside it
READFIRST_NEEDLES = (
    'relay data/b754_closing.txt |',
    'relay data/b754_rules.txt |',
    'relay data/b754_author_answers.txt |',
    'relay data/b754_defects.txt |',
    'relay data/b754_events.txt, data/b754_events_postseal.txt |',
    'relay data/b753_registrations.txt |',
    'relay tools/b722_coeffs.py |',
    'relay tools/b720_predict.py |',
    'relay data/b711_coeffs.txt |',
    'relay data/b721_offset_tier.txt |',
    'relay tools/b754_lockgate.py |',
    'relay data/b725_interference.txt, data/b713_list.txt |',
)
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R365)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'WALK ((R365)(3))', 'CANDIDATES ((R365)(4))', 'REGISTRATIONS AT -59 ((R365)(5))', 'CENSUS ((R365)(6))', 'LINE OF (7)',
 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """b755: the citation check's bank: every cite checked, OK and misses summing (88 = 88 + 0, data/b755_citation_check.txt :141), no
    miss; the check CLEAN (:143, halts 0), as the step-zero bank enters it (data/b755_stepzero.txt :49-:50, after the act_current commit
    and the subject read; the first dry run's one miss the readfirst bank not yet written, :30); the bank written before the step-zero
    banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 88 \
        and '### ### **THE CHECK CLEAN** (halts 0: Lean paths and nouns 0, comparatives 0)' in c \
        and 'THE CITATION CHECK BANKED (' in (S['stepz'] or '') and 'CITES CHECKED 88 ; OK 88 ; MISSES 0;' in (S['stepz'] or '') \
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
                    MISSES=tfirst('b755_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b754's figures, read at FINDINGS :15250 as Component 1 landed them (b754's closing head quoted, PLACE-papers dc89f3e7)
    return landed(S, 0, ['b754 AT ITS WEIGHT', 'suite 111 of 116', 'f8a5f7f19bc6f2d2', '70 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b755's title by its objects, the ferry's Component 6 order (data/b755_ferry.txt :52) adjusted to what the act did (record 31's _title
# ### over the banks' feet: the walk 14 of 14, the candidates 6 and 7, the two verdicts at -59, the literature 9 and 10)
TITLE_NEEDLES = ('## The class-number-3 walk and two predictions at -59 under (R365): H-C3-LAW held at fourteen of its fourteen fields (b755_walk)',
                 'six candidates reproduced, seven plants failing as wanted (b755_candidates)',
                 'H-ZEROS-FROM-PRIMES held to height 200, 0 zeros of real part at least 0.85 against 0 roots, a vacuous pass (b755_zeros_from_primes_59)',
                 'H-RECURRENCE refuted, S = 10 against the largest draw 14 (b755_recur_59)',
                 'the literature bank 9 sources at content, 10 not read (b755_literature)', 'nothing built')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R365)(1)-(2): the generated corrigendum for b754's record landed (its line in the json, FINDINGS :15252, the title at that line
    through conv): b754's 79 events, 16 post-seal events and 70 defects by count from their banks, 165 items, CLAIM 13 and CLOSE 152,
    REPEAT 119, the thirteen CLAIM items in full; the three repairs of (2) -- the lock gate carried at 9a2e55b6, no post-seal events bank,
    tools/standing/ v1.34.6 by its controls bank ALL AS WANTED; the carried faults banked; the corrigenda bank appended at row (75) and
    nothing before it changed; in Component 1's commits (the figures read from data/b755_corrigendum.json and the bank's foot)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 75 and j.get('claim') == 13 == len(j.get('claims') or []) and j.get('close') == 152 and j.get('repeat') == 119 \
        and '### ### **ITEMS 165: EVENTS 79, POST-SEAL 16, DEFECTS 70 ; CLAIM 13, CLOSE 152 ; REPEAT 119 ; THE CLAIM ITEMS IN FULL 13 ; THE REPAIRS 3: ' in (S['corrt'] or '') \
        and 'THE LOCK GATE AT 9a2e55b6, NO POST-SEAL EVENTS BANK, v1.34.6 AT eac02515 (15 OF 15 AS WANTED) ; THE CARRIED FAULTS 24 ROWS ; THE ENTRY AT FINDINGS :15252.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and '### ### **v1.34.6: CONTROLS (phases), (mirror), (version) ; CASES 15 ; AS WANTED 15 ; ALL AS WANTED.**' in (S['v1346'] or '') \
        and (S['v1346'] or '') == (S['v1346_blob'] or '\x00') and 'data/b755_standing_v1346.txt' in S['files']['standing'] and 'tools/standing/VERSION' in S['files']['standing'] \
        and 'tools/b755_lockgate.py' in S['files']['lockgate'] and 'data/b755_carried_faults.txt' in S['files']['c1'] \
        and '  (75) ' in S['corrigenda'] and '  (76) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R365)(1) binds this act by the rules of data/b754_rules.txt, read where they stand: its seventeen
    rows at HEAD their blob at the act's base, no row written; this act writes no rules bank of its own (no data/b755_rules.txt); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here not written at all."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^  \((\d+)\) ', rd('b754_rules.txt') or '')] == list(range(1, 18)) and not os.path.exists(os.path.join(D, 'b755_rules.txt')) \
        and bool(_s(blob(ROOT, 'HEAD:data/b754_rules.txt'))) and _s(blob(ROOT, '%s:data/b754_rules.txt' % PRE['relay'])) == _s(blob(ROOT, 'HEAD:data/b754_rules.txt')) \
        and gs(ROOT, 'log', '--format=%H', '--', 'data/b755_rules.txt').split() == [] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b755's report lines (report sections 2-5): each key a phrase its line opens with
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.34.6', 'CERTIFIED -- THE LIST AT -59 BY THE CERTIFIED ENGINE', 'CERTIFIED -- THE CANDIDATES REPRODUCED',
               'REGISTERED -- H-C3-LAW AT ITS FOURTEEN FIELDS', 'REGISTERED -- THE PRIOR CLAUSE AND THE LITERATURE BANK',
               'REGISTERED -- H-ZEROS-FROM-PRIMES AT -59', 'REGISTERED -- H-RECURRENCE AT -59',
               'HELD -- (6), EXPLORATORY AND MARKED SO', 'HELD -- THE LINE OF (7), [L16]',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b755: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b754, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b755_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b754, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail), the ledgers changed; no rename; no paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b755's headings and banks, as its _finding_text (record 34) writes them; the last the INTEGRATION line's opening words (_integ_line)
ENTRY_NEEDLES = ('**The weight, the corrigendum and the standing change**', '**The walk**', '**The prior clause and the literature bank**',
                 '**The candidates**', '**The two rules and their test**', '**After both verdicts, exploratory and marked so**', '**The line of (7)**',
                 '**The price and the ceiling**', '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b755_corrigendum.txt', 'data/b755_standing_v1346.txt', 'data/b755_carried_faults.txt', 'data/b755_walk.txt', 'data/b755_literature.txt',
                 'data/b755_candidates.txt', 'data/b755_registrations.txt', 'data/b755_roots_59.txt', 'data/b755_list_59.txt', 'data/b755_zeros_from_primes_59.txt',
                 'data/b755_recur_59.txt', 'data/b755_recur_control.txt', 'data/b755_census_from_primes.txt', 'data/b755_l16.json',
                 'data/b755_reproduce.txt', 'data/b755_address_scan.txt', 'data/b755_touch.txt',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: the walk: ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R365)(1), (2), (7), (9), N5 (the name the frozen run list carries): PLACE-papers written by the weight line and the corrigendum, then
    (7)'s line, in that order, and by nothing else before the record -- the weight and corrigendum in a commit touching FINDINGS alone in one
    hunk, its first two added lines b754 at its weight ("*Appended 2026-11-14 by b755 to b754’s entry") and the corrigendum's heading ("##
    Corrigendum to b754’s record"), removing none, the first PLACE-papers commit of the act on its base; [L16]'s commit the second, touching
    OPEN_TRAILS alone in one hunk, four lines added and none removed, its first added line the dated head and its second the line, the l16
    bank's confirm naming it; the changed files within PP_WRITTEN; by ancestry the base, the weight, [L16] and HEAD; b753's registration
    at HEAD its blob at the commit the walk reads ((R365)(9): not written again), and the earlier acts' registrations at HEAD their blobs."""
    dd_ = S['disch_diff'] or {}
    lines_ = lambda h_, p_: [l for l in (dd_.get(h_) or '').split(NL) if l.startswith(p_) and not l.startswith(p_ * 3)]
    a0_, r0_ = [l for l in lines_(K.C1_PP, '+') if l[1:].strip()], lines_(K.C1_PP, '-')
    a1_, r1_ = [l for l in lines_(K.L16_PP, '+') if l[1:].strip()], lines_(K.L16_PP, '-')
    hunks_ = lambda h_: [l for l in (dd_.get(h_) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(a0_) >= 2 and len(hunks_(K.C1_PP)) == 1 and a0_[0].startswith('+*Appended 2026-11-14 by b755 to b754’s entry') \
        and a0_[1].startswith('+## Corrigendum to b754’s record') and r0_ == []
    l16_ = len(a1_) == 2 and len(hunks_(K.L16_PP)) == 1 and a1_[0].startswith('+**Dated head, 2026-11-14, b755, `(R365)`(7)') and a1_[1].startswith('+[L16] ') \
        and r1_ == [] and (S['numstat'] or {}).get(K.L16_PP) == ['4', '0', 'OPEN_TRAILS.md'] and (S['reg_pp'] or {}).get(K.L16_PP) == ['OPEN_TRAILS.md'] \
        and ('PLACE-papers %s ' % K.L16_PP[:8]) in ((S['l16j'] or {}).get('confirm') or '')
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:2]] == [K.C1_PP[:8], K.L16_PP[:8]]
    rw_ = S['reg_walk'] or (None, None, None)
    b753_ = bool(rw_[0]) and rw_[0] == rw_[1] == _s(rw_[2])
    return bool(one_) and (S['reg_pp'] or {}).get(K.C1_PP) == ['FINDINGS.md'] and l16_ and order_ and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) and b753_ \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b755_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R365)(3), (8), N2 (the name the frozen run list carries): the act's order by time -- the act_current commit, step zero's banks,
    then each commit of _chain after v9 in its order (v1.34.6, the lock gate, PLACE-papers' weight and corrigendum, the corrigendum banks, the
    walk's generator and its bank, the literature, the candidates' commits, the candidates bank with the prior clause, the ceiling, the two
    rules, the roots, the engine, the list, the census's generator and its bank, [L16]'s generator, PLACE-papers' line after it, and the
    l16 bank and the handoff page where made); by ancestry within the relay from v9 through each of them; v1.34.6's bank at HEAD its blob at
    its commit, with VERSION moved there and its foot ALL AS WANTED. The walk: the registration read at its blob (the walk's head naming
    it), the bank at HEAD its blob at its commit, its controls json written by the generator's commit before the bank and all as wanted,
    the bank's controls printed before its rows, its foot grading every one of the fourteen rows HELD, REFUTED or NOT SCORABLE."""
    t_ = S['t']
    ks_ = ['actcur', 'stepzero'] + [k_ for k_, _h in S['r365_chain'][1:3]] + ['c1pp'] + [k_ for k_, _h in S['r365_chain'][3:]]
    ks_.insert(ks_.index('l16_gen') + 1, 'l16pp')
    v_ = _txt(S['v1346'])
    vs_ = _vlast(v_).startswith('v1.34.6: CONTROLS ') and _vlast(v_).endswith('ALL AS WANTED.') and v_ == _txt(S['v1346_blob']) \
        and 'tools/standing/VERSION' in S['files']['standing'] and 'data/b755_standing_v1346.txt' in S['files']['standing']
    w_, wc_ = _txt(S['walk']), S['walk_ctl'] or {}
    rw_ = S['reg_walk'] or (None, None, None)
    wf_ = re.search(r'H-C3-LAW: (\d+) OF (\d+) HELD, REFUTED (\d+), NOT SCORABLE (\d+) ;', _vlast(w_))
    walk_ = bool(w_) and w_ == _txt(S['walk_blob']) and 'its bytes equal to its blob at %s' % K.REG_WALK[1] in w_ and bool(rw_[0]) and rw_[0] == rw_[1] \
        and wc_.get('ok') is True and wc_.get('tool_commit') == K.C2_PLAN_FIRST[:8] and (_iso_epoch(wc_.get('at') or '') or 0) < (t_.get('walk') or 0) \
        and 0 <= w_.find('THE CONTROLS FIRST (data/b755_coeffs_controls.json') < w_.find('### THE ROWS, EACH ON THE FALSIFIER') \
        and bool(wf_) and int(wf_.group(2)) == 14 and int(wf_.group(1)) + int(wf_.group(3)) + int(wf_.group(4)) == 14
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and len(S['anc']) == len(S['r365_chain']) - 1 and all(v is True for v in S['anc'].values()) and vs_ and walk_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R365)(4), (5)(i), (8), N2, N3 (the name the frozen run list carries): each generator of K.GENS first added by a commit of its own,
    every one of its commits carrying it and not its bank, the bank's commit carrying the bank and not the generator and after every
    generator commit, the bank at HEAD its blob there; the literature bank at HEAD its blob at its commit, its foot grading every source at
    content (T-rows) or not read (N-rows); the candidates bank at HEAD its blob at its commit, committed with the registrations bank's first
    form (the prior clause and no rule) after the literature; each reproduced candidate's block present with its (S1) line, the prior work
    the ruling names in the bank's words at content or NOT READ (the record's N3 reads the same words); the ceiling bank at HEAD its blob at
    its commit, after the candidates and before either rule, its foot the ceiling after Component 3."""
    t_ = S['t']
    gk_ = _gens_ok(S)
    lit_ = _txt(S['lit'])
    lf_ = re.search(r'SOURCES READ AT CONTENT (\d+) \(T1-T(\d+)\) ; NOT READ (\d+) ROWS \(N1-N(\d+)\)', _vlast(lit_))
    litok_ = bool(lit_) and lit_ == _txt(S['lit_blob']) and bool(lf_) and lf_.group(1) == lf_.group(2) and lf_.group(3) == lf_.group(4) \
        and 'data/b755_literature.txt' in S['files']['literature']
    c_, rp_ = _txt(S['cands']), _txt((S['regs'] or {}).get('prior'))
    cands_ = bool(c_) and c_ == _txt(S['cands_blob']) and 'data/b755_candidates.txt' in S['files']['candidates'] \
        and 'data/b755_registrations.txt' in S['files']['candidates'] and '## (1) THE PRIOR CLAUSE' in rp_ and '## (2) THE RULE' not in rp_ \
        and bool(t_.get('literature')) and t_['literature'] < (t_.get('candidates') or 0)
    src_ = all(('\n## %s ' % l_) in c_ for l_ in ('(a)', '(c)', '(h)', '(j)', '(k)', '(l)')) and c_.count('  (S1): ') >= 6 \
        and all(w_ in ' '.join(c_.split()) for w_ in PRIOR_WORDS)
    ce_ = S['ceiling'] or (None, None)
    ceil_ = bool(ce_[0]) and _txt(ce_[0]) == _txt(ce_[1]) and 'data/b755_ceiling.txt' in S['files']['ceiling'] \
        and (t_.get('candidates') or 0) < (t_.get('ceiling') or 0) < (t_.get('rule_zeros') or 0) \
        and _vlast(_txt(ce_[0])).startswith('THE CEILING AFTER COMPONENT 3: LOWER SUM ')
    return len(gk_) == len(K.GENS) >= 12 and all(o_ for _n, o_ in gk_) and litok_ and cands_ and src_ and ceil_


# ### the prior work (R365)(4) names, in the candidates bank's own words (the record's N3_PRIOR, the same bytes)
PRIOR_WORDS = ('Lee, arXiv 1204.6297, section 3.1 (T2.c', 'Bombieri and Ghosh 2011, section 9 (T1.j',
               'Bombieri and Ghosh 2011, Theorem 7, for the Davenport-Heilbronn family (T1.f',
               '"classical genus theory", as the ruling names it, with no source: NOT READ (N10)',
               'van de Lune and te Riele, Mathematisch Centrum NW 44/77 (1977), Lemma 5.1, almost-periods of the partial sums of zeta from '
               'rational approximations to ratios of logarithms of primes (T7.c')


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R365)(6) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b754 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b754's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
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
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.34.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1310') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b754's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R365)(5)(ii), (iii), (6), (7), (9), N2, N3 (the name the frozen run list carries): the two rules and their test, the census and
    (7)'s line -- the registrations bank at the two rules' commits: H-ZEROS-FROM-PRIMES added alone (its commit carrying the bank and
    nothing else beside the step row and the scan), H-RECURRENCE added with its null's generator and its seed (SEED = 59) and nothing else,
    its bank the first rule's text less that text's foot line, the new section and the foot after it (the first rule's lines unmoved; the
    foot alone rewritten, data/b755_defects.txt (p)), the bank at HEAD its blob at the second rule (nothing written after it); the list of roots at -59 committed after both rules and before
    the engine, at HEAD its blob there; the engine (tools/b755_list.py) committed after the roots and before the list, its controls run
    after the roots' commit by the controls bank's own time and AS WANTED; the list complete in every band, its head saying the roots came
    first, the list and both verdicts in one commit; each verdict bank reading its rule and nothing written after it, its foot a verdict the
    rule allows; the recurrence's control AS WANTED; the census after both verdicts, its generator first, its foot EXPLORATORY; the l16 bank's
    two items (the dated head and [L16]) and its confirm naming PLACE-papers' commit, after its generator; b746's draft unchanged; no Zenodo
    tool this act."""
    t_ = S['t']
    fs_ = dict((k_, sorted(set(v_) - set(RIDERS))) for k_, v_ in S['files'].items() if isinstance(v_, list))
    rg_ = S['regs'] or {}
    rz_, rr_, rh_ = _txt(rg_.get('zeros')), _txt(rg_.get('recur')), _txt(rg_.get('head'))
    rules_ = '## (2) THE RULE (H-ZEROS-FROM-PRIMES)' in rz_ and '## (3) THE RULE (H-RECURRENCE)' not in rz_ and '## (3) THE RULE (H-RECURRENCE)' in rr_ \
        and bool(rz_) and rr_.startswith(NL.join(rz_.rstrip(NL).split(NL)[:-1]) + NL) and rz_.rstrip(NL).split(NL)[-1].startswith('### ### **THE PRIOR CLAUSE: ') \
        and bool(rh_) and rh_ == rr_ == _txt(S['regs_now']) \
        and fs_.get('rule_zeros') == ['data/b755_registrations.txt'] and fs_.get('rule_recur') == ['data/b755_registrations.txt', 'tools/b755_recur.py'] \
        and 'SEED = 59' in _txt(blob(ROOT, '%s:tools/b755_recur.py' % K.C4_RULE_RECUR))
    ts_ = [t_.get(k_) for k_ in ('rule_zeros', 'rule_recur', 'roots', 'engine', 'list', 'census_gen', 'census')]
    order_ = all(ts_) and ts_ == sorted(ts_)
    roots_ = bool(S['roots']) and _txt(S['roots']) == _txt(S['roots_blob']) and 'tools/b755_list.py' in fs_.get('engine', []) \
        and 'data/b755_list_59.txt' not in fs_.get('engine', [])
    lc_ = _txt(S['list59_ctl'])
    lc0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) ; ', lc_.split(NL)[0] if lc_ else '')
    ctl_ = bool(lc0_) and (_iso_epoch(lc0_.group(1)) or 0) > (t_.get('roots') or 0) and _vlast(lc_).endswith('AS WANTED.')
    l_ = _txt(S['list59'])
    lf_ = re.search(r'THE LIST COMPLETE TO ([\d.]+), .* ; BANDS (\d+) \(COMPLETE (\d+)\) ;', _vlast(l_))
    list_ = bool(lf_) and lf_.group(2) == lf_.group(3) and 'The list of roots at -59 (data/b755_roots_59.txt) committed before any band ran.' in l_ \
        and {'data/b755_list_59.txt', 'data/b755_zeros_from_primes_59.txt', 'data/b755_recur_59.txt'} <= set(fs_.get('list', []))
    z_, r2_, rc_ = _txt(S['zfp']), _txt(S['recur']), _txt(S['recur_ctl'])
    verd_ = 'data/b755_registrations.txt (2) and nothing written after it' in z_ and bool(re.match(r'H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT \d+: (HELD|REFUTED) ;', _vlast(z_))) \
        and 'rule of data/b755_registrations.txt (3) and nothing written after it' in r2_ and bool(re.match(r'H-RECURRENCE AT -59: (HELD|REFUTED|NOT DECIDED): ', _vlast(r2_))) \
        and bool(re.match(r"H-RECURRENCE'S CONTROL: S = \d+, AS WANTED ;", _vlast(rc_)))
    census_ = _vlast(_txt(S['census'])).startswith('(6), EXPLORATORY: ') and 'data/b755_census_from_primes.txt' in fs_.get('census', [])
    lj_ = S['l16j'] or {}
    l16_ = [x_.get('item') for x_ in lj_.get('lines') or []] == ['head', '[L16]'] and ('PLACE-papers %s ' % K.L16_PP[:8]) in (lj_.get('confirm') or '') \
        and bool(t_.get('l16_gen')) and t_['l16_gen'] < (t_.get('l16pp') or 0)
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b755_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return rules_ and order_ and roots_ and ctl_ and list_ and verd_ and census_ and l16_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b755_steps.json', 'data/b755_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order, the tool's own list at the act's base 28255aea (I-109, entered at
    b753, stands in no row of it, and this act changes no research tool); each row REPRODUCES,
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
    """standing clauses v9 (Component 6 of (R365): the close "as the standing clauses order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b755_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b754's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R365-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b754's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R365) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b754's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 28255aea',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 88 = 88 OK + 0 misses, the check CLEAN (halts 0) as the step-zero bank enters it after the act_current commit and the subject read; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b754-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b755: the tip removed from "(was 28255aea, 19:01:51Z)" (data/b755_stepzero.txt :57-:59); the carried plant wanted the tip closed by its paren and mutated nothing (the probe's VAC)
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 6 order adjusted to what the act did: the class-number-3 walk under (R365), H-C3-LAW held at fourteen of its fourteen fields; six candidates reproduced, seven plants failing as wanted; H-ZEROS-FROM-PRIMES held to height 200, 0 zeros against 0 roots, a vacuous pass; H-RECURRENCE refuted, S = 10 against the largest draw 14; the literature bank 9 sources at content, 10 not read; nothing built; each finding`s name in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R365)(1), (2): the generated corrigendum for b754`s record, landed at FINDINGS :15252: b754`s 79 events, 16 post-seal events and 70 defects by count from their banks, 165 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 13 CLOSE 152, REPEAT 119, the thirteen CLAIM items in full; its three repairs -- the lock gate carried at 9a2e55b6, no post-seal events bank, v1.34.6 by data/b755_standing_v1346.txt; the carried faults 24 rows; the corrigenda bank appended at row (75)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R365)(1), data/b754_rules.txt`s seventeen rows at HEAD their blob at the act`s base, no row written; no rules bank of this act',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b755's objects
    ('G-REGISTRATIONS-FIRST', '(R365)(1), (2), (7), (9), N5: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (dc89f3e7), one hunk, none removed, the act`s first PLACE-papers commit; then (7)`s line in a commit touching OPEN_TRAILS alone (f948f606), one hunk, 4 lines appended, none removed, its confirm naming it; the changed files within FINDINGS and OPEN_TRAILS; data/b753_registrations.txt at HEAD its blob at 3f865479, not written again; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('REGISTRY.md'))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b755_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R365)(1)-(8), N2: the act`s order by time -- the act_current commit and step zero`s banks, v1.34.6, the lock gate, the weight and corrigendum, the walk`s generator then its bank, the literature, the candidates with the prior clause, the ceiling, the two rules, the roots, the engine, the list, the census`s generator then its bank, [L16]`s generator then its write, the handoff page -- and by ancestry within the relay; v1.34.6`s bank ALL AS WANTED in its own commit with VERSION moved; the walk read against data/b753_registrations.txt at 3f865479, its generator 3bdb6561 first, its controls before its rows, its fourteen rows graded',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(rule_table=False))),
    ('G-DERIVATION-GRADED', '(R365)(3)-(5)(i), (8), N2, N3: each generator of the worklist`s list first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; the literature bank at HEAD its blob, 9 sources at content (T1-T9) and 10 not read (N1-N10); the candidates bank at HEAD its blob at aa102044 with the prior clause and no rule, after the literature, its six blocks each with its (S1) line and the prior work the ruling names, at content or NOT READ; the ceiling after Component 3 between the candidates and the first rule',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'ceiling', ((S['ceiling'] or (None, None))[0], 'planted'))),
    ('G-OFFSET-POST-HOC', 'N5, (R365)(9): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R365)(5)(ii), (iii), (6), (7), (9), N2, N3: H-ZEROS-FROM-PRIMES committed alone (11fc3c93) and H-RECURRENCE with its null`s generator and seed 59 and nothing else (a937fbb7), the registrations bank at HEAD its blob there; the roots at -59 after both rules (e21b5c8c) and before the engine (2b4a3942), at HEAD their blob; the engine`s controls after the roots` commit, AS WANTED; the list complete in every band, committed with both verdicts (b03fc15e); each verdict reading its rule and nothing written after it; the recurrence`s control AS WANTED; the census after both verdicts, its generator first, EXPLORATORY; [L16]`s two items and its confirm naming PLACE-papers f948f606, after its generator; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'l16j', lambda d: d.update(lines=(d.get('lines') or [])[:1]))),
    ('G-DIFFERS-ERRATA', '(R365)(9): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line and the corrigendum in dc89f3e7, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b755_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R365-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b754 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b754 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS and OPEN_TRAILS: the weight line, the corrigendum, the entry, the trail and (7)`s line, (R365)(1), (2), (7), (9)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b754`s trail record on OPEN_TRAILS (:18296) and its root in the chain', lambda S: '### b754 — lane two, act one hundred and eighty-one, the sitting under (R364)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b755 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b754's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b755: (R365)'s rows, written at step zero in place of b754's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch cites755.py, cites755b.py, cites755c.py); (1)'s line read from
    # ### the public relay at 28255aea. A place is named by its role or its file name, never by a folder of the host (N5); no line under [Q]'s
    # ### row (3) is cited by these rows (the ledger lines they read: FINDINGS :15053, :15055, :15208; OPEN_TRAILS :18292, :18296, :18310, :18344).
    import hashlib as _h
    pub = _blob('D:/relay', '28255aea', 'data/b754_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1), SCOPE', 'data/b754_closing.txt :1, the head line as the public relay carries it at 28255aea', bool(pub) and pub[0] == at(cl, 1) and 'relay 18d335fa' in pub[0] and 'PLACE-papers 0545f36' in pub[0],
        'remote main %s' % rm[:8], '1')
    add('ruling (1), SCOPE', 'relay remote main read back at 28255aea after b754`s closing and step-row commits', rm.startswith('28255aea'), rm[:8], '1')
    for w_ in ('suite 111 of 116', 'root f8a5f7f19bc6f2d2', '25 prompts answered', 'scores 8 of 8 HELD', '70 defects'):
        add('ruling (1)', 'data/b754_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, 28255aea and 0545f368', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('28255aea') and gr(PP, 'rev-parse', K.PRE_PP).startswith('0545f368'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    ru_ = lines_of(p('data', 'b754_rules.txt'))
    hd_ = (10, 16, 21, 26, 30, 43, 47, 51, 59, 71, 86, 96)
    add('ruling (1), N5, ferry (read first)', 'data/b754_rules.txt rows (1)-(12) at :%s; the sourcing rows (1)-(5), the quoting rows (6)-(9), [U3] row (12) binding' % ', :'.join(str(n_) for n_ in hd_),
        all(re.match(r'^\s*\(%d\)' % (k_ + 1), at(ru_, n_)) for k_, n_ in enumerate(hd_)), '%d lines ; heads %d of 12' % (len(ru_), sum(1 for k_, n_ in enumerate(hd_) if re.match(r'^\s*\(%d\)' % (k_ + 1), at(ru_, n_)))), '1')
    aa_ = lines_of(p('data', 'b754_author_answers.txt'))
    add('ruling (1), ferry (read first)', 'data/b754_author_answers.txt :121, [U1] and [U2] not in force at this act: their tool changes land after the walk',
        at(aa_, 121).startswith('On [U1] and [U2] as passed: their rows are written now') and 'not at the opening of b755' in at(aa_, 121), at(aa_, 121)[:60], '1')
    add('ferry (read first)', 'data/b754_author_answers.txt :201, the root`s answer: the walk as b755', at(aa_, 201).startswith('RESULT (transcript line 11d67961:45672') and 'Confirmed: walk as b755' in at(aa_, 201), at(aa_, 201)[:40], '1')
    # ### (R365)(2): the corrigendum's three repairs and the carried faults' source
    lg_ = lines_of(p('tools', 'b754_lockgate.py'))
    add('ruling (2)(i), ferry (read first)', 'tools/b754_lockgate.py :2, the lock gate with the handoff census read as STOPPED (147 lines), to be carried as tools/b755_lockgate.py',
        'THE LOCK GATE WITH THE HANDOFF CENSUS READ AS STOPPED' in at(lg_, 2), '%d lines' % len(lg_), '1')
    f4_ = lines_of(p('data', 'b754_ferry.txt'))
    add('ruling (2)(ii)', 'data/b754_ferry.txt :13, (R364)(3)(v): the post-seal events bank the navigator ordered', at(f4_, 13).startswith('(3) THE CORRIGENDUM') and '(v) THE POST-SEAL EVENTS BANK' in at(f4_, 13), at(f4_, 13)[:30], '1')
    add('ruling (2)(ii), (8)', 'no post-seal events bank at this act: data/b755_events_postseal.txt absent', not os.path.exists(p('data', 'b755_events_postseal.txt')), 'absent' if not os.path.exists(p('data', 'b755_events_postseal.txt')) else 'PRESENT', '6')
    import itertools as _it
    try:
        with open(C.SESSION, encoding='utf-8', errors='replace') as fh_:
            cm_ = json.loads(next(_it.islice(fh_, 52067, 52068)))
    except Exception:
        cm_ = {}
    ct_ = ''.join(c_.get('text', '') for c_ in ((cm_.get('message') or {}).get('content') or []) if isinstance(c_, dict) and c_.get('type') == 'text')
    add('ruling (2)', 'the seat`s closing message for b754, transcript line 52068 of the act`s session (2026-11-14T18:00:57Z), the carried faults` source: its open items',
        cm_.get('type') == 'assistant' and str(cm_.get('timestamp', '')).startswith('2026-11-14T18:00:57') and 'Open items, not acted on' in ct_, '%d characters' % len(ct_), '1')
    # ### (R365)(3): the registration read at its blob, the generator's two lines, the controls' figures
    rg3_ = lines_of(p('data', 'b753_registrations.txt'))
    add('ruling (3), ferry (read first)', 'data/b753_registrations.txt :14-:16, the rule (class number 3, n0 = min(p1^4·p2, p1^2·p2·p3), b(n0) = −2)',
        at(rg3_, 14).startswith('Let D be a negative fundamental discriminant of class number 3') and 'n0 = min(p1^4·p2, p1^2·p2·p3), and b(n0) = −2' in at(rg3_, 15), at(rg3_, 14)[:50], '2')
    add('ruling (3), ferry (read first)', 'data/b753_registrations.txt :29-:46, the table: sixteen rows :30-:45 with the minus sign U+2212, two controls and fourteen tests',
        at(rg3_, 29).split() == ['D', 'p1,', 'p2,', 'p3', 'n0', 'pattern', 'b(n0)'] and all(at(rg3_, n_).startswith('  \u2212') for n_ in range(30, 46))
        and 'sixteen rows, two controls and fourteen tests' in at(rg3_, 46), 'rows %d' % sum(1 for n_ in range(30, 46) if at(rg3_, n_).startswith('  \u2212')), '2')
    for n_, ws_ in ((30, ('\u221223', '2, 3, 13', '48', 'CONTROL')), (32, ('\u221259', '3, 5, 7', '315', '(2,1,1)')), (43, ('\u2212643', '32683')), (44, ('\u2212883', '83317')), (45, ('\u2212907', '73853'))):
        add('ruling (3), (5)(iii)', 'data/b753_registrations.txt :%d, the row at %s' % (n_, ws_[0].replace('\u2212', '-')), all(w_ in at(rg3_, n_) for w_ in ws_), ' '.join(at(rg3_, n_).split()[:5]), '2')
    add('ruling (3), ferry (read first)', 'data/b753_registrations.txt :54, the falsifier', at(rg3_, 54) == 'FALSIFIER: any of the fourteen where either differs from its row.', at(rg3_, 54)[:40], '2')
    add('ruling (3), (5)(i), ferry (read first)', 'data/b753_registrations.txt :57-:59, the list: OEIS A006203; Arno, Robinson and Wheeler 1998 as the source of completeness',
        'OEIS A006203' in at(rg3_, 57) and 'Arno' in at(rg3_, 58) and 'Robinson and Wheeler, Acta Arithmetica 83 (1998)' in at(rg3_, 59), at(rg3_, 57)[:40], '3')
    add('ruling (4), (5)(ii), ferry (read first)', 'data/b753_registrations.txt :66 the candidates (a)-(d), :84-:86 the candidate for registration at the walk`s act',
        at(rg3_, 66).startswith('(a)-(d) as (R363)(4) words them') and at(rg3_, 84).startswith("A CANDIDATE FOR REGISTRATION AT THE WALK'S ACT") and 'within 0.01' in at(rg3_, 86), at(rg3_, 84)[:40], '3')
    bl_ = [gr('D:/relay', 'rev-parse', 'HEAD:data/b753_registrations.txt'), gr('D:/relay', 'rev-parse', '28255aea:data/b753_registrations.txt'), gr('D:/relay', 'hash-object', 'data/b753_registrations.txt')]
    add('ruling (9)', 'data/b753_registrations.txt not written again: its blob at HEAD, at 28255aea and in the working tree one blob', len(set(bl_)) == 1 and bool(bl_[0]), bl_[0][:12], '6')
    cf_ = lines_of(p('tools', 'b722_coeffs.py'))
    add('ruling (3), ferry (read first)', 'tools/b722_coeffs.py :46 the bound 32532, :345 the exit at a field of other than two reduced forms', at(cf_, 46) == 'CUT = 32532' and 'REDUCED FORMS, NOT 2 -- NOTHING BANKED' in at(cf_, 345),
        at(cf_, 46), '2')
    add('ruling (3), ferry (read first)', 'tools/b720_predict.py :34, the group-ring model`s bound 32532', at(lines_of(p('tools', 'b720_predict.py')), 34) == 'CUT = 32532', 'read', '2')
    c11_ = lines_of(p('data', 'b711_coeffs.txt'))
    add('ruling (3), ferry (read first)', 'data/b711_coeffs.txt :12, -23`s control: the least negative n = 48, c(48) = (-8) log 2 + (-2) log 3',
        'THE LEAST n WITH c(n) < 0: n = 48 ; c(48) = (-8) log 2 + (-2) log 3' in at(c11_, 12), at(c11_, 12)[:50], '2')
    add('ruling (3)', 'data/b711_coeffs.txt :14, -23`s count of negative coefficients through 32532: 1066', 'THE COUNT OF NEGATIVE COEFFICIENTS through 32532: 1066' in at(c11_, 14), at(c11_, 14)[:50], '2')
    for f_, c_ in (('data/b722_walk.txt', '2'), ('tools/b718_abstract.py', '2'), ('data/b751_literature.txt', '3'), ('tools/b717_list.py', '4')):
        add('ruling (3)-(5)', '%s tracked at 28255aea, the form the act`s bank or tool takes' % f_, bool(_blob('D:/relay', '28255aea', f_)), '%d lines' % len(_blob('D:/relay', '28255aea', f_).split(NL)), c_)
    # ### (R365)(4): the two banked lists; (5)(ii) and (8): the engine's banked timings
    it_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (4)(h), (4)(l), ferry (read first)', 'data/b725_interference.txt :106, the 69 heights at -23 (107 lines)', 'ZEROS 69 ; READ 69' in at(it_, 106), at(it_, 106)[:40], '3')
    add('ruling (4)(h), ferry (read first)', 'data/b713_list.txt, the banked list at -15, tracked at 28255aea', bool(_blob('D:/relay', '28255aea', 'data/b713_list.txt')), '%d lines' % len(_blob('D:/relay', '28255aea', 'data/b713_list.txt').split(NL)), '3')
    ot_ = lines_of(p('data', 'b721_offset_tier.txt'))
    add('ruling (5)(ii), (8), ferry (read first)', 'data/b721_offset_tier.txt :66-:68, the certified engine`s banked totals: -15 2745 s, -39 3131 s, Q0 4507 s',
        'total 2745 s' in at(ot_, 66) and 'total 3131 s' in at(ot_, 67) and 'total 4507 s' in at(ot_, 68), at(ot_, 67)[:50], '0')
    # ### (R365)(4)(k), (7): OPEN_TRAILS's [L14] and the file's end
    add('ruling (4)(k)', 'OPEN_TRAILS :18292, [L14], the diagonal field among the walk`s fields', at(ot, 18292).startswith("[L14] THE DIAGONAL FIELD AMONG THE WALK'S FIELDS"), at(ot, 18292)[:40], '3')
    add('ruling (7)', 'OPEN_TRAILS :18344, the file`s last line before (7)`s: b754`s Next line, the walk as b755', at(ot, 18344).startswith('**Next:** the class-number-3 walk (b755)') and len(ot) == 18345 and at(ot, 18345) == '',
        '%d lines' % (len(ot) - 1), '6')
    # ### (R365)(8): the hook's table and the handoff page's tool
    hk_ = lines_of(p('tools', 'standing', 'hook.py'))
    nk_ = sum(1 for l_ in hk_[60:88] if re.match(r"^    '[A-Z]+': ", l_))
    add('ruling (8)', 'tools/standing/hook.py :61-:89, the table of kinds (21, the seat`s file`s count)', at(hk_, 61) == 'ROWS = {' and at(hk_, 89) == '}' and nk_ == 21, '%d kinds' % nk_, '0')
    add('ruling (8)', 'tools/standing/handoff.py, the handoff page`s tool, run once before the gate', os.path.exists(p('tools', 'standing', 'handoff.py')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 2⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 3⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b755 step zero: (R365)(2)'s counts over b754's banks, written in place of b754's rows over b753's; each tag read as the bank tags it,
    # ### an owner of more than one word read whole (THE ANSWERS ROUTE'S, defect (n')), the post-seal rows (80)-(95) beside the events (1)-(79)
    ps_ = lines_of(p('data', 'b754_events_postseal.txt'))
    eps_ = [int(m_.group(1)) for m_ in (re.match(r'^    \((\d+)\) ', l_) for l_ in ps_) if m_]
    add('ruling (2), ferry (read first)', 'b754`s events (1)-(79), its post-seal events (80)-(95) and its 70 lettered defects (a)-(s``) (data/b754_events.txt, data/b754_events_postseal.txt, data/b754_defects.txt)',
        starts == list(range(1, 80)) and eps_ == list(range(80, 96)) and len(letters) == 70, 'events %s ; post-seal %s-%s ; letters %d' % (starts[-1:], eps_[:1], eps_[-1:], len(letters)), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_, ncl_, ncs_ in (('data/b754_events.txt', ev, 79, 0, 79), ('data/b754_events_postseal.txt', ps_, 16, 2, 14), ('data/b754_defects.txt', dl, 70, 11, 59)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_.group(2) for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        add('ruling (2), ferry (read first)', '%s: %d rows, each tagged CLAIM or CLOSE and NEW or REPEAT as its bank tags it; CLAIM %d, CLOSE %d' % (f_, nr_, ncl_, ncs_),
            len(rr_) == nr_ and len(tg_) == nr_ and tg_.count('CLAIM') == ncl_ and tg_.count('CLOSE') == ncs_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d' % (len(rr_), len(tg_), tg_.count('CLAIM'), tg_.count('CLOSE')), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1), (2)', 'FINDINGS :%d, b754`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## The sitting under (R364)'), at(fi, K.B711_ENTRY)[:50], '1')
    add('ruling (1)', 'FINDINGS :%d and :%d, b753`s weight line and corrigendum (b754`s), the form b755`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM),
        at(fi, K.B711_WEIGHT).startswith('*Appended 2026-11-13 by b754 to b753’s entry') and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b753’s record'), at(fi, K.B711_WEIGHT)[:40], '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b754`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b754 — lane two, act one hundred and eighty-one, the sitting under (R364)'), at(ot, K.B711_TRAIL)[:50], '1')
    add('ruling (1)', 'OPEN_TRAILS :%d, b754`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '1')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula and SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.34.5 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.34.5',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry, (8)', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### (R365) SCOPE, (2)(iii): b754's export by its file name, bytes and hash, the folder that holds it not printed
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    add('ruling SCOPE, (2)(iii)', 'b754`s mirror %s, its sha256 opening 7579d52d as the navigator read it' % os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest().startswith('7579d52d'),
        '%d bytes ; sha256 %s' % (len(mz_), _h.sha256(mz_).hexdigest()[:16]), '6')
    # ### PATHS: the clones at the paths the worklist holds, counted; one absent printed by its name alone
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R365)(8): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (8)', 'the push-b754-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R365)(8): act_current alone, then b754's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b754_relay_push-b754-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['tools/mirror_prevbuild.json'])):
        if not c_:
            add('ruling (8)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (8)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (9)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (9)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (8)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (8), ferry (read first)', 'data/b755_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b755_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b755_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with v1.34.6's controls and the carried faults, the walk, the candidates with the literature bank and the
ceiling, the registrations at -59 with the roots, the certified list and the two verdicts, the census, the line of (7), the name and address
scan, the reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R365)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R365)(8)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R365)(9): no kernel touched, no branch of any kernel merged, created,
moved or deleted, no tag, no Lean file, no description or README edited).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b755 ((R365)(8) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R364)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b755 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTY-TWO, THE CLASS-NUMBER-3 WALK: b754 AT ITS WEIGHT; A SHORT CORRIGENDUM; '
              'H-C3-LAW AT ITS FOURTEEN FIELDS; THE CANDIDATES REPRODUCED WITH THEIR PLANTS AND THEIR PRIOR WORK; H-ZEROS-FROM-PRIMES AND H-RECURRENCE REGISTERED AT -59 '
              'AND TESTED BY THE CERTIFIED ENGINE; ONE LINE FOR OPEN_TRAILS; NOTHING BUILT, UNDER (R365).**')   # ### b755 step zero: the ferry`s ACT line (data/b755_ferry.txt :40) as it stands; adjusted at Component 6 to what the act did
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b754's sections over b754's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.34.6: the mirror`s folder by role ((R365)(2)(iii)) and the act phases component 5 and component 6 (the amendment row 1), each case through the route before and the route after', 'b755_standing_v1346.txt'),
                ('the open items of b754`s closing message banked as its carried faults, each with its place, none repaired here', 'b755_carried_faults.txt'),
                ('the probe-path refusal printed before the lock gate', 'b755_pathrefusal.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE WALK ((R365)(3))', [
                ('the controls before any row, then the fourteen rows against data/b753_registrations.txt at its blob, the second route and the model beside them', 'b755_walk.txt')]),
            ('THE CANDIDATES ((R365)(4))', [
                ('the literature bank of (5)(i), each source read at content with its locator or printed NOT READ', 'b755_literature.txt'),
                ('the candidates reproduced from their statements alone, each with its planted error and the prior work the ruling names', 'b755_candidates.txt'),
                ('the ceiling read again after Component 3', 'b755_ceiling.txt')]),
            ('THE REGISTRATIONS AT -59 ((R365)(5))', [
                ('the prior clause, then each rule committed alone', 'b755_registrations.txt'),
                ('the list of roots at -59 from the primes, committed before any value of the function was read there', 'b755_roots_59.txt'),
                ('the certified engine`s controls, run after the roots` commit', 'b755_list_59_controls.txt'),
                ('the certified list at -59, band by band in the foreground', 'b755_list_59.txt'),
                ('H-ZEROS-FROM-PRIMES read against its rule (the falsifier`s population empty on both sides: a vacuous pass, relay data/b755_events.txt (16))', 'b755_zeros_from_primes_59.txt'),
                ('H-RECURRENCE read against its rule', 'b755_recur_59.txt'),
                ('H-RECURRENCE`s control at -23, (4)(l) by the same tool', 'b755_recur_control.txt')]),
            ('THE CENSUS ((R365)(6))', [
                ('exploratory and marked so: -23`s roots to height 5,000 and the least height of a root above Re s = 1 at three bounds, its control printed after its figures (relay data/b755_defects.txt (l))', 'b755_census_from_primes.txt')]),
            ('THE LINE OF (7)', [
                ('[L16] appended at OPEN_TRAILS` end under a dated head by one PLACE-papers commit, its write and confirm', 'b755_l16.json', r'"confirm": "[^"]*"')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b755_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument entered, a planted wrong figure per run row', 'b755_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R364)(2)(vi): composed, not carried
    '    no kernel touched ((R365)(9)): no branch of any kernel merged, created, moved or deleted ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    no kernel`s description or README written ; [B1] and [B3], the two kernel README items, in the clearing act the root`s question offers ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b754 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b754-* branches of relay and PLACE-papers deleted at step zero by name, after the --merged listing, one per command and each its own message ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ v1.34.6 landed before the gate ; each generator committed before its run and its controls before its figures, the census`s control printed after its figures (relay data/b755_defects.txt (l)) ; the prior clause and the literature bank before either rule of (5) ; each rule committed alone ; the list of roots at -59 committed before any tool read a value of the function there, the engine`s own controls among those tools ; the null of (5)(iii) committed with its seed before the certified list ; the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: no bank calling a result new ; each candidate`s sourcing line naming the prior work the ruling names, at content or NOT READ ; no figure of the navigator`s workspace printed as a banked figure ; the verdicts of (3) and (5) read against the registered rows and rules and against nothing written after them ; the entry`s INTEGRATION line composed from the banks` feet ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; nothing computed at a field of class number 3 beyond what (3) and (5) order ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b755_address_scan.txt, data/b755_address_scan_postlock.txt, data/b755_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written ; no README written ; no anchor edited ; no order entered ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS ((7)`s line under its dated head, and the trail) ; no paper`s body written ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b755`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; data/b753_registrations.txt not written again ;',
    '    tools/standing/ v1.34.6 by a version commit of its own with its controls in its bank (relay data/b755_standing_v1346.txt) ; HANDOFF.md written once by tools/standing/handoff.py before the gate ; act_current`s shared_edits as standing/carry.py shared reads them ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R365)(8) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one, its answer in relay data/b755_author_answers.txt ; the clearing act as b756 -- the twelve work-orders the triage of b724 read as ready, the tool changes of [U1] and [U2] (relay data/b754_author_answers.txt :121), the README route with [B1] and [B3], [H1]`s held part, the carried faults of (2) (relay data/b755_carried_faults.txt) and closing lines for checkpoints CP-6 and CP-7 ;',
    '        or the build of T0 then T1 as b756 (relay data/b752_attribution_plan.txt) with the clearing act after it ((R365)(8)) ;',
    '        defects (b), (e) and the tools` (d) open for the author, and the older corrigenda row naming the data volume`s folder (relay data/b755_defects.txt, data/b755_events.txt (11)) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b755_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b754 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b755: the one standing change is v1.34.6 ((R365)(2)(iii) with the amendment row 1, relay data/b755_standing_v1346.txt, read in
    # ### the corrigendum section); the carry's diffs here (b755 carried at step zero before the fold; its tools since are the templates and
    # ### tools/acts/b755.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b754 left them; port-b707 at b712`s tip %s)' % (
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
    b755's form over b755's objects: the corrigendum's foot; v1.34.6's controls from its bank; the carried faults' foot; the walk's foot;
    the literature bank's; the candidates bank's; the ceiling after Component 3; the list of roots at -59, the certified list and its
    controls; the two verdicts and the recurrence's control; the census; [L16]'s write bank; the citation check; the reproduction run; the
    address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter from the act's
    defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    vs_ = [('v1.34.6',) + _bfig('%s_standing_v1346.txt' % ACT, r'\*\*v1\.34\.6: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.34.6`s controls')]
    cf_ = _bfig('%s_carried_faults.txt' % ACT, r'\*\*THE CARRIED FAULTS : (\d+) ROWS FROM (\d+) ITEMS', 'the carried faults` foot')
    wk_ = _bfig('%s_walk.txt' % ACT, r'\*\*H-C3-LAW: (\d+) OF (\d+) HELD, REFUTED (\d+), NOT SCORABLE (\d+) ; THE CONTROL ROWS -23 (HELD|REFUTED), -31 (HELD|REFUTED) ; '
                r'THE THREE PRIMES AS THE ROW`S AT (\d+) OF (\d+) ; THE SECOND ROUTE: A CUBIC AT (\d+) OF (\d+), MISMATCHES (\d+) ; THE MODEL \(FORCED\) AGREEING AT (\d+) OF (\d+) ; '
                r'THROUGH (\d+) ; (\d+) s\.\*\*', 'the walk`s foot')
    lt_ = _bfig('%s_literature.txt' % ACT, r'\*\*THE LITERATURE: QUERIES (\d+) .*? ; SOURCES READ AT CONTENT (\d+) \(([^)]*)\) ; NOT READ (\d+) ROWS \(([^)]*)\)', 'the literature bank`s foot')
    cd_ = _bfig('%s_candidates.txt' % ACT, r'\*\*THE CANDIDATES: REPRODUCED (\d+) \(((?:\([a-z]\)(?:, )?)+)\), [^;]*; PLANTS (\d+), EACH FAILING AS WANTED', 'the candidates bank`s foot')
    ce_ = _bfig('%s_ceiling.txt' % ACT, r'\*\*THE CEILING AFTER COMPONENT 3: LOWER SUM ([\d.]+) h <= (\d+) h: (NOTHING CARRIED)\.\*\*', 'the ceiling after Component 3')
    rt_ = _bfig('%s_roots_59.txt' % ACT, r'\*\*THE LIST AT -59 TO ([\d.]+): ROOTS WITH Re >= 0\.85 (\d+), WITH Re IN \[0\.83, 0\.85\) (\d+)\.\*\*', 'the roots` foot')
    nr_ = _bfig('%s_zeros_from_primes_59.txt' % ACT, r'the list of roots data/%s_roots_59\.json \(relay [0-9a-f]+\): roots (\d+)' % ACT, 'the roots read by the verdict')
    ls_ = _bfig('%s_list_59.txt' % ACT, r'\*\*THE LIST COMPLETE TO ([\d.]+), [^;]* ; BANDS (\d+) \(COMPLETE (\d+)\) ; ON-LINE ZEROS (\d+) ; OFF-LINE PAIRS (\d+)\.\*\*', 'the list`s foot')
    lc_ = _bfig('%s_list_59_controls.txt' % ACT, r'\*\*(\(C-a\) .*?) ; (AS WANTED)\.\*\*', 'the list controls` foot')
    mx_ = _bfig('%s_zeros_from_primes_59.txt' % ACT, r'the largest real part among them ([\d.]+)', 'the largest real part read by the verdict')
    zf_ = _bfig('%s_zeros_from_primes_59.txt' % ACT, r'\*\*H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT (\d+): (HELD|REFUTED) ; ZEROS WITH Re >= 0\.85 (\d+) AGAINST ROOTS (\d+) ;', 'the zeros` verdict')
    rc_ = _bfig('%s_recur_59.txt' % ACT, r'\*\*H-RECURRENCE AT -59: (HELD|REFUTED|NOT DECIDED): S = (\d+) AGAINST THE LARGEST DRAW (\d+) ;', 'the recurrence`s verdict')
    rp_ = _bfig('%s_recur_59.txt' % ACT, r'S = (\d+) of (\d+) pairs with log 3 and log 5 ; the null, (\d+) draws of (\d+) heights uniform on \[2, (\d+)\], seed (\d+): mean ([\d.]+), largest (\d+)',
                'the recurrence`s pairs and null')
    rcc_ = _bfig('%s_recur_control.txt' % ACT, r"\*\*H-RECURRENCE['`]S CONTROL: S = (\d+), (AS WANTED) ; THE NULL['`]S LARGEST (\d+) ;", 'the recurrence control`s foot')
    cs_ = _bfig('%s_census_from_primes.txt' % ACT, r"\*\*\(6\), EXPLORATORY: AT -23 TO HEIGHT ([\d,]+) THE ROUTE['`]S ROOTS WITH Re >= 0\.85 AT P = 3 x 10\^5: (\d+) ; "
                r'THE LEAST HEIGHT OF A ROOT WITH Re > 1: (.*?) ; THE CONTROL TO (\d+) (ONE TO ONE)\.\*\*', 'the census` foot')
    l16_ = jl('%s_l16.json' % ACT)
    if not (l16_.get('lines') and l16_.get('confirm')):
        sys.exit('### data/%s_l16.json DOES NOT CARRY (7)`s LINES AND ITS CONFIRM -- NOTHING COMPOSED' % ACT)
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b755: no order entered this act ((R365)(9) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                vers=[(v_, c_, int(n_), int(w_)) for v_, c_, n_, w_ in vs_],   # ### v1.34.6: (version, controls, cases, as wanted)
                cf_rows=int(cf_[0]), cf_items=int(cf_[1]),
                wk_held=int(wk_[0]), wk_of=int(wk_[1]), wk_refuted=int(wk_[2]), wk_unscorable=int(wk_[3]), wk_c23=wk_[4], wk_c31=wk_[5],
                wk_primes=(int(wk_[6]), int(wk_[7])), wk_cubic=(int(wk_[8]), int(wk_[9])), wk_mism=int(wk_[10]), wk_model=(int(wk_[11]), int(wk_[12])),
                wk_bound=int(wk_[13]), wk_secs=int(wk_[14]),
                lt_queries=int(lt_[0]), lt_content=int(lt_[1]), lt_content_rows=lt_[2], lt_notread=int(lt_[3]), lt_notread_rows=lt_[4],
                cd_rep=int(cd_[0]), cd_labels=cd_[1], cd_plants=int(cd_[2]),
                ce_lower=ce_[0], ce_ceiling=int(ce_[1]), ce_word=ce_[2],
                rt_height=rt_[0], rt_high=int(rt_[1]), rt_band=int(rt_[2]), rt_all=int(nr_[0]),
                ls_height=ls_[0], ls_bands=int(ls_[1]), ls_complete=int(ls_[2]), ls_online=int(ls_[3]), ls_offline=int(ls_[4]), ls_ctl=lc_[0], ls_maxre=mx_[0],
                zf_height=int(zf_[0]), zf_verdict=zf_[1], zf_zeros=int(zf_[2]), zf_roots=int(zf_[3]),
                rc_verdict=rc_[0], rc_s=int(rc_[1]), rc_max=int(rc_[2]), rc_pairs=int(rp_[1]), rc_draws=int(rp_[2]), rc_heights=int(rp_[3]), rc_seed=int(rp_[5]), rc_mean=rp_[6],
                rcc_s=int(rcc_[0]), rcc_max=int(rcc_[2]),
                cs_height=cs_[0], cs_count=int(cs_[1]), cs_least=cs_[2], cs_ctl_to=int(cs_[3]), cs_ctl=cs_[4],
                l16_lines=[(x_.get('item'), x_.get('line')) for x_ in l16_.get('lines') or []], l16_confirm=l16_.get('confirm'),
                l16_counts=(l16_.get('count_before'), l16_.get('count_after')),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R365): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b755_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b755_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b755's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line);
# ### the census's control read as its bank prints it, beside the figures and after them (its tool's form, data/b755_census_from_primes.txt :20)
N2_CONTROLS = (('data/b755_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b755_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b755_standing_v1346.txt', '## THE CONTROLS', '### ### **v1.34.6: CONTROLS '),
               ('data/b755_walk.txt', 'THE CONTROLS FIRST (data/b755_coeffs_controls.json', '### THE ROWS, EACH ON THE FALSIFIER'),
               ('data/b755_cand_a.txt', '## THE CONTROLS, BEFORE ANY ROW', '## THE ROWS'),
               ('data/b755_cand_c.txt', 'THE CONTROLS FIRST (the divisor recursion', 'THE ROWS:'),
               ('data/b755_cand_j.txt', 'THE CONTROLS AGAINST PRINT, BEFORE ANY ROW', 'THE ROWS, the eighteen fields'),
               ('data/b755_list_59.txt', '### THE CONTROLS, PRINTED BEFORE THE FIGURES', '  band [0.5, 15.0]'),
               ('data/b755_census_from_primes.txt', '  THE CONTROL BESIDE IT', '  P = 100000: roots'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
N2_SECTIONS = ()
N2_RIDERS = ('data/b755_steps.json', 'data/b755_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


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
    """N2 (R365): the step-zero reads, the chain read and the carry printed before any write (the step-zero bank's times before the
    act_current commit); step zero's commits, v1.34.6, the lock gate carried, the weight and corrigendum (PLACE-papers, then relay), the walk's
    generator and its bank, the literature bank, the candidates' generators and banks, the candidates bank with the prior clause, the ceiling,
    each rule, the list of roots, the engine, the list with the verdicts, the census's generator and its bank, [L16]'s generator and its
    PLACE-papers write, in that order by time; the standing change landing before the gate, VERSION moved with its controls bank, no other
    commit of the act under tools/standing/; each generator of the act first added by a commit of its own carrying it and not its bank, the
    bank's commit not the generator; each tool's controls before its figures (the census's control as its bank prints it); the prior clause
    and the literature bank banked before either rule; each rule committed alone (H-RECURRENCE with its null's generator and seed, as
    (5)(iii) orders); the list of roots committed before the engine and its controls; the null with its seed before the certified list; the
    (W) regeneration, the pre-lock comparison and the probe-path refusal before the lock gate; v1.34.6 an ancestor of HEAD."""
    ct_ = lambda r_, h_: int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0)
    chain_ = [(ROOT, K.ACT_CURRENT_COMMIT), (ROOT, K.STEPZERO), (ROOT, K.STEPZERO_PREVBUILD), (ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING),
              (ROOT, K.C1_LOCKGATE), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_PLAN_FIRST), (ROOT, K.C2_RELAY), (ROOT, K.C3_LITERATURE)] \
        + [(ROOT, h_) for h_ in K.C3_RELAY[1:]] + [(ROOT, K.C4_RULE_ZEROS), (ROOT, K.C4_RULE_RECUR), (ROOT, K.C4_ROOTS), (ROOT, K.C4_ENGINE),
                                                  (ROOT, K.C4_LIST), (ROOT, K.C5_GEN), (ROOT, K.C5_RELAY), (ROOT, K.L16_GEN), (PP, K.L16_PP)]
    tm_ = [ct_(r_, h_) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    files_ = lambda h_: [x for x in g(ROOT, 'show', '--name-only', '--format=', h_).split() if x.strip() and x not in N2_RIDERS]
    # ### the step-zero reads, the chain read and the carry, each with its time in the step-zero bank, before the act_current commit
    sz_ = rdn('%s_stepzero.txt' % ACT)
    szt_ = [(n_, re.search(p_, sz_)) for n_, p_ in (('the step-zero reads', r'THE STEP-ZERO READS \((\d\d:\d\d:\d\d)Z, before any write\)'),
                                                    ('the chain read', r'THE CHAIN READ \((\d\d:\d\d:\d\d)Z\)'),
                                                    ('the carry', r'THE CARRY before any write of the relay: .*?\((\d\d:\d\d:\d\d)Z'))]
    sze_ = [(n_, _hms_epoch(m_.group(1)) if m_ else None) for n_, m_ in szt_]
    stepzero_ = all(e_ for _n, e_ in sze_) and [e_ for _n, e_ in sze_] == sorted(e_ for _n, e_ in sze_) and sze_[-1][1] < tm_[0]
    # ### the standing change: VERSION moved with its controls bank at v1.34.6's commit, the act's one commit under tools/standing/
    st_commits_ = [h_ for h_ in g(ROOT, 'log', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()]
    standing_ = 'tools/standing/VERSION' in files_(K.C1_STANDING) and 'data/%s_standing_v1346.txt' % ACT in files_(K.C1_STANDING) \
        and [h_[:8] for h_ in st_commits_] == [K.C1_STANDING[:8]]
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, 'HEAD'], capture_output=True).returncode == 0
    # ### each generator before its bank (K.GENS)
    gens_ok_ = []
    for n_, tool_, gens_, data_, bank_ in K.GENS:
        fa_ = _first_add(tool_)
        gens_ok_.append((n_, bool(fa_) and fa_ == g(ROOT, 'rev-parse', gens_[0]).strip() and all(tool_ in files_(h_) and data_ not in files_(h_) for h_ in gens_)
                         and data_ in files_(bank_) and tool_ not in files_(bank_) and max(ct_(ROOT, h_) for h_ in gens_) < ct_(ROOT, bank_)))
    gen_ = len(gens_ok_) == len(K.GENS) >= 12 and all(o_ for _n, o_ in gens_ok_)
    # ### the prior clause and the literature before either rule; each rule alone; the roots before the engine; the null before the list
    r1_, r2_, r3_ = (g(ROOT, 'show', '%s:data/%s_registrations.txt' % (h_, ACT)) or '' for h_ in (K.C3_CANDIDATES, K.C4_RULE_ZEROS, K.C4_RULE_RECUR))
    prior_ = ct_(ROOT, K.C3_LITERATURE) < ct_(ROOT, K.C3_CANDIDATES) < ct_(ROOT, K.C4_RULE_ZEROS) and _first_add('data/%s_registrations.txt' % ACT) == g(ROOT, 'rev-parse', K.C3_CANDIDATES).strip() \
        and '## (1) THE PRIOR CLAUSE' in r1_ and '## (2) THE RULE' not in r1_ and 'data/%s_literature.txt' % ACT in files_(K.C3_LITERATURE)
    alone_ = files_(K.C4_RULE_ZEROS) == ['data/%s_registrations.txt' % ACT] and sorted(files_(K.C4_RULE_RECUR)) == ['data/%s_registrations.txt' % ACT, 'tools/%s_recur.py' % ACT] \
        and '## (2) THE RULE (H-ZEROS-FROM-PRIMES)' in r2_ and '## (3) THE RULE (H-RECURRENCE)' not in r2_ and '## (3) THE RULE (H-RECURRENCE)' in r3_ and r2_ and r3_.startswith(r2_.rstrip(NL))
    lc0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) ; ', (rdn('%s_list_59_controls.txt' % ACT).split(NL) or [''])[0])
    roots_ = ct_(ROOT, K.C4_RULE_RECUR) < ct_(ROOT, K.C4_ROOTS) < ct_(ROOT, K.C4_ENGINE) < ct_(ROOT, K.C4_LIST) and bool(lc0_) \
        and (_iso_epoch(lc0_.group(1)) or 0) > ct_(ROOT, K.C4_ROOTS) and 'The list of roots at -59 (data/%s_roots_59.txt) committed before any band ran.' % ACT in rdn('%s_list_59.txt' % ACT)
    null_ = 'SEED = 59' in (g(ROOT, 'show', '%s:tools/%s_recur.py' % (K.C4_RULE_RECUR, ACT)) or '') and ct_(ROOT, K.C4_RULE_RECUR) < ct_(ROOT, K.C4_ENGINE)
    sect_ = stepzero_ and standing_ and gen_ and prior_ and alone_ and roots_ and null_
    route_ = sect_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT, optional=True)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the step-zero reads, the chain read and the carry printed before any write (%s, each by the step-zero bank, before the act_current commit %s): %s; the standing change landing before the gate, v1.34.6 moving VERSION with its controls bank, the act`s one commit under tools/standing/ (%s): %s; each generator first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the generator (%s): %s; the prior clause and the literature bank banked before either rule (literature %s, the prior clause %s): %s; each rule committed alone, H-RECURRENCE with its null`s generator (%s, %s): %s; the list of roots committed before the engine, the engine`s controls run after it, before the list (%s, %s, %s): %s; the null with its seed committed before the certified list exists: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero`s commits, v1.34.6, the lock gate, the weight and corrigendum, the c1 route, the walk`s generator and bank, the literature, Component 3`s %d commits after it, the two rules, the roots, the engine, the list, the census`s generator and bank, [L16]`s generator and its PLACE-papers write, in that order by time: %s (%s); v1.34.6 an ancestor of HEAD: %s; the tools` controls before their figures: %s' % (
            ', '.join('%s %s' % (n_, ('%sZ' % m_.group(1)) if m_ else 'unread') for n_, m_ in szt_), K.ACT_CURRENT_COMMIT, stepzero_,
            ' '.join(h_[:8] for h_ in st_commits_) or 'none', standing_, ', '.join('%s %s' % x_ for x_ in gens_ok_), gen_,
            K.C3_LITERATURE, K.C3_CANDIDATES, prior_, K.C4_RULE_ZEROS, K.C4_RULE_RECUR, alone_, K.C4_ROOTS, K.C4_ENGINE, K.C4_LIST, roots_, null_,
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_,
            len(K.C3_RELAY) - 1, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b755's objects): the banks whose grade prints at their end, (bank, the words the foot carries); the reproduction run and the
# ### address scan written before the gate
N3_GRADED = (('b755_walk.txt', ('H-C3-LAW: 14 OF 14 HELD', 'REFUTED 0')),
             ('b755_literature.txt', ('THE LITERATURE:', 'SOURCES READ AT CONTENT', 'NOT READ')),
             ('b755_candidates.txt', ('THE CANDIDATES: REPRODUCED 6', 'EACH FAILING AS WANTED')),
             ('b755_cand_a.txt', ('REPRODUCED', 'CONTROLS ALL AS WANTED')), ('b755_cand_a_plant.txt', ('AS WANTED',)),
             ('b755_cand_c.txt', ('THE CONTROLS AS WANTED',)), ('b755_cand_c_plant.txt', ('AS WANTED',)),
             ('b755_cand_h.txt', ('EVERY ZERO FOUND WITHIN 0.02',)), ('b755_cand_h_plant.txt', ('RISE IN BOTH GROUPS',)),
             ('b755_cand_j.txt', ('BOTH CONTROLS WITHIN 1e-6',)), ('b755_cand_j_plant.txt', ('AS WANTED',)),
             ('b755_cand_k.txt', ('BOTH IDENTITIES 0 MISMATCHES',)), ('b755_cand_k_plant.txt', ('AS WANTED',)),
             ('b755_cand_l.txt', ('ABOVE',)), ('b755_cand_l_plant.txt', ('AS WANTED',)),
             ('b755_ceiling.txt', ('THE CEILING AFTER COMPONENT 3', 'NOTHING CARRIED')),
             ('b755_registrations.txt', ('THE PRIOR CLAUSE:', 'NOT RUN AT -59')),
             ('b755_roots_59.txt', ('THE LIST AT -59 TO 200.00',)),
             ('b755_list_59_controls.txt', ('AS WANTED.',)),
             ('b755_list_59.txt', ('THE LIST COMPLETE TO 200.0', 'COMPLETE 14')),
             ('b755_zeros_from_primes_59.txt', ('H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT 200:',)),
             ('b755_recur_control.txt', ('H-RECURRENCE\'S CONTROL: S = 168, AS WANTED',)),
             ('b755_recur_59.txt', ('H-RECURRENCE AT -59:',)),
             ('b755_census_from_primes.txt', ('(6), EXPLORATORY', 'ONE TO ONE')),
             ('b755_standing_v1346.txt', ('v1.34.6: CONTROLS', 'ALL AS WANTED')),
             ('b755_corrigendum.txt', ('ITEMS',)), ('b755_carried_faults.txt', ('THE CARRIED FAULTS', 'REPAIRED HERE 0')),
             ('b755_citation_check.txt', ('THE CHECK CLEAN',)), ('b755_reproduce.txt', ('REPRODUCES',)), ('b755_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### N3 (R365): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word; the centre
# ### matcher over zeta (the symbol, Riemann's, or a zeta function not the Epstein's), RH, GRH and Weil positivity on classK, (R365)'s N3
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
N3_LOC = (r'(?:\b(?:RH|GRH|classK)\b|ζ|\bRiemann(?:`s|\'s)? zeta\b|(?<!Epstein )\bzeta function\b|\bWeil positivity on classK\b).*'
          r'\b(?:holds|hold|fails|fail|proved|refuted|moved)\b')
N3_BANKS = ('stepzero', 'corrigendum', 'carried_faults', 'walk', 'literature', 'candidates', 'ceiling', 'registrations', 'roots_59', 'list_59',
            'list_59_controls', 'zeros_from_primes_59', 'recur_59', 'recur_control', 'census_from_primes', 'standing_v1346', 'events', 'defects')
# ### N3 (R365): each candidate's sourcing line names the prior work the ruling names, at content or NOT READ -- (candidate, the bank's words
# ### in its PRIOR WORK paragraph, the literature bank's row the words cite); (a) and (c) carry none in the ruling ((4)(a), (4)(c))
N3_PRIOR = (('(h)', 'Lee, arXiv 1204.6297, section 3.1 (T2.c', 'T2.c'),
            ('(h)', 'Bombieri and Ghosh 2011, section 9 (T1.j', 'T1.j'),
            ('(j)', 'Bombieri and Ghosh 2011, Theorem 7, for the Davenport-Heilbronn family (T1.f', 'T1.f'),
            ('(k)', '"classical genus theory", as the ruling names it, with no source: NOT READ (N10)', 'N10'),
            ('(l)', 'van de Lune and te Riele, Mathematisch Centrum NW 44/77 (1977), Lemma 5.1, almost-periods of the partial sums of zeta from '
                    'rational approximations to ratios of logarithms of primes (T7.c', 'T7.c'))
N3_SOURCED = ('(a)', '(c)', '(h)', '(j)', '(k)', '(l)')   # ### each reproduced candidate's block carries its (S1) line
# ### N3 (R365): no figure of the navigator's workspace printed as a banked figure -- each NAVIGATOR'S SCRIPT paragraph of the candidates bank
# ### says its figures stand in no bank; the walk's bank and its controls print the act's figure for the plant and not the ruling's 1,401
# ### (data/b755_events.txt (12))
N3_NAV = ('in no bank', 'kept no output', 'no output kept', 'kept in no file')
N3_NAV_FIGS = r'(?<![\d,.])1,?401(?![\d,])'


def _own_sentences(t):
    """the act's own sentences of a bank: the quote rows (`  :n "...`) and the quoted spans dropped, the `### ` lines dropped."""
    ls = []
    for l in (t or '').replace(chr(13), '').split(NL):
        if not l.strip() or l.startswith('### ') or re.match(r'^\s+:\d+(?:-:\d+)? ["“]', l):
            continue
        ls.append(re.sub(r'“[^”\n]*”', '“…”', re.sub(r'"[^"\n]*"', '"…"', l)).strip())
    return [x for x in re.split(r'(?<=[.;])\s+', ' '.join(ls)) if x.strip()]


def _integ_line(f):
    """the entry's last line, (R365)'s INTEGRATION line (data/b755_ferry.txt :52) composed from the banks' feet through _figs; the zeros'
    verdict carries `a vacuous pass` in its own clause where both populations of the falsifier are empty (data/b755_events.txt (16))."""
    vac_ = ', a vacuous pass' if f['zf_verdict'] == 'HELD' and f['zf_zeros'] == 0 and f['zf_roots'] == 0 else ''
    return ('INTEGRATION: the walk: %d of %d fields held; the candidates: %d reproduced, %d plants failing as wanted; the zeros from the primes '
            'at -59 %s to height %d, %d zeros of real part at least 0.85 against %d roots%s; the recurrence %s, S = %d against the largest draw %d; '
            'the literature bank: %d sources at content, %d not read; nothing built' % (
                f['wk_held'], f['wk_of'], f['cd_rep'], f['cd_plants'], f['zf_verdict'].lower(), f['zf_height'], f['zf_zeros'], f['zf_roots'], vac_,
                f['rc_verdict'].lower(), f['rc_s'], f['rc_max'], f['lt_content'], f['lt_notread']))


def _cand_blocks():
    """the candidates bank's blocks by their label, each block's lines stripped and joined by one space (the bank hard-wraps)."""
    out_ = {}
    for ch_ in rdn('%s_candidates.txt' % ACT).replace(chr(13), '').split('\n## ')[1:]:
        out_.setdefault(ch_.split(' ', 1)[0], ' '.join(l_.strip() for l_ in ch_.split(NL) if l_.strip()))
    return out_


def _prior_rows():
    """N3 (R365): for each (candidate, words, row) of N3_PRIOR, whether the words stand in that candidate's PRIOR WORK paragraph and the row
    in the literature bank; and the reproduced candidates whose block carries no (S1) line."""
    bl_, lit_ = _cand_blocks(), rdn('%s_literature.txt' % ACT)
    rows_ = []
    for c_, w_, r_ in N3_PRIOR:
        b_ = bl_.get(c_, '')
        i_ = b_.find('PRIOR WORK')
        pw_ = b_[i_:b_.find('(S1):', i_)] if i_ >= 0 else ''
        rows_.append((c_, r_, w_ in pw_ and bool(re.search(r'(?m)^\s+%s\s' % re.escape(r_), lit_))))
    return rows_, [c_ for c_ in N3_SOURCED if '(S1): ' not in bl_.get(c_, '')]


def _nav_rows():
    """N3 (R365): the candidates bank's NAVIGATOR'S SCRIPT paragraphs, those saying no bank holds their figures, and the walk's banks
    printing the ruling's workspace figure 1,401."""
    ps_ = [' '.join(p_.split()) for p_ in re.findall(r"(?ms)^  THE NAVIGATOR'S SCRIPTS?: (.*?)(?=^  \S)", rdn('%s_candidates.txt' % ACT).replace(chr(13), ''))]
    bad_ = [p_[:48] for p_ in ps_ if not any(w_ in p_ for w_ in N3_NAV)]
    wf_ = [n_ for n_ in ('%s_walk.txt' % ACT, '%s_coeffs_controls.json' % ACT) if re.search(N3_NAV_FIGS, rdn(n_))]
    return len(ps_), bad_, wf_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R365): no sentence of the act says that anything of zeta, RH, GRH or Weil positivity on classK holds, fails or moved, outside a
    negation; no bank and no sentence of the entry calls a result new or the earliest of its kind; each candidate's sourcing line names the
    prior work the ruling names, at content or NOT READ, with its row in the literature bank; no figure of the navigator's workspace printed
    as a banked figure; the verdicts of (3) and (5) read against the registered rows and rules and against nothing written after them (b753's
    registration equal to its blob at the commit the walk names, data/b755_registrations.txt written by no commit after the second rule, each
    verdict bank saying so); each bank's foot carrying its grade; each matcher's control caught; the entry's last line (R365)'s INTEGRATION
    line composed from the banks; the banks' nouns in the entry; the root prompt's sentences about the entry the composer's. From the banks'
    last lines and own sentences, git, the entry's sentences and the root prompt in the answers bank. The deposit clause of b749 to b754 is no
    clause of (R365)'s N3 and is not read here; N5 reads the deposits."""
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
    nsents_ = []
    for b_ in N3_BANKS:
        nsents_ += _own_sentences(rdn('%s_%s.txt' % (ACT, b_)))
    neg_ = N3_NEG
    ctl3_ = dict(lit=bool(re.search(N3_LIT, 'The walk is a new result.', re.I)), loc=bool(re.search(N3_LOC, 'RH holds at every height.')),
                 loc_k=bool(re.search(N3_LOC, 'Weil positivity on classK holds.')), loc_e=not re.search(N3_LOC, 'The Epstein zeta function holds no zero there.'),
                 neg=bool(re.search(neg_, 'RH is not proved.')))
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    # ### the prior work each candidate's sourcing line names; the navigator's figures; the verdicts against the registered rows and rules
    prior_, unsourced_ = _prior_rows()
    navn_, navbad_, navfig_ = _nav_rows()
    b753_ = (rd(os.path.join(ROOT, 'data', 'b753_registrations.txt'), optional=True) or '') == (g(ROOT, 'show', '%s:%s' % (K.REG_WALK[1], K.REG_WALK[0])) or None)
    walkreg_ = 'its bytes equal to its blob at %s' % K.REG_WALK[1] in rdn('%s_walk.txt' % ACT)
    late_ = [h_ for h_ in g(ROOT, 'log', '--format=%h', '%s..HEAD' % K.C4_RULE_RECUR, '--', 'data/%s_registrations.txt' % ACT).split() if h_.strip()]
    vsay_ = ['data/%s_registrations.txt (2) and nothing written after it' % ACT in rdn('%s_zeros_from_primes_59.txt' % ACT),
             'rule of data/%s_registrations.txt (3) and nothing written after it' % ACT in rdn('%s_recur_59.txt' % ACT)]
    verd_ = b753_ and walkreg_ and not late_ and all(vsay_)
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    nouns_ = [w_ for w_ in ('H-C3-LAW', 'H-ZEROS-FROM-PRIMES', 'H-RECURRENCE', '[L16]', 'v1.34.6', 'data/%s_walk.txt' % ACT, 'data/%s_candidates.txt' % ACT,
                            'data/%s_literature.txt' % ACT, 'data/%s_registrations.txt' % ACT, 'data/%s_list_59.txt' % ACT,
                            'data/%s_census_from_primes.txt' % ACT, 'data/%s_corrigendum.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not more_ and not first_ and not loc_ and all(o_ for _c, _r, o_ in prior_) \
        and not unsourced_ and navn_ == 6 and not navbad_ and not navfig_ and verd_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence passed, a negation read): %s; over %d of the act`s own sentences and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; each candidate`s sourcing line naming the prior work the ruling names, with its row in the literature bank (relay data/%s_candidates.txt, data/%s_literature.txt): %s, the reproduced candidates with no (S1) line: %s; the navigator`s workspace figures: %d of its scripts` paragraphs read, saying no bank holds their figures but %s, the walk`s banks printing the ruling`s 1,401: %s; the verdicts against the registered rows and rules and nothing written after them: data/b753_registrations.txt equal to its blob at %s %s, the walk naming that blob %s, data/%s_registrations.txt written after %s by %s, each verdict bank saying so %s: %s; the entry`s last line (R365)`s INTEGRATION line composed from the banks (%s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', ACT, ACT, ', '.join('%s %s %s' % x_ for x_ in prior_), unsourced_ or 'NONE',
            navn_, navbad_ or 'NONE', navfig_ or 'NONE', K.REG_WALK[1], b753_, walkreg_, ACT, K.C4_RULE_RECUR, late_ or 'NONE', vsay_, verd_,
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
#⟪OVERRIDE record MARK 82a559f5c96c 2⟫
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    tag_one = _ef_now[0] == _ef_prev[0] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **{'v0.38': '14ca572'})
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main == K.EF_MAIN and sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) == ['v0.37', 'v0.38'] \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') and ch_ok \
        and bool(prev) and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 (made at b754 under (R364)(3), after b754`s face), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R365)(9), N5: no kernel touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act), and no other exception: (R365) writes no kernel branch; no
    # ### .lean file changed or untracked in a kernel's tree; the rebuild-b721 branches kept as b753 left them; the address scan's count from its
    # ### bank (relay data/b755_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R354)(2)(v): the face's branch list (none this act)
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
    # ### (R364)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', re.sub(r'"(?:[^"\\]|\\.)*"|\'[^\']*\'', '""', r_.get('cmd') or ''))]   # ### b754 (p''): a run of gh, not its words inside a quoted argument (a commit's words, the capture's row 1001)
    # ### v1.30.0, (R360)(3)(vi), b749 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R364)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and not zdel_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b755_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel (no kernel touched, (R365)(9); a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b755 step zero: the ruling's ordinal and title (the ferry's ACT line, data/b755_ferry.txt :40) as it stands; adjusted at Component 6
    # ### to what the act did
    return ('### b755 — lane two, act one hundred and eighty-two, the class-number-3 walk under (R365): b754 at its weight; a short corrigendum; '
            'H-C3-LAW at its fourteen fields; the candidates reproduced with their plants and their prior work; H-ZEROS-FROM-PRIMES and H-RECURRENCE '
            'registered at -59 and tested by the certified engine; one line for OPEN_TRAILS; nothing built')
#⟪END⟫
#⟪SECTION record 29⟫
# ### b755: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict


def _guard(f):
    """the composer's refusals before any sentence: v1.34.6 alone, all as wanted; the walk's rows summing to its fields; the candidates'
    count equal to its labels; the zeros' verdict reading the roots bank's count; the list complete in every band; the recurrence's verdict
    agreeing with S against the largest draw (or NOT DECIDED); [L16]'s bank carrying its lines and its confirm."""
    if [v_ for v_, _c, _n, _w in f['vers']] != ['v1.34.6'] or any(n_ != w_ for _v, _c, n_, w_ in f['vers']):
        sys.exit('### THE STANDING VERSION IS NOT v1.34.6 ALL AS WANTED -- NOTHING COMPOSED')
    if f['wk_held'] + f['wk_refuted'] + f['wk_unscorable'] != f['wk_of']:
        sys.exit('### THE WALK`S ROWS DO NOT SUM TO ITS FIELDS -- NOTHING COMPOSED')
    if f['cd_rep'] != len(re.findall(r'\([a-z]\)', f['cd_labels'])):
        sys.exit('### THE CANDIDATES` COUNT IS NOT ITS LABELS -- NOTHING COMPOSED')
    if f['zf_roots'] != f['rt_high'] or f['ls_complete'] != f['ls_bands']:
        sys.exit('### THE ZEROS` VERDICT DOES NOT READ THE ROOTS BANK, OR THE LIST IS NOT COMPLETE IN EVERY BAND -- NOTHING COMPOSED')
    if f['rc_verdict'] != 'NOT DECIDED' and (f['rc_verdict'] == 'HELD') != (f['rc_s'] > f['rc_max']):
        sys.exit('### THE RECURRENCE`S VERDICT DISAGREES WITH S AGAINST THE LARGEST DRAW -- NOTHING COMPOSED')
    if not f['l16_lines'] or not f['l16_confirm']:
        sys.exit('### [L16]`S BANK CARRIES NO LINES OR NO CONFIRM -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 6 order ("the FINDINGS entry titled by its objects", data/b755_ferry.txt :52):
    the walk (b755_walk); the candidates (b755_candidates); the two verdicts at -59 (b755_zeros_from_primes_59, b755_recur_59), the zeros'
    vacuous pass said in its own clause; the literature bank (b755_literature); nothing built. Each finding's name in the heading, for the
    line reader. Every figure from the banks' feet."""
#⟪END⟫
#⟪SECTION record 31⟫
    _guard(f)
    vac_ = ', a vacuous pass' if f['zf_verdict'] == 'HELD' and f['zf_zeros'] == 0 and f['zf_roots'] == 0 else ''
    return ('## The class-number-3 walk and two predictions at -59 under (R365): H-C3-LAW %s at %s of its %s fields (b755_walk); %s candidates '
            'reproduced, %s plants failing as wanted (b755_candidates); H-ZEROS-FROM-PRIMES %s to height %d, %d zeros of real part at least 0.85 '
            'against %d roots%s (b755_zeros_from_primes_59), and H-RECURRENCE %s, S = %d against the largest draw %d (b755_recur_59); the literature '
            'bank %d sources at content, %d not read (b755_literature); nothing built' % (
                'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', num_word(f['wk_held']), num_word(f['wk_of']),
                num_word(f['cd_rep']), num_word(f['cd_plants']), f['zf_verdict'].lower(), f['zf_height'], f['zf_zeros'], f['zf_roots'], vac_,
                f['rc_verdict'].lower(), f['rc_s'], f['rc_max'], f['lt_content'], f['lt_notread']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) H-ZEROS-FROM-PRIMES read HELD by its rule with the falsifier`s population empty on both sides, 0 zeros and 0 roots of real part at least 0.85 to height 200: a vacuous pass at the rule`s threshold and no evidence for the prediction; the verdict bank prints the rule`s verdict alone, as its tool wrote it, and the entry carries the counts beside it in the same clause (relay data/b755_events.txt (16)); '
            '(2) the census`s control printed after its figures, against N2`s words, and N2 read by the clause as written, its clause of the controls failing on that bank (relay data/b755_defects.txt (l)); '
            '(3) the seat`s readings of (6), fixed in its generator`s head before the run: to height 5,000 as five segments of the scan, counted at the route`s Newton bound 3 x 10^5, the three prime bounds 10^5, 3 x 10^5 and 10^6 refining the same minima (relay tools/b755_census.py :12-:18); and of (4)(l)`s same range as the 69 heights` own (relay data/b755_candidates.txt, (l)); '
            '(4) the second route`s plant at -23 reading 1,014 mismatches where the ruling quotes the navigator`s workspace at 1,401, the bank printing the act`s figure alone (relay data/b755_events.txt (12)); and the figure 1.133906322 at -20 standing in no source read, printed beside the computed value and no control (relay data/b755_literature.txt R4); '
            '(5) an older row of the corrigenda bank naming the data volume`s folder in two quoted paths, which part of the amendment row 1 reads it being the author`s (relay data/b755_events.txt (11)); defects (b), (e) and the tools` (c) and (d) entered with no clause ordering their repair, (c) answered at step zero by the author`s answer to put_1, the others open for the author (relay data/b755_defects.txt); '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R365)(8)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b755's objects; b754's composer in git at
    b754's record tool). Its last line (R365)'s INTEGRATION line, composed from the banks' feet (_integ_line)."""
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
    co_ = jl('%s_corrigendum.json' % ACT)
    ps_ = ((co_.get('by_bank') or {}).get('postseal') or {}).get('total', '-')   # ### b754's post-seal events, the corrigendum json's count
    v_, _vc, vn_, vw_ = f['vers'][0]
    vac_ = (', a vacuous pass at the rule`s threshold and no evidence for the prediction' if f['zf_verdict'] == 'HELD' and f['zf_zeros'] == 0
            and f['zf_roots'] == 0 else '')
    e = ['', _title(), '',
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b755_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b755_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b755_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b755_zeros_from_primes_59.txt, data/b755_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b755 on the author’s ruling `(R365)` and its two amendment rows (relay data/b755_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b755_corrigendum.txt`, `data/b755_carried_faults.txt`, `data/b755_standing_v1346.txt`, `data/b755_walk.txt`, `data/b755_coeffs_controls.json`, `data/b755_literature.txt`, '
         '`data/b755_cand_a.txt` to `data/b755_cand_l_plant.txt`, `data/b755_candidates.txt`, `data/b755_ceiling.txt`, `data/b755_registrations.txt`, `data/b755_roots_59.txt`, '
         '`data/b755_list_59.txt`, `data/b755_list_59_controls.txt`, `data/b755_zeros_from_primes_59.txt`, `data/b755_recur_59.txt`, `data/b755_recur_control.txt`, '
         '`data/b755_census_from_primes.txt`, `data/b755_l16.json`, `data/b755_put_1.json`, `data/b755_put_2.json`, `data/b755_author_answers.txt`, `data/b755_events.txt`, '
         '`data/b755_defects.txt`, `data/b755_prelock.txt`, `data/b755_pathrefusal.txt`, `data/b755_reproduce.txt`, `data/b755_address_scan.txt`, `data/b755_touch.txt`, '
         '`data/b755_standing_figures.txt`, `data/b755_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R365)(1), (2); relay %s, %s, PLACE-papers %s): b754 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b754’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b755_corrigendum.txt). Its three repairs: the lock gate carried as tools/b755_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b755_standing_v1346.txt; the amendment row 1). '
         'The open items of b754`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b755_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R365)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b755_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b755_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b755_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b755_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R365)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b755_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b755_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R365)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b755_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes` phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b755_candidates.txt, data/b755_cand_a.txt to data/b755_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R365)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b755_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b755_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b755_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b755_zeros_from_primes_59.txt, data/b755_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b755_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b755_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R365)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b755_defects.txt (l)); its generator committed at relay %s before its run (relay data/b755_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R365)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b755_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R365)(8)): the price table at step zero from banked timings where a bank held one (relay data/b755_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b755_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b755_stepzero.txt); step zero from %s (data/act_current.json) through b754`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]`s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b755_prelock.txt, data/b755_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b755_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b755_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b755_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
         '**The standing arms**: the four figures at b755 -- %s, %s, %s, %s -- against b754’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b755_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b755_citation_check.txt, data/b755_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R365)(8), as the author answers the one question at the root: the clearing act as b756 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]`s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b756 with the clearing act after it; defects (b), (e) and the tools` (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH, GRH or Weil positivity on classK holds or fails, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b754():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b755's objects; b754's composer in git at b754's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the ledger writes; the walk, the literature, the candidates, the two rules and
    their verdicts, the census, (7)'s line and the ceiling; the standing version."""
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
    vac_ = ', a vacuous pass' if f['zf_verdict'] == 'HELD' and f['zf_zeros'] == 0 and f['zf_roots'] == 0 else ''
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R365) ratified.** Its components as the ferry orders them (relay data/b755_ferry.txt), with its two amendment rows (relay data/b755_amendments.json), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b754’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md (7)`s line under its dated head (PLACE-papers %s); no order entered; no paper written; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.L16_PP[:8]), '',
             '**The walk:** H-C3-LAW %d of %d HELD, %d REFUTED, %d NOT SCORABLE, the control rows -23 %s and -31 %s, through %d (relay data/b755_walk.txt); the sixteen fields all of class number 3 by the literature bank`s reading at content (relay data/b755_literature.txt R9).' % (
                 f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_bound']), '',
             '**The literature and the candidates:** %d sources at content, %d not read (relay data/b755_literature.txt); %d candidates reproduced (%s), %d plants failing as wanted, each row`s sourcing line naming the prior work the ruling names (relay data/b755_candidates.txt).' % (
                 f['lt_content'], f['lt_notread'], f['cd_rep'], f['cd_labels'], f['cd_plants']), '',
             '**The two rules at -59:** each committed alone before the list of roots, the roots before the engine, the engine`s controls %s; the certified list complete to %s, %d off-line pairs; H-ZEROS-FROM-PRIMES %s, %d zeros against %d roots of real part at least 0.85%s; H-RECURRENCE %s, S = %d against the largest draw %d, its control at -23 S = %d (relay data/b755_registrations.txt, data/b755_list_59.txt, data/b755_zeros_from_primes_59.txt, data/b755_recur_59.txt, data/b755_recur_control.txt).' % (
                 f['ls_ctl'], f['ls_height'], f['ls_offline'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_max'], f['rcc_s']), '',
             '**After both verdicts, exploratory:** at -23 to height %s, %d roots of real part at least 0.85 at P = 3 x 10^5; the least height above Re s = 1: %s; its control %s, printed after its figures (relay data/b755_census_from_primes.txt; data/b755_defects.txt (l)).' % (
                 f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl'].lower()), '',
             '**The line of (7) and the ceiling:** [L16] %s (relay data/b755_l16.json); the ceiling after Component 3, %s h against %d h, %s (relay data/b755_ceiling.txt).' % (
                 f['l16_confirm'], f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower()), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The standing version:** %s (relay data/b755_standing_v1346.txt); HANDOFF.md regenerated once by tools/standing/handoff.py before the gate, at relay %s.' % (
                 '; '.join('%s %d of %d' % (v_, w_, n_) for v_, _c, n_, w_ in f['vers']), (K.HANDOFF_COMMIT or 'NOT MADE')[:8]), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b755_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b755_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b755_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b755 `%s` (previous `%s`, b754’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b755_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b755_standing_v1346.txt); the standing '
             'report tool (relay data/b755_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b754 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root with the two ledgers’ cuts beside it (the ferry`s Component 6), its file named in the closing by its name, bytes and hash and its folder by role ((R365)(2)(iii); relay data/b755_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b754’s %s, %s, %s, %s (relay data/b755_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b755_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b754():
    """b753's trail record over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b754 left them, the six; MEASURED off the six kernels` refs/heads.'),
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
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b754-closing, push-b754-preroot, push-b754-record; PLACE-papers push-b754-preroot, push-b754-record; each local, by name, through the one-call tool, after the --merged listing (data/b755_stepzero.txt :55-:60).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written this act ((R365)(9): no ledger row edited beyond the weight line, the corrigendum, the entry, the trail and (7)`s line).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R365)(2): FINDINGS :15252 (relay data/b755_corrigendum_landing.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R365)(2): row (75).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R365)(9)).'),
    ('walk rows read against their registration', 14, 14, 'rows', '### (R365)(3): the fourteen fields of data/b753_registrations.txt at its blob, 14 HELD, its two control rows beside them (relay data/b755_walk.txt).'),
    ('candidates reproduced, each by a generator committed before its run', 6, 6, 'candidates', '### (R365)(4): (a), (c), (h), (j), (k), (l) (relay data/b755_candidates.txt).'),
    ('planted errors run, each failing as wanted', 7, 7, 'plants', '### (R365)(4): one plant a candidate, two at (h); (c)`s first plant run defective and made again (relay data/b755_candidates.txt; data/b755_defects.txt (k)).'),
    ('rules registered at -59', 2, 2, 'rules', '### (R365)(5)(ii), (iii): H-ZEROS-FROM-PRIMES and H-RECURRENCE, each committed alone before the certified list (relay data/b755_registrations.txt (2), (3)).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R365) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b755_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.34.6`s controls, the walk, the literature, the candidates, the ceiling, the roots, the list`s controls, the list, the two verdicts, the recurrence`s control, the census, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### the rules of (5)(ii) and (iii) committed each alone beside the one-call tool`s step row and scan (relay 11fc3c93; a937fbb7 with the null`s generator), so a commit carrying data/b755_registrations.txt and no other path is none; MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### the roots, the list`s controls, the list and the two verdicts at -59, each first committed after H-ZEROS-FROM-PRIMES (relay 11fc3c93); MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2): no value of the function at -59 before the two rules and the list of roots; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R365)(9)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R365)(2)(iii) and the amendment row 1: tools/standing/ v1.34.6 by a version commit of its own with its controls in its bank (data/b755_standing_v1346.txt); MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b755_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, the literature`s searches and fetches under a generic client name, and the gh reads under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b755: the figure banks at -59, the field the two rules name (the walk's fields registered at b753, its bank read against that blob)
    fig_banks = [p for p in ('data/b755_roots_59.txt', 'data/b755_list_59_controls.txt', 'data/b755_list_59.txt', 'data/b755_zeros_from_primes_59.txt', 'data/b755_recur_59.txt')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b755_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b755_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1346', 'walk', 'literature', 'candidates', 'ceiling', 'roots_59', 'list_59_controls', 'list_59',
                                               'zeros_from_primes_59', 'recur_59', 'recur_control', 'census_from_primes', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b755_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b755_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b755_registration_%s.txt -- b755, THE CLASS-NUMBER-3 WALK: b754 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.34.6; "
                             "H-C3-LAW AT ITS FOURTEEN FIELDS; THE CANDIDATES REPRODUCED WITH THEIR PLANTS; H-ZEROS-FROM-PRIMES AND H-RECURRENCE "
                             "REGISTERED AT -59 AND TESTED BY THE CERTIFIED ENGINE; ONE LINE FOR OPEN_TRAILS; NOTHING BUILT, UNDER (R365)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b754's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b755: b754's lines read banks this
act does not write, and are not carried; the lines are b755's: tools/standing/ v1.34.6 by its controls, the list at -59 by the certified
engine and the six candidates reproduced with their plants (CERTIFIED); the walk against its registration, the prior clause and the
literature bank, and the two rules at -59 by their verdict banks (REGISTERED); the census, exploratory and marked so, (7)'s line [L16] of
pattern grade, and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b755's lines, each from the record tool's figures over b755's banks (REC._figs), the record's guard first
    REC._guard(f)
    vac_ = ', a vacuous pass at the rule`s threshold' if f['zf_verdict'] == 'HELD' and f['zf_zeros'] == 0 and f['zf_roots'] == 0 else ''
    # ------------------------------------------------------------------ REGISTERED: (R365)(3), the walk, against data/b753_registrations.txt at its blob
    sa = seat('%s_walk.txt' % ACT, '**H-C3-LAW: ')
    keys['WALK'] = ('REGISTERED -- H-C3-LAW AT ITS FOURTEEN FIELDS (data/b753_registrations.txt at relay %s): %d of %d HELD, %d REFUTED, %d not scorable; the controls -23 %s, -31 %s; the three primes as the row`s at %d of %d; the second route a cubic at %d of %d, mismatches %d; the bound %d; the generator at relay %s, committed before its run. SOURCE %s.' % (
        K.REG_WALK[1], f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
        f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_bound'], K.C2_PLAN_FIRST[:8], sa['text']))
    seats.append(sa)
    # ------------------------------------------------------------------ REGISTERED: (R365)(5)(i), the prior clause and the literature bank
    sb = seat('%s_literature.txt' % ACT, '**THE LITERATURE: QUERIES ')
    keys['LITERATURE'] = ('REGISTERED -- THE PRIOR CLAUSE AND THE LITERATURE BANK, before either rule: %d queries; %d sources read at content (%s); %d not read (%s); the bank at relay %s. SOURCE %s.' % (
        f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], sb['text']))
    seats.append(sb)
    # ------------------------------------------------------------------ REGISTERED: (R365)(5)(ii), H-ZEROS-FROM-PRIMES at -59
    sc = seat('%s_zeros_from_primes_59.txt' % ACT, '**H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT ')
    keys['ZEROS'] = ('REGISTERED -- H-ZEROS-FROM-PRIMES AT -59 TO HEIGHT %d: %s, %d zeros of real part at least 0.85 against %d roots%s; the rule at relay %s and the roots at %s, both before the certified list. SOURCE %s.' % (
        f['zf_height'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, K.C4_RULE_ZEROS[:8], K.C4_ROOTS[:8], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: (R365)(5)(iii), H-RECURRENCE at -59 (the name the template appends)
    sk = seat('%s_recur_59.txt' % ACT, '**H-RECURRENCE AT -59: ')
    keys['RECUR'] = ('REGISTERED -- H-RECURRENCE AT -59: %s, S = %d of %d pairs over %d heights against the largest of %d draws %d (mean %s, seed %d); its control at -23 S = %d against the null`s largest %d; the rule and its null at relay %s. SOURCE %s.' % (
        f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_max'], f['rc_mean'], f['rc_seed'], f['rcc_s'], f['rcc_max'],
        K.C4_RULE_RECUR[:8], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.34.6 ((R365)(2)(iii)), by its controls
    v_, c_, n_, w_ = f['vers'][0]
    sv = seat('%s_standing_v1346.txt' % ACT, '**%s: CONTROLS ' % v_)
    keys['V1346'] = ('CERTIFIED -- tools/standing/ %s: controls %s -- %d cases, %d as wanted; by a commit of its own moving VERSION, relay %s. SOURCE %s.' % (
        v_, c_, n_, w_, K.C1_STANDING[:8], sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: (R365)(5)(ii), the list at -59 by the certified engine
    sl = seat('%s_list_59.txt' % ACT, '**THE LIST COMPLETE TO ')
    keys['LIST'] = ('CERTIFIED -- THE LIST AT -59 BY THE CERTIFIED ENGINE: complete to %s in %d of %d bands, %d on-line zeros, %d off-line pairs, the largest real part %s; its controls AS WANTED, run after the roots` commit; the engine at relay %s, the list at %s. SOURCE %s.' % (
        f['ls_height'], f['ls_complete'], f['ls_bands'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_ENGINE[:8], K.C4_LIST[:8], sl['text']))
    seats.append(sl)
    # ------------------------------------------------------------------ CERTIFIED: (R365)(4), the candidates reproduced (the name the template appends)
    sw = seat('%s_candidates.txt' % ACT, '**THE CANDIDATES: REPRODUCED ')
    keys['CANDIDATES'] = ('CERTIFIED -- THE CANDIDATES REPRODUCED: %d (%s), each by the seat`s generator from the statement alone, committed before its run; %d plants, each failing as wanted; the bank at relay %s. SOURCE %s.' % (
        f['cd_rep'], f['cd_labels'], f['cd_plants'], K.C3_CANDIDATES[:8], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ HELD: (R365)(6), the census, exploratory and marked so
    se = seat('%s_census_from_primes.txt' % ACT, '**(6), EXPLORATORY: ')
    keys['CENSUS'] = ('HELD -- (6), EXPLORATORY AND MARKED SO, deciding nothing: at -23 to height %s, %d roots of real part at least 0.85 at P = 3 x 10^5; the least height of a root with real part above 1: %s; the control to %d %s, printed after the figures (relay data/b755_defects.txt (l)); the generator at relay %s. SOURCE %s.' % (
        f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], se['text']))
    seats.append(se)
    # ------------------------------------------------------------------ HELD: (R365)(7), [L16], pattern grade, promoting nothing
    s7 = seat('%s_l16.json' % ACT, '"confirm"')
    keys['L16'] = ('HELD -- THE LINE OF (7), [L16], pattern grade, promoting nothing: appended under a dated head at OPEN_TRAILS :%s and :%s, %s. SOURCE %s.' % (
        f['l16_lines'][0][1], f['l16_lines'][1][1], f['l16_confirm'], s7['text']))
    seats.append(s7)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R365)(9))
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1346', 'LIST', 'CANDIDATES']), ('REGISTERED', ['WALK', 'LITERATURE', 'ZEROS', 'RECUR']), ('HELD', ['CENSUS', 'L16', 'HELD'])]
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
