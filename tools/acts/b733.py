# -*- coding: utf-8 -*-
# b733 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R343)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R343)(2) repair it carries. Edited by the Edit tool. Carried at b733 by tools/b733_fold.py (`carry`) from tools/acts/b732.py,
# b732`s names substituted; the citation`s sections adopted from tools/b733_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b732`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b732`s carried till
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
# ### b733, Component 1 (the Edit tool): THE c1 ROUTE FOR b732'S WEIGHT LINE AND ITS CORRIGENDUM, (R343)(1)-(2). Carried from b732's
# ### override and rewritten here against b732's own banks: the closing's lines by needle, the events (12), the defects (23), the refusals
# ### (4), the v1.11.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = '5a7d5778'          # ### b732's closing commit
C1_REFUSAL_AT = '5a7d5778'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-01'
C1_CORRIGENDA_LAST = 51
C1_V170 = 'b733_standing_v1120.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-01 by b733 to b732’s entry (:%d), under `(R343)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-ZQ-DERIVES: the logDeriv field CLOSED'
C1_TRAIL_NEEDLE = '### b732 — lane two, act one hundred and fifty-eight, the second field act under (R342)'
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
    for l in _c1_rd('b732_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b732_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b732_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b732_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b732_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b732_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b732_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b732_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 7:
        sys.exit('### data/b732_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b732_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b732_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 11)) or len(dr) != 19:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b732 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b732_closing.txt):* “%s” (data/b732_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b732_steps.json, the record and closing rows). As its rows read: the logDeriv and zeros fields CLOSED on zq-b730 at 23b006df with the standard three, no sorry, 786 and 340 lines, 3 and 1 dispatches, three of five fields; '
            'the measured rows beside the estimates, the ratios 0.278-0.557, 1.965-3.930 and 0.567-1.133 on lines (data/b732_price_measured.txt :17-:19); count and explicitFormula untouched; the standing tools v1.11.0, 17 cases as wanted (data/b732_standing_v1110.txt); '
            'the scores 7 of 8 HELD, N4 REFUTED on 044063b0 by the author’s word, N3 HELD on the seat’s hand read, its reader not reading the landed entry (data/b732_events.txt row (10)). '
            'The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both (:%d, :%d); the counter CLAIM %s, CLOSE %s, REPEAT %s of %s (:%d). '
            'The root %s over %s banks, chained from %s (data/b732_act_root.json; :%d), the chain AGREE b624-b732; %s questions banked as put by the seat (:%d), in two calls; %d events in data/b732_events.txt, rows (1)-(%d); %d defects, (a)–(s) '
            '(data/b732_defects.txt). '
            'Nothing deposited, no draft published; the corrigendum for these rows follows, under `(R343)`(1)-(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                cc, cd, rp, rn, l_cn, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b732's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '14:04:16Z', 'defect (d)'), (2, 'ENV', '14:55:36Z', 'defect (j)'), (3, 'PIPE', '15:18:42Z', 'defect (p)'), (4, 'PIPE', '15:34:02Z', 'defect (r)')]
C1_CORR_TITLE = ('## Corrigendum to b732’s record (relay data/b732_events.txt rows (1)-(10) and data/b732_defects.txt): ten events and nineteen defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the author’s repair at its head, the act module rendered and the dropped name failing the pre-lock dry; the re-price computed from the banks, the Lean paths and the declarations beside them read against the tree, '
                 'the N3 reader keyed to the landed lines, at tools/standing/ v1.12.0, each controlled on b732’s banks, under (R343)(1)-(2)')


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
    rl = _c1_git('show', '%s:data/b732_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b732_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.12.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=[])
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(10)', sorted(ev) == list(range(1, 11))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 19', len(dr) == 19), ('the refusals 4, each answered as listed', len(rl) == 4 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.12.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.12.0
C1_EV_EXTRA = {1: '; repair (module): the render refuses the drop, the dry reads the name before any lock', 2: '; the reading behind the word; no file touched', 3: '; repair (module); N4 stands REFUTED unreworded by the author’s word', 4: '; the form `scan --bank` carried',
               5: '; no arm dead; read again at the pre-push suite', 6: '; the order of the two stands as it ran', 7: '; rows (2)-(5) carried by dated note, no locked bank edited', 8: '; `record counter` reads the bank whole; the record not rewritten',
               9: '; the refusal did its work', 10: '; repair (n3); N3 stands HELD on the hand read, unreworded'}
C1_CLASSES = (
    ('module', 'the act module rendered, a render that drops a name any arm calls failing the pre-lock dry (`(R343)`(2)(i), events (1)-(3), the author’s word)', 'standing.actmodule puts the act’s own sections, tools/<act>_sections.txt, over the carried module and refuses, writing nothing, where a block dropped a function the rest still reads; standing.reportdry now reads all seven rendered tools by the compiler’s symbol table, step [5a], a live name failing the bank the seal requires. b732’s module at its lock, blob d7a0c14e, reads live research_reproduces_ok; the restored blob reads none'),
    ('reprice', 'the re-price computed from the banks (`(R343)`(2)(ii), defect (o))', 'standing.pricebank.reprice_read reads the estimates from the price bank and the measured row from the measured bank, no figure typed: 55-223 and 83-334 against the plans’ hand 56-223 and 83-335. The plans are not edited'),
    ('leanpath', 'the citation check reads every Lean path a ruling or ferry names against the tree at the pin (`(R343)`(2)(iii))', 'standing.cites.lean_rows halts the check on a path no tree holds. The instance is not of that kind: Chi/Generic.lean STANDS in the tree, and chiZeroConfig, the declaration (R342)(4) cites it for, stands in Chi/ZeroConfig.lean; so the nearest declaration before a path, declared elsewhere, halts too. A check of absent paths alone would have passed the instance'),
    ('n3', 'the N3 reader keyed to the landed entry’s lines, with a plant (`(R343)`(2)(iv), event (10))', 'standing.act.landed_entry reads the entry from PLACE-papers by the bank’s line and bytes and raises where the line does not read the bank’s head, never falling to the composer; b732’s entry and b730’s read by the tool, the byte span beside as the hand read, equal; the planted key and the planted sentence each caught; the template’s line count kept'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b732’s events bank (relay data/b732_events.txt) carries ten rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank nineteen lettered rows, (a)-(s), each tagged in its own bracket (%s); its refusal bank four lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R343)`(2), at tools/standing/ v1.12.0, each with a control on b732’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b732’s events (1)-(10):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?(\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?|post-push|pre-push and post-push): ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b732_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b732’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b732_defects.txt; %s; %s; %s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c))]
    L += ['', '**b732’s refusals** (relay data/b732_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (ten events, nineteen defects), as b732’s closing prints it (relay data/b732_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b733 on the author’s ruling `(R343)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b733.py) from '
          'b732’s events and defects banks read unedited, its refusal bank, and the v1.12.0 controls bank; banked as relay `data/b733_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b732’s record; no sealed tool, face, trail or root-named bank of b732 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b733 -- THE CORRIGENDUM FOR b732, (R343)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b732_events.txt rows (1)-(10), data/b732_defects.txt 19 rows, data/b732_hook_refusals.txt 4 '
             'lines at %s; data/%s (the v1.12.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 10, DEFECTS 19 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.12.0: THE ACT MODULE RENDERED, THE RE-PRICE FROM THE BANKS, '
               'THE LEAN PATHS AGAINST THE TREE, THE N3 READER ON THE LANDED LINES ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b732 at its weight after its entry, and the corrigendum for b732, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.12.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b733, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b733 ran three
# ### ((R343)(4)(iii)-(iv), N1), rowed in data/b733_dispatch_rows.json. Replaced for b733 alone; the arms' names stand, their plants on b733's rows.
#⟪OVERRIDE checks 1129 1141⟫
def rebuild_wf_ok(S):
    """(R342)(7), as b732 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R343), N1, b733: the dispatches of (R343)(3)-(4) -- at most twelve, all on zq-b732; every dispatch read by its run id; the rows' runs the worklist's."""
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
# ### b733, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R343)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks 1521 1521⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % PRE['relay'])) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks 1664 1664⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, unedited this act (its blob at the act`s base the same); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b733, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b732's record has twelve
#⟪OVERRIDE checks 983 983⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 11)) \
#⟪END⟫
# ### b733, Component 4 (the Edit tool): b733's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b732's override of checks 526 -- no registration commit -- removed: b733
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 754 754⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b733_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b733, Component 6 (the Edit tool): b733's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b732's wording
#⟪OVERRIDE checks 779 779⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b733, Component 4 (the Edit tool): b732's overrides of checks 1516 and 1659 (hook.py edited by b732's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b733 as it stands
# ### b733, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 988 988⟫
        and 'data/b733_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b733, Component 4 (the Edit tool): b732's override of checks 1476-1482 (one ERRATA entry at b732's (R342)(5)) removed -- (R343)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b733 as it stands
# ### b733, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b732's step-zero wording; b733's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 744 744⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks 745 745⟫
        and 'port-b707' in z and 'KEPT as banked: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b733, Component 4 (the Edit tool): G-RUNNER-READ's plant on b733's dispatch rows -- run 2's axiom lines carrying sorryAx (b732's
# ### plant read the lv rows' closure log, which b733 does not write)
#⟪OVERRIDE checks 1691 1691⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b733, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b733, Component 6 (the Edit tool): the fold bank was b732's own route
# ### (tools/b732_fold.py); b733's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b733_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1008 1008 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b732.py -> tools/acts/b733.py' in (rd('b733_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b733, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks 1011 1011 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b733_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b733, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b733_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 259 266 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b733_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b733, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R343): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 340 341⟫
    rows = [l for n_ in ('b733_defects.txt', 'b733_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R343) Component 5, the act`s events and defects together; relay data/b733_defects.txt, data/b733_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b733, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b733's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 395 396⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-DERIVES, annotated at b733, three of its five fields closed,',
    '        count and explicitFormula open, and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b733, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b732's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b733_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b733_registration_%s.txt' % __import__('b733_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b733, Component 4 (the Edit tool, before the face): b732's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b733, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b733's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b733, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R343)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b733 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b733, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b732's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b733 scorer reads; the needles set to the banks b733's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 906 907 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_logderiv.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b733, Component 4 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b732's ruling's form; (R343)(5) writes "kept: c2-b725, keiper-b725, detect-b729, zq-b732, and the rest as banked." naming port-b707 nowhere
# ### (data/b733_ferry.txt :17), so the arm failed on the act's real deletes; read as written, port-b707 still out of the deletes (defect (u))
#⟪OVERRIDE checks 767 770 REPAIR (needle)⟫
    # ### (R342)(9) wrote "port-b707 kept;" and (R343)(5) writes "kept: c2-b725, keiper-b725, detect-b729, zq-b732, and the rest as banked."; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or 'kept: c2-b725, keiper-b725, detect-b729, zq-b732, and the rest as banked' in S['ferry']) \
#⟪END⟫
# ### b733, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b733_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqrstuvwxyz') + ("a'", "b'", "c'", "d'")))   # ### (a)-(z), (a')-(d'), entered before the lock, every one the seat's (data/b733_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b733_corrigendum.txt', 'data/b733_standing_v1120.txt', 'data/b733_objects_rule.txt', 'data/b733_objects.txt', 'data/b733_door_controls.txt', 'data/b733_phase2_doors.txt', 'data/b733_a0_restatement.txt',
                  'data/b733_phase2_frontdoors.txt', 'data/b733_beurling_read.txt', 'data/b733_dispatch_rows.json',
                  'data/b733_reproduce.txt', 'data/b733_reproduce.json', 'data/b733_address_scan.txt', 'data/b733_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b733 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R343)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b733_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R343)(2)-(6) (b733's keys over b733's objects): the order by time and ancestry; v1.12.0's controls; the objects rule, the door controls, the grades, the drafts, the A0 bank, the Beurling read and the dispatch rows;
        # ### the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the plan at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1120', K.STANDING_COMMIT, K.C1_STANDING), ('rule_standing', K.REG_COMMIT, K.C1_STANDING), ('v1120_corr', K.C1_STANDING, K.C1_CORR), ('corr_a0', K.C1_CORR, K.C2_RELAY), ('a0_doors', K.C2_RELAY, K.DOORS_COMMIT), ('doors_mech', K.DOORS_COMMIT, K.MECH_COMMIT), ('mech_front', K.MECH_COMMIT, K.FRONTDOORS_COMMIT))),
        v190=rd('b733_standing_v1120.txt'), doors=rd('b733_phase2_doors.txt'), front=rd('b733_phase2_frontdoors.txt'), a0=rd('b733_a0_restatement.txt'), dctl=rd('b733_door_controls.txt'), beurling=rd('b733_beurling_read.txt'), mech=rd('b726_mechanisms.txt'), classes=jl('b733_door_classes.json'), rule=rd('b733_objects_rule.txt'),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b733_dispatch_rows.json') or '[]'), reproduce=rd('b733_reproduce.txt'), reproducej=jl('b733_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b733_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b732 left them
        rebuild=None, rebuild_rows=json.loads(rd('b733_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               rule=_ct(ROOT, K.REG_COMMIT), a0=_ct(EF, K.ZQ_FIRST), doors=_ct(ROOT, K.DOORS_COMMIT), mech=_ct(ROOT, K.MECH_COMMIT), front=_ct(ROOT, K.FRONTDOORS_COMMIT),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.C2_RELAY),
                   doors=files_of(ROOT, K.DOORS_COMMIT), mech=files_of(ROOT, K.MECH_COMMIT), front=files_of(ROOT, K.FRONTDOORS_COMMIT), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b733's read-first bank's items by path, as its step zero wrote them (data/b733_readfirst.txt :9-:22)
READFIRST_NEEDLES = ('relay data/b732_closing.txt |', 'relay data/b732_events.txt |', 'relay data/b732_defects.txt |', 'relay data/b732_price_measured.txt |', 'relay data/b729_count_price.txt |',
                     'relay data/b721_frozen_line.txt |', 'relay data/b726_frontdoors.txt |', 'relay data/b726_zenodo_read.json |', 'relay data/b726_mechanisms.txt |',
                     'SIDE-explicit-formula Schema/EpsteinZQ.lean |', 'SIDE-explicit-formula Schema/Config.lean |', 'THE_KEYSTONE_CENSUS_v0_8_3 |', 'REGISTRY |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R343)(1)-(2))', 'A0 PREMISE ((R343)(3))', 'PHASE 2 DOORS ((R343)(4))', 'DRAFTS ((R343)(5)-(6)(i))', 'BEURLING READ ((R343)(6)(ii))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (110 = 110 + 0, data/b733_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 110 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b732's figures, read at FINDINGS :12474 as Component 1 landed them
    return landed(S, 0, ['b732 AT ITS WEIGHT', 'suite 115 of 116', 'the closing’s 5a7d5778', '19 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b733's title in the ferry's Component 5 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## Phase 2’s doors graded: ', ' kernels, ', ' deposits, ', ' synthesis heads, ', ' sentences, EXCEEDS ', ', LOAD-BEARING ', ' and SILENT ', ' drafts for the second sitting', '; the A0 premise restated to the existential form', '; the 2C note drafted', '; the Beurling row ', '; the rendered module landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R343)(1)-(2): the generated entry for b732's ten events and nineteen defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(10), the defects by the one lettering, no dated note; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 3, CLOSE 26 over 29, REPEAT 9); the repairs at tools/standing/ v1.12.0 by their controls
    bank; the corrigenda bank appended at row (52) and nothing before it changed; in Component 1's commits (the figures read from
    data/b733_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 19 and len(items) == j.get('items') == 29 and j.get('row') == 52 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 29 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 3 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 9 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.12.0' and (j.get('repairs') or {}).get('bank') == 'data/b733_standing_v1120.txt' \
        and len(j.get('notes') or []) == 0 \
        and '  (52) ' in S['corrigenda'] and '  (53) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b733_rules.txt and data/b733_rules.txt, by form in (R343)(7)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b732's form, its names b733's); no author's word of b733 orders a rules row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b733_rules.txt')) and not os.path.exists(os.path.join(D, 'b733_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b733's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- THE A0 PREMISE', 'CERTIFIED -- tools/standing/ v1.12.0', 'REGISTERED -- THE PHASE 2 DOORS', 'REGISTERED -- THE DRAFTS',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b733: the one dispatch of (R343)(3) -- each `gh workflow run` command of the capture a row of the bank, the rows' count the worklist's and within the cap, every
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
# ### b733's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The A0 premise**', '**The doors**', '**The drafts**', '**The 2C note and the Beurling read**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b733_corrigendum.txt', 'data/b733_standing_v1120.txt', 'data/b733_objects_rule.txt', 'data/b733_door_controls.txt', 'data/b733_phase2_doors.txt', 'data/b733_a0_restatement.txt', 'data/b733_phase2_frontdoors.txt', 'data/b733_beurling_read.txt', 'data/b726_mechanisms.txt', 'data/b733_dispatch_rows.json',
                 'data/b733_reproduce.txt', 'data/b733_address_scan.txt', 'data/b733_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b733: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R343)(2)-(6), N2 (the name the frozen run list carries): the objects rule's commit first, then v1.12.0's and the corrigendum's, the one Lean commit, the grades, the mechanisms row and the drafts, in that order by time and by ancestry within the relay;
    the rule at HEAD its text at its commit; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('rule', 'standing', 'corr', 'a0', 'doors', 'mech', 'front')
    return K.REGISTRATIONS in S['files']['reg'] and bool(reg) and reg == head \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b733_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    SIDE-explicit-formula's zq-b730; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address and name read from
    history and held in memory -- the address 0, the author's name 0, the previous name 0, its four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R343)(4), N2 (the name the frozen run list carries): the objects rule printed and committed before any kernel named, its foot saying so; the door controls all as wanted, their bank in the grades' commit, the rule's commit an ancestor of v1.12.0's and before the grades by time."""
    return 'NO KERNEL NAMED ABOVE ITS OWN RULE' in _vlast(S['rule']) and K.REGISTRATIONS in S['files']['reg'] \
        and 'CONTROLS ALL AS WANTED' in _vlast(S['dctl']) and 'data/b733_door_controls.txt' in S['files']['doors'] \
        and S['anc'].get('rule_standing') is True and S['t']['rule'] < S['t']['doors']
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R343)(3)-(4), N1, N3 (the name the frozen run list carries): the doors' foot recounted -- every EXCEEDS row in the class file, LOAD-BEARING and SILENT summing to EXCEEDS and each the foot's; the one dispatch read by its run id at build exit 0, no sorryAx, the A0 bank's foot its run."""
    cl = S['classes'] or []
    m = re.search(r'KERNELS (\d+) ; DEPOSITS (\d+) ; SYNTHESIS HEADS (\d+) ; SENTENCES (\d+) ; EXCEEDS (\d+) ; LOAD-BEARING (\d+) ; SILENT (\d+) ;', _vlast(S['doors']))
    if not m:
        return False
    e_, l_, q_ = int(m.group(5)), int(m.group(6)), int(m.group(7))
    rows = S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    return len(cl) == e_ == l_ + q_ and sum(1 for r in cl if r.get('cls') == 'LOAD-BEARING') == l_ and sum(1 for r in cl if r.get('cls') == 'SILENT') == q_ \
        and len(disp) == len(reads) == 1 and str(disp[0]['run']) == str(reads[0]['run']) and str(reads[0].get('build_exit')) == '0' and not reads[0].get('sorryAx') \
        and ('RUN %s, BUILD EXIT 0, NO sorryAx' % reads[0]['run']) in _vlast(S['a0'])
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip locally and at origin; no kernel's main moved (G-MERGES-ON-GATE's read); the act's one Lean commit on
    zq-b730 alone, the branch's diff against its entering tip Schema/EpsteinZQ.lean and nothing else."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and sorted(S['zq_files'] or []) == ['SIDEExplicitFormula/Schema/EpsteinZQ.lean']

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.12.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1120') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.12.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b732's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R343)(3), (5)-(6), N3, N5 (the name the frozen run list carries): the drafts' foot, LISTED, APPLIED NOWHERE, its controls four of four, the 2C note's part present; the A0 bank's foot, two conclusions unchanged and zq_count moved; the Beurling row in data/b726_mechanisms.txt by a commit carrying no drafts bank, its foot printed."""
    f, a, b = _vlast(S['front']), _vlast(S['a0']), _vlast(S['beurling'])
    return 'LISTED, APPLIED NOWHERE' in f and re.search(r'; DRAFTS \d+ ;', f) is not None and 'CONTROLS 4 OF 4 AS WANTED' in f and '## PART E -- THE 2C NOTE' in (S['front'] or '') \
        and '2 of 3 CONCLUSIONS UNCHANGED ; zq_count MOVED' in a and 'THE BEURLING ROW: ' in b and '## EXTENDED AT b733, (R343)(6)(ii)' in (S['mech'] or '') \
        and 'data/b726_mechanisms.txt' in S['files']['mech'] and 'data/b733_phase2_frontdoors.txt' not in S['files']['mech'] and 'data/b733_phase2_frontdoors.txt' in S['files']['front']


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
    """standing clauses v9 (Component 7 of (R343): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b733_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b732's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R343-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b732's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R343) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b732's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R342)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 110 = 110 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b732-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 5 form: Phase 2`s doors graded, its counts, the drafts, the A0 premise, the 2C note, the Beurling row, the rendered module',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R343)(1)-(2): the generated corrigendum for b732`s record, landed at FINDINGS :12476: its ten events and nineteen defects, 29 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 3 CLOSE 26, REPEAT 9; v1.12.0`s repairs by data/b733_standing_v1120.txt; the corrigenda bank appended at row (52)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b733 and no b733 rules bank: no author`s word of b733 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b733's objects
    ('G-REGISTRATIONS-FIRST', '(R343)(2)-(6), N2: the objects rule`s commit, v1.12.0`s, the corrigendum`s, the one Lean commit, the grades, the mechanisms row and the drafts in that order by time and ancestry; the rule at HEAD its text at 9aa8e011; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_a0=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b733_address_scan.py run live over every commit of the act in the relay, PLACE-papers and zq-b730, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R343)(4), N2: the objects rule printed and committed before any kernel named; the door controls all as wanted, before the grades',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'dctl', (S['dctl'] or '').replace('CONTROLS ALL AS WANTED', 'CONTROLS NOT AS WANTED'))),
    ('G-DERIVATION-GRADED', '(R343)(3)-(4), N1, N3: the doors` foot recounted over the class file, LOAD-BEARING and SILENT summing to EXCEEDS; the one dispatch read by its run id at exit 0, no sorryAx, the A0 bank`s foot its run',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'drows', lambda d: [r.update(sorryAx=True) for r in d if r.get('kind') == 'read'])),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against its entering tip Schema/EpsteinZQ.lean alone',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 5a7d5778, VERSION 9; v8 at HEAD its blob at 5a7d5778; no v10; v9`s commit an ancestor of v1.12.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R343)(3), (5)-(6), N3, N5: the drafts` foot LISTED, APPLIED NOWHERE, four controls, the 2C part; the A0 foot, two conclusions unchanged and zq_count moved; the Beurling row by a commit carrying no drafts bank',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'front', (S['front'] or '').replace('LISTED, APPLIED NOWHERE', 'APPLIED'))),
    ('G-DIFFERS-ERRATA', '(R343): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in af07e3c, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b733_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R343-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b732`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 5a7d5778 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: the one dispatch of (R343)(3), read by its run id; the rows` runs the worklist`s',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: each `gh workflow run` of the capture a row, the count within the cap of one, the push before its dispatch before its read, the rows` free memory at the hold; no b721-b732 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b732 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b732`s [41] tip; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers alone); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b732`s trail record on OPEN_TRAILS (:17017) and its root in the chain', lambda S: '### b732 — lane two, act one hundred and fifty-eight, the second field act under (R342)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers alone): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b732`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: one; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b733, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R343)(3): a main at its sitting tip, its tags unmoved, is not a move against b732's face
#⟪OVERRIDE record 2554 2554⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b733: (R343)'s rows. (1)'s line quoted by the ruling from the public relay at a8a702dd
    pub = _blob('D:/relay', 'a8a702dd', 'data/b732_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b732_closing.txt :1, the head line as the public relay carries it at a8a702dd', bool(pub) and pub[0] == at(cl, 1) and 'relay c7737a81' in pub[0] and 'PLACE-papers 998dc4a' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root 339e8eed0e5251f6', '3 prompts answered', 'scores 8 of 8 HELD', '30 defects'):
        add('ruling (1)', 'data/b732_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    df_ = rd(p('data', 'b732_defects.txt')) or ''
    tg_ = re.findall(r"\[(CLAIM|CLOSE) ; (NEW|REPEAT)", df_)
    add('ruling (1)', 'the counter CLAIM 5, CLOSE 25, REPEAT 14 of 30 is the defects bank alone (data/b732_defects.txt); the closing :5 reads the events with it, CLAIM 7, CLOSE 34, REPEAT 19 OF 41',
        (sum(1 for a_, _b in tg_ if a_ == 'CLAIM'), sum(1 for a_, _b in tg_ if a_ == 'CLOSE'), sum(1 for _a, b_ in tg_ if b_ == 'REPEAT'), len(tg_)) == (5, 25, 14, 30) and 'CLAIM 7, CLOSE 34, REPEAT 19 OF 41' in at(cl, 5),
        'tags %d ; %s' % (len(tg_), at(cl, 5)[-40:]), '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b732']]
    add('ruling (1)', 'data/act_roots.txt, b732`s root 339e8eed chained from b731`s a89f753b', len(ar8_) == 1 and ar8_[0][1].startswith('339e8eed') and ar8_[0][2].startswith('a89f753b'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b732_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b732 (b732`s post-push part b3)', 'b732 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b732 AGREE' if 'b732 AGREE' in b3_ else 'ABSENT', '1')
    dr_ = lines_of(p('data', 'b732_phase2_doors.txt'))
    add('ruling (1)', 'data/b732_phase2_doors.txt :2649, 24 kernels, 6 deposits, 6 synthesis heads, 1816 sentences, EXCEEDS 472, LOAD-BEARING 59, SILENT 413', all(w_ in at(dr_, 2649) for w_ in ('1816', '472', '59', '413')), at(dr_, 2649)[:70], '1')
    fr_ = lines_of(p('data', 'b732_phase2_frontdoors.txt'))
    add('ruling (1)', 'data/b732_phase2_frontdoors.txt :832, 52 drafts in 111 items', '52' in at(fr_, 832) and '111' in at(fr_, 832), at(fr_, 832)[:70], '1')
    a0_ = lines_of(p('data', 'b732_a0_restatement.txt'))
    add('ruling (1)', 'data/b732_a0_restatement.txt :23, the conclusions at 1b34964a', 'zq_count' in at(a0_, 23), at(a0_, 23)[:70], '1')
    ev_ = rd(p('data', 'b732_events.txt')) or ''
    for w_ in ('SIDE-bijection, SIDE-effects, SIDE-interfaces, SIDE-kernel, SIDE-meta, SIDE-orchestrator, SIDE-residual-bridge', 'SIDE-fano-darkness, SIDE-carrier-spec, SIDE-t7-topology-cmb'):
        add('ruling (1)', 'data/b732_events.txt row (9), the sets of the miss of seven and the excess of three: %s' % w_[:40], w_ in ev_, 'read', '1')
    add('ruling (2)(i)', 'data/b732_events.txt row (3), the comparison the opening repairs', '(3) THE SEAT' in ev_ and 'The failing lists were not compared' in ev_, 'read', '1')
    add('ruling (2)(vi)', 'data/b732_events.txt row (11), the two post-seal reads', '(11) THE SEAT' in ev_ and 'two shell commands named the trail' in ev_, 'read', '1')
    add('ruling (1)', 'tools/standing/VERSION v1.12.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.12.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(11) and 30 defects (data/b732_events.txt, data/b732_defects.txt)',
        starts == list(range(1, 12)) and len(letters) == 30, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b732_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    cp_ = lines_of(p('data', 'b729_count_price.txt'))
    for f_ in ('b729_count_price.txt', 'b732_author_answers.txt', 'b732_author_words.txt', 'b731_price_measured.txt', 'b732_defects.txt', 'b732_a0_restatement.txt', 'b685_count_plan.txt', 'b685_search.txt', 'b732_phase2_frontdoors.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    add('ruling (3)', 'data/b729_count_price.txt :25, the count row, 800-2,000 lines, 15-35 dispatches', '800-2,000' in at(cp_, 25) and '15-35' in at(cp_, 25), at(cp_, 25)[:70], '3')
    add('ruling (3)', 'data/b729_count_price.txt :29, (4) the count field`s lemmas', at(cp_, 29).startswith('## (4) THE COUNT FIELD'), at(cp_, 29)[:50], '3')
    add('ruling (3)', 'data/b729_count_price.txt :32, C3 ABSENT', 'C3 the lower bound' in at(cp_, 32) and 'ABSENT' in at(cp_, 32), at(cp_, 32)[:50], '3')
    add('ruling (3)', 'data/b729_count_price.txt :33, C4 ABSENT', 'C4 Z_Q(3/2)' in at(cp_, 33) and 'ABSENT' in at(cp_, 33), at(cp_, 33)[:50], '3')
    add('ruling (3)', 'data/b729_count_price.txt :37, the existential A0, WeilConfig.count', 'WeilConfig.count asks (Schema/Config.lean :31)' in at(cp_, 37), at(cp_, 37)[:50], '3')
    pm_ = lines_of(p('data', 'b731_price_measured.txt'))
    add('ruling (3)', 'data/b731_price_measured.txt :29-:31, the count row re-read by the three ratios', '222-7860' in at(pm_, 31), at(pm_, 31)[:60], '3')
    b6_ = lines_of(p('data', 'b685_count_plan.txt'))
    add('ruling (3)', 'data/b685_count_plan.txt :26, step (3), the right edge', at(b6_, 26).startswith('  (3) THE RIGHT EDGE'), at(b6_, 26)[:50], '3')
    add('ruling (3)', 'data/b685_count_plan.txt :55, :57, step (6), 4 - Z_Q(c)', at(b6_, 55).startswith('  (6) THE JENSEN') and '4 − Z_Q(c)' in at(b6_, 57), at(b6_, 57)[:60], '3')
    EF_ = 'D:/SIDE-explicit-formula'
    ez_ = gr(EF_, 'show', '1b34964a:SIDEExplicitFormula/Schema/EpsteinZQ.lean').split(NL)
    fl_ = [at(ez_, n_).strip().split(' ')[0] for n_ in range(138, 143)]
    add('ruling (3)', 'ZQPremises has five fields, quoted from the structure at the pin, Schema/EpsteinZQ.lean :137-:142',
        at(ez_, 137).startswith('structure ZQPremises') and fl_ == ['continuation', 'zeros', 'logDeriv', 'explicitFormula', 'count'] and at(ez_, 143).strip() == '', ' '.join(fl_), '2')
    add('ruling (3)', 'Schema/EpsteinZQ.lean :142, the restated premise', 'count : ∃ A₀ : ℝ, Wide.HCount Z A₀' in at(ez_, 142), at(ez_, 142)[:50], '2')
    cf_ = gr(EF_, 'show', '1b34964a:SIDEExplicitFormula/Schema/Config.lean').split(NL)
    add('ruling (3)', 'Schema/Config.lean :31, WeilConfig.count, the existential form', 'count : ∃ A₀ : ℝ, B321.HCount' in at(cf_, 31), at(cf_, 31)[:60], '2')
    wc_ = gr(EF_, 'show', '1b34964a:SIDEExplicitFormula/Schema/Wide/Config.lean').split(NL)
    add('ruling (3)', 'Schema/Wide/Config.lean :49, Wide.HCount', at(wc_, 49).startswith('def HCount'), at(wc_, 49)[:50], '2')
    lc_ = gr(EF_, 'show', '1b34964a:Zeta23/RvM/LocalCount.lean').split(NL)
    for n_, w_ in ((112, 'half_count_large'), (271, 'count_small'), (310, 'zetaZeroConfig_local_count')):
        add('ruling (3)', 'Zeta23/RvM/LocalCount.lean :%d, %s' % (n_, w_), w_ in at(lc_, n_), at(lc_, n_)[:60], '2')
    cl_ = gr(EF_, 'show', '1b34964a:SIDEExplicitFormula/Chi/LocalCount.lean').split(NL)
    for n_, w_ in ((81, 'half_count_large_chi'), (207, 'count_small_chi'), (218, 'chiZeroConfig_local_count')):
        add('ruling (3)', 'Chi/LocalCount.lean :%d, %s' % (n_, w_), w_ in at(cl_, n_), at(cl_, n_)[:60], '2')
    zg_ = gr(EF_, 'show', '1b34964a:Zeta23/RvM/ZetaGrowth.lean')
    add('ruling (3)', 'Zeta23/RvM/ZetaGrowth.lean, the C2 neighbour', bool(zg_), '%d lines' % zg_.count(NL), '2')
    bd_ = gr(EF_, 'show', '23b006df:SIDEExplicitFormula/Schema/ZQ/Bound.lean').split(NL)
    add('ruling (3)', 'zq-b730`s Bound module at 23b006df, zq_three_halves_lt :319', at(bd_, 319).startswith('theorem zq_three_halves_lt'), at(bd_, 319)[:60], '2')
    add('ruling (3)', 'zq_three_halves_tsum_lt :370, the same bound in the coefficients', at(bd_, 370).startswith('theorem zq_three_halves_tsum_lt'), at(bd_, 370)[:60], '2')
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ferry (read first)', 'zq-b730 at 1b34964a', zt_.startswith('1b34964a'), zt_[:8], '3')
    ml_ = gr('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'rev-parse', 'HEAD')
    add('ruling (3)', 'Mathlib at de5ce8a9', ml_.startswith('de5ce8a9'), ml_[:12], '3')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (2)', 'OPEN_TRAILS :17157, the trail`s hand section at b732 carrying the author`s repairs', at(ot_, 17157).startswith('**Carried to b733’s opening, the author’s word:**'), at(ot_, 17157)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.12.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.12.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R343)(4): b732's export, the mirror's last
    add('ruling (4)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-01-b732.zip, b732`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R343)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b732-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R343)(4): act_current alone, then b732's step row 29 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b732_steps.json'),
                   (K.STEPZERO, 'data/b732_relay_push-b732-closing_push_out.txt')):
        if not c_:
            add('ruling (4)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (4)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (4)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (4)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b733_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b733_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b733 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b732_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 5) are the corrigendum with v1.12.0's controls, the A0 premise, the Phase 2 doors, the drafts, the Beurling read, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R343)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R343)(9)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: on the branch zq-b730 of SIDE-explicit-formula alone, the one commit of (R343)(3) to Schema/EpsteinZQ.lean; no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b733 ((R343)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R342)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b733 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-NINE, THE PHASE 2 DOORS ACT: THE DOORS GRADED, THE DRAFTS LISTED AND APPLIED NOWHERE; '
              'THE A0 PREMISE RESTATED ON zq-b730; v1.12.0 LANDED; THE 2C NOTE DRAFTED; THE BEURLING READ ENTERED, UNDER (R343).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b732's sections over b732's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.12.0: the act module rendered, the re-price from the banks, the Lean paths against the tree, the N3 reader on the landed lines, each case failing before its repair and passing after', 'b733_standing_v1120.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE A0 PREMISE ((R343)(3))', [
                ('the commit on zq-b730, the one dispatch and every theorem binding the premises, conclusions before and after', 'b733_a0_restatement.txt')]),
            ('THE PHASE 2 DOORS ((R343)(4))', [
                ('the objects rule, printed before any kernel named', 'b733_objects_rule.txt'),
                ('the controls before any sentence', 'b733_door_controls.txt'),
                ('every sentence graded at the pins, the counts', 'b733_phase2_doors.txt')]),
            ('THE DRAFTS ((R343)(5)-(6)(i))', [
                ('the drafts for the second sitting and the 2C note, listed, applied nowhere', 'b733_phase2_frontdoors.txt')]),
            ('THE BEURLING READ ((R343)(6)(ii))', [
                ('the sources read, the row entered in data/b726_mechanisms.txt by a commit of its own', 'b733_beurling_read.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b733_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b732`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b733_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R342)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; on its branch zq-b730 alone the one commit of (R343)(3) to Schema/EpsteinZQ.lean, pushed through push_gated.sh, off main, untagged ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatch (N1, one), read by its run id, relay data/b733_dispatch_rows.json ; the rebuild-b721 branches of the wave 1 kernels as b732 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part, computation, push and dispatch ;',
    '    the push-b732-* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message ; N2: the objects rule printed before any kernel named, the controls before any sentence, the statements quoted at the census pin ;',
    '    N3: every grade at its bank`s end, no Phase 2 door called corrected, the drafts LISTED, applied nowhere ; N5: no new occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay data/b733_address_scan.txt, data/b733_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the workflow dispatch under the GitHub login ; the Zenodo records read anonymously') + ' ;',
    '    nothing deposited ; no new Zenodo version ; the deposit route untouched, publish never called, the draft held at v5 ; no README, GitHub description, Zenodo description or paper written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) written ; no paper cut, moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt (b733`s root), data/b726_mechanisms.txt (the Beurling row) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.12.0 by (R343)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b732 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R343)(9)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For b733, each from its bank: the fields count and explicitFormula, open, with W-ORD-ZQ-DERIVES (OPEN_TRAILS), on the restated premise (relay data/b733_a0_restatement.txt) ; the drafts, relay data/b733_phase2_frontdoors.txt, the second sitting`s agenda on the author`s word ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b733_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b732 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b732`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b733: the standing repairs are v1.12.0's ((R343)(2), relay data/b733_standing_v1120.txt, read in the corrigendum section); the
    # ### carry's diffs here (b733 carried at step zero before the fold; its tools since are the templates and tools/acts/b733.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b732 left them; port-b707 at b712`s tip %s)' % (
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
    b733's form over b733's objects (b732's form in git at b732's record tool): the corrigendum's foot and v1.12.0's controls; the doors', the drafts', the A0 bank's and the Beurling read's feet;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1120.txt' % ACT, r'\*\*v1\.12\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.12.0`s controls')
    dr = _bfig('%s_phase2_doors.txt' % ACT, r'\*\*KERNELS (\d+) ; DEPOSITS (\d+) ; SYNTHESIS HEADS (\d+) ; SENTENCES (\d+) ; EXCEEDS (\d+) ; LOAD-BEARING (\d+) ; SILENT (\d+) ; SWEEP CONTROLS (\d+) OF (\d+) AS WANTED', 'the doors` foot')
    fd = _bfig('%s_phase2_frontdoors.txt' % ACT, r'\*\*ITEMS (\d+) ; DRAFTS (\d+) ; LOAD-BEARING (\d+) ; SILENT (\d+) CARRIED ; THE BEURLING ROW AT data/b726_mechanisms\.txt BY ITS OWN COMMIT ; CONTROLS (\d+) OF (\d+) AS WANTED ; LISTED, APPLIED NOWHERE\.\*\*', 'the drafts` foot')
    a0 = _bfig('%s_a0_restatement.txt' % ACT, r'\*\*THE A0 PREMISE RESTATED ON zq-b730 AT ([0-9a-f]{8}): RUN (\d+), BUILD EXIT (\d+), NO sorryAx, AXIOMS ([^;]+?) ; (\d) of (\d) CONCLUSIONS UNCHANGED ; zq_count MOVED\.\*\*', 'the A0 bank`s foot')
    bu = _bfig('%s_beurling_read.txt' % ACT, r'\*\*THE BEURLING ROW: (NO INSTANCE FOUND|CITED) IN THE SOURCES READ', 'the Beurling read`s foot')
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1120_ctl=v5[0], v1120_cases=v5[1], v1120_wanted=v5[2], repairs=len(v5[0].split(', ')),
                d_k=int(dr[0]), d_d=int(dr[1]), d_s=int(dr[2]), d_n=int(dr[3]), d_e=int(dr[4]), d_l=int(dr[5]), d_q=int(dr[6]), d_cw=dr[7], d_ct=dr[8],
                fd_items=int(fd[0]), fd_drafts=int(fd[1]), fd_cw=fd[4], fd_ct=fd[5],
                a0_tip=a0[0], a0_run=a0[1], a0_exit=a0[2], a0_axioms=a0[3], a0_same=a0[4], a0_of=a0[5],
                beurling=bu[0].lower(),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R343)(3): the kernel rows of one kind as banked (data/b733_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R343): no lean process runs on this host; the dispatch that of (R343)(3), the one, read by its run id. From the command bank (the seat's commands, read live from the
    capture by the `commands` route) and the dispatch rows beside the worklist's EF_RUNS."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b733_commands.json): %s; dispatch commands in the capture: %s, the worklist`s runs %d, each read by its run id: %s (relay data/b733_dispatch_rows.json)' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b733's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b733_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b733_phase2_doors.txt', '## THE CONTROLS OF THE CITATION SWEEP', '## THE TALLY PER KERNEL'),
               ('data/b733_phase2_frontdoors.txt', '## THE CONTROLS, BEFORE ANY DRAFT', '## PART A -- '))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R343): the objects rule prints before any kernel named, the controls before any sentence: the rule's commit, v1.12.0's, the corrigendum's, the one Lean commit, the grades, the mechanisms row and the drafts in that order by time across the repositories;
    each tool's controls before its figures."""
    chain_ = [(ROOT, K.REG_COMMIT), (ROOT, K.C1_STANDING), (ROOT, K.C1_CORR), (K.EF_DIR, K.ZQ_FIRST), (ROOT, K.DOORS_COMMIT), (ROOT, K.MECH_COMMIT), (ROOT, K.FRONTDOORS_COMMIT)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    t = rdn('%s_objects_rule.txt' % ACT)
    tz = rdn('%s_door_controls.txt' % ACT)
    fg_ = rdn('%s_phase2_doors.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = 'NO KERNEL NAMED ABOVE ITS OWN RULE' in t and 'CONTROLS ALL AS WANTED' in tz and order_ and all(o for _p, o in ctl) and bool(fg_)
#⟪END⟫
#⟪SECTION record 13⟫
        'the rule`s foot, no kernel named above it: %s; the door controls all as wanted: %s; the rule, v1.12.0, the corrigendum, the Lean commit, the grades, the mechanisms row and the drafts in that order by time: %s (%s); the tools` controls before their figures: %s' % (
            'NO KERNEL NAMED ABOVE ITS OWN RULE' in t, 'CONTROLS ALL AS WANTED' in tz, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b733's objects; b732's in git at b732's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b733_standing_v1120.txt', ('ALL AS WANTED',)), ('b733_objects_rule.txt', ('NO KERNEL NAMED',)), ('b733_door_controls.txt', ('CONTROLS ALL AS WANTED',)), ('b733_phase2_doors.txt', ('KERNELS', 'LOAD-BEARING', 'SILENT')),
             ('b733_phase2_frontdoors.txt', ('DRAFTS', 'LISTED, APPLIED NOWHERE')), ('b733_a0_restatement.txt', ('THE A0 PREMISE RESTATED',)), ('b733_beurling_read.txt', ('THE BEURLING ROW',)), ('b733_citation_check.txt', ('CITES CHECKED',)), ('b733_reproduce.txt', ('REPRODUCES',)), ('b733_address_scan.txt', ('PREVIOUS ADDRESS',)))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R343): every grade prints at its end; the entry's counts the banks'; no sentence of the entry calls any Phase 2 door corrected, and the drafts stand LISTED, applied nowhere. From the banks' last
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
    bad = [s_ for s_ in sents if (re.search(r'\b(?:doors?|READMEs?|descriptions?|deposits?)\b', s_) and re.search(r'\b(?:corrected|repaired|fixed|rewritten|updated)\b', s_) and 'corrigendum' not in s_.lower() and 'hand read' not in s_) or re.search(r'\bdrafts?\b[^.;]*\bapplied\b(?! nowhere)', s_)]
    ok = all(o for _n, o in graded) and not bad and (not sents or any('LISTED' in s_ and 'APPLIED NOWHERE' in s_ for s_ in sents))
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the entry`s sentences calling a Phase 2 door corrected or a draft applied, read from %s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bad or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R343) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R343)(5))
# ### (R343)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R343) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b732's form, carried) -- read from git,
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
    # ### (R343)(3), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-explicit-formula's zq-b730 or a branch the worklist names at its tip; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b732 left them; the address scan's count from its bank (relay data/b733_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b733_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s named branches, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b733 — lane two, act one hundred and fifty-nine, the Phase 2 doors act under (R343): b732 at its weight and its corrigendum; v1.12.0; '
            'the A0 premise restated; Phase 2’s doors graded; the drafts listed, applied nowhere')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 5 form; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## Phase 2’s doors graded: %d kernels, %d deposits, %d synthesis heads, %d sentences, EXCEEDS %d, LOAD-BEARING %d and SILENT %d; %d drafts for the second sitting; the A0 premise restated to the existential form; the 2C note drafted; the Beurling row %s; the rendered module landed' % (
        f['d_k'], f['d_d'], f['d_s'], f['d_n'], f['d_e'], f['d_l'], f['d_q'], f['fd_drafts'], f['beurling']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the objects rule named 24 kernels where the navigator’s list named 20, 17 in both, the rule governing, printed at relay data/b733_objects.txt; (2) the p2-10 head sentence drafted as a removal, the edition form’s, where (R343)(5) says restated, printed at relay data/b733_phase2_frontdoors.txt; '
            '(3) SIDE-constants being private, its one load-bearing row carried by digest and no draft text for it on the public relay; (4) the second kind of (R343)(6)(i) empty among the five fields, Z_Q(3/2) < 4 being analysis at the standard three, so the 2C note says so; '
            '(5) zq_count’s conclusion moved with the field on the author’s word, and C4 compiled at b732 as zq_three_halves_lt, for b733’s pricing; ' +
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
            'author beside the next act of (R343)(9)): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b733's objects; b732's composer in git at
    b732's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R342)(2)(v)
    e = ['', _title(), '',
         'Every sentence of Phase 2’s doors is graded by b721’s vocabulary against its kernel’s statements at the census pin, %d sentences over %d kernels, %d deposits and %d synthesis heads, %d of them EXCEEDS their kernel’s statements: %d LOAD-BEARING and %d SILENT. %d drafts stand LISTED, APPLIED NOWHERE, for the second sitting on the author’s word. ZQPremises.count is restated to the existential form on zq-b730 at `%s`, run %s at axioms %s, a premise still stated and not proved; the draft stands at v5, HELD.' % (
             f['d_n'], f['d_k'], f['d_d'], f['d_s'], f['d_e'], f['d_l'], f['d_q'], f['fd_drafts'], K.ZQ_TIP[:8], f['a0_run'], f['a0_axioms']), '',
         '*Filed at b733 on the author’s ruling `(R343)`; %d question%s put before the root. Banks: relay '
         '`data/b733_corrigendum.txt`, `data/b733_standing_v1120.txt`, `data/b733_objects_rule.txt`, `data/b733_door_controls.txt`, `data/b733_phase2_doors.txt`, `data/b733_a0_restatement.txt`, `data/b733_phase2_frontdoors.txt`, `data/b733_beurling_read.txt`, `data/b726_mechanisms.txt`, `data/b733_dispatch_rows.json`, '
         '`data/b733_reproduce.txt`, `data/b733_address_scan.txt`, `data/b733_touch.txt`, `data/b733_standing_figures.txt`, `data/b733_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R343)(1)-(2), `%s`, `%s`, `%s`): b732 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b732’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b733_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b733_standing_v1120.txt); the act module rendered from tools/b733_sections.txt by tools/standing/actmodule.py.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1120_ctl'], f['v1120_cases'],
             f['v1120_wanted']), '',
         '**The order of the act** (N2): the objects rule printed before any kernel named (relay data/b733_objects_rule.txt, committed at `%s`); the door controls all as wanted before any sentence (relay data/b733_door_controls.txt); the rule names 24 kernels, the navigator’s list 20, 17 in both, the rule governing (relay data/b733_objects.txt).' % K.REG_COMMIT[:8], '',
         '**The A0 premise** ((R343)(3), N1, N3): `count : ∃ A₀ : ℝ, Wide.HCount Z A₀` on zq-b730 at `%s`, one dispatch, run %s, build exit %s, no sorryAx, the three binders at axioms %s. %s of %s conclusions unchanged; zq_count moved with the field, on the author’s word, printed at the bank. A0Q stays a separate definition and no theorem row is added. The premise stands stated and not proved (relay data/b733_a0_restatement.txt, data/b733_dispatch_rows.json).' % (
             f['a0_tip'], f['a0_run'], f['a0_exit'], f['a0_axioms'], f['a0_same'], f['a0_of']), '',
         '**The doors** ((R343)(4), N2, N3): %d kernels, %d deposits and %d synthesis heads, %d sentences, each graded STATED, EXCEEDS, OUTSIDE, SCOPE or NO CLAIM against the statements at the pin, a README read at main and the distance printed where a main moved; EXCEEDS %d, of them LOAD-BEARING %d and SILENT %d by the class’s matcher, its yield printed beside b726’s and the matchers’ lineage at the bank, the citation sweep’s controls %s of %s. The six grading seats’ proposals were hand-read on every EXCEEDS row, and a row graded too low elsewhere is not caught by that read (relay data/b733_phase2_doors.txt).' % (
             f['d_k'], f['d_d'], f['d_s'], f['d_n'], f['d_e'], f['d_l'], f['d_q'], f['d_cw'], f['d_ct']), '',
         '**The drafts** ((R343)(5), N3): %d items, %d drafts LISTED, APPLIED NOWHERE: README paragraphs quoting statements at the pin, one-line descriptions, the deposit notes in b726’s words, the head sentences in the edition form and the 2C note; controls %s of %s. The second sitting is the author’s (relay data/b733_phase2_frontdoors.txt).' % (
             f['fd_items'], f['fd_drafts'], f['fd_cw'], f['fd_ct']), '',
         '**The 2C note and the Beurling read** ((R343)(6)): the note is drafted for p2-41’s next edition, Part E of the drafts; the second kind it names is empty among the five fields. The Beurling row is entered in W-ORD-MECHANISM-TABLE’s additions by a commit of its own, `%s`: %s in the sources read; two sources were not read and stand so (relay data/b733_beurling_read.txt, data/b726_mechanisms.txt).' % (K.MECH_COMMIT[:8], f['beurling']), '',
         '**What this act is not**: the grades say what each sentence claims against its kernel’s statements and no more. They grade no physics and no mathematics beyond the pin. No field of ZQPremises is discharged. Nothing here proves RH or GRH; the one Lean commit is on the branch alone, not on main, no tag.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b733_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b733_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b733_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b733 -- %s, %s, %s, %s -- against b732’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b733_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the doors and the premise read one way: a sentence stands against what its kernel compiles, and a premise against what it asks; the count’s existential asks no named value, as the doors’ grades ask no more than the statements.', '',
         '**Carried to:** %s: the count field on the restated premise, C3 and C4 priced before any build, explicitFormula open; the drafts for the second sitting on the author’s word; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b732():
    """b732's form over b732's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b733's objects; b732's composer in git at b732's record tool): W-ORD-ZQ-DERIVES and W-ORD-MECHANISM-TABLE annotated each by its own line, then the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD with those lines beneath it."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['**`W-ORD-ZQ-DERIVES` CARRIED at b733, (R343)(3):** ZQPremises.count restated to the existential form at zq-b730 `%s`; three of five fields closed as b732 left them, count and explicitFormula open; b733 takes the count on the restated premise.' % K.ZQ_TIP[:8],
           '**`W-ORD-MECHANISM-TABLE` CARRIED at b733, (R343)(6)(ii):** the Beurling row entered at relay data/b726_mechanisms.txt: %s in the sources read (relay data/b733_beurling_read.txt).' % f['beurling']]
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-ZQ-DERIVES' not in op:
        sys.exit('### THE TRAIL: AN ANNOTATED ORDER NOT READ OPEN BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R343) ratified.** Its components as the ferry orders them (relay data/b733_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b732’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders annotated** ((R343)(3), (6)(ii)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b733_standing_v1120.txt).' % (
                 f['ver'], f['v1120_cases'], f['v1120_wanted']), '',
             '**The A0 premise:** restated on zq-b730 at `%s`, run %s, %s of %s conclusions unchanged, zq_count moved on the author’s word, axioms %s (relay data/b733_a0_restatement.txt).' % (
                 K.ZQ_TIP[:8], f['a0_run'], f['a0_same'], f['a0_of'], f['a0_axioms']), '',
             '**The doors:** %d kernels, %d deposits, %d synthesis heads, %d sentences, EXCEEDS %d, LOAD-BEARING %d and SILENT %d (relay data/b733_phase2_doors.txt).' % (
                 f['d_k'], f['d_d'], f['d_s'], f['d_n'], f['d_e'], f['d_l'], f['d_q']), '',
             '**The drafts:** %d drafts of %d items, LISTED, APPLIED NOWHERE, the 2C note among them (relay data/b733_phase2_frontdoors.txt).' % (f['fd_drafts'], f['fd_items']), '',
             '**The Beurling row:** %s in the sources read (relay data/b733_beurling_read.txt, data/b726_mechanisms.txt).' % f['beurling'], '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b733_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b733_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b733_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b733 `%s` (previous `%s`, b732’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b733_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b733_standing_v1120.txt); the standing '
             'report tool (relay data/b733_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no main written, no tag; on SIDE-explicit-formula’s zq-b730 alone the one commit of (R343)(3), %d dispatch read by its run id; the %s branches as b732 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b733_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b732’s %s, %s, %s, %s (relay data/b733_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b733_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b732():
    """b732's trail record over b732's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R343)(3)`s one; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730, kept, zq-b730 moved by (R343)(3); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b732 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b732`s and this act`s; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R343)(5): relay push-b732-closing, push-b732-preroot, push-b732-record; PLACE-papers push-b732-preroot, push-b732-record; each local, by name, after --merged listed it (data/b733_stepzero.txt).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: Schema/EpsteinZQ.lean alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R343) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (69eeba3) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R343)(1)-(2): FINDINGS :12476.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R343)(1)-(2): row (52).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-DERIVES and W-ORD-MECHANISM-TABLE annotated by the trail.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b733_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.12.0`s controls, the A0 bank, the grades, the drafts, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the objects rule committed with the step-zero banks at 9aa8e011.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### the grades and the drafts, after the objects rule; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none of this act`s.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### (R343)(3): MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R343)(2): tools/standing/ to v1.12.0, each repair with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 4, 4, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended; data/b726_mechanisms.txt, (R343)(6)(ii); data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation and push; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b733_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, gh reads, the workflow dispatch and the anonymous Zenodo reads; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### (R343)(4)-(5): the figure banks of the registered objects
    fig_banks = [p for p in ('data/b733_phase2_doors.txt', 'data/b733_phase2_frontdoors.txt')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b733_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b733_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1120', 'a0_restatement', 'phase2_doors', 'phase2_frontdoors', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b733_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b733_registration_%s.txt -- b733, THE PHASE 2 DOORS ACT: b732 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.12.0; THE A0 PREMISE RESTATED; "
                             "PHASE 2'S DOORS GRADED; THE DRAFTS LISTED, APPLIED NOWHERE; NO DEPOSIT, NO TAG, UNDER (R343)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b732's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b733: b732's lines read banks this
act does not write, and are not carried; the lines are b733's: the A0 premise (KERNEL, on the runner only), tools/standing/ v1.12.0 by its controls (CERTIFIED), the doors and the drafts
(REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b733's lines, each from the record tool's figures over b733's banks
    # ------------------------------------------------------------------ KERNEL: (R343)(3), on the runner only
    sz = seat('%s_a0_restatement.txt' % ACT, '**THE A0 PREMISE RESTATED ON ')
    sk = sz   # ### (R342)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- THE A0 PREMISE: ZQPremises.count restated to the existential form on zq-b730 at %s, run %s, axioms %s, %s of %s conclusions unchanged, zq_count moved; a premise stated and not proved. SOURCE %s.' % (f['a0_tip'], f['a0_run'], f['a0_axioms'], f['a0_same'], f['a0_of'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.12.0 ((R343)(2)), by its controls
    sw = seat('%s_standing_v1120.txt' % ACT, '**v1.12.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.12.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1120_ctl'], f['v1120_cases'], f['v1120_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the doors and the drafts, each read from its bank
    so = seat('%s_phase2_doors.txt' % ACT, '**KERNELS ')
    keys['ORD'] = ('REGISTERED -- THE PHASE 2 DOORS: %d kernels, %d deposits, %d synthesis heads, %d sentences, EXCEEDS %d, LOAD-BEARING %d, SILENT %d. SOURCE %s.' % (f['d_k'], f['d_d'], f['d_s'], f['d_n'], f['d_e'], f['d_l'], f['d_q'], so['text']))
    sv = seat('%s_phase2_frontdoors.txt' % ACT, '**ITEMS ')
    keys['DL'] = ('REGISTERED -- THE DRAFTS: %d drafts of %d items, LISTED, APPLIED NOWHERE. SOURCE %s.' % (f['fd_drafts'], f['fd_items'], sv['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R343)(8))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD', 'DL']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b733 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
