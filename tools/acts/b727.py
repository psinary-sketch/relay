# -*- coding: utf-8 -*-
# b727 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R337)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R337)(2) repair it carries. Edited by the Edit tool. Carried at b727 by tools/b727_fold.py (`carry`) from tools/acts/b726.py,
# b726`s names substituted; the citation`s sections adopted from tools/b727_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b726`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b726`s carried till
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
# ### b727, Component 1 (the Edit tool): THE c1 ROUTE FOR b726'S WEIGHT LINE AND ITS CORRIGENDUM, (R337)(1)-(2). Carried from b726's
# ### override and rewritten here against b726's own banks: the closing's lines by needle, the events (10), the defects (28), the refusals
# ### (9 at e2246a8e), the v1.6.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = '9fac0a1d'          # ### b726's closing commit: its refusal bank read at it
C1_NOTED = '2026-10-31'
C1_CORRIGENDA_LAST = 46
C1_V170 = 'b727_standing_v170.txt'
C1_WEIGHT_HEAD = '*Appended 2026-10-31 by b727 to b726’s entry (:%d), under `(R337)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## Which Structure Confines v2.4.0 carrying the zeta_K figure and the closed form'
C1_TRAIL_NEEDLE = '### b726 — lane two, act one hundred and fifty-three, the wave 1 act under (R336)'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


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
    for l in _c1_rd('b726_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b726_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b726_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b726_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b726_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b726_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b726_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    (nc2,), l_c2 = _c1_fl('b726_c2.txt', r'CERTIFICATES COMPILED AT (\d+) OF 18 BY decide \+kernel, EACH DEPENDING ON NO AXIOM', 'the certificates')
    (nrow,), l_mc = _c1_fl('b726_mechanisms.txt', r'THE MECHANISM TABLE: (\d+) ROWS', 'the mechanism table')
    fd = _c1_rd('b726_frontdoors.txt')
    nitems, nload = len(re.findall(r'(?m)^  \[\d+\] ', fd)), len(re.findall(r'(?m)^  \[\d+\] LOAD-BEARING', fd))
    sc = json.load(open(os.path.join(D, 'b726_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = sum(1 for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD')
    if held != 8:
        sys.exit('### data/b726_scores_close.json: %d HELD -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b726_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b726_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 17)) or len(dr) != 22:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b726 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b726_closing.txt):* “%s” (data/b726_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b726_steps.json, the record and closing rows). As its rows read: the C2 certificates compiled at %s of 18 fields by '
            'decide +kernel, each depending on no axiom, on c2-b725, no main and no tag, D=-267 and D=-427 stopped under the hold and D=-403 not dispatched (data/b726_c2.txt :%d); '
            'the edition v2.4.0 of Which Structure Confines on PLACE-papers main, beside v2.3.1, unpublished; the front-door list at %d items, %d LOAD-BEARING, assembled and not applied '
            '(data/b726_frontdoors.txt); the mechanism table at %s rows, its order open for the fourth (data/b726_mechanisms.txt :%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s '
            'pre-push and %s of %s post-push, NOT CLEAN both (:%d, :%d); the counter CLAIM %s, CLOSE %s, REPEAT %s of %s (:%d), where the entry and the trail print CLAIM 5, CLOSE 27, REPEAT 12 '
            'of 32, composed before events (11)-(16); the scores 8 of 8 HELD (data/b726_scores_close.json). The root %s over %s banks, chained from %s (data/b726_act_root.json; :%d), the '
            'chain AGREE b624-b726; %s prompts answered (:%d); %d events in data/b726_events.txt, rows (1)-(%d); %d defects, (a)–(v) (data/b726_defects.txt). Nothing deposited, nothing '
            'published; the corrigendum for these rows follows, under `(R337)`(1)-(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, nc2, l_c2, nitems, nload, nrow, l_mc, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                cc, cd, rp, rn, l_cn, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b726's bank at its closing commit, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '23:32:19Z', 'defect (c)'), (2, 'PIPE', '02:19:03Z', 'event (7)')]
C1_CORR_TITLE = ('## Corrigendum to b726’s record (relay data/b726_events.txt rows (1)-(16) and data/b726_defects.txt): sixteen events and twenty-two defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; G-ACT-CURRENT and G-BRANCHES-BANKED repaired at tools/standing/ v1.7.0, the answers pair and the answer check outside the lock’s hash set and N4’s read, '
                 'each controlled on b726’s and b725’s banks, under (R337)(1)-(2)')


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
    rl = _c1_git('show', '%s:data/b726_hook_refusals.txt' % C1_PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if at[:5] not in src and ('REFUSED BY THE HOOK (%s' % kind) not in src and 'refused by the hook' not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b726_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.7.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=[])
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(16)', sorted(ev) == list(range(1, 17))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 22', len(dr) == 22), ('the refusals 2, each answered as listed', len(rl) == 2 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.7.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.7.0
C1_EV_EXTRA = {1: '; this act’s face writes the arm’s words', 2: '; repair (actcur)', 3: '; repair (branches)', 9: '; repair (answers), the separate read standing until it landed',
               12: '; the arms named in event (9) are not in the suite', 14: '; the two plants still inert, carried', 15: '; the rule stands'}
C1_CLASSES = (
    ('actcur', 'G-ACT-CURRENT (`(R337)`(2), event (2))', 'the worklist’s REPAIRED_TOOLS is read from data/act_current.json’s shared_edits, the one hand list, and the arm reads that list against the '
               'shared tools git shows changed, so a repair recorded in one of two lists cannot pass or fail silently'),
    ('branches', 'G-BRANCHES-BANKED (`(R337)`(2), event (3))', 'the citation bank keeps its first banking’s time through a re-bank (first_at) and the arm reads that against the first delete; the arm’s NEG plant is a '
                 'pattern over the bank, where the literal had gone inert'),
    ('answers', 'the answers pair and the answer check (`(R337)`(2), b725 event (4))', 'data/bNNN_author_answers.txt, .json and data/bNNN_answer_check.txt, the check’s own bank, stand outside the lock’s hash set and N4’s read, '
                'one list (tools/standing/act.py post_lock_appended), the lock gate printing it by name; b725’s event (4) replayed reads no refutation'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b726’s events bank (relay data/b726_events.txt) carries sixteen rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-two lettered rows, (a)-(v), each tagged in its own bracket (%s); its refusal bank two lines at b726’s closing commit %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_PREV_CLOSE), '']
    L += ['', '**The repairs of `(R337)`(2), at tools/standing/ v1.7.0, each with a control on b726’s and b725’s banks, failing on the route before the repair '
          'and passing after, both instances printed** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b726’s events (1)-(16):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_]).split(': ', 1)[0]
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b726_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b726’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b726_defects.txt; %s; %s; %s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c))]
    L += ['', '**b726’s refusals** (relay data/b726_hook_refusals.txt at %s, one a line): ' % C1_PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (sixteen events, twenty-two defects), as b726’s closing prints it (relay data/b726_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b727 on the author’s ruling `(R337)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b727.py) from '
          'b726’s events, defects and refusal banks read unedited, and the v1.7.0 controls bank; banked as relay `data/b727_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b726’s record; no sealed tool, face, trail or root-named bank of b726 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b727 -- THE CORRIGENDUM FOR b726, (R337)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b726_events.txt rows (1)-(16), data/b726_defects.txt 22 rows, data/b726_hook_refusals.txt 2 '
             'lines at %s; data/%s (the v1.7.0 controls); the corrigenda bank`s last row (%d).' % (C1_PREV_CLOSE, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 16, DEFECTS 22 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.7.0: G-ACT-CURRENT, '
               'G-BRANCHES-BANKED, THE ANSWERS PAIR ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b726 at its weight after its entry, and the corrigendum for b726, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.7.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b727, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b727 ran three
# ### ((R337)(4)(iii)-(iv), N1), rowed in data/b727_dispatch_rows.json. Replaced for b727 alone; the arms' names stand, their plants on b727's rows.
#⟪OVERRIDE checks 1128 1140⟫
def rebuild_wf_ok(S):
    """(R336)(7), as b726 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
#⟪OVERRIDE checks 1143 1158⟫
def runner_ok(S):
    """(R337), N1, b727: no runner dispatch this act -- the rows empty, the worklist's runs none, the dispatch cap zero, no dispatch-rows bank. VACUOUS on run ids by the order."""
    return (S['drows'] or []) == [] and K.EF_RUNS == () and K.MAX_DISPATCHES == 0 and not os.path.exists(os.path.join(D, 'b727_dispatch_rows.json'))
#⟪END⟫
#⟪OVERRIDE checks 1169 1172⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        pu_ = [j for j, r in enumerate(rows) if r.get('kind') == 'push' and r.get('sha') == d_.get('sha')]
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(pu_) == 1 and len(rd_) == 1 and pu_[0] < i_ < rd_[0]
#⟪END⟫
#⟪OVERRIDE checks 1175 1175⟫
    return (not mem or all(int(r.get('free_mb') or 0) >= K.HOLD for r in mem)) and order \
#⟪END⟫
# ### b727, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b726's record has eighteen
#⟪OVERRIDE checks 982 982⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 17)) \
#⟪END⟫
# ### b727, Component 4 (the Edit tool): b727's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b726's override of checks 526 -- no registration commit -- removed: b727
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 753 753⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b727_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b727, Component 6 (the Edit tool): b727's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b726's wording
#⟪OVERRIDE checks 778 778⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b727, Component 4 (the Edit tool): b726's overrides of checks 1516 and 1659 (hook.py edited by b726's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b727 as it stands
# ### b727, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 987 987⟫
        and 'data/b727_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b727, Component 4 (the Edit tool): b726's override of checks 1476-1482 (one ERRATA entry at b726's (R336)(5)) removed -- (R337)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b727 as it stands
# ### b727, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b726's step-zero wording; b727's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 744 744⟫
        and 'port-b707' in z and 'KEPT as banked: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b727, Component 4 (the Edit tool): G-RUNNER-READ's plant on b727's dispatch rows -- run 2's axiom lines carrying sorryAx (b726's
# ### plant read the lv rows' closure log, which b727 does not write)
#⟪OVERRIDE checks 1690 1690⟫
     lambda S: runner_ok(S), lambda S: put(S, 'drows', [dict(kind='dispatch')])),
#⟪END⟫
# ### b727, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b727, Component 6 (the Edit tool): the fold bank was b726's own route
# ### (tools/b726_fold.py); b727's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b727_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1007 1007 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b726.py -> tools/acts/b727.py' in (rd('b727_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b727, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b727_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 258 265 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b727_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b727, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R337): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 339 340⟫
    rows = [l for n_ in ('b727_defects.txt', 'b727_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R337) Component 4, the act`s events and defects together; relay data/b727_defects.txt, data/b727_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b727, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b727's orders are (R337)(10)'s six,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-CHAIN-PAGE-LLM-LINE entered by (R337)(3) [34]-[35],',
    '        W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b727, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b726's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b727_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b727_registration_%s.txt' % __import__('b727_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b727, Component 4 (the Edit tool, before the face): b726's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b727, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b727's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's two branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b727, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R337)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b727 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b727, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b726's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b727 scorer reads; the needles set to the banks b727's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 905 906 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_FIGURE_BANKS' in n and '_first_add(' in n \
        and "_onset_mass_control.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b727, Component 3 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b726's ruling's form; (R337)(5) writes "; kept as banked." naming no branch
# ### (data/b727_ferry.txt :22), so the arm failed on the act's real deletes; read as written, port-b707 still out of the deletes (defect (u))
#⟪OVERRIDE checks 766 769 REPAIR (needle)⟫
    # ### (R336)(9) wrote "port-b707 kept;" and (R337)(5) writes "; kept as banked."; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or '; kept as banked.' in S['ferry']) \
#⟪END⟫
# ### b727, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b727_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b727, Component 3 (the Edit tool): (R337)(4) orders one ERRATA entry: the arm's template form (no entry) replaced for this act
#⟪OVERRIDE checks 1480 1486⟫
def differs_errata_ok(S):
    """(R337)(4): one ERRATA entry, naming the sitting -- ERRATA.md at HEAD its blob at the act's base with the entry appended and nothing before it changed, the id once at its line; no
    DIFFERS entry; the weight line and the corrigendum at FINDINGS in Component 1's PLACE-papers commit, FINDINGS the one file there."""
    now, pre = (S['errata_pp_now'] or b'').decode('utf-8'), (S['errata_pp_pre'] or b'').decode('utf-8')
    return bool(pre) and now.startswith(pre.rstrip(NL)) and now.count('## %s ' % K.ERRATA_ID) == 1 and not S['differs'] and K.DIFFERS_LINE is None \
        and now.split(NL)[K.ERRATA_LINE - 1].startswith('## %s ' % K.ERRATA_ID) and S['files']['c1pp'] == ['FINDINGS.md'] and 'weight' in fline(S, K.WEIGHT_LINE).lower()
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvw'))   # ### (a)-(w), entered before the lock, every one the seat's (data/b727_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b727_corrigendum.txt', 'data/b727_standing_v170.txt', 'data/b727_sitting.txt', 'data/b727_sitting.json',
                  'data/b727_zenodo_readback.json', 'data/b727_reproduce.txt', 'data/b727_reproduce.json', 'data/b727_address_scan.txt',
                  'data/b727_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b727 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R337)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b727_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R337)(2)-(4), Component 3 (b727's keys over b727's objects): the components' order by ancestry; v1.7.0's controls; the sitting's record, its Zenodo
        # ### read-backs, the kernels it wrote; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### b725's registrations at their commit and at HEAD; b727 registers nothing
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v160', K.STANDING_COMMIT, K.C1_STANDING), ('v160_c1', K.C1_STANDING, K.C1_RELAY),
                                 ('c1_corr', K.C1_RELAY, K.C1_CORR), ('corr_c3', K.C1_CORR, K.C3_RELAY[0]), ('c3_c2', K.C2_RELAY, K.C3_RELAY[0]))),
        v170=rd('b727_standing_v170.txt'), sitting=rd('b727_sitting.txt'), sittingj=jl('b727_sitting.json'), zenback=jl('b727_zenodo_readback.json'),
        frontdoors=rd('b726_frontdoors.txt'), frontdoors_pre=_s(blob(ROOT, '%s:data/b726_frontdoors.txt' % PRE['relay'])),
        ws_now=_s(blob(PP, 'HEAD:day1/Which_Structure_Confines.md')) or None, ws_pre=_s(blob(PP, '%s:day1/Which_Structure_Confines.md' % PRE['pp'])) or None,
        ws_edition=_s(blob(PP, 'HEAD:day1/Which_Structure_Confines_v2_4_0.md')) or None, ws_edition_pre=_s(blob(PP, '%s:day1/Which_Structure_Confines_v2_4_0.md' % PRE['pp'])) or None,
        sit_repos=dict((n_, dict(head=gs(r_, 'rev-parse', 'main'), remote=gs(r_, 'rev-parse', 'origin/main'),
                                 files=sorted(x for x in gs(r_, 'diff', '--name-only', p_, 'main').split(NL) if x.strip()), tags=[x for x in gs(r_, 'tag', '--merged', 'main', '--no-merged', p_).split(NL) if x.strip()]))
                       for n_, r_, p_ in K.SITTING_REPOS),
        drows=[], reproduce=rd('b727_reproduce.txt'), reproducej=jl('b727_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b727_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read N1's nothing (no dispatch rows this act); the wave 1 kernels' rebuild-b721 branches as b726 left them
        rebuild=None, rebuild_rows=[], rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               c2=_ct(ROOT, K.C2_RELAY), c3=_ct(ROOT, K.C3_RELAY[0]),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.C2_RELAY),
                   c3=[f_ for c_ in K.C3_RELAY for f_ in files_of(ROOT, c_)], v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b727's read-first bank's items by path, as its step zero wrote them (data/b727_readfirst.txt :12-:27)
READFIRST_NEEDLES = ('relay data/b726_closing.txt |', 'relay data/b726_events.txt |', 'relay data/b726_defects.txt |', 'relay data/b726_frontdoors.txt |',
                     'relay data/b726_zenodo_read.json |', 'relay data/b721_frozen_line_drafts.txt |', 'relay data/b723_axiom.txt |',
                     'PLACE-papers day1/Which_Structure_Confines.md |', 'PLACE-papers OPEN_TRAILS.md |', 'the author`s word of 2026-10-31 passing PART C |'.replace('`', "'"))
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R337)(1)-(2))', 'SITTING ((R337)(3)-(4))', 'DEPOSIT DESCRIPTIONS ((R337)(3) PART C)', 'NAME AND ADDRESS ((R337)(5))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (79 = 79 + 0, data/b727_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 79 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b726's figures, read at FINDINGS :11911 as Component 1 landed them
    return landed(S, 0, ['b726 AT ITS WEIGHT', 'suite 111 of 116; root 720308d8bd702563…', 'the closing’s 9fac0a1d', '22 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b727's title in the ferry's Component 3 form adjusted to what the act did (the record tool's _title over the banks)
TITLE_NEEDLES = ('## The release sitting: ', ' items applied, ', ' struck, ', ' not applied', '; the four checkpoint kernels’ READMEs and descriptions at their compiled statements',
                 '; the LLM line at ', ' papers and ', ' READMEs', ' deposit descriptions noted', '; the edition’s byline restored')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R337)(1)-(2): the generated entry for b726's sixteen events and twenty-two defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(16), the defects by the one lettering ((a)-(v)), no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 5, CLOSE 33 over 38, REPEAT 14); the repairs at tools/standing/ v1.7.0 by their controls
    bank; the corrigenda bank appended at row (47) and nothing before it changed; in Component 1's commits (the figures read from
    data/b727_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 22 and len(items) == j.get('items') == 38 and j.get('row') == 47 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 38 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 5 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 14 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.7.0' and (j.get('repairs') or {}).get('bank') == 'data/b727_standing_v170.txt' \
        and (j.get('notes') or []) == [] \
        and '  (47) ' in S['corrigenda'] and '  (48) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b727_rules.txt and data/b728_rules.txt, by form in (R337)(8)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b726's form, its names b727's); no author's word of b727 orders a rules row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b727_rules.txt')) and not os.path.exists(os.path.join(D, 'b728_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b727's keys, the report sections' own heads
REPORT_KEYS = ('REGISTERED -- THE SITTING', 'REGISTERED -- THE DEPOSIT DESCRIPTIONS', 'REGISTERED -- THE LLM LINE', 'REGISTERED -- THE BYLINE', 'CERTIFIED -- tools/standing/ v1.7.0',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b727: no dispatch this act -- VACUOUS on the rows by the ruling's order, each clause read on nothing; the dispatch count zero and no
    `gh workflow run` command in the capture; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and not [r for r in rows if r.get('kind') == 'dispatch'] and len(K.EF_RUNS) == K.MAX_DISPATCHES == 0 and cmds == [] \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (the ledgers, ERRATA, SPIRAL_MAP, the papers (R337)(3) passes), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b727's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The sitting**', '**The four checkpoint kernels**', '**The deposit descriptions**', '**The LLM line**', '**The edition**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b727_corrigendum.txt', 'data/b727_standing_v170.txt', 'data/b727_sitting.txt', 'data/b727_zenodo_readback.json',
                 'data/b727_reproduce.txt', 'data/b727_address_scan.txt', 'data/b727_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b727: no row of the defects bank the navigator's ((a)-(o) the seat's)
#⟪END⟫
#⟪SECTION checks 31⟫
    """the name the frozen run list carries: b727 registers nothing ((R337) orders no registration; the next stands at b728, its M and A read
    before it): no data/b727_registrations.txt; b725's registrations at HEAD their text at their last commit; the components committed in
    their order, each the ancestor of the next; the earlier acts' registrations at HEAD their blobs at their commits."""
    reg, head = S['reg_now']
    return not os.path.exists(os.path.join(D, 'b727_registrations.txt')) and S['files']['reg'] == [K.REGISTRATIONS] and bool(reg) and reg == head \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R337)(5), N5, the scan arm (the name the frozen run list carries): tools/b727_address_scan.py run live over every commit of the act (relay, PLACE-papers and the
    seven sitting repositories; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address and name read from
    history and held in memory -- the address 0, the author's name 0, the previous name 0, its four controls as wanted; [46]'s byline named apart under I-23, the
    address 0 there and at most three of the name; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and 'THE [46] BYLINE, EXCEPTED UNDER I-23: PLACE-papers ' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R337)(3) [46], N5 (the name the frozen run list carries): the edition's byline and two self-citations restored -- :3, :160, :162 the three lines of the
    edition that moved against its blob at the act's base, :160 and :162 equal to day1/Which_Structure_Confines.md's :142 and :144, :3 that file's first two
    fields with v2.4.0; every other line of the edition unchanged; never printed."""
    new, old, src = (S['ws_edition'] or '').split(NL), (S['ws_edition_pre'] or '').split(NL), (S['ws_now'] or '').split(NL)
    moved = [i for i in range(min(len(new), len(old))) if new[i] != old[i]]
    return len(new) == len(old) and moved == [2, 159, 161] and new[159] == src[141] and new[161] == src[143] \
        and new[2] == ' | '.join(src[2].split(' | ')[:2] + ['v2.4.0, October 2026'])
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R337)(3)-(4), N2 (the name the frozen run list carries): the sitting's record -- 46 rows, in number order, the struck items the ruling's five, none NOT APPLIED, every
    item not struck compared EQUAL at its file before its write; the bank's foot its last line; the list itself unmoved. The comparison's four controls ran before the first write and are not re-runnable after it (defect, the capture carries them)."""
    j = S['sittingj'] or {}
    st = dict((int(k), v) for k, v in j.items())
    head = lambda v: v.get('state', '').split(' ')[0].rstrip(',')
    last = ((S['sitting'] or '').rstrip(NL).split(NL) or [''])[-1]
    return sorted(st) == list(range(1, 47)) and [k for k in sorted(st) if head(st[k]) == 'STRUCK'] == list(K.SITTING_STRUCK) \
        and not [k for k in st if head(st[k]) not in ('PASS', 'STRUCK')] \
        and all(st[k].get('compared', '').startswith('EQUAL') for k in st if k not in K.SITTING_STRUCK) \
        and last.startswith('### ### **') \
        and bool(S['frontdoors']) and S['frontdoors'] == S['frontdoors_pre']
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R337)(3), N1, N5 (the name the frozen run list carries): the seven sitting repositories -- each main at its sitting tip locally and at origin, the files it moved against
    its head before the sitting README.md alone, SIDE-cosmo's AGENTS.md beside it by [20] and [22]'s pass, no .lean and no workflow file; no tag since the sitting's first head."""
    rp = S['sit_repos'] or {}
    return sorted(rp) == sorted(K.SITTING_TIPS) and all(v['head'] == v['remote'] == K.SITTING_TIPS[k] and v['tags'] == [] for k, v in rp.items()) \
        and all(v['files'] == (['AGENTS.md', 'README.md'] if k == 'SIDE-cosmo' else ['README.md']) for k, v in rp.items())


def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.7.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v160') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED as b726
    left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since b726's v1.3.0;
    this suite's run list 116 arms, no standing arm added (Component 6, the Edit tool)."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R337)(3) PART C, N3 (the name the frozen run list carries): the deposit descriptions -- [13]-[19] alone, each record the ruling's, each read back anonymously with the
    draft carried, its other metadata, files, record, DOI and version equal, its text banked; no other record in the bank."""
    z = S['zenback'] or {}
    return sorted(int(k) for k in z) == list(range(13, 20)) and all(z[str(n)].get('record') == K.ZEN_RECORDS[n] for n in range(13, 20)) \
        and all(v.get('other_metadata_equal') is True and v.get('files_equal') is True and v.get('record_doi_version_equal') is True and v.get('description') for v in z.values())


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b726's (R336)(7), carried in the run list): tools/research/reproduce.py's full run banked this
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
    """standing clauses v9 (Component 7 of (R337): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b727_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b726's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R337-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b726's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R337) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b726's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R336)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 9fac0a1d',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 79 = 79 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b726-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the sitting`s counts; the four checkpoint kernels; the LLM line; the deposit descriptions; the edition`s byline), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R337)(1)-(2): the generated corrigendum for b726`s record, landed at FINDINGS :11913: its sixteen events and twenty-two defects, 38 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 5 CLOSE 33, REPEAT 14; v1.7.0`s repairs by data/b727_standing_v170.txt; the corrigenda bank appended at row (47)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b727 and no b728 rules bank: no author`s word of b727 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b727's objects
    ('G-REGISTRATIONS-FIRST', 'b727 registers nothing: no data/b727_registrations.txt; b725`s registrations at HEAD their text at dc0d4133; the components each the ancestor of the next; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_c3=False))),
    ('G-PREDICTION-FIRST', '(R337)(5), N5, the scan arm: tools/b727_address_scan.py run live over every commit of the act in nine repositories, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, [46]`s byline named apart under I-23; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R337)(3) [46], N5: the edition`s byline and two self-citations restored from v2.3.1 with the version v2.4.0, the three lines the only lines moved',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'ws_edition', (S['ws_edition'] or '').replace('v2.4.0, October 2026', 'v2.4.1, October 2026'))),
    ('G-DERIVATION-GRADED', '(R337)(3)-(4), N2: the sitting`s record: 46 rows, the five struck, none NOT APPLIED, every other compared EQUAL before its write, the list unmoved',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'sittingj', lambda d: d['23'].update(compared='MISMATCH'))),
    ('G-OFFSET-POST-HOC', '(R337)(3), N1, N5: the seven sitting repositories, each main at its sitting tip locally and at origin, README.md alone moved, SIDE-cosmo`s AGENTS.md beside it by [20] and [22]`s pass, no .lean, no workflow file, no tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'sit_repos', lambda d: d['SIDE-spinor'].update(files=['README.md', 'Spinor.lean']))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 9fac0a1d, VERSION 9; v8 at HEAD its blob at 9fac0a1d; no v10; v9`s commit an ancestor of v1.7.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- the file byte-equal at 9fac0a1d, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R337)(3) PART C, N3: the deposit descriptions [13]-[19] alone, each read back anonymously with its other metadata, files, record, DOI and version equal, its text banked in data/b727_zenodo_readback.json',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'zenback', lambda d: d['13'].update(files_equal=False))),
    ('G-DIFFERS-ERRATA', '(R337)(1)-(2), (4): one ERRATA entry, E-2026-10-31-1, appended; no DIFFERS entry; the weight line and the corrigendum in 3e0ca39, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b727_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R337-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b726`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at e2246a8e (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, VACUOUS BY THE ORDER: no dispatch this act -- the rows empty, the worklist`s runs none, the dispatch cap zero, no dispatch-rows bank',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4, VACUOUS BY THE ORDER: no dispatch row and no `gh workflow run` command in the capture; no b721-b726 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b726 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at the sitting`s [41] tip; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers, ERRATA, SPIRAL_MAP, the papers (R337)(3) passes); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b726`s trail record on OPEN_TRAILS (:16669) and its root in the chain', lambda S: '### b726 — lane two, act one hundred and fifty-three, the wave 1 act under (R336)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers, ERRATA, SPIRAL_MAP, the papers (R337)(3) passes): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b726`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none this act; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
# ### b727, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R337)(3): a main at its sitting tip, its tags unmoved, is not a move against b726's face
#⟪OVERRIDE record 2554 2554⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b727: (R337)'s rows, b726's (R336) rows pruned. (1)'s line is the seat's fill on the author's word, from the public relay at 9fac0a1d
    pub = _blob('D:/relay', '9fac0a1d', 'data/b726_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b726_closing.txt :1, the head line as the public relay carries it at 9fac0a1d, the seat`s fill of (1)', bool(pub) and pub[0] == at(cl, 1) and 'relay 3dd8f806' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 111 of 116', 'root 720308d8bd702563', 'scores 8 of 8 HELD', '22 defects'):
        add('ruling (1)', 'data/b726_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt'))]
    add('ruling (1)', 'data/act_roots.txt :106, b726`s root 720308d8 chained from b725`s d85513ca', at(ar_, 106)[:1] == ['b726']
        and at(ar_, 106)[1].startswith('720308d8') and at(ar_, 106)[2].startswith('d85513ca'), ' '.join(x[:8] for x in at(ar_, 106)), '1')
    c2_ = lines_of(p('data', 'b726_c2.txt'))
    add('ruling (1)', 'data/b726_c2.txt :45, the certificates at 15 of 18 with no axiom', 'CERTIFICATES COMPILED AT 15 OF 18' in at(c2_, 45) and 'EACH DEPENDING ON NO AXIOM' in at(c2_, 45), at(c2_, 45)[:60], '1')
    fd_ = rd(p('data', 'b726_frontdoors.txt')) or ''
    nums_ = [int(x) for x in re.findall(r'(?m)^  \[(\d+)\] ', fd_)]
    add('ruling (1), (3)', 'data/b726_frontdoors.txt, items [1]-[46], 3 LOAD-BEARING', sorted(nums_) == list(range(1, 47)) and len(re.findall(r'(?m)^  \[\d+\] LOAD-BEARING', fd_)) == 3,
        'items %d' % len(nums_), '2')
    mc_ = lines_of(p('data', 'b726_mechanisms.txt'))
    add('ruling (1)', 'data/b726_mechanisms.txt :30, the table`s 3 rows', 'THE MECHANISM TABLE: 3 ROWS' in at(mc_, 30), at(mc_, 30)[:50], '1')
    add('ruling (1)', 'data/b726_act_root.json, the root', (_jl('b726_act_root.json').get('root') or '').startswith('720308d8'), (_jl('b726_act_root.json').get('root') or '')[:16], '1')
    add('ruling (1)', 'the edition v2.4.0 on PLACE-papers main', bool(_blob(PP, 'main', 'day1/Which_Structure_Confines_v2_4_0.md')), 'present', '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(16) and 22 defects (data/b726_events.txt, data/b726_defects.txt)',
        starts == list(range(1, 17)) and len(letters) == 22, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((4, 1, 'CLOSE ; REPEAT b725 event (1)'), (7, 2, 'CLOSE ; NEW'), (12, 3, 'CLOSE ; NEW'), (36, 9, 'CLOSE ; REPEAT b725 event (4)'), (49, 10, 'CLOSE ; NEW')):
        add('ferry (read first)', 'event (%d) at data/b726_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:60],
            at(ev, n_)[:50], '0')
    add('ferry (read first)', 'data/b726_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    for f_ in ('b726_frontdoors.txt', 'b726_zenodo_read.json', 'b721_frozen_line_drafts.txt', 'b723_axiom.txt', 'b726_edition_diff.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    zr_ = rd(p('data', 'b726_zenodo_read.json')) or ''
    for z_ in ('21539068', '19938917', '19937590', '21436282', '21539167', '21520474'):
        add('ruling (3) PART C', 'data/b726_zenodo_read.json carries the record %s' % z_, z_ in zr_, 'present' if z_ in zr_ else 'ABSENT', '2')
    ax_ = rd(p('data', 'b723_axiom.txt')) or ''
    add('ruling (3) [12]', 'data/b723_axiom.txt, the prints at the wave 1 pins', 'Classical.choice' in ax_ and 'Quot.sound' in ax_ and 'propext' in ax_, 'lines %d' % ax_.count(NL), '2')
    ws_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines.md'))
    add('ferry (read first), ruling (3) [46]', 'day1/Which_Structure_Confines.md :3, :142, :144, read, not printed', bool(at(ws_, 3)) and bool(at(ws_, 142)) and bool(at(ws_, 144)), 'lengths %d, %d, %d' % (len(at(ws_, 3)), len(at(ws_, 142)), len(at(ws_, 144))), '2')
    add('ferry (read first), ruling (3) [46]', 'OPEN_TRAILS :11864, THE FORM OF AN EDITION', 'THE FORM OF AN EDITION' in at(ot, 11864), at(ot, 11864)[60:150], '2')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    add('ruling (5)', 'phase1.5/method/INSTRUMENTS.md :416, I-23, THE NAME-AND-TITLE EXCEPTION', at(ins_, 416).startswith('## I-23') and 'NAME-AND-TITLE' in at(ins_, 416).upper().replace(' ', '-').replace('--', '-') or 'I-23' in at(ins_, 416), at(ins_, 416)[:60], '2')
    add('ferry (read first), ruling (3) PART C', 'the author`s word passing PART C, in the ruling itself', 'move forward on all that needed' in text, 'carried in the delivery, no earlier bank holds it', '2')
    rg_ = rd(os.path.join(PP, 'REGISTRY.md')) or ''
    for w_ in ('1.5a-3', '1.5a-4'):
        add('ruling (3) [32], [33]', 'REGISTRY.md carries %s' % w_, w_ in rg_, 'present' if w_ in rg_ else 'ABSENT', '2')
    add('ruling (3) [34], [35]', 'tools/chain_page.py, the generator of the two pages', os.path.exists(p('tools', 'chain_page.py')), 'present' if os.path.exists(p('tools', 'chain_page.py')) else 'ABSENT', '2')
    sm_ = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (3) [12]', 'SPIRAL_MAP.md :104, the line by its digest 8ffb56940a0ee30d', __import__('hashlib').sha256(at(sm_, 104).encode('utf-8')).hexdigest().startswith('8ffb56940a0ee30d'), __import__('hashlib').sha256(at(sm_, 104).encode('utf-8')).hexdigest()[:16], '2')
    cs_ = rd(p('tools', 'standing', 'fold', 'checks.tpl')) or ''
    add('ruling (2)', 'tools/standing/fold/checks.tpl, G-ANSWERS-CHECKED defined', 'G-ANSWERS-CHECKED' in cs_, 'present', '1')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-cosmo at D:/SIDE-cosmo', os.path.isdir('D:/SIDE-cosmo/.git'), 'D:/SIDE-cosmo', '0')
    for k_ in ('SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve'):
        add('PATHS', '%s at D:/%s' % (k_, k_), os.path.isdir('D:/%s/.git' % k_), 'D:/' + k_, '0')
    add('ferry', 'tools/standing/ at v1.6.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.6.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R337)(5): b726's export, the mirror's last
    add('ruling (5)', 'D:/MY-DOwnloads/mirror-refresh-2026-10-30-b726.zip, b726`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R337)(5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (5)', 'the push-b726-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R337)(5): act_current alone, then b726's step row 27 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b726_steps.json'),
                   (K.STEPZERO, 'data/b726_relay_push-b726-closing_push_out.txt')):
        if not c_:
            add('ruling (5)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (5)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (5)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (5)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (5)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b727_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b727_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b727 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b726_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R337)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.7.0's controls, the sitting's record, the deposit descriptions' read-backs, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R337)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R337)(7)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: README.md alone on seven mains, SIDE-cosmo's AGENTS.md beside it by [20] and [22] ((R337)(3)); no Lean file, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b728 ((R337)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b727 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-FOUR, THE RELEASE SITTING: THE FRONT-DOOR LIST APPLIED ITEM BY ITEM; '
              'THE FOUR CHECKPOINT KERNELS AT THEIR COMPILED STATEMENTS; THE LLM LINE; THE DEPOSIT DESCRIPTIONS ON THE AUTHOR`S PASS; THE EDITION`S BYLINE RESTORED; '
              'v1.7.0 LANDED, UNDER (R337).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b726's sections over b726's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.7.0: G-ACT-CURRENT and G-BRANCHES-BANKED repaired, the answers pair and the answer check out of the lock`s set, each case failing before its repair and passing after', 'b727_standing_v170.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE SITTING ((R337)(3)-(4))', [
                ('one row per item of the list, every current read and compared before its write', 'b727_sitting.txt')]),
            ('THE DEPOSIT DESCRIPTIONS ((R337)(3) PART C)', [
                ('[13]-[19] on the author`s pass by number, each read back anonymously; no file, version or DOI changed', 'b727_sitting.txt', r'(?m)^\[19\] PASS')]),
            ('THE NAME AND ADDRESS ((R337)(5))', [
                ('the scan over every commit and bank of the act in nine repositories, the [46] byline excepted under I-23 and so named, the counts alone', 'b727_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b726`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b727_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: README.md on main of SIDE-archimedean, SIDE-frobenius, SIDE-spinor, SIDE-rcurve, SIDE-cosmo, SIDE-kernel and SIDE-lv-conservation, SIDE-cosmo`s AGENTS.md beside it',
    '    by [20] and [22]`s pass (ruled by number; N5`s words name README.md alone: printed, not smoothed), each commit under the noreply identity, each pushed through push_gated.sh and read back ;',
    '    the four GitHub descriptions [5], [7], [9], [11] edited and read back ; no Lean file, no workflow file, no tag, no release ; [skip ci] on the SIDE-kernel and SIDE-cosmo commits, no run started ;',
    '    0 runner dispatches (N1) ; the rebuild-b721 branches of the wave 1 kernels as b726 left them ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, keiper-b725, c2-b725 and the challenge branch',
    '    challenge-b720-h2-sign-iff-rh standing ; port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part, computation and push ;',
    '    the push-b726-* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message ; N2: every CURRENT read and compared before its write, no mismatch ;',
    '    N3: PART C edited as [13]-[19] alone, seven description edits on six records, each read back anonymously and banked (relay data/b727_zenodo_readback.json), no other deposit record touched, no file, no new version ;',
    '    (R337)(5): no new occurrence of the author`s name or address in anything the act wrote, committed or pushed, [46]`s byline excepted under I-23 and so named in relay data/b727_address_scan.txt ;',
    '    the commits under the GitHub login and its noreply address ; no identifier of the author in any outbound request header, URL, input or payload, or in any workflow file ; no secret added ;',
    '    the Zenodo token read from the environment by tools/b727_sitting.py alone, its value never printed ; the deposit route untouched, publish never called, the draft held at v5 ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry), OPEN_TRAILS (the trail), ERRATA (E-2026-10-31-1), SPIRAL_MAP :104 and the papers the sitting names written ; no paper cut, moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt (b727`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.7.0 by (R337)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b726 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R337)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For b728, each from its bank: the sitting`s findings printed for the author (relay data/b727_defects.txt); W-ORD-CHAIN-PAGE-LLM-LINE at tools/chain_page.py`s next run; the three C2 fields not compiled (relay data/b726_c2.txt);',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b727_reproduce.txt); the onset successor, its M and A read from computed form before any registration; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 and c2-b725 (at ' + WL.EF_BRANCHES[1][1][:8] + ') of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay; the seven push-b727-sitting branches;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b726 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, seven kernels` README.md and SIDE-cosmo`s AGENTS.md by (R337)(3)`s sitting, no Lean file, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (the sitting`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b727: the standing repairs are v1.7.0's ((R337)(2), relay data/b727_standing_v170.txt, read in the corrigendum section); the
    # ### carry's diffs here (b727 carried at step zero before the fold; its tools since are the templates and tools/acts/b727.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; seven mains written by (R337)(3)`s sitting, README.md and SIDE-cosmo`s AGENTS.md; '
          'no Lean file; the %s branches of the wave 1 kernels as b726 left them; port-b707 at b712`s tip %s)' % (
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
    b727's form over b727's objects (b726's form in git at b726's record tool): the corrigendum's foot and v1.7.0's controls; the sitting's record; the deposit read-backs;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v170.txt' % ACT, r'\*\*v1\.7\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.7.0`s controls')
    si = _bfig('%s_sitting.txt' % ACT, r'\*\*THE SITTING: (\d+) ROWS OF (\d+) ; PASS (\d+) ; PASS, (\d+) ; STRUCK (\d+)\.\*\*', 'the sitting`s foot')
    sj = jl('%s_sitting.json' % ACT)
    ok_ = lambda k: (sj.get(str(k)) or {}).get('state', '').startswith('PASS')
    zb = jl('%s_zenodo_readback.json' % ACT)
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v170_ctl=v5[0], v170_cases=v5[1], v170_wanted=v5[2],
                si_rows=si[0], si_a=int(si[2]) + int(si[3]), si_s=int(si[4]), si_n=int(si[0]) - int(si[2]) - int(si[3]) - int(si[4]),
                llm_p=sum(1 for k in list(range(23, 32)) + [37, 38, 39] if ok_(k)), llm_k=sum(1 for k in range(40, 46) if ok_(k)),
                zen_d=len(zb), zen_r=len(set(v.get('record') for v in zb.values())),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R337)(3): the kernel rows of one kind as banked (data/b727_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R337): no lean process runs on this host and no runner dispatch this act. From the command bank (the seat's commands, read live from the capture by the
    `commands` route: local lean none; the dispatch commands `gh workflow run` none) and the worklist's EF_RUNS (none). VACUOUS on run ids by the ruling's order."""
#⟪END⟫
#⟪SECTION record 8⟫
    ok = bool(cm) and not seat_lean and not disp and K.MAX_DISPATCHES == 0 and K.EF_RUNS == ()
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b727_commands.json): %s; dispatch commands in the capture: %s, none ordered, VACUOUS on run ids by the ruling`s order' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread'))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b727's objects): the one tool's controls before its figures banked this act, (bank, the controls' line, the first figure's line); the sitting's four
# ### comparison controls ran before its first write, by `control`, and stand in the capture
N2_CONTROLS = (('data/b727_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),)


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R337): every CURRENT read and compared, the comparison printed, no write on a mismatch. From the sitting's json, a row per item: every item not struck its comparison EQUAL, its
    time before the next item's; the bank carrying the comparison line at every row."""
    st = jl('%s_sitting.json' % ACT)
    reads = sorted(int(k) for k in st)
    miss = [k for k in reads if k not in K.SITTING_STRUCK and not str(st[str(k)].get('compared', '')).startswith('EQUAL')]
    printed = rdn('%s_sitting.txt' % ACT).count('  COMPARED TO THE BANK: ')
#⟪END⟫
#⟪SECTION record 12⟫
    ok = reads == list(range(1, 47)) and not miss and printed == 46 and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the sitting`s rows read %d of 46, the comparison printed at %d, an item not struck and not EQUAL: %s; the tool`s controls before its figures: %s' % (
            len(reads), printed, miss or 'NONE', ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b727's objects; b726's in git at b726's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b727_standing_v170.txt', ('ALL AS WANTED',)), ('b727_sitting.txt', ('THE SITTING',)), ('b727_citation_check.txt', ('CITES CHECKED',)),
             ('b727_reproduce.txt', ('REPRODUCES',)), ('b727_address_scan.txt', ('PREVIOUS ADDRESS',)))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R337): PART C edited as [13]-[19] alone, each read back and banked; no other deposit record touched; every grade prints at its end. From the banks' last lines and the
    read-back bank."""
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
    zb = jl('%s_zenodo_readback.json' % ACT)
    zk = sorted(int(k) for k in zb)
    zeq = all(v.get(c) is True for v in zb.values() for c in ('other_metadata_equal', 'files_equal', 'record_doi_version_equal'))
    zrec = all(v.get('record') == K.ZEN_RECORDS[int(k)] and v.get('description') for k, v in zb.items())
    ok = all(o for _n, o in graded) and zk == list(range(13, 20)) and zeq and zrec
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the deposit read-backs: %s, each record the ruling`s: %s; each other metadata, files, record, DOI and version equal: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), zk, zrec, zeq))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R337) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R337)(5))
# ### (R337)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R337) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b726's form, carried) -- read from git,
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
    # ### (R337)(3), N5: every ref of every kernel carrying a commit made after the act's opening commit stands at that kernel's sitting tip; each sitting repository's files against its
    # ### head before the sitting README.md alone, SIDE-cosmo's AGENTS.md beside it by [20] and [22]'s pass; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b726 left them; the address scan's count from its bank (relay data/b727_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w, sit_new = [], []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if K.SITTING_TIPS.get(kn) == r_[1] and r_[0].startswith('refs/heads/'):
                    sit_new.append(kn)
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    sit_files = dict((n_, sorted(x for x in g(p_, 'diff', '--name-only', h_, 'main').split() if x.strip())) for n_, p_, h_ in K.SITTING_REPOS)
    sit_ok = sorted(set(sit_new)) == sorted(K.SITTING_TIPS) and all(v == (['AGENTS.md', 'README.md'] if k == 'SIDE-cosmo' else ['README.md']) for k, v in sit_files.items())
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and sit_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b727_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than at its sitting tip, or a .lean file in a kernel`s tree (%d kernels read): %s; the seven repositories` files against their heads before the sitting, README.md alone and '
            'SIDE-cosmo`s AGENTS.md beside it by [20] and [22]`s pass, ruled by number though N5`s words name README.md alone (printed, not smoothed): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', sit_ok, K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b727 — lane two, act one hundred and fifty-four, the release sitting under (R337): b726 at its weight and its corrigendum; v1.7.0; '
            'the front-door list applied item by item; the deposit descriptions on the author’s pass; the sitting’s record')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 3 form adjusted to what the act did; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## The release sitting: %d items applied, %d struck, %d not applied; the four checkpoint kernels’ READMEs and descriptions at their compiled statements; '
            'the LLM line at %d papers and %d READMEs; %d deposit descriptions noted on %d records; the edition’s byline restored' % (
                f['si_a'], f['si_s'], f['si_n'], f['llm_p'], f['llm_k'], f['zen_d'], f['zen_r']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) [12]’s ruled sentence against data/b723_axiom.txt: SIDE-frobenius g_two_three and SIDE-spinor spectral_volume read [propext] alone, aperture_decomp none; written verbatim as ruled; '
            '(2) the edition’s :316 still says the author’s name is not carried, which [46] made stale, outside the list; (3) N5’s README.md alone against [20] and [22]’s pass of SIDE-cosmo’s AGENTS.md, the pass followed; '
            '(4) SIDE-rcurve’s README still says positivity is closed and names a deposited proof beside [14]’s note, outside the list; (5) the edition form’s current-unedited clause against the table’s in-place items; '
            '(6) %s and the seat’s %s '
            'defect%s as lettered' % (
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
            'author beside the next act of (R337)(7)): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b727's objects; b726's composer in git at
    b726's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The front-door list of data/b726_frontdoors.txt was applied in number order: %d items applied, %d struck by the ruling, %d not applied; every current read matched its bank before its write. '
         'SIDE-archimedean, SIDE-frobenius, SIDE-spinor and SIDE-rcurve now state in their READMEs and GitHub descriptions what they compile; the LLM line stands at %d papers and %d READMEs; '
         '%d deposit descriptions on %d records carry their notes on the author’s pass, no deposited file, version or DOI changed; the edition’s byline and two self-citations are restored; the draft stands at v5, HELD.' % (
             f['si_a'], f['si_s'], f['si_n'], f['llm_p'], f['llm_k'], f['zen_d'], f['zen_r']), '',
         '*Filed at b727 on the author’s ruling `(R337)`; %d question%s put before the root. Banks: relay '
         '`data/b727_corrigendum.txt`, `data/b727_standing_v170.txt`, `data/b727_sitting.txt`, `data/b727_zenodo_readback.json`, `data/b727_reproduce.txt`, `data/b727_address_scan.txt`, '
         '`data/b727_touch.txt`, `data/b727_standing_figures.txt`, `data/b727_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R337)(1)-(2), `%s`, `%s`, `%s`): b726 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b726’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b727_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b727_standing_v170.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v170_ctl'], f['v170_cases'],
             f['v170_wanted']), '',
         '**The sitting** ((R337)(3)-(4), N2): %s rows, one per item, in number order; %d applied, %d struck ([32]-[33] scope dropped, [34]-[35] struck as hand edits, [36] a ledger), %d not applied; '
         'every current read at its file, record or by gh and compared before the write, no mismatch; [3]’s first comparison read the wrong line by a routing defect of the sitting’s tool and was read again by gh before its write (relay data/b727_sitting.txt). ERRATA E-2026-10-31-1 records the sitting.' % (
             f['si_rows'], f['si_a'], f['si_s'], f['si_n']), '',
         '**The four checkpoint kernels** ((R337)(3) PARTS A and B): the title lines and the sentences the list grades EXCEEDS replaced in the four READMEs ([4], [6], [8], [10]), the one-line GitHub descriptions replaced and read back ([5], [7], [9], [11]); [1]-[3] satisfied by [10] and [11]; '
         'SIDE-cosmo’s error bar ([20]-[22]) and SPIRAL_MAP :104 ([12]) as ruled.', '',
         '**The deposit descriptions** ((R337)(3) PART C, N3): [13]-[19], the author’s pass by number, %d description edits on %d records, each read back anonymously with its other metadata, files, record, DOI and version equal; no other deposit record touched; no new version (relay data/b727_zenodo_readback.json).' % (
             f['zen_d'], f['zen_r']), '',
         '**The LLM line** ((R337)(3) PART E): the monograph’s words at %d papers and %d kernel READMEs; [34]-[35] struck as hand edits, the generator’s next run carrying them under W-ORD-CHAIN-PAGE-LLM-LINE.' % (f['llm_p'], f['llm_k']), '',
         '**The edition** ((R337)(3) [46], PLACE-papers `%s`): day1/Which_Structure_Confines_v2_4_0.md’s byline and two self-citations restored to v2.3.1’s words under I-23, the three lines the only lines moved; the edition form gains its sentence by a dated line in the trail.' % K.C2_PP[:8], '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b727_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R337)(5), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted, [46]’s byline named apart under I-23 (relay data/b727_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b727_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b727 -- %s, %s, %s, %s -- against b726’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b727_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the READMEs and the deposit descriptions are one correction read at two doors, each now saying what compiled and what stands unsupported; '
         'the sitting’s comparison and the corrigendum meet at the same habit, a word read against its bank before it is carried.', '',
         '**Carried to:** %s, the research act: the onset successor from the six banked products and off18’s, M and A read from the computed form and checked against the banked onsets before any registration commits; H-DIAL’s finding into the mechanism table; the three C2 fields finished by split dispatch; '
         'lambda_2’s two premises; W-ORD-VISIBILITY from H-INTERFERENCE’s table; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b726():
    """b726's form over b726's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b727's objects; b726's composer in git at b726's record tool): THE ORDER W-ORD-CHAIN-PAGE-LLM-LINE entered and the dated line to THE FORM OF AN EDITION, each by its
    own line, then the open-orders line written from tools/standing/orders.py's output over the trail at HEAD with those lines beneath it, the new order read OPEN by the generator's rule."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['*Appended 2026-10-31 by b727, under the author’s ruling `(R337)`(3) [34]-[35] -- THE ORDER **`W-ORD-CHAIN-PAGE-LLM-LINE`**: relay tools/chain_page.py gains the LLM line in the monograph’s words under the edition form at its next run; [34] and [35] struck as hand edits. Trigger: the generator’s next run. Status: OPEN.*',
           '*2026-10-31, b727, under `(R337)`(3) [46], to THE FORM OF AN EDITION (:11864):* “a paper\'s byline and self-citations are the paper\'s own words and are carried unchanged”']
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-CHAIN-PAGE-LLM-LINE' not in op:
        sys.exit('### THE TRAIL: THE NEW ORDER NOT READ OPEN BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R337) ratified.** Its components as the ferry orders them (relay data/b727_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b726’s weight), :%s (the corrigendum), :%s (the entry); ERRATA E-2026-10-31-1 (:%d); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line'), K.ERRATA_LINE), '',
             '**The orders acted** ((R337)(3)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the line above from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b727_standing_v170.txt).' % (
                 f['ver'], f['v170_cases'], f['v170_wanted']), '',
             '**The sitting:** %d items applied, %d struck, %d not applied, no mismatch (relay data/b727_sitting.txt).' % (f['si_a'], f['si_s'], f['si_n']), '',
             '**The deposit descriptions:** %d edits on %d records, each read back, no file, version or DOI changed (relay data/b727_zenodo_readback.json).' % (f['zen_d'], f['zen_r']), '',
             '**The LLM line:** %d papers and %d READMEs; the generator’s pages carried by the order above.' % (f['llm_p'], f['llm_k']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b727_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, [46]’s byline excepted under I-23 and so named (relay data/b727_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b727_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b727 `%s` (previous `%s`, b726’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b727_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b727_standing_v170.txt); the standing '
             'report tool (relay data/b727_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** seven mains written by the sitting, README.md alone and SIDE-cosmo’s AGENTS.md beside it, no Lean file and no tag; no runner dispatch; the %s branches as b726 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b727_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b726’s %s, %s, %s, %s (relay data/b727_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b727_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b726():
    """b726's trail record over b726's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b727*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725 and c2-b725, kept, none cut; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b726 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b727*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s two branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s and b726`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: README.md, SIDE-cosmo`s AGENTS.md beside it, alone.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R337)(5): relay push-b726-closing, push-b726-preroot, push-b726-record; PLACE-papers push-b726-preroot, push-b726-record; each local, by name, after --merged listed it (data/b727_stepzero.txt).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: README.md and AGENTS.md alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R337) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (9338dc3f) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R337)(1)-(2): FINDINGS :11913.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R337)(1)-(2): one row, b726`s (47).'),
    ('ERRATA entries filed', 1, 1, 'entries', '### (R337)(4): E-2026-10-31-1, naming the sitting.'),
    ('orders entered with the trail', 1, 1, 'orders', '### (R337)(3) [34]-[35]: W-ORD-CHAIN-PAGE-LLM-LINE.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b727_reproduce.json.'),
    ('items of the list applied', 'SITPASS', 'SITPASS', 'items', '### (R337)(3); MEASURED off data/b727_sitting.json.'),
    ('items of the list struck', 'SITSTRUCK', 'SITSTRUCK', 'items', '### (R337)(3): [32]-[36]; MEASURED off data/b727_sitting.json.'),
    ('deposit descriptions edited', 'ZENEDITS', 'ZENEDITS', 'edits', '### (R337)(3) PART C: [13]-[19], on six records; MEASURED off data/b727_zenodo_readback.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.7.0`s controls, the sitting`s record, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: b727 registers nothing; the next stands at b728, its M and A read before it.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 0, 0, 'modules', '### none: N5.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R337)(2): tools/standing/ to v1.7.0, each repair with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; data/b675_corrigenda.txt`s row (47), appended; data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation and push; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R337)(5), N5: PREVIOUS ADDRESS 0, [46]`s byline named apart under I-23; MEASURED off data/b727_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, gh reads and edits of the four descriptions, the Zenodo edits by token and their anonymous read-backs; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b727 registers nothing: no figure bank of a registered object this act
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b727_reproduce.json', lambda j: len(j.get('rows') or [])),
                    SITPASS=jcount('b727_sitting.json', lambda j: len([k for k, v in j.items() if v.get('state', '').startswith('PASS')])),
                    SITSTRUCK=jcount('b727_sitting.json', lambda j: len([k for k, v in j.items() if v.get('state', '').startswith('STRUCK')])),
                    ZENEDITS=jcount('b727_zenodo_readback.json', lambda j: len(j)),
                    ADDRESS=tfirst('b727_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v170', 'sitting', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b727_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFRUNS', 'REPROWS', 'ADDRESS', 'SITPASS', 'SITSTRUCK', 'ZENEDITS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b727_registration_%s.txt -- b727, THE RELEASE SITTING: b726 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.7.0; THE FRONT-DOOR LIST APPLIED ITEM BY ITEM; "
                             "PART C ON THE AUTHOR`S PASS BY NUMBER; THE SITTING`S RECORD; NO RUNNER DISPATCH, NO DEPOSIT, NO LEAN FILE, NO TAG, UNDER (R337)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b726's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b727: b726's lines read banks this
act does not write, and are not carried; the lines are b727's: tools/standing/ v1.7.0 by its controls (CERTIFIED), the sitting, the four checkpoint kernels,
the deposit descriptions, the LLM line and the byline (REGISTERED), and the draft (HELD). No KERNEL line: nothing compiled this act.
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b727's lines, each from the record tool's figures over b727's banks
    # ------------------------------------------------------------------ REGISTERED: THE SITTING ((R337)(3)-(4))
    sk = seat('%s_sitting.txt' % ACT, '**THE SITTING: ')
    keys['SIT'] = ('REGISTERED -- THE SITTING: %d items applied, %d struck, %d not applied, every current read and compared before its write. SOURCE %s.' % (
                      f['si_a'], f['si_s'], f['si_n'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.7.0 ((R337)(2)), by its controls
    sw = seat('%s_standing_v170.txt' % ACT, '**v1.7.0: CONTROLS ')   # ### appended by the template after this section
    keys['V170'] = ('CERTIFIED -- tools/standing/ v1.7.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v170_ctl'], f['v170_cases'], f['v170_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the kernels, the descriptions, the LLM line, the byline, each read from the sitting's foot
    keys['KER'] = ('REGISTERED -- THE FOUR CHECKPOINT KERNELS: READMEs and GitHub descriptions at their compiled statements, [4]-[11], each read back; no Lean file, no tag. SOURCE %s.' % sk['text'])
    keys['ZEN'] = ('REGISTERED -- THE DEPOSIT DESCRIPTIONS: %d edits on %d records on the author`s pass by number, each read back anonymously, no file, version or DOI changed. SOURCE %s.' % (
        f['zen_d'], f['zen_r'], sk['text']))
    keys['LLM'] = ('REGISTERED -- THE LLM LINE: the monograph`s words at %d papers and %d READMEs; the generator`s pages carried by W-ORD-CHAIN-PAGE-LLM-LINE. SOURCE %s.' % (
        f['llm_p'], f['llm_k'], sk['text']))
    keys['BYL'] = ('REGISTERED -- THE BYLINE: the edition`s byline and two self-citations restored under I-23. SOURCE %s.' % sk['text'])
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R337)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('CERTIFIED', ['V170']), ('REGISTERED', ['SIT', 'KER', 'ZEN', 'LLM', 'BYL']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b727 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
