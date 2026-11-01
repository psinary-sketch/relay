# -*- coding: utf-8 -*-
# b731 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R341)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R341)(2) repair it carries. Edited by the Edit tool. Carried at b731 by tools/b731_fold.py (`carry`) from tools/acts/b730.py,
# b730`s names substituted; the citation`s sections adopted from tools/b731_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b730`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b730`s carried till
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
# ### b731, Component 1 (the Edit tool): THE c1 ROUTE FOR b730'S WEIGHT LINE AND ITS CORRIGENDUM, (R341)(1)-(2). Carried from b730's
# ### override and rewritten here against b730's own banks: the closing's lines by needle, the events (12), the defects (23), the refusals
# ### (4), the v1.11.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = 'd0bedc7d'          # ### b730's closing commit
C1_REFUSAL_AT = 'd0bedc7d'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-01'
C1_CORRIGENDA_LAST = 50
C1_V170 = 'b731_standing_v1110.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-01 by b731 to b730’s entry (:%d), under `(R341)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-DERIVES entered, five fields'
C1_TRAIL_NEEDLE = '### b730 — lane two, act one hundred and fifty-seven, the continuation act under (R340)'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")


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
    for l in _c1_rd('b730_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b730_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b730_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b730_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b730_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b730_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b730_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b730_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 7:
        sys.exit('### data/b730_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b730_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b730_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 13)) or len(dr) != 23:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b730 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b730_closing.txt):* “%s” (data/b730_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b730_steps.json, the record and closing rows). As its rows read: the continuation field CLOSED, zq_continuation and exists_zq_continuation compiled on zq-b730 at 5688816e with the standard three, no sorry, '
            '6 dispatches, 835 lines, one field of five, the instance not moved (data/b730_continuation.txt :55); W-ORD-ZQ-DERIVES entered; D9 and D13 named with what each needs (data/b730_detection_lemmas.txt :11); the standing tools v1.10.0, 26 cases as wanted '
            '(data/b730_standing_v1100.txt); the scores 7 of 8 HELD, N4 HELD and N5 REFUTED (data/b730_scores_close.json). '
            'The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both (:%d, :%d); the counter CLAIM %s, CLOSE %s, REPEAT %s of %s (:%d). '
            'The root %s over %s banks, chained from %s (data/b730_act_root.json; :%d), the chain AGREE b624-b730; %s questions banked as put by the seat (:%d), in one call, the head line counting the call; %d events in data/b730_events.txt, rows (1)-(%d); %d defects, (a)–(w) '
            '(data/b730_defects.txt). THE NAVIGATOR’S ERROR the author’s word names, a write ordered outside the (W) list it wrote, stands: N5 REFUTED unreworded, the composer repaired below. '
            'Nothing deposited, no draft published; the corrigendum for these rows follows, under `(R341)`(1)-(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                cc, cd, rp, rn, l_cn, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b730's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'REDIR', '08:47:00Z', 'defect (d)'), (2, 'PIPE', '09:13:58Z', 'defect (e)'), (3, 'READ', '09:27:08Z', 'defect (f)'), (4, 'ENV', '09:32:44Z', 'defect (g)')]
C1_CORR_TITLE = ('## Corrigendum to b730’s record (relay data/b730_events.txt rows (1)-(12) and data/b730_defects.txt): twelve events and twenty-three defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the author’s three repairs at its head, the composer reading the clauses into (W), the price bank’s measured row, a stamped route’s re-run to a suffixed path; the post-lock scan’s bank, '
                 'the seat’s three arms refused at the hand, the citation check over the author’s word and the head line’s count of questions, at tools/standing/ v1.11.0, each controlled on b730’s banks, under (R341)(1)-(2)')


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
    rl = _c1_git('show', '%s:data/b730_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b730_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.11.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=[])
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(12)', sorted(ev) == list(range(1, 13))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 23', len(dr) == 23), ('the refusals 4, each answered as listed', len(rl) == 4 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.11.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.11.0
C1_EV_EXTRA = {1: '; repair (arms); the arm stands failing at b730, the call in its capture', 2: '; repair (arms); the row not rewritten', 3: '; repair (face); N5 stands REFUTED unreworded by the author’s word', 4: '; the control working as built',
               5: '; repair (rerun)', 6: '; repairs (face), (price), (rerun), carried by `(R341)`(2)(i)-(iii)', 7: '; repair (word)', 8: '; repair (arms); the arm stands failing at b730', 9: '; the face not edited; b731’s (W) rows read from its own face’s date',
               10: '; no guard moved; carried', 11: '; no cause named; carried', 12: '; the four as named; G-AXIOM-CLAIM declared and carried'}
C1_CLASSES = (
    ('face', 'the face composer reads the clauses into (W) (`(R341)`(2)(i), event (3), the author’s word (1))', 'standing.faceform reads a ruling’s clauses for the paths a write verb governs and for a move’s target, the source’s kind at the act named; a path only cited is not picked; the composer adds the row the list lacks. (R340)(6)’s move reads into b730’s list; b730’s N5 stands REFUTED unreworded'),
    ('price', 'the price bank’s measured row, in I-10’s form (`(R341)`(2)(ii), the author’s word (2))', 'standing.pricebank: a measured row read from the tree and the run ids beside its estimate, refused without a run; 835 lines and 6 dispatches beside 1,500-3,000 and 25-50, the ratio 0.278-0.557 and 0.12-0.24 printed. The rooted bank is not edited: the rows stand in the act’s data/<act>_price_measured.txt'),
    ('rerun', 'a stamped route’s re-run to a suffixed path (`(R341)`(2)(iii), event (5), the author’s word (4))', 'the rowgen route takes the first free <stem>_rerunN name where the bank stands, the stamp standing; a first run keeps the plain name'),
    ('postlock', 'the post-lock scan’s bank out of the lock’s hash (`(R341)`(2)(iv))', 'the root’s exclusion takes data/<act>_address_scan_postlock.txt beside the lock’s list, which v1.9.0 had; b730’s nine scans printed after its lock, read from the session’s transcript, enter the form, the texts kept in no bank'),
    ('arms', 'the seat’s three (`(R341)`(2)(v), events (1), (2), (8), (12))', 'each refused at the seat’s hand, since a read of b730’s calls cannot be repaired: the hook refuses a command of more than one suite part or combine, kind SUITE, and a branch delete before the act’s citation check, kind ORDER; the step recorder refuses a second `lock` row, naming `seal`'),
    ('word', 'the citation check over the author’s word (`(R341)`(2)(vi), event (7))', 'standing.cites reads a word’s clauses against their ruling’s items, its instruments against INSTRUMENTS.md and its figures of lines and dispatches against the banks of the act and the act before; b730’s word, 0 cites and VACUOUS, reads 4 rows, 4 found'),
    ('questions', 'the head line’s count of questions (`(R341)`(2)(vii))', 'the closing reads the bank’s PROMPT rows and not the calls: b730’s one call of two questions reads two'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b730’s events bank (relay data/b730_events.txt) carries twelve rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-three lettered rows, (a)-(w), each tagged in its own bracket (%s); its refusal bank four lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R341)`(2), at tools/standing/ v1.11.0, each with a control on b730’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b730’s events (1)-(12):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?(\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?|post-push|pre-push and post-push): ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b730_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b730’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b730_defects.txt; %s; %s; %s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c))]
    L += ['', '**b730’s refusals** (relay data/b730_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (twelve events, twenty-three defects), as b730’s closing prints it (relay data/b730_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b731 on the author’s ruling `(R341)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b731.py) from '
          'b730’s events and defects banks read unedited, its refusal bank, and the v1.11.0 controls bank; banked as relay `data/b731_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b730’s record; no sealed tool, face, trail or root-named bank of b730 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b731 -- THE CORRIGENDUM FOR b730, (R341)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b730_events.txt rows (1)-(12), data/b730_defects.txt 23 rows, data/b730_hook_refusals.txt 4 '
             'lines at %s; data/%s (the v1.11.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 12, DEFECTS 23 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.11.0: THE COMPOSER AND (W), THE MEASURED ROW, A STAMPED RE-RUN, '
               'THE POST-LOCK SCAN, THE SEAT`S THREE ARMS, THE AUTHOR`S WORD, THE QUESTIONS COUNT ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b730 at its weight after its entry, and the corrigendum for b730, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.11.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b731, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b731 ran three
# ### ((R341)(4)(iii)-(iv), N1), rowed in data/b731_dispatch_rows.json. Replaced for b731 alone; the arms' names stand, their plants on b731's rows.
#⟪OVERRIDE checks 1129 1141⟫
def rebuild_wf_ok(S):
    """(R340)(7), as b730 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
#⟪OVERRIDE checks 1144 1159⟫
def runner_ok(S):
    """(R341), N1, b731: the dispatches of (R341)(3)-(4) -- at most twelve, all on zq-b730; every dispatch read by its run id; the rows' runs the worklist's."""
    rows = S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    return bool(disp) and len(disp) <= K.MAX_DISPATCHES \
        and sorted(str(r['run']) for r in disp) == sorted(str(r['run']) for r in reads) == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪OVERRIDE checks 1170 1173⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        pu_ = [j for j, r in enumerate(rows) if r.get('kind') == 'push' and r.get('sha') == d_.get('sha')]
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(pu_) == 1 and len(rd_) == 1 and pu_[0] < i_ < rd_[0]
#⟪END⟫
# ### b731, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R341)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks 1521 1521⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) == cr0(blob(ROOT, 'HEAD:tools/standing/hook.py')) \
        and [h[:8] for h in gs(ROOT, 'log', '--format=%H', '%s..HEAD' % PRE['relay'], '--', 'tools/standing/hook.py').split()] == [K.C1_STANDING] \
#⟪END⟫
#⟪OVERRIDE checks 1664 1664⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, edited this act by v1.11.0`s commit ca3f73f3 alone (the bank bound to act_current); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b731, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b730's record has twelve
#⟪OVERRIDE checks 983 983⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 13)) \
#⟪END⟫
# ### b731, Component 4 (the Edit tool): b731's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b730's override of checks 526 -- no registration commit -- removed: b731
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 754 754⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b731_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b731, Component 6 (the Edit tool): b731's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b730's wording
#⟪OVERRIDE checks 779 779⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b731, Component 4 (the Edit tool): b730's overrides of checks 1516 and 1659 (hook.py edited by b730's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b731 as it stands
# ### b731, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 988 988⟫
        and 'data/b731_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b731, Component 4 (the Edit tool): b730's override of checks 1476-1482 (one ERRATA entry at b730's (R340)(5)) removed -- (R341)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b731 as it stands
# ### b731, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b730's step-zero wording; b731's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 744 744⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks 745 745⟫
        and 'port-b707' in z and 'KEPT as banked: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b731, Component 4 (the Edit tool): G-RUNNER-READ's plant on b731's dispatch rows -- run 2's axiom lines carrying sorryAx (b730's
# ### plant read the lv rows' closure log, which b731 does not write)
#⟪OVERRIDE checks 1691 1691⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b731, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b731, Component 6 (the Edit tool): the fold bank was b730's own route
# ### (tools/b730_fold.py); b731's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b731_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1008 1008 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b730.py -> tools/acts/b731.py' in (rd('b731_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b731, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks 1011 1011 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b731_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b731, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b731_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 259 266 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b731_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b731, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R341): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 340 341⟫
    rows = [l for n_ in ('b731_defects.txt', 'b731_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R341) Component 4, the act`s events and defects together; relay data/b731_defects.txt, data/b731_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b731, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b731's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 395 396⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-DERIVES, annotated at b731, three of its five fields closed,',
    '        count and explicitFormula open, and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b731, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b730's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b731_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b731_registration_%s.txt' % __import__('b731_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b731, Component 4 (the Edit tool, before the face): b730's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b731, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b731's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b731, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R341)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b731 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b731, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b730's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b731 scorer reads; the needles set to the banks b731's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 906 907 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_logderiv.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b731, Component 4 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b730's ruling's form; (R341)(5) writes "kept: c2-b725, keiper-b725, detect-b729, zq-b730, and the rest as banked." naming port-b707 nowhere
# ### (data/b731_ferry.txt :17), so the arm failed on the act's real deletes; read as written, port-b707 still out of the deletes (defect (u))
#⟪OVERRIDE checks 767 770 REPAIR (needle)⟫
    # ### (R340)(9) wrote "port-b707 kept;" and (R341)(5) writes "kept: c2-b725, keiper-b725, detect-b729, zq-b730, and the rest as banked."; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or 'kept: c2-b725, keiper-b725, detect-b729, zq-b730, and the rest as banked' in S['ferry']) \
#⟪END⟫
# ### b731, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b731_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrs'))   # ### (a)-(s), entered before the lock, every one the seat's (data/b731_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b731_corrigendum.txt', 'data/b731_standing_v1110.txt', 'data/b731_logderiv_plan.txt', 'data/b731_zeros_plan.txt', 'data/b731_bound_check.txt', 'data/b731_logderiv.txt', 'data/b731_logderiv.json',
                  'data/b731_zeros.txt', 'data/b731_zeros.json', 'data/b731_price_measured.txt', 'data/b731_dispatch_rows.json',
                  'data/b731_reproduce.txt', 'data/b731_reproduce.json', 'data/b731_address_scan.txt', 'data/b731_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b731 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R341)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b731_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R341)(1)-(5), Component 4 (b731's keys over b731's objects): the order by time and ancestry; v1.11.0's controls; the two plans, the bound's control, the two grades, the dispatch rows and the price bank;
        # ### the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the plan at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1110', K.STANDING_COMMIT, K.C1_STANDING), ('v1110_corr', K.C1_STANDING, K.C1_CORR), ('corr_plan', K.C1_CORR, K.REG_COMMIT), ('plan_zplan', K.REG_COMMIT, K.ZEROS_REG_COMMIT))),
        v190=rd('b731_standing_v1110.txt'), ld=rd('b731_logderiv.txt'), ldj=jl('b731_logderiv.json'), zf=rd('b731_zeros.txt'), zfj=jl('b731_zeros.json'), plan=rd('b731_logderiv_plan.txt'), zplan=rd('b731_zeros_plan.txt'), bound=rd('b731_bound_check.txt'), price=rd('b731_price_measured.txt'),
        zq_src=dict((m_, _s(blob(EF, '%s:SIDEExplicitFormula/Schema/ZQ/%s.lean' % (K.ZQ_TIP, m_)))) for m_ in K.ZQ_MODULES),
        zq_files=gs(EF, 'diff', '--name-only', K.EF_BASE, K.ZQ_TIP).split(),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b731_dispatch_rows.json') or '[]'), reproduce=rd('b731_reproduce.txt'), reproducej=jl('b731_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b731_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b730 left them
        rebuild=None, rebuild_rows=json.loads(rd('b731_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               order=_ct(PP, K.C2_PP), plan=_ct(ROOT, K.REG_COMMIT), lean=_ct(EF, K.ZQ_FIRST), zplan=_ct(ROOT, K.ZEROS_REG_COMMIT), zlean=_ct(EF, K.ZQ_ZEROS_FIRST),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.REG_COMMIT),
                   c3=files_of(ROOT, K.ZEROS_REG_COMMIT), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b731's read-first bank's items by path, as its step zero wrote them (data/b731_readfirst.txt :9-:22)
READFIRST_NEEDLES = ('relay data/b730_closing.txt |', 'relay data/b730_events.txt |', 'relay data/b730_defects.txt |', 'relay data/b730_continuation.txt |', 'relay data/b730_continuation_plan.txt |',
                     'relay data/b729_count_price.txt |', 'SIDE-explicit-formula Schema/EpsteinZQ.lean |', 'SIDE-explicit-formula Schema/Wide/Config.lean |', 'SIDE-explicit-formula Zeta23/RvM/LocalCount.lean |',
                     'Mathlib de5ce8a9 NumberTheory/LSeries/Convolution.lean |', 'Mathlib de5ce8a9 NumberTheory/LSeries/Deriv.lean |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R341)(1)-(2))', 'logDeriv FIELD ((R341)(3))', 'zeros FIELD ((R341)(4))', 'PRICE BANK ((R341)(2)(ii), (4))', 'NAME AND ADDRESS ((R341)(5))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (83 = 82 + 1, data/b731_citation_check.txt, the one miss printed there and decided in data/b731_stepzero.txt :19-:20); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 1 and int(m.group(1)) == 83 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b730's figures, read at FINDINGS :12367 as Component 1 landed them
    return landed(S, 0, ['b730 AT ITS WEIGHT', 'suite 112 of 116', 'the closing’s d0bedc7d', '23 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b731's title in the ferry's Component 4 form (the record tool's _title over the banks); the first needle lower-case, the arm folding the article
TITLE_NEEDLES = ('W-ORD-ZQ-DERIVES: the logDeriv field CLOSED', ', the zeros field CLOSED', ', three of five fields closed', '; the author’s three repairs landed', ' repairs in all')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R341)(1)-(2): the generated entry for b730's twelve events and twenty-three defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(12), the defects by the one lettering, no dated note; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 2, CLOSE 33 over 35, REPEAT 10); the repairs at tools/standing/ v1.11.0 by their controls
    bank; the corrigenda bank appended at row (51) and nothing before it changed; in Component 1's commits (the figures read from
    data/b731_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 23 and len(items) == j.get('items') == 35 and j.get('row') == 51 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 35 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 2 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 10 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.11.0' and (j.get('repairs') or {}).get('bank') == 'data/b731_standing_v1110.txt' \
        and len(j.get('notes') or []) == 0 \
        and '  (51) ' in S['corrigenda'] and '  (52) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b731_rules.txt and data/b732_rules.txt, by form in (R341)(5)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b730's form, its names b731's); no author's word of b731 orders a rules row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b731_rules.txt')) and not os.path.exists(os.path.join(D, 'b732_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b731's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- THE logDeriv FIELD', 'KERNEL -- THE zeros FIELD', 'CERTIFIED -- tools/standing/ v1.11.0', 'REGISTERED -- W-ORD-ZQ-DERIVES', 'REGISTERED -- THE PRICE BANK',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b731: the dispatches of (R341)(3)-(4) -- each `gh workflow run` command of the capture a row of the bank, the rows' count the worklist's and within the cap, every
    row's free memory at or above the hold, each push before its dispatch and each dispatch before its read; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('push', 'dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by sha and by run id
    order = all(any(p.get('kind') == 'push' and p.get('sha') == d.get('sha') and seq_.index(p) < seq_.index(d) for p in seq_)
                and any(r.get('kind') == 'read' and str(r.get('run')) == str(d.get('run')) and seq_.index(r) > seq_.index(d) for r in seq_) for d in seq_ if d.get('kind') == 'dispatch') and bool(seq_)
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (the ledgers alone), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b731's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The plans**', '**The logDeriv field**', '**The zeros field**', '**What the fields are not**', '**The price bank**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b731_corrigendum.txt', 'data/b731_standing_v1110.txt', 'data/b731_logderiv.txt', 'data/b731_logderiv_plan.txt', 'data/b731_zeros.txt', 'data/b731_zeros_plan.txt', 'data/b731_bound_check.txt', 'data/b731_price_measured.txt', 'data/b731_dispatch_rows.json',
                 'data/b731_reproduce.txt', 'data/b731_address_scan.txt', 'data/b731_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b731: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R341)(3)-(5), N2 (the name the frozen run list carries): (2) whole before (3) -- the corrigendum's commit at or before the logDeriv plan's by time, across repositories, and an ancestor of it; each plan's commit before the first Lean commit of its field on zq-b730,
    the zeros plan after the logDeriv plan by ancestry; the first plan at HEAD its text at its commit; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    return K.REGISTRATIONS in S['files']['reg'] and bool(reg) and reg == head \
        and all(bool(t_.get(k_)) for k_ in ('order', 'plan', 'lean', 'zplan', 'zlean')) and t_['order'] <= t_['plan'] < t_['lean'] and t_['lean'] <= t_['zplan'] < t_['zlean'] \
        and 'data/b731_zeros_plan.txt' in S['files']['c3'] \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R341)(5), N5, the scan arm (the name the frozen run list carries): tools/b731_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    SIDE-explicit-formula's zq-b730; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address and name read from
    history and held in memory -- the address 0, the author's name 0, the previous name 0, its four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R341)(3), N2, N3 (the name the frozen run list carries): the bound's numerical control before any Lean: its foot printing Z_Q(3/2), the route's total below 4 and the pointwise step on the grid; the bank and its tool in the logDeriv plan's commit, before the first Lean commit. A float control, not the proof; zq_three_halves_tsum_lt is the proof, read by the grade."""
    m = re.match(r'Z_Q\(3/2\) ABOUT ([0-9.]+) ; THE ROUTE`S TOTAL ([0-9.]+) ; POINTWISE STEP HOLDS ON THE GRID True\.?$', _vlast(S['bound']))
    return bool(m) and float(m.group(1)) < float(m.group(2)) < 4 \
        and 'data/b731_bound_check.txt' in S['files']['reg'] and 'tools/b731_bound_check.py' in S['files']['reg']
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R341)(3)-(4), N1, N3 (the name the frozen run list carries): each field's bank -- every dispatch read by its run id, at most six a field and twelve in all; the field's last read at build exit 0, no sorryAx, its terminals at the standard three in the
    artifact's own lines; the field's modules at the tip carrying no sorry and no axiom; the foot's grade, dispatches and lines the rows' and the tip's; a grade CLOSED only so."""
    rows = S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    src = S['zq_src'] or {}
    three = "' depends on axioms: [propext, Classical.choice, Quot.sound]"

    def one(prefix, name, term, terms, mods, bank, j, tip, cap):
        d_ = [r for r in disp if (r.get('item') or '').startswith(prefix)]
        r_ = [r for r in reads if (r.get('item') or '').startswith(prefix)]
        last = r_[-1] if r_ else {}
        n_ = sum(len(src.get(m_, '').split(NL)) - 1 for m_ in mods)
        m = re.search(r'THE %s FIELD CLOSED: %s COMPILED ; AXIOMS propext, Classical\.choice, Quot\.sound ; NO sorry ; DISPATCHES (\d+) OF AT MOST %d ; LINES (\d+)\.' % (name, term, cap), _vlast(bank))
        return bool(m) and bool(d_) and len(d_) <= cap and sorted(str(r['run']) for r in r_) == sorted(str(r['run']) for r in d_) \
            and str(last.get('build_exit')) == '0' and not last.get('sorryAx') \
            and all(any(('ZQ.%s%s' % (t_, three)) in l for l in last.get('axioms_lines') or []) for t_ in terms) \
            and all(src.get(m_) and not re.search(r'\b(sorry|axiom)\b', src[m_]) for m_ in mods) \
            and int(m.group(1)) == len(d_) and int(m.group(2)) == n_ and j.get('grade') == 'CLOSED' and j.get('lines') == n_ and j.get('dispatches') == len(d_) and j.get('tip') == tip
    return len(disp) <= K.MAX_DISPATCHES and len(src) == 3 \
        and one('(3)', 'logDeriv', 'zq_logDeriv', ('zq_logDeriv',), K.ZQ_LOGDERIV_MODULES, S['ld'], S['ldj'] or {}, K.ZQ_LOGDERIV_TIP, K.MAX_LOGDERIV) \
        and one('(4)', 'zeros', 'zq_zeros', ('zq_zeros', 'exists_zq_zeros', 'zqZeroConfig', 'zq_conj'), K.ZQ_ZEROS_MODULES, S['zf'], S['zfj'] or {}, K.ZQ_TIP, K.MAX_ZEROS)
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R341)(6) (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip locally and at origin; no kernel's main moved (G-MERGES-ON-GATE's read); every Lean file of the act
    on zq-b730 alone, the branch's diff against main b730's four modules, this act's three and print_targets.txt and nothing else."""
    tp = S['ef_tips'] or {}
    want = sorted(['SIDEExplicitFormula/Schema/ZQ/%s.lean' % m_ for m_ in K.ZQ_MODULES_B730 + K.ZQ_MODULES] + ['print_targets.txt'])
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and sorted(S['zq_files'] or []) == want

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.11.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1110') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.11.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b730's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R341)(3)-(4), N1, N2 (the name the frozen run list carries): the two plans -- the statement, the route, the groups or module and the cap in each foot, nothing of the field on the branch at its commit; each field's spend within its cap; the price bank's foot: three rows measured, count and explicitFormula re-read and not touched."""
    p, z, r = _vlast(S['plan']), _vlast(S['zplan']), _vlast(S['price'])
    return 'THE FIELD STATED' in p and '3 GROUPS' in p and 'THE CAP SIX' in p and "NOTHING BUILT AT THIS BANK'S COMMIT" in p \
        and 'THE FIELD STATED' in z and '1 MODULE' in z and 'THE CAP SIX' in z and "NOTHING OF THE FIELD ON THE BRANCH AT THIS BANK'S COMMIT" in z \
        and (S['ldj'] or {}).get('dispatches', 99) <= K.MAX_LOGDERIV and (S['zfj'] or {}).get('dispatches', 99) <= K.MAX_ZEROS \
        and 'THREE ROWS MEASURED' in r and 'count AND explicitFormula RE-READ AND NOT TOUCHED' in r


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
    """standing clauses v9 (Component 7 of (R341): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b731_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b730's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R341-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b730's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R341) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b730's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R340)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 83 = 82 OK + 1 miss, the one printed and decided, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b730-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (W-ORD-ZQ-DERIVES; the logDeriv field; the zeros field; the fields closed; the author`s three repairs; the repairs in all), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R341)(1)-(2): the generated corrigendum for b730`s record, landed at FINDINGS :12369: its twelve events and twenty-three defects, 35 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 2 CLOSE 33, REPEAT 10; v1.11.0`s repairs by data/b731_standing_v1110.txt; the corrigenda bank appended at row (51)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b731 and no b732 rules bank: no author`s word of b731 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b731's objects
    ('G-REGISTRATIONS-FIRST', '(R341)(3)-(5), N2: the corrigendum`s commit at or before the logDeriv plan`s, each plan`s before the first Lean commit of its field on zq-b730; the logDeriv plan at HEAD its text at 4f610ea0; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_plan=False))),
    ('G-PREDICTION-FIRST', '(R341)(5), N5, the scan arm: tools/b731_address_scan.py run live over every commit of the act in the relay, PLACE-papers and zq-b730, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R341)(3), N2, N3: the bound`s numerical control: Z_Q(3/2) below the route`s total below 4, the pointwise step on the grid; the bank and its tool in the logDeriv plan`s commit',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'bound', (S['bound'] or '').replace('ON THE GRID True', 'ON THE GRID False'))),
    ('G-DERIVATION-GRADED', '(R341)(3)-(4), N1, N3: each field`s bank: at most six dispatches a field each read by its run id, its last at exit 0, no sorryAx, its terminals at the standard three, no sorry or axiom at the tip, the foot the rows`',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'drows', lambda d: [r.update(sorryAx=True) for r in d if r.get('kind') == 'read'])),
    ('G-OFFSET-POST-HOC', 'N5, (R341)(6): SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against main b730`s four modules, this act`s three and print_targets.txt alone',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at d0bedc7d, VERSION 9; v8 at HEAD its blob at d0bedc7d; no v10; v9`s commit an ancestor of v1.11.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R341)(3)-(4), N1, N2: each plan`s foot the statement, the route, its groups or module, the cap six and nothing of the field at its commit; each field`s spend within its cap; the price bank`s foot, three rows measured, count and explicitFormula re-read and not touched',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'plan', (S['plan'] or '').replace('THE CAP SIX', 'NO CAP'))),
    ('G-DIFFERS-ERRATA', '(R341): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in d660659, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b731_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R341-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b730`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at d0bedc7d (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: the dispatches of (R341)(3)-(4), twelve at most, each read by its run id; the rows` runs the worklist`s',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: each `gh workflow run` of the capture a row, the count within the cap, each push before its dispatch before its read, the rows` free memory at the hold; no b721-b730 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b730 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b730`s [41] tip; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers alone); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b730`s trail record on OPEN_TRAILS (:16959) and its root in the chain', lambda S: '### b730 — lane two, act one hundred and fifty-seven, the continuation act under (R340)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers alone): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b730`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: twelve at most; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b731, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R341)(3): a main at its sitting tip, its tags unmoved, is not a move against b730's face
#⟪OVERRIDE record 2554 2554⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b731: (R341)'s rows. (1)'s line quoted by the ruling from the public relay at d0bedc7d
    pub = _blob('D:/relay', 'd0bedc7d', 'data/b730_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b730_closing.txt :1, the head line as the public relay carries it at d0bedc7d', bool(pub) and pub[0] == at(cl, 1) and 'relay 25a434f1' in pub[0] and 'PLACE-papers 12abf2b' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root 991878af05fb436b', '1 prompt answered', 'scores 7 of 8 HELD', '23 defects'):
        add('ruling (1)', 'data/b730_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'data/b730_closing.txt :5, the counter CLAIM 2, CLOSE 33, REPEAT 10 OF 35', 'CLAIM 2, CLOSE 33, REPEAT 10 OF 35' in at(cl, 5), at(cl, 5)[-40:], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b730']]
    add('ruling (1)', 'data/act_roots.txt, b730`s root 991878af chained from b729`s 78885ea8', len(ar8_) == 1 and ar8_[0][1].startswith('991878af') and ar8_[0][2].startswith('78885ea8'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b730_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b730 (b730`s post-push part b3)', 'b730 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b730 AGREE' if 'b730 AGREE' in b3_ else 'ABSENT', '1')
    for f_, n_, w_ in (('b730_continuation.txt', 55, 'zq_continuation AND exists_zq_continuation COMPILED'), ('b730_continuation.txt', 55, 'AXIOMS propext, Classical.choice, Quot.sound'), ('b730_continuation.txt', 55, 'NO sorry'),
                       ('b730_continuation.txt', 55, 'DISPATCHES 6 OF AT MOST 12'), ('b730_continuation.txt', 55, 'LINES 835'), ('b730_continuation.txt', 55, 'ONE FIELD OF FIVE'), ('b730_detection_lemmas.txt', 11, 'D9')):
        add('ruling (1)', 'data/%s :%d carries %s' % (f_, n_, w_), w_ in at(lines_of(p('data', f_)), n_), at(lines_of(p('data', f_)), n_)[:50], '1')
    add('ruling (1)', 'data/b730_standing_v1100.txt, the controls 26 of 26', 'ALL AS WANTED' in (rd(p('data', 'b730_standing_v1100.txt')) or '') and '26' in (rd(p('data', 'b730_standing_v1100.txt')) or ''), 'read', '1')
    add('ruling (1)', 'tools/standing/VERSION v1.10.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.10.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(12) and 23 defects (data/b730_events.txt, data/b730_defects.txt)',
        starts == list(range(1, 13)) and len(letters) == 23, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((14, 6, "THE AUTHOR'S WORD [CLOSE ; NEW]"), (17, 7, 'CLOSE ; NEW'), (21, 9, 'CLOSE ; NEW')):
        add('ferry (read first)', 'event (%d) at data/b730_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:70], at(ev, n_)[:50], '1')
    add('ferry (read first)', 'data/b730_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    cp_ = lines_of(p('data', 'b729_count_price.txt'))
    for f_ in ('b729_count_price.txt', 'b730_author_answers.txt', 'b730_continuation_plan.txt', 'b730_continuation.txt', 'b730_detection_lemmas.txt', 'b730_defects.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    add('ruling (3)', 'data/b729_count_price.txt :23, (3) the logDeriv row at 200-400 lines, 3-8 dispatches', '200-400' in at(cp_, 23) and '3-8' in at(cp_, 23) and 'Convolution :142' in at(cp_, 23), at(cp_, 23)[:50], '3')
    add('ruling (4)', 'data/b729_count_price.txt :22, (3) the zeros row at 300-600 lines, 5-10 dispatches', '300-600' in at(cp_, 22) and '5-10' in at(cp_, 22), at(cp_, 22)[:50], '3')
    add('ruling (2)(ii)', 'data/b729_count_price.txt :21, (3) the continuation row at 1,500-3,000 lines, 25-50 dispatches', '1,500-3,000' in at(cp_, 21) and '25-50' in at(cp_, 21), at(cp_, 21)[:50], '3')
    add('ruling (4)', 'data/b729_count_price.txt :33, C4: Z_Q(3/2) bounded above by a rational, ABSENT', 'C4 Z_Q(3/2)' in at(cp_, 33) and 'ABSENT' in at(cp_, 33), at(cp_, 33)[:50], '3')
    ez_ = gr('D:/SIDE-explicit-formula', 'show', 'main:SIDEExplicitFormula/Schema/EpsteinZQ.lean').split(NL)
    fl_ = [at(ez_, n_).strip().split(' ')[0] for n_ in range(138, 143)]
    add('ruling (3)', 'ZQPremises has five fields, quoted from the structure at the pin, Schema/EpsteinZQ.lean :137-:142 (the author`s word at b729: a discharge sentence halts unless the count is so quoted)',
        at(ez_, 137).startswith('structure ZQPremises') and fl_ == ['continuation', 'zeros', 'logDeriv', 'explicitFormula', 'count'] and at(ez_, 143).strip() == '', ' '.join(fl_), '2')
    add('ruling (3)', 'Schema/EpsteinZQ.lean :140, the field logDeriv', 'logDeriv : ∀ s : ℂ, 3 / 2 ≤ s.re' in at(ez_, 140), at(ez_, 140)[:50], '2')
    add('ruling (4)', 'Schema/EpsteinZQ.lean :139, the field zeros', 'zeros : ZQZeros zq Z' in at(ez_, 139), at(ez_, 139)[:50], '2')
    for n_, w_ in ((153, 'theorem zq_count'), (157, 'theorem zq_explicit_formula'), (164, 'theorem zq_li_nonneg_imp_online')):
        add('ruling (3)', 'Schema/EpsteinZQ.lean :%d, %s' % (n_, w_), at(ez_, n_).startswith(w_), at(ez_, n_)[:40], '2')
    zt_ = (gr('D:/SIDE-explicit-formula', 'rev-parse', 'zq-b730') or '').strip()
    add('ferry (read first)', 'zq-b730 at 5688816e', zt_.startswith('5688816e'), zt_[:8], '3')
    gn_ = gr('D:/SIDE-explicit-formula', 'show', 'zq-b730:SIDEExplicitFormula/Chi/Generic.lean')
    add('ruling (4)', 'Chi/Generic.lean, read at the pin, chiZeroConfig used and its definition there', '\ndef chiZeroConfig' in gn_, 'defined there %s ; used %d times' % ('\ndef chiZeroConfig' in gn_, gn_.count('chiZeroConfig')), '2')
    cz_ = gr('D:/SIDE-explicit-formula', 'show', 'zq-b730:SIDEExplicitFormula/Chi/ZeroConfig.lean')
    add('ruling (4)', 'chiZeroConfig at Chi/ZeroConfig.lean, the form the field follows', 'chiZeroConfig' in cz_, 'read', '2')
    lc_ = gr('D:/SIDE-explicit-formula', 'show', 'zq-b730:Zeta23/RvM/LocalCount.lean')
    add('ferry (read first)', 'Zeta23/RvM/LocalCount.lean at the pin', 'half_count_large' in lc_, 'read', '2')
    ml_ = gr('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'rev-parse', 'HEAD')
    add('ruling (3)', 'Mathlib at de5ce8a9', ml_.startswith('de5ce8a9'), ml_[:12], '3')
    for f_, n_, w_ in (('Mathlib/NumberTheory/LSeries/Convolution.lean', 142, 'LSeriesHasSum.convolution'), ('Mathlib/NumberTheory/LSeries/Deriv.lean', 45, 'LSeries.hasDerivAt_term'), ('Mathlib/NumberTheory/LSeries/Deriv.lean', 105, 'LSeries.abscissaOfAbsConv_logMul')):
        add('ferry (read first)', '%s :%d, %s' % (f_, n_, w_), w_ in at(gr('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'show', 'HEAD:' + f_).split(NL), n_), 'read', '3')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ferry (read first)', 'OPEN_TRAILS :17009, the trail`s hand section at b730 carrying the author`s repairs', at(ot_, 17009).startswith('### b730 — the author’s answers at the root') and 'Carried to b731' in at(ot_, 17015), at(ot_, 17009)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ferry (read first)', 'REGISTRY :134, PHASE 1.5', at(rg_, 134).startswith('## PHASE 1.5'), at(rg_, 134)[:40], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    for k_ in ('SIDE-explicit-formula',):
        add('PATHS', '%s at D:/%s' % (k_, k_), os.path.isdir('D:/%s/.git' % k_), 'D:/' + k_, '0')
    add('ferry', 'tools/standing/ at v1.10.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.10.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R341)(5): b730's export, the mirror's last
    add('ruling (5)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-01-b730.zip, b730`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R341)(5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (5)', 'the push-b730-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R341)(5): act_current alone, then b730's step row 29 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b730_steps.json'),
                   (K.STEPZERO, 'data/b730_relay_push-b730-closing_push_out.txt')):
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
    add('ferry (read first)', 'data/b731_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b731_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b731 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b730_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.11.0's controls, the logDeriv field, the zeros field, the price bank, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R341)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R341)(7)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: on the branch zq-b730 of SIDE-explicit-formula alone, the three Lean modules of (R341)(3)-(4) and print_targets.txt; no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b732 ((R341)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R340)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b731 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-EIGHT, THE SECOND FIELD ACT: THE logDeriv AND zeros FIELDS ON zq-b730; '
              'THE AUTHOR`S THREE REPAIRS LANDED; v1.11.0 LANDED; THE PRICE BANK MEASURED, UNDER (R341).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b730's sections over b730's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.11.0: the composer reading the clauses into (W), the price bank`s measured row, a stamped route`s re-run, the post-lock scan`s bank, the seat`s three arms, the citation over the author`s word and the head line`s count of questions, each case failing before its repair and passing after', 'b731_standing_v1110.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE logDeriv FIELD ((R341)(3))', [
                ('the plan before any Lean, its re-price the seat`s', 'b731_logderiv_plan.txt'),
                ('the bound`s numerical control before any Lean', 'b731_bound_check.txt'),
                ('the field`s grade: each dispatch by its run id, the terminals` axiom print, the lines by module', 'b731_logderiv.txt')]),
            ('THE zeros FIELD ((R341)(4))', [
                ('the plan before any Lean of the field, its re-price the seat`s', 'b731_zeros_plan.txt'),
                ('the field`s grade: each dispatch by its run id, the terminals` axiom print, the lines by module', 'b731_zeros.txt')]),
            ('THE PRICE BANK ((R341)(2)(ii), (4))', [
                ('the three measured rows beside their estimates, count and explicitFormula re-read by each ratio and not touched', 'b731_price_measured.txt')]),
            ('THE NAME AND ADDRESS ((R341)(5))', [
                ('the scan over every commit and bank of the act, the counts alone', 'b731_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b730`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b731_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R340)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; on its branch zq-b730 alone the three Lean modules of (R341)(3)-(4) and print_targets.txt, pushed through push_gated.sh, off main, untagged ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1, twelve at most), each read by its run id, relay data/b731_dispatch_rows.json ; the rebuild-b721 branches of the wave 1 kernels as b730 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part, computation, push and dispatch ;',
    '    the push-b730-* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message ; N2: the corrigendum`s commit, each plan`s and its field`s first Lean commit in that order by time ;',
    '    N3: every grade at its bank`s end ; (R341)(5): no new occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay data/b731_address_scan.txt, data/b731_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the workflow dispatches under the GitHub login') + ' ;',
    '    nothing deposited ; the deposit route untouched, publish never called, the draft held at v5 ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) written ; no paper cut, moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt (b731`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.11.0 by (R341)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b730 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R341)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For b732, each from its bank: the fields count and explicitFormula, open, with W-ORD-ZQ-DERIVES (OPEN_TRAILS), their re-price at relay data/b731_price_measured.txt ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b731_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b730 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b730`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b731: the standing repairs are v1.11.0's ((R341)(2), relay data/b731_standing_v1110.txt, read in the corrigendum section); the
    # ### carry's diffs here (b731 carried at step zero before the fold; its tools since are the templates and tools/acts/b731.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b730 left them; port-b707 at b712`s tip %s)' % (
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
    b731's form over b731's objects (b730's form in git at b730's record tool): the corrigendum's foot and v1.11.0's controls; the two plans', the two grades', the bound control's and the price bank's feet;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1110.txt' % ACT, r'\*\*v1\.11\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.11.0`s controls')
    pl = _bfig('%s_logderiv_plan.txt' % ACT, r'THE FIELD STATED ; ROUTE ([^;]+?) ; (\d+) GROUPS, ABOUT (\d+) LINES, (\d+-\d+) DISPATCHES', 'the logDeriv plan`s foot')
    pz = _bfig('%s_zeros_plan.txt' % ACT, r'THE FIELD STATED ; ROUTE ([^;]+?) ; (\d+) MODULE, ABOUT (\d+) LINES, (\d+-\d+) DISPATCHES', 'the zeros plan`s foot')
    ld = _bfig('%s_logderiv.txt' % ACT, r'\*\*THE logDeriv FIELD (CLOSED): zq_logDeriv COMPILED ; AXIOMS ([^;]+?) ; NO sorry ; DISPATCHES (\d+) OF AT MOST (\d+) ; LINES (\d+)\.\*\*', 'the logDeriv field`s foot')
    zf = _bfig('%s_zeros.txt' % ACT, r'\*\*THE zeros FIELD (CLOSED): zq_zeros COMPILED ; AXIOMS ([^;]+?) ; NO sorry ; DISPATCHES (\d+) OF AT MOST (\d+) ; LINES (\d+)\.\*\*', 'the zeros field`s foot')
    th = _bfig('%s_bound_check.txt' % ACT, r'\*\*Z_Q\(3/2\) ABOUT ([0-9.]+) ; THE ROUTE`S TOTAL ([0-9.]+) ; POINTWISE STEP HOLDS ON THE GRID True\.\*\*', 'the bound control`s foot')
    pm = _bfig('%s_price_measured.txt' % ACT, r'\*\*THE PRICE BANK: (THREE) ROWS MEASURED ; count AND explicitFormula RE-READ AND NOT TOUCHED ;', 'the price bank`s foot')
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1110_ctl=v5[0], v1110_cases=v5[1], v1110_wanted=v5[2], repairs=len(v5[0].split(', ')),
                plan_route=pl[0], plan_groups=pl[1], plan_lines=pl[2], plan_disp=pl[3],
                zp_route=pz[0], zp_lines=pz[2], zp_disp=pz[3],
                ld_grade=ld[0], ld_axioms=ld[1], ld_disp=int(ld[2]), ld_cap=int(ld[3]), ld_lines=int(ld[4]),
                zf_grade=zf[0], zf_axioms=zf[1], zf_disp=int(zf[2]), zf_cap=int(zf[3]), zf_lines=int(zf[4]),
                closed=1 + sum(1 for g_ in (ld[0], zf[0]) if g_ == 'CLOSED'), ld_bound=(jl('%s_logderiv.json' % ACT).get('lines_by_module') or {}).get('Bound'),
                th_z=th[0], th_total=th[1], pm_rows=pm[0].lower(),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R341)(3)-(4): the kernel rows of one kind as banked (data/b731_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R341): no lean process runs on this host; the dispatches those of (R341)(3)-(4), twelve at most, each read by its run id. From the command bank (the seat's commands, read live from the
    capture by the `commands` route) and the dispatch rows beside the worklist's EF_RUNS."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b731_commands.json): %s; dispatch commands in the capture: %s, the worklist`s runs %d, each read by its run id: %s (relay data/b731_dispatch_rows.json)' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b731's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b731_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b731_logderiv.txt', '## THE CONTROLS FIRST', '## THE DISPATCHES'),
               ('data/b731_zeros.txt', '## THE CONTROLS FIRST', '## THE DISPATCHES'),
               ('data/b731_price_measured.txt', '## THE CONTROLS FIRST', '## THE THREE MEASURED ROWS'))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R341): (2) whole before (3), the corrigendum's commit before the logDeriv plan; each plan before any Lean file of its field, the order printed by time across the three repositories and by ancestry within the relay;
    each tool's controls before its figures."""
    chain_ = [(K.PP, K.C2_PP), (ROOT, K.REG_COMMIT), (K.EF_DIR, K.ZQ_FIRST), (ROOT, K.ZEROS_REG_COMMIT), (K.EF_DIR, K.ZQ_ZEROS_FIRST)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_[0] <= tm_[1] < tm_[2] <= tm_[3] < tm_[4]
    t = rdn('%s_logderiv_plan.txt' % ACT)
    tz = rdn('%s_zeros_plan.txt' % ACT)
    fg_ = rdn('%s_logderiv.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = "NOTHING BUILT AT THIS BANK'S COMMIT" in t and "NOTHING OF THE FIELD ON THE BRANCH AT THIS BANK'S COMMIT" in tz and order_ and all(o for _p, o in ctl) and bool(fg_)
#⟪END⟫
#⟪SECTION record 13⟫
        'the plans` feet, nothing of the field at each bank`s commit: %s, %s; the corrigendum, the logDeriv plan, its first Lean commit, the zeros plan and its first Lean commit in that order by time: %s (%s); the tools` controls before their figures: %s' % (
            "NOTHING BUILT AT THIS BANK'S COMMIT" in t, "NOTHING OF THE FIELD ON THE BRANCH AT THIS BANK'S COMMIT" in tz, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b731's objects; b730's in git at b730's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b731_standing_v1110.txt', ('ALL AS WANTED',)), ('b731_logderiv_plan.txt', ('THE FIELD STATED',)), ('b731_zeros_plan.txt', ('THE FIELD STATED',)), ('b731_bound_check.txt', ('POINTWISE STEP',)), ('b731_logderiv.txt', ('THE logDeriv FIELD',)),
             ('b731_zeros.txt', ('THE zeros FIELD',)), ('b731_price_measured.txt', ('THE PRICE BANK',)), ('b731_citation_check.txt', ('CITES CHECKED',)), ('b731_reproduce.txt', ('REPRODUCES',)), ('b731_address_scan.txt', ('PREVIOUS ADDRESS',)))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R341): every grade prints at its end; the entry's nouns the banks'; no sentence calls the instance DERIVES while a field is open (the order's own name not counted), or a field closed without its axiom print (the title's ferry form read apart, the head line beneath it carrying the axioms). From the banks' last
    lines and the entry's sentences."""
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
    bad = [s_ for s_ in sents if re.search(r'\binstance\b[^.;]*(?<!-)\bDERIVES\b', s_) or (not s_.lstrip().startswith('## ') and re.search(r'(?:logDeriv|zeros) fields?[^.;]*\bCLOSED\b', s_) and 'standard three' not in s_ and 'axiom' not in s_)]
    ok = all(o for _n, o in graded) and not bad
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the entry`s sentences calling the instance DERIVES or a field closed with no axiom print, read from %s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bad or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R341) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R341)(5))
# ### (R341)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R341) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b730's form, carried) -- read from git,
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
    # ### (R341)(3)-(4), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-explicit-formula's zq-b730 or a branch the worklist names at its tip; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b730 left them; the address scan's count from its bank (relay data/b731_address_scan.txt), the suite's arm recounting it live
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
                if not (kn == 'SIDE-explicit-formula' and r_[0] in tuple('refs/heads/' + b_ for b_, _t in K.EF_BRANCHES)):
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
            'the address scan (relay data/b731_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s named branches, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b731 — lane two, act one hundred and fifty-eight, the second field act under (R341): b730 at its weight and its corrigendum; v1.11.0; '
            'the logDeriv and zeros fields on zq-b730; the measured price rows')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## W-ORD-ZQ-DERIVES: the logDeriv field %s, the zeros field %s, %s of five fields closed; the author’s three repairs landed; %d repairs in all' % (f['ld_grade'], f['zf_grade'], num_word(f['closed']), f['repairs']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the bank’s 200-400 lines for logDeriv against %d spent: its row held no line for Z_Q(3/2) < 4, %s of those lines in Schema/ZQ/Bound.lean; the three rows and the spread of their ratios at relay data/b731_price_measured.txt, every estimate the seat’s and no one ratio chosen; (2) the count field’s A0 sentence carried on the order’s line, undecided until the author’s word; '
            '(3) step zero’s one citation miss, chiZeroConfig defined at Chi/ZeroConfig.lean and not Chi/Generic.lean, decided at relay data/b731_stepzero.txt :20; (4) ZQZeros asks no nonempty carrier and the theorem claims none, printed at relay data/b731_zeros.txt; '
            '(5) the two plans’ hand figures, 56-223 and 83-335, left unedited and read exact beside them at relay data/b731_price_measured.txt; ' % (f['ld_lines'], f['ld_bound']) +
            '(6) %s and the seat’s %s defect%s as lettered' % (
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
            'author beside the next act of (R341)(7)): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b731's objects; b730's composer in git at
    b730's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R340)(2)(v)
    e = ['', _title(), '',
         'The logDeriv field of ZQPremises is %s and the zeros field %s, each with the standard three on zq-b730: zq_logDeriv at axioms %s, %d dispatches of at most %d, %d lines; zq_zeros and exists_zq_zeros at axioms %s, %d dispatch%s of at most %d, %d lines; no sorry in either. With b730’s continuation %s of five fields stand closed; count and explicitFormula stay named premises, the Epstein theorems still bind them and the grade of those theorems does not move; '
         'the author’s three repairs landed among %d at tools/standing/ %s; the draft stands at v5, HELD.' % (
             f['ld_grade'], f['zf_grade'], f['ld_axioms'], f['ld_disp'], f['ld_cap'], f['ld_lines'], f['zf_axioms'], f['zf_disp'], '' if f['zf_disp'] == 1 else 'es', f['zf_cap'], f['zf_lines'], num_word(f['closed']), f['repairs'], f['ver']), '',
         '*Filed at b731 on the author’s ruling `(R341)`; %d question%s put before the root. Banks: relay '
         '`data/b731_corrigendum.txt`, `data/b731_standing_v1110.txt`, `data/b731_logderiv_plan.txt`, `data/b731_bound_check.txt`, `data/b731_logderiv.txt`, `data/b731_zeros_plan.txt`, `data/b731_zeros.txt`, `data/b731_price_measured.txt`, `data/b731_dispatch_rows.json`, '
         '`data/b731_reproduce.txt`, `data/b731_address_scan.txt`, `data/b731_touch.txt`, `data/b731_standing_figures.txt`, `data/b731_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R341)(1)-(2), `%s`, `%s`, `%s`): b730 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b730’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b731_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b731_standing_v1110.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1110_ctl'], f['v1110_cases'],
             f['v1110_wanted']), '',
         '**The plans** ((R341)(3)-(5), N2): (2) whole before (3): the corrigendum at PLACE-papers `%s` before the logDeriv plan at relay `%s`, that plan before the first Lean commit `%s` on zq-b730, the zeros plan at relay `%s` before its field’s first Lean commit `%s`. The bound’s float control stands in the first plan’s commit: Z_Q(3/2) about %s against the route’s total %s, a control and not a proof (relay data/b731_bound_check.txt).' % (
             K.C2_PP[:8], K.REG_COMMIT[:8], K.ZQ_FIRST[:8], K.ZEROS_REG_COMMIT[:8], K.ZQ_ZEROS_FIRST[:8], f['th_z'], f['th_total']), '',
         '**The logDeriv field** ((R341)(3), N1, N3): the plan’s route %s, %s groups, about %s lines and %s dispatches, the seat’s. Spent %d dispatches, each read by its run id, %d lines in Schema/ZQ/Bound.lean and LogDeriv.lean; zq_logDeriv at axioms %s by the artifact’s own print. The first two reads showed a conclusion of success over build exit 1, and the exit file governed (relay data/b731_logderiv.txt, data/b731_dispatch_rows.json).' % (
             f['plan_route'], f['plan_groups'], f['plan_lines'], f['plan_disp'], f['ld_disp'], f['ld_lines'], f['ld_axioms']), '',
         '**The zeros field** ((R341)(4), N1, N3): the plan’s route %s, about %s lines and %s dispatches, the seat’s. Spent %d dispatch%s, read by its run id, %d lines in Schema/ZQ/Zeros.lean at `%s`; zq_zeros, exists_zq_zeros, zqZeroConfig and zq_conj at axioms %s by the artifact’s own print (relay data/b731_zeros.txt, data/b731_dispatch_rows.json).' % (
             f['zp_route'], f['zp_lines'], f['zp_disp'], f['zf_disp'], '' if f['zf_disp'] == 1 else 'es', f['zf_lines'], K.ZQ_TIP[:8], f['zf_axioms']), '',
         '**What the fields are not**: each theorem says its clause of ZQPremises and no more. zq_zeros says the zeros of Lambda_Q off 0, 1 and the trivial zeros, with their orders, form a WideConfig; it does not say the carrier is nonempty, counts nothing and places no zero on any line. Wide.HCount, the field count, is not touched. The fields count and explicitFormula stay named premises and the Epstein theorems still bind them. Nothing here proves RH or GRH; the files are on the branch alone, not on main, no tag.', '',
         '**The price bank** ((R341)(2)(ii), (4)): %s rows measured beside their estimates in I-10’s form, each a floor on one route; count and explicitFormula re-read by each ratio and not touched. The ratios disagree, the spread is printed and no one ratio is chosen (relay data/b731_price_measured.txt).' % f['pm_rows'], '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b731_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R341)(5), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b731_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b731_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b731 -- %s, %s, %s, %s -- against b730’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b731_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the price repair and the fields read one way: an estimate stands beside a measurement now, and the two missed in both directions; a measured row replaces no estimate of a field not built.', '',
         '**Carried to:** %s: the fields count and explicitFormula, open, their re-price printed; the count field’s A0 sentence, on the author’s word; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b730():
    """b730's form over b730's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b731's objects; b730's composer in git at b730's record tool): W-ORD-ZQ-DERIVES annotated by its own line, then the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD with that line beneath it."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['**`W-ORD-ZQ-DERIVES` CARRIED at b731, (R341)(3)-(4):** the fields logDeriv %s and zeros %s with the standard three at zq-b730 `%s`, %s of five with b730’s continuation; count and explicitFormula open.' % (f['ld_grade'].lower(), f['zf_grade'].lower(), K.ZQ_TIP[:8], num_word(f['closed']))]
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-ZQ-DERIVES' not in op:
        sys.exit('### THE TRAIL: AN ANNOTATED ORDER NOT READ OPEN BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R341) ratified.** Its components as the ferry orders them (relay data/b731_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b730’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders annotated** ((R341)(3)-(4)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the line above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b731_standing_v1110.txt).' % (
                 f['ver'], f['v1110_cases'], f['v1110_wanted']), '',
             '**The logDeriv field:** %s with the standard three, axioms %s, %d dispatches of at most %d, %d lines, on zq-b730 (relay data/b731_logderiv.txt).' % (
                 f['ld_grade'], f['ld_axioms'], f['ld_disp'], f['ld_cap'], f['ld_lines']), '',
             '**The zeros field:** %s with the standard three, axioms %s, %d dispatch%s of at most %d, %d lines, on zq-b730 at `%s`; count and explicitFormula open (relay data/b731_zeros.txt).' % (
                 f['zf_grade'], f['zf_axioms'], f['zf_disp'], '' if f['zf_disp'] == 1 else 'es', f['zf_cap'], f['zf_lines'], K.ZQ_TIP[:8]), '',
             '**The price bank:** %s rows measured, count and explicitFormula re-read and not touched (relay data/b731_price_measured.txt).' % f['pm_rows'], '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b731_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b731_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b731_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b731 `%s` (previous `%s`, b730’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b731_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b731_standing_v1110.txt); the standing '
             'report tool (relay data/b731_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no main written, no tag; on SIDE-explicit-formula’s zq-b730 alone the three Lean modules of (R341)(3)-(4) and print_targets.txt, %d dispatches each read by its run id; the %s branches as b730 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b731_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b730’s %s, %s, %s, %s (relay data/b731_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b731_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b730():
    """b730's trail record over b730's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: those of (R341)(3)-(4), twelve at most; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b731*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730, kept, zq-b730 moved by (R341)(3)-(4); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b730 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b731*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b730`s and this act`s; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R341)(5): relay push-b730-closing, push-b730-preroot, push-b730-record; PLACE-papers push-b730-preroot, push-b730-record; each local, by name, after --merged listed it (data/b731_stepzero.txt).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: the Lean modules and print_targets.txt.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R341) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (12abf2bd) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R341)(1)-(2): FINDINGS :12369.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R341)(1)-(2): row (51).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-DERIVES annotated by the trail, entered at b730.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b731_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.11.0`s controls, the bound control, the two grades, the price bank, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the logDeriv plan committed with its bound control at 4f610ea0; the zeros plan at ca204110.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### the two grades, after the first plan; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none of this act`s.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### (R341)(3)-(4): MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R341)(2): tools/standing/ to v1.11.0, each repair with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended; data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation and push; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R341)(5), N5: PREVIOUS ADDRESS 0; MEASURED off data/b731_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, gh reads and the workflow dispatches; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### (R341)(3)-(4): the figure banks of the planned objects
    fig_banks = [p for p in ('data/b731_logderiv.txt', 'data/b731_zeros.txt')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b731_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b731_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1110', 'bound_check', 'logderiv', 'zeros', 'price_measured', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b731_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b731_registration_%s.txt -- b731, THE SECOND FIELD ACT: b730 AT ITS WEIGHT AND ITS CORRIGENDUM; THE AUTHOR`S THREE REPAIRS, v1.11.0; "
                             "THE logDeriv AND zeros FIELDS ON zq-b730; NO DEPOSIT, NO TAG, UNDER (R341)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b730's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b731: b730's lines read banks this
act does not write, and are not carried; the lines are b731's: the logDeriv and zeros fields (KERNEL, on the runner only), tools/standing/ v1.11.0 by its controls (CERTIFIED), the order and the price bank
(REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b731's lines, each from the record tool's figures over b731's banks
    # ------------------------------------------------------------------ KERNEL: (R341)(3)-(4), on the runner only
    sz = seat('%s_logderiv.txt' % ACT, '**THE logDeriv FIELD ')
    sk = sz   # ### (R340)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- THE logDeriv FIELD: %s, zq_logDeriv, axioms %s, %d dispatches of at most %d each read by its run id, %d lines, on zq-b730 alone. SOURCE %s.' % (f['ld_grade'], f['ld_axioms'], f['ld_disp'], f['ld_cap'], f['ld_lines'], sz['text']))
    s0 = seat('%s_zeros.txt' % ACT, '**THE zeros FIELD ')
    seats.append(s0)
    keys['ZQ0'] = ('KERNEL -- THE zeros FIELD: %s, zq_zeros and exists_zq_zeros, axioms %s, %d dispatch%s of at most %d read by its run id, %d lines, on zq-b730 alone. SOURCE %s.' % (f['zf_grade'], f['zf_axioms'], f['zf_disp'], '' if f['zf_disp'] == 1 else 'es', f['zf_cap'], f['zf_lines'], s0['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.11.0 ((R341)(2)), by its controls
    sw = seat('%s_standing_v1110.txt' % ACT, '**v1.11.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1110'] = ('CERTIFIED -- tools/standing/ v1.11.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1110_ctl'], f['v1110_cases'], f['v1110_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the order and the price bank, each read from its bank
    so = seat('%s_ferry.txt' % ACT, "(7) THE ACT'S PLACE ON THE PAPER PATH")
    keys['ORD'] = ('REGISTERED -- W-ORD-ZQ-DERIVES: five fields, %s closed, count and explicitFormula open. SOURCE %s.' % (REC.num_word(f['closed']), so['text']))
    sv = seat('%s_price_measured.txt' % ACT, '**THE PRICE BANK: ')
    keys['DL'] = ('REGISTERED -- THE PRICE BANK: %s rows measured, count and explicitFormula re-read and not touched. SOURCE %s.' % (f['pm_rows'], sv['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R341)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ', 'ZQ0']), ('CERTIFIED', ['V1110']), ('REGISTERED', ['ORD', 'DL']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b731 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
