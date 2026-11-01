# -*- coding: utf-8 -*-
# b729 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R339)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R339)(2) repair it carries. Edited by the Edit tool. Carried at b729 by tools/b729_fold.py (`carry`) from tools/acts/b728.py,
# b728`s names substituted; the citation`s sections adopted from tools/b729_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b728`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b728`s carried till
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
# ### b729, Component 1 (the Edit tool): THE c1 ROUTE FOR b728'S WEIGHT LINE AND ITS CORRIGENDUM, (R339)(1)-(2). Carried from b728's
# ### override and rewritten here against b728's own banks: the closing's lines by needle, the events (13), the defects (25), the refusals
# ### (9 at 0650a188), the v1.9.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = '0650a188'          # ### b728's closing commit: its refusal bank read at it
C1_NOTED = '2026-10-31'
C1_CORRIGENDA_LAST = 48
C1_V170 = 'b729_standing_v190.txt'
C1_WEIGHT_HEAD = '*Appended 2026-10-31 by b729 to b728’s entry (:%d), under `(R339)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## 11 carried repairs landed'
C1_TRAIL_NEEDLE = '### b728 — lane two, act one hundred and fifty-five, the research act under (R338)'
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
    for l in _c1_rd('b728_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b728_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b728_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b728_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b728_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b728_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b728_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b728_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8:
        sys.exit('### data/b728_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b728_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b728_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 14)) or len(dr) != 25:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b728 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b728_closing.txt):* “%s” (data/b728_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b728_steps.json, the record and closing rows). As its rows read: the C2 certificates at 18 of 18 fields with no axiom, the theorem not compiled, (L1), (L2) and '
            'c2_value_law remaining (data/b728_c2.txt); lambda_2: GammaRZetaValues at index 1 proved with the standard three, (stieltjes 1).re < -1/20 remaining (data/b728_lambda2.txt); the six-onset table POST HOC, the pairs not '
            'within 10%%, nothing registered (data/b728_onset_table.txt); W-ORD-VISIBILITY NOT CLEAN at 69 zeros, nothing registered (data/b728_visibility.txt); the scores 8 of 8 HELD (data/b728_scores_close.json). '
            'The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both (:%d, :%d); the counter CLAIM %s, CLOSE %s, REPEAT %s of %s (:%d). '
            'The root %s over %s banks, chained from %s (data/b728_act_root.json; :%d), the chain AGREE b624-b728; %s prompts answered (:%d); %d events in data/b728_events.txt, rows (1)-(%d); %d defects, (a)–(y) '
            '(data/b728_defects.txt). THE TITLE as landed (“the C2 theorem at 18 of 18 fields”) stands with its dated note; what compiled at b728 is each field’s certificate. Nothing deposited, no draft published; the corrigendum '
            'for these rows follows, under `(R339)`(1)-(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                cc, cd, rp, rn, l_cn, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b728's bank at its closing commit, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '15:47:32Z', 'defect (b)'), (2, 'READ', '15:51:01Z', 'defect (e)'), (3, 'READ', '15:51:04Z', 'defect (f)'), (4, 'PIPE', '15:51:39Z', 'defect (g)'),
               (5, 'REDIR', '16:25:21Z', 'defect (h)'), (6, 'ENV', '16:32:47Z', 'defect (i)'), (7, 'READ', '16:43:32Z', 'defect (j)'), (8, 'REDIR', '16:45:43Z', 'defect (k)'), (9, 'REDIR', '19:15:06Z', 'event (2)')]
C1_CORR_TITLE = ('## Corrigendum to b728’s record (relay data/b728_events.txt rows (1)-(13) and data/b728_defects.txt): thirteen events and twenty-five defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the REDIR class at its head, report dry before the lock, the required list, the two plants, the scan written back, N5’s count, counts and nouns from the banks and the prompt-once clause '
                 'at tools/standing/ v1.9.0, each controlled on b728’s banks, under (R339)(1)-(2)')


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
    rl = _c1_git('show', '%s:data/b728_hook_refusals.txt' % C1_PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b728_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.9.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=[])
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(13)', sorted(ev) == list(range(1, 14))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 25', len(dr) == 25), ('the refusals 9, each answered as listed', len(rl) == 9 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.9.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.9.0
C1_EV_EXTRA = {2: '; repair (redir)', 3: '; repair (nouns); the title stands with its dated note', 4: '; repair (n5count)', 5: '; repair (nouns)', 6: '; repairs (reportdry), (promptonce)', 9: '; repair (required)', 12: '; repair (plants)',
               13: '; traced at this act: tools/standing/fold/checks.tpl :2108 prints a retired arm’s reading, drives no verdict, and stands outside (R339)(2); carried'}
C1_CLASSES = (
    ('redir', 'the REDIR class (`(R339)`(2)(i), event (2), defects (h), (k))', 'the hook reaches a redirect inside an inner shell’s quoted argument and the redirect-by-cmdlet forms; the banked REDIR rows replayed and refused, a planted clean command passed. The citation missed: `> $null` stands in no bank, every banked form was refused when it ran, and nothing slipped past (relay data/b729_stepzero.txt :22-:26)'),
    ('reportdry', 'report dry before the lock (`(R339)`(2)(ii), event (6))', 'the registration gate reads the rendered report tool at step [5a], and the seal refuses where its bank is absent or failing; b728’s sk fails it'),
    ('required', 'the required list (`(R339)`(2)(iii), event (9))', 'REQUIRED_BANKS read against what the root route can list; data/b726_mechanisms.txt refused as an unlistable name'),
    ('plants', 'the two plants (`(R339)`(2)(iv), event (12))', 'G-SEAL-HASHES’ plant fails and G-TRAIL-CARRIES-SEAL’s mutates, each replayed over b728’s state'),
    ('scanback', 'the scan written back (`(R339)`(2)(v))', 'a post-lock scan writes its own bank, outside the locked set; b728’s bank was last written before its lock, the closing’s foot reproduced in the bank form'),
    ('n5count', 'N5’s count (`(R339)`(2)(vi), event (4))', 'the count of README writes derived from the (W) list; b728’s three read as three'),
    ('nouns', 'counts and nouns from the banks (`(R339)`(2)(vii), events (3), (5))', 'a typed count or object noun that differs from its bank halts the citation check; “theorem” against data/b728_c2.txt halts, and seven against the table’s six'),
    ('promptonce', 'the prompt-once clause (`(R339)`(2)(viii), event (6))', 'a halt after the root that needs the author’s word counts as a prompt in the head line; b728’s three read as three'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b728’s events bank (relay data/b728_events.txt) carries thirteen rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-five lettered rows, (a)-(y), each tagged in its own bracket (%s); its refusal bank nine lines at b728’s closing commit %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_PREV_CLOSE), '']
    L += ['', '**The repairs of `(R339)`(2), at tools/standing/ v1.9.0, each with a control on b728’s banks, failing on the route before the repair '
          'and passing after, both instances printed** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b728’s events (1)-(13):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?(\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?|post-push|pre-push and post-push): ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b728_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b728’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b728_defects.txt; %s; %s; %s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c))]
    L += ['', '**b728’s refusals** (relay data/b728_hook_refusals.txt at %s, one a line): ' % C1_PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (thirteen events, twenty-five defects), as b728’s closing prints it (relay data/b728_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b729 on the author’s ruling `(R339)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b729.py) from '
          'b728’s events, defects and refusal banks read unedited, and the v1.9.0 controls bank; banked as relay `data/b729_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b728’s record; no sealed tool, face, trail or root-named bank of b728 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b729 -- THE CORRIGENDUM FOR b728, (R339)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b728_events.txt rows (1)-(13), data/b728_defects.txt 25 rows, data/b728_hook_refusals.txt 9 '
             'lines at %s; data/%s (the v1.9.0 controls); the corrigenda bank`s last row (%d).' % (C1_PREV_CLOSE, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 13, DEFECTS 25 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.9.0: THE REDIR CLASS, '
               'REPORT DRY, THE REQUIRED LIST, THE PLANTS, THE SCAN, N5`S COUNT, THE NOUNS, THE PROMPT-ONCE CLAUSE ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b728 at its weight after its entry, and the corrigendum for b728, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.9.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b729, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b729 ran three
# ### ((R339)(4)(iii)-(iv), N1), rowed in data/b729_dispatch_rows.json. Replaced for b729 alone; the arms' names stand, their plants on b729's rows.
#⟪OVERRIDE checks 1129 1141⟫
def rebuild_wf_ok(S):
    """(R338)(7), as b728 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R339), N1, b729: the dispatches of (R339)(4)-(5) -- at most eight, six on c2-b725 and two on keiper-b725; every dispatch read by its run id; the rows' runs the worklist's."""
    rows = S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    return bool(disp) and len(disp) <= K.MAX_DISPATCHES and sum(1 for r in disp if str(r.get('item', '')).startswith('(4)')) <= K.MAX_C2 \
        and sum(1 for r in disp if str(r.get('item', '')).startswith('(5)')) <= K.MAX_KEIPER \
        and sorted(str(r['run']) for r in disp) == sorted(str(r['run']) for r in reads) == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪OVERRIDE checks 1170 1173⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        pu_ = [j for j, r in enumerate(rows) if r.get('kind') == 'push' and r.get('sha') == d_.get('sha')]
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(pu_) == 1 and len(rd_) == 1 and pu_[0] < i_ < rd_[0]
#⟪END⟫
# ### b729, Component 5 (the Edit tool): v1.9.0 edited tools/standing/hook.py for the REDIR class ((R339)(2)(i)); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.9.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks 1521 1521⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) == cr0(blob(ROOT, 'HEAD:tools/standing/hook.py')) \
        and [h[:8] for h in gs(ROOT, 'log', '--format=%H', '%s..HEAD' % PRE['relay'], '--', 'tools/standing/hook.py').split()] == [K.C1_STANDING] \
#⟪END⟫
#⟪OVERRIDE checks 1664 1664⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, edited this act by v1.9.0`s commit 17ee7abd alone (the REDIR class); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b729, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b728's record has eighteen
#⟪OVERRIDE checks 983 983⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 14)) \
#⟪END⟫
# ### b729, Component 4 (the Edit tool): b729's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b728's override of checks 526 -- no registration commit -- removed: b729
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 754 754⟫
    return len(tips) >= len(NAMED_PUSH) == 6 and 'data/b729_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b729, Component 6 (the Edit tool): b729's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b728's wording
#⟪OVERRIDE checks 779 779⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b729, Component 4 (the Edit tool): b728's overrides of checks 1516 and 1659 (hook.py edited by b728's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b729 as it stands
# ### b729, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 988 988⟫
        and 'data/b729_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b729, Component 4 (the Edit tool): b728's override of checks 1476-1482 (one ERRATA entry at b728's (R338)(5)) removed -- (R339)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b729 as it stands
# ### b729, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b728's step-zero wording; b729's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 744 744⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 6 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks 745 745⟫
        and 'port-b707' in z and 'KEPT as banked: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b729, Component 4 (the Edit tool): G-RUNNER-READ's plant on b729's dispatch rows -- run 2's axiom lines carrying sorryAx (b728's
# ### plant read the lv rows' closure log, which b729 does not write)
#⟪OVERRIDE checks 1691 1691⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b729, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b729, Component 6 (the Edit tool): the fold bank was b728's own route
# ### (tools/b728_fold.py); b729's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b729_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1008 1008 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b728.py -> tools/acts/b729.py' in (rd('b729_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b729, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks 1011 1011 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b729_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b729, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b729_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 259 266 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b729_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b729, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R339): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 340 341⟫
    rows = [l for n_ in ('b729_defects.txt', 'b729_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R339) Component 4, the act`s events and defects together; relay data/b729_defects.txt, data/b729_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b729, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b729's orders are (R339)(10)'s six,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 395 396⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-CHAIN-PAGE-LLM-LINE, entered at b728,',
    '        W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b729, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b728's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b729_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b729_registration_%s.txt' % __import__('b729_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b729, Component 4 (the Edit tool, before the face): b728's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b729, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b729's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's two branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b729, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R339)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b729 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b729, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b728's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b729 scorer reads; the needles set to the banks b729's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 906 907 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_onset_fit.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b729, Component 3 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b728's ruling's form; (R339)(9) writes "; kept: c2-b725, keiper-b725, detect-b729 once made, and the rest as banked." naming port-b707 nowhere
# ### (data/b729_ferry.txt :23), so the arm failed on the act's real deletes; read as written, port-b707 still out of the deletes (defect (u))
#⟪OVERRIDE checks 767 770 REPAIR (needle)⟫
    # ### (R338)(9) wrote "port-b707 kept;" and (R339)(9) writes "; kept: c2-b725, keiper-b725, detect-b729 once made, and the rest as banked."; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or '; kept: c2-b725, keiper-b725, detect-b729 once made, and the rest as banked.' in S['ferry']) \
#⟪END⟫
# ### b729, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b729_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxy'))   # ### (a)-(y), entered before the lock, every one the seat's (data/b729_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b729_corrigendum.txt', 'data/b729_standing_v190.txt', 'data/b729_c2.txt', 'data/b729_lambda2.txt', 'data/b729_detection.txt', 'data/b729_count_price.txt',
                  'data/b729_dispatch_rows.json', 'data/b729_registrations.txt', 'data/b729_onset_fit.txt', 'data/b729_onset_pred.txt', 'data/b729_onset_score.txt',
                  'data/b729_reproduce.txt', 'data/b729_reproduce.json', 'data/b729_address_scan.txt', 'data/b729_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b729 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R339)(9): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b729_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R339)(1)-(7), Component 5 (b729's keys over b729's objects): the order by ancestry; v1.9.0's controls; the C2, lambda_2, detection and count banks and the dispatch rows;
        # ### H-ONSET-C's fit, predictions and score; the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### H-ONSET-C's registration at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v190', K.STANDING_COMMIT, K.C1_STANDING), ('v190_fit', K.C1_STANDING, K.FIT_COMMIT), ('fit_reg', K.FIT_COMMIT, K.REG_COMMIT), ('reg_pred', K.REG_COMMIT, K.PRED_COMMIT),
                                 ('pred_onset', K.PRED_COMMIT, K.ONSET_COMMIT), ('c1_corr', K.C1_RELAY, K.C1_CORR), ('corr_c3', K.C1_CORR, K.C3_RELAY[0]), ('c3_c2', K.C3_RELAY[0], K.C2_RELAY))),
        v190=rd('b729_standing_v190.txt'), fit=rd('b729_onset_fit.txt'), pred=rd('b729_onset_pred.txt'), score=rd('b729_onset_score.txt'), c2=rd('b729_c2.txt'), lambda2=rd('b729_lambda2.txt'),
        detection=rd('b729_detection.txt'), count_price=rd('b729_count_price.txt'),
        keiper_src=_s(blob(EF, '%s:SIDEExplicitFormula/KeiperGammaBound.lean' % K.EF_BRANCHES[0][1])), c2_src=_s(blob(EF, '%s:SIDEExplicitFormula/C2Theorem.lean' % K.EF_BRANCHES[1][1])),
        detect_src=_s(blob(EF, '%s:SIDEExplicitFormula/Schema/SupportDetection.lean' % K.EF_BRANCHES[2][1])),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b729_dispatch_rows.json') or '[]'), reproduce=rd('b729_reproduce.txt'), reproducej=jl('b729_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b729_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b728 left them
        rebuild=None, rebuild_rows=json.loads(rd('b729_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
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
# ### b729's read-first bank's items by path, as its step zero wrote them (data/b729_readfirst.txt :9-:25)
READFIRST_NEEDLES = ('relay data/b728_closing.txt |', 'relay data/b728_events.txt |', 'relay data/b728_defects.txt |', 'relay data/b728_sitting.txt |',
                     'relay data/b724_legacy.txt |', 'relay data/b725_dial.txt |', 'relay data/b725_onset_mass.txt |', 'relay data/b725_interference.txt |',
                     'relay data/b723_support.txt |', 'relay data/b709_grid.txt |', 'relay data/b723_axiom.txt |', 'relay data/b726_c2.txt |', 'relay data/b726_mechanisms.txt |',
                     'SIDE-explicit-formula KeiperIdentities.lean |', 'SIDE-explicit-formula KeiperBounds.lean |', 'PLACE-papers REGISTRY.md |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R339)(1)-(2))', 'THE C2 THEOREM ((R339)(3))', 'THE gamma_1 BOUND ((R339)(4))', 'THE DETECTION STATEMENT AND THE COUNT LAW ((R339)(5)-(6))', 'H-ONSET-C ((R339)(7))', 'NAME AND ADDRESS ((R339)(9))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (82 = 80 + 2, data/b729_citation_check.txt, the two misses printed there and carried for the author); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 2 and int(m.group(1)) == 82 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b728's figures, read at FINDINGS :12141 as Component 1 landed them
    return landed(S, 0, ['b728 AT ITS WEIGHT', 'suite 113 of 116', 'the closing’s 0650a188', '25 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b729's title in the ferry's Component 5 form (the record tool's _title over the banks); the first needle lower-case, the arm folding the article
TITLE_NEEDLES = ('the C2 theorem compiled at ', ' of 18 with its lemmas', '; lambda_2 > 0 with the standard three', '; the detection theorem stated and graded ', ', priced in ',
                 '; the count law priced', '; H-ONSET-C ', '; the REDIR class repaired')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R339)(1)-(2): the generated entry for b728's thirteen events and twenty-five defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(13), the defects by the one lettering, no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 4, CLOSE 34 over 38, REPEAT 11); the repairs at tools/standing/ v1.9.0 by their controls
    bank; the corrigenda bank appended at row (49) and nothing before it changed; in Component 1's commits (the figures read from
    data/b729_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 25 and len(items) == j.get('items') == 38 and j.get('row') == 49 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 38 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 4 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 11 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.9.0' and (j.get('repairs') or {}).get('bank') == 'data/b729_standing_v190.txt' \
        and (j.get('notes') or []) == [] \
        and '  (49) ' in S['corrigenda'] and '  (50) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b729_rules.txt and data/b730_rules.txt, by form in (R339)(9)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b728's form, its names b729's); no author's word of b729 orders a rules row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b729_rules.txt')) and not os.path.exists(os.path.join(D, 'b729_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b729's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- THE C2 THEOREM', 'KERNEL -- lambda_2', 'CERTIFIED -- tools/standing/ v1.9.0', 'REGISTERED -- H-ONSET-C', 'REGISTERED -- THE DETECTION STATEMENT', 'REGISTERED -- THE COUNT PRICE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b729: the dispatches of (R339)(3)-(4) -- each `gh workflow run` command of the capture a row of the bank, the rows' count the worklist's and within the cap, every
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
# ### b729's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The C2 theorem**', '**lambda_2**', '**The detection statement**', '**The count law**', '**H-ONSET-C**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b729_corrigendum.txt', 'data/b729_standing_v190.txt', 'data/b729_c2.txt', 'data/b729_lambda2.txt', 'data/b729_detection.txt', 'data/b729_count_price.txt', 'data/b729_onset_score.txt',
                 'data/b729_reproduce.txt', 'data/b729_address_scan.txt', 'data/b729_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b729: no row of the defects bank the navigator's ((a)-(o) the seat's)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R339)(7), N2 (the name the frozen run list carries): H-ONSET-C's order by ancestry -- the fit before the registration, the registration committed alone and before the predictions, the predictions by a commit of their own
    and before the onsets' commit; the registration at HEAD its text at its commit; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    return S['files']['reg'] == [K.REGISTRATIONS] and bool(reg) and reg == head \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R339)(9), N5, the scan arm (the name the frozen run list carries): tools/b729_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    SIDE-explicit-formula's three branches; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address and name read from
    history and held in memory -- the address 0, the author's name 0, the previous name 0, its four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R339)(7), N2, N3 (the name the frozen run list carries): H-ONSET-C -- the fit's five residuals POST HOC and the controls before any onset; the score bank's verdict one of the registration's, its onset rows' deviations
    the rows' a over a*_pred, a computed row marked by the falsifier's 0.05 as its figure falls; the scope printed; no sentence of the score calling the candidate a law."""
    sc, v = S['score'] or '', _vlast(S['score'])
    m = re.match(r'H-ONSET-C (HELD at 2|REFUTED|CARRIED, HELD AT ONE|CARRIED) ; ONSETS COMPUTED (\d+) ;', v)
    rows = re.findall(r'(?m)^  (off24|off44) the onset at \S+, a = ([\d.]+) ; a\*_pred ([\d.]+) ; a\*/a\*_pred - 1 = ([+-][\d.]+) ; (WITHIN|BEYOND) 0\.05$', sc)
    good = all(abs(float(a) / float(p) - 1 - float(d)) < 1e-5 and (abs(float(d)) <= 0.05) == (w == 'WITHIN') for _z, a, p, d, w in rows)
    bound = re.findall(r'(?m)^  (off24|off44) no onset computed; positive to a = ([\d.]+), so a\*/a\*_pred - 1 > ([+-][\d.]+) ; REFUTED BY THE BOUND$', sc)
    fired = any(w == 'BEYOND' for _z, _a, _p, _d, w in rows) or bool(bound)
    return bool(m) and good and (m.group(1) == 'REFUTED') == fired and int(m.group(2)) == len(rows) and 'FIVE RESIDUALS PRINTED' in (S['fit'] or '') and 'C1 AND C2 AS WANTED' in (S['fit'] or '') \
        and 'ONSETS COMPUTED 0' in _vlast(S['pred']) and 'a HELD is two points, not a law' in sc and not re.search(r'H-ONSET-C[^.;\n]*\blaw\b', sc)
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R339)(3), N1, N3 (the name the frozen run list carries): the C2 bank -- the dispatches on c2-b725 at most three, each read by its run id; the theorem's read at build exit 0, 18 certificates traced KERNEL, no sorryAx, c2_value_law and
    c2_least_negative at the standard three in the artifact's own lines; the module at the tip carrying no sorry and the scope in a comment; the foot's count the rows'."""
    t, rows = S['c2'] or '', S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch' and str(r.get('item', '')).startswith('(3)')]
    reads = [r for r in rows if r.get('kind') == 'read' and str(r.get('item', '')).startswith('(3)')]
    th = [r for r in reads if r.get('verdict') == 'KERNEL' and str(r.get('build_exit')) == '0' and not r.get('sorryAx') and len(r.get('traces') or {}) == 18 and set((r.get('traces') or {}).values()) == {'KERNEL'}
          and all(any(("C2Walk.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % n) in l for l in r.get('axioms_lines') or []) for n in ('c2_value_law', 'c2_least_negative'))]
    m = re.search(r'THE C2 THEOREM: c2_value_law AND c2_least_negative COMPILED AT (\d+) OF 18 ; AXIOMS propext, Classical\.choice, Quot\.sound ; NO sorry ; E0 DERIVES ; DISPATCHES (\d+) OF AT MOST 3', _vlast(t))
    return bool(m) and bool(disp) and len(disp) <= K.MAX_C2 and len(reads) == len(disp) and sorted(str(r['run']) for r in reads) == sorted(str(r['run']) for r in disp) \
        and bool(th) and int(m.group(1)) == 18 and int(m.group(2)) == len(disp) and bool(S['c2_src']) and 'sorry' not in S['c2_src'] and 'Baker 1971' in S['c2_src'] and 'Stark 1975' in S['c2_src']
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R339)(5) (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the three branches each at the worklist's tip locally and at origin; no kernel's main moved (G-MERGES-ON-GATE's read); the detection statement
    on detect-b729 five definitions, no `theorem`, no `sorry`: stated and not proved."""
    tp = S['ef_tips'] or {}
    src = S['detect_src'] or ''
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and bool(src) and not re.search(r'(?m)^\s*(theorem|lemma)\b', src) and 'sorry' not in src and 'def SupportDetection' in src and 'def StripCertificate' in src

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.9.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v190') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.9.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b728's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R339)(4)-(6), N1, N3 (the name the frozen run list carries): the gamma_1 bound -- the dispatches on keiper-b725 at most two, each read by its run id, the module at the tip carrying no sorry, liCoeff_two_pos at the standard three;
    the detection bank's foot the grade, the lemmas and the words NOT COMPILED, NO PROOF; the count bank's foot its lemmas and NOTHING BUILT."""
    t, rows = S['lambda2'] or '', S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch' and str(r.get('item', '')).startswith('(4)')]
    reads = [r for r in rows if r.get('kind') == 'read' and str(r.get('item', '')).startswith('(4)')]
    return bool(disp) and len(disp) <= K.MAX_KEIPER and sorted(str(r['run']) for r in reads) == sorted(str(r['run']) for r in disp) \
        and bool(S['keiper_src']) and 'sorry' not in S['keiper_src'] and _vlast(t).startswith('lambda_2 > 0 COMPILED WITH THE STANDARD THREE') \
        and any("liCoeff_two_pos' depends on axioms: [propext, Classical.choice, Quot.sound]" in l for r in reads for l in r.get('axioms_lines') or []) \
        and 'NOT COMPILED, NO PROOF' in _vlast(S['detection']) and 'PRICED IN 14 LEMMAS' in _vlast(S['detection']) and 'NOTHING BUILT' in _vlast(S['count_price'])


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b728's (R338)(7), carried in the run list): tools/research/reproduce.py's full run banked this
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
    """standing clauses v9 (Component 7 of (R339): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b729_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b728's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R339-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b728's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R339) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b728's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R338)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 82 = 80 OK + 2 misses, the two printed, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b728-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the C2 theorem; lambda_2; the detection theorem; the count law; H-ONSET-C; the REDIR class), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R339)(1)-(2): the generated corrigendum for b728`s record, landed at FINDINGS :12143: its thirteen events and twenty-five defects, 38 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 4 CLOSE 34, REPEAT 11; v1.9.0`s repairs by data/b729_standing_v190.txt; the corrigenda bank appended at row (49)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b729 and no b729 rules bank: no author`s word of b729 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b729's objects
    ('G-REGISTRATIONS-FIRST', '(R339)(7), N2: H-ONSET-C`s order by ancestry: the fit, the registration committed alone, the predictions by their own commit, the onsets; the registration at HEAD its text at d1f94c17; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(reg_pred=False))),
    ('G-PREDICTION-FIRST', '(R339)(9), N5, the scan arm: tools/b729_address_scan.py run live over every commit of the act in the relay, PLACE-papers and the three branches, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R339)(7), N2, N3: H-ONSET-C: the fit`s residuals and controls before any onset, the verdict one of the registration`s, each onset row`s deviation its own a over a*_pred, the scope printed, no sentence a law',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'score', (S['score'] or '').replace('a HELD is two points, not a law', 'a HELD'))),
    ('G-DERIVATION-GRADED', '(R339)(3), N1, N3: the C2 bank: at most three dispatches each read by its run id, exit 0, 18 certificates traced KERNEL, no sorryAx, c2_value_law and c2_least_negative at the standard three, no sorry at the tip, the scope in a comment',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'drows', lambda d: [r.update(sorryAx=True) for r in d if r.get('kind') == 'read'])),
    ('G-OFFSET-POST-HOC', 'N5, (R339)(5): SIDE-explicit-formula`s main at its base, the three branches each at the worklist`s tip locally and at origin; the detection statement five definitions, no theorem, no sorry',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'detect_src', (S['detect_src'] or '') + NL + 'theorem planted : True := by sorry')),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at 0650a188, VERSION 9; v8 at HEAD its blob at 0650a188; no v10; v9`s commit an ancestor of v1.9.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R339)(4)-(6), N1, N3: gamma_1: at most two dispatches each read by its run id, no sorry at the tip, liCoeff_two_pos at the standard three; the detection foot NOT COMPILED, NO PROOF and its 14 lemmas; the count foot NOTHING BUILT',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'keiper_src', (S['keiper_src'] or '') + NL + 'sorry')),
    ('G-DIFFERS-ERRATA', '(R339): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 07910b7, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b729_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R339-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b728`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at e2246a8e (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: the dispatches of (R339)(3)-(4), five at most, three and two, each read by its run id; the rows` runs the worklist`s',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: each `gh workflow run` of the capture a row, the count within the cap, each push before its dispatch before its read, the rows` free memory at the hold; no b721-b728 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b728 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b728`s [41] tip; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers alone); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b728`s trail record on OPEN_TRAILS (:16820) and its root in the chain', lambda S: '### b728 — lane two, act one hundred and fifty-five, the research act under (R338)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers alone): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b728`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: five at most; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
# ### b729, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R339)(3): a main at its sitting tip, its tags unmoved, is not a move against b728's face
#⟪OVERRIDE record 2554 2554⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b729: (R339)'s rows. (1)'s line quoted by the ruling from the public relay at 0650a188
    pub = _blob('D:/relay', '0650a188', 'data/b728_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b728_closing.txt :1, the head line as the public relay carries it at 0650a188', bool(pub) and pub[0] == at(cl, 1) and 'relay 90d7af67' in pub[0] and 'PLACE-papers 26fb938' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 113 of 116', 'root b097c2b0b6fc6269', '4 prompts answered', 'scores 8 of 8 HELD', '25 defects'):
        add('ruling (1)', 'data/b728_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'data/b728_closing.txt :5, the counter CLAIM 4, CLOSE 34, REPEAT 11 OF 38', 'CLAIM 4, CLOSE 34, REPEAT 11 OF 38' in at(cl, 5), at(cl, 5)[-40:], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b728']]
    add('ruling (1)', 'data/act_roots.txt, b728`s root b097c2b0 chained from b727`s c527524a', len(ar8_) == 1 and ar8_[0][1].startswith('b097c2b0') and ar8_[0][2].startswith('c527524a'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b728_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b728 (b728`s post-push part b3)', 'b728 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b728 AGREE' if 'b728 AGREE' in b3_ else 'ABSENT', '1')
    for f_, w_, why_ in (('b728_c2.txt', '18 OF 18 FIELDS COMPILED WITH NO AXIOM', 'the certificates'), ('b728_c2.txt', 'WHAT REMAINS: (L1), (L2), c2_value_law', 'what remains'),
                         ('b728_lambda2.txt', 'REMAINS (stieltjes 1).re < -1/20', 'lambda_2'), ('b728_onset_table.txt', 'THE PAIRS DO NOT AGREE WITHIN 10%', 'the table'),
                         ('b728_onset_table.txt', 'M_C (Spearman +0.90)', 'the quantity moving'), ('b728_standing_v180.txt', 'CASES 23 ; AS WANTED 23', 'the controls')):
        add('ruling (1)', 'data/%s carries %s' % (f_, w_), w_ in (rd(p('data', f_)) or ''), why_, '1')
    add('ruling (1)', 'tools/standing/VERSION v1.8.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.8.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(13) and 25 defects (data/b728_events.txt, data/b728_defects.txt)',
        starts == list(range(1, 14)) and len(letters) == 25, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((6, 2, 'CLOSE ; REPEAT b726 (a)'), (17, 6, 'CLOSE ; NEW'), (29, 9, 'CLOSE ; NEW'), (37, 12, 'CLOSE ; NEW')):
        add('ferry (read first)', 'event (%d) at data/b728_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:70], at(ev, n_)[:50], '1')
    add('ferry (read first)', 'data/b728_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    for f_ in ('b728_postclose_rulings.txt', 'b728_author_answers.txt', 'b728_c2.txt', 'b728_lambda2.txt', 'b728_onset_table.txt', 'b728_visibility.txt', 'b728_report_wrapper.txt', 'b716_epstein_count_price.txt', 'b725_onset_mass.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    # ### (R339)(2)(i), the fact clause: the forms the ruling names against the banks of b726-b728
    hr_ = ''.join(rd(p('data', 'b72%d_hook_refusals.txt' % n_)) or '' for n_ in (6, 7, 8))
    add('ruling (2)(i)', 'the `> $null` form the ruling says the banks of b726-b728 hold (a form slipped past the hook) -- data/b726-b728_hook_refusals.txt', '$null' in hr_, 'in the refusal banks %s' % ('$null' in hr_), '1')
    add('ruling (2)(i)', 'the `2>&1` form, a refusal of data/b727_hook_refusals.txt', '2>&1' in hr_, 'in the refusal banks %s' % ('2>&1' in hr_), '1')
    add('ruling (2)(i)', 'three banked REDIR refusals to replay (b727, b728 :5, :8, :9 -- four rows)', hr_.count('| REDIR |') >= 3, 'REDIR rows %d' % hr_.count('| REDIR |'), '1')
    om_ = lines_of(p('data', 'b725_onset_mass.txt'))
    add('ruling (7), (2)(ix)', 'data/b725_onset_mass.txt :15, off44 and :18, off24 by name', at(om_, 15).lstrip().startswith('off44') and at(om_, 18).lstrip().startswith('off24'), at(om_, 15)[:30], '4')
    add('ruling (7)', 'off44 a zero whose onset the ladder reaches ((R339)(7) tests at it) -- data/b725_onset_mass.txt :17', 'beyond reach' not in at(om_, 17), at(om_, 17)[:70], '4')
    ot_ = lines_of(p('data', 'b728_onset_table.txt'))
    add('ruling (7)', 'data/b728_onset_table.txt :30-:34, the five computed onsets` C rows, off52 at :35 a bound', all('M_C' in at(ot_, n_) for n_ in range(30, 36)) and '>=(a BOUND)' in at(ot_, 27), at(ot_, 34)[:30], '4')
    kb_ = gr('D:/SIDE-explicit-formula', 'show', 'keiper-b725:SIDEExplicitFormula/KeiperBounds.lean').split(NL)
    add('ruling (4)', 'KeiperBounds.lean :98-:112 on keiper-b725, higher_stieltjes among them', any('higher_stieltjes' in at(kb_, n_) for n_ in range(98, 113)), 'read', '2')
    cw_ = gr('D:/SIDE-explicit-formula', 'show', 'c2-b725:SIDEExplicitFormula/C2Walk.lean')
    for w_ in ('def L1 : Prop', 'def L2 : Prop', 'def C2ValueLaw : Prop', 'def cert (D : Int)'):
        add('ruling (3)', 'C2Walk.lean on c2-b725 carries %s' % w_, w_ in cw_, 'read', '2')
    dt_ = gr('D:/SIDE-explicit-formula', 'show', 'main:SIDEExplicitFormula/Schema/Detector.lean').split(NL)
    fo_ = gr('D:/SIDE-explicit-formula', 'show', 'main:SIDEExplicitFormula/FirstOrderBound.lean').split(NL)
    add('ruling (5)', 'Schema/Detector.lean :99-:125, the detector theorem', any('theorem detector' in at(dt_, n_) for n_ in range(99, 126)), 'read', '3')
    add('ruling (5)', 'FirstOrderBound.lean :149, B1', 'offScore_plateau_first_order' in at(fo_, 149) or 'offScore_plateau_first_order' in at(fo_, 148), at(fo_, 149)[:60], '3')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ferry (read first)', 'REGISTRY :134, PHASE 1.5', at(rg_, 134).startswith('## PHASE 1.5'), at(rg_, 134)[:40], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    for k_ in ('SIDE-explicit-formula', 'SIDE-rcurve', 'SIDE-archimedean', 'SIDE-spinor'):
        add('PATHS', '%s at D:/%s' % (k_, k_), os.path.isdir('D:/%s/.git' % k_), 'D:/' + k_, '0')
    add('ferry', 'tools/standing/ at v1.8.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.8.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R339)(9): b728's export, the mirror's last
    add('ruling (9)', 'D:/MY-DOwnloads/mirror-refresh-2026-10-31-b728.zip, b728`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R339)(3)-(5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (9)', 'the push-b728-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R339)(9): act_current alone, then b728's step row 36 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b728_steps.json'),
                   (K.STEPZERO, 'data/b728_relay_push-b728-closing_push_out.txt')):
        if not c_:
            add('ruling (9)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (9)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (9)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (9)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (9)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b729_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b729_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b729 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b728_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 5) are the corrigendum with v1.9.0's controls, the C2 theorem, the gamma_1 bound, the detection statement and the count price, H-ONSET-C's score, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R339)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R339)(11)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: on the branches c2-b725, keiper-b725 and detect-b729 of SIDE-explicit-formula alone, the Lean modules of (R339)(3)-(5); no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b730 ((R339)(11)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R338)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b729 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-SIX, THE COMPILE ACT: THE C2 THEOREM; THE gamma_1 BOUND; THE DETECTION STATEMENT AND THE COUNT PRICE; '
              'H-ONSET-C FITTED ON FIVE AND TESTED ON TWO; v1.9.0 LANDED, UNDER (R339).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b728's sections over b728's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.9.0: the REDIR class, the report dry, the required list, the plants, the scan, N5`s count, the nouns and the prompt-once clause, each case failing before its repair and passing after', 'b729_standing_v190.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE C2 THEOREM ((R339)(3))', [
                ('c2_value_law and c2_least_negative, one build, axioms printed, E0 printed, the scope in a comment', 'b729_c2.txt')]),
            ('THE gamma_1 BOUND ((R339)(4))', [
                ('(stieltjes 1).re < -1/20 and liCoeff_two_pos, axioms printed, the numeric control in order', 'b729_lambda2.txt')]),
            ('THE DETECTION STATEMENT AND THE COUNT LAW ((R339)(5)-(6))', [
                ('the statement on detect-b729, graded, not compiled, no proof, priced', 'b729_detection.txt'),
                ('the count law priced; the count alone does not move the instance', 'b729_count_price.txt')]),
            ('H-ONSET-C ((R339)(7))', [
                ('the fit on five, POST HOC, the controls', 'b729_onset_fit.txt', r'(?m)^### ### \*\*H-ONSET-C`S CONTROLS'),
                ('the predictions by their own commit', 'b729_onset_pred.txt'),
                ('the onsets at off24 and off44 and the registration`s verdict', 'b729_onset_score.txt')]),
            ('THE NAME AND ADDRESS ((R339)(9))', [
                ('the scan over every commit and bank of the act, the counts alone', 'b729_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b728`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b729_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: no kernel`s main ; ' + FF.n5_kernel_clause() + ' ;',
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; on its branches c2-b725, keiper-b725 and detect-b729 alone the Lean modules of (R339)(3)-(5), each pushed through push_gated.sh, off main, untagged ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1, five at most), each read by its run id, relay data/b729_dispatch_rows.json ; the rebuild-b721 branches of the wave 1 kernels as b728 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part, computation, push and dispatch ;',
    '    the push-b728-* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message ; N2: H-ONSET-C`s fit, registration, predictions and onsets in that order by ancestry ;',
    '    N3: every grade at its bank`s end ; (R339)(9): no new occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay data/b729_address_scan.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the workflow dispatches under the GitHub login') + ' ;',
    '    nothing deposited ; the deposit route untouched, publish never called, the draft held at v5 ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) written ; no paper cut, moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt (b729`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.9.0 by (R339)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b728 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R339)(11)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For b730, each from its bank: the detection theorem`s 14 lemmas, unbuilt (relay data/b729_detection.txt); the count law and the four other premises, unbuilt (relay data/b729_count_price.txt); the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b729_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ((R339)(8)) ; H-ONSET-C as scored (relay data/b729_onset_score.txt) ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ' and detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b728 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b728`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b729: the standing repairs are v1.9.0's ((R339)(2), relay data/b729_standing_v190.txt, read in the corrigendum section); the
    # ### carry's diffs here (b729 carried at step zero before the fold; its tools since are the templates and tools/acts/b729.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b728 left them; port-b707 at b712`s tip %s)' % (
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
    b729's form over b729's objects (b728's form in git at b728's record tool): the corrigendum's foot and v1.9.0's controls; the C2, lambda_2, detection, count and onset banks' feet;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v190.txt' % ACT, r'\*\*v1\.9\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.9.0`s controls')
    c2 = _bfig('%s_c2.txt' % ACT, r'\*\*THE C2 THEOREM: c2_value_law AND c2_least_negative COMPILED AT (\d+) OF 18 ; AXIOMS ([^;]+?) ; NO sorry ; E0 (\w+) ; DISPATCHES (\d+) OF AT MOST 3', 'the C2 foot')
    l2 = _bfig('%s_lambda2.txt' % ACT, r'\*\*lambda_2 > 0 COMPILED WITH THE STANDARD THREE, RUN (\d+), ONE DISPATCH OF TWO ; ([^;]+?) ;', 'the gamma_1 foot')
    dt = _bfig('%s_detection.txt' % ACT, r'SupportDetection STATED ON detect-b729, GRADED (\w+); StripCertificate ([A-Z-]+) ON ITS CERTIFICATE ; NOT COMPILED, NO PROOF ; PRICED IN (\d+) LEMMAS, (\d+) WITH NO COMPILED NEIGHBOUR ; (\d+-\d+) DISPATCHES', 'the detection foot')
    cn = _bfig('%s_count_price.txt' % ACT, r'THE COUNT ALONE DOES NOT MOVE THE INSTANCE, FIVE FIELDS DO ; (\d+) LEMMAS, (\d+) ABSENT, FOR THE COUNT ; (\d+-\d+) DISPATCHES FOR ALL FIVE', 'the count foot')
    on = _bfig('%s_onset_score.txt' % ACT, r'\*\*H-ONSET-C ([^;]+?) ; ONSETS COMPUTED (\d+) ;', 'the onset score`s foot')
    onr = re.findall(r'(?m)^  (off24|off44) (.+)$', rdn('%s_onset_score.txt' % ACT))
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v190_ctl=v5[0], v190_cases=v5[1], v190_wanted=v5[2], repairs=len(v5[0].split(', ')),
                c2_k=int(c2[0]), c2_axioms=c2[1], c2_e0=c2[2], c2_disp=int(c2[3]), l2_run=l2[0], l2_clause=l2[1],
                det_grade=dt[0], det_strip=dt[1], det_lemmas=dt[2], det_open=dt[3], det_price=dt[4],
                cnt_lemmas=cn[0], cnt_absent=cn[1], cnt_price=cn[2],
                on_verdict=on[0], on_computed=on[1], on_rows=['%s %s' % r_ for r_ in onr],
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R339)(3)-(4): the kernel rows of one kind as banked (data/b729_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R339): no lean process runs on this host; the dispatches those of (R339)(3)-(4), five at most, each read by its run id. From the command bank (the seat's commands, read live from the
    capture by the `commands` route) and the dispatch rows beside the worklist's EF_RUNS."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b729_commands.json): %s; dispatch commands in the capture: %s, the worklist`s runs %d, each read by its run id: %s (relay data/b729_dispatch_rows.json)' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b729's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b729_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b729_c2.txt', '  CONTROL premise', '  c2_value_law '))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R339): the fit prints with its residuals before the registration, the registration is committed before any figure at off44 or off24, and the predictions by their own commit before any onset, the order printed by ancestry;
    each tool's controls before its figures."""
    log_ = g(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY).split()
    chain_ = [_first_add(p_) for p_ in ('data/b729_onset_fit.txt', 'data/b729_registrations.txt', 'data/b729_onset_pred.txt', 'data/b729_onset_score.txt')]
    pos_ = [_order_of(h_, log_) if h_ else None for h_ in chain_]
    order_ = all(p_ is not None for p_ in pos_) and pos_ == sorted(pos_) and len(set(pos_)) == 4
    t = rdn('%s_onset_fit.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = 'FIVE RESIDUALS PRINTED' in t and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the fit`s five residuals printed: %s; the fit, the registration, the predictions and the score first committed in that order: %s (%s); the tools` controls before their figures: %s' % (
            'FIVE RESIDUALS PRINTED' in t, order_, ' '.join((h_ or 'none')[:8] for h_ in chain_), ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b729's objects; b728's in git at b728's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b729_standing_v190.txt', ('ALL AS WANTED',)), ('b729_c2.txt', ('THE C2 THEOREM',)), ('b729_lambda2.txt', ('lambda_2',)), ('b729_detection.txt', ('SupportDetection',)),
             ('b729_count_price.txt', ('THE COUNT LAW PRICED',)), ('b729_onset_fit.txt', ('CONTROLS',)), ('b729_onset_pred.txt', ('PREDICTIONS BANKED',)), ('b729_onset_score.txt', ('H-ONSET-C',)),
             ('b729_citation_check.txt', ('CITES CHECKED',)), ('b729_reproduce.txt', ('REPRODUCES',)), ('b729_address_scan.txt', ('PREVIOUS ADDRESS',)))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R339): every grade prints at its end; the entry's nouns the banks' ("theorem" once c2_value_law compiled); no sentence of the entry calls H-ONSET-C a law, or lambda_2 a rung with no axiom print. From the banks' last
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
    bad = [s_ for s_ in sents if re.search(r'H-ONSET-C[^.;]*\blaw\b', s_) or (re.search(r'lambda_2[^.;]*\brung\b', s_) and 'axiom' not in s_)]
    ok = all(o for _n, o in graded) and not bad
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the entry`s sentences calling H-ONSET-C a law or lambda_2 a rung with no axiom print, read from %s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bad or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R339) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R339)(5))
# ### (R339)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R339) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b728's form, carried) -- read from git,
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
    # ### (R339)(3)-(5), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-explicit-formula's c2-b725, keiper-b725 or detect-b729; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b728 left them; the address scan's count from its bank (relay data/b729_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b729_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than c2-b725, keiper-b725 or detect-b729, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b729 — lane two, act one hundred and fifty-six, the compile act under (R339): b728 at its weight and its corrigendum; v1.9.0; '
            'the C2 theorem; the gamma_1 bound; the detection statement and the count price; H-ONSET-C')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 5 form adjusted to what the act did; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## The C2 theorem compiled at %d of 18 with its lemmas; lambda_2 > 0 with the standard three; the detection theorem stated and graded %s, priced in %s lemmas; '
            'the count law priced; H-ONSET-C %s; the REDIR class repaired' % (f['c2_k'], f['det_grade'], f['det_lemmas'], f['on_verdict']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the ruling’s “the one compile that moves the Epstein instance” against ZQPremises’ five fields: the count alone leaves INTERFACES, printed at relay data/b729_count_price.txt; (2) (6)’s b716 band against HCount at every height, different statements, printed there; '
            '(3) off24’s bracket wholly inside its window: the point could not fire, read at that weight; (4) the ruling’s falsifier has no “computed”: the seat’s bound reading fixed in the registration before any figure; '
            '(5) a run read `success` with build exit 1: the exit file governs; (6) %s and the seat’s %s '
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
            'author beside the next act of (R339)(10)): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b729's objects; b728's composer in git at
    b728's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The C2 theorem compiles at %d of 18 with its lemmas, axioms %s, E0 %s: for each row of the walk the least n with b(n) < 0 is n0 and b(n0) is the walk’s value; lambda_2 > 0 compiles with the standard three, %s; the support-face detection statement stands on detect-b729, graded %s, not compiled and not proved, priced in %s lemmas; '
         'the count law is priced, and the count alone does not move the Epstein instance, five fields do; H-ONSET-C reads %s; tools/standing/ stands at %s; the draft stands at v5, HELD.' % (
             f['c2_k'], f['c2_axioms'], f['c2_e0'], f['l2_clause'], f['det_grade'], f['det_lemmas'], f['on_verdict'], f['ver']), '',
         '*Filed at b729 on the author’s ruling `(R339)`; %d question%s put before the root. Banks: relay '
         '`data/b729_corrigendum.txt`, `data/b729_standing_v190.txt`, `data/b729_c2.txt`, `data/b729_lambda2.txt`, `data/b729_detection.txt`, `data/b729_count_price.txt`, `data/b729_dispatch_rows.json`, `data/b729_registrations.txt`, `data/b729_onset_fit.txt`, `data/b729_onset_pred.txt`, `data/b729_onset_score.txt`, '
         '`data/b729_reproduce.txt`, `data/b729_address_scan.txt`, `data/b729_touch.txt`, `data/b729_standing_figures.txt`, `data/b729_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R339)(1)-(2), `%s`, `%s`, `%s`): b728 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b728’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b729_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b729_standing_v190.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v190_ctl'], f['v190_cases'],
             f['v190_wanted']), '',
         '**The C2 theorem** ((R339)(3), N1): c2_value_law and c2_least_negative on c2-b725 at %s, (L1) and (L2) proved and joined to the eighteen certificates, all built by one run at one ref; %d dispatches of the three allowed, the first breaking on one line of the seat’s, each read by its run id; axioms %s, the certificates none; E0 %s, a control first. The list’s completeness is Baker 1971 and Stark 1975, cited in a comment and in no binder; that bL is the Dirichlet coefficient is the definition’s docstring, not compiled (relay data/b729_c2.txt, data/b729_dispatch_rows.json).' % (K.EF_BRANCHES[1][1][:8], f['c2_disp'], f['c2_axioms'], f['c2_e0']), '',
         '**lambda_2** ((R339)(4), N3): run %s, the one dispatch of two used: %s, and lambda_2 > 0, each at the standard three by the artifact’s axiom print; a numeric control beside the proof. One rung, axioms printed, not Li’s criterion (relay data/b729_lambda2.txt).' % (f['l2_run'], f['l2_clause']), '',
         '**The detection statement** ((R339)(5)): SupportDetection on detect-b729, graded %s, StripCertificate %s on its certificate; not compiled, no proof; priced in %s lemmas, %s with no compiled neighbour, %s dispatches the seat’s. The route is new, not detector’s: the compiled route cannot give K (relay data/b729_detection.txt).' % (f['det_grade'], f['det_strip'], f['det_lemmas'], f['det_open'], f['det_price']), '',
         '**The count law** ((R339)(6)): %s lemmas, %s absent, for the count; %s dispatches for all five premises, the seat’s. Against the ruling’s word, the count alone does not move the Epstein instance: ZQPremises has five fields, and b716’s band and the count at every height are different statements; nothing built (relay data/b729_count_price.txt).' % (f['cnt_lemmas'], f['cnt_absent'], f['cnt_price']), '',
         '**H-ONSET-C** ((R339)(7), N2): fitted on five POST HOC (relay data/b729_onset_fit.txt), registered alone at `%s`, predicted by a commit of its own at `%s`, then the onsets: %s. Verdict: %s. Off24’s bracket lay wholly inside its window, so that point could not fire. Fitted on five, tested on two (relay data/b729_onset_score.txt).' % (K.REG_COMMIT[:8], K.PRED_COMMIT[:8], ' ; '.join(f['on_rows']), f['on_verdict']), '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b729_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R339)(9), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b729_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b729_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b729 -- %s, %s, %s, %s -- against b728’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b729_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the theorem’s build and the onsets’ falsifier read one way: the exit file, not the conclusion, and the registered window, not the fit’s look, decide; '
         'and the pricing clauses returned what the ruling did not expect, the count alone moving nothing, a finding of the same weight as a compile.', '',
         '**Carried to:** %s: the detection theorem’s lemmas and the count law’s, unbuilt; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b728():
    """b728's form over b728's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b729's objects; b728's composer in git at b728's record tool): W-ORD-VISIBILITY annotated by its own line, then the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD with that line beneath it."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['**`W-ORD-VISIBILITY` CARRIED at b729, (R339)(8):** NOT CLEAN as b728 left it, no further read.']
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-VISIBILITY' not in op:
        sys.exit('### THE TRAIL: AN ANNOTATED ORDER NOT READ OPEN BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R339) ratified.** Its components as the ferry orders them (relay data/b729_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b728’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders annotated** ((R339)(8)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the line above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b729_standing_v190.txt).' % (
                 f['ver'], f['v190_cases'], f['v190_wanted']), '',
             '**The C2 theorem:** compiled at %d of 18 with its lemmas, axioms %s, E0 %s, %d dispatches (relay data/b729_c2.txt).' % (f['c2_k'], f['c2_axioms'], f['c2_e0'], f['c2_disp']), '',
             '**lambda_2:** > 0, with the standard three, %s (relay data/b729_lambda2.txt).' % f['l2_clause'], '',
             '**The detection statement:** on detect-b729, graded %s, not compiled, no proof, priced in %s lemmas (relay data/b729_detection.txt).' % (f['det_grade'], f['det_lemmas']), '',
             '**The count law:** %s lemmas, %s absent, for the count; five fields to move the instance (relay data/b729_count_price.txt).' % (f['cnt_lemmas'], f['cnt_absent']), '',
             '**H-ONSET-C:** %s; %s (relay data/b729_onset_score.txt).' % (f['on_verdict'], ' ; '.join(f['on_rows'])), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b729_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b729_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b729_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b729 `%s` (previous `%s`, b728’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b729_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b729_standing_v190.txt); the standing '
             'report tool (relay data/b729_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no main written, no tag; on SIDE-explicit-formula’s c2-b725, keiper-b725 and detect-b729 the Lean modules of (R339)(3)-(5), %d dispatches each read by its run id; the %s branches as b728 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b729_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b728’s %s, %s, %s, %s (relay data/b729_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b729_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b728():
    """b728's trail record over b728's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: those of (R339)(3)-(4), five at most; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b729*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725 and c2-b725, kept, and detect-b729, cut at (R339)(5); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b728 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b729*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s three branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b728`s and this act`s; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 6, 6, 'branches', '### (R339)(9): relay push-b728-closing, push-b728-preroot, push-b728-preroot2, push-b728-record; PLACE-papers push-b728-preroot, push-b728-record; each local, by name, after --merged listed it (data/b729_stepzero.txt).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: the Lean modules and print_targets.txt.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R339) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (26fb938d) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R339)(1)-(2): FINDINGS :12143.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R339)(1)-(2): one row.'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-VISIBILITY annotated CARRIED.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b729_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.9.0`s controls, H-ONSET-C`s fit, predictions and score, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 1, 1, 'commits', '### (R339)(7): H-ONSET-C at d1f94c17.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### the onset score and units; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none of this act`s; b725`s ladders carried and named in the registration.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### (R339)(3)-(5): MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R339)(2): tools/standing/ to v1.9.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R339)(9), N5: PREVIOUS ADDRESS 0; MEASURED off data/b729_address_scan.txt (the address never printed).'),
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
    # ### (R339)(7): the two figure banks of the registered object
    fig_banks = [p for p in ('data/b729_onset_score.txt', 'data/b729_onset_units.jsonl')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b729_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b729_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v190', 'onset_fit', 'onset_pred', 'onset_score', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b729_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b729_registration_%s.txt -- b729, THE COMPILE ACT: b728 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.9.0; THE C2 THEOREM; THE gamma_1 BOUND; "
                             "THE DETECTION STATEMENT AND THE COUNT PRICE; H-ONSET-C; NO DEPOSIT, NO TAG, UNDER (R339)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b728's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b729: b728's lines read banks this
act does not write, and are not carried; the lines are b729's: the C2 theorem and lambda_2 (KERNEL, on the runner only), tools/standing/ v1.9.0 by its controls (CERTIFIED), H-ONSET-C, the detection statement and the count price
(REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b729's lines, each from the record tool's figures over b729's banks
    # ------------------------------------------------------------------ KERNEL: (R339)(3)-(4), on the runner only
    sc2 = seat('%s_c2.txt' % ACT, '**THE C2 THEOREM: ')
    sk = sc2   # ### (R338)(2)(ii): the name the template appends
    keys['C2'] = ('KERNEL -- THE C2 THEOREM: c2_value_law and c2_least_negative compiled at %d of 18 with their lemmas, axioms %s, E0 %s, %d dispatches each read by its run id. SOURCE %s.' % (f['c2_k'], f['c2_axioms'], f['c2_e0'], f['c2_disp'], sc2['text']))
    sl2 = seat('%s_lambda2.txt' % ACT, '**lambda_2 > 0 COMPILED')
    keys['L2'] = ('KERNEL -- lambda_2: > 0 with the standard three, %s, run %s. SOURCE %s.' % (f['l2_clause'], f['l2_run'], sl2['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.9.0 ((R339)(2)), by its controls
    sw = seat('%s_standing_v190.txt' % ACT, '**v1.9.0: CONTROLS ')   # ### appended by the template after this section
    keys['V190'] = ('CERTIFIED -- tools/standing/ v1.9.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v190_ctl'], f['v190_cases'], f['v190_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the three, each read from its foot
    so = seat('%s_onset_score.txt' % ACT, '**H-ONSET-C ')
    keys['ONS'] = ('REGISTERED -- H-ONSET-C: %s, fitted on five, tested on two. SOURCE %s.' % (f['on_verdict'], so['text']))
    sv = seat('%s_detection.txt' % ACT, '**SupportDetection STATED')
    keys['DET'] = ('REGISTERED -- THE DETECTION STATEMENT: graded %s, not compiled, no proof, priced in %s lemmas. SOURCE %s.' % (f['det_grade'], f['det_lemmas'], sv['text']))
    sm = seat('%s_count_price.txt' % ACT, '**THE COUNT LAW PRICED')
    keys['CNT'] = ('REGISTERED -- THE COUNT PRICE: %s lemmas, %s absent, for the count; the count alone does not move the instance. SOURCE %s.' % (f['cnt_lemmas'], f['cnt_absent'], sm['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R339)(10))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['C2', 'L2']), ('CERTIFIED', ['V190']), ('REGISTERED', ['ONS', 'DET', 'CNT']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b729 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
