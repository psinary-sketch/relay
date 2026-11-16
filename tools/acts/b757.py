# -*- coding: utf-8 -*-
# b757 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R367)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R367)(2) repair it carries. Edited by the Edit tool. Carried at b757 by tools/b757_fold.py (`carry`) from tools/acts/b756.py,
# b756`s names substituted; the citation`s sections adopted from tools/b757_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b756`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b756`s carried till
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
# ### b757, Component 1: THE c1 ROUTE FOR b756'S WEIGHT LINE AND ITS SHORT CORRIGENDUM, (R367)(1), written by the Edit tool against b756's
# ### banks (37 events, 11 defects, 9 refusals; no post-seal events bank at b756 by (R366)(1)(ii)), the seven findings the seat printed after
# ### b756's lock entered as this act's events from the author's relay of that message (data/b757_events.txt (7)-(13)), and the navigator's
# ### correction to (F6); short, as (1) orders: the counts from the banks, the one CLAIM item in full, the seven findings, the correction. The
# ### line of (1) for OPEN_TRAILS is composed here (`c1 next`, which prints only) and lands in (9)'s one dated block. The carried stub
# ### (tools/standing/carry.py v1.34.0) removed by the Edit tool; nothing composed by it. The weight line is the head line and one sentence.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_PREV_CLOSE = '38024feb'          # ### b756's closing step-row commit, the public relay's main at step zero ((R367)(1))
C1_HEAD_RELAY = '778050cd'          # ### the relay commit b756's closing head names (its record step rows)
C1_CLOSING_COMMIT = '59507f62'      # ### b756's closing commit (its closing row, data/b756_steps.json)
C1_PP_RECORD = 'b6860142'           # ### b756's PLACE-papers record commit (its pp record row)
C1_NOTED = '2026-11-16'
C1_CORRIGENDA_LAST = 76
C1_WEIGHT_HEAD = '*Appended 2026-11-16 by b757 to b756’s entry (:%d), under `(R367)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## The clearing act under (R366): the results of b755 written into the documents they bear on'
C1_TRAIL_NEEDLE = '### b756 — lane two, act one hundred and eighty-three, the clearing act under (R366)'
C1_NEXT_LINE = 18487                # ### OPEN_TRAILS: b756's trail Next line, the build as b757 (v1.34.7's line from the answers bank)
C1_NEXT_NEEDLE = '**Next:** ((R366)(7)) the build as b757'
C1_ANSWER = (27, 'Build as b757')   # ### data/b756_author_answers.txt :27, the root prompt's RESULT (transcript line 86704, 01:19:42Z)
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b756_events.txt'), ('defects', 'b756_defects.txt'))
C1_FINDINGS_BANK = 'b757_events.txt'
C1_FINDINGS_IDS = ('7', '8', '9', '10', '11', '12', '13')   # ### (F1)-(F7) of (R367)(1), in its order (the message's lines 10-19)
C1_CLAIM_ID = ('events', '10')      # ### b756's one CLAIM item (data/b756_events.txt :64)
C1_CORR_TITLE = ('## Corrigendum to b756’s record, short (relay data/b756_events.txt rows (1)-(37) and data/b756_defects.txt (a)-(k)): its events and '
                 'defects by count from their banks, its one CLAIM item in full, and the seven findings the seat printed after the lock, entered as '
                 'events, with the navigator’s correction to the sixth')
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
    """a finding's head: its words before "(the message's line"."""
    m = re.match(r"^(.*?) \(the message's lines? [\d-]+\)", text)
    return m.group(1) if m else text[:120]


def _c1_weight():
    head = _c1_rd('b756_closing.txt').split(NL)[0]
    pub = _c1_git('show', '%s:data/b756_closing.txt' % C1_PREV_CLOSE).stdout.replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b756_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    on_main = _c1_git('merge-base', '--is-ancestor', C1_PREV_CLOSE, 'origin/main').returncode == 0
    steps = json.load(open(os.path.join(D, 'b756_steps.json'), encoding='utf-8')).get('rows') or []
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    prec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'pp']
    two = [c_[:8] for c_ in _c1_git('rev-list', '%s..%s' % (C1_HEAD_RELAY, C1_PREV_CLOSE)).stdout.split()]
    if not on_main or C1_CLOSING_COMMIT not in clo or C1_PP_RECORD not in prec or two != [C1_PREV_CLOSE, C1_CLOSING_COMMIT] or 'relay %s,' % C1_HEAD_RELAY not in head:
        sys.exit('### %s on the pushed main %s ; closing %s ; pp record %s ; the commits after %s %s -- NOTHING COMPOSED' % (C1_PREV_CLOSE, on_main, clo, prec, C1_HEAD_RELAY, two))
    return (C1_WEIGHT_HEAD + ' -- b756 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b756_closing.txt):* “%s” (data/b756_closing.txt :1, the public relay '
            'at %s). The relay’s main stands at %s, two closing commits after the head’s %s (the closing %s and its step rows %s), and PLACE-papers at its '
            'record %s.') % (head, C1_PREV_CLOSE, C1_PREV_CLOSE, C1_HEAD_RELAY, C1_CLOSING_COMMIT, C1_PREV_CLOSE, C1_PP_RECORD[:7])


def _c1_trail():
    """(R367)(1): the line for OPEN_TRAILS giving b756's root answer, the build as b757, read from the answers bank's line; it lands in (9)'s one
    dated block, not here."""
    _g, ln = _c1_fl('b756_author_answers.txt', r'^RESULT \(transcript line 86704, 2026-11-16T01:19:42\.171Z\): .*"="(%s)"\. ' % re.escape(C1_ANSWER[1]), 'the root answer')
    if ln != C1_ANSWER[0]:
        sys.exit('### THE ROOT ANSWER AT :%d, NOT :%d -- NOTHING COMPOSED' % (ln, C1_ANSWER[0]))
    ot = _c1_rd(R.OT).split(NL)          # ### an absolute path: os.path.join keeps it whole
    if not (len(ot) >= C1_NEXT_LINE and ot[C1_NEXT_LINE - 1].startswith(C1_NEXT_NEEDLE) and ot[K.B711_TRAIL - 1].startswith(C1_TRAIL_NEEDLE)):
        sys.exit('### OPEN_TRAILS :%d OR :%d IS NOT b756`S TRAIL AS READ -- NOTHING COMPOSED' % (K.B711_TRAIL, C1_NEXT_LINE))
    return ('b756’s one question at the root was answered “%s” (relay data/b756_author_answers.txt :%d, 2026-11-16T01:19:42Z): the act after b756 is '
            'b757, the build, as b756’s trail reads it (:%d).') % (C1_ANSWER[1], C1_ANSWER[0], C1_NEXT_LINE)


def _c1_state():
    s = dict((k_, _c1_rows(n_)) for k_, n_ in C1_BANKS)
    ev, df = s['events'], s['defects']
    tot = _c1_tally(ev + df)
    cnt, l_cn = _c1_fl('b756_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    rf = [l for l in _c1_rd('b756_hook_refusals.txt').split(NL) if l.strip()]
    kinds = {}
    for l in rf:
        m = re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \| ([A-Z]+) \| ', l)
        kinds[m.group(1) if m else '?'] = kinds.get(m.group(1) if m else '?', 0) + 1
    cr_ = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    own = dict((r[0], r) for r in _c1_rows(C1_FINDINGS_BANK))
    fnd = [own.get(i_) for i_ in C1_FINDINGS_IDS]
    claims = [(k_, r) for k_, _n in C1_BANKS for r in s[k_] if r[2] == 'CLAIM']
    chk = _c1_rd('b756_checks.txt').split(NL)
    tpl = _c1_rd(os.path.join('tools', 'standing', 'fold', 'closing.tpl'), base=ROOT).split(NL)
    bad = [k_ for k_, ok_ in (
        ('the event rows (1)-(37)', [int(r[0]) for r in ev] == list(range(1, 38))),
        ('no post-seal events bank at b756', not os.path.exists(os.path.join(D, 'b756_events_postseal.txt'))),
        ('the defect rows 11, the last (k)', len(df) == 11 and df[-1][0] == 'k'),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev)) == tuple(int(x) for x in cnt)),
        ('the one CLAIM item events (10)', [(k_, r[0]) for k_, r in claims] == [C1_CLAIM_ID]),
        ('the refusals 9, each by its kind', len(rf) == 9 and '?' not in kinds),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the seven findings, each from the message`s line', all(fnd) and all("(the message's line" in r[4] for r in fnd)),
        ('(F6)`s correction: G-RUNNER-GATE vacuous at data/b756_checks.txt :18', len(chk) > 17 and 'VACUOUS' in chk[17] and "['G-RUNNER-GATE']" in chk[17]),
        ('(F6)`s correction: ARM_LIVE at closing.tpl :353, PASS or FAIL in three columns', len(tpl) > 352 and tpl[352].startswith('ARM_LIVE = ') and tpl[352].count('(PASS|FAIL)') == 3),
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
    L = ['*b756’s events bank (relay data/b756_events.txt) carries %d rows, (1)-(37): CLAIM %d, CLOSE %d, REPEAT %d; its defects bank (relay '
         'data/b756_defects.txt) %d lettered rows, (a)-(k): CLAIM %d, CLOSE %d, REPEAT %d. Together CLAIM %d, CLOSE %d, REPEAT %d of %d, as b756’s closing '
         'counter prints it (relay data/b756_closing.txt :%d). Its refusals bank %d lines (relay data/b756_hook_refusals.txt), by kind %s, the ninth '
         'committed at b757’s step zero (relay 72292507). No post-seal events bank at b756, by `(R366)`(1)(ii). Each item is tagged in its own bracket; the '
         'tags are the banks’ own and this entry edits none of them.*' % (
             pe['total'], pe['claim'], pe['close'], pe['repeat'], pd['total'], pd['claim'], pd['close'], pd['repeat'],
             t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds), '']
    L += ['**The CLAIM item, in full:**', '']
    for k_, (i_, o_, tg_, col_, tx_) in s['claims']:
        L += ['**(%s)** %s (relay data/%s, row (%s); %s; %s; %s).' % (i_, _c1_q(tx_).replace("'", '’'), dict(C1_BANKS)[k_], i_, _c1_owner(o_), tg_, _c1_col(col_)), '']
    L += ['**The seven findings the seat printed after b756’s lock**, entered as events of b757 from the author’s relay of that message in `(R367)`(1) '
          '(the message at transcript line 87851, 2026-11-16T03:20:05Z; relay data/b757_events.txt rows (7)-(13), for (F1)-(F7)): CLAIM %d, CLOSE %d, '
          'REPEAT %d of %d. %s.' % (
              ft['claim'], ft['close'], ft['repeat'], ft['total'],
              '; '.join('(%s) %s [%s ; %s]' % (r[0], _c1_q(_c1_head(r[4])).replace("'", '’'), r[2], _c1_col(r[3])) for r in s['findings'])), '']
    L += ['**The CLAIM item among them, in full:**', '']
    for i_, o_, tg_, col_, tx_ in [r for r in s['findings'] if r[2] == 'CLAIM']:
        L += ['**(%s)** %s (relay data/%s, row (%s); %s; %s; %s).' % (i_, _c1_q(tx_).replace("'", '’'), C1_FINDINGS_BANK, i_, _c1_owner(o_), tg_, _c1_col(col_)), '']
    L += ['**The correction to (F6), the navigator’s read in `(R367)`(1):** the arm that separates 115 from 116 is G-RUNNER-GATE, vacuous and counted '
          'neither way (relay data/b756_checks.txt :18); the pattern at tools/standing/fold/closing.tpl :353 keeps a row marked PASS or FAIL in all three '
          'columns and drops that one; the two untagged arms are listed apart and are counted. The message’s reading, that the two untagged arms account '
          'for the difference, stands corrected.', '',
          '**The repairs:** (F5), (F6) and (F7) are repaired at b757 under `(R367)`(8)(i) to (iii); the line giving b756’s root answer, the build as b757, '
          'is appended to OPEN_TRAILS with the writes of `(R367)`(9).', '',
          '*Filed at b757 on the author’s ruling `(R367)`(1): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b757.py) from b756’s events, defects and refusals banks read unedited and b757’s events rows (7)-(13); banked '
          'as relay `data/b757_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b756’s record; no sealed '
          'tool, face, trail or root-named bank of b756 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    ft = _c1_tally(s['findings'])
    return (['b757 -- THE CORRIGENDUM FOR b756, SHORT, (R367)(1) (%s)' % utc(), '',
             '### the banks read unedited: data/b756_events.txt rows (1)-(37), data/b756_defects.txt %d rows, data/b756_hook_refusals.txt %d lines; no '
             'post-seal events bank at b756; data/%s rows (7)-(13) (the seven findings); data/b756_checks.txt :18 and tools/standing/fold/closing.tpl :353 '
             '(the correction to (F6)); the corrigenda bank`s last row (%d).' % (len(s['defects']), s['refusals'], C1_FINDINGS_BANK, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEMS IN FULL %d ; THE SEVEN FINDINGS %d: CLAIM %d, '
               'CLOSE %d, REPEAT %d ; THE CORRECTION TO (F6) ENTERED ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['defects']), t['claim'], t['close'], t['repeat'], t['claim'], ft['total'], ft['claim'],
                   ft['close'], ft['repeat'], ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b756 at its weight after its entry and the short corrigendum for b756, each landed through b698's
    guarded landing; `c1 next` prints (R367)(1)'s line for OPEN_TRAILS, which lands in (9)'s one dated block; dry prints and writes nothing."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        text = _c1_weight()
        land([('FINDINGS.md', C1_WEIGHT_HEAD, NL + text + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B711_ENTRY,
             check=[('FINDINGS.md', K.B711_ENTRY, C1_ENTRY_NEEDLE), ('OPEN_TRAILS.md', K.B711_TRAIL, C1_TRAIL_NEEDLE)], dry=dry)
        return
    if route == 'next':
        if not dry:
            sys.exit('### (R367)(9): THE LINE OF (1) LANDS IN (9)`S ONE DATED BLOCK -- `c1 next` PRINTS ONLY, NOTHING WRITTEN')
        print(_c1_trail())
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
        ft = _c1_tally(s['findings'])
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=t['claim'], close=t['close'], repeat=t['repeat'], items=t['total'],
                                                   by_bank=dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS),
                                                   claims=[dict(bank=dict(C1_BANKS)[k_], id=r[0], owner=r[1], column=r[3]) for k_, r in s['claims']],
                                                   findings=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_FINDINGS_IDS), claim=ft['claim'],
                                                                 close=ft['close'], repeat=ft['repeat'],
                                                                 claims=[dict(id=r[0], owner=r[1], column=r[3]) for r in s['findings'] if r[2] == 'CLAIM']),
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   correction=dict(f6='G-RUNNER-GATE', checks='data/b756_checks.txt :18', pattern='tools/standing/fold/closing.tpl :353'),
                                                   repairs=dict(f5='(R367)(8)(i)', f6='(R367)(8)(ii)', f7='(R367)(8)(iii)', trail_line='OPEN_TRAILS, in (9)`s one dated block'),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEMS %d ; THE SEVEN FINDINGS CLAIM %d ; FINDINGS :%s' % (
            t['claim'], t['close'], t['total'], t['repeat'], t['claim'], ft['claim'], ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum | next  [dry | write]')
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
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b756, naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base 28255aea the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b756-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b757_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
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
        and 'data/b757_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b756, Component 6 (the Edit tool): the corrigendum's json (data/b756_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 46, CLAIM 0, CLOSE 46, REPEAT 20, the CLAIM items 0, the corrigenda row (76); the rows stand in the bank by
# ### their banks (data/b756_corrigendum.txt); the template's row range read as the json's counts
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 46 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
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
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and '| ruling (8) | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
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
                                                                          or (bool(S['report_tool']) and 'tools/acts/b756.py -> tools/acts/b757.py' in (rd('b757_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and (_ for _ in ()).throw(SystemExit('### b757`s a probe`s needle (OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED'))   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 1 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    raise SystemExit('### b757`s a probe`s needle (OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 8 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b757')
    return '### THE COUNTER ((R367) Component 5, the act`s events and defects together; relay data/b757_defects.txt, data/b757_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act ((R367)(9)); W-ORD-MECHANISM-ATTRIBUTION open, its plan passed at b752`s [P1] (relay data/b752_attribution_plan.txt), its build T0 then T1 one of the two acts the root`s question offers as b757;',
    '        W-ORD-LI-ARITH, W-ORD-ZQ-FAMILY, W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    raise SystemExit('### b757`s a probe`s needle (OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 1 code lines, stands in the carry`s diff bank
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b757_author_answers.txt', 'b757_answer_check.txt', 'b757_events.txt'))   # noqa: E731,E702
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
REG = os.path.join(ROOT, 'data', 'b757_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b757_registration_%s.txt' % __import__('b757_worklist').DATE)   # ### the gate imports no worklist of its own
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
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b757_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): G-SCORER-READS-BANKS's needles set to the banks b755's N1-N4 read (the command bank and the
# ### dispatch rows, N2's controls and first adds, the walk among the figure banks, the seal and step banks), the carried stub's refusal
# ### removed; the ledger exclusion unchanged. The arm stands in tools/standing/arms.py's RETIRED and is not in the run list; read so, its
# ### template line :971 would fire on N3's label of the landed entry (record.tpl :2444, a string naming FINDINGS.md), not edited here
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    raise SystemExit('### b757`s a probe`s needle (OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)) IS A CARRIED STUB (tools/standing/carry.py v1.34.0), ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED: written for the act before use -- NOTHING COMPOSED')
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abefg'))   # ### b756: the seat's rows of data/b756_defects.txt as the template's reader takes them (THE SEAT'S: (a), (b), (e), (f), (g)); (c) THE TOOLS' and (d) THE TOOL'S fall outside its three actors and are read by the counter, not by this floor; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b757_corrigendum.txt', 'data/b757_rules.txt', 'data/b757_standing_v1347.txt', 'data/b757_standing_v1348.txt', 'data/b757_standing_v1349.txt',
                  'data/b757_standing_v1350.txt', 'data/b757_standing_v1351.txt', 'data/b757_standing_v1352.txt', 'data/b757_standing_v1353.txt',
                  'data/b757_constellation_summary.txt', 'data/b757_constellation_control.txt', 'data/b757_reverse_read.txt', 'data/b757_beyond_three.txt',
                  'data/b757_notes.json', 'data/b757_orders_read.txt', 'data/b757_instruments_draft.txt', 'data/b757_put_1.json', 'data/b757_passed.json',
                  'data/b757_orders_moves.txt', 'data/b757_ceiling_c4.txt', 'data/b757_faults.txt', 'data/b757_faults_placed.txt', 'data/b757_doors.txt',
                  'data/b757_amendments.json', 'data/b757_author_answers.txt', 'data/b757_pathrefusal.txt',
                  'data/b757_address_scan.txt', 'data/b757_touch.txt',   # ### b756, Component 6: the act's banks by its components, in place of b755's carried names; no reproduce bank: the run computes at fields (I-96 to I-106, I-108), which (R366)(8) bars, and is not run (events (29))
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b757_address_scan.py'), 'scan'], capture_output=True, text=True,
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
    """(R366)(1)-(7): the act's relay commits after step zero in their order, (key, commit) -- v9, then the worklist's CHAIN (v1.34.7, the lock
    gate carried, the corrigendum banks, the map's four tool commits and its banks, the notes' tool and bank, the orders' tool and bank, the put,
    the passed writes' tool, v1.34.8, the status lines' tool and bank, the ceiling, v1.34.9 to v1.35.3 with the fault count, the placing and
    the README route among them), the passed bank and the handoff page where each is made; read from the worklist at the call."""
    c = [('v9', K.STANDING_COMMIT)] + list(K.CHAIN)
    c += [(k_, h_) for k_, h_ in (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT)) if h_]
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
        # ### the three tools of (6) committed with their banks ((R366)(6) orders no commit before a run): the tool's first add, the commit's files
        gens_wb=dict((n_, dict(tool=t_, data=d_, bank=rd(d_.split('/', 1)[1]), blob=_s(blob(ROOT, '%s:%s' % (c_, d_))), full=gs(ROOT, 'rev-parse', c_).strip(),
                               first=([h_ for h_ in gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', t_).split() if h_.strip()][-1:] or [None])[0],
                               files=files_of(ROOT, c_))) for n_, t_, d_, c_ in K.GENS_WITH_BANK),
        # ### the map ((R366)(4)): the rerun's summary and controls, the reverse read and what the two find beyond (3)
        csum=rd('b757_constellation_summary.txt'), cctl=rd('b757_constellation_control.txt'), rev=rd('b757_reverse_read.txt'), beyond=rd('b757_beyond_three.txt'),
        # ### the notes of (3), the orders read and the drafts, the put and its answers, the passed writes, the status lines, the ceiling after
        # ### Component 4 ((R366)(3), (5), (7)); the fault count, its placing and the README route ((R366)(6))
        notesj=jl('b757_notes.json'), orders=rd('b757_orders_read.txt'), instr=rd('b757_instruments_draft.txt'),
        putj=jl('b757_put_1.json'), zanswers=rd('b757_author_answers.txt'), passedj=jl('b757_passed.json'), moves=rd('b757_orders_moves.txt'),
        ceiling=(rd('b757_ceiling_c4.txt'), _s(blob(ROOT, '%s:data/b757_ceiling_c4.txt' % dict(K.CHAIN)['ceiling']))),
        faults=rd('b757_faults.txt'), placed=rd('b757_faults_placed.txt'), doors=rd('b757_doors.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        pp_files=dict((k_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        numstat=dict((k_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
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
        drows=json.loads(rd('b757_dispatch_rows.json') or '[]'), reproduce=rd('b757_reproduce.txt'), reproducej=jl('b757_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b757_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b757_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [(k_, _ct(PP, h_)) for k_, h_ in K.PP_CHAIN]
               + [('c1', _ct(ROOT, K.C1_RELAY)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)), ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), lockgate=files_of(ROOT, K.C1_LOCKGATE), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), handoff=files_of(ROOT, K.HANDOFF_COMMIT) if K.HANDOFF_COMMIT else [],
                   **dict([('rc_' + k_, files_of(ROOT, h_)) for k_, h_ in K.CHAIN] + [('pp_' + k_, files_of(PP, h_)) for k_, h_ in K.PP_CHAIN]),   # ### b756: each commit of the two chains by its key
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b755's read-first bank's items by path, the ferry's read-first list in its order (data/b755_readfirst_rows.json); b755 step zero: the
# ### carried stub replaced, one needle for each item of the ferry's list (:44) and for the act's own reads beside it
# ### b756 step zero: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b756_ferry.txt :46), in its order
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): statement READFIRST_NEEDLES; it carried an act ordinal or the read-first needles
READFIRST_NEEDLES = __import__('standing.carry', fromlist=['Carried']).Carried('b757`s READFIRST_NEEDLES')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R367)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'MAP ((R367)(4))', 'NOTES OF (3) ((R367)(3))', 'ORDERS AND THE CHECKPOINTS ((R367)(5))', 'TOOL CHANGES ((R367)(6))',
 'NAME AND ADDRESS (N5)', 'RESEARCH INSTRUMENTS NOT REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', 'TOUCH READ (standing clauses v9)')   # ### b756: closing 7's sections, the ferry's components in order
#⟪END⟫
#⟪SECTION checks 12⟫
    """b757: the citation check's bank: every cite checked, OK and misses summing (80 = 80 + 0, data/b757_citation_check.txt :130), no
    miss; the check CLEAN (:132, halts 0), as the step-zero bank enters it (data/b757_stepzero.txt :56-:57, after the act_current commit
    and the subject read; the first dry run's one miss the readfirst bank not yet written, :32); the bank written before the step-zero
    banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 80 \
        and '### ### **THE CHECK CLEAN** (halts 0: Lean paths and nouns 0, comparatives 0)' in c \
        and 'THE CITATION CHECK BANKED (' in (S['stepz'] or '') and 'CITES CHECKED 80 ; OK 80 ; MISSES 0;' in (S['stepz'] or '') \
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
                    MISSES=tfirst('b757_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b755's figures, read at FINDINGS :15344 as Component 1 landed them (b755's closing head quoted, PLACE-papers d1133807)
    return landed(S, 0, ['b756 AT ITS WEIGHT', 'suite 111 of 116', '0ed5cf5ded61ecf1', '19 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b756's title by its objects, the ferry's Component 6 order (data/b756_ferry.txt :54) adjusted to what the act did (record 31's _title
# ### over the banks' feet: the notes 9 of 9, the rerun 39 and 7, the reverse read 4, the orders 1, 1, 5 and 5, the CP lines passed, the tool
# ### changes 5 landed and 1 carried)
TITLE_NEEDLES = ('## The clearing act under (R367): the results of b756 written into the documents they bear on, 9 notes of 9 (b757_notes)',
                 'the constellation map run again over 39 documents, 7 rows moved or gone (b757_constellation_summary)',
                 'and read in reverse, 4 lines beyond those written (b757_reverse_read)',
                 'the twelve ready orders placed, 1 done, 1 here, 5 with the build, 5 later (b757_orders_read)',
                 'CP-6 and CP-7 passed (b757_passed)', 'the tool changes, 5 landed and 1 carried (b757_faults_placed, b757_doors)',
                 'nothing computed, nothing built')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R367)(1): the generated corrigendum for b756's record landed, short (its line in the json, FINDINGS :15346, the title at that line
    through conv): b756's 27 events and 19 defects by count from their banks, 46 items, CLAIM 0 and CLOSE 46, REPEAT 20, the CLAIM items in
    full none; the nine findings of the seat's closing message entered as events (CLAIM 1, CLOSE 8, REPEAT 5); the two repairs -- tools/standing/
    v1.34.7 at dc8319ea by its controls bank, 16 of 16 as wanted, and the lock gate carried at 5e37bf97; the corrigenda bank appended at row (76)
    and nothing before it changed; in Component 1's commits (the figures read from data/b757_corrigendum.json and the bank's foot)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 76 and j.get('claim') == 0 == len(j.get('claims') or []) and j.get('close') == 46 and j.get('repeat') == 20 \
        and '### ### **ITEMS 46: EVENTS 27, DEFECTS 19 ; CLAIM 0, CLOSE 46 ; REPEAT 20 ; THE CLAIM ITEMS IN FULL 0 ; THE NINE FINDINGS 9: CLAIM 1, CLOSE 8, REPEAT 5 ; ' in (S['corrt'] or '') \
        and 'THE REPAIRS 2: v1.34.7 AT dc8319ea (16 OF 16 AS WANTED), THE LOCK GATE AT 5e37bf97 ; THE ENTRY AT FINDINGS :15346.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and _vlast(_txt((S['stbanks'] or {}).get('v1.34.7', ('',))[0])) == 'v1.34.7: CONTROLS (next), (n4), (version) ; CASES 16 ; AS WANTED 16 ; ALL AS WANTED.' \
        and 'data/b757_standing_v1347.txt' in S['files']['standing'] and 'tools/standing/VERSION' in S['files']['standing'] \
        and 'tools/b757_lockgate.py' in S['files']['lockgate'] \
        and '  (76) ' in S['corrigenda'] and '  (77) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R367)(2) orders this act's rules bank, data/b757_rules.txt, its rows (a) to (c) in force from
    b757 (the rule this act works by); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here rows (a) to (c), lettered as (R367)(2) letters them, in Component 1's commit (relay 0a151012) and no other, the working tree its blob at HEAD."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and re.findall(r'(?m)^  \(([a-z])\) ', rd('b757_rules.txt') or '') == ['a', 'b', 'c'] \
        and bool(r1) and _txt(r1) == _txt(blob(ROOT, 'HEAD:data/b757_rules.txt')) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', 'data/b757_rules.txt').split()] == [K.C1_RULES[:8]] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b756's report lines (report sections 2-5): each key a phrase its line opens with
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.34.7 TO v1.35.3', 'CERTIFIED -- THE CONSTELLATION RERUN BY ITS CONTROLS', 'CERTIFIED -- THE REVERSE READ BY ITS CONTROLS',
               'REGISTERED -- THE NOTES OF (3) IN THE RULING`S WORDS', 'REGISTERED -- THE TWELVE ORDERS PLACED ON THE AUTHOR`S PASS',
               'REGISTERED -- CP-6 AND CP-7 AND THE TWO INSTRUMENTS ROWS', 'HELD -- THE README ROUTE AND THE TWO DESCRIPTIONS, CARRIED WHOLE',
               'HELD -- THE REPRODUCTION RUN, NOT RUN',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b757: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b754, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b757_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
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
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: (1)(i)'s
    and (3)(v)'s dated lines, the CP lines and the trail; INSTRUMENTS: I-110 and I-111; the four documents of (3)(i) to (iv), a dated note
    each), the ledgers changed; no rename; no other paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b756's headings and banks, as its _finding_text (record 34) writes them; the last the INTEGRATION line's opening words (_integ_line)
ENTRY_NEEDLES = ('**The weight, the corrigendum and the standing change**', '**The rule this act works by**', '**The map of dependent statements**',
                 '**The notes of (3)**', '**The orders and the checkpoints**', '**The tool changes**', '**The order of the act**', '**What this act is not**',
                 '**The research instruments not reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b757_corrigendum.txt', 'data/b757_rules.txt', 'data/b757_standing_v1347.txt', 'data/b757_standing_v1348.txt', 'data/b757_standing_v1353.txt',
                 'data/b757_constellation_control.txt', 'data/b757_constellation_summary.txt', 'data/b757_reverse_read.txt', 'data/b757_beyond_three.txt',
                 'data/b757_notes.json', 'data/b757_orders_read.txt', 'data/b757_instruments_draft.txt', 'data/b757_put_1.json', 'data/b757_orders_moves.txt',
                 'data/b757_passed.json', 'data/b757_ceiling_c4.txt', 'data/b757_faults.txt', 'data/b757_faults_placed.txt', 'data/b757_doors.txt',
                 'data/b757_events.txt', 'data/b757_address_scan.txt', 'data/b757_touch.txt',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: the notes of (3): ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R367)(1), (3), (5), N5 (the name the frozen run list carries): PLACE-papers written by the worklist's PP_CHAIN in its order and by
    nothing else before the record -- the weight, the corrigendum and (1)(i)'s dated line in one commit touching FINDINGS and OPEN_TRAILS, the
    first of the act on its base; the five writes of (3) each touching its one file, the notes bank's confirm naming each; the CP lines and
    the two INSTRUMENTS rows each touching its one file, the passed writes' bank's confirm naming each; every one removing no line; the changed
    files since the base within PP_WRITTEN; by ancestry the base, each commit of the chain and HEAD; the earlier acts' registrations at HEAD
    their blobs."""
    pf_, ns_ = S['pp_files'] or {}, S['numstat'] or {}
    nj_, pj_ = (S['notesj'] or {}).get('items') or {}, (S['passedj'] or {}).get('items') or {}
    pc_ = dict(K.PP_CHAIN)
    want_ = [('c1pp', ['FINDINGS.md', 'OPEN_TRAILS.md'], None)] \
        + [('pp_' + lab_.strip('()'), [fn_], (nj_.get(lab_.strip('()')) or {}).get('confirm')) for lab_, fn_, _h in K.C3_NOTES_PP] \
        + [('pp_' + k_, [fn_], (pj_.get(k_) or {}).get('confirm')) for k_, fn_, _h in K.C4_PASSED_PP]
    rows_ = [(k_, sorted(pf_.get(k_) or []) == sorted(fs_) and bool(ns_.get(k_)) and all(x_ == '0' for x_ in (ns_.get(k_) or [])[1::3])
              and (c_ is None or (c_ or '').startswith('PLACE-papers %s ' % pc_.get(k_, '-')[:8]))) for k_, fs_, c_ in want_]
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:len(K.PP_CHAIN)]] == [h_[:8] for _k, h_ in K.PP_CHAIN]
    return len(rows_) == len(K.PP_CHAIN) == 8 and set(k_ for k_, _o in rows_) == set(pc_) and all(o_ for _k, o_ in rows_) and order_ \
        and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b757_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R367)(1), (5)(i), (6), N2, N4 (the name the frozen run list carries): the act's order by time -- the worklist's TIME_ORDER, relay and
    PLACE-papers together (the act_current commit, step zero's banks, v1.34.7, the lock gate, PLACE-papers' weight and corrigendum, the
    corrigendum banks, the map's tool commits and banks, the notes' tool, its five writes and its bank, the orders read, the put, the passed
    writes' tool and its two writes, v1.34.8, the status lines, the ceiling, v1.34.9 to v1.35.3 with the fault count, the placing and the
    README route), then the passed bank and the handoff page where made; by ancestry within the relay from v9 through each commit of _chain;
    each of the seven standing versions' banks at HEAD its blob at its commit, its foot ALL AS WANTED at the worklist's cases, VERSION and the
    bank in that commit's files; the act's commits under tools/standing/ those seven and no other."""
    t_ = S['t']
    ks_ = list(K.TIME_ORDER) + [k_ for k_, _h in S['r366_chain'] if k_ in ('passed', 'handoff') and k_ not in K.TIME_ORDER]
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
        and len(sb_) == 7 and all(sb_) and st_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R367)(3)-(7), N2, N3 (the name the frozen run list carries): each tool of K.GENS first added by a commit of its own, every one of
    its commits carrying it and not its bank, the bank's commit carrying the bank and not the tool and after every tool commit, the bank at
    HEAD its blob there (seven once the passed bank is committed); the three tools of (6) committed with their banks, each bank at HEAD its
    blob at that commit, the tool first added there; the map -- the rerun's foot reading every table and leaving no row unread after the
    hand-read, its controls all as wanted, the reverse read's controls all as wanted and its count for (4)(iii), what the two find beyond (3)
    carrying both counts; the ceiling after Component 4 at HEAD its blob at its commit, nothing carried."""
    gk_ = _gens_ok(S)
    wb_ = []
    for n_, d_ in sorted((S['gens_wb'] or {}).items()):
        wb_.append(bool(d_.get('bank')) and _txt(d_['bank']) == _txt(d_.get('blob')) and d_.get('first') == d_.get('full')
                   and d_['tool'] in (d_.get('files') or []) and d_['data'] in (d_.get('files') or []))
    cs_, cc_, rv_, bt_ = _txt(S['csum']), _txt(S['cctl']), _txt(S['rev']), _txt(S['beyond'])
    map_ = _vlast(cs_).startswith('TABLES READ: 39 OF 39.') and 'AFTER THE HAND-READ: 7 COUNTED, 5 NOT, 0 UNREAD.' in _vlast(cs_) \
        and _vlast(cc_).startswith('THE CONTROLS: 6 OF 6 AS WANTED') and 'THE REVERSE READ: CONTROLS 16 OF 16 AS WANTED ;' in rv_ \
        and _vlast(rv_).startswith('THE COUNT FOR (4)(iii) AND THE ROOT PROMPT: 4 LINE(S) BEYOND (3)') \
        and _vlast(bt_).startswith('THE TWO COUNTS FOR THE ROOT PROMPT: THE CONSTELLATION RERUN 7 ROWS MOVED OR GONE') and 'THE REVERSE READ 4 LINE(S) BEYOND (3)' in _vlast(bt_)
    ce_ = S['ceiling'] or (None, None)
    ceil_ = bool(ce_[0]) and _txt(ce_[0]) == _txt(ce_[1]) and _vlast(_txt(ce_[0])).startswith('THE CEILING AFTER COMPONENT 4: ') and ' ; NOTHING CARRIED ;' in _vlast(_txt(ce_[0]))
    return len(gk_) == len(K.GENS) >= (7 if K.PASSED_BANK else 6) and all(o_ for _n, o_ in gk_) and len(wb_) == 3 and all(wb_) and map_ and ceil_


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R367)(6), (8) (the name the frozen run list carries): no kernel's main touched and no Lean file written, read at
    SIDE-explicit-formula alone -- its main at the worklist's EF_MAIN (8fbab45d, as b757 found it), the four branches each at the worklist's
    tip locally and at origin, zq-b730 at its entering tip 1e658870 with nothing past it; no commit on any of its refs since the act opened;
    the one tag v0.38, its object the worklist's and its peel 14ca5725, the only tag at that commit and no tag added this act; no sitting
    kernel. The README route wrote no kernel (data/b757_doors.txt :14), so the worklist holds no constant of another kernel to read."""
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
    arm list since b756's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R367)(3), (5), (6), N3 (the name the frozen run list carries): the counts the entry and the root prompt carry, each read from its
    bank -- the notes bank's five items in the ruling's order, each at its file and confirmed at its PLACE-papers commit with none removed,
    the lines other than the trail's head 9, the worklist's count; the orders read's foot the worklist's four places, the drafts' foot the two
    rows; the one put of three questions, the answers' RESULT passing each as recommended; the passed bank's two items, each confirmed at its
    commit with none removed; the twelve status lines' foot; the fault count's 16 of two acts or more and the placing's foot, none unplaced;
    the README route's two descriptions refused by the server for length and read back unchanged; b746's draft unchanged; no Zenodo tool
    this act."""
    nj_, pj_ = (S['notesj'] or {}).get('items') or {}, (S['passedj'] or {}).get('items') or {}
    notes_ = list(nj_) == ['i', 'ii', 'iii', 'iv', 'v'] and all(
        (nj_.get(it_.strip('()')) or {}).get('file') == f_ and (nj_[it_.strip('()')].get('confirm') or '').startswith('PLACE-papers %s at ' % c_[:8])
        and 'none removed' in nj_[it_.strip('()')]['confirm'] for it_, f_, c_ in K.C3_NOTES_PP) \
        and sum(1 for v_ in nj_.values() for x_ in v_.get('lines') or [] if x_.get('kind') != 'head') == K.C3_NOTES_WRITTEN == 9 \
        and [x_.get('kind') for x_ in (nj_.get('v') or {}).get('lines') or []][:1] == ['head']
    om_ = re.match(r'THE TWELVE ORDERS AT TODAY`S TREE: DONE (\d+) ; HERE (\d+) ; WITH THE BUILD (\d+) ; LATER (\d+) ;', _vlast(_txt(S['orders'])))
    orders_ = bool(om_) and tuple(int(x_) for x_ in om_.groups()) == K.C4_ORDERS \
        and _vlast(_txt(S['instr'])).startswith('TWO ROWS DRAFTED, I-110 AND I-111, AFTER I-109 ;') \
        and _vlast(_txt(S['moves'])).startswith('TWELVE STATUS LINES: DISCHARGED 2 (DONE 1, HERE 1) ; CARRIED 10 (WITH THE BUILD 5, LATER 5) ;')
    rl_ = [l_ for l_ in _txt(S['zanswers']).split(NL) if l_.startswith('RESULT (')]
    put_ = len((S['putj'] or {}).get('questions') or []) == 3 and len(rl_) == 1 and len(re.findall(r'="[^"]*\(Recommended\)"', rl_[0])) == 3
    passed_ = list(pj_) == ['cp', 'instruments'] and all(
        (pj_.get(it_) or {}).get('file') == f_ and (pj_[it_].get('confirm') or '').startswith('PLACE-papers %s at ' % c_[:8])
        and 'none removed' in pj_[it_]['confirm'] for it_, f_, c_ in K.C4_PASSED_PP) and K.C4_CP == 'passed'
    faults_ = 'IN TWO ACTS OR MORE 16 ' in _vlast(_txt(S['faults'])) \
        and _vlast(_txt(S['placed'])).startswith('THE FAULTS OF TWO ACTS OR MORE: 16 ; LANDED 11 (v1.35.1 and v1.35.2) ; CARRIED 1 ; NO CODE 4 ; UNPLACED 0 ;')
    doors_ = _vlast(_txt(S['doors'])).startswith('THE DESCRIPTIONS: WRITTEN AS RULED AND READ BACK EQUAL 0 of 2 ; REFUSED BY THE SERVER FOR LENGTH, EACH READ BACK UNCHANGED, 2 ')
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b757_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return notes_ and orders_ and put_ and passed_ and faults_ and doors_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b757_steps.json', 'data/b757_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order, the tool's own list at the act's base b19867ac (I-109, entered at
    b753, and I-110 and I-111, entered at this act on the author's pass, stand in no row of it, and this act changes no research tool). Not
    run at b756: the run computes at a field where (R366)(8) bars it; the arm fails and is declared so on the face (data/b756_events.txt
    (29)). Each row REPRODUCES,
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
    """standing clauses v9 (Component 6 of (R367): the close "as the standing clauses order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b757_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b756's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R367-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b756's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R367) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b756's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base b19867ac; not run at b757 under (R367)(8), declared failing on the face (events (29))',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 80 = 80 OK + 0 misses, the check CLEAN (halts 0) as the step-zero bank enters it after the act_current commit and the subject read; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b756-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b757: the tip removed from "(was b19867ac, 12:56:12Z)" and the four after it (data/b757_stepzero.txt :66-:67); the carried plant wanted the tip closed by its paren and mutated nothing (the probe's VAC)
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 6 order adjusted to what the act did: the clearing act under (R367); the notes of (3) 9 of 9; the constellation map run again over 39 documents, 7 rows moved or gone; the reverse read 4 lines beyond those written; the twelve orders placed, 1 done, 1 here, 5 with the build, 5 later; CP-6 and CP-7 passed; the tool changes 5 landed and 1 carried; nothing computed, nothing built; each object`s bank in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R367)(1): the generated corrigendum for b756`s record, short, landed at FINDINGS :15346: b756`s 27 events and 19 defects by count from their banks, 46 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 0 CLOSE 46, REPEAT 20, the CLAIM items in full none; the nine findings of the seat`s closing message entered as events; its two repairs -- v1.34.7 at dc8319ea by data/b757_standing_v1347.txt, 16 of 16 as wanted, and the lock gate carried at 5e37bf97; the corrigenda bank appended at row (76)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R367)(2), data/b757_rules.txt`s rows (a) to (c), in force from b757, in Component 1`s commit (0a151012) and no other, the working tree its blob at HEAD',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b757's objects
    ('G-REGISTRATIONS-FIRST', '(R367)(1), (3), (5), N5: PLACE-papers written by the worklist`s chain in its order and by nothing else before the record -- the weight line, the corrigendum and (1)(i)`s dated line in one commit touching FINDINGS and OPEN_TRAILS (d1133807), the act`s first on its base; the five writes of (3) each touching its one file (ed23042f, a680411c, 1795559c, 2cab7417, 6fb72eba), the notes bank`s confirm naming each; the CP lines (e50a394b) and the two INSTRUMENTS rows (3b45826d), the passed bank`s confirm naming each; none removing a line; the changed files within the act`s list; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('REGISTRY.md'))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b757_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R367)(1), (5)(i), (6), N2, N4: the act`s order by time across the relay and PLACE-papers -- the act_current commit and step zero`s banks, v1.34.7, the lock gate, the weight and corrigendum, the map`s tools before their banks, the notes` tool before its five writes and its bank, the orders read, the put, the passed writes, v1.34.8, the status lines, the ceiling, v1.34.9 to v1.35.3 with the fault count, the placing and the README route, then the passed bank and the handoff page -- and by ancestry within the relay; each of the seven standing versions` banks ALL AS WANTED at its cases in its own commit with VERSION moved; the act`s commits under tools/standing/ those seven alone',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update({next(iter(d), 'none'): False}))),   # ### b757: the first pair of the chain's ancestry set False (b756's planted key stood in no state of b757's)
    ('G-DERIVATION-GRADED', '(R367)(3)-(7), N2, N3: each tool of the worklist`s list first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; the three tools of (6) committed with their banks; the rerun reading 39 tables of 39 and, after the hand-read, 7 counted, 5 not, 0 unread, its controls 6 of 6; the reverse read`s controls 16 of 16 and 4 lines beyond (3); what the two find beyond (3) carrying both counts; the ceiling after Component 4 at HEAD its blob, nothing carried',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'ceiling', ((S['ceiling'] or (None, None))[0], 'planted'))),
    ('G-OFFSET-POST-HOC', 'N5, (R367)(6), (8): no kernel`s main touched and no Lean file written, read at SIDE-explicit-formula -- its main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it; the README route wrote no kernel',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R367)(3), (5), (6), N3: the counts read from their banks -- the notes` five items in the ruling`s order, each at its file and confirmed at its commit with none removed, 9 lines of 9; the orders read 1 done, 1 here, 5 with the build, 5 later, the drafts I-110 and I-111; the one put of three questions, each passed as recommended; the passed bank`s two items, each confirmed with none removed; the twelve status lines; the faults of two acts or more 16, landed 11, carried 1, no code 4, unplaced 0; the two descriptions refused for length and read back unchanged; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'notesj', lambda d: (d.get('items') or {}).pop('v', None))),   # ### b757: the trail's five lines dropped from the notes bank
    ('G-DIFFERS-ERRATA', '(R367)(1), (8): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line, the corrigendum and (1)(i)`s dated line in d1133807, FINDINGS and OPEN_TRAILS the two files there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b757_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R367-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal to its blob at the act`s base b19867ac (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b756 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b757 found it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: (1)(i)`s and (3)(v)`s dated lines, the CP lines and the trail; INSTRUMENTS: I-110 and I-111; the four documents of (3)(i) to (iv), a dated note each; (R367)(1), (3), (5), (7)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    (_ for _ in ()).throw(SystemExit('### b757`s a block reading an act ordinal or the read-first needles (SECTION checks 60) IS A CARRIED STUB (tools/standing/carry.py v1.34.0), ITS CODE KEPT BEHIND THIS REFUSAL, UNREACHED: written for the act before use -- NOTHING COMPOSED')),
    ('G-PRIOR-CLOSED-PUSHED', 'b756`s trail record on OPEN_TRAILS (:18350) and its root in the chain', lambda S: '### b756 — lane two, act one hundred and eighty-two, the class-number-3 walk under (R366)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS, INSTRUMENTS, the four documents of (3)): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b757, (R367)(1)(i): Component 1's PLACE-papers commit carries (1)(i)'s dated line in OPEN_TRAILS beside the weight line and the
# ### corrigendum in FINDINGS (d1133807), so its files are the two ledgers and not FINDINGS alone
#⟪OVERRIDE checks MARK e92df47c9946 1⟫
        and K.DIFFERS_LINE is None and K.ERRATA_LINE is None and K.ERRATA_ID is None and S['files']['c1pp'] == ['FINDINGS.md', 'OPEN_TRAILS.md'] \
#⟪END⟫
# ### (carried; b757 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b756's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b757: (R367)'s rows, written at step zero in place of b756's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch facts757.py, scope757.py, counts757.py, closemsg757.py,
    # ### keiper757.py, overlap757.py, mergesim757.py, b1757.py); (1)'s line read from the public relay at 38024feb. A place is named by its role
    # ### or its file name, never by a folder of the host (N5); no PLACE-papers line these rows cite stands under [Q]'s row (3) (the masking
    # ### reader read each: protected 0 of them); the lines of data/b703_epstein_merge_push_out.txt that name the remote are read by no row.
    import hashlib as _h
    import itertools as _it
    import math as _m
    EF_ = 'D:/SIDE-explicit-formula'
    MOD_ = 'D:/SIDE-dirichlet-mod-24'
    HEAD1_ = 'b756 closed: relay 778050cd, PLACE-papers b686014; suite 110 of 116; root 48bf6d77facceaf4…; 4 prompts answered; scores 8 of 8 HELD; 11 defects'
    pub = _blob('D:/relay', '38024feb', 'data/b756_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1), SCOPE', 'data/b756_closing.txt :1, the head line as the ruling quotes it and as the public relay carries it at 38024feb', at(cl, 1) == HEAD1_ and ('"%s"' % HEAD1_) in text and bool(pub) and pub[0] == HEAD1_,
        'remote main %s' % rm[:8], '1')
    n2_ = gr('D:/relay', 'rev-list', '--count', '778050cd..38024feb')
    add('ruling (1), SCOPE', 'relay remote main read back at 38024feb, two closing commits past 778050cd', rm.startswith('38024feb') and n2_ == '2', '%s ; %s commits past 778050cd' % (rm[:8], n2_), '1')
    npp_, tpp_ = gr(PP, 'rev-list', '--count', K.PRE_PP), gr(PP, 'tag', '--list').split()
    add('ruling SCOPE', 'relay main and PLACE-papers main at the act`s start, 38024feb and b6860142; PLACE-papers 2,167 commits and 2 tags at b6860142',
        gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('38024feb') and gr(PP, 'rev-parse', K.PRE_PP).startswith('b6860142') and npp_ == '2167' and len(tpp_) == 2,
        '%s ; %s ; %s commits ; %d tags' % (K.PRE_RELAY[:8], K.PRE_PP[:8], npp_, len(tpp_)), '0')
    aa_ = lines_of(p('data', 'b756_author_answers.txt'))
    add('ruling (1), ferry (read first)', 'data/b756_author_answers.txt :25 and :27, the root`s answer: the build as b757 (transcript line 86704)',
        at(aa_, 25).startswith('  OPTION 1: Build as b757 ::') and at(aa_, 27).startswith('RESULT (transcript line 86704, 2026-11-16T01:19:42') and '="Build as b757"' in at(aa_, 27), at(aa_, 27)[:40], '1')
    rl5_ = [k_ + 1 for k_, l_ in enumerate(aa_) if l_.startswith('RESULT (')]
    ac6_ = lines_of(p('tools', 'acts', 'b756.py'))
    add('ruling (1)(F5), (8)(i)', 'tools/acts/b756.py :946-:947, the check that wants one RESULT line; data/b756_author_answers.txt`s two RESULT lines at :18 and :27, the root`s section appended at :20',
        "if l_.startswith('RESULT (')]" in at(ac6_, 946) and 'len(rl_) == 1' in at(ac6_, 947) and rl5_ == [18, 27] and at(aa_, 20).startswith('## APPENDED BY `record answers` AT 2026-11-16T01:20:40Z'),
        'RESULT lines at %s' % rl5_, '6')

    def _tr(n_):
        try:
            with open(C.SESSION, encoding='utf-8', errors='replace') as fh_:
                return json.loads(next(_it.islice(fh_, n_ - 1, n_)))
        except Exception:
            return {}
    for n_, t_, w_ in ((86237, '2026-11-16T00:26:00', '(F1)'), (87108, '2026-11-16T02:21:32', '(F4)')):
        b_ = _tr(n_)
        add('ruling (1)%s' % w_, 'transcript line %d of the act`s session, a summary of context at %sZ' % (n_, t_), b_.get('type') == 'system' and b_.get('subtype') == 'compact_boundary'
            and str(b_.get('timestamp', '')).startswith(t_) and b_.get('parentUuid') is None and bool(b_.get('logicalParentUuid')), '%s %s' % (b_.get('subtype'), str(b_.get('timestamp'))[:19]), '1')
    cm_ = _tr(87851)
    ct_ = ''.join(c_.get('text', '') for c_ in ((cm_.get('message') or {}).get('content') or []) if isinstance(c_, dict) and c_.get('type') == 'text')
    add('ruling (1)', 'the seat`s closing message for b756, transcript line 87851 of the act`s session (2026-11-16T03:20:05Z), the seven findings` source',
        cm_.get('type') == 'assistant' and str(cm_.get('timestamp', '')).startswith('2026-11-16T03:20:05') and 'Findings after the lock, for b757' in ct_ and all(('\n%d. ' % k_) in ct_ for k_ in range(1, 8)),
        '%d characters' % len(ct_), '1')
    rf_ = lines_of(p('data', 'b756_hook_refusals.txt'))
    add('ruling (1)(F2), (2)', 'data/b756_hook_refusals.txt :9, a PIPE refusal at 00:36:22Z, the row b756 left uncommitted', at(rf_, 9).startswith('2026-11-16T00:36:22Z | PIPE | Bash |'), '%d rows' % len([l_ for l_ in rf_ if l_.strip()]), '1')
    add('ruling (1)(F3)', 'data/b756_root_banks_parts.json, root part 1`s 831.3 s, past the 600 s limit', '"seconds": 831.3' in (rd(p('data', 'b756_root_banks_parts.json')) or ''), 'present', '1')
    ck_ = lines_of(p('data', 'b756_checks.txt'))
    ct6_ = lines_of(p('tools', 'standing', 'fold', 'closing.tpl'))
    add('ruling (1)(F6), (8)(ii), ferry (read first)', 'data/b756_checks.txt :16 and :18 (116 run, 110 passing, G-RUNNER-GATE vacuous); data/b756_closing.txt :704-:705 ("110 OF 115"); tools/standing/fold/closing.tpl :353 (ARM_LIVE) and :356-:368 (claim_figure)',
        at(ck_, 16).startswith('  ### ### **ARMS RUN : 116. ### LIVE PASSING : 110.') and "['G-RUNNER-GATE']" in at(ck_, 18) and 'VACUOUS' in at(ck_, 18)
        and all('THE WHOLE SUITE PASSING 110 OF 115' in at(cl, n_) for n_ in (704, 705)) and at(ct6_, 353).startswith('ARM_LIVE = re.compile(') and at(ct6_, 356) == 'def claim_figure(text):'
        and 'THE WHOLE SUITE PASSING %d OF %d' in at(ct6_, 366), '%d ; %d lines' % (len(ck_), len(ct6_)), '6')
    dr6_ = lines_of(p('tools', 'b756_doors.py'))
    add('ruling (1)(F7), (8)(iii), (8)(v)', 'tools/acts/b756.py :1875, N5`s reader of "gh repo edit in the capture", beside tools/b756_doors.py :184, the description write sent by gh from inside the tool',
        'gh repo edit in the capture: %s' in at(ac6_, 1875) and "run(['gh', 'repo', 'edit', '--description', new]" in at(dr6_, 184), '%d lines' % len(dr6_), '6')
    # ### (R367)(3): the route for kernel writes
    cmd5_ = lines_of(p('data', 'b745_commands.txt'))
    hk_ = lines_of(p('tools', 'standing', 'hook.py'))
    cm7_ = lines_of(p('tools', 'standing', 'commit.py'))
    add('ruling (3), ferry (read first)', 'data/b745_commands.txt :375-:376, b745`s kernel add and commit by plain git from a scratch clone', '| seat | Bash | cd /d/zq-b738 && git add ' in at(cmd5_, 375)
        and '| seat | Bash | git commit -m "b745 ' in at(cmd5_, 376), '%d lines' % len(cmd5_), '1')
    add('ruling (3), ferry (read first)', 'tools/standing/hook.py :23, :270-:279 and :704, the PLAINGIT refusal since v1.29.0', at(hk_, 23).lstrip().startswith('PLAINGIT (v1.29.0, (R359)(3)(iii))')
        and at(hk_, 270).startswith('def plain_git(cmd, GW=None):') and at(hk_, 279) == "    return ''" and "return 'PLAINGIT', " in at(hk_, 704), '%d lines' % len(hk_), '1')
    add('ruling (3), ferry (read first)', 'tools/standing/commit.py :71 and :726, the one-call tool taking two repositories', at(cm7_, 71).startswith("REPOS = {'relay': RELAY, 'pp': ") and at(cm7_, 71).count("': ") == 2
        and 'argv[0] not in REPOS' in at(cm7_, 726), '%d lines' % len(cm7_), '1')
    pg_ = lines_of(p('tools', 'push_gated.sh'))
    po_ = lines_of(p('data', 'b703_epstein_merge_push_out.txt'))
    add('ruling (3), ferry (read first)', 'tools/push_gated.sh :4 and :6, the default mode and the branch mode with --scratch; data/b703_epstein_merge_push_out.txt :5, :6 and :9, main read back, v0.37 cut at the read-back, its peel read back',
        at(pg_, 4).startswith('# usage: push_gated.sh <repo> <push-branch> [tag[::message] ...]') and '--branch <branch> [--scratch]' in at(pg_, 6) and at(po_, 5).startswith('push_gated: main read back at the remote: 38e27347')
        and at(po_, 6).startswith('push_gated: tag v0.37 made at the read-back 38e27347') and at(po_, 9).startswith('push_gated: tag v0.37 peeled local 38e27347') and 'remote 38e27347' in at(po_, 9),
        '%d ; %d lines' % (len(pg_), len(po_)), '1')
    bc_ = lines_of(p('tools', 'b745_controls.py'))
    add('ruling (3), ferry (read first)', 'tools/b745_controls.py :2, b745`s dispatch and read, to be carried as tools/b757_controls.py with the repository a parameter',
        at(bc_, 2).startswith('"""tools/b745_controls.py -- (R355)(4): THE TWO CONTROLS ON ROUTE (K)') and os.path.exists(p('data', 'b745_dispatch_rows.json')), '%d lines' % len(bc_), '1')
    # ### (R367)(4): the join
    TIPS_ = (('detect-b729', '1023301c'), ('keiper-b725', '01fd33c2'), ('c2-b725', '0395f15d'), ('zq-b730', '1e658870'))
    add('ruling (4), SCOPE', 'SIDE-explicit-formula: main at 8fbab45d and the four tips at their commits, each forking at badacccb', gr(EF_, 'rev-parse', 'main').startswith('8fbab45d')
        and all(gr(EF_, 'rev-parse', b_).startswith(c_) and gr(EF_, 'merge-base', c_, '8fbab45d').startswith('badacccb') for b_, c_ in TIPS_),
        ' '.join('%s %s' % (b_, gr(EF_, 'rev-parse', '--short=8', b_)) for b_, c_ in TIPS_), '2')
    ch_ = dict((c_, gr(EF_, 'diff', '--name-only', 'badacccb', c_).split()) for c_ in ('8fbab45d',) + tuple(c_ for _b, c_ in TIPS_))
    ln_ = [f_ for c_ in ch_ for f_ in ch_[c_] if f_.endswith('.lean')]
    pt_ = sorted(c_ for c_ in ch_ if 'print_targets.txt' in ch_[c_])
    add('ruling (4)', 'since the fork no Lean file is changed on two sides; three tips edit print_targets.txt (keiper-b725, c2-b725, zq-b730); main changed README.md alone',
        len(ln_) == len(set(ln_)) and pt_ == sorted(['01fd33c2', '0395f15d', '1e658870']) and ch_['8fbab45d'] == ['README.md'],
        'Lean files %d, on two sides %d ; print_targets.txt on %s' % (len(ln_), len(ln_) - len(set(ln_)), ' '.join(pt_)), '2')
    U_ = set()
    for c_ in ('8fbab45d',) + tuple(c_ for _b, c_ in TIPS_):
        U_ |= set(l_.strip() for l_ in _blob(EF_, c_, 'print_targets.txt').replace(chr(13), '').split(NL) if l_.strip())
    add('ruling (4)', 'print_targets.txt: the union of main`s and the four tips` lines, each kept once, the set the joined file is read against', len(U_) == 419, '%d lines' % len(U_), '2')
    ez_ = _blob(EF_, '8fbab45d', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean').split(NL)
    ez3_ = _blob(EF_, '1e658870', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean').split(NL)
    mn_ = _blob(EF_, '1e658870', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean').split(NL)
    add('ruling (4)(i)', 'Schema/EpsteinZQ.lean :124 and :136 ("stated, not proved") at main and at zq-b730, :135 differing between the two; Schema/ZQ/EF/Main.lean :25 zq_explicitFormula and :190 zq_premises at zq-b730',
        all('stated, not proved' in at(L_, 124) and 'Each stated, not proved; open. -/' in at(L_, 136) for L_ in (ez_, ez3_)) and at(ez_, 135) != at(ez3_, 135)
        and at(mn_, 25).startswith('theorem zq_explicitFormula : ZQExplicitFormula zqZeroConfig') and at(mn_, 190).startswith('theorem zq_premises : ZQPremises zqFn zqZeroConfig'),
        '%d ; %d ; %d lines' % (len(ez_), len(ez3_), len(mn_)), '2')
    kt_ = _blob(EF_, '01fd33c2', 'SIDEExplicitFormula/KeiperTwo.lean')
    la_ = lines_of(p('data', 'b725_lambda2.txt'))
    keq_ = kt_ == _blob(EF_, 'f52e188c', 'SIDEExplicitFormula/KeiperTwo.lean')
    add('ruling (4)(ii)', 'KeiperTwo.lean :86 at keiper-b725, the sorry in the fallback alternative; the alternative that closes liCoeff_two_keiper read from the banked run: A (:82), data/b725_lambda2.txt :27-:29 (run 41091360710 at f52e188c), the file byte-equal at 01fd33c2',
        'trace "ALT liCoeff_two_keiper SORRY"; sorry)' in at(kt_.split(NL), 86) and 'trace "ALT liCoeff_two_keiper A")' in at(kt_.split(NL), 82) and 'run 41091360710' in at(la_, 27)
        and at(la_, 29).lstrip().startswith('step closed by its alternative A') and keq_, 'alternative A ; the file equal at the two %s' % keq_, '2')
    bd_ = lines_of(p('data', 'b754_doors.txt'))
    ag_ = lines_of(p('data', 'b754_agenda.txt'))
    a4_ = lines_of(p('data', 'b754_author_answers.txt'))
    st4_ = lines_of(p('data', 'b754_sitting.txt'))
    b1_ = ' '.join(at(ag_, n_) for n_ in range(231, 245))
    add('ruling (4)(iii), ferry (read first)', 'data/b754_doors.txt :21-:24, [B1]: SIDE-explicit-formula`s README at main 8fbab45d as it stands, the lines :3, :5-:7, :23-:26; the drafted text at data/b754_agenda.txt :231-:244 (from data/b754_ferry.txt :27); [B1] carried at the b754 sitting (data/b754_author_answers.txt :88, data/b754_sitting.txt :25); no "verified surround" in the draft',
        at(bd_, 21).strip() == '[B1] [B2] SIDE-explicit-formula' and 'README.md at main 8fbab45d' in at(bd_, 23) and 'the lines [B1] names: :3, :5, :6, :7, :23, :24, :25, :26' in at(bd_, 24)
        and at(ag_, 221) == '[B1]' and at(ag_, 231).startswith('  DRAFTED (data/b754_ferry.txt :27, digest 53a09fdfd3237ae1):') and '?"="Carried to a later sitting"' in at(a4_, 88)
        and at(st4_, 25) == '[B1] CARRIED' and 'verified surround' not in b1_, 'the draft %d characters' % len(b1_), '2')
    add('ruling (4), N5', 'v0.38 at SIDE-explicit-formula: the tag object 21c6edaf, its peel 14ca5725', gr(EF_, 'rev-parse', 'v0.38^{commit}').startswith('14ca5725') and gr(EF_, 'rev-parse', 'v0.38').startswith('21c6edaf'),
        gr(EF_, 'rev-parse', 'v0.38^{commit}')[:8], '2')
    add('ruling (4), (7)', 'Schema/Detector.lean :99 `theorem detector` at main and at detect-b729', all(at(_blob(EF_, c_, 'SIDEExplicitFormula/Schema/Detector.lean').split(NL), 99).startswith('theorem detector (C : WeilConfig) (ρ₀ : ℂ)')
        for c_ in ('8fbab45d', '1023301c')), 'both', '5')
    # ### (R367)(5): T0 and T1
    ap_ = lines_of(p('data', 'b752_attribution_plan.txt'))
    add('ruling (5), ferry (read first)', 'data/b752_attribution_plan.txt :43 (T0), :57 (T1), :88 the order of the build and :93 the stops (T0 360 lines, T1 1350)', at(ap_, 43).startswith('  (T0) NO EULER PRODUCT, COMPILED')
        and at(ap_, 57).startswith('  (T1) THE SEPARATION') and at(ap_, 88).lstrip().startswith('BUILD T0 THEN T1') and at(ap_, 93).lstrip().startswith('STOPS: T0 not closing within 360 lines')
        and 'T1 not closing within 1350' in at(ap_, 93), '%d lines' % len(ap_), '3')
    it_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (5) T0, ferry (read first)', 'data/b725_interference.txt :11, r_Q0 at 1, 2, 3 and 6: 2, 0, 0 and 4', '1: 2 0 1 1 ; 2: 0 2 2 -1 ; 3: 0 2 2 -1 ;' in at(it_, 11) and ' ; 6: 4 2 4 1 ;' in at(it_, 11), at(it_, 11)[:40], '3')
    cq_ = lines_of(p('data', 'b750_cq_sign.txt'))
    v48_ = -8 * _m.log(2) - 2 * _m.log(3)
    add('ruling (5) T1, ferry (read first)', 'data/b750_cq_sign.txt :39, the smallest negative n = 48, cQ = -7.742402021816, equal to -8 log 2 - 2 log 3 and to -2 log 48 within 1e-11',
        'THE SMALLEST NEGATIVE n = 48, cQ = -7.742402021816' in at(cq_, 39) and abs(v48_ + 7.742402021816) < 1e-11 and abs(-2 * _m.log(48) + 7.742402021816) < 1e-11, '%.12f' % v48_, '3')
    rg_ = lines_of(p('data', 'b753_registrations.txt'))
    add('ruling (5) T1, ferry (read first)', 'data/b753_registrations.txt :14-:16, H-C3-LAW: n0 = min(p1^4·p2, p1^2·p2·p3), b(n0) = −2, cQ(n) = b(n)·log n at −23', at(rg_, 14).startswith('Let D be a negative fundamental discriminant of class number 3')
        and 'n0 = min(p1^4·p2, p1^2·p2·p3), and b(n0) = −2' in at(rg_, 15) and 'cQ(n) = b(n)·log n at −23' in at(rg_, 16), '%d lines' % len(rg_), '3')
    # ### (R367)(6): the modulus-24 module
    mt_ = gr(MOD_, 'ls-tree', '-r', '--name-only', '597b0869').split()
    bs_ = _blob(MOD_, '597b0869', 'SIDEDirichletMod24/Basic.lean').split(NL)
    add('ruling (6), SCOPE', 'SIDE-dirichlet-mod-24 at 597b0869, its one commit: toolchain v4.29.0-rc8, no Mathlib in its lakefile or manifest, one module beneath its root file, no build workflow',
        gr(MOD_, 'rev-parse', 'main').startswith('597b0869') and gr(MOD_, 'rev-list', '--count', '597b0869') == '1' and _blob(MOD_, '597b0869', 'lean-toolchain').strip() == 'leanprover/lean4:v4.29.0-rc8'
        and not any('mathlib' in _blob(MOD_, '597b0869', f_).lower() for f_ in ('lakefile.toml', 'lake-manifest.json')) and [f_ for f_ in mt_ if f_.endswith('.lean')] == ['SIDEDirichletMod24.lean', 'SIDEDirichletMod24/Basic.lean']
        and not any(f_.startswith('.github/') for f_ in mt_), '%d files ; tags %s' % (len(mt_), ' '.join(gr(MOD_, 'tag', '--list').split())), '4')
    add('ruling (6)', 'SIDEDirichletMod24/Basic.lean :80-:81, the docstring: every unit of order at most 2, with |G| = 8 forcing (ℤ/24)* ≅ (ℤ/2)³', at(bs_, 80).startswith('/-- Theorem 2.1.  Every unit of (ℤ/24)* has order ≤ 2.')
        and 'this forces (ℤ/24)* ≅ (ℤ/2)³. -/' in at(bs_, 81), '%d lines' % len(bs_), '4')
    add('ruling (6)', 'OPEN_TRAILS :12649, the mod-24 lemma priced at b613 for the author`s word, stated there as a Prop over Mathlib`s units', at(ot, 12649).startswith('*Appended 2026-10-04 by b613, under `(R223)`(2)(iii) -- THE MOD-24 LEMMA')
        and 'stated as a Prop over Mathlib’s' in at(ot, 12649), at(ot, 12649)[:40], '4')
    # ### (R367)(7): the wide direction
    SU_ = (('SIDEExplicitFormula/PowerWindow.lean', 339, 'have hstrip := Z.strip ρ hρc'), ('SIDEExplicitFormula/PowerLimit.lean', 813, 'have hstrip := Z.strip ρ hρ'),
           ('SIDEExplicitFormula/RestBound.lean', 311, '(Z.strip ρ hρ).1'), ('Zeta23/Tail.lean', 214, 'have hstrip := Z.strip ρ hρ'), ('Zeta23/WeilEF/ZeroSummability.lean', 214, 'have hstrip := Z.strip _ hρmem'))
    su_ = [w_ in at(_blob(EF_, '8fbab45d', f_).split(NL), n_) for f_, n_, w_ in SU_]
    add('ruling (7)', 'the five uses of the strip field at main: PowerWindow.lean :339, PowerLimit.lean :813, RestBound.lean :311, Zeta23/Tail.lean :214, Zeta23/WeilEF/ZeroSummability.lean :214', all(su_),
        '%d of 5' % sum(su_), '5')
    df_ = _blob(EF_, '8fbab45d', 'Zeta23/Defs.lean').split(NL)
    wc_ = _blob(EF_, '1e658870', 'SIDEExplicitFormula/Schema/Wide/Config.lean').split(NL)
    add('ruling (7)', 'Zeta23/Defs.lean :136-:147, ZeroConfig, its strip field at :142 the closed strip; Schema/Wide/Config.lean :28 at zq-b730, WideConfig over the open strip -1/2 < Re < 3/2 (:7)',
        at(df_, 136) == 'structure ZeroConfig where' and at(df_, 142).strip() == 'strip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1' and at(wc_, 28) == 'structure WideConfig where' and '`-1/2 < Re ρ < 3/2`' in at(wc_, 7),
        '%d ; %d lines' % (len(df_), len(wc_)), '5')
    sp4_ = _blob(EF_, '1e658870', 'SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean')
    add('ruling (7)', 'Schema/ZQ/OffZero/SP4.lean :32 at zq-b730, zq_offline_zero', _decl_line(sp4_, 'zq_offline_zero') == 32, ':%d' % _decl_line(sp4_, 'zq_offline_zero'), '5')
    # ### (R367)(8) and (9): the repairs and the notes
    rg2_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (8)(iv)', 'REGISTRY :13, the header dated 2026-08-24 (b145), to be replaced in place, no line moving', at(rg2_, 13).startswith('**Last updated:** **2026-08-24** (b145,'), at(rg2_, 13)[:40], '6')

    def _dq(a_):
        i_ = text.find(a_)
        j_ = text.find('"', i_ + len(a_)) if i_ >= 0 else -1
        return text[i_ + len(a_):j_] if j_ > 0 else ''
    d1_, d2_ = _dq('PLACE-papers: "'), _dq('SIDE-kernel: "')
    add('ruling (8)(v)', 'the two descriptions as the ruling gives them, 302 and 328 characters as the navigator counted them', len(d1_) == 302 and len(d2_) == 328, '%d ; %d characters' % (len(d1_), len(d2_)), '6')
    ep_ = lines_of(os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'))
    add('ruling (9)(a)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md :5-:15, six dated notes, the last b756`s at :15, a blank :16 and §1`s heading at :17',
        all(at(ep_, n_).startswith('*Dated note, ') for n_ in (5, 7, 9, 11, 13, 15)) and at(ep_, 15).startswith('*Dated note, 2026-11-15, b756:') and at(ep_, 16) == '' and at(ep_, 17).startswith('## 1. The object'),
        '%d lines' % (len(ep_) - 1), '6')
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    add('ruling (9)(b)', 'FACES_LEDGER.md :541, b712`s UPDATE section, the form the act`s follows', at(fl_, 541).startswith('## UPDATE — filed 2026-10-25 (b712): the faces joined by closure at SIDE-faces-join v0.1.0'),
        '%d lines' % (len(fl_) - 1), '6')
    kc_ = lines_of(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md'))
    add('ruling (9)(c)', 'THE_KEYSTONE_CENSUS_v0_8_3.md :1568, b743`s appended note, the file`s last line', at(kc_, 1568).startswith("*Appended 2026-11-06 by b743 under the author's ruling `(R353)`(4)(B):*")
        and not any(l_.strip() for l_ in kc_[1568:]), '%d lines' % (len(kc_) - 1), '6')
    add('ruling (9)(d)', 'REGISTRY :177-:179, the rows 1.5c-21 to 1.5c-23; :924, SIDE-explicit-formula`s kernel row; :1244, b745`s dated note, the form the act`s follows',
        at(rg2_, 177).startswith('| 1.5c-21 |') and at(rg2_, 178).startswith('| 1.5c-22 |') and at(rg2_, 179).startswith('| 1.5c-23 |') and at(rg2_, 924).startswith('| **`SIDE-explicit-formula`**')
        and at(rg2_, 1244).startswith("*Dated note, b745, 2026-11-07, under the author's ruling `(R355)`(3), to the rows 1.5c-21, 1.5c-22 and 1.5c-23 (:177-:179)"), '%d lines' % (len(rg2_) - 1), '6')
    OR_ = ('W-ORD-KEIPER-FACE', 'W-ORD-EXPLICIT-FORMULA-C1', 'W-ORD-E2-SEPARATION', 'W-ORD-BESSEL-BOUND-TIGHTEN', 'W-ORD-B518-FLOAT', 'W-ORD-MECHANISM-ATTRIBUTION')
    ott_ = NL.join(ot)
    add('ruling (9), (5)', 'OPEN_TRAILS: the six orders the ruling names, each standing; W-ORD-SQUARES-AT-24 not yet entered', all(o_ in ott_ for o_ in OR_) and 'W-ORD-SQUARES-AT-24' not in ott_,
        '%d of 6 ; W-ORD-SQUARES-AT-24 %d' % (sum(1 for o_ in OR_ if o_ in ott_), ott_.count('W-ORD-SQUARES-AT-24')), '6')
    add('ruling (9), (1)', 'OPEN_TRAILS :18487, the file`s last line: b756`s Next line, the build as b757', at(ot, 18487).startswith('**Next:** ((R366)(7)) the build as b757') and not any(l_.strip() for l_ in ot[18487:]),
        '%d lines' % (len(ot) - 1), '6')
#⟪END⟫
#⟪SECTION citation 2⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 3⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b757 step zero: (R367)(1)'s counts over b756's banks, written in place of b756's rows over b755's; each tag read as the bank tags it,
    # ### an owner of more than one word read whole; no post-seal events bank at b756 ((R366)(1)(ii)); THE TOOLS' owner carries no 'S and the
    # ### tag reader passes it by (five events rows and one defects row, read apart below: the one CLAIM item is events (10))
    add('ruling (1), ferry (read first)', 'b756`s events (1)-(37) and its 11 lettered defects (a)-(k), no post-seal events bank (data/b756_events.txt, data/b756_defects.txt)',
        starts == list(range(1, 38)) and len(letters) == 11 and letters[-1] == 'k' and not os.path.exists(p('data', 'b756_events_postseal.txt')),
        'events %s ; letters %d (%s-%s) ; post-seal %s' % (starts[-1:], len(letters), letters[:1], letters[-1:], 'absent' if not os.path.exists(p('data', 'b756_events_postseal.txt')) else 'PRESENT'), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_, nt_, ncl_, ncs_ in (('data/b756_events.txt', ev, 37, 32, 0, 32), ('data/b756_defects.txt', dl, 11, 10, 0, 10)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_.group(2) for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        add('ruling (1), ferry (read first)', '%s: %d rows, %d tagged by the reader`s owner form; CLAIM %d, CLOSE %d' % (f_, nr_, nt_, ncl_, ncs_),
            len(rr_) == nr_ and len(tg_) == nt_ and tg_.count('CLAIM') == ncl_ and tg_.count('CLOSE') == ncs_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d' % (len(rr_), len(tg_), tg_.count('CLAIM'), tg_.count('CLOSE')), '1')
    TO_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE TOOLS' \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    tev_ = [(k_ + 1, TO_.match(l_).group(1)) for k_, l_ in enumerate(ev) if TO_.match(l_)]
    tdl_ = [(k_ + 1, TO_.match(l_).group(1)) for k_, l_ in enumerate(dl) if TO_.match(l_)]
    add('ruling (1)', 'THE TOOLS` rows the owner form passes by: events :64 (10) [CLAIM ; NEW], the one CLAIM item, and :85, :99, :132, :165 [CLOSE]; defects :12 (c) [CLOSE ; REPEAT b755 (d)]',
        tev_ == [(64, 'CLAIM'), (85, 'CLOSE'), (99, 'CLOSE'), (132, 'CLOSE'), (165, 'CLOSE')] and tdl_ == [(12, 'CLOSE')] and at(ev, 64).startswith("    (10) THE TOOLS' [CLAIM ; NEW]:"),
        'events %s ; defects %s' % (tev_, tdl_), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (1)', 'FINDINGS :%d, b756`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## The clearing act under (R366): the results of b755 written into the documents they bear on'), at(fi, K.B711_ENTRY)[:50], '1')
    add('ruling (1)', 'FINDINGS :%d and :%d, b755`s weight line and corrigendum (b756`s), the form b757`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM),
        at(fi, K.B711_WEIGHT).startswith('*Appended 2026-11-15 by b756 to b755’s entry (:15296)') and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b755’s record, short'), at(fi, K.B711_WEIGHT)[:40], '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b756`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b756 — lane two, act one hundred and eighty-three, the clearing act under (R366)'), at(ot, K.B711_TRAIL)[:50], '1')
    add('ruling (1)', 'OPEN_TRAILS :%d, b756`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '1')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula and SIDE-dirichlet-mod-24, the two kernels this act opens', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-dirichlet-mod-24/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.35.3 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.35.3',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### (R367) SCOPE: b756's export by its file name, bytes and hash, the folder that holds it not printed (N5)
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    add('ruling SCOPE', 'b756`s mirror %s, its sha256 opening 852b6dde as the navigator read it' % os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest().startswith('852b6dde'),
        '%d bytes ; sha256 %s' % (len(mz_), _h.sha256(mz_).hexdigest()[:16]), '6')
    # ### PATHS: the clones at the paths the worklist holds, counted; one absent printed by its name alone
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R367)(3), (4), (6): the two kernels' clones before any kernel write, on main and clean
    kc2_ = [(os.path.basename(r_), gr(r_, 'rev-parse', '--abbrev-ref', 'HEAD'), gr(r_, 'status', '--porcelain')) for r_ in ('D:/SIDE-explicit-formula', 'D:/SIDE-dirichlet-mod-24')]
    add('ruling (3), (4), (6)', 'the two kernels` clones on main with nothing changed or staged, before any kernel write', all(h_ == 'main' and not s_ for _n, h_, s_ in kc2_),
        ' ; '.join('%s %s %s' % (n_, h_, 'clean' if not s_ else 'CHANGED') for n_, h_, s_ in kc2_), '1')
#⟪END⟫
#⟪SECTION citation 6⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 6); the body carried, 0 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (2)', 'the push-b756-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R367)(2): act_current alone, then b756's four carried files, each alone; tools/mirror_prevbuild.json's commit holds act_current
    # ### beside it, the shared-tool refusal's route (amend.py shared --staged --write) having written its entry (events (2))
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b756_relay_push-b756-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['data/act_current.json', 'tools/mirror_prevbuild.json']),
                    ((K.STEPZERO_REFUSALS or (None,))[0], ['data/b756_hook_refusals.txt']),
                    (getattr(K, 'STEPZERO_SCAN', None), ['data/b757_address_scan_commits.txt'])):
        if not c_:
            add('ruling (2)', '%s -- TO BE COMMITTED at step zero' % ' '.join(fs_), False, 'NOT COMMITTED', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (2)', '%s committed %s at %s, an ancestor of HEAD' % (' '.join(fs_), 'alone' if len(fs_) == 1 else 'together (the shared-tool route)', c_), sorted(nm_) == sorted(fs_)
            and gr('D:/relay', 'merge-base', c_, 'HEAD').startswith(c_), ' '.join(nm_)[:90], '0')
    # ### data/b757_address_scan_commits.txt is the act's own scan bank, appended by the one-call tool at every commit after its own: read apart
    stz_ = gr('D:/relay', 'status', '--porcelain', '--', 'data/b756_relay_push-b756-closing_push_out.txt', 'tools/mirror_prevbuild.json', 'data/b756_hook_refusals.txt')
    add('ruling (2)', 'three of the four files b756 left uncommitted clean at HEAD after their commits; the fourth, the act`s own scan bank, appended at every commit since', not stz_,
        stz_.replace(NL, ' | ') or 'clean', '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4), (10)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (10)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (2)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (2), ferry (read first)', 'data/b757_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b757_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b757_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with v1.34.7's controls and the rules' rows, the map (the constellation's controls and rerun, the
reverse read, what the two find beyond (3)), the notes of (3), the orders and the checkpoints (the orders read, the instruments draft, the
status lines, the passed writes, the ceiling after Component 4), the tool changes (v1.34.8 to v1.35.3, the fault count and its placing, the
README route and the descriptions), the name and address scan, the reproduction not run (events (29)), the touch read of v9 and the standing
arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R367)'s counter line beneath the title, the
repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the seal printed from
its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R367)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R367)(8): no kernel touched, no branch of any kernel merged, created,
moved or deleted, no tag, no Lean file; (6)'s README route carried whole and the two descriptions refused by the server for length, each read
back unchanged, relay data/b757_events.txt (27)).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b757 ((R367)(7) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R365)(2)(iv)(c): the outbound sentence from the one clause
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): statement TITLE_LINE; it carried an act ordinal or the read-first needles
TITLE_LINE = __import__('standing.carry', fromlist=['Carried']).Carried('b757`s TITLE_LINE')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b756's sections over b756's objects not carried), headed as CLOSING_SECTIONS names them. A row
    of two reads its bank's verdict line by vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.34.7: (R367)(1)(i) the next act`s line as the author answers at the root and (1)(ii) the words that name a bank not kept, each case through the route before and the route after', 'b757_standing_v1347.txt'),
                ('the rows (a) to (c) of the rule this act works by, in force from b757 ((R367)(2))', 'b757_rules.txt', r'(?m)^  \(c\) [^\n]*'),
                ('the probe-path refusal printed before the lock gate', 'b757_pathrefusal.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE MAP ((R367)(4))', [
                ('the constellation`s controls as b589 ran them, printed before its figures', 'b757_constellation_control.txt'),
                ('the rerun over the roster`s current editions, one line per table, the hand-read beneath it', 'b757_constellation_summary.txt'),
                ('the reverse read of the six statements, its controls before its figures, run before the writes of (3)', 'b757_reverse_read.txt'),
                ('what the two find beyond (3), banked with its count and written nowhere at this act', 'b757_beyond_three.txt')]),
            ('THE NOTES OF (3) ((R367)(3))', [
                ('the five writes of (3)(i) to (v), each cut from the ruling`s text and read against it, one PLACE-papers commit each', 'b757_notes.json', r'"confirm": "[^"]*"')]),
            ('THE ORDERS AND THE CHECKPOINTS ((R367)(5))', [
                ('the twelve ready orders read at today`s tree, each placed', 'b757_orders_read.txt'),
                ('the two INSTRUMENTS rows drafted for the put', 'b757_instruments_draft.txt'),
                ('the twelve status lines on the author`s pass', 'b757_orders_moves.txt'),
                ('the CP lines and the two INSTRUMENTS rows written as passed, one PLACE-papers commit each', 'b757_passed.json', r'"confirm": "[^"]*"'),
                ('the ceiling read again after Component 4', 'b757_ceiling_c4.txt')]),
            ('THE TOOL CHANGES ((R367)(6))', [
                ('tools/standing/ at v1.34.8: W-ORD-LABEL-READER, the HERE work of (5)(i)', 'b757_standing_v1348.txt'),
                ('tools/standing/ at v1.34.9: [U1], the cadence of the passes', 'b757_standing_v1349.txt'),
                ('tools/standing/ at v1.35.0: [U2], the ledgers` writers', 'b757_standing_v1350.txt'),
                ('the faults of b756`s carried faults and defects by the acts they stand in, descending', 'b757_faults.txt'),
                ('tools/standing/ at v1.35.1: the faults of two acts or more, the first three by count', 'b757_standing_v1351.txt'),
                ('tools/standing/ at v1.35.2: the faults of two acts or more, the next by count', 'b757_standing_v1352.txt'),
                ('where each fault of two acts or more went', 'b757_faults_placed.txt'),
                ('tools/standing/ at v1.35.3: [H1]`s held part, the handoff page in the archive', 'b757_standing_v1353.txt'),
                ('the README route with [B1] and [B3], carried whole, and the two descriptions, each refused by the server for length (relay data/b757_events.txt (27))', 'b757_doors.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b757_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS NOT REPRODUCED (the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run not run: its rows compute at a field, which (R367)(8) and N1 bar; the arm declared failing on the face', 'b757_events.txt', r'(?m)^    \(29\) [^\n]*')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R365)(2)(vi): composed, not carried
    '    no kernel touched ((R367)(8)): no branch of any kernel merged, created, moved or deleted ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    no kernel`s README written: (6)`s README route with [B1] and [B3] carried whole, no route within (8) writing one (relay data/b757_doors.txt, data/b757_events.txt (27)) ; the two descriptions sent as ruled and each refused by the server for length, read back unchanged ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b757 found them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b756-* branches of relay and PLACE-papers deleted at step zero by name, after the --merged listing, one per command and each its own message ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ v1.34.7 to v1.35.3 landed before the gate, each a version commit of its own with its controls ; each tool of (4) committed before its run and its controls printed before its figures ; the reverse read run before the writes of (3) ; the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: each write of (3) equal to the ruling`s text byte for byte between its quotation marks (relay data/b757_notes.json) ; no sentence of any paper above a note edited ; no bank calling a result new ; no figure of the navigator`s workspace printed as a banked figure ; the entry`s INTEGRATION line composed from the banks` feet ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; nothing computed at any field ((R367)(8) ; the reproduction not run, relay data/b757_events.txt (29)) ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b757_address_scan.txt, data/b757_address_scan_postlock.txt, data/b757_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written (both refused for length) ; no README written ; no anchor edited ; no order entered, two statuses moved by the orders tool`s route in the trail ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS ((1)(i)`s dated line, (3)(v)`s five lines under one dated head, the CP-6 and CP-7 lines, and the trail), INSTRUMENTS (I-110 and I-111) and the four documents of (3)(i) to (iv), each a dated note beside its text ; no sentence of a paper`s body edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b757`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; data/b757_rules.txt written at Component 1 ;',
    '    tools/standing/ v1.34.7 to v1.35.3, seven version commits each with its controls in its bank (relay data/b757_standing_v1347.txt to data/b757_standing_v1353.txt) ; HANDOFF.md written once by tools/standing/handoff.py before the gate, and carried in the archive ([H1], v1.35.3) ; act_current`s shared_edits as standing/carry.py shared reads them ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R367)(8) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one, its answer in relay data/b757_author_answers.txt ; the build as b757 -- the four branches of the criterion kernel joined under a tag on main, T0 and T1, the criterion over the wider strip, the modulus-24 lemma, the written proofs of the class-number-3 law and of the closed form ((R367)(7)), or another the author names ;',
    '        what the constellation rerun and the reverse read find beyond (3), for the prose pass and the re-cuts (relay data/b757_beyond_three.txt) ; the README route with [B1] and [B3] and the two descriptions, carried whole for the author`s wording (relay data/b757_doors.txt) ;',
    '        the one fault carried by the placing (relay data/b757_faults_placed.txt) ; the reproduction not run at this act (relay data/b757_events.txt (29)) ; the defects of relay data/b757_defects.txt for the next corrigendum ;',
    '        the ten orders carried with the build and later (relay data/b757_orders_moves.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b757 found them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b756: seven standing changes, v1.34.7 ((R366)(1), read in the corrigendum section) and v1.34.8 to v1.35.3 ((5)(i)'s HERE work and
    # ### (6), read in the tool changes section); the carry's diffs here (b756 carried at step zero before the fold; its tools since are the
    # ### templates and tools/acts/b756.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b757 found them; port-b707 at b712`s tip %s; no README written, (R367)(6)`s route carried whole)' % (
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
    b757's form over b757's objects: the corrigendum's foot; the seven standing versions' controls from their banks; the constellation's
    controls and its rerun's foot; the reverse read's two feet and what the two find beyond (3); the notes' bank (the five writes of (3)
    and their lines); the orders read, the instruments draft and the status lines; the passed writes' bank; the ceiling after Component 4;
    the fault count, its placing and the README route's two feet; the citation check; the address scan; each by its own lines through
    _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed. No
    reproduction bank: the run is not run at this act (relay data/b757_events.txt (29))."""
#⟪END⟫
#⟪SECTION record 4⟫
    vs_ = [(v_,) + _bfig(b_.split('/', 1)[1], r'\*\*%s: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*' % re.escape(v_), '%s`s controls' % v_)
           for v_, _c, b_, _n in K.STANDING_BANKS]
    vh_ = [(v_, '(R367)(6)' in (rdn(b_.split('/', 1)[1]).split(NL) or [''])[0]) for v_, _c, b_, _n in K.STANDING_BANKS]   # ### the versions of (6), by each bank's head
    cc_ = _bfig('%s_constellation_control.txt' % ACT, r'\*\*THE CONTROLS: (\d+) OF (\d+) AS WANTED ; ([\d.]+) s\.\*\*', 'the constellation`s controls')
    cm_ = _bfig('%s_constellation_summary.txt' % ACT, r'\*\*TABLES READ: (\d+) OF (\d+)\. ### ROWS MOVED OR GONE BY THE TOOL: (\d+) \{[^}]*\} ; AFTER THE HAND-READ: (\d+) COUNTED, (\d+) NOT, (\d+) UNREAD\.',
                'the rerun`s foot')
    rv_ = _bfig('%s_reverse_read.txt' % ACT, r'\*\*THE REVERSE READ: CONTROLS (\d+) OF (\d+) AS WANTED ; LINES CARRYING THE SIX STATEMENTS (\d+): ADDRESSED BY \(3\) (\d+) ; '
                r'REPAIRED BY \(1\)\(ii\) (\d+) ; THE RECORD (\d+) ; BEYOND \(3\) (\d+), OF THEM OVERTAKEN (\d+),', 'the reverse read`s foot')
    rn_ = _bfig('%s_reverse_read.txt' % ACT, r'\*\*THE COUNT FOR \(4\)\(iii\) AND THE ROOT PROMPT: (\d+) LINE\(S\) BEYOND \(3\)', 'the reverse read`s count')
    bt_ = _bfig('%s_beyond_three.txt' % ACT, r'\*\*THE TWO COUNTS FOR THE ROOT PROMPT: THE CONSTELLATION RERUN (\d+) ROWS MOVED OR GONE \((\d+) BY THE TOOL\) ; THE REVERSE READ (\d+) LINE\(S\) BEYOND \(3\)',
                'the two counts')
    nj_ = jl('%s_notes.json' % ACT).get('items') or {}
    if sorted(nj_) != ['i', 'ii', 'iii', 'iv', 'v'] or not all((nj_[k_].get('confirm') or '').startswith('PLACE-papers ') for k_ in nj_):
        sys.exit('### data/%s_notes.json DOES NOT CARRY THE FIVE WRITES OF (3) AND THEIR CONFIRMS -- NOTHING COMPOSED' % ACT)
    od_ = _bfig('%s_orders_read.txt' % ACT, r'\*\*THE TWELVE ORDERS AT TODAY`S TREE: DONE (\d+) ; HERE (\d+) ; WITH THE BUILD (\d+) ; LATER (\d+) ;', 'the orders read`s foot')
    om_ = _bfig('%s_orders_moves.txt' % ACT, r'\*\*TWELVE STATUS LINES: DISCHARGED (\d+) \(DONE (\d+), HERE (\d+)\) ; CARRIED (\d+) \(WITH THE BUILD (\d+), LATER (\d+)\) ;', 'the status lines` foot')
    id_ = _bfig('%s_instruments_draft.txt' % ACT, r'\*\*TWO ROWS DRAFTED, (I-\d+) AND (I-\d+), AFTER (I-\d+) ; FIGURES ON THEIR LINES (\d+) OF (\d+) ;', 'the instruments draft`s foot')
    pj_ = jl('%s_passed.json' % ACT).get('items') or {}
    if sorted(pj_) != ['cp', 'instruments'] or not all((pj_[k_].get('confirm') or '').startswith('PLACE-papers ') for k_ in pj_):
        sys.exit('### data/%s_passed.json DOES NOT CARRY THE TWO PASSED WRITES AND THEIR CONFIRMS -- NOTHING COMPOSED' % ACT)
    c4_ = _bfig('%s_ceiling_c4.txt' % ACT, r'\*\*THE CEILING AFTER COMPONENT 4: SPENT ([\d.]+) h \+ REMAINING LOWER ([\d.]+) h = ([\d.]+) h AGAINST (\d+) h ; (NOTHING CARRIED) ;',
                'the ceiling after Component 4')
    fc_ = _bfig('%s_faults.txt' % ACT, r'\*\*THE FAULTS : (\d+) ROWS ; IN TWO ACTS OR MORE (\d+) \(', 'the fault count`s foot')
    fp_ = _bfig('%s_faults_placed.txt' % ACT, r'\*\*THE FAULTS OF TWO ACTS OR MORE: (\d+) ; LANDED (\d+) \(([^)]*)\) ; CARRIED (\d+) ; NO CODE (\d+) ; UNPLACED (\d+) ;', 'the placing`s foot')
    dr_ = _bfig('%s_doors.txt' % ACT, r'\*\*THE DESCRIPTIONS: WRITTEN AS RULED AND READ BACK EQUAL (\d+) of (\d+) ; REFUSED BY THE SERVER FOR LENGTH, EACH READ BACK UNCHANGED, (\d+) ',
                'the descriptions` foot')
    dh_ = _bfig('%s_doors.txt' % ACT, r'\*\*(THE README ROUTE HALTED): .*?(\[B1\] AND \[B3\] CARRIED WHOLE)', 'the README route`s foot')
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b757: no order entered this act ((R367) enters none; two statuses move by the orders tool's route in the trail)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                corr_findings=((co.get('findings') or {}).get('claim'), (co.get('findings') or {}).get('close'), (co.get('findings') or {}).get('repeat')),
                vers=[(v_, c_, int(n_), int(w_)) for v_, c_, n_, w_ in vs_],   # ### the seven: (version, controls, cases, as wanted)
                vers6=[v_ for v_, o_ in vh_ if o_],
                cc_ok=int(cc_[0]), cc_of=int(cc_[1]), cc_secs=cc_[2],
                cm_tables=int(cm_[0]), cm_of=int(cm_[1]), cm_tool=int(cm_[2]), cm_counted=int(cm_[3]), cm_not=int(cm_[4]), cm_unread=int(cm_[5]),
                rv_ctl=(int(rv_[0]), int(rv_[1])), rv_lines=int(rv_[2]), rv_addressed=int(rv_[3]), rv_repaired=int(rv_[4]), rv_record=int(rv_[5]),
                rv_beyond_all=int(rv_[6]), rv_overtaken=int(rv_[7]), rv_beyond=int(rn_[0]),
                bt_moved=int(bt_[0]), bt_tool=int(bt_[1]), bt_beyond=int(bt_[2]),
                notes=[(k_, nj_[k_].get('file'), nj_[k_].get('confirm'), len([x_ for x_ in nj_[k_].get('lines') or [] if x_.get('kind') != 'head'])) for k_ in ('i', 'ii', 'iii', 'iv', 'v')],
                notes_written=sum(len([x_ for x_ in nj_[k_].get('lines') or [] if x_.get('kind') != 'head']) for k_ in nj_),
                od=tuple(int(x_) for x_ in od_), om=tuple(int(x_) for x_ in om_),
                id_rows=(id_[0], id_[1]), id_after=id_[2], id_figs=(int(id_[3]), int(id_[4])),
                passed=[(k_, pj_[k_].get('file'), pj_[k_].get('confirm'), len([x_ for x_ in pj_[k_].get('lines') or [] if x_.get('kind') != 'head'])) for k_ in ('cp', 'instruments')],
                cp='passed' if len([x_ for x_ in (pj_.get('cp') or {}).get('lines') or [] if x_.get('kind') != 'head']) == 2 else 'struck',
                c4_spent=c4_[0], c4_lower=c4_[1], c4_sum=c4_[2], c4_ceiling=int(c4_[3]), c4_word=c4_[4],
                fc_rows=int(fc_[0]), fc_two=int(fc_[1]),
                fp_two=int(fp_[0]), fp_landed=int(fp_[1]), fp_where=fp_[2], fp_carried=int(fp_[3]), fp_nocode=int(fp_[4]), fp_unplaced=int(fp_[5]),
                dr_equal=int(dr_[0]), dr_of=int(dr_[1]), dr_refused=int(dr_[2]), dr_halted=dh_[0],
                tc_landed=len([v_ for v_, o_ in vh_ if o_]), tc_carried=1 if dh_[1] else 0,
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R367): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b757_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b757_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b757's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line);
# ### the constellation's controls stand in a bank of their own (data/b757_constellation_control.txt), read by time in _n2
N2_CONTROLS = (('data/b757_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b757_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b757_standing_v1347.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.34.7: CONTROLS '),
               ('data/b757_standing_v1348.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.34.8: CONTROLS '),
               ('data/b757_standing_v1349.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.34.9: CONTROLS '),
               ('data/b757_standing_v1350.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.35.0: CONTROLS '),
               ('data/b757_standing_v1351.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.35.1: CONTROLS '),
               ('data/b757_standing_v1352.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.35.2: CONTROLS '),
               ('data/b757_standing_v1353.txt', '### THE COMPILE CONTROL, BEFORE ANY FIGURE', '### ### **v1.35.3: CONTROLS '),
               ('data/b757_reverse_read.txt', '## THE CONTROLS, BEFORE THE FIGURES', '## (1) A ZERO LOCATED IN LEAN, OR NONE'),
               ('data/b757_orders_moves.txt', 'CONTROLS 12 OF 12 AS WANTED', '#### THE LINES BEGIN'),
               ('data/b757_ceiling_c4.txt', 'CONTROLS 4 OF 4 AS WANTED', '## THE ROWS'),
               ('data/b757_faults.txt', '## THE CONTROLS, BEFORE ANY COUNT', '## THE FAULTS, DESCENDING'),
               ('data/b757_faults_placed.txt', '## THE CONTROLS, BEFORE ANY PLACING', '## THE PLACING, IN THE COUNT'),
               ('data/b757_doors.txt', '### the matcher`s controls: 5 of 5 AS WANTED', '## THE WRITES, EACH READ BACK'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
N2_SECTIONS = ()
N2_RIDERS = ('data/b757_steps.json', 'data/b757_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


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
    """N2 (R367): the step-zero reads, the chain read and the carry printed before any write (the step-zero bank's times before the
    act_current commit); the act's commits in the worklist's TIME_ORDER by time, relay and PLACE-papers together -- step zero's, v1.34.7, the
    lock gate carried, the weight and corrigendum (PLACE-papers, then relay), the map's tool and banks, the notes' tool, its five PLACE-papers
    writes and its bank, the orders read, the put, the passed writes' tool and its two PLACE-papers writes, v1.34.8, the status lines, the
    ceiling, v1.34.9 to v1.35.3 with the fault count, the placing and the README route, then the passed bank and the handoff page where made;
    each standing change landing before the gate, a commit of its own moving VERSION with its controls bank, the act's commits under
    tools/standing/ those seven and no other; each tool of K.GENS first added by a commit of its own carrying it and not its bank, the bank's
    commit not the tool; the constellation's tool committed before its controls ran, and those AS WANTED; each tool's controls before its
    figures; the reverse read banked before the first write of (3); the (W) regeneration, the pre-lock comparison and the probe-path refusal
    before the lock gate; v1.34.7 an ancestor of HEAD."""
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
    szt_ = [(n_, re.search(p_, sz_)) for n_, p_ in (('the step-zero reads', r'THE STEP-ZERO READS \((\d\d:\d\d:\d\d)Z, before any write\)'),
                                                    ('the chain read', r'THE CHAIN READ \((\d\d:\d\d:\d\d)Z\)'),
                                                    ('the carry', r'THE CARRY before any write of the relay: .*?\((\d\d:\d\d:\d\d)Z'))]
    sze_ = [(n_, _hms_epoch(m_.group(1)) if m_ else None) for n_, m_ in szt_]
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
    # ### the constellation's tool committed before its controls ran, those AS WANTED; the reverse read banked before the first write of (3)
    cc_t_ = rdn('%s_constellation_control.txt' % ACT)
    cc0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)\s*$', (cc_t_.split(NL) or [''])[0])
    cons_ = bool(cc0_) and ct_(ROOT, K.C2_PLAN_FIRST) < (_iso_epoch(cc0_.group(1)) or 0) and '### ### **THE CONTROLS: 6 OF 6 AS WANTED ;' in cc_t_
    rv0_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)\s*$', (rdn('%s_reverse_read.txt' % ACT).split(NL) or [''])[0])
    rev_ = bool(rv0_) and (_iso_epoch(rv0_.group(1)) or 0) < ct_(PP, dict(K.PP_CHAIN)['pp_i']) and ct_(ROOT, dict(K.CHAIN)['c2_reverse']) < (_iso_epoch(rv0_.group(1)) or 0)
    sect_ = stepzero_ and standing_ and gen_ and cons_ and rev_
    route_ = sect_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT, optional=True)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the step-zero reads, the chain read and the carry printed before any write (%s, each by the step-zero bank, before the act_current commit %s): %s; the standing changes landing before the gate, each a commit of its own moving VERSION with its controls bank (%s), the act`s commits under tools/standing/ those seven and no other (%s): %s; each tool first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the tool (%s): %s; the constellation`s tool committed (%s) before its controls ran, those AS WANTED: %s; the reverse read banked after its tool`s last commit and before the first write of (3): %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; the act`s %d commits in the worklist`s order by time, relay and PLACE-papers together: %s (%s); v1.34.7 an ancestor of HEAD: %s; the tools` controls before their figures: %s' % (
            ', '.join('%s %s' % (n_, ('%sZ' % m_.group(1)) if m_ else 'unread') for n_, m_ in szt_), K.ACT_CURRENT_COMMIT, stepzero_,
            ', '.join('%s %s %s' % (v_, c_[:8], o_) for v_, c_, o_ in st_rows_), ' '.join(h_[:8] for h_ in st_commits_) or 'none', standing_,
            ', '.join('%s %s' % x_ for x_ in gens_ok_), gen_, K.C2_PLAN_FIRST[:8], cons_, rev_,
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_,
            len(chain_), order_, ' '.join('%s %s@%d' % (k_, h_[:8], c_) for k_, (_r, h_), c_ in zip([k_ for k_ in okeys_ if k_ in keyed_], chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b756's objects): the banks whose grade prints at their end, (bank, the words the foot carries); the address scan written
# ### before the gate; no reproduction bank (relay data/b756_events.txt (29))
N3_GRADED = (('b757_corrigendum.txt', ('ITEMS 46',)),
             ('b757_standing_v1347.txt', ('v1.34.7: CONTROLS', 'ALL AS WANTED')), ('b757_standing_v1348.txt', ('v1.34.8: CONTROLS', 'ALL AS WANTED')),
             ('b757_standing_v1349.txt', ('v1.34.9: CONTROLS', 'ALL AS WANTED')), ('b757_standing_v1350.txt', ('v1.35.0: CONTROLS', 'ALL AS WANTED')),
             ('b757_standing_v1351.txt', ('v1.35.1: CONTROLS', 'ALL AS WANTED')), ('b757_standing_v1352.txt', ('v1.35.2: CONTROLS', 'ALL AS WANTED')),
             ('b757_standing_v1353.txt', ('v1.35.3: CONTROLS', 'ALL AS WANTED')),
             ('b757_constellation_control.txt', ('THE CONTROLS: 6 OF 6 AS WANTED',)),
             ('b757_constellation_summary.txt', ('TABLES READ: 39 OF 39', 'AFTER THE HAND-READ: 7 COUNTED')),
             ('b757_reverse_read.txt', ('THE COUNT FOR (4)(iii) AND THE ROOT PROMPT: 4 LINE(S) BEYOND (3)',)),
             ('b757_beyond_three.txt', ('THE TWO COUNTS FOR THE ROOT PROMPT', 'THE CONSTELLATION RERUN 7 ROWS', 'THE REVERSE READ 4 LINE(S)')),
             ('b757_orders_read.txt', ('DONE 1 ; HERE 1 ; WITH THE BUILD 5 ; LATER 5',)),
             ('b757_instruments_draft.txt', ('FIGURES ON THEIR LINES 26 OF 26',)),
             ('b757_orders_moves.txt', ('TWELVE STATUS LINES', 'DISCHARGED 2')),
             ('b757_ceiling_c4.txt', ('THE CEILING AFTER COMPONENT 4', 'NOTHING CARRIED')),
             ('b757_faults.txt', ('THE FAULTS : 43 ROWS', 'IN TWO ACTS OR MORE 16')),
             ('b757_faults_placed.txt', ('UNPLACED 0', 'EACH LANDED ROW CHECKED AS WANTED')),
             ('b757_doors.txt', ('THE DESCRIPTIONS:', 'CARRIED WHOLE')),
             ('b757_citation_check.txt', ('THE CHECK CLEAN',)), ('b757_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### N3 (R366): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word; the centre
# ### matcher over zeta (the symbol, Riemann's, or a zeta function not the Epstein's), RH, GRH and Weil positivity on classK, (R366)'s N3
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
N3_LOC = (r'(?:\b(?:RH|GRH|classK)\b|ζ|\bRiemann(?:`s|\'s)? zeta\b|(?<!Epstein )\bzeta function\b|\bWeil positivity on classK\b).*'
          r'\b(?:holds|hold|fails|fail|proved|refuted|moved)\b')
N3_BANKS = ('stepzero', 'corrigendum', 'rules', 'constellation_summary', 'constellation_control', 'reverse_read', 'beyond_three', 'orders_read',
            'instruments_draft', 'orders_moves', 'ceiling_c4', 'faults', 'faults_placed', 'doors', 'standing_v1347', 'standing_v1348', 'standing_v1349',
            'standing_v1350', 'standing_v1351', 'standing_v1352', 'standing_v1353', 'events', 'defects')
# ### N3 (R366): no figure of the navigator's workspace printed as a banked figure -- the two workspace readings (3)(v)'s [L19] names "in the
# ### navigator's workspace and in no bank" (data/b756_ferry.txt :21), written by (3) as the ruling's words and nowhere else: never an act's
# ### own sentence, the ruling's text being a quotation the matcher reads past
N3_NAV_FIGS = r'\b14 of 666\b|\b10 of 465\b'
# ### N3 (R366): each write of (3) against the ruling's text between its quotation marks -- (item, the ferry's line(s)); (v)'s lines each the
# ### quoted line, one space and the closing words "(the navigator's)" ((3)(v), data/b756_ferry.txt :18)
N3_NOTES = (('i', (14,)), ('ii', (15,)), ('iii', (16,)), ('iv', (17,)), ('v', (19, 20, 21, 22, 23)))
N3_CLOSING = " (the navigator's)"
N3_PAPERS = ('phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
             'day1/Which_Structure_Confines_v2_4_0.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md')


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
    """the entry's last line, (R366)'s INTEGRATION line (data/b756_ferry.txt :54) composed from the banks' feet through _figs, adjusted to
    what the act did: the notes of (3) by the notes bank's lines, the rerun by its tables and its hand-read count, the reverse read by its
    count for (4)(iii), the orders by the orders read's foot, the checkpoints by the passed writes' bank, the tool changes by the standing
    banks of (6) and the README route's foot."""
    return ('INTEGRATION: the notes of (3): %d written of 9; the constellation rerun: %d documents, %d rows moved or gone; the reverse read: %d '
            'lines beyond those written; the orders: %d done, %d here, %d with the build, %d later; CP-6 and CP-7 %s; the tool changes: %d landed, '
            '%d carried; nothing computed, nothing built' % (
                f['notes_written'], f['cm_tables'], f['cm_counted'], f['rv_beyond'], f['od'][0], f['od'][1], f['od'][2], f['od'][3], f['cp'],
                f['tc_landed'], f['tc_carried']))


def _quoted(s_):
    """the text between a line's opening quotation mark and its last (tools/b756_notes.py quoted, read again); None where either is missing
    or one stands inside."""
    s_ = (s_ or '').rstrip()
    if s_.count('"') < 2 or not s_.endswith('"'):
        return None
    t_ = s_[s_.index('"') + 1:s_.rindex('"')]
    return t_ if t_ and '"' not in t_ else None


def _notes_rows():
    """N3 (R366): each write of (3) at PLACE-papers HEAD against the ruling's text between its quotation marks: each line the notes bank
    names, read from its file at HEAD, equal to the cut ((i) to (iv)) or to the cut, one space and the closing words ((v)); (item, lines,
    equal). And the four papers and OPEN_TRAILS since the act's base: lines added, none removed (no sentence above a note edited)."""
    L_ = rdn('%s_ferry.txt' % ACT).split(NL)
    nj_ = jl('%s_notes.json' % ACT).get('items') or {}
    rows_ = []
    for k_, fl_ in N3_NOTES:
        it_ = nj_.get(k_) or {}
        want_ = [(_quoted(L_[n_ - 1]) or '\x00') + (N3_CLOSING if k_ == 'v' else '') for n_ in fl_]
        txt_ = (_show(PP, 'HEAD', it_.get('file') or '-') or '').replace(chr(13), '').split(NL)
        got_ = [txt_[x_['line'] - 1] if 0 < (x_.get('line') or 0) <= len(txt_) else None for x_ in it_.get('lines') or [] if x_.get('kind') != 'head']
        rows_.append((k_, len(got_), got_ == want_))
    rm_ = []
    for p_ in N3_PAPERS + ('OPEN_TRAILS.md', 'phase1.5/method/INSTRUMENTS.md'):
        ns_ = g(PP, 'diff', '--numstat', K.PRE_PP, 'HEAD', '--', p_).split()
        if not ns_ or ns_[1] != '0':
            rm_.append('%s %s' % (p_, ns_[:2] or 'UNCHANGED'))
    return rows_, rm_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R367): each write of (3) equal to the ruling's text byte for byte between its quotation marks (each line the notes bank names read
    at PLACE-papers HEAD against the ferry's line); no sentence of any paper above a note edited (the four papers, OPEN_TRAILS and
    INSTRUMENTS since the act's base: lines added, none removed); no sentence of the act says that anything of zeta, RH, GRH or Weil
    positivity on classK holds, fails or moved, outside a negation; no bank and no sentence of the entry calls a result new or the earliest of
    its kind; no figure of the navigator's workspace printed as a banked figure (the two readings [L19] names, in the act's own sentences or
    the entry's); each bank's foot carrying its grade; each matcher's control caught; the entry's last line (R367)'s INTEGRATION line composed
    from the banks; the banks' nouns in the entry; the root prompt's sentences about the entry the composer's. From the banks' last lines and
    own sentences, git, the entry's sentences and the root prompt in the answers bank."""
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
                 neg=bool(re.search(neg_, 'RH is not proved.')),
                 quote=not any(re.search(N3_LIT, x_, re.I) for x_ in _own_sentences('  T9.a  X (:1): "Many zeros are listed here, as far as\n        we know, for the first time." The bank reads on.\n'))
                 and 'The bank reads on.' in ' '.join(_own_sentences('  T9.a  X (:1): "Many zeros are listed here, as far as\n        we know, for the first time." The bank reads on.\n')),
                 nav=bool(re.search(N3_NAV_FIGS, 'The lists read 14 of 666 pairs.')) and not re.search(N3_NAV_FIGS, 'The lists read 114 of 6660 pairs.'),
                 notes=_quoted('(x) planted: "a b c"') == 'a b c' and _quoted('(x) planted: "a "b" c"') is None)
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    # ### the writes of (3) against the ruling's text; no line of a paper removed; the navigator's workspace figures
    notes_, removed_ = _notes_rows()
    navfig_ = [x[:60] for x in nsents_ + sents if re.search(N3_NAV_FIGS, x)]
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    nouns_ = [w_ for w_ in ('CP-6', 'CP-7', 'I-110', 'I-111', 'v1.34.7', 'v1.35.3', 'data/%s_notes.json' % ACT, 'data/%s_constellation_summary.txt' % ACT,
                            'data/%s_reverse_read.txt' % ACT, 'data/%s_beyond_three.txt' % ACT, 'data/%s_orders_read.txt' % ACT, 'data/%s_passed.json' % ACT,
                            'data/%s_faults_placed.txt' % ACT, 'data/%s_doors.txt' % ACT, 'data/%s_corrigendum.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not more_ and not first_ and not loc_ and len(notes_) == 5 \
        and all(o_ for _k, _n, o_ in notes_) and sum(n_ for _k, n_, _o in notes_) == 9 and not removed_ and not navfig_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence passed, a negation read, a quotation wrapped over two lines dropped and the text after it kept, a planted workspace figure caught and a longer number passed, the quotation cut taken and a cut with a mark inside refused): %s; each write of (3) at PLACE-papers HEAD equal to the ruling`s text between its quotation marks, (v)`s lines each with the closing words (relay data/%s_notes.json, data/%s_ferry.txt :14-:23): %s, %d lines of 9; the four papers, OPEN_TRAILS and INSTRUMENTS since the act`s base with a line removed: %s; over %d of the act`s own sentences and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; a sentence printing the navigator`s workspace readings of [L19] as the act`s own figure: %s; the entry`s last line (R367)`s INTEGRATION line composed from the banks (%s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            ACT, ACT, ', '.join('(%s) %d %s' % x_ for x_ in notes_), sum(n_ for _k, n_, _o in notes_), removed_ or 'NONE',
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', navfig_ or 'NONE',
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
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 (made at b756 under (R366)(3), after b756`s face), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R366)(8), N5: no kernel touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act), and no other exception: (R366) writes no kernel branch, (6)'s
    # ### README route carried whole (relay data/b756_events.txt (27)); no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b756 found them; the address scan's count from its bank (relay data/b756_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b757_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel (no kernel touched, (R367)(8), the README route carried whole; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    raise SystemExit('### b757`s a block reading an act ordinal or the read-first needles (SECTION record 28) IS A CARRIED STUB (tools/standing/carry.py v1.34.0): written for the act before use -- NOTHING COMPOSED')   # ### CARRIED STUB (tools/standing/carry.py v1.34.0): the body carried, 3 code lines, stands in the carry`s diff bank
#⟪END⟫
#⟪SECTION record 29⟫
# ### b756: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict


def _guard(f):
    """the composer's refusals before any sentence: the seven standing versions in the worklist's order, each all as wanted; the rerun's
    tables all read and its hand-read leaving none unread, its counted rows the two counts' figure; the reverse read's count the two counts'
    figure; the notes nine lines over the five writes; the orders read's four places summing to twelve and agreeing with the status lines;
    the placing's rows summing to the count's; the descriptions refused or equal, two of two."""
    if [v_ for v_, _c, _n, _w in f['vers']] != [v_ for v_, _c, _b, _n in K.STANDING_BANKS] or any(n_ != w_ for _v, _c, n_, w_ in f['vers']) \
            or [n_ for _v, _c, n_, _w in f['vers']] != [n_ for _v, _c, _b, n_ in K.STANDING_BANKS]:
        sys.exit('### THE STANDING VERSIONS ARE NOT THE WORKLIST`S SEVEN, EACH ALL AS WANTED -- NOTHING COMPOSED')
    if f['cm_tables'] != f['cm_of'] or f['cm_unread'] != 0 or f['cm_counted'] + f['cm_not'] != f['cm_tool'] or f['cm_counted'] != f['bt_moved'] or f['cm_tool'] != f['bt_tool']:
        sys.exit('### THE RERUN`S FOOT AND THE TWO COUNTS DISAGREE -- NOTHING COMPOSED')
    if f['rv_beyond'] != f['bt_beyond'] or f['rv_ctl'][0] != f['rv_ctl'][1]:
        sys.exit('### THE REVERSE READ`S COUNT AND THE TWO COUNTS DISAGREE, OR ITS CONTROLS ARE NOT ALL AS WANTED -- NOTHING COMPOSED')
    if f['notes_written'] != 9 or [n_ for _k, _f, _c, n_ in f['notes']] != [1, 1, 1, 1, 5]:
        sys.exit('### THE NOTES OF (3) ARE NOT NINE LINES OVER THE FIVE WRITES -- NOTHING COMPOSED')
    if sum(f['od']) != 12 or f['od'] != (f['om'][1], f['om'][2], f['om'][4], f['om'][5]) or f['om'][0] != f['om'][1] + f['om'][2] or f['om'][3] != f['om'][4] + f['om'][5]:
        sys.exit('### THE ORDERS READ AND THE STATUS LINES DISAGREE -- NOTHING COMPOSED')
    if f['fp_two'] != f['fc_two'] or f['fp_landed'] + f['fp_carried'] + f['fp_nocode'] + f['fp_unplaced'] != f['fp_two']:
        sys.exit('### THE PLACING`S ROWS DO NOT SUM TO THE COUNT`S -- NOTHING COMPOSED')
    if f['dr_equal'] + f['dr_refused'] != f['dr_of']:
        sys.exit('### THE DESCRIPTIONS ARE NEITHER EQUAL NOR REFUSED, EACH -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 6 order ("the FINDINGS entry titled by its objects", data/b757_ferry.txt :54):
    the notes of (3) (b757_notes); the constellation rerun (b757_constellation_summary) and the reverse read (b757_reverse_read); the orders
    placed (b757_orders_read); the CP lines (b757_passed); the tool changes (b757_faults_placed, b757_doors); nothing computed, nothing built.
    Each object's name in the heading, for the line reader. Every figure from the banks' feet, printed in digits."""
#⟪END⟫
#⟪SECTION record 31⟫
    _guard(f)
    return ('## The clearing act under (R367): the results of b756 written into the documents they bear on, %d notes of 9 (b757_notes); '
            'the constellation map run again over %d documents, %d rows moved or gone (b757_constellation_summary), and read in reverse, %d lines '
            'beyond those written (b757_reverse_read); the twelve ready orders placed, %d done, %d here, %d with the build, %d later (b757_orders_read); '
            'CP-6 and CP-7 %s (b757_passed); the tool changes, %d landed and %d carried (b757_faults_placed, b757_doors); nothing computed, nothing built' % (
                f['notes_written'], f['cm_tables'], f['cm_counted'], f['rv_beyond'], f['od'][0], f['od'][1], f['od'][2], f['od'][3], f['cp'],
                f['tc_landed'], f['tc_carried']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the reproduction run not run: its rows compute at a field, which (R367)(8) and N1 bar, so the standing arm G-RESEARCH-REPRODUCES fails at the gate and is declared so on the face; neither the whole run nor a part of it run (relay data/b757_events.txt (29)); '
            '(2) (6)`s README route carried whole, no route within (8) writing a kernel`s README, the halt proved by the kernel`s own hook and its positive control; the two descriptions sent as ruled and refused by the server for length, the seat shortening no word of the ruling`s, the four writes standing for the author`s wording (relay data/b757_doors.txt, data/b757_events.txt (27)); '
            '(3) a reading of b756`s closing cause that differs from (R367)(1)(i)`s, printed and carried, the matcher of the next act`s word not repaired, the standing change of (1)(i) carrying the ruling`s words whether or not it finds an answer (relay data/b757_events.txt (11)); '
            '(4) the orders read`s control of the label reader flipping at v1.34.8 by design, the orders bank standing as run at v1.34.7 (relay data/b757_events.txt (22)); and the constellation`s carried fall-back reading a declaration retired from main as missing, two rows counted by hand as moved (relay data/b757_events.txt (19)); '
            '(5) the navigator`s two HERE readings placed otherwise by the orders read, the author passing the placements (relay data/b757_orders_read.txt, data/b757_author_answers.txt); defects (b) to (e) entered with no clause ordering a repair beyond (R367)`s, (c) answered by the (W) regeneration before the lock (relay data/b757_defects.txt); '
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R367)(8)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b757's objects; b756's composer in git at
    b756's record tool). Its last line (R367)'s INTEGRATION line, composed from the banks' feet (_integ_line)."""
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
    v_, _vc, vn_, vw_ = f['vers'][0]
    sc_ = dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)   # ### version -> its commit
    sv_ = dict((x_[0], (x_[2], x_[3])) for x_ in f['vers'])   # ### version -> (cases, as wanted)
    ch_, pc_ = dict(K.CHAIN), dict(K.PP_CHAIN)
    nl_ = '; '.join('(%s) %s, %d line%s' % (k_, (c_ or '').split(' at ')[0], n_, '' if n_ == 1 else 's') for k_, _f, c_, n_ in f['notes'])
    pl_ = dict((k_, (c_ or '').split(' at ')[0]) for k_, _f, c_, _n in f['passed'])
    e = ['', _title(), '',
         'The results b756 left in banks were written into the documents they bear on as notes beside the text, in the ruling`s words and no others: %d lines by five PLACE-papers commits, one dated note each in THE_EPSTEIN_CONTROL_OBJECT_v0_1, SIMPLICITY_OF_RIEMANN_ZEROS, Which_Structure_Confines_v2_4_0 and THE_FINDINGS_AS_THEY_STAND_v0_7, and [L17] to [L21] at OPEN_TRAILS` end under one dated head, each line read at PLACE-papers HEAD equal to the ruling`s text between its quotation marks (relay data/b757_notes.json). The constellation map, last run at b589, was run again over the roster`s current editions: %d tables read, %d rows moved or gone by the tool, %d of them counted after the seat`s hand-read of every moved row and %d not, its controls %d of %d as wanted (relay data/b757_constellation_summary.txt, data/b757_constellation_control.txt); and the six statements the ruling lists were read in reverse over the roster, the two cuts` ledgers and the standing templates: %d lines carry them, %d of them beyond the lines (3) addresses, %d of those reading against their record in the form the ruling names (relay data/b757_reverse_read.txt), the two counts banked for the prose pass and the re-cuts and written nowhere at this act (relay data/b757_beyond_three.txt). The twelve ready orders were read at today`s tree and placed, %d done, %d here, %d with the build, %d later, and the author passed the placements; CP-6 and CP-7 were given their lines, %s, and I-110 and I-111 were entered in INSTRUMENTS (relay data/b757_orders_read.txt, data/b757_passed.json). Nothing was computed at any field and nothing was built.' % (
             f['notes_written'], f['cm_tables'], f['cm_tool'], f['cm_counted'], f['cm_not'], f['cc_ok'], f['cc_of'], f['rv_lines'], f['rv_beyond_all'], f['rv_beyond'],
             f['od'][0], f['od'][1], f['od'][2], f['od'][3], f['cp']), '',
         '*Filed at b757 on the author’s ruling `(R367)` and its amendment row (relay data/b757_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b757_corrigendum.txt`, `data/b757_rules.txt`, `data/b757_standing_v1347.txt` to `data/b757_standing_v1353.txt`, `data/b757_constellation_control.txt`, '
         '`data/b757_constellation_summary.txt` with its document banks, `data/b757_reverse_read.txt`, `data/b757_beyond_three.txt`, `data/b757_notes.json`, '
         '`data/b757_orders_read.txt`, `data/b757_instruments_draft.txt`, `data/b757_put_1.json`, `data/b757_author_answers.txt`, `data/b757_orders_moves.txt`, '
         '`data/b757_passed.json`, `data/b757_ceiling_c4.txt`, `data/b757_faults.txt`, `data/b757_faults_placed.txt`, `data/b757_doors.txt`, `data/b757_events.txt`, '
         '`data/b757_defects.txt`, `data/b757_prelock.txt`, `data/b757_pathrefusal.txt`, `data/b757_address_scan.txt`, `data/b757_touch.txt`, '
         '`data/b757_standing_figures.txt`, `data/b757_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R367)(1); relay %s, %s, PLACE-papers %s): b756 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b756’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats, no CLAIM item to print in full -- '
         'with the nine findings of the seat`s closing message for b756 entered as events, CLAIM %s, CLOSE %s, %s repeats, at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b757_corrigendum.txt). '
         'Its two repairs: the entry`s and the closing`s line for the act that follows, read from this act on as the author answers at the root, and the N4 wording of the desk and of the scores that named a bank not kept, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted (relay data/b757_standing_v1347.txt); '
         'and the lock gate carried as tools/b757_lockgate.py at relay %s. (R367)(1)(i)`s dated line giving b756`s answer appended to OPEN_TRAILS (:%s). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'],
             f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], f['corr_line'], f['corr_row'], v_, K.C1_STANDING[:8], vw_, vn_, K.C1_LOCKGATE[:8],
             K.NEXT_TRAIL_LINE, f['ver']), '',
         '**The rule this act works by** ((R367)(2)): rows (a) to (c) of relay data/b757_rules.txt -- the sentence for each outcome ratified with the ruling; the lines that carry a changed statement printed; a note at a document`s end, no cited line moving -- in force from b757, committed at relay %s.' % K.C1_RULES[:8], '',
         '**The map of dependent statements** ((R367)(4)): the rerun by tools/b757_constellation.py, carried from tools/b589_constellation.py and committed at relay %s before its run, each row`s declaration read at its pin and at its kernel`s main as the host holds it, nothing fetched; its controls as b589 ran them and the seat`s beside them, %d of %d as wanted, printed before its figures (relay data/b757_constellation_control.txt); %d of %d tables read, %d rows moved or gone by the tool, %d counted and %d not after the hand-read, %d unread (relay data/b757_constellation_summary.txt). '
         'The reverse read by tools/b757_reverse.py, committed before its run and run before the writes of (3): its controls %d of %d as wanted; %d lines carrying the six statements, %d addressed by (3), %d repaired by (1)(ii), %d the record`s own, %d beyond (3), %d of those overtaken (relay data/b757_reverse_read.txt). What the two find beyond (3): the rerun`s %d rows and the reverse read`s %d lines, banked with the count and written nowhere at this act (relay data/b757_beyond_three.txt).' % (
             K.C2_PLAN_FIRST[:8], f['cc_ok'], f['cc_of'], f['cm_tables'], f['cm_of'], f['cm_tool'], f['cm_counted'], f['cm_not'], f['cm_unread'],
             f['rv_ctl'][0], f['rv_ctl'][1], f['rv_lines'], f['rv_addressed'], f['rv_repaired'], f['rv_record'], f['rv_beyond_all'], f['rv_overtaken'], f['bt_moved'], f['bt_beyond']), '',
         '**The notes of (3)** ((R367)(3)): five PLACE-papers commits through the one-call tool with its scan, each cut by tools/b757_notes.py (relay %s, committed before its run) from the ruling`s text and read against it before the commit: %s; no sentence above a note edited (relay data/b757_notes.json).' % (
             K.C3_NOTES_GEN[:8], nl_), '',
         '**The orders and the checkpoints** ((R367)(5)): the twelve ready orders read at today`s tree by tools/b757_orders.py, committed before its run: %d done, %d here, %d with the build, %d later (relay data/b757_orders_read.txt); one put of three questions through the composer, each answered as recommended (relay data/b757_put_1.json, data/b757_author_answers.txt); on the pass the twelve status lines for this act`s trail, %d discharged and %d carried (relay data/b757_orders_moves.txt), the HERE work W-ORD-LABEL-READER done as tools/standing/ v1.34.8 at relay %s, its controls %d of %d as wanted (relay data/b757_standing_v1348.txt); '
         'the CP-6 and CP-7 lines appended to OPEN_TRAILS as passed, %s, and the two INSTRUMENTS rows %s and %s, drafted from the banks with %d of %d figures on their lines, appended as passed, %s (relay data/b757_instruments_draft.txt, data/b757_passed.json). The ceiling read again after Component 4: %s h spent and %s h remaining at the lower figures, %s h against %d h, %s (relay data/b757_ceiling_c4.txt).' % (
             f['od'][0], f['od'][1], f['od'][2], f['od'][3], f['om'][0], f['om'][3], sc_['v1.34.8'][:8], sv_['v1.34.8'][1], sv_['v1.34.8'][0],
             pl_.get('cp'), f['id_rows'][0], f['id_rows'][1], f['id_figs'][0], f['id_figs'][1], pl_.get('instruments'),
             f['c4_spent'], f['c4_lower'], f['c4_sum'], f['c4_ceiling'], f['c4_word'].lower()), '',
         '**The tool changes** ((R367)(6)), in the ruling`s order, each a version commit of its own with its controls all as wanted (relay data/b757_standing_v1349.txt to data/b757_standing_v1353.txt): [U1] the cadence of the passes, v1.34.9 at relay %s; [U2] the ledgers` writers, v1.35.0 at %s; the faults repeated in two acts or more, %d of %d rows by the acts they stand in (relay data/b757_faults.txt), %d landed as v1.35.1 at %s and v1.35.2 at %s, %d carried, %d with no code, %d unplaced (relay data/b757_faults_placed.txt); [H1]`s held part, the handoff page in the archive, v1.35.3 at %s. '
         'The README route with [B1] and [B3] carried whole: no route within (8) writes a kernel`s README, the halt proved by the kernel`s own hook and its positive control; the two descriptions sent as ruled and each refused by the server for length, %d of %d, each read back unchanged and no word shortened (relay data/b757_doors.txt).' % (
             sc_['v1.34.9'][:8], sc_['v1.35.0'][:8], f['fc_two'], f['fc_rows'], f['fp_landed'], sc_['v1.35.1'][:8], sc_['v1.35.2'][:8], f['fp_carried'], f['fp_nocode'], f['fp_unplaced'],
             sc_['v1.35.3'][:8], f['dr_refused'], f['dr_of']), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b757_stepzero.txt); step zero from %s (data/act_current.json) through b756`s carried files to its banks at %s; tools/standing/ v1.34.7 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the constellation`s tool at %s and the map`s banks at %s; the notes` tool at %s, its five writes at PLACE-papers %s to %s and its bank at %s; the orders read at %s; the put at %s; the passed writes` tool at %s and its two writes at PLACE-papers %s and %s; v1.34.8 at %s; the status lines at %s; the ceiling at %s; v1.34.9 to v1.35.3 at %s to %s, the fault count at %s and the placing at %s among them, and the README route at %s after them; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b757_prelock.txt, data/b757_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], ch_['standing'][:8], ch_['lockgate'][:8], pc_['c1pp'][:8], ch_['corr'][:8], ch_['c2first'][:8], ch_['map'][:8],
             ch_['notes_gen'][:8], pc_['pp_i'][:8], pc_['pp_v'][:8], ch_['notes'][:8], ch_['orders'][:8], ch_['put'][:8], ch_['passed_gen'][:8], pc_['pp_cp'][:8], pc_['pp_instruments'][:8],
             ch_['v1348'][:8], ch_['moves'][:8], ch_['ceiling'][:8], ch_['v1349'][:8], ch_['v1353'][:8], ch_['faults'][:8], ch_['placed'][:8], ch_['doors'][:8]), '',
         '**What this act is not**: nothing computed at any field; nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README or anchor edited and no description changed; no sentence of any paper edited, each write of (3) a note beside the text; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail, the dated lines of (1)(i) and (3)(v), the CP lines and the two INSTRUMENTS rows; no order entered; the draft held at v5.', '',
         '**The research instruments not reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run calls rows that compute at a field, the Epstein control`s and the class groups at -23 and -15 among them, which (R367)(8) and N1 bar; neither the run nor a part of it was run, and the arm fails at the gate, declared so on the face (relay data/b757_events.txt (29)).', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b757_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b757_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b757 -- %s, %s, %s, %s -- against b756’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b757_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b757_citation_check.txt, data/b757_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the reverse read and the notes of (3) read the same statements from two sides -- of the %d lines carrying the six statements, %d are those the notes of (3) stand beside and %d more stand beyond them in the form the ruling names, banked for the prose pass; the rerun`s %d counted rows are a second list of the same kind, drawn by a tool and not by a reading; none is a finding about zeta.' % (
             f['rv_lines'], f['rv_addressed'], f['rv_beyond'], f['cm_counted']), '',
         '**Carried to:** %s, per (R367)(7), as the author answers the one question at the root: the build as b757 (the four branches of the criterion kernel joined under a tag on main; T0 and T1; the criterion over the wider strip; the modulus-24 lemma; the written proofs of the class-number-3 law and of the closed form), or another the author names; what the rerun and the reverse read find beyond (3), for the prose pass and the re-cuts; the README route with [B1] and [B3] and the two descriptions, for the author`s wording; the one fault the placing carried; the reproduction run, not run at this act; the ten orders carried with the build and later; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH, GRH or Weil positivity on classK holds or fails, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b756_body():
    """b755's paragraphs over b755's objects, kept for the record and not called (b756, Component 6): held as text, their names b755's
    locals, which the gate's report dry (tools/standing/reportdry.py unbound) read as live unbound globals beside _finding_text's own (defect (j))."""
    return r"""
    e = [
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b757_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b757_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b757_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b757_zeros_from_primes_59.txt, data/b757_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b757 on the author’s ruling `(R367)` and its two amendment rows (relay data/b757_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b757_corrigendum.txt`, `data/b757_carried_faults.txt`, `data/b757_standing_v1346.txt`, `data/b757_walk.txt`, `data/b757_coeffs_controls.json`, `data/b757_literature.txt`, '
         '`data/b757_cand_a.txt` to `data/b757_cand_l_plant.txt`, `data/b757_candidates.txt`, `data/b757_ceiling.txt`, `data/b757_registrations.txt`, `data/b757_roots_59.txt`, '
         '`data/b757_list_59.txt`, `data/b757_list_59_controls.txt`, `data/b757_zeros_from_primes_59.txt`, `data/b757_recur_59.txt`, `data/b757_recur_control.txt`, '
         '`data/b757_census_from_primes.txt`, `data/b757_l16.json`, `data/b757_put_1.json`, `data/b757_put_2.json`, `data/b757_author_answers.txt`, `data/b757_events.txt`, '
         '`data/b757_defects.txt`, `data/b757_prelock.txt`, `data/b757_pathrefusal.txt`, `data/b757_reproduce.txt`, `data/b757_address_scan.txt`, `data/b757_touch.txt`, '
         '`data/b757_standing_figures.txt`, `data/b757_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R367)(1), (2); relay %s, %s, PLACE-papers %s): b756 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b756’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b757_corrigendum.txt). Its three repairs: the lock gate carried as tools/b757_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b757_standing_v1346.txt; the amendment row 1). '
         'The open items of b756`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b757_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R367)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b757_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b757_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b757_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b757_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R367)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b757_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b757_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R367)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b757_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes’ phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b757_candidates.txt, data/b757_cand_a.txt to data/b757_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R367)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b757_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b757_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b757_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b757_zeros_from_primes_59.txt, data/b757_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b757_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b757_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R367)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b757_defects.txt (l)); its generator committed at relay %s before its run (relay data/b757_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R367)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b757_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R367)(8)): the price table at step zero from banked timings where a bank held one (relay data/b757_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b757_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b757_stepzero.txt); step zero from %s (data/act_current.json) through b756`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]’s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b757_prelock.txt, data/b757_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b757_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b757_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b757_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b756: [U3] in force, the counter's line as it prints (its event in data/b756_events.txt (22))
         '**The standing arms**: the four figures at b757 -- %s, %s, %s, %s -- against b756’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b757_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b757_citation_check.txt, data/b757_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R367)(8), as the author answers the one question at the root: the clearing act as b757 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]’s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b757 with the clearing act after it; defects (b), (e) and the tools’ (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH, GRH or Weil positivity on classK holds or fails, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)
"""


def _finding_text_b756():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b757's objects; b756's composer in git at b756's record tool): the ledger writes; the notes of (3); the map;
    the twelve status lines of (5)(i) written here and nowhere before, the open-orders line from tools/standing/orders.py's output over the
    trail at HEAD with them; the checkpoints and the instruments; the tool changes; the ceiling; the standing versions."""
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
    # ### (R366)(5)(i) on the author's pass: the twelve status lines of relay data/b756_orders_moves.txt, written by this trail and nowhere before,
    # ### read through the orders tool with the trail at HEAD: the two DISCHARGED out of the open list, the ten CARRIED in it
    mv_ = rdn('%s_orders_moves.txt' % ACT)
    two = [l_ for l_ in mv_[mv_.find('#### THE LINES BEGIN'):mv_.find('#### THE LINES END')].split(NL)[1:] if l_.strip()]
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    dis_ = [re.match(r'^`(W-ORD-[A-Z0-9-]+)`', l_).group(1) for l_ in two if ' DISCHARGED, ' in l_]
    car_ = [re.match(r'^`(W-ORD-[A-Z0-9-]+)`', l_).group(1) for l_ in two if ' CARRIED, ' in l_]
    if len(two) != 12 or len(dis_) != f['om'][0] or len(car_) != f['om'][3] or set(dis_) & set(op) or not set(car_) <= set(op):
        sys.exit('### THE TRAIL: THE TWELVE STATUS LINES NOT READ AS PLACED BY THE ORDERS TOOL -- NOTHING COMPOSED')
    pl_ = dict((k_, (c_ or '').split(' at ')[0]) for k_, _f, c_, _n in f['passed'])
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R367) ratified.** Its components as the ferry orders them (relay data/b757_ferry.txt), with its amendment row (relay data/b757_amendments.json), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b756’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md (1)(i)`s dated line (:%s), (3)(v)`s five lines under one dated head (%s), the CP-6 and CP-7 lines (%s); INSTRUMENTS I-110 and I-111 (%s); the four dated notes of (3)(i) to (iv); no order entered; no sentence of a paper edited; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.NEXT_TRAIL_LINE, f['notes'][4][2].split(' at ')[0], pl_.get('cp'), pl_.get('instruments')), '',
             '**The notes of (3):** %d lines of 9 in the ruling`s words, each read at PLACE-papers HEAD against its text (relay data/b757_notes.json).' % f['notes_written'], '',
             '**The map:** the constellation rerun %d of %d tables, %d rows moved or gone by the tool, %d counted after the hand-read, its controls %d of %d (relay data/b757_constellation_summary.txt); the reverse read %d lines carrying the six statements, %d beyond (3) in the form the ruling names, its controls %d of %d (relay data/b757_reverse_read.txt); banked and written nowhere at this act (relay data/b757_beyond_three.txt).' % (
                 f['cm_tables'], f['cm_of'], f['cm_tool'], f['cm_counted'], f['cc_ok'], f['cc_of'], f['rv_lines'], f['rv_beyond'], f['rv_ctl'][0], f['rv_ctl'][1]), '',
             '**The orders acted** ((R367)(5)(i), on the author’s pass): %d done, %d here, %d with the build, %d later (relay data/b757_orders_read.txt, data/b757_orders_moves.txt):' % f['od'], '']
    rows_ += two + ['',
             '**The checkpoints and the instruments** ((R367)(5)(ii), (iii)): CP-6 and CP-7 %s; I-110 and I-111 entered (relay data/b757_passed.json).' % f['cp'], '',
             '**The tool changes** ((R367)(6)): %d landed (%s), %d carried, the README route with [B1] and [B3] (relay data/b757_doors.txt); the faults of two acts or more %d, landed %d, carried %d, no code %d (relay data/b757_faults_placed.txt).' % (
                 f['tc_landed'], ', '.join(f['vers6']), f['tc_carried'], f['fp_two'], f['fp_landed'], f['fp_carried'], f['fp_nocode']), '',
             '**The ceiling:** after Component 4, %s h against %d h, %s (relay data/b757_ceiling_c4.txt).' % (f['c4_sum'], f['c4_ceiling'], f['c4_word'].lower()), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The standing versions:** %s (relay data/b757_standing_v1347.txt to data/b757_standing_v1353.txt); HANDOFF.md regenerated once by tools/standing/handoff.py before the gate, at relay %s.' % (
                 '; '.join('%s %d of %d' % (v_, w_, n_) for v_, _c, n_, w_ in f['vers']), (K.HANDOFF_COMMIT or 'NOT MADE')[:8]), '',
             '**The instruments not reproduced:** the run not run at this act, its rows computing at a field, which (R367)(8) bars; G-RESEARCH-REPRODUCES declared failing on the face (relay data/b757_events.txt (29)).', '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b757_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b757_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b757 `%s` (previous `%s`, b756’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b757_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b757_standing_v1353.txt); the standing '
             'report tool (relay data/b757_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel touched, (6)`s README route carried whole; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b757 found them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root with the two ledgers’ cuts beside it (the ferry`s Component 6), HANDOFF.md among its files ([H1], v1.35.3), its file named in the closing by its name, bytes and hash and its folder by role (relay data/b757_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b756’s %s, %s, %s, %s (relay data/b757_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b757_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b756():
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
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b757 found them, the six; MEASURED off the six kernels` refs/heads.'),
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
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b756-closing, push-b756-preroot, push-b756-record; PLACE-papers push-b756-preroot, push-b756-record; each local, by name, through the one-call tool, after the --merged listing (data/b757_stepzero.txt :62-:69).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written this act ((R367)(7)`s (W) list names FINDINGS, OPEN_TRAILS, INSTRUMENTS and the four documents of (3) in PLACE-papers, and no other ledger).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R367)(1): FINDINGS :15346 (relay data/b757_corrigendum_landing.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R367)(1): row (76).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R367)(8)).'),
    ('notes of (3) written in the ruling`s words', 9, 9, 'lines', '### (R367)(3)(i)-(v): four notes and five trail lines by five PLACE-papers commits, each cut from the ruling`s text and read against it before its commit (relay data/b757_notes.json).'),
    ('documents read by the constellation rerun', 39, 39, 'documents', '### (R367)(4)(i): each table`s rows read at their pins and at their kernels` mains as the host holds them, nothing fetched (relay data/b757_constellation_summary.txt).'),
    ('constellation rows moved or gone', 7, 7, 'rows', '### (R367)(4)(i): after the hand-read of 12 rows, 7 counted and 5 not, 0 unread (relay data/b757_constellation_summary.txt).'),
    ('reverse-read lines beyond those written', 4, 4, 'lines', '### (R367)(4)(ii), (iii): banked with the count and written nowhere at this act (relay data/b757_reverse_read.txt; data/b757_beyond_three.txt).'),
    ('orders placed', 12, 12, 'orders', '### (R367)(5)(i): 1 done, 1 here, 5 with the build, 5 later, on the author`s pass (relay data/b757_orders_read.txt; data/b757_orders_moves.txt).'),
    ('checkpoint lines written', 2, 2, 'lines', '### (R367)(5)(ii): CP-7 and CP-6 on the author`s pass (relay data/b757_passed.json).'),
    ('INSTRUMENTS rows added', 2, 2, 'rows', '### (R367)(3)(vi), (5)(iii): I-110 and I-111 on the author`s pass (relay data/b757_passed.json).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R367) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: not run at b757, the run computing at a field where (R367)(8) bars it (data/b757_events.txt (29)); MEASURED off data/b757_reproduce.json, absent.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### the tools` runs over the record, none at a field ((R367)(8)): the seven standing versions` controls, the constellation`s controls and summary, the reverse read, what the two find beyond (3), the orders read, the drafts, the status lines, the ceiling, the fault count, its placing, the README route, the probe-path refusal, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### none: (R367) registers no rule at this act (the rule of (2) stands in data/b757_rules.txt, in force from b757), and no data/b757_registrations.txt is written; MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2): no registered object this act, nothing computed at any field; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R367)(8)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R367)(1), (5)(i), (6) and the amendment row 1: tools/standing/ v1.34.7 to v1.35.3, each by a version commit of its own with its controls in its bank (data/b757_standing_v1347.txt to data/b757_standing_v1353.txt); MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b757_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, and the gh reads and the two refused description writes under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b756: no registered object and no figure bank ((R366)(8): nothing computed at any field)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b757_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b757_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1347', 'standing_v1348', 'standing_v1349', 'standing_v1350', 'standing_v1351', 'standing_v1352',
                                               'standing_v1353', 'constellation_control', 'constellation_summary', 'reverse_read', 'beyond_three', 'orders_read',
                                               'instruments_draft', 'orders_moves', 'ceiling_c4', 'faults', 'faults_placed', 'doors', 'pathrefusal', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b757_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b757_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b757_registration_%s.txt -- b757, THE CLEARING ACT: b756 AT ITS WEIGHT AND ITS CORRIGENDUM; THE RULE OF (2); "
                             "THE NOTES OF (3) IN THE RULING'S WORDS; THE CONSTELLATION MAP RUN AGAIN AND READ IN REVERSE; THE TWELVE ORDERS PLACED; "
                             "CP-6 AND CP-7 AND TWO INSTRUMENTS ROWS; v1.34.7 TO v1.35.3; NOTHING COMPUTED, NOTHING BUILT, UNDER (R367)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b756's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b757: b756's lines read banks this
act does not write, and are not carried; the lines are b757's: tools/standing/ v1.34.7 to v1.35.3 by their controls, the constellation rerun
and the reverse read by theirs (CERTIFIED); the notes of (3) in the ruling's words, the twelve orders placed on the author's pass, and the CP
lines with the two INSTRUMENTS rows as passed (REGISTERED); the README route and the two descriptions carried whole, the reproduction run not
run, and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b756's lines, each from the record tool's figures over b756's banks (REC._figs), the record's guard first
    REC._guard(f)
    ch_ = dict(K.CHAIN)
    # ------------------------------------------------------------------ REGISTERED: (R366)(3), the notes in the ruling's words
    sa = seat('%s_notes.json' % ACT, '"confirm"')
    keys['NOTES'] = ('REGISTERED -- THE NOTES OF (3) IN THE RULING`S WORDS: %d lines of 9 by five PLACE-papers commits (%s), each cut from the ruling`s text by the notes` tool at relay %s, committed before its run, and read against it before the commit. SOURCE %s.' % (
        f['notes_written'], ', '.join((c_ or '').split(' at ')[0].replace('PLACE-papers ', '') for _k, _f, c_, _n in f['notes']), K.C3_NOTES_GEN[:8], sa['text']))
    seats.append(sa)
    # ------------------------------------------------------------------ REGISTERED: (R366)(5)(i), the twelve orders on the author's pass
    sb = seat('%s_orders_moves.txt' % ACT, '**TWELVE STATUS LINES: ')
    keys['ORDERS'] = ('REGISTERED -- THE TWELVE ORDERS PLACED ON THE AUTHOR`S PASS: %d done, %d here, %d with the build, %d later; %d status lines discharged and %d carried, written by the trail at the record; the orders read at relay %s and the status lines at %s. SOURCE %s.' % (
        f['od'][0], f['od'][1], f['od'][2], f['od'][3], f['om'][0], f['om'][3], ch_['orders'][:8], ch_['moves'][:8], sb['text']))
    seats.append(sb)
    # ------------------------------------------------------------------ REGISTERED: (R366)(5)(ii), (iii), the CP lines and the two INSTRUMENTS rows (the name the template appends)
    sk = seat('%s_passed.json' % ACT, '"confirm"')
    keys['PASSED'] = ('REGISTERED -- CP-6 AND CP-7 AND THE TWO INSTRUMENTS ROWS, AS PASSED: the CP lines %s at %s; %s and %s at %s, drafted with %d of %d figures on their lines; the passed writes` tool at relay %s. SOURCE %s.' % (
        f['cp'], (f['passed'][0][2] or '').split(' at ')[0], f['id_rows'][0], f['id_rows'][1], (f['passed'][1][2] or '').split(' at ')[0], f['id_figs'][0], f['id_figs'][1],
        ch_['passed_gen'][:8], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.34.7 to v1.35.3 ((R366)(1), (5)(i), (6)), by their controls
    sv = seat('%s_standing_v1353.txt' % ACT, '**v1.35.3: CONTROLS ')
    keys['VERSIONS'] = ('CERTIFIED -- tools/standing/ v1.34.7 TO v1.35.3, each by a commit of its own moving VERSION, its controls all as wanted: %s. SOURCE %s.' % (
        '; '.join('%s at relay %s, %d of %d' % (v_, dict((x_[0], x_[1]) for x_ in K.STANDING_BANKS)[v_][:8], w_, n_) for v_, _c, n_, w_ in f['vers']), sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: (R366)(4)(i), the constellation rerun by its controls
    sl = seat('%s_constellation_control.txt' % ACT, '**THE CONTROLS: ')
    keys['MAP'] = ('CERTIFIED -- THE CONSTELLATION RERUN BY ITS CONTROLS: %d of %d as wanted, printed before its figures; %d of %d tables read, %d rows moved or gone by the tool, %d counted after the hand-read, %d not, %d unread; the tool at relay %s, committed before its run. SOURCE %s.' % (
        f['cc_ok'], f['cc_of'], f['cm_tables'], f['cm_of'], f['cm_tool'], f['cm_counted'], f['cm_not'], f['cm_unread'], K.C2_PLAN_FIRST[:8], sl['text']))
    seats.append(sl)
    # ------------------------------------------------------------------ CERTIFIED: (R366)(4)(ii), the reverse read by its controls (the name the template appends)
    sw = seat('%s_reverse_read.txt' % ACT, '**THE REVERSE READ: CONTROLS ')
    keys['REVERSE'] = ('CERTIFIED -- THE REVERSE READ BY ITS CONTROLS: %d of %d as wanted, run before the writes of (3); %d lines carrying the six statements, %d addressed by (3), %d beyond (3), %d of those in the form the ruling names. SOURCE %s.' % (
        f['rv_ctl'][0], f['rv_ctl'][1], f['rv_lines'], f['rv_addressed'], f['rv_beyond_all'], f['rv_beyond'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ HELD: (R366)(6), the README route and the two descriptions, carried whole
    se = seat('%s_doors.txt' % ACT, '**THE DESCRIPTIONS: ')
    keys['DOORS'] = ('HELD -- THE README ROUTE AND THE TWO DESCRIPTIONS, CARRIED WHOLE: [B1] and [B3] halted, no route within (8) writing a kernel`s README; the two descriptions sent as ruled, %d of %d refused by the server for length, each read back unchanged, no word shortened; the tool at relay %s. SOURCE %s.' % (
        f['dr_refused'], f['dr_of'], dict(K.CHAIN)['doors'][:8], se['text']))
    seats.append(se)
    # ------------------------------------------------------------------ HELD: the reproduction run, not run ((R366)(8), N1)
    s7 = seat('%s_events.txt' % ACT, '    (29) ')
    keys['REPRO'] = ('HELD -- THE REPRODUCTION RUN, NOT RUN: its rows compute at a field, which (R367)(8) and N1 bar; neither the run nor a part of it run; G-RESEARCH-REPRODUCES declared failing on the face. SOURCE %s.' % s7['text'])
    seats.append(s7)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R366)(8))
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['VERSIONS', 'MAP', 'REVERSE']), ('REGISTERED', ['NOTES', 'ORDERS', 'PASSED']), ('HELD', ['DOORS', 'REPRO', 'HELD'])]
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
