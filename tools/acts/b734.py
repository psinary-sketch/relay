# -*- coding: utf-8 -*-
# b734 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R344)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R344)(2) repair it carries. Edited by the Edit tool. Carried at b734 by tools/b734_fold.py (`carry`) from tools/acts/b733.py,
# b733`s names substituted; the citation`s sections adopted from tools/b734_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b733`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b733`s carried till
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
# ### b734, Component 1 (the Edit tool): THE c1 ROUTE FOR b733'S WEIGHT LINE AND ITS CORRIGENDUM, (R344)(1)-(2). Carried from b733's
# ### override and rewritten here against b733's own banks: the closing's lines by needle, the events (11), the defects (30), the refusals
# ### (15), the v1.13.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = 'a8a702dd'          # ### b733's closing commit
C1_REFUSAL_AT = 'a8a702dd'          # ### its refusal bank read at its closing commit
C1_NOTED = '2026-11-02'
C1_CORRIGENDA_LAST = 52
C1_V170 = 'b734_standing_v1130.txt'
C1_WEIGHT_HEAD = '*Appended 2026-11-02 by b734 to b733’s entry (:%d), under `(R344)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## Phase 2’s doors graded: 24 kernels'
C1_TRAIL_NEEDLE = '### b733 — lane two, act one hundred and fifty-nine, the Phase 2 doors act under (R343)'
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
    for l in _c1_rd('b733_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b733_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b733_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b733_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b733_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b733_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b733_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    sc = json.load(open(os.path.join(D, 'b733_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if len(held) != 8:
        sys.exit('### data/b733_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    ar = json.load(open(os.path.join(D, 'b733_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b733_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 12)) or len(dr) != 30:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b733 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b733_closing.txt):* “%s” (data/b733_closing.txt :1, the public relay at %s); its '
            'relay commit the record’s %s, the closing’s %s (data/b733_steps.json, the record and closing rows). As its rows read: Phase 2’s doors graded, 24 kernels, 6 deposits, 6 synthesis heads, 1816 sentences, EXCEEDS 472, LOAD-BEARING 59, SILENT 413 (data/b733_phase2_doors.txt :2649); '
            '52 drafts in 111 items listed and applied nowhere (data/b733_phase2_frontdoors.txt :832); the A0 premise restated on zq-b730 at 1b34964a, run 41337967613, the standard three, no sorry, zq_count’s conclusion moved by the author’s word (data/b733_a0_restatement.txt :23); '
            'the Beurling row “no instance found” in the sources read, two sources not read. '
            'The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both (:%d, :%d); the counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d), the ruling’s CLAIM 5, CLOSE 25, REPEAT 14 of 30 the defects bank’s alone. '
            'The root %s over %s banks, chained from %s (data/b733_act_root.json; :%d), the chain AGREE b624-b733; scores 8 of 8 HELD; %s questions banked as put by the seat (:%d), in two calls; %d events in data/b733_events.txt, rows (1)-(%d); %d defects, (a)–(d’) '
            '(data/b733_defects.txt). '
            'ROW (4) OF THE ROOT, corrected by `(R344)`(1): the navigator’s “four” was the net of seven kernels in the rule alone and three in the navigator’s list alone; the two sets as events row (9) prints them govern, and the navigator’s list stands as a miss of seven and an excess of three. '
            'Nothing deposited, no draft published; the corrigendum for these rows follows, under `(R344)`(1)-(2).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_PREV_CLOSE, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post,
                cc, cd, rp, rn, l_cn, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b733's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '18:12:28Z', 'defect (b)'), (2, 'READ', '18:12:29Z', 'defect (b)'), (3, 'PIPE', '18:25:35Z', 'defect (i)'), (4, 'READ', '18:32:18Z', 'defect (j)')] + [
    (k_, 'READ', '18:47:38Z', 'defect (o)') for k_ in range(5, 11)] + [(11, 'READ', '19:06:57Z', 'defect (w)'), (12, 'READ', '19:24:53Z', "defect (b')"), (13, 'PIPE', '19:28:31Z', "defect (b')"), (14, 'REDIR', '19:31:22Z', "defect (b')"), (15, 'READ', '20:34:05Z', 'event (5)')]
C1_CORR_TITLE = ('## Corrigendum to b733’s record (relay data/b733_events.txt rows (1)-(11) and data/b733_defects.txt): eleven events and thirty defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT; the pre-lock failing-list comparison at its head; free_mb in every dispatch-row kind, the delete arm’s needle read from the ferry, the 2C note’s words amended, the ORCID the scan’s third target, the post-seal rule read by the hook, the kept branch held out of the carry, '
                 'at tools/standing/ v1.13.0, each controlled, under (R344)(1)-(2)')


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
    rl = _c1_git('show', '%s:data/b733_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b733_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.13.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=[])
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(11)', sorted(ev) == list(range(1, 12))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 30', len(dr) == 30), ('the refusals 15, each answered as listed', len(rl) == 15 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.13.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
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


# ### the repairs each event is met by at v1.13.0
C1_EV_EXTRA = {1: '; repair (rows): the one writer refuses the row before it is written', 2: '; repairs (needle) and (carry)', 3: '; repair (prelock): the comparison prints before the lock gate and holds it', 4: '; the refusal did its work; `--prev` in all seven parts carried',
               5: '; nothing ran', 6: '; no arm dead; read again at the pre-push suite', 7: '; acted on as checked', 8: '; the word reader carried with BEGIN first',
               9: '; (R344)(1): the two sets as this row prints them govern, the navigator’s list a miss of seven and an excess of three', 10: '; the order add, scan, commit kept at this act’s commits', 11: '; repair (postseal): the hook refuses the command before it runs; the arm stood failing as it read'}
C1_DF_EXTRA = {'c': '; repair (carry)', 'p': '; repair (orcid): the hole named here closed at b734’s step zero'}
C1_CLASSES = (
    ('prelock', 'the pre-lock failing-list comparison (`(R344)`(2)(i), event (3))', 'standing.prelock reads the act’s probes against the previous act’s pre-run lists by arm name, a ruling’s own arm the same arm across acts; every arm newly failing prints by name in the registration gate, the gate NOT CLEAR while one is not on the face, the seal refusing where the bank is absent or not clear. On b733’s lists against b731’s: G-DELETES-ONE-BRANCH and G-RUNNER-GATE, the two the ruling names, and G-ARMS-PRERUN, which waits on the combine and is a pending arm a face names'),
    ('rows', 'every dispatch-row kind carries free_mb from the read before it (`(R344)`(2)(ii), event (1))', 'standing.dispatchrows is the one writer of the rows and refuses a row with no read or under the hold, before it writes. b733’s file is refused at its commit, push and dispatch rows; the same rows with b733’s own read, 4314 MB at 18:41:53Z, pass'),
    ('needle', 'the G-DELETES-ONE-BRANCH needle read from the act’s ferry (`(R344)`(2)(iii), event (2))', 'standing.allow.kept_clause reads the clause from the ferry; the override types no string. b733’s hand needle named zq-b731 where its ferry wrote zq-b730, and b734’s carried it to zq-b732; the route reads zq-b730 from both'),
    ('note', 'the 2C note’s words amended as the author’s row (6) ruled (`(R344)`(2)(iv))', 'relay data/b734_2c_note.txt, the one sentence moved by tool, every other byte of the draft standing and the rooted bank unedited: the five fields instancing two kinds and the C2 certificates the third. The figures stay b733’s, and the note stays applied nowhere'),
    ('orcid', 'the scan’s third target held in memory (`(R344)`(2)(v), defect (p))', 'set at step zero in tools/b734_address_scan.py: read at run time, counted, never printed, excepted in a paper’s byline under I-23 and nowhere else; the control a string in memory, the value neither printed nor written'),
    ('postseal', 'the post-seal read rule’s lists read by the hook (`(R344)`(2)(vi), event (11))', 'standing.hook reads the ledger names, the shell filter and the exclude list from tools/rule_arms.py at the call, the arm’s own text, and refuses the command the arm would count once the seal is recorded. b733’s two commands, judged on replay and not run, are refused; a name added to the arm’s file alone, in a scratch copy, is refused with no hook edit'),
    ('carry', 'the runs-of-three row b730 (m), b731 (b), b733 (c) as its class, the shift of a kept branch (`(R344)`(2)(vii))', 'standing.carry.substitute holds a kept branch’s name out of the act names’ shift, the act’s carry tool going through it; the act’s banks and push branches still shift. b734’s own carry ran before this repair and shifted the name a fourth time, in the act module: set back by the same commit that reads the needle from the ferry'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b733’s events bank (relay data/b733_events.txt) carries eleven rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank thirty lettered rows, (a)-(d’), each tagged in its own bracket (%s); its refusal bank fifteen lines at %s, '
         'each recorded by a row. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R344)`(2), at tools/standing/ v1.13.0, each with a control on b733’s banks, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v170_line('### (%s) ' % k_)), '']
    L += ['**b733’s events (1)-(11):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?(\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?|post-push|pre-push and post-push): ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b733_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b733’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b733_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), C1_DF_EXTRA.get(x, ''))]
    L += ['', '**b733’s refusals** (relay data/b733_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (eleven events, thirty defects), as b733’s closing prints it (relay data/b733_closing.txt :5), the ruling’s CLAIM 5, CLOSE 25, REPEAT 14 of 30 the defects bank’s alone; REPEAT %d of %d; the CLAIM items %s.' % (
              nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b734 on the author’s ruling `(R344)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b734.py) from '
          'b733’s events and defects banks read unedited, its refusal bank, and the v1.13.0 controls bank; banked as relay `data/b734_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b733’s record; no sealed tool, face, trail or root-named bank of b733 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b734 -- THE CORRIGENDUM FOR b733, (R344)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b733_events.txt rows (1)-(11), data/b733_defects.txt 30 rows, data/b733_hook_refusals.txt 15 '
             'lines at %s; data/%s (the v1.13.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 11, DEFECTS 30 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.13.0: THE PRE-LOCK COMPARISON, free_mb IN EVERY ROW KIND, THE NEEDLE FROM THE FERRY, THE 2C NOTE, '
               'THE ORCID, THE POST-SEAL RULE IN THE HOOK, THE KEPT BRANCH IN THE CARRY ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b733 at its weight after its entry, and the corrigendum for b733, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.13.0', bank='data/' + C1_V170),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b734, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b734 ran three
# ### ((R344)(4)(iii)-(iv), N1), rowed in data/b734_dispatch_rows.json. Replaced for b734 alone; the arms' names stand, their plants on b734's rows.
#⟪OVERRIDE checks 1129 1141⟫
def rebuild_wf_ok(S):
    """(R343)(7), as b733 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R344), N1, b734: the dispatches of (R344)(3)-(4) -- at most twelve, all on zq-b730; every dispatch read by its run id; the rows' runs the worklist's."""
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
# ### b734, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R344)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks 1521 1521⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks 1664 1664⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, edited this act by v1.13.0`s commit alone (its blob at 0f47615d the same), (R344)(2)(vi); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b734, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b733's record has twelve
#⟪OVERRIDE checks 983 983⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 12)) \
#⟪END⟫
# ### b734, Component 4 (the Edit tool): b734's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b733's override of checks 526 -- no registration commit -- removed: b734
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 754 754⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b734_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b734, Component 6 (the Edit tool): b734's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b733's wording
#⟪OVERRIDE checks 779 779⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b734, Component 4 (the Edit tool): b733's overrides of checks 1516 and 1659 (hook.py edited by b733's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b734 as it stands
# ### b734, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 988 988⟫
        and 'data/b734_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b734, Component 4 (the Edit tool): b733's override of checks 1476-1482 (one ERRATA entry at b733's (R343)(5)) removed -- (R344)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b734 as it stands
# ### b734, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b733's step-zero wording; b734's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 744 744⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks 745 745⟫
        and 'port-b707' in z and 'KEPT as banked: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b734, Component 4 (the Edit tool): G-RUNNER-READ's plant on b734's dispatch rows -- run 2's axiom lines carrying sorryAx (b733's
# ### plant read the lv rows' closure log, which b734 does not write)
#⟪OVERRIDE checks 1691 1691⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b734, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b734, Component 6 (the Edit tool): the fold bank was b733's own route
# ### (tools/b733_fold.py); b734's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b734_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1008 1008 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b733.py -> tools/acts/b734.py' in (rd('b734_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b734, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks 1011 1011 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b734_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b734, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b734_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 259 266 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b734_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b734, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R344): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 340 341⟫
    rows = [l for n_ in ('b734_defects.txt', 'b734_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R344) Component 5, the act`s events and defects together; relay data/b734_defects.txt, data/b734_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b734, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b734's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 395 396⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-ZQ-DERIVES, annotated at b734, four of its five fields closed,',
    '        explicitFormula open, and W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b734, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b733's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b734_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b734_registration_%s.txt' % __import__('b734_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b734, Component 4 (the Edit tool, before the face): b733's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b734, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b734's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b734, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R344)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b734 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|tools/b734_count\.py dispatch\b', re.M)
#⟪END⟫
# ### b734, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b733's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b734 scorer reads; the needles set to the banks b734's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 906 907 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_count_plan.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b734, (R344)(2)(iii): G-DELETES-ONE-BRANCH reads the kept clause from the act's ferry through standing.allow.kept_clause, no string typed here; the ruling writes "kept: ..., and the rest as banked." naming port-b707 nowhere
# ### (data/b734_ferry.txt :17), so the arm failed on the act's real deletes; read as written, port-b707 still out of the deletes (defect (u))
#⟪OVERRIDE checks 767 770 REPAIR (needle)⟫
    # ### (R343)(9) wrote "port-b707 kept;" and (R344)(4) writes a kept clause; allow.py's NOT-deleted reader takes neither; each read as written, the clause by kept_clause
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or bool(STW.kept_clause(S['ferry']))) \
#⟪END⟫
# ### b734, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b734_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in tuple('abcdefghijklmnopqr')))   # ### (a)-(r), entered before the lock, every one the seat's (data/b734_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b734_corrigendum.txt', 'data/b734_standing_v1130.txt', 'data/b734_count_plan.txt', 'data/b734_count.txt', 'data/b734_2c_note.txt', 'data/b734_dispatch_rows.json',
                  'data/b734_reproduce.txt', 'data/b734_reproduce.json', 'data/b734_address_scan.txt', 'data/b734_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b734 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R344)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b734_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R344)(2)-(3) (b734's keys over b734's objects): the order by time and ancestry; v1.13.0's controls; the plan, the count bank, the 2C note and the dispatch rows;
        # ### the branches; v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the plan at its commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1130', K.STANDING_COMMIT, K.C1_STANDING), ('standing_corr', K.C1_STANDING, K.C1_CORR), ('corr_plan', K.C1_CORR, K.REG_COMMIT), ('plan_count', K.REG_COMMIT, K.COUNT_BANK))),
        v1130=rd('b734_standing_v1130.txt'), plan=rd('b734_count_plan.txt'), count=rd('b734_count.txt'), note=rd('b734_2c_note.txt'),
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_ENTERING, K.ZQ_TIP).split(),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b734_dispatch_rows.json') or '[]'), reproduce=rd('b734_reproduce.txt'), reproducej=jl('b734_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b734_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows; the wave 1 kernels' rebuild-b721 branches as b733 left them
        rebuild=None, rebuild_rows=json.loads(rd('b734_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               plan=_ct(ROOT, K.REG_COMMIT), lean=_ct(EF, K.ZQ_FIRST), count=_ct(ROOT, K.COUNT_BANK),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), c2=files_of(ROOT, K.COUNT_BANK),
                   count=files_of(ROOT, K.COUNT_BANK), v9=files_of(ROOT, K.STANDING_COMMIT),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b734's read-first bank's items by path, as its step zero wrote them (data/b734_readfirst.txt :9-:22)
READFIRST_NEEDLES = ('relay data/b733_closing.txt |', 'relay data/b733_events.txt |', 'relay data/b733_defects.txt |', 'relay data/b733_a0_restatement.txt |', 'relay data/b731_price_measured.txt |', 'relay data/b729_count_price.txt |',
                     'relay data/b685_count_plan.txt |', 'SIDE-explicit-formula Schema/EpsteinZQ.lean |', 'SIDE-explicit-formula Schema/Config.lean |', 'SIDE-explicit-formula Zeta23/RvM/LocalCount.lean |',
                     'SIDE-explicit-formula Zeta23/RvM/ZetaGrowth.lean |', 'SIDE-explicit-formula Chi/LocalCount.lean |', 'SIDE-explicit-formula Schema/Wide/Config.lean |', 'SIDE-explicit-formula Schema/ZQ/Bound.lean |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R344)(1)-(2))', 'count FIELD ((R344)(3))', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (87 = 87 + 0, data/b734_citation_check.txt); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 87 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b733's figures, read at FINDINGS :12571 as Component 1 landed them
    return landed(S, 0, ['b733 AT ITS WEIGHT', 'suite 112 of 116', 'relay c7737a81', '30 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b734's title in the ferry's Component 3 form (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-ZQ-DERIVES: the count field CLOSED with the standard three, ', ' of five fields closed; C3 and C4 compiled; ', 'the pre-lock comparison and ', ' repairs landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R344)(1)-(2): the generated entry for b733's eleven events and thirty defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(11), the defects by the one lettering, no dated note; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 7, CLOSE 34 over 41, REPEAT 19); the repairs at tools/standing/ v1.13.0 by their controls
    bank; the corrigenda bank appended at row (53) and nothing before it changed; in Component 1's commits (the figures read from
    data/b734_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 30 and len(items) == j.get('items') == 41 and j.get('row') == 53 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 41 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 7 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 19 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.13.0' and (j.get('repairs') or {}).get('bank') == 'data/b734_standing_v1130.txt' \
        and len(j.get('notes') or []) == 0 \
        and '  (53) ' in S['corrigenda'] and '  (54) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b734_rules.txt and data/b734_rules.txt, by form in (R344)(4)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b733's form, its names b734's); no author's word of b734 orders a rules row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b734_rules.txt')) and not os.path.exists(os.path.join(D, 'b734_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b734's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- THE count FIELD', 'CERTIFIED -- tools/standing/ v1.13.0', 'REGISTERED -- THE PLAN',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b734: the dispatches of (R344)(3) -- each dispatch command of the capture a row of the bank, the rows' count the worklist's and within the cap, every
    row's free memory at or above the hold, each push before its dispatch and each dispatch before its read; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('push', 'dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by sha and by run id
    order = all(any(p.get('kind') == 'push' and p.get('sha') == d.get('sha') and seq_.index(p) < seq_.index(d) for p in seq_)
                and any(r.get('kind') == 'read' and str(r.get('run')) == str(d.get('run')) and seq_.index(r) > seq_.index(d) for r in seq_) for d in seq_ if d.get('kind') == 'dispatch') and bool(seq_)
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|tools/b734_count\.py dispatch\b', re.M)
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
# ### b734's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The order of the act**', '**The route**', '**The count field**', '**The price**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b734_corrigendum.txt', 'data/b734_standing_v1130.txt', 'data/b734_count_plan.txt', 'data/b734_count.txt', 'data/b734_dispatch_rows.json',
                 'data/b734_reproduce.txt', 'data/b734_address_scan.txt', 'data/b734_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b734: no row of the defects bank the navigator's, every row the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R344)(2)-(3), N2 (the name the frozen run list carries): v1.13.0's commit first, then the corrigendum's, the plan bank's, the first Lean commit and the count bank's, in that order by time and by ancestry within the relay;
    the plan at HEAD its text at its commit; the earlier acts' registrations at HEAD their blobs."""
    reg, head = S['reg_now']
    t_ = S['t']
    keys_ = ('standing', 'corr', 'plan', 'lean', 'count')
    return K.REGISTRATIONS in S['files']['reg'] and bool(reg) and reg == head \
        and all(bool(t_.get(k_)) for k_ in keys_) and [t_[k_] for k_ in keys_] == sorted(t_[k_] for k_ in keys_) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b734_address_scan.py run live over every commit of the act (relay, PLACE-papers and
    SIDE-explicit-formula's zq-b730; fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its six controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 6 OF 6 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R344)(3), N2 (the name the frozen run list carries): the plan bank with C3 and C4 in full committed before any Lean file, by the bank's own row and by the commits' times; v1.13.0 and the corrigendum before it, (2) whole before (3)."""
    return '## C3 IN FULL' in (S['plan'] or '') and '## C4 IN FULL' in (S['plan'] or '') and K.REGISTRATIONS in S['files']['reg'] \
        and 'plan before Lean: True' in (S['count'] or '') and S['t']['plan'] < S['t']['lean'] \
        and S['anc'].get('corr_plan') is True
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R344)(3), N1, N3 (the name the frozen run list carries): the last read a kernel build of the tip with no sorryAx, the count bank's foot its run and the field's axioms the standard three; the grade printing at the bank's end with four of five fields and the instance not deriving."""
    rows = S['drows'] or []
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    if not disp or not reads:
        return False
    last = reads[-1]
    return len(disp) == len(reads) <= K.MAX_DISPATCHES and str(last.get('build_exit')) == '0' and last.get('built_ref') == K.ZQ_TIP and not any(r.get('sorryAx') for r in reads) \
        and ('zq_count_holds, RUN %s, BUILD EXIT 0, NO sorryAx, AXIOMS propext, Classical.choice, Quot.sound' % last['run']) in _vlast(S['count']) \
        and 'FOUR OF FIVE FIELDS ; THE INSTANCE NOT DERIVES' in _vlast(S['count'])
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5 (the name the frozen run list carries): SIDE-explicit-formula's main at its base and the four branches each at the worklist's tip locally and at origin; no kernel's main moved (G-MERGES-ON-GATE's read); the act's Lean commits on
    zq-b730 alone, the branch's diff against its entering tip the two modules and the print list and nothing else."""
    tp = S['ef_tips'] or {}
    return S['ef_main'] == K.EF_MAIN and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and sorted(S['zq_files'] or []) == ['SIDEExplicitFormula/Schema/ZQ/Count.lean', 'SIDEExplicitFormula/Schema/ZQ/Growth.lean', 'print_targets.txt']

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.13.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.13.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b733's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R344)(2)(iv), (3), N3 (the name the frozen run list carries): the plan's seven rows, each with its neighbour and price, the envelope re-read, its foot; the count bank's seven rows, C4 the compiled theorem and C5 absorbed; the 2C note amended as the author's row (6) ruled."""
    p, c = S['plan'] or '', S['count'] or ''
    return all(('  %s  ' % n) in p and ('  %s | ' % n) in c for n in ('C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7')) and 'THE ENVELOPE ' in p \
        and 'THE PLAN: SEVEN ROWS, C4 TAKEN AS COMPILED, C5 ABSORBED, FIVE TO BUILD ; C3 AND C4 IN FULL ; THREE GROUPS ; AT MOST FOURTEEN DISPATCHES ; NOTHING BUILT' in _vlast(p) \
        and 'C4 | zq_three_halves_tsum_lt | TAKEN AS COMPILED' in c and 'C5 | (no declaration) | ABSORBED' in c and bool(S['note'])


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
    """standing clauses v9 (Component 7 of (R344): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b734_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b733's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R344-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b733's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R344) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b733's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R343)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from 0650a188',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 87 = 87 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b733-\w+) \([0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 3 form: W-ORD-ZQ-DERIVES, the count field, the fields closed, C3 and C4, the pre-lock comparison and the repairs',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R344)(1)-(2): the generated corrigendum for b733`s record, landed at FINDINGS :12573: its eleven events and thirty defects, 41 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 7 CLOSE 34, REPEAT 19; v1.13.0`s repairs by data/b734_standing_v1130.txt; the corrigenda bank appended at row (53)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b734 and no b734 rules bank: no author`s word of b734 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b734's objects
    ('G-REGISTRATIONS-FIRST', '(R344)(2)-(3), N2: v1.13.0`s commit, the corrigendum`s, the plan bank`s, the first Lean commit and the count bank`s in that order by time and ancestry; the plan at HEAD its text at 00a0f586; the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_plan=False))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b734_address_scan.py run live over every commit of the act in the relay, PLACE-papers and zq-b730, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, six controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R344)(3), N2: the plan bank with C3 and C4 in full committed before any Lean file, by the bank`s row and the commits` times; (2) whole before (3)',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'count', (S['count'] or '').replace('plan before Lean: True', 'plan before Lean: False'))),
    ('G-DERIVATION-GRADED', '(R344)(3), N1, N3: the last read a kernel build of the tip, no sorryAx in any read, the count bank`s foot its run at the standard three, four of five fields, the instance not deriving',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'drows', lambda d: [r.update(sorryAx=True) for r in d if r.get('kind') == 'read'])),
    ('G-OFFSET-POST-HOC', 'N5: SIDE-explicit-formula`s main at its base, the four branches each at the worklist`s tip locally and at origin; zq-b730`s diff against its entering tip the two modules Growth and Count and the print list alone',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at a8a702dd, VERSION 9; v8 at HEAD its blob at a8a702dd; no v10; v9`s commit an ancestor of v1.13.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R344)(2)(iv), (3), N3: the plan`s seven rows with the envelope re-read, its foot; the count bank`s seven rows, C4 the compiled theorem, C5 absorbed; the 2C note',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'plan', (S['plan'] or '').replace('AT MOST FOURTEEN DISPATCHES', 'NO CAP'))),
    ('G-DIFFERS-ERRATA', '(R344): no ERRATA entry ordered; ERRATA.md byte-equal to its blob at the act`s base, no id; no DIFFERS entry; the weight line and the corrigendum in 7d52bdd, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b734_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R344-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b733`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at a8a702dd (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: the dispatches of (R344)(3), at most fourteen, each read by its run id; the rows` runs the worklist`s',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: each dispatch command of the capture a row, the count within the cap of fourteen, the push before its dispatch before its read, the rows` free memory at the hold; no b721-b733 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b733 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved, its main at b733`s [41] tip; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (the ledgers alone); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b733`s trail record on OPEN_TRAILS (:17085) and its root in the chain', lambda S: '### b733 — lane two, act one hundred and fifty-nine, the Phase 2 doors act under (R343)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (the ledgers alone): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b733`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: at most fourteen; -1 the command bank not yet written)' % (
#⟪END⟫
# ### b734, Component 3 (the Edit tool): the sitting moved seven kernels' mains by (R344)(3): a main at its sitting tip, its tags unmoved, is not a move against b733's face
#⟪OVERRIDE record 2554 2554⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b734: (R344)'s rows. (1)'s line quoted by the ruling from the public relay at 05d53af9
    pub = _blob('D:/relay', '05d53af9', 'data/b733_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b733_closing.txt :1, the head line as the public relay carries it at 05d53af9', bool(pub) and pub[0] == at(cl, 1) and 'relay da240250' in pub[0] and 'PLACE-papers 0cfc7d1' in pub[0],
        'remote main %s' % rm[:8], '1')
    for w_ in ('suite 115 of 116', 'root ca38c6f2de07dcaf', '2 prompts answered', 'scores 6 of 8 HELD', '18 defects'):
        add('ruling (1)', 'data/b733_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'the counter CLAIM 4, CLOSE 25, REPEAT 17 OF 29, data/b733_closing.txt :5', 'CLAIM 4, CLOSE 25, REPEAT 17 OF 29' in at(cl, 5), at(cl, 5)[-40:], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    ar8_ = [x for x in ar_ if x[:1] == ['b733']]
    add('ruling (1)', 'data/act_roots.txt, b733`s root ca38c6f2 chained from b732`s 339e8eed', len(ar8_) == 1 and ar8_[0][1].startswith('ca38c6f2') and ar8_[0][2].startswith('339e8eed'), ' '.join(x_[:8] for x_ in (ar8_[0] if ar8_ else [])), '1')
    b3_ = rd(p('data', 'b733_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the chain AGREE b624-b733 (b733`s post-push part b3)', 'b733 AGREE' in b3_ and 'DISAGREE' not in b3_, 'b733 AGREE' if 'b733 AGREE' in b3_ else 'ABSENT', '1')
    ct_ = lines_of(p('data', 'b733_count.txt'))
    for w_ in ('RUN 41374814817', 'NO sorryAx', '5 OF 14 DISPATCHES', '883 LINES', 'FOUR OF FIVE FIELDS', 'THE INSTANCE NOT DERIVES'):
        add('ruling (1)', 'data/b733_count.txt :58 carries %s' % w_, w_ in at(ct_, 58), at(ct_, 58)[:60], '1')
    ev_ = rd(p('data', 'b733_events.txt')) or ''
    add('ruling (2)(iv)', 'data/b733_events.txt row (3), "THE FACE IS NOT LOCKED"', '(3) THE SEAT' in ev_ and 'THE FACE IS NOT LOCKED' in ev_, 'read', '1')
    add('ruling (2)(i)', 'data/b733_events.txt row (11), seventeen probe banks', '(11) THE SEAT' in ev_ and 'seventeen of them stood tracked at the lock commit' in ev_, 'read', '1')
    add('ruling (2)(iii)', 'data/b733_events.txt row (10), GIT_WRITE on a path', '(10) THE SEAT' in ev_ and 'GIT_WRITE matching the word in the path' in ev_, 'read', '2')
    add('ruling (2)(ix)', 'data/b733_events.txt row (9), the seventh commit 834f6ac', '(9) THE SEAT' in ev_ and '834f6ac' in ev_, 'read', '2')
    df_ = rd(p('data', 'b733_defects.txt')) or ''
    add('ruling (2)(ix)', 'data/b733_defects.txt (q) names 3471c14b', '(q)' in df_ and '3471c14b' in df_, 'read', '2')
    fe_ = lines_of(p('data', 'b733_ferry.txt'))
    add('ruling (1)', 'data/b733_ferry.txt :39, the ferry`s N5, the one-git-write clause not named', 'N5' in at(fe_, 39) and 'one git write' not in at(fe_, 39), at(fe_, 39)[:50], '1')
    add('ruling (1)', 'tools/standing/VERSION v1.13.0 entering the act', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.13.0', at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(11) and 18 defects (data/b733_events.txt, data/b733_defects.txt)',
        starts == list(range(1, 12)) and len(letters) == 18, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b733_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    cp_ = lines_of(p('data', 'b729_count_price.txt'))
    for f_ in ('b729_count_price.txt', 'b733_author_answers.txt', 'b731_price_measured.txt', 'b733_defects.txt', 'b733_count.txt', 'b733_count_plan.txt', 'b732_phase2_frontdoors.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    add('ruling (3)', 'data/b729_count_price.txt :24, the explicitFormula row, 3,000-5,000 lines, 40-80 dispatches, 12 modules, 3,742 lines', all(w_ in at(cp_, 24) for w_ in ('3,000-5,000', '40-80', '12 modules, 3,742 lines')), at(cp_, 24)[:70], '3')
    add('ruling (3)', 'data/b729_count_price.txt :21-:23, :25, the four fields` rows', '1,500-3,000' in at(cp_, 21) and '300-600' in at(cp_, 22) and '200-400' in at(cp_, 23) and '800-2,000' in at(cp_, 25), at(cp_, 25)[:70], '3')
    pm_ = lines_of(p('data', 'b731_price_measured.txt'))
    add('ruling (3)', 'data/b731_price_measured.txt :17-:19, the three measured rows, 835, 786, 340', ' 835 ' in at(pm_, 17) and ' 786 ' in at(pm_, 18) and ' 340 ' in at(pm_, 19), at(pm_, 18)[:60], '3')
    add('ruling (3)', 'data/b731_price_measured.txt :32-:36, explicitFormula re-read by the three ratios, 835-19650 lines, 4-80 dispatches', '835-19650 lines, 4-80 dispatches' in at(pm_, 36), at(pm_, 36)[:60], '3')
    EF_ = 'D:/SIDE-explicit-formula'
    ez_ = gr(EF_, 'show', '09053d3b:SIDEExplicitFormula/Schema/EpsteinZQ.lean').split(NL)
    fl_ = [at(ez_, n_).strip().split(' ')[0] for n_ in range(138, 143)]
    add('ruling (3)', 'ZQPremises has five fields, Schema/EpsteinZQ.lean :137-:142 at 09053d3b',
        at(ez_, 137).startswith('structure ZQPremises') and fl_ == ['continuation', 'zeros', 'logDeriv', 'explicitFormula', 'count'], ' '.join(fl_), '2')
    add('ruling (3)', 'Schema/EpsteinZQ.lean :141, ZQPremises.explicitFormula', 'explicitFormula : ZQExplicitFormula Z c' in at(ez_, 141), at(ez_, 141)[:50], '2')
    add('ruling (3)', 'Schema/EpsteinZQ.lean :127, ZQExplicitFormula', at(ez_, 127).startswith('structure ZQExplicitFormula'), at(ez_, 127)[:50], '2')
    mn_ = gr(EF_, 'show', '09053d3b:Zeta23/WeilEF/Main.lean').split(NL)
    add('ruling (3)', 'Zeta23/WeilEF/Main.lean :67, EF_lit_zeta, the main theorem named from the tree', at(mn_, 67).startswith('theorem EF_lit_zeta (hs : ZetaSeam)'), at(mn_, 67)[:60], '2')
    add('ruling (3)', 'Zeta23/WeilEF/Main.lean :286, EF_lit_zetaZeroConfig', at(mn_, 286).startswith('theorem EF_lit_zetaZeroConfig'), at(mn_, 286)[:60], '2')
    ef_ = gr(EF_, 'show', '09053d3b:Zeta23/ExplicitFormula.lean').split(NL)
    add('ruling (3)', 'Zeta23/ExplicitFormula.lean :80, gammaBracket, the bracket at 1/4 + iτ/2 with log π', at(ef_, 80).startswith('def gammaBracket') and '1 / 4' in at(ef_, 80) and 'Real.log π' in at(ef_, 80), at(ef_, 80)[:70], '2')
    gb_ = gr(EF_, 'show', '09053d3b:Zeta23/WeilEF/GammaRBracket.lean').split(NL)
    add('ruling (3)', 'Zeta23/WeilEF/GammaRBracket.lean :114, gammaR_bracket', at(gb_, 114).startswith('theorem gammaR_bracket'), at(gb_, 114)[:60], '2')
    gf_ = gr(EF_, 'ls-tree', '--name-only', '09053d3b', 'Zeta23/GammaFacts/').split()
    add('ruling (3)', 'Zeta23/GammaFacts/ at the pin, Mu, Series, StirlingVert', len(gf_) == 3, ' '.join(g_.split('/')[-1] for g_ in gf_), '2')
    for m_ in ('Bound', 'Continuation', 'Count', 'FEPair', 'Growth', 'Lattice', 'LogDeriv', 'Theta', 'Zeros'):
        b_ = gr(EF_, 'show', '09053d3b:SIDEExplicitFormula/Schema/ZQ/%s.lean' % m_)
        add('ruling (3)', 'SIDEExplicitFormula/Schema/ZQ/%s.lean at 09053d3b' % m_, bool(b_), '%d lines' % b_.count(NL), '2')
    wf_ = gr(EF_, 'show', '09053d3b:.github/workflows/build-module.yml')
    add('ruling (3)', '.github/workflows/build-module.yml, the closure step over the root CircuitClosure.lean', 'out/closure.jsonl' in wf_, 'closure step read', '2')
    cc_ = gr(EF_, 'show', '09053d3b:CircuitClosure.lean')
    add('ruling (3)', 'CircuitClosure.lean at 09053d3b, carried, no Lean file to write', 'collectAxioms' in cc_, '%d lines' % cc_.count(NL), '2')
    zt_ = (gr(EF_, 'rev-parse', 'zq-b730') or '').strip()
    add('ferry (read first)', 'zq-b730 at 09053d3b', zt_.startswith('09053d3b'), zt_[:8], '3')
    ml_ = gr('D:/SIDE-explicit-formula/.lake/packages/mathlib', 'rev-parse', 'HEAD')
    add('ruling (3)', 'Mathlib at de5ce8a9', ml_.startswith('de5ce8a9'), ml_[:12], '3')
    ot_ = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    add('ruling (2)', 'OPEN_TRAILS :17223, the trail`s line of what b733 carried to the next corrigendum', at(ot_, 17223).startswith('**Carried to the next corrigendum:**'), at(ot_, 17223)[:50], '0')
    fd_ = lines_of(os.path.join(PP, 'FINDINGS.md'))
    add('ferry (read first)', 'FINDINGS :6154, the neutral-name carry naming Zeta23.WeilEF.GammaRBracket', 'Zeta23.WeilEF.GammaRBracket' in at(fd_, 6154) and 'under neutral names' in at(fd_, 6154), at(fd_, 6154)[:50], '0')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (scope)', 'REGISTRY :231, PHASE 2', at(rg_, 231).startswith('## PHASE 2'), at(rg_, 231)[:40], '0')
    rl_ = (gr(PP, 'log', '-1', '--format=%h', '--', 'REGISTRY.md') or '').strip()
    add('ruling (scope)', 'REGISTRY`s own last commit 5872b89', rl_.startswith('5872b89'), rl_, '0')
    add('ruling (2)(vi)', 'the seat`s memory note on G-READ-RULE-STANDING (the ruling`s; the print at data/b733_checks_postpush_standing-c.txt :15)', 'G-READ-RULE-STANDING' in at(lines_of(p('data', 'b733_checks_postpush_standing-c.txt')), 15), 'read', '2')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula', os.path.isdir('D:/SIDE-explicit-formula/.git'), 'present', '0')
    add('ferry', 'tools/standing/ at v1.13.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.13.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R344)(4): b733's export, the mirror's last
    add('ruling (4)', 'D:/MY-DOwnloads/mirror-refresh-2026-11-02-b733.zip, b733`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R344)(4): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b733-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R344)(4): act_current alone, then b733's step row 27 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b733_steps.json'),
                   (K.STEPZERO, 'data/b733_relay_push-b733-closing_push_out.txt')):
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
    add('ferry (read first)', 'data/b734_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b734_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b734 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b733_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.13.0's controls, the count field, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R344)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R344)(6)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: on the branch zq-b730 of SIDE-explicit-formula alone, the Lean commits of (R344)(3), Schema/ZQ/Growth.lean, Schema/ZQ/Count.lean and the print list; no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b734 ((R344)(6)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R343)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b734 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND SIXTY, THE COUNT ACT: b733 AT ITS WEIGHT; THE CORRIGENDUM OPENING ON THE PRE-LOCK COMPARISON; '
              'THE count FIELD PLANNED WITH C3 AND C4 IN FULL, RE-PRICED, BUILT AND GRADED ON zq-b730, UNDER (R344).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b733's sections over b733's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.13.0: the pre-lock comparison, free_mb in every row kind, the needle from the ferry, the 2C note, the ORCID, the post-seal rule in the hook, the kept branch in the carry, each case failing before its repair and passing after', 'b734_standing_v1130.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE count FIELD ((R344)(3))', [
                ('the plan, C3 and C4 in full, committed before any Lean file', 'b734_count_plan.txt'),
                ('the seven built on zq-b730, each dispatch read by its run id, the grade', 'b734_count.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b734_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b733`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b734_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R343)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s main at badaccc and v0.37 unmoved ; on its branch zq-b730 alone the Lean commits of (R344)(3), Schema/ZQ/Growth.lean, Schema/ZQ/Count.lean and the print list, pushed through push_gated.sh, off main, untagged ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1, at most fourteen), each read by its run id, relay data/b734_dispatch_rows.json ; the rebuild-b721 branches of the wave 1 kernels as b733 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part, computation, push and dispatch ;',
    '    the push-b733-* branches of relay and PLACE-papers deleted at step zero by name, one per command and each its own message ; N2: the plan bank with C3 and C4 in full committed before any Lean file, the tools` controls before their figures, the pre-lock comparison before the lock gate ;',
    '    N3: every grade at its bank`s end, the instance not called DERIVES, the field closed with its axiom print ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b734_address_scan.txt, data/b734_address_scan_postlock.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads and the workflow dispatch under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; the deposit route untouched, publish never called, the draft held at v5 ; no README, GitHub description, Zenodo description or paper written ; no Phase 2 door written, the drafts of b733 waiting for the second sitting ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) written ; no paper cut, moved or renamed ;',
    '    no FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt (b734`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.13.0 by (R344)(2) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b733 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R344)(6)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For b734, each from its bank: the second sitting`s agenda, relay data/b733_phase2_frontdoors.txt ; for b735, the field explicitFormula, the last of five, with W-ORD-ZQ-DERIVES (OPEN_TRAILS), the count closed at relay data/b734_count.txt ; the reproduction`s NOT RUN rows, each with its price',
    '        (relay data/b734_reproduce.txt); W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b733 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file on a main, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b733`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b734: the standing repairs are v1.13.0's ((R344)(2), relay data/b734_standing_v1130.txt, read in the corrigendum section); the
    # ### carry's diffs here (b734 carried at step zero before the fold; its tools since are the templates and tools/acts/b734.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written; '
          'no Lean file on a main; the %s branches of the wave 1 kernels as b733 left them; port-b707 at b712`s tip %s)' % (
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
    b734's form over b734's objects (b733's form in git at b733's record tool): the corrigendum's foot and v1.13.0's controls; the count bank's foot;
    the citation check; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1130.txt' % ACT, r'\*\*v1\.13\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.13.0`s controls')
    ct = _bfig('%s_count.txt' % ACT, r'\*\*THE count FIELD CLOSED: zq_count_holds, RUN (\d+), BUILD EXIT (\d+), NO sorryAx, AXIOMS ([^;]+?) ; (\d+) OF (\d+) DISPATCHES ; (\d+) LINES ; C3 COMPILED, C4 THE COMPILED THEOREM ; FOUR OF FIVE FIELDS ; THE INSTANCE NOT DERIVES\.\*\*', 'the count bank`s foot')
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 6 OF 6 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], repairs=len(v5[0].split(', ')),
                ct_run=ct[0], ct_exit=ct[1], ct_axioms=ct[2], ct_d=int(ct[3]), ct_of=int(ct[4]), ct_lines=int(ct[5]),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R344)(3): the kernel rows of one kind as banked (data/b734_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R344): no lean process runs on this host; the dispatches those of (R344)(3), at most fourteen, each read by its run id. From the command bank (the seat's commands, read live from the
    capture by the `commands` route) and the dispatch rows beside the worklist's EF_RUNS."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) <= K.MAX_DISPATCHES and reads_ == sorted(str(x[1]) for x in K.EF_RUNS)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b734_commands.json): %s; dispatch commands in the capture: %s, the worklist`s runs %d, each read by its run id: %s (relay data/b734_dispatch_rows.json)' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(K.EF_RUNS), reads_))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b734's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b734_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b734_count.txt', '## THE GRADE`S CONTROLS FIRST', '## THE DISPATCHES'))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R344): the plan bank, C3 and C4 in full, before any Lean file; v1.13.0's commit, the corrigendum's, the plan bank's, the first Lean commit and the count bank's in that order by time across the repositories;
    the pre-lock comparison before the lock gate; each tool's controls before its figures."""
    chain_ = [(ROOT, K.C1_STANDING), (ROOT, K.C1_CORR), (ROOT, K.REG_COMMIT), (K.EF_DIR, K.ZQ_FIRST), (ROOT, K.COUNT_BANK)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    t = rdn('%s_count_plan.txt' % ACT)
    tz = rdn('%s_prelock.txt' % ACT)
    fg_ = rdn('%s_count.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = '## C3 IN FULL' in t and '## C4 IN FULL' in t and bool(tz) and 'plan before Lean: True' in fg_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the plan`s C3 and C4 in full: %s; the pre-lock comparison banked: %s; the count bank`s row, plan before Lean: %s; v1.13.0, the corrigendum, the plan, the first Lean commit and the count bank in that order by time: %s (%s); the tools` controls before their figures: %s' % (
            '## C3 IN FULL' in t and '## C4 IN FULL' in t, bool(tz), 'plan before Lean: True' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b734's objects; b733's in git at b733's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b734_standing_v1130.txt', ('ALL AS WANTED',)), ('b734_count_plan.txt', ('THE PLAN', 'NOTHING BUILT')), ('b734_count.txt', ('THE count FIELD', 'FOUR OF FIVE FIELDS', 'THE INSTANCE NOT DERIVES')),
             ('b734_corrigendum.txt', ('ITEMS',)), ('b734_citation_check.txt', ('CITES CHECKED',)), ('b734_reproduce.txt', ('REPRODUCES',)), ('b734_address_scan.txt', ('PREVIOUS ADDRESS',)))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R344): every grade prints at its end; the entry's counts the banks'; no sentence of the entry calls the instance DERIVES while a field is open, and the field closed stands beside its axiom print. From the banks' last
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
    bad = [s_ for s_ in sents if re.search(r'(?<![\w-])(?:DERIVES|derives)\b', s_.replace('W-ORD-ZQ-DERIVES', '')) and not re.search(r'\b(?:NOT|not|no)\b', s_.replace('W-ORD-ZQ-DERIVES', ''))]
    ok = all(o for _n, o in graded) and not bad and (not sents or any('CLOSED' in s_ and 'propext' in s_ and 'Quot.sound' in s_ for s_ in sents))
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the entry`s sentences calling the instance DERIVES, read from %s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bad or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R344) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R344)(5))
# ### (R344)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
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
    # ### (R344) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b733's form, carried) -- read from git,
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
    # ### (R344)(3), N5: every ref of every kernel carrying a commit made after the act's opening commit is SIDE-explicit-formula's zq-b730 or a branch the worklist names at its tip; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept as b733 left them; the address scan's count from its bank (relay data/b734_address_scan.txt), the suite's arm recounting it live
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
            'the address scan (relay data/b734_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s named branches, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b734 — lane two, act one hundred and sixty, the count act under (R344): b733 at its weight and its corrigendum; v1.13.0; '
            'the count field planned, built and graded on zq-b730')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 5 form; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## W-ORD-ZQ-DERIVES: the count field CLOSED with the standard three, four of five fields closed; C3 and C4 compiled; the pre-lock comparison and %d repairs landed' % (f['repairs'] - 1))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) a failing group re-dispatched alone and not with the next group, so that group A stood compiled before group B was read, at the price of one dispatch each, printed at relay data/b734_count.txt; (2) C3 fixed at c = 3/2 and the disc at centre 3/2 + (t + 1/2)i, the plan’s, where (R344)(3) leaves c to the plan; '
            '(3) C4 taken as zq_three_halves_tsum_lt, the sum form, beside the lattice form zq_three_halves_lt the ruling names, the sum being the statement C3 reads; (4) the left edge by the functional equation and Gamma’s recursion, no Stirling, Jensen on aE, so C5 absorbed and two Lean modules where the plan’s neighbours were the kernel’s four; ' +
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rd('%s_ferry.txt' % ACT)), len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b734's objects; b733's composer in git at
    b733's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R343)(2)(v)
    e = ['', _title(), '',
         'The count field of the Epstein instance is CLOSED: `zq_count_holds : ∃ A₀, Wide.HCount zqZeroConfig A₀` compiled on zq-b730 at `%s`, run %s, at axioms %s, no sorry, in %d of at most %d dispatches and %d lines. Four of the five fields of the instance stand closed; explicitFormula is open, so the instance does not derive and its grade is unchanged. The draft stands at v5, HELD.' % (
             K.ZQ_TIP[:8], f['ct_run'], f['ct_axioms'], f['ct_d'], f['ct_of'], f['ct_lines']), '',
         '*Filed at b734 on the author’s ruling `(R344)`; %d question%s put before the root. Banks: relay '
         '`data/b734_corrigendum.txt`, `data/b734_standing_v1130.txt`, `data/b734_count_plan.txt`, `data/b734_count.txt`, `data/b734_2c_note.txt`, `data/b734_dispatch_rows.json`, `data/b734_prelock.txt`, '
         '`data/b734_reproduce.txt`, `data/b734_address_scan.txt`, `data/b734_touch.txt`, `data/b734_standing_figures.txt`, `data/b734_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R344)(1)-(2), `%s`, `%s`, `%s`): b733 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b733’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b734_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b734_standing_v1130.txt), the pre-lock comparison first among them; the act module rendered from tools/b734_sections.txt by tools/standing/actmodule.py.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted']), '',
         '**The order of the act** (N2): the plan bank with C3 and C4 in full committed at `%s` before the first Lean commit `%s` (relay data/b734_count.txt prints both); the tools’ controls before their figures; the pre-lock comparison printed before the lock gate (relay data/b734_prelock.txt).' % (K.REG_COMMIT[:8], K.ZQ_FIRST[:8]), '',
         '**The route** ((R344)(3)): Jensen on the entire aE(s) = (1 - s)Z_Q(s), through the ported ZerosBound on the disc at 3/2 + (t + 1/2)i, the reflection halving the count; aE has no pole, so the disc holds at every t and the small heights’ lemma C5 is absorbed. C2 is Phragmén–Lindelöf on aE(s)/(s + 2)^3 between Re s = 3/2 and Re s = -1/2, the left edge read off the right by the functional equation and Gamma’s recursion, with no Stirling; the order in the strip comes from 1/Gamma by the reflection formula and from Lam0 bounded by its Mellin integral. C3 is |Z_Q(s)| >= 4 - Z_Q(3/2) on Re s >= 3/2, resting on the series’ first term and no Euler product; C4 is Z_Q(3/2) < 4, the compiled zq_three_halves_tsum_lt, no line of this act (relay data/b734_count_plan.txt).', '',
         '**The count field** ((R344)(3), N1, N3): %s dispatches of at most %s, each read by its run id, the rows carrying free memory; two broke, each on one proof step, and each repair was dispatched alone, so each group stood compiled before the next; the seven rows, the axiom prints and the grade at relay data/b734_count.txt, data/b734_dispatch_rows.json. The grade CLOSED rests on the build of the tip at build exit %s, no sorryAx, no sorry in the modules.' % (
             f['ct_d'], f['ct_of'], f['ct_exit']), '',
         '**The price** ((R344)(3)): the seat’s plan 515 lines and 3-8 dispatches on this route, the bank’s 800-2000 lines and 15-35 dispatches; the act %d lines and %d dispatches. One act’s figure sets no bound, and the bank’s range priced the kernel’s route, which this one did not take.' % (f['ct_lines'], f['ct_d']), '',
         '**What this act is not**: the count is an upper bound on zeros in windows of unit height and locates none. A₀ is unnamed: the theorem is existential, as the restated premise asks. No Phase 2 door is written. Nothing here proves RH or GRH; the Lean files are on the branch alone, not on main, no tag; explicitFormula stands open, the contour chain.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b734_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its six controls as wanted (relay data/b734_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b734_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b734 -- %s, %s, %s, %s -- against b733’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b734_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the growth and the lower bound read one way: Jensen counts what the size on the disc allows against the size at its centre, and the centre stands on the series’ first term, 2, against a tail below 2, so Q0’s own arithmetic carries the field where no Euler product is to be had.', '',
         '**Carried to:** %s: the second sitting on the author’s word, relay data/b733_phase2_frontdoors.txt its agenda; then b735, explicitFormula, the last of the five; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b733():
    """b733's form over b733's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b734's objects; b733's composer in git at b733's record tool): W-ORD-ZQ-DERIVES annotated by its own line, then the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD with that line beneath it."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['**`W-ORD-ZQ-DERIVES` CARRIED at b734, (R344)(3):** the count field closed with the standard three at zq-b730 `%s`, run %s, axioms %s; four of five fields closed, explicitFormula open at b735; the instance’s grade unchanged.' % (K.ZQ_TIP[:8], f['ct_run'], f['ct_axioms'])]
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-ZQ-DERIVES' not in op:
        sys.exit('### THE TRAIL: AN ANNOTATED ORDER NOT READ OPEN BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R344) ratified.** Its components as the ferry orders them (relay data/b734_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b733’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders annotated** ((R344)(3)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b734_standing_v1130.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The count field:** CLOSED, `zq_count_holds` on zq-b730 at `%s`, run %s, axioms %s, %d of at most %d dispatches, %d lines; C3 compiled, C4 the compiled theorem, C5 absorbed (relay data/b734_count_plan.txt, data/b734_count.txt).' % (
                 K.ZQ_TIP[:8], f['ct_run'], f['ct_axioms'], f['ct_d'], f['ct_of'], f['ct_lines']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b734_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b734_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b734_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b734 `%s` (previous `%s`, b733’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b734_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b734_standing_v1130.txt); the standing '
             'report tool (relay data/b734_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no main written, no tag; on SIDE-explicit-formula’s zq-b730 alone the Lean commits of (R344)(3), %d dispatches each read by its run id; the %s branches as b733 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  len(K.EF_RUNS), K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b734_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b733’s %s, %s, %s, %s (relay data/b734_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b734_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b733():
    """b733's trail record over b733's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R344)(3)`s, at most fourteen; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730, kept, zq-b730 moved by (R344)(3); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b733 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s, b733`s and this act`s; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R344)(5): relay push-b733-closing, push-b733-preroot, push-b733-record; PLACE-papers push-b733-preroot, push-b733-record; each local, by name, after --merged listed it (data/b734_stepzero.txt).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: Schema/ZQ/Growth.lean, Schema/ZQ/Count.lean and the print list alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R344) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (69eeba3) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R344)(1)-(2): FINDINGS :12573.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R344)(1)-(2): row (53).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none ordered.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-ZQ-DERIVES annotated by the trail.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b734_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.13.0`s controls, the plan, the count bank, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: the plan bank committed with its tool and the worklist at 00a0f586.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### the count bank, after the plan; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none of this act`s.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### (R344)(3): MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R344)(2): tools/standing/ to v1.13.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b734_address_scan.txt (the address never printed).'),
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
    # ### (R344)(3): the figure bank of the registered object
    fig_banks = [p for p in ('data/b734_count.txt',)
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b734_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b734_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1130', 'count_plan', 'count', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b734_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b734_registration_%s.txt -- b734, THE COUNT ACT: b733 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.13.0; THE count FIELD PLANNED, BUILT AND GRADED ON zq-b730; "
                             "NO DEPOSIT, NO TAG, UNDER (R344)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b733's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b734: b733's lines read banks this
act does not write, and are not carried; the lines are b734's: the count field (KERNEL, on the runner only), tools/standing/ v1.13.0 by its controls (CERTIFIED), the plan
(REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b734's lines, each from the record tool's figures over b734's banks
    # ------------------------------------------------------------------ KERNEL: (R344)(3), on the runner only
    sz = seat('%s_count.txt' % ACT, '**THE count FIELD CLOSED')
    sk = sz   # ### (R343)(2)(ii): the name the template appends
    keys['ZQ'] = ('KERNEL -- THE count FIELD: zq_count_holds on zq-b730 at %s, run %s, axioms %s, no sorry, %d of at most %d dispatches, %d lines; four of five fields closed, explicitFormula open, the instance`s grade unchanged. SOURCE %s.' % (K.ZQ_TIP[:8], f['ct_run'], f['ct_axioms'], f['ct_d'], f['ct_of'], f['ct_lines'], sz['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.13.0 ((R344)(2)), by its controls
    sw = seat('%s_standing_v1130.txt' % ACT, '**v1.13.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1120'] = ('CERTIFIED -- tools/standing/ v1.13.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the plan, read from its bank
    so = seat('%s_count_plan.txt' % ACT, '**THE PLAN: ')
    keys['ORD'] = ('REGISTERED -- THE PLAN: seven rows, C4 taken as compiled, C5 absorbed, C3 and C4 in full, committed before any Lean file. SOURCE %s.' % so['text'])
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R344)(5))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['ZQ']), ('CERTIFIED', ['V1120']), ('REGISTERED', ['ORD']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b734 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
