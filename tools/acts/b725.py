# -*- coding: utf-8 -*-
# b725 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R335)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R335)(2) repair it carries. Edited by the Edit tool. Carried at b725 by tools/b725_fold.py (`carry`) from tools/acts/b724.py,
# b724`s names substituted; the citation`s sections adopted from tools/b725_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b724`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b724`s carried till
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
# ### b725, Component 1 (the Edit tool): THE c1 ROUTE FOR b724'S WEIGHT LINE AND ITS CORRIGENDUM, (R335)(1)-(2). Carried from b724's
# ### override (its b723 needles shifted by the carry, class (ix)) and rewritten here against b724's own banks: the closing's lines by
# ### needle, the events (18), the defects (19), the refusals (8 at f4ab9491), the v1.5.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = 'f4ab9491'          # ### b724's closing commit (relay main at b725's step zero): its refusal bank read at it
C1_NOTED = '2026-10-30'
C1_CORRIGENDA_LAST = 44
C1_V140 = 'b725_standing_v150.txt'  # ### the name kept for the routes below: b725's controls bank is v1.5.0's
C1_WEIGHT_HEAD = '*Appended 2026-10-30 by b725 to b724’s entry (:%d), under `(R335)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## 9 of 10 repeat classes repaired with controls'
C1_TRAIL_NEEDLE = '### b724 — lane two, act one hundred and fifty-one, the second checkpoint act under (R334)'
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
    for l in _c1_rd('b724_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b724_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b724_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    q = re.search(r'^\(1\) b724 AT ITS WEIGHT\. Its closing head line, quoted from data/b724_closing\.txt :1 as the public relay carries it at '
                  r'f4ab9491: "([^"]+)"', _c1_rd('b725_ferry.txt'), re.M)
    if not q or q.group(1) != head:
        sys.exit('### data/b724_closing.txt :1 IS NOT THE HEAD LINE (R335)(1) QUOTES -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b724_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b724_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    (gi, gc, gl, gr), l_cg = _c1_fl(c, r'ITEMS (\d+): EVENTS 18, DEFECTS 39 ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;', 'the corrigendum for b723')
    (vc,), l_v = _c1_fl(c, r'v1\.4\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED \1 ; ALL AS WANTED', 'v1.4.0`s controls')
    _x, l_rw = _c1_fl(c, r"THE ROW WRITTEN IN b680'S FORM ; VERIFY OVER IT: b723 DISAGREE, ONE BANK", 'b723`s row')
    _x, l_pc = _c1_fl(c, r'THE CHOICE: \(3\) CARRIED WHOLE WITH ITS PRICE, \(2\) AND \(4\)-\(6\) RUN', 'the price table')
    _x, l_sp = _c1_fl(c, r'THE LEDGER SPLIT: CARRIED WHOLE TO b725 WITH ITS PRICE', 'the ledger split')
    (otr, odn, onm, omt, oaw, ort, okp, ors), l_or = _c1_fl(
        c, r'THE OPEN ORDERS: (\d+) TRIAGED -- DONE (\d+) ; TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) .* AUTHOR.S WORD (\d+) \(RETIRE (\d+), '
           r'KEEP (\d+), RE-SCOPE (\d+)\)', 'the orders triage')
    otl = [i for i, l in enumerate(_c1_git('show', 'HEAD:OPEN_TRAILS.md', repo=PP).replace(chr(13), '').split(NL), 1)
           for m in [re.search(r'open orders (\d+) before these lines, (\d+) after', l)] if m and m.group(1) == '82' and m.group(2) == '63']
    if len(otl) != 1:
        sys.exit('### OPEN_TRAILS: %d LINES READ "open orders 82 before these lines, 63 after", NOT ONE -- NOTHING COMPOSED' % len(otl))
    (lvc, lvr), l_lv = _c1_fl(c, r'THE lv NEGATION: not_T3_perClass_to_combinations COMPILES ON scratch-b724 \(([0-9a-f]{8})\), RUN (\d+), AXIOMS '
                                 r'\[propext, Classical\.choice, Quot\.sound\], NO sorryAx', 'the lv negation')
    l_lv43 = 43                         # ### (R335)(1) cites data/b724_lv.txt :43 for the standard three; the line read, not trusted
    if 'propext, Classical.choice, Quot.sound' not in _c1_rd('b724_lv.txt').split(NL)[l_lv43 - 1]:
        sys.exit('### data/b724_lv.txt :43 DOES NOT CARRY THE STANDARD THREE -- NOTHING COMPOSED')
    _x, l_er = _c1_fl(c, r'ERRATA E-2026-10-29-1; no main or tag touched', 'the erratum')
    _x, l_lg = _c1_fl(c, r'THE LEGACY IMPORTS: CARRIED WITH THE REMAINING PRICE \(ABOUT 1\.5-2 H\) -- 186 SOURCES SCANNED', 'the legacy imports')
    _x, l_re = _c1_fl(c, r'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4 ; PLANTED CONTROLS AS WANTED 64 OF 64 ;', 'the reproduction')
    _x, l_ad = _c1_fl(c, r'PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; PLACES 48 ; CONTROLS 4 OF 4 AS WANTED ;', 'the name and address')
    _x, l_tr = _c1_fl(c, r'entered in the trail beside its citation of touch row \(6\)', 'the touch row (6) reading')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = _c1_fl(c, r'^\s*pre-push, \(R334\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = _c1_fl(c, r'^### THE MIRROR .*mirror-refresh-2026-10-29-b724\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b724 '
                           + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    _x, l_sc = _c1_fl(c, r'^\s*\(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) REFUTED \(N5\) HELD ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the scores')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    ar = json.load(open(os.path.join(D, 'b724_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b724_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 19)) or len(dr) != 19:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b724 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b724_closing.txt):* “%s” (data/b724_closing.txt :1); its '
            'relay commit the record’s %s, the closing’s %s (data/b724_steps.json, the record and closing rows). As the closing’s rows read: '
            'the corrigendum for b723 at %s items, CLAIM %s, CLOSE %s, REPEAT %s, and v1.4.0’s %s controls AS WANTED, the repeat classes '
            'repaired with controls as data/b724_standing_v140.txt banks them (:%d, :%d); b723’s row written at act_roots :102 in b680’s form, '
            'verify over it b723 DISAGREE on one bank (:%d); the ledger split carried whole with its price, as step zero’s price table chose '
            'it (:%d, :%d); the open orders triaged, %s -- done %s, trigger not met %s, trigger met %s, %s for the author’s word (retire %s, '
            'keep %s, re-scope %s) (:%d), 82 open to 63 on the author’s word (OPEN_TRAILS :%d); the lv negation compiled on scratch-b724 '
            '(%s), run %s read by its id, its axioms the standard three (:%d; data/b724_lv.txt :%d), E-2026-10-29-1 entered (:%d); the legacy '
            'flattening carried with its price (:%d; data/b724_legacy.txt); tools/research/reproduce.py 64 REPRODUCES, 0 DIFFERS, 4 NOT RUN, '
            'the plants 64 of 64 (:%d); the name and address 0 and 0 (:%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s '
            'pre-push and %s of %s post-push, NOT CLEAN both, the claim arms %s of %s (:%d, :%d, :%d); the counter CLAIM %s, CLOSE %s, '
            'REPEAT %s of %s (:%d); N4 REFUTED, the rest HELD (:%d). The three readings, as `(R335)`(1) rules them: (i) the imprecision '
            'entered in the trail beside its citation of touch row (6) stands (:%d); (ii) event (13)’s form -- a note on an earlier act’s '
            'line written in the current act’s section, naming the line by number -- stands for every later dated note, and the notes in '
            'the corrigendum below take it; (iii) S2 HELD stands: an arm failing on an earlier act’s row alone while the act reads AGREE is '
            'not a disagreement with the act’s own score. The root %s over %s banks by the repaired route, chained from %s '
            '(data/b724_act_root.json; :%d), the chain AGREE at b724 and DISAGREE at b723 alone; the mirror (sha256 %s…) CLEAN on all three '
            'clauses with the root line (:%d); %s prompts answered (:%d); %d events in data/b724_events.txt, rows (1)-(%d); %d defects, '
            '(a)–(s) (data/b724_defects.txt). Nothing deposited, nothing published; the corrigendum for these rows follows, under '
            '`(R335)`(1)-(2).' % (
                head, K.B714_RECORD[:8], C1_PREV_CLOSE, gi, gc, gl, gr, vc, l_cg, l_v, l_rw, l_pc, l_sp, otr, odn, onm, omt, oaw, ort, okp,
                ors, l_or, otl[0], lvc, lvr, l_lv, l_lv43, l_er, l_lg, l_re, l_ad, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], ca, cb,
                l_pre, l_post, l_cl, cc, cd, rp, rn, l_cn, l_sc, l_tr, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, msha, l_mi,
                np_, l_an, len(ev), max(ev), len(dr)))


# ### the refusals: b724's bank at its closing commit, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'PIPE', '21:03:28Z', 'defect (c)'), (2, 'PIPE', '21:44:56Z', 'defect (f)'), (3, 'PIPE', '21:51:19Z', 'defect (g)'),
               (4, 'REDIR', '21:51:37Z', 'defect (h)'), (5, 'REDIR', '22:02:03Z', 'defect (m)'), (6, 'PIPE', '22:28:49Z', 'defect (n)'),
               (7, 'REDIR', '22:30:55Z', 'defect (o)'), (8, 'PIPE', '02:01:42Z', 'event (11)')]
C1_CORR_TITLE = ('## Corrigendum to b724’s record (relay data/b724_events.txt rows (1)-(18) and data/b724_defects.txt): eighteen events and '
                 'nineteen defects, each CLAIM or CLOSE and NEW or REPEAT; the three readings ruled; dated notes, in this section, naming '
                 'the lines that read wrong; and the short names, the plant needle, the legacy copy and the mirror’s citations repaired at '
                 'tools/standing/ v1.5.0, each controlled on its last banked instance, under (R335)(1)-(2)')
C1_ROSTER_FIX = ('the clause that ordered the roster read from PLACE-papers main is b715’s `(R325)`(5) (relay data/b715_ferry.txt :26); '
                 'b724’s `(R334)`(5) is its lv negation -- a citation moved by the carry’s act substitution (event (18)), repaired at v1.5.0 '
                 '(relay tools/standing/cites.py; data/b725_standing_v150.txt, :%d)')
C1_W_FIX = ('the (W) clause naming tools/mirror_prevbuild.json is b724’s `(R334)`(8) (relay data/b724_ferry.txt :23); `(R334)`(10) is '
            'another clause -- a third wrong citation in the bank, beyond the two event (18) names, caught by v1.5.0’s control (relay '
            'data/b725_standing_v150.txt, :%d)')
C1_MANIFEST_FIX = ('the clause that ordered the MANIFEST control at the build commit is b721’s `(R331)`(2)(iii) (relay data/b721_ferry.txt '
                   ':11); repaired at v1.5.0 (relay data/b725_standing_v150.txt, :%d)')
C1_NOTES = [
    ('the mirror bank, the roster’s citation', None, 'data/b724_mirror.txt', 8, '((R334)(5);', 'READS WRONG', 'roster'),
    ('the mirror bank, (W)’s citation', None, 'data/b724_mirror.txt', 8, '((R334)(10))', 'READS WRONG', 'w'),
    ('the mirror bank, the MANIFEST control’s citation', None, 'data/b724_mirror.txt', 9, '(R334)(2)(iii)`S MANIFEST CONTROL', 'READS WRONG', 'manifest'),
    ('the closing’s mirror row', None, 'data/b724_closing.txt', 105, '((R334)(5))', 'READS WRONG', 'roster'),
]


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_written(repo, path, n):
    out = _c1_git('blame', '--porcelain', '-L', '%d,%d' % (n, n), 'HEAD', '--', path, repo=repo)
    m = re.search(r'(?m)^committer-time (\d+)$', out)
    return (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(m.group(1)))) if m else None), out.split(' ', 1)[0][:8]


def _c1_v140_line(needle):
    t = _c1_rd(C1_V140).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.4.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_notes():
    lc = _c1_v140_line('### (cites) ')
    fixes = dict(roster=C1_ROSTER_FIX % lc, w=C1_W_FIX % lc, manifest=C1_MANIFEST_FIX % lc)
    out = []
    for where, repo, path, n, needle, cls, fx in C1_NOTES:
        lines = _c1_git('show', 'HEAD:' + path, repo=repo).replace(chr(13), '').split(NL)
        line = lines[n - 1] if n <= len(lines) else ''
        if line.count(needle) != 1:
            sys.exit('### %s :%d (%s) DOES NOT CARRY ITS SENTENCE ONCE (%d) -- NOTHING COMPOSED' % (path, n, where, line.count(needle)))
        at, cm = _c1_written(repo or ROOT, path, n)
        i = line.index(needle)
        a, b = max(0, i - 40), min(len(line), i + len(needle) + 100)
        quote = ('…' if a else '') + line[a:b].strip() + ('…' if b < len(line) else '')
        out.append(dict(where=where.replace('`', '’'), place=('relay ' + path) if repo is None else path, line=n, written=at, commit=cm,
                        cls=cls, quote=quote, fix=fixes[fx]))
    return out


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b724_hook_refusals.txt' % C1_PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '') if row.startswith('defect') else ev.get(int(k), '')
        if ('REFUSED BY THE HOOK (%s' % kind) not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b724_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+) ; REPEAT', 'the counter')
    v = _c1_rd(C1_V140)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.5.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=_c1_notes())
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(18)', sorted(ev) == list(range(1, 19))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 19', len(dr) == 19), ('the refusals 8, each answered as listed', len(rl) == 8 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.5.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter equal to the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl_) == (int(cc), int(cd)))) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; counter %d, %d)' % (bad, bad_ref, nc, nl_))
    s['v140_foot'] = foot[0]
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


# ### the repairs each event or defect is met by at v1.4.0 (the ten classes of (R335)(2) and the root route)
C1_EV_EXTRA = {3: '; repair (needle)', 4: '; b723’s row, (R335)(2)(i)', 9: '; repair (needle)', 10: '; repair (needle)',
               13: '; its form ruled the standing one, (R335)(1)(ii)', 18: '; repair (cites), the dated notes above'}
C1_DF_EXTRA = {}
C1_REFUSAL_LETTERS = set(row.split('(', 1)[1].rstrip(')') for _l, _k, _a, row in C1_REFUSALS if row.startswith('defect'))
C1_CLASSES = (
    ('short', 'Short branch names after a full one', 'tools/standing/allow.py reads "push-b724-preroot, -record and -closing" as three '
              'names: b724’s and b725’s five deletes, each three of five outside on v1.4.0’s reader and none on v1.5.0’s; b724’s hand-kept '
              'regex in its own module retired'),
    ('needle', 'The plant’s needle (`(R335)`(2)(ii))', 'G-DELETES-ONE-BRANCH’s plant reads the delete clause from the act’s own ferry by '
               'the branch names it must carry (allow.py delete_clause, plant_kept): the b723, b724 and b725 ferries found, each changed '
               'by the new plant and by none of the old, and a ferry with no such clause given no plant'),
    ('legacy', 'The legacy copy (`(R335)`(2)(iii))', 'tools/b644_record.py copied as tools/standing/routes/b644_record.py, its :1088 '
               'replaced by the account login, the header stating both; the copy equal to its source at 2456 of 2457 lines, no identifier '
               'in it, served by tools/standing/fold.py’s RouteLoader with the original’s __file__; legacy.py at 191 names, its remainder '
               'listed with its price (about 1.5-2 h)'),
    ('cites', 'The mirror’s citations (`(R335)`(2)(v))', 'the mirror bank’s citations read from tools/standing/cites.py’s table of '
              '(act, clause) and the current ferry’s (W) clause, the ruling token gone from record.tpl’s mbank; b724’s bank checked: the '
              'two event (18) names caught, and a third'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v140_foot'])
    L = ['*b724’s events bank (relay data/b724_events.txt) carries eighteen rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank nineteen lettered rows, (a)-(s), each tagged in its own bracket (%s); its '
         'refusal bank eight lines at b724’s closing commit %s, each recorded by a letter or an event. Each item is tagged CLAIM, where it '
         'touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the '
         'banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_PREV_CLOSE), '',
         '**The three readings, ruled** (`(R335)`(1)): (i) the imprecision entered in the trail beside its citation of touch row (6) '
         'stands; (ii) event (13)’s form stands for every later dated note -- a note on an earlier act’s line is written in the current '
         'act’s section, naming the line by number, not beneath the line; (iii) S2 HELD stands -- an arm failing on an earlier act’s row '
         'alone while the act reads AGREE is not a disagreement with the act’s own score. **Dated notes**, in (ii)’s form (no line '
         'rewritten; each line that reads wrong named here by its place and number), each dated %s:' % C1_NOTED, '']
    for x in s['notes']:
        L += ['- **%s :%d** (%s; written %s at %s; %s, noted %s): "%s" -- %s.' % (
            x['place'], x['line'], x['where'], x['written'], x['commit'], x['cls'], C1_NOTED, _c1_q(x['quote']), x['fix'])]
    L += ['', '**The repairs of `(R335)`(2)(ii), (iii) and (v), at tools/standing/ v1.5.0, each with a control replaying its last banked '
          'instance, failing on the route before the repair and passing after, both instances printed** (relay data/%s, %s cases, AS '
          'WANTED %s):' % (C1_V140, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v140_line('### (%s) ' % k_)), '']
    L += ['**b723’s row** (`(R335)`(2)(i)): the row in b680’s form stands at relay data/act_roots.txt :102 and the chain’s reader takes '
          'b723 through it (corrected 1); verify re-read reads b722 AGREE, b723 DISAGREE on one bank (data/b723_bank_hashes.json), b724 '
          'AGREE. The bytes b723’s root hashed rebuilt: the bank’s blob at 2be0135c with the two root-banks entries of 49de42fe hashes to '
          'the recorded 133004c8, and no commit carries those bytes, so no row reading a bank at a commit can turn the reading AGREE; a '
          'side-branch commit carrying them, or the reading standing, put to the author at b725’s root (relay data/b725_root_row.txt). '
          '**The three RE-SCOPE orders** (`(R335)`(2)(iv)): each source read and each given a written trigger -- W-ORD-LI-FAMILY-CONTROL '
          'and W-ORD-STRICT-BOUND kept, W-ORD-EXACT-SUPPORT kept after a draft offering it for retire was withdrawn on a search -- for '
          'the root’s prompt (relay data/b725_rescope.txt).', '',
          '**b724’s events (1)-(18):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_]).split(': ', 1)[0]
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b724_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b724’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        extra = '; a hook refusal, its line below' if x in C1_REFUSAL_LETTERS else C1_DF_EXTRA.get(x, '')
        L += ['**(%s)** (relay data/b724_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), extra)]
    L += ['', '**b724’s refusals** (relay data/b724_hook_refusals.txt at %s, one a line): ' % C1_PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (eighteen events, nineteen defects), equal to b724’s closing’s (relay '
          'data/b724_closing.txt :5); REPEAT %d of %d; the CLAIM items %s.' % (nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b725 on the author’s ruling `(R335)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 '
          'corrigendum`, the act’s override in relay tools/acts/b725.py) from b724’s events, defects and refusal banks read unedited, the '
          'lines noted read at their repositories’ HEAD, and the v1.5.0 controls bank; banked as relay `data/b725_corrigendum.txt`, the '
          'corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b724’s record; no sealed tool, face, trail or '
          'root-named bank of b724 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b725 -- THE CORRIGENDUM FOR b724, (R335)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b724_events.txt rows (1)-(18), data/b724_defects.txt 19 rows, data/b724_hook_refusals.txt 8 '
             'lines at %s; the noted lines at their repositories` HEAD; data/%s (the v1.5.0 controls); the corrigenda bank`s last row (%d).' % (
                 C1_PREV_CLOSE, C1_V140, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 18, DEFECTS 19 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.5.0: THE SHORT NAMES, THE PLANT '
               'NEEDLE, THE LEGACY COPY, THE MIRROR CITATIONS ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b724 at its weight after its entry, and the corrigendum for b724, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.5.0', bank='data/' + C1_V140),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b725, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b725 ran three
# ### ((R335)(4)(iii)-(iv), N1), rowed in data/b725_dispatch_rows.json. Replaced for b725 alone; the arms' names stand, their plants on b725's rows.
#⟪OVERRIDE checks 1126 1138⟫
def rebuild_wf_ok(S):
    """(R334)(7), as b724 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
#⟪OVERRIDE checks 1141 1156⟫
def runner_ok(S):
    """(R335)(4)(iii)-(iv), N1, b725: the three dispatches read by their run ids -- SIDE-explicit-formula's build-module.yml at main with the
    ref input, each at a commit of keiper-b725 or c2-b725 pushed with its remote equal before it, its run the worklist's EF_RUNS in order,
    each read once with the built ref its commit: run 1 (keiper-b725 9a61ba22) BUILD EXIT 1, FAILS; run 2 (f52e188c) BUILD EXIT 0, BUILDS,
    the six names at the standard three, no sorryAx; run 3 (c2-b725 52cbbc11) completed; the lambda_2 bank's foot naming run 2 and
    DISPATCHES 2 OF 3, the C2 bank's naming run 3 and DISPATCHES 3 OF 3."""
    rows = S['drows'] or []
    cm = [r for r in rows if r.get('kind') == 'commit']
    pu = [r for r in rows if r.get('kind') == 'push']
    dp = [r for r in rows if r.get('kind') == 'dispatch']
    rd_ = [r for r in rows if r.get('kind') == 'read']
    std = '[propext, Classical.choice, Quot.sound]'
    by = dict((str(r.get('run')), r) for r in rd_)
    runs = [str(r) for _i, r in K.EF_RUNS]
    ok = len(cm) == len(pu) == len(dp) == len(rd_) == len(runs) == 3 \
        and runs == [str(r.get('run')) for r in dp] == [str(r.get('run')) for r in rd_] \
        and [r.get('sha') for r in cm] == [r.get('sha') for r in pu] == [r.get('sha') for r in dp] == [r.get('built_ref') for r in rd_] \
        and cm[1].get('sha') == K.EF_BRANCHES[0][1] and cm[2].get('sha') == K.EF_BRANCHES[1][1] \
        and all(r.get('remote_equal') is True for r in pu) and all(r.get('at_ref') == 'main' and r.get('workflow') == 'build-module.yml' for r in dp) \
        and all(r.get('status') == 'completed' for r in rd_)
    r1, r2 = by.get(runs[0]) or {}, by.get(runs[1]) or {}
    return ok and str(r1.get('build_exit')) == '1' and r1.get('verdict') == 'FAILS' \
        and str(r2.get('build_exit')) == '0' and r2.get('verdict') == 'BUILDS' and r2.get('sorryAx') is False \
        and len(r2.get('axioms_lines') or []) == 6 and all(x.endswith(std) for x in r2.get('axioms_lines') or []) \
        and ('RUN %s' % runs[1]) in _verdict(S['lambda2']) and 'DISPATCHES 2 OF 3' in _verdict(S['lambda2']) \
        and ('RUN %s' % runs[2]) in _vlast(S['c2']) and 'DISPATCHES 3 OF 3' in _vlast(S['c2'])
#⟪END⟫
#⟪OVERRIDE checks 1167 1170⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        pu_ = [j for j, r in enumerate(rows) if r.get('kind') == 'push' and r.get('sha') == d_.get('sha')]
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(pu_) == 1 and len(rd_) == 1 and pu_[0] < i_ < rd_[0]
#⟪END⟫
#⟪OVERRIDE checks 1173 1173⟫
    return bool(mem) and all(int(r.get('free_mb') or 0) >= K.HOLD for r in mem) and order \
#⟪END⟫
# ### b725, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b724's record has eighteen
#⟪OVERRIDE checks 980 980⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 19)) \
#⟪END⟫
# ### b725, Component 4 (the Edit tool): b725's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b724's override of checks 526 -- no registration commit -- removed: b725
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 751 751⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b725_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b725, Component 6 (the Edit tool): b725's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b724's wording
#⟪OVERRIDE checks 776 776⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b725, Component 4 (the Edit tool): b724's overrides of checks 1516 and 1659 (hook.py edited by b724's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b725 as it stands
# ### b725, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 985 985⟫
        and 'data/b725_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b725, Component 4 (the Edit tool): b724's override of checks 1476-1482 (one ERRATA entry at b724's (R334)(5)) removed -- (R335)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b725 as it stands
# ### b725, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b724's step-zero wording; b725's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 742 742⟫
        and 'port-b707' in z and 'Kept: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b725, Component 4 (the Edit tool): G-RUNNER-READ's plant on b725's dispatch rows -- run 2's axiom lines carrying sorryAx (b724's
# ### plant read the lv rows' closure log, which b725 does not write)
#⟪OVERRIDE checks 1686 1686⟫
     lambda S: runner_ok(S), lambda S: put(S, 'drows', [dict(r, axioms_lines=[x.replace('[propext, Classical.choice, Quot.sound]', '[propext, sorryAx, Classical.choice, Quot.sound]') for x in (r.get('axioms_lines') or [])]) for r in (S['drows'] or [])])),
#⟪END⟫
# ### b725, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b725, Component 6 (the Edit tool): the fold bank was b724's own route
# ### (tools/b724_fold.py); b725's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b725_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1005 1005 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b724.py -> tools/acts/b725.py' in (rd('b725_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b725, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b725_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 256 263 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b725_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b725, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R335): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 339 340⟫
    rows = [l for n_ in ('b725_defects.txt', 'b725_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R335) Component 4, the act`s events and defects together; relay data/b725_defects.txt, data/b725_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b725, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b725's orders are (R335)(10)'s six,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: (R335)(10)`s six (W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL, W-ORD-SILENT-SENTENCES, W-ORD-SIDE-DIAGNOSTIC) entered with',
    '        the trail, none acted on; the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; beside them the three',
#⟪END⟫
# ### b725, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b724's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b725_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b725_registration_%s.txt' % __import__('b725_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b725, Component 4 (the Edit tool, before the face): b724's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b725, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b725's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's two branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b725, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R335)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b725 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b725, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b724's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b725 scorer reads; the needles set to the banks b725's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 903 904 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_FIGURE_BANKS' in n and '_first_add(' in n \
        and "_onset_mass_control.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b725, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b724's ruling's form "port-b707 kept;", where (R335)(9)
# ### writes "kept: port-b707, …" (data/b725_ferry.txt :34), so the arm failed on the act's real deletes; both forms read as written
#⟪OVERRIDE checks 764 767 REPAIR (needle)⟫
    # ### (R334)(9) wrote "port-b707 kept;" and (R335)(9) writes "kept: port-b707, …"; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or bool(re.search(r'\bkept: [^.;]*\b%s\b' % re.escape(K.PORT_BRANCH), S['ferry']))) \
#⟪END⟫
# ### b725, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b725_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxy'))   # ### (a)-(y) entered before the lock, every one the seat's (data/b725_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b725_price.txt', 'data/b725_corrigendum.txt', 'data/b725_standing_v150.txt', 'data/b725_root_row.txt',
                  'data/b725_rescope.txt', 'data/b725_registrations.txt', 'data/b725_onset_mass_control.txt', 'data/b725_onset_mass_rule.txt',
                  'data/b725_onset_mass.txt', 'data/b725_addendum.txt', 'data/b725_addendum_citation.txt', 'data/b725_interference.txt',
                  'data/b725_dial.txt', 'data/b725_stop_rule.txt', 'data/b725_lambda2.txt', 'data/b725_c2.txt', 'data/b725_dispatch_rows.json',
                  'data/b725_author_words_preseal.txt', 'data/b725_reproduce.txt', 'data/b725_reproduce.json', 'data/b725_address_scan.txt',
                  'data/b725_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b725 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R335)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b725_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R335)(2)-(4), Component 4, the Edit tool, before the lock (b724's keys over b724's objects in git at b724's suite): the
        # ### registrations committed alone (3); the components' order by ancestry; the price table, v1.5.0's controls and b723's row (2);
        # ### the computations (4) -- H-ONSET-MASS with its control and rule, H-DIAL, lambda_2 and the C2 theorem on SIDE-explicit-formula's
        # ### two branches, their three dispatches by their rows; the addendum's H-INTERFERENCE and its citation check; the stop rule; v8 and
        # ### v9; the address scan (R332)(9); the reproduction run under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### (R335)(3): the registrations at their commit and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v150', K.STANDING_COMMIT, K.C1_STANDING), ('v150_c1', K.C1_STANDING, K.C1_RELAY),
                                 ('c1_corr', K.C1_RELAY, K.C1_CORR), ('corr_c2', K.C1_CORR, K.C2_RELAY), ('c2_c3', K.C2_RELAY, K.C3_RELAY[0]))
                 + tuple(('c3_%d' % i, a, b) for i, (a, b) in enumerate(zip(K.C3_RELAY, K.C3_RELAY[1:]), 1))),
        registrations=rd('b725_registrations.txt'), price=rd('b725_price.txt'), v150=rd('b725_standing_v150.txt'),
        root_row=rd('b725_root_row.txt'), rescope=rd('b725_rescope.txt'), stop_rule=rd('b725_stop_rule.txt'),
        onset=rd('b725_onset_mass.txt'), onset_control=rd('b725_onset_mass_control.txt'), onset_rule=rd('b725_onset_mass_rule.txt'),
        dial=rd('b725_dial.txt'), interference=rd('b725_interference.txt'), addendum=rd('b725_addendum.txt'),
        addendum_cit=rd('b725_addendum_citation.txt'), lambda2=rd('b725_lambda2.txt'), c2=rd('b725_c2.txt'),
        drows=json.loads(rd('b725_dispatch_rows.json') or '[]'),
        reg_first=dict((p, gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', p).split()[-1:] or [None])
                       for p in ('data/b725_onset_mass.txt', 'data/b725_onset_mass_control.txt', 'data/b725_onset_mass_rule.txt',
                                 'data/b725_dial.txt', 'data/b725_interference.txt', 'data/b725_lambda2.txt', 'data/b725_c2.txt',
                                 'data/b725_dispatch_rows.json')),
        reproduce=rd('b725_reproduce.txt'), reproducej=jl('b725_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b725_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read THIS ACT'S three dispatches ((R335)(4)(iii)-(iv), N1): the dispatch rows (commit, push, dispatch,
        # ### read), the lambda_2 bank beside them; the wave 1 kernels' rebuild-b721 branches, main and tags as b724 left them (its axiom rows
        # ### read for the workflows there, no commit on those kernels this act)
        rebuild=rd('b725_lambda2.txt'), rebuild_rows=json.loads(rd('b725_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows: the act shift had moved this name to b724, which has no such bank (defect (y))
        ef_branches=dict((b, dict(local=gs(EF, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b),
                                  remote=gs(EF, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + b),
                                  base=gs(EF, 'merge-base', K.EF_BASE, t_),
                                  files=sorted(x for x in gs(EF, 'diff', '--name-only', K.EF_BASE, t_).split(NL) if x.strip()),
                                  on_main=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', t_, 'main']).returncode == 0,
                                  tags=[x for x in gs(EF, 'tag', '--contains', t_).split(NL) if x.strip()]))
                         for b, t_ in K.EF_BRANCHES),
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
# ### b725's read-first bank's items by path, as its step zero wrote them (Component 4, the Edit tool, before the lock: the carried needles
# ### were b724's items; data/b725_readfirst.txt :15-:36)
READFIRST_NEEDLES = ('relay data/b724_closing.txt |', 'relay data/b724_events.txt |', 'relay data/b724_defects.txt |',
                     'relay data/b724_orders_triage.txt |', 'relay data/b724_lv.txt | :43 |', 'relay data/b724_legacy.txt |',
                     'relay data/b723_registrations.txt |', 'relay data/b723_support.txt |', 'relay data/b723_zetak.txt |',
                     'relay data/b722_c2_price.txt |', 'relay data/b711_list.json |', 'relay data/b707_onset.txt |',
                     'SIDE-explicit-formula SIDEExplicitFormula/KeiperIdentities.lean |', 'SIDE-explicit-formula SIDEExplicitFormula/KeiperBounds.lean |',
                     'SIDE-explicit-formula SIDEExplicitFormula/KeiperSign.lean |', 'relay data/b725_ferry.txt |',
                     'relay data/standing_clauses_v9.txt |', 'relay tools/standing/VERSION | :1 v1.4.0 |', 'relay data/act_roots.txt |',
                     'relay data/b724_mirror.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R335)(1)-(2))', 'REGISTRATIONS ((R335)(3))', 'H-ONSET-MASS ((R335)(4)(i), (8))', 'H-DIAL ((R335)(4)(ii))',
                    'lambda_2 ((R335)(4)(iii))', 'C2 THEOREM ((R335)(4)(iv))', 'H-INTERFERENCE ((R335)(9))', 'NAME AND ADDRESS ((R332)(9))',
                    'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (72 = 72 + 0, data/b725_citation_check.txt :81); the bank
    written before the step-zero banks' commit and that commit before Component 1's (Component 4, the Edit tool: the carried 57 = 56 + 1
    were b724's own). The addendum's own check (data/b725_addendum_citation.txt, 21 cites, one MISS closed by the author's word (1)) is a
    bank of its own, not read by this arm."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 72 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 4, the Edit tool, before the lock: the carried needles were b723's figures under b724's name; these are b724's, read
    # ### at FINDINGS :11681 as Component 1 landed it)
    return landed(S, 0, ['b724 AT ITS WEIGHT', 'suite 110 of 116; root e09d0fac7d52e9e2…', 'the closing’s f4ab9491', '19 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### Component 4, before the lock, the Edit tool: b725's title in the ferry's Component 4 form adjusted to what the act did (the record
# ### tool's _title over the banks), cut at its objects; the carried needles were b724's
TITLE_NEEDLES = ('## H-ONSET-MASS at ', ' of 3 zeros ', '; H-DIAL at c = 0.6, 0.8, 1.0 REFUTED', '; H-INTERFERENCE at 69 of 69 zeros HELD',
                 '; lambda_2 > 0 compiled with the standard three on two named premises, both printed as what remains',
                 '; the C2 theorem graded DERIVES, carried where its build stopped under the runner’s hold',
                 '; b723’s row read in b680’s form, the chain DISAGREE at b723 (one bank)', '; the plant needle and the legacy copy landed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R335)(1)-(2): the generated entry for b724's eighteen events and nineteen defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(18), the defects by the one lettering ((a)-(s)), no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 4, CLOSE 33 over 37, REPEAT 25); the CLAIM items events (4) and (16) and defects (q)
    and (r); the repairs at tools/standing/ v1.5.0 by their controls bank; the mirror bank's three citations and the closing's mirror row
    READS WRONG among the dated notes; the corrigenda bank appended at row (45) and nothing before it changed; in Component 1's commits
    (Component 4, the Edit tool, before the lock: the carried figures were b724's corrigendum's, of b723's record; these read from
    data/b725_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 19 and len(items) == j.get('items') == 37 and j.get('row') == 45 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 37 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 4 and claims == ['e16', 'e4', 'q', 'r'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 25 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.5.0' and (j.get('repairs') or {}).get('bank') == 'data/b725_standing_v150.txt' \
        and sorted(n.get('where') for n in (j.get('notes') or []) if n.get('cls') == 'READS WRONG') == [
            'the closing’s mirror row', 'the mirror bank, (W)’s citation', 'the mirror bank, the MANIFEST control’s citation', 'the mirror bank, the roster’s citation'] \
        and '  (45) ' in S['corrigenda'] and '  (46) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b725_rules.txt and data/b726_rules.txt, by form in (R335)(5)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (Component 4, the Edit tool: the line above is b724's form, its names b725's); no author's word of b725 orders a rules row (its one word
    before the seal, data/b725_author_words_preseal.txt, strikes a phrase of (R335)(9) and orders runs), so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b725_rules.txt')) and not os.path.exists(os.path.join(D, 'b726_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b725's keys, the report sections' own heads (Component 6, the Edit tool, before the lock; b724's carried till then)
REPORT_KEYS = ('KERNEL -- lambda_2 ON keiper-b725', 'KERNEL -- THE C2 THEOREM ON c2-b725', 'CERTIFIED -- tools/standing/ v1.5.0',
               'REGISTERED -- H-ONSET-MASS', 'REGISTERED -- H-DIAL', 'REGISTERED -- H-INTERFERENCE', 'REGISTERED -- b723`S ROW',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over THIS ACT'S three dispatches ((R335)(4)(iii)-(iv), data/b725_dispatch_rows.json; Component 4, the Edit tool): every
    push, dispatch and read row with the host's free memory at or above the hold (each figure read as an integer); each dispatch with one
    push of its commit before it and one read of its run after it; the dispatches three, the three N1 allows, none push-triggered; the
    capture's dispatch commands (gh workflow run build-module.yml at main with the ref input) one per dispatch row, at the rows' commits;
    no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run build-module\.yml -R psinary-sketch/SIDE-explicit-formula --ref main '
                       r'-f ref=([0-9a-f]{40}) -f target=SIDEExplicitFormula\.\w+', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == len(K.EF_RUNS) == K.MAX_DISPATCHES == 3 \
        and not [r for r in rows if r.get('kind') == 'dispatch' and r.get('via')] \
        and len(cmds) == len(K.EF_RUNS) and sorted(route.search(r['cmd']).group(1) for r in cmds) == sorted(r.get('sha') for r in rows if r.get('kind') == 'dispatch') \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS and OPEN_TRAILS; (R335) orders no ERRATA, REGISTRY or archive
    write), both ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b725's headings and banks, as its _finding_text writes them (Component 6, the Edit tool, before the lock; b724's carried till then)
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**b723’s row**', '**The registrations**', '**H-ONSET-MASS**', '**H-DIAL**',
                 '**lambda_2**', '**The C2 theorem**', '**H-INTERFERENCE**', '**The research instruments reproduced**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b725_corrigendum.txt', 'data/b725_standing_v150.txt', 'data/b725_root_row.txt', 'data/b725_registrations.txt',
                 'data/b725_onset_mass.txt', 'data/b725_dial.txt', 'data/b725_lambda2.txt', 'data/b725_c2.txt', 'data/b725_dispatch_rows.json',
                 'data/b725_interference.txt', 'data/b725_reproduce.txt', 'data/b725_address_scan.txt', 'data/b725_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b725: no row of the defects bank the navigator's ((a)-(o) the seat's)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R335)(3), N2, the name the frozen run list carries (Component 4, the Edit tool, over b725's objects): the registrations committed
    alone (REG_COMMIT, its one file data/b725_registrations.txt) after Component 1 and before any figure they name -- each figure bank of a
    registered object (the onset bank, its control and rule, H-DIAL's, H-INTERFERENCE's, lambda_2's, the C2 bank, the dispatch rows)
    first added in a commit descending from it and not it, H-INTERFERENCE's after its amendment 706b4ca1 and H-DIAL's after dc0d4133; the
    amendments each descending from it and the file at HEAD its text at that commit with lines appended alone; the components committed
    in their order, each the ancestor of the next; the earlier acts' registrations at HEAD their blobs at their commits."""
    reg, head = S['reg_now']
    first = dict((p, c[0]) for p, c in S['reg_first'].items())
    after = lambda a, c: bool(c) and c != a and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, c]).returncode == 0
    return S['files']['reg'] == [K.REGISTRATIONS] and bool(reg) and bool(head) and head.startswith(reg) \
        and all(after(K.REG_COMMIT, c) for c in first.values()) and all(after(K.REG_COMMIT, c) for c in K.C2_AMEND) \
        and after('706b4ca1', first['data/b725_interference.txt']) and after('dc0d4133', first['data/b725_dial.txt']) \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R332)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 6, the Edit tool): tools/b725_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address and name read from history and held in memory -- the address 0, the author's name 0, the previous name 0, its
    four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R335)(4)(i), (8), N3 (the name the frozen run list carries; Component 4, the Edit tool, over b725's H-ONSET-MASS): the post hoc
    control and the rule banked before any onset (ONSETS COMPUTED 0 at both; the control's (C2) AS WANTED; the rule WALKED 3, SELECTED 3);
    the onset bank's foot its last line -- C1 AS WANTED, ZEROS 3, the computed, beyond-reach and not-run counts summing to 3, the
    hypothesis graded; each computed onset printed with its deviation and each zero not computed CARRIED, NOT COMPUTED ((R335)(8)) with
    its ladder reading; REFUTED exactly where a printed deviation passes 0.05."""
    o = S['onset'] or ''
    last = ((o.rstrip(NL).split(NL)) or [''])[-1]
    m = re.match(r'^### ### \*\*H-ONSET-MASS: C1 AS WANTED ; ZEROS 3 ; ONSETS COMPUTED (\d+) ; WITHIN 0\.05 (\d+) ; BEYOND REACH (\d+) ; '
                 r'NOT RUN (\d+) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*$', last)
    devs = [float(x) for x in re.findall(r'a\*/a\*_pred - 1 = ([+-]\d+\.\d+) -- (?:WITHIN|BEYOND) 0\.05', o)]
    return bool(m) and int(m.group(1)) + int(m.group(3)) + int(m.group(4)) == 3 and len(devs) == int(m.group(1)) \
        and int(m.group(2)) == sum(1 for d in devs if abs(d) <= 0.05) \
        and m.group(5) == ('REFUTED' if any(abs(d) > 0.05 for d in devs) else ('HELD' if devs else 'NOT SCORABLE')) \
        and o.count('CARRIED, NOT COMPUTED ((R335)(8))') == int(m.group(4)) \
        and 'ONSETS COMPUTED 0' in _verdict(S['onset_control']) and '(C2) AS WANTED' in _verdict(S['onset_control']) \
        and 'WALKED 3 ; SELECTED 3 ; ONSETS COMPUTED 0' in _verdict(S['onset_rule'])
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R335)(4)(iii), N1, N3, N5 (the name the frozen run list carries; Component 4, the Edit tool, over b725's lambda_2): keiper-b725 of
    SIDE-explicit-formula at its tip locally and at origin, cut from the worklist's base (main, untouched), its files against the base
    KeiperTwo.lean and print_targets.txt alone, off main and in no tag; the bank's last line naming the branch's tip, run 2, the standard
    three, no sorryAx, the two named premises and DISPATCHES 2 OF 3, NO MAIN, NO TAG; every grade printed (DERIVES 2, INTERFACES 4) and
    what remains printed as sorry-free statements."""
    b = S['ef_branches'].get('keiper-b725') or {}
    tip = K.EF_BRANCHES[0][1]
    v = _verdict(S['lambda2'])
    return b.get('local') == tip == b.get('remote') and b.get('base') == K.EF_BASE and b.get('on_main') is False and b.get('tags') == [] \
        and b.get('files') == ['SIDEExplicitFormula/KeiperTwo.lean', 'print_targets.txt'] \
        and v.startswith('lambda_2 > 0 -- NOT COMPILED OUTRIGHT') and ('ON keiper-b725 (%s, RUN %s)' % (tip[:8], K.EF_RUNS[1][1])) in v \
        and 'WITH THE STANDARD THREE, NO sorryAx, ON TWO NAMED PREMISES' in v and 'GRADES DERIVES 2, INTERFACES 4' in v \
        and v.endswith('DISPATCHES 2 OF 3 ; NO MAIN, NO TAG.') \
        and '## WHAT REMAINS, THE SORRY-FREE STATEMENTS PRINTED' in (S['lambda2'] or '') and '## THE GRADES' in (S['lambda2'] or '')
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R335)(4)(iv), N1, N3, N5 (the name the frozen run list carries; Component 4, the Edit tool, over b725's C2 theorem): the E0 grade
    printed first -- the bank's section (1), DERIVES, before its section (2), route (B) mirrored equal to the statement at 18 of 18, and both
    before section (3), the branch; c2-b725 of SIDE-explicit-formula at its tip locally and at origin, cut from the worklist's base, its
    files against the base C2Walk.lean and print_targets.txt alone, off main and in no tag; section (4), the read of run 3, after (3); the
    bank's last verdict line naming the tip, run 3, the certificates read as closed by decide +kernel out of 18, what remains, and
    DISPATCHES 3 OF 3, NO MAIN, NO TAG; where the run stopped under the hold, the count 0, the line CARRIED and the dispatch rows' read of
    run 3 STOPPED UNDER THE HOLD with exit 143 -- the bank and the rows one reading."""
    t = S['c2'] or ''
    b = S['ef_branches'].get('c2-b725') or {}
    tip = K.EF_BRANCHES[1][1]
    v = _vlast(t)
    i1, i2, i3, i4 = (t.find(x) for x in ('## (1) THE E0 GRADE', '## (2) ROUTE (B) MIRRORED', '## (3) THE BRANCH', '## (4) THE READ OF RUN %s' % K.EF_RUNS[2][1]))
    m = re.search(r'CERTIFICATES BY decide \+kernel (\d+) OF 18', v)
    rd = [r for r in (S['drows'] or []) if r.get('kind') == 'read' and r.get('run') == K.EF_RUNS[2][1]]
    held = 'STOPPED UNDER THE RUNNER\'S HOLD' in v
    return 0 <= i1 < i2 < i3 < i4 and '  THE GRADE: DERIVES -- ' in t[i1:i2] and 'EQUAL TO THE STATEMENT AND THE CERTIFICATE TRUE AT 18 OF 18' in t[i2:i3] \
        and b.get('local') == tip == b.get('remote') and b.get('base') == K.EF_BASE and b.get('on_main') is False and b.get('tags') == [] \
        and b.get('files') == ['SIDEExplicitFormula/C2Walk.lean', 'print_targets.txt'] \
        and v.startswith('THE C2 THEOREM: E0 DERIVES') and ('ON c2-b725 (%s, RUN %s)' % (tip[:8], K.EF_RUNS[2][1])) in v \
        and m is not None and 'WHAT REMAINS' in v and v.endswith('DISPATCHES 3 OF 3 ; NO MAIN, NO TAG.') and len(rd) == 1 \
        and held == (rd[0].get('verdict') == 'STOPPED UNDER THE HOLD' and rd[0].get('build_exit') == '143') \
        and (not held or (m.group(1) == '0' and 'CARRIED WITH ITS TREE STATE' in v))


def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut (the C2 bank carries two: its mirror's foot, then its
    branch's after the read; the template's _verdict reads the first)."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries (Component 4, the Edit tool, over b725's v9): standing clauses v9 binding the act whole as b723
    landed it -- the working tree's text its blob at STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's
    base; no v10 written; v9's commit an ancestor of v1.5.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v150') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED as b724
    left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since b724's v1.3.0;
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
    """(R335)(4)(ii), (8), N3, the stop rule (the name the frozen run list carries; Component 4, the Edit tool, over b725's H-DIAL): the
    dial bank's foot its last line -- (c0) and (id) AS WANTED, ONSETS 3 OF 3, the hypothesis graded; its spread over the three products
    printed against the 0.10 bound and the grade REFUTED exactly where it passes it; the stop rule's (4)(ii) row in its bank (read after
    the fact, defect (p)); the bank in the computations' commits."""
    d = S['dial'] or ''
    last = ((d.rstrip(NL).split(NL)) or [''])[-1]
    m = re.match(r'^### ### \*\*H-DIAL: \(c0\) AS WANTED ; \(id\) AS WANTED ; ONSETS 3 OF 3 ; THE HYPOTHESIS (HELD|REFUTED)\.\*\*$', last)
    sp = re.search(r'spread[^0-9]*([0-9.]+)', d, re.I)
    return bool(m) and bool(sp) and m.group(1) == ('REFUTED' if float(sp.group(1)) > 0.10 else 'HELD') \
        and '## (4)(ii) H-DIAL' in (S['stop_rule'] or '') and 'data/b725_dial.txt' in S['files']['c3']


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b724's (R334)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at the act's base (unchanged this act; Component 6, the Edit
    tool: the carried read named b724's commit of it) and the working tree's."""
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
    """standing clauses v9 (Component 7 of (R335): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b725_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b724's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R335-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b724's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R335) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b724's standing arm, carried in the run list of 116 (Component 6, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R334)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from f4ab9491',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 72 = 72 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b724-closing (f4ab9491)', 'push-b724-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (H-ONSET-MASS at its zeros; H-DIAL at c = 0.6, 0.8, 1.0; H-INTERFERENCE at its zeros; lambda_2 > 0 and what remains; the C2 theorem, its grade and its certificates; b723`s row and the chain; the plant needle and the legacy copy landed), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R335)(1)-(2): the generated corrigendum for b724`s record, landed at FINDINGS :11683: its eighteen events and nineteen defects, 37 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 4 CLOSE 33, REPEAT 25; the four mirror citations READS WRONG among the dated notes; v1.5.0`s repairs by data/b725_standing_v150.txt; the corrigenda bank appended at row (45)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b725 and no b725 rules bank: no author`s word of b725 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b725's objects (Component 6, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R335)(3), N2: data/b725_registrations.txt committed alone at 22210d4b after Component 1 and before any figure it names -- the onset bank, its control and rule, H-DIAL`s, H-INTERFERENCE`s, lambda_2`s, the C2 bank and the dispatch rows each first added in a commit descending from it and not it, H-INTERFERENCE`s after its amendment 706b4ca1 and H-DIAL`s after dc0d4133; the file at HEAD its text at 22210d4b with lines appended alone; the components each the ancestor of the next (d9739558, 7be1601c, e6c6348a, c59a3e97, 22210d4b, then the computations` commits); the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'reg_first', lambda d: d.update({'data/b725_dial.txt': [K.REG_COMMIT]}))),
    ('G-PREDICTION-FIRST', '(R332)(9)(i), N5, the scan arm: tools/b725_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, the bank`s counts the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R335)(4)(i), (8), N3: H-ONSET-MASS -- the POST HOC control and the rule banked before any onset (ONSETS COMPUTED 0 at both, the control`s (C2) AS WANTED, the rule WALKED 3, SELECTED 3); the onset bank`s foot its last line, C1 AS WANTED, ZEROS 3, the computed, beyond-reach and not-run counts summing to 3; each computed onset with its deviation, each zero not computed CARRIED, NOT COMPUTED ((R335)(8)) with its bracket; REFUTED exactly where a printed deviation passes 0.05',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'onset', re.sub(r'THE HYPOTHESIS (\w+(?: \w+)?)\.\*\*(\s*)$', lambda m: 'THE HYPOTHESIS %s.**%s' % ('HELD' if m.group(1) != 'HELD' else 'REFUTED', m.group(2)), S['onset'] or ''))),
    ('G-DERIVATION-GRADED', '(R335)(4)(iii), N1, N3, N5: lambda_2 on keiper-b725 alone -- the branch at f52e188c locally and at origin, cut from main badaccc, its files KeiperTwo.lean and print_targets.txt, off main and untagged; the bank`s last line (run 41091360710, the standard three, NO sorryAx, the two named premises, DISPATCHES 2 OF 3, NO MAIN, NO TAG); the grades DERIVES 2, INTERFACES 4 and what remains printed',
     lambda S: derivation_graded_ok(S), lambda S: _mut(S, 'ef_branches', lambda d: d['keiper-b725'].update(tags=['v0.38']))),
    ('G-OFFSET-POST-HOC', '(R335)(4)(iv), N1, N3, N5: the C2 theorem -- the E0 grade (DERIVES) before route (B) mirrored equal at 18 of 18, both before the branch and the read; c2-b725 at 52cbbc11 locally and at origin, cut from main badaccc, its files C2Walk.lean and print_targets.txt, off main and untagged; the bank`s last line naming run 41095053686, the certificates read, what remains and DISPATCHES 3 OF 3, NO MAIN, NO TAG; the build stopped under the hold, 0 OF 18, CARRIED, the dispatch rows` read the same',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'drows', lambda d: [r.update(build_exit='0') for r in d if r.get('kind') == 'read' and r.get('run') == K.EF_RUNS[2][1]])),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at f4ab9491, VERSION 9; v8 at HEAD its blob at f4ab9491; no v10; v9`s commit an ancestor of v1.5.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- the file byte-equal at f4ab9491, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R335)(4)(ii), N3, the stop rule: H-DIAL -- the bank`s foot its last line, (c0) and (id) AS WANTED, ONSETS 3 OF 3, the hypothesis graded; the products` spread printed against 0.10 and REFUTED exactly where it passes it (0.4120); the stop rule`s (4)(ii) row; the bank in the computations` commits',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'dial', (S['dial'] or '').replace('spread (max - min)/mean 0.4120', 'spread (max - min)/mean 0.0412'))),
    ('G-DIFFERS-ERRATA', '(R335)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at a6d363b6, no b725 differs or errata bank, the worklist naming no line or id for either; the weight line and the corrigendum in 9b0daac6, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b725_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R335-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b724`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at f4ab9491 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R335)(4)(iii)-(iv): the three runs, 41090029391, 41091360710 and 41095053686, each read once by its id -- three commits, pushes, dispatches and reads chained, the commits the branches` tips; run 1 FAILS with exit 1, run 2 BUILDS with the standard three at its six terminals and no sorryAx, run 3 STOPPED UNDER THE HOLD; the lambda_2 bank naming run 2 and DISPATCHES 2 OF 3, the C2 bank run 3 and DISPATCHES 3 OF 3',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: the dispatches` order and hold -- free memory at or above 2,560 MB at each push, dispatch and read; for each dispatch its commit before its push before it before its read; three dispatches, each by `gh workflow run build-module.yml` at main with the ref input the branch`s tip, none by push; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b724 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, keiper-b725 and c2-b725 off it; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s two (FINDINGS and OPEN_TRAILS, (R335)(5)); no ERRATA, no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b724`s trail record on OPEN_TRAILS (:16422) and its root in the chain', lambda S: '### b724 — lane two, act one hundred and fifty-one, the second checkpoint act under (R334)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b724`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: (R335)(4)(iii)-(iv)`s three by gh workflow run, each read by its id in data/b725_dispatch_rows.json; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b725: (R335)'s rows, b724's (R334) rows pruned. The quote read from the bank (data/b725_ferry.txt :7)
    hq = _quote(rd(p('data', 'b725_ferry.txt')) or '', '"b724 closed: relay 6ca86862', '". Its rows')
    add('ruling (1)', 'data/b724_closing.txt :1, the head line as the ruling quotes it (data/b725_ferry.txt :7)', bool(hq) and hq[1:] == at(cl, 1),
        at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', 'f4ab9491', 'data/b724_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'the head line as the public relay carries it at f4ab9491', bool(pub) and pub[0] == at(cl, 1),
        'remote main %s' % rm[:8], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt'))]
    add('ruling (1)', 'data/act_roots.txt :103, b724`s root e09d0fac chained from b723`s 92964067', at(ar_, 103)[:1] == ['b724']
        and at(ar_, 103)[1].startswith('e09d0fac') and at(ar_, 103)[2].startswith('92964067'), ' '.join(x[:8] for x in at(ar_, 103)), '1')
    add('ruling (1), (2)(i)', 'data/act_roots.txt :102, b724`s corrigendum row for b723', at(ar_, 102)[:2] == ['corrigendum', 'b723'],
        ' '.join(x[:12] for x in at(ar_, 102)), '1')
    for f_ in ('b724_orders_triage.txt', 'b724_legacy.txt', 'b724_split_price.txt', 'b724_defects.txt'):
        add('ruling (1)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '1')
    lv_ = lines_of(p('data', 'b724_lv.txt'))
    add('ruling (1)', 'data/b724_lv.txt :43, the negation with the standard three', 'not_T3_perClass_to_combinations' in at(lv_, 43)
        and at(lv_, 43).endswith('[propext, Classical.choice, Quot.sound]'), at(lv_, 43)[-60:], '1')
    er_ = rd(os.path.join(PP, 'ERRATA.md')) or ''
    add('ruling (1)', 'ERRATA.md: E-2026-10-29-1 entered', 'E-2026-10-29-1' in er_, 'present' if 'E-2026-10-29-1' in er_ else 'ABSENT', '1')
    add('ruling (1)', 'OPEN_TRAILS :16571, the open orders 82 to 63', 'open orders 82 before these lines, 63 after' in at(ot, 16571),
        at(ot, 16571)[:60], '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(18) and 19 defects (data/b724_events.txt, data/b724_defects.txt; the head line`s "19 defects")',
        starts == list(range(1, 19)) and len(letters) == 19, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((77, 13, 'CLOSE ; NEW'), (97, 16, 'CLAIM ; NEW'), (114, 18, 'CLOSE ; REPEAT class (ix)')):
        add('ferry (read first)', 'event (%d) at data/b724_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:60],
            at(ev, n_)[:50], '0')
    add('ferry (read first)', 'data/b724_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    for f_ in ('b723_registrations.txt', 'b723_support.txt', 'b723_zetak.txt', 'b722_c2_price.txt', 'b711_list.json', 'b707_onset.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    rg_ = lines_of(p('data', 'b723_registrations.txt'))
    add('ferry (read first), ruling (3)(ii)', 'data/b723_registrations.txt (iii), H-DIAL', any(l.startswith('## (iii) H-DIAL') for l in rg_),
        next((l[:50] for l in rg_ if l.startswith('## (iii)')), 'NONE'), '2')
    cp_ = lines_of(p('data', 'b722_c2_price.txt'))
    add('ferry (read first), ruling (3)(iv)', 'data/b722_c2_price.txt (B), the certificate route', any(l.startswith('### (B) the certificate route') for l in cp_),
        next((l[:50] for l in cp_ if l.startswith('### (B)')), 'NONE'), '2')
    tg_ = rd(p('data', 'b724_orders_triage.txt')) or ''
    for o_ in ('W-ORD-LI-FAMILY-CONTROL', 'W-ORD-EXACT-SUPPORT', 'W-ORD-STRICT-BOUND'):
        add('ferry (read first), ruling (2)(iv)', 'data/b724_orders_triage.txt, the RE-SCOPE row %s' % o_, o_ in tg_, 'present' if o_ in tg_ else 'ABSENT', '1')
    ki_ = lines_of(os.path.join(K.EF_DIR, 'SIDEExplicitFormula', 'KeiperIdentities.lean'))
    add('ferry (read first), ruling (3)(iii)', 'SIDE-explicit-formula KeiperIdentities.lean :20, (O4) GammaRZetaValues not proved', 'GammaRZetaValues' in at(ki_, 20),
        at(ki_, 20)[:60], '3')
    kb_ = lines_of(os.path.join(K.EF_DIR, 'SIDEExplicitFormula', 'KeiperBounds.lean'))
    add('ferry (read first)', 'SIDE-explicit-formula KeiperBounds.lean :109-:112, BoundPremises', at(kb_, 109).startswith('structure BoundPremises')
        and 'higher_stieltjes' in at(kb_, 111), at(kb_, 109)[:40], '3')
    ks_ = rd(os.path.join(K.EF_DIR, 'SIDEExplicitFormula', 'KeiperSign.lean')) or ''
    add('ferry (read first)', 'SIDE-explicit-formula KeiperSign.lean, liCoeff_one_pos by the gamma route', 'theorem liCoeff_one_pos ' in ks_ and 'gamma_gt_seq_fifteen' in ks_,
        'present' if ks_ else 'ABSENT', '3')
    add('PATHS', 'SIDE-explicit-formula at the path its clone has on this host', os.path.isdir(os.path.join(K.EF_DIR, '.git')), K.EF_DIR, '0')
    add('PATHS', 'SIDE-lv-conservation at D:/SIDE-lv-conservation', os.path.isdir(os.path.join(K.LV_DIR, '.git')), K.LV_DIR, '0')
    add('ferry (read first), ruling (2)(i)', 'tools/act_root.py', os.path.exists(p('tools', 'act_root.py')), 'present', '1')
    lg = (rd(p('tools', 'standing', 'legacy.py')) or '')
    add('ruling (2)(iii)', 'the exception file tools/standing/legacy.py, its NAMES', lg.count("    'b") > 0, '%d names' % lg.count("    'b"), '1')
    b644_ = lines_of(p('tools', 'b644_record.py'))
    add('ruling (2)(iii)', 'tools/b644_record.py :1088 (the line the copy replaces; its text not printed)', len(b644_) >= 1088 and bool(at(b644_, 1088).strip()),
        'lines %d' % len(b644_), '1')
    mb_ = rd(p('data', 'b724_mirror.txt')) or ''
    add('ruling (2)(v)', 'data/b724_mirror.txt, the two carried citations (R334)(5) and (R334)(2)(iii)', '(R334)(5)' in mb_ and '(R334)(2)(iii)' in mb_,
        '(R334)(5) %d ; (R334)(2)(iii) %d' % (mb_.count('(R334)(5)'), mb_.count('(R334)(2)(iii)')), '1')
    add('ferry', 'tools/standing/ at v1.4.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.4.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ruling (2), ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R335)(2)(i): b723's row and the chain's reader -- b723's root commit and its bank_hashes at that commit
    add('ruling (2)(i)', 'f585420f, the commit b723`s root banks rode in', gr('D:/relay', 'cat-file', '-t', 'f585420f') == 'commit',
        gr('D:/relay', 'log', '--format=%s', '-1', 'f585420f')[:60], '1')
    # ### (R335)(2)(ii): the plant needle reads the act's own ferry; its control the b723 and b724 ferries
    for f_ in ('b723_ferry.txt', 'b724_ferry.txt'):
        add('ruling (2)(ii)', 'data/%s, the plant needle`s control ferry' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '1')
    # ### (R335)(3)(i): the certified list and the template family's onset route
    add('ruling (3)(i)', 'data/b711_list.json, the certified list H-ONSET-MASS reads M(gamma) from', bool(_jl('b711_list.json')), 'readable %s' % bool(_jl('b711_list.json')), '2')
    # ### (R335)(4): the price sources -- b723's banked timings
    for f_ in ('b723_support.txt', 'b723_zetak.txt'):
        add('ruling (4)(i)', 'data/%s, b723`s banked onset timings (the price source)' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    # ### (R335)(5): the kept branches, the deletes, the (W) list's tools/mirror_prevbuild.json
    add('ruling (5)', 'D:/MY-DOwnloads/mirror-refresh-2026-10-29-b724.zip, b724`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '4')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R335)(5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (5)', 'the push-b724-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R335)(5): act_current alone, then b724's step row 32 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b724_steps.json'),
                   (K.STEPZERO, 'data/b724_relay_push-b724-closing_push_out.txt')):
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (5)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (5)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (5)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (5)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '4')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b725_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b725_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b725 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b724_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R335)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 4) are the corrigendum with v1.5.0's controls, b723's row and the RE-SCOPE reads, the registrations and the price table,
H-ONSET-MASS, H-DIAL, H-INTERFERENCE, lambda_2, the C2 theorem, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R335)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for b726 ((R335)(7)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act on SIDE-explicit-formula's keiper-b725 and c2-b725 alone ((R335)(4)(iii)-(iv), N5): no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b726 ((R335)(7)); the open orders by tools/standing/orders.py's output over the trail, (R335)(10)'s six
    among them, not a hand list (Component 4, the Edit tool)."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b725 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-TWO, THE RESEARCH ACT: H-ONSET-MASS, H-DIAL AND '
              'H-INTERFERENCE READ AGAINST THEIR REGISTRATIONS; lambda_2 > 0 ON TWO NAMED PREMISES ON keiper-b725; THE C2 THEOREM GRADED DERIVES '
              'AND CARRIED ON c2-b725; b723`S ROW READ IN b680`S FORM; v1.5.0 LANDED, UNDER (R335).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 4, the Edit tool; b724's sections over b724's objects not carried). A row of two
    reads its bank's verdict line by vtail; a row of three reads the line its pattern names (a bank with several verdict lines, or a verdict
    wrapped across lines)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.5.0: the short names, the plant needle, the legacy copy and the mirror citations, each case failing before '
                 'its repair and passing after', 'b725_standing_v150.txt'),
                ('b723`s row at act_roots :102 in b680`s form, the chain`s verify, the hashed bytes rebuilt, routes (A) and (B)', 'b725_root_row.txt'),
                ('the three RE-SCOPE orders, each trigger written, for the root`s prompt', 'b725_rescope.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE REGISTRATIONS ((R335)(3))', [
                ('the price table, each item priced before it ran', 'b725_price.txt'),
                ('the stop rule read at each item`s start', 'b725_stop_rule.txt', r'(?m)^  ENDED [^\n]*'),
                ('the citation check over the addendum', 'b725_addendum_citation.txt')]),
            ('THE H-ONSET-MASS ((R335)(4)(i), (8))', [
                ('the five-zero control, POST HOC', 'b725_onset_mass_control.txt'),
                ('the rule`s output, before any onset', 'b725_onset_mass_rule.txt'),
                ('the onsets on the zeros the rule named, read against the falsifier; the zeros carried with their brackets', 'b725_onset_mass.txt')]),
            ('THE H-DIAL ((R335)(4)(ii))', [
                ('the onsets at c = 0.6, 0.8, 1.0 and their products', 'b725_dial.txt')]),
            ('THE H-INTERFERENCE ((R335)(9))', [
                ('Z_Q1 at every certified off-line zero of Z_Q0 to height 445', 'b725_interference.txt')]),
            ('THE lambda_2 ((R335)(4)(iii))', [
                ('the closed form and the sign on keiper-b725, two dispatches each read by its id', 'b725_lambda2.txt')]),
            ('THE C2 THEOREM ((R335)(4)(iv))', [
                ('the E0 grade, route (B) mirrored, c2-b725 and its one dispatch read by its id', 'b725_c2.txt', r'\*\*THE C2 THEOREM: [^*]*')]),
            ('THE NAME AND ADDRESS ((R332)(9))', [
                ('the scan over every commit and bank of the act, the previous address and name held in memory, the counts alone', 'b725_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b724`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b725_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: SIDE-explicit-formula`s keiper-b725 and c2-b725 alone ((R335)(4)(iii)-(iv), N5), each cut from main badaccc --',
    '    keiper-b725 two tree states (9a61ba22, f52e188c; SIDEExplicitFormula/KeiperTwo.lean and print_targets.txt), c2-b725 one (52cbbc11;',
    '    SIDEExplicitFormula/C2Walk.lean and print_targets.txt), each pushed alone through push_gated.sh and read back equal, the commits',
    '    under the noreply identity on the command (the local configuration not edited, defect (d)) ; three dispatches of build-module.yml,',
    '    runs 41090029391, 41091360710 and 41095053686, each read by its run id (relay data/b725_dispatch_rows.json) ; no kernel`s main',
    '    touched, no tag cut (N5) ; the rebuild-b721 branches of the wave 1 kernels as b724 left them ; SIDE-explicit-formula`s main at',
    '    badaccc and v0.37 unmoved, the challenge branch challenge-b720-h2-sign-iff-rh standing ; port-b707 of SIDE-lv-conservation at',
    '    b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main and its deposit v0.10.0 unmoved ; SIDE-faces-join`s',
    '    main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host, three dispatches of three at most ; free',
    '    memory read before each computation, push, dispatch and read ; the push-b724-* branches of relay and PLACE-papers deleted at step',
    '    zero by name, one per command and each its own message ; nothing vendored ; the units files of H-ONSET-MASS, H-DIAL and',
    '    H-INTERFERENCE banked as the act`s banks ; N2: the registrations committed before any figure, the order printed by ancestry, the',
    '    rule`s output before any onset, each tool`s controls before its figures, the five-zero control POST HOC ; N3: every grade at its',
    '    bank`s end ; (R332)(9): no new occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay',
    '    data/b725_address_scan.txt), the commits under the GitHub login and its noreply address ; no identifier of the author in any',
    '    outbound request header, URL, input or payload, or in any workflow file ; no secret added ; the seat`s plain requests to github.com',
    '    (its git reads, pushes, the dispatches and the run reads) and the computations` reads the act`s outbound calls ; the deposit route',
    '    untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry)',
    '    and OPEN_TRAILS (the trail with (R335)(10)`s six orders) appended ; no ERRATA, no paper cut, moved or renamed ; no FOUNDATIONS,',
    '    REGISTRY, README or faces page byte ; data/act_roots.txt (b725`s root alone; b723`s row read at :102 as b724 wrote it) and the corrigenda bank appended ; data/act_current.json',
    '    written at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.5.0 by (R335)(2) ; the hook in D:/.claude/settings.json',
    '    unedited ; the per-act tools of b698-b724 unedited ; the mirror zip written outside every repository over the roster read from',
    '    PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE',
    '    or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R335)(7)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        RE-SCOPE orders as the author rules them at the root`s prompt (relay data/b725_rescope.txt).',
    '    (c) For b726, each from its bank: H-ONSET-MASS`s carried zeros with their ladder brackets and its successor written from the',
    '        banked onsets (relay data/b725_onset_mass.txt); lambda_2`s two premises (relay data/b725_lambda2.txt); the C2 theorem`s',
    '        certificates, (L1) and (L2) at c2-b725, a memory-bounded route priced (relay data/b725_c2.txt); b723`s routes (A) and (B)',
    '        (relay data/b725_root_row.txt); the reproduction`s NOT RUN rows, each with its price (relay data/b725_reproduce.txt); the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 (at f52e188c) and c2-b725 (at',
    '        52cbbc11) of SIDE-explicit-formula, (R335)(4)(iii)-(iv)`s, off main, untagged; scratch-b724 of SIDE-lv-conservation;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the rebuild-b721 branches of the wave 1 kernels as b724 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, SIDE-explicit-formula`s keiper-b725 and c2-b725 carrying (R335)(4)(iii)-(iv)`s commits, no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b725: the standing repairs are v1.5.0's ((R335)(2), relay data/b725_standing_v150.txt, read in the corrigendum section); the
    # ### carry's diffs here (b725 carried at step zero before the fold; its tools since are the templates and tools/acts/b725.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act; '
          'SIDE-explicit-formula`s %s ((R335)(4)(iii)-(iv)), cut from main %s; the %s branches of the wave 1 kernels as b724 left them; '
          'SIDE-lv-conservation`s main untouched, port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], ' and '.join('%s at %s' % (b, t[:8]) for b, t in K.EF_BRANCHES), K.EF_BASE[:8], K.REBUILD_BRANCH,
              K.PORT_NEW_TIP[:8]))
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
    b725's form over b725's objects (Component 4, the Edit tool; b724's form in git at b724's record tool): the corrigendum's foot and v1.5.0's
    controls; b723's row and the chain's verify; the RE-SCOPE reads; the price table; H-ONSET-MASS; H-DIAL; H-INTERFERENCE; lambda_2; the C2
    theorem; the two citation checks; the reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank
    does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v150.txt' % ACT, r'\*\*v1\.5\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.5.0`s controls')
    rr = _bfig('%s_root_row.txt' % ACT, r"\*\*b723'S ROW IN b680'S FORM: STANDING AT :(\d+), [^;]* ; VERIFY ([^;]+?) ; THE HASHED BYTES REBUILT: "
               r"([^;]+?) ; NO COMMIT CARRIES THEM ; ROUTES \(A\) AND \(B\) FOR THE AUTHOR\.\*\*", 'b723`s row`s foot')
    rs_foot, = _bfig('%s_rescope.txt' % ACT, r"\*\*\(R335\)\(2\)\(iv\): (.*) ; ALL THREE FOR THE ROOT'S PROMPT\.\*\*", 'the RE-SCOPE reads` foot')
    rs = re.findall(r"([A-Z][A-Z-]+) -- TRIGGER WRITTEN, (KEEP|RETIRE)", rs_foot)
    pr = _bfig('%s_price.txt' % ACT, r"\*\*THE PRICE TABLE: (.*) ; THE CLOSE ([\d.-]+) H ; THE BUDGET ([\d.]+) H \(b723'S ACT\) ; ([^*]*)\.\*\*", 'the price table`s foot')
    on = _bfig('%s_onset_mass.txt' % ACT, r'\*\*H-ONSET-MASS: C1 AS WANTED ; ZEROS (\d+) ; ONSETS COMPUTED (\d+) ; WITHIN 0\.05 (\d+) ; BEYOND REACH (\d+) ; '
               r'NOT RUN (\d+) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*', 'H-ONSET-MASS`s foot')
    on_out = [re.sub(r"[\[\]']", '', x) for x in _bfig('%s_onset_mass.txt' % ACT, r'(?m)^BEYOND REACH, NO ONSET COMPUTED: (.*) ; NOT RUN \(carried with its '
                                                         r'price\): (.*)$', 'H-ONSET-MASS`s carried zeros')]   # ### the tool prints Python lists
    # ### each computed onset: (zero, a*_pred, a*, lambda_min, a*/a*_pred - 1, the falsifier's reading), from the zero's three lines
    on_onsets = re.findall(r'(?m)^  (\w+): beta [\d.]+ ; gamma0 \S+ ; a\*_pred ([\d.]+)\n    the ladder[^\n]*\n    THE ONSET: \S+ \(grid point [^)]*\) at '
                           r'a = ([\d.]+) \+- \S+, lambda_min (-?[\d.]+) \+- \S+ ; a\*/a\*_pred - 1 = ([+-][\d.]+) -- (WITHIN 0\.05|BEYOND 0\.05)',
                           rdn('%s_onset_mass.txt' % ACT))
    on_brackets = re.findall(r'(?m)^  (\w+): beta [^\n]*\n    the ladder[^\n]*\n    CARRIED, NOT COMPUTED \(\(R335\)\(8\)\): ([^\n]+)$',
                             rdn('%s_onset_mass.txt' % ACT))
    dl = _bfig('%s_dial.txt' % ACT, r'\*\*H-DIAL: \(c0\) AS WANTED ; \(id\) AS WANTED ; ONSETS (\d) OF 3 ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*', 'H-DIAL`s foot')
    dlp = _bfig('%s_dial.txt' % ACT, r"THE PRODUCTS \[([^\]]*)\] ; mean ([\d.]+) ; spread \(max - min\)/mean ([\d.]+) against ([\d.]+)", 'H-DIAL`s products')
    itf = _bfig('%s_interference.txt' % ACT, r'\*\*H-INTERFERENCE: \(C1\) AS WANTED ; \(C2\)-\(C4\) AS WANTED ; ZEROS (\d+) ; READ (\d+) ; Z_Q1 EXCLUDES 0 AT (\d+) ; '
                r'THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*', 'H-INTERFERENCE`s foot')
    l2 = _bfig('%s_lambda2.txt' % ACT, r'ON keiper-b725 \(([0-9a-f]{8}), RUN (\d+)\) WITH THE STANDARD THREE, NO sorryAx, ON TWO NAMED PREMISES -- (.*?) -- BOTH '
               r'PRINTED AS WHAT REMAINS ; GRADES DERIVES (\d+), INTERFACES (\d+) ; DISPATCHES (\d) OF 3 ; NO MAIN, NO TAG\.\*\*', 'lambda_2`s foot')
    c2 = _bfig('%s_c2.txt' % ACT, r"\*\*THE C2 THEOREM: E0 DERIVES ; ROUTE \(B\) EQUAL TO THE STATEMENT AT (\d+) OF 18 ; ON c2-b725 \(([0-9a-f]{8}), RUN (\d+)\) "
               r"(.*?) ; CERTIFICATES BY decide \+kernel (\d+) OF 18 READ ; ([^;]+?) ; WHAT REMAINS: ([^;]+?) ; DISPATCHES (\d) OF 3 ; NO MAIN, NO TAG\.\*\*",
               'the C2 theorem`s foot')
    c2low, = _bfig('%s_c2.txt' % ACT, r'LOW (\d+) MB, EXIT 143', 'the C2 run`s low')
    acit = _bfig('%s_addendum_citation.txt' % ACT, r'\*\*CITES (\d+) ; OK (\d+) ; MISS (\d+) --', 'the addendum`s citation check')
    cit = _bfig(K.CITATION_BANK, r'\*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
    drows = json.loads(rdn('%s_dispatch_rows.json' % ACT) or '[]')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v150_ctl=v5[0], v150_cases=v5[1], v150_wanted=v5[2],
                rr_row=rr[0], rr_verify=rr[1], rr_bytes=rr[2], rs=rs,
                pr_rows=pr[0], pr_close=pr[1], pr_budget=pr[2], pr_choice=pr[3],
                on_zeros=on[0], on_computed=on[1], on_within=on[2], on_beyond=on[3], on_notrun=on[4], on_word=on[5],
                on_beyond_names=on_out[0], on_notrun_names=on_out[1], on_onsets=on_onsets, on_brackets=on_brackets,
                dl_onsets=dl[0], dl_word=dl[1], dl_products=dlp[0], dl_mean=dlp[1], dl_spread=dlp[2], dl_bar=dlp[3],
                it_zeros=itf[0], it_read=itf[1], it_excl=itf[2], it_word=itf[3],
                l2_tip=l2[0], l2_run=l2[1], l2_premises=l2[2], l2_derives=l2[3], l2_interfaces=l2[4], l2_dispatches=l2[5],
                c2_mirror=c2[0], c2_tip=c2[1], c2_run=c2[2], c2_how=c2[3], c2_certs=c2[4], c2_word=c2[5], c2_remains=c2[6], c2_dispatches=c2[7],
                c2_low=c2low, acit_n=acit[0], acit_ok=acit[1], acit_miss=acit[2], cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                drows=drows,
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R335)(4)(iii)-(iv): the kernel rows of one kind as banked (data/b725_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R335): no lean process runs on this host; the runner dispatches are those of (R335)(4)(iii)-(iv), three at most, each read by its
    run id. From the command bank (the seat's commands, read live from the capture by the `commands` route: local lean none; the dispatch
    commands `gh workflow run`) and the dispatch rows (relay data/b725_dispatch_rows.json: each dispatch by command and each read by its run
    id), against the worklist's EF_RUNS (Component 4, the Edit tool; b724's N1 read b724's lv run)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = json.loads(rdn('%s_dispatch_rows.json' % ACT) or '[]')
    dsp, rds = _ef_kind(rows, 'dispatch'), _ef_kind(rows, 'read')
    ran = [(r.get('item'), r.get('run')) for r in dsp]
    want = [(i, r) for i, r in K.EF_RUNS]
    read_ids = [r.get('run') for r in rds]
    ok = bool(cm) and not seat_lean and len(ran) <= K.MAX_DISPATCHES and ran == want and read_ids == [r for _i, r in want] \
        and len(disp) == len(dsp)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b725_commands.json): %s; dispatch commands in the capture: %s against '
        'the rows` dispatches %d; the runs dispatched (relay data/b725_dispatch_rows.json) %d of %d at most, equal to the worklist`s EF_RUNS: %s '
        '(%s); each read by its id: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(dsp), len(ran), K.MAX_DISPATCHES, ran == want,
            ', '.join('%s %s' % x for x in ran) or 'NONE', read_ids == [r for _i, r in want]))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (Component 4, the Edit tool, over b725's objects; b724's over v1.4.0's classes in git at b724's record tool): the banks holding a
# ### figure at a test zero of H-ONSET-MASS or at F_c, each first added after the registrations' commit
N2_FIGURE_BANKS = ('data/b725_onset_mass.txt', 'data/b725_onset_mass_units.jsonl', 'data/b725_dial.txt', 'data/b725_dial_units.jsonl')
# ### N2: H-ONSET-MASS's rule output and predictions, committed before any onset
N2_RULE = 'data/b725_onset_mass_rule.txt'
N2_ONSETS = ('data/b725_onset_mass.txt', 'data/b725_onset_mass_units.jsonl')
# ### N2: each tool's controls before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b725_onset_mass.txt', '## (C1) THE BANKED ONSETS', '## THE ZEROS, IN THE RULE`S ORDER'),
               ('data/b725_dial.txt', '## (c0)', '## THE ONSETS'),
               ('data/b725_interference.txt', '## THE CONTROLS: ', '## THE ZEROS '),
               ('data/b725_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None


def _strictly_before(a, b):
    return bool(a) and bool(b) and a != b and grc(ROOT, 'merge-base', '--is-ancestor', a, b) == 0
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R335): data/b725_registrations.txt committed before any bank holding a figure at a test zero of H-ONSET-MASS or at F_c, the order
    printed by ancestry; H-ONSET-MASS's rule output and predictions committed before any onset; each tool's controls print before its
    figures; the five-zero control labelled POST HOC wherever it is named. From git (each bank's first-adding commit against the
    registrations' commit and the rule's), the banks' own lines, and the entry as composed (the findings bank's text, or the composer before
    it is written)."""
    reg = _first_add('data/b725_registrations.txt')
    figs_ = [(p, _first_add(p)) for p in N2_FIGURE_BANKS]
    fig_ok = [(p, _strictly_before(reg, c)) for p, c in figs_]
    rule = _first_add(N2_RULE)
    rule_ok = [(p, _strictly_before(rule, _first_add(p))) for p in N2_ONSETS]
    fj_ = jl('%s_findings.json' % ACT)
    etext = fj_.get('text') or _finding_text()[1]
    ctl_t = rdn('%s_onset_mass_control.txt' % ACT)
    named = [s.strip()[:90] for s in re.split(r'(?<=[.;])\s+', etext) if re.search(r'(?i)\bfive\b[^.;]*\bcontrol\b|onset_mass_control', s)]
    unlabelled = [s for s in named if 'POST HOC' not in s]
    ph_ok = not unlabelled and 'CONTROL (POST HOC)' in ctl_t
#⟪END⟫
#⟪SECTION record 12⟫
    ok = bool(reg) and reg.startswith(K.REG_COMMIT) and all(o for _p, o in fig_ok) and all(o for _p, o in rule_ok) \
        and all(o for _p, o in ctl) and ph_ok
#⟪END⟫
#⟪SECTION record 13⟫
        'the registrations` commit %s (the worklist`s %s); each figure bank first added strictly after it, by ancestry: %s; H-ONSET-MASS`s '
        'rule (%s, first added %s) strictly before each onset bank: %s; each tool`s controls before its figures: %s; the five-zero control '
        'named in the entry %d time%s, unlabelled POST HOC: %s; its bank`s foot CONTROL (POST HOC): %s' % (
            (reg or 'NONE')[:8], K.REG_COMMIT, ', '.join('%s %s (%s)' % (os.path.basename(p), o, (c or 'uncommitted')[:8]) for (p, o), (_p, c)
                                                         in zip(fig_ok, figs_)),
            N2_RULE, (rule or 'NONE')[:8], ', '.join('%s %s' % (os.path.basename(p), o) for p, o in rule_ok),
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl), len(named), '' if len(named) == 1 else 's', unlabelled or 'NONE',
            'CONTROL (POST HOC)' in ctl_t))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (Component 4, the Edit tool, over b725's objects; b724's over the ledger split in git at b724's record tool): the banks whose
# ### grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b725_standing_v150.txt', ('ALL AS WANTED',)), ('b725_root_row.txt', ('VERIFY', 'FOR THE AUTHOR')),
             ('b725_rescope.txt', ('TRIGGER WRITTEN', 'FOR THE ROOT')), ('b725_price.txt', ('THE PRICE TABLE',)),
             ('b725_onset_mass.txt', ('THE HYPOTHESIS',)), ('b725_onset_mass_control.txt', ('POST HOC', 'ONSETS COMPUTED 0')),
             ('b725_onset_mass_rule.txt', ('SELECTED', 'ONSETS COMPUTED 0')), ('b725_dial.txt', ('THE HYPOTHESIS',)),
             ('b725_interference.txt', ('THE HYPOTHESIS',)), ('b725_lambda2.txt', ('GRADES', 'DISPATCHES')),
             ('b725_c2.txt', ('THE C2 THEOREM', 'DISPATCHES')), ('b725_citation_check.txt', ('CITES CHECKED',)),
             ('b725_reproduce.txt', ('REPRODUCES',)))
# ### N3: a sentence saying a module compiles, and the words that carry its axiom print; a negation before the verb
N3_COMPILES = re.compile(r'(?i)\bcompil(?:es|ed)\b')
N3_AXIOMS = re.compile(r'(?i)standard three|propext|axioms?\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|nothing|no)\b[^.;]{0,24}$')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R335): every grade prints at its end; no sentence of the entry calls a compile complete without its axiom print, or a hypothesis
    held on fewer zeros than its rule named without saying so. From the banks' last lines and the entry as composed (the findings bank's text,
    or the composer before it is written): each sentence saying a module compiles, not in negation, carries its axioms; each sentence holding
    H-ONSET-MASS or H-INTERFERENCE carries the zeros read against those its rule named, equal, or says fewer."""
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
    rules = (('H-ONSET-MASS', f['on_word'], f['on_computed'], f['on_zeros']), ('H-INTERFERENCE', f['it_word'], f['it_read'], f['it_zeros']))
#⟪END⟫
#⟪SECTION record 20⟫
    bare = []
    for s in sents:
        for m in N3_COMPILES.finditer(s):
            if not N3_NEGATED.search(s[:m.start()]) and not N3_AXIOMS.search(s):
                bare.append(s.strip()[:120])
                break
    short = []
    for h, word, read_, named_ in rules:
        for s in sents:
            if h in s and re.search(r'\bHELD\b', s) and not ('%s of %s' % (read_, named_) in s and read_ == named_) and 'fewer' not in s:
                short.append(s.strip()[:120])
    ok = all(o for _n, o in graded) and not bare and not short
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the sentences of %s saying a module compiles, not in negation, without its '
        'axioms: %s; the hypotheses by their rules -- %s; the sentences holding one on fewer zeros than its rule named without saying so: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bare or 'NONE',
            ', '.join('%s %s at %s of %s' % (h, w, r_, n_) for h, w, r_, n_ in rules), short or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R335) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R335)(5))
N4_APPENDED = ('data/%s_steps.json' % ACT, 'data/%s_bank_hashes.json' % ACT, 'data/%s_hook_refusals.txt' % ACT, 'tools/mirror_prevbuild.json')


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
    # ### (R335) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b724's form, carried) -- read from git,
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
    # ### (R335)(6), N5 (Component 4, the Edit tool): no kernel's main touched and no tag cut, every Lean file of the act on keiper-b725 or
    # ### c2-b725 alone -- every ref of every kernel carrying a commit made after the act's opening commit is one of SIDE-explicit-formula's
    # ### two branches at its tip (the worklist's EF_BRANCHES), each over the base by its own commits, off main and untagged; no .lean file
    # ### changed or untracked in a kernel's tree; the rebuild-b721 branches kept as b724 left them; the address scan's count from its bank
    # ### (relay data/b725_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w, ef_new = [], []
    tips = dict(('refs/heads/' + b, t) for b, t in K.EF_BRANCHES)
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if kn == 'SIDE-explicit-formula' and tips.get(r_[0]) == r_[1]:
                    ef_new.append(r_[0][len('refs/heads/'):])
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    ef_scr = [(b, grc(K.EF_DIR, 'merge-base', '--is-ancestor', K.EF_BASE, t) == 0 and grc(K.EF_DIR, 'merge-base', '--is-ancestor', t, 'main') != 0
               and not g(K.EF_DIR, 'tag', '--points-at', t).strip()
               and all(p.endswith('.lean') or p == 'print_targets.txt' for p in g(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split()))
              for b, t in K.EF_BRANCHES]
    ef_scr_ok = sorted(ef_new) == sorted(b for b, _t in K.EF_BRANCHES) and all(o for _b, o in ef_scr)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and ef_scr_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b725_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s %s, or a .lean file in a kernel`s tree (%d kernels read): %s; each of those branches over '
            'the base %s, off main, untagged, its files against the base Lean files and the print list alone: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', ' and '.join('%s at %s' % (b, t[:8]) for b, t in K.EF_BRANCHES), len(K.KERNEL_PATHS),
                lean_w or 'NONE', K.EF_BASE[:8], ', '.join('%s %s' % x for x in ef_scr), K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b725 — lane two, act one hundred and fifty-two, the research act under (R335): b724 at its weight and its corrigendum; '
            'v1.5.0 and b723’s row; the registrations; H-ONSET-MASS, H-DIAL and H-INTERFERENCE; lambda_2 and the C2 theorem on their branches')
#⟪END⟫
#⟪SECTION record 29⟫
# ### (R335)(10): the six orders entered in OPEN_TRAILS at b725's trail, none acted on, each line carrying the addendum's sentence
SIX_ORDERS = ('W-ORD-MECHANISM-TABLE', 'W-ORD-VISIBILITY', 'W-ORD-ADMISSIBLE-CONE', 'W-ORD-DETECTION-DUAL', 'W-ORD-SILENT-SENTENCES',
              'W-ORD-SIDE-DIAGNOSTIC')
SIX_SENTENCE = 'entered from the navigator’s reflection of 2026-10-30, on the author’s word ‘enact’; no result is claimed by its entry.'


def _six_lines():
    """(R335)(10): the six orders' trail lines, each its name, its text as the addendum writes it (relay data/b725_addendum.txt) and the
    sentence; the text read from the addendum by the order's name, refusing where the addendum does not carry it."""
    add = rdn('%s_addendum.txt' % ACT)
    out = []
    for n in SIX_ORDERS:
        m = re.search(r'(?m)^%s -- ([^\n]+)$' % re.escape(n), add)   # ### at a line's head: (9) and the cone's trigger name two of them in prose
        if not m:
            sys.exit('### THE TRAIL: THE ADDENDUM DOES NOT CARRY %s -- NOTHING COMPOSED' % n)
        # ### tools/standing/orders.py reads an order OPEN by an entry word in upper case in the clause after its name
        out.append('**`%s` ENTERED 2026-10-30, b725, (R335)(10):** %s -- %s' % (n, m.group(1).strip().rstrip('.'), SIX_SENTENCE))
    return out


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 form adjusted to what the act did ("H-ONSET-MASS at <z> zeros <HELD |
    REFUTED | carried>; H-DIAL at c = 0.6, 0.8, 1.0 <...>; lambda_2 > 0 <compiled with the standard three | <what remains>>; the C2 theorem
    <compiled at 18 of 18, graded <grade> | <where it fell short>>; b723's row written, the chain AGREE; the plant needle and the legacy copy
    landed"), H-INTERFERENCE ((R335)(9)) beside H-DIAL, every figure from the banks (Component 4, the Edit tool; b724's title over b724's
    objects in git at b724's record tool)."""
#⟪END⟫
#⟪SECTION record 31⟫
    carried = int(f['on_beyond']) + int(f['on_notrun'])
    if f['c2_word'] != 'CARRIED WITH ITS TREE STATE' or f['c2_certs'] != '0':
        sys.exit('### THE TITLE: THE C2 THEOREM %s AT %s OF 18 -- THE FORM BELOW NAMES THE STOPPED BUILD; NOTHING COMPOSED' % (f['c2_word'], f['c2_certs']))
    chain = re.findall(r'(b\d{3}) (AGREE|DISAGREE)', f['rr_verify'])
    bad = [a for a, v in chain if v == 'DISAGREE']
    return ('## H-ONSET-MASS at %s of %s zeros %s%s; H-DIAL at c = 0.6, 0.8, 1.0 %s; H-INTERFERENCE at %s of %s zeros %s; lambda_2 > 0 compiled '
            'with the standard three on two named premises, both printed as what remains; the C2 theorem graded DERIVES, carried where its build '
            'stopped under the runner’s hold; b723’s row read in b680’s form, the chain %s; the plant needle and the legacy copy landed' % (
                f['on_computed'], f['on_zeros'], f['on_word'], (', %s carried' % num_word(carried)) if carried else '', f['dl_word'],
                f['it_read'], f['it_zeros'], f['it_word'],
                ('AGREE' if not bad else 'DISAGREE at %s (one bank)' % ', '.join(bad))))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) b723`s row in b680`s form at act_roots :%s, the chain`s verify reading %s, routes (A) and (B) for the author at the root`s '
            'prompt, none taken (relay data/b725_root_row.txt); (2) the RE-SCOPE reads, %s, each trigger written (relay data/b725_rescope.txt); '
            '(3) H-ONSET-MASS read as (R335)(8) orders: %s; carried, not computed: %s, their ladder brackets printed; no successor registered '
            '(relay data/b725_onset_mass.txt); (4) lambda_2`s two named premises, %s, printed as what remains (relay data/b725_lambda2.txt); '
            '(5) the C2 theorem carried with its tree state at c2-b725 %s, its one run stopped under the runner`s hold at %s MB, a memory-bounded '
            'route priced (relay data/b725_c2.txt); (6) SIDE-explicit-formula`s local configuration naming the previous address, left as it '
            'stands for the author`s word, the act`s commits there carrying the identity on the command (defect (d)); (7) %s and the seat’s %s '
            'defect%s as lettered' % (
                f['rr_row'], f['rr_verify'].lower(), ', '.join('%s %s' % x for x in f['rs']),
                'computed at %s of %s zeros, %s' % (f['on_computed'], f['on_zeros'], f['on_word']), ', '.join(x for x in (f['on_beyond_names'], f['on_notrun_names']) if x != 'none') or 'none',
                f['l2_premises'], f['c2_tip'], f['c2_low'],
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
            'author beside (R335)(7)’s naming of b726): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 6, the Edit tool, over b725's objects;
    b724's composer over b724's objects kept below as _finding_text_b724, not called, and in git at b724's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    ons = '; '.join('%s’s onset at a* = %s against a*_pred = %s, a*/a*_pred - 1 = %s, %s' % (
        z, a, p, d, 'within 0.05' if w.startswith('WITHIN') else 'beyond 0.05, the falsifier firing') for z, p, a, _l, d, w in f['on_onsets']) \
        or 'no onset computed'
    brk = '; '.join('%s carried, not computed: %s' % (z, b) for z, b in f['on_brackets']) or 'none carried'
    carried_n = int(f['on_beyond']) + int(f['on_notrun'])
    chain = re.findall(r'(b\d{3}) (AGREE|DISAGREE)', f['rr_verify'])
    e = ['', _title(), '',
         'H-ONSET-MASS reads %s, %s of its %s zeros computed (%s), %s carried with their ladder brackets; H-DIAL reads %s, its products (c/2) a* '
         '%s at c = 0.6, 0.8, 1.0 spreading %s of their mean against %s; H-INTERFERENCE reads %s at %s of %s zeros, Z_Q1 excluding 0 at %s; '
         'lambda_2 > 0 compiles with the standard three, no sorryAx, on two named premises printed as what remains; the C2 statement grades '
         'DERIVES and its route equals the statement at %s of 18 fields, but its one kernel build stopped under the runner’s hold with no '
         'certificate read, and the theorem is carried with its tree state; b723’s row stands in b680’s form and the chain’s verify reads %s.' % (
             f['on_word'], f['on_computed'], f['on_zeros'], ons, num_word(carried_n), f['dl_word'], f['dl_products'].replace("'", ''),
             f['dl_spread'], f['dl_bar'], f['it_word'], f['it_read'], f['it_zeros'], f['it_excl'], f['c2_mirror'],
             ', '.join('%s %s' % x for x in chain)), '',
         '*Filed at b725 on the author’s ruling `(R335)` and its addendum (8)-(10); %d question%s put before the root. Banks: relay '
         '`data/b725_corrigendum.txt`, `data/b725_standing_v150.txt`, `data/b725_root_row.txt`, `data/b725_rescope.txt`, '
         '`data/b725_registrations.txt`, `data/b725_price.txt`, `data/b725_stop_rule.txt`, `data/b725_onset_mass_control.txt`, '
         '`data/b725_onset_mass_rule.txt`, `data/b725_onset_mass.txt`, `data/b725_dial.txt`, `data/b725_interference.txt`, '
         '`data/b725_lambda2.txt`, `data/b725_c2.txt`, `data/b725_dispatch_rows.json`, `data/b725_reproduce.txt`, `data/b725_address_scan.txt`, '
         '`data/b725_touch.txt`, `data/b725_standing_figures.txt`, `data/b725_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R335)(1)-(2), N2, `%s`, `%s`, `%s`, `%s`): b724 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b724’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b725_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after: the short names, the plant needle, the legacy copy '
         'and the mirror citations (relay data/b725_standing_v150.txt); the three RE-SCOPE orders read, %s, each trigger written, for the '
         'root’s prompt (relay data/b725_rescope.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v150_ctl'], f['v150_cases'],
             f['v150_wanted'], ', '.join('%s %s' % x for x in f['rs'])), '',
         '**b723’s row** ((R335)(2), `%s`): standing in b680’s form at act_roots :%s (written at b724) and read by the chain’s reader; verify reads %s; the bytes '
         'b723’s root hashed rebuilt, %s, and no commit carries them, so no row turns b723 to AGREE; routes (A) and (B) for the author at the '
         'root’s prompt, none taken (relay data/b725_root_row.txt).' % (K.C1_RELAY[:8], f['rr_row'], f['rr_verify'], f['rr_bytes']), '',
         '**The registrations** ((R335)(3), N2, `%s`, then %s): data/b725_registrations.txt committed alone before any figure; H-INTERFERENCE '
         '((R335)(9)) and H-DIAL’s build reading and c = 1.0 amendment each committed before any figure at it, the order printed by ancestry in '
         'N2; the price table %s, the close %s h, the budget %s h; the stop rule read at each item’s start (relay data/b725_price.txt, '
         'data/b725_stop_rule.txt).' % (K.C2_RELAY[:8], ', '.join('`%s`' % c for c in K.C2_AMEND), f['pr_rows'], f['pr_close'], f['pr_budget']), '',
         '**H-ONSET-MASS** ((R335)(4)(i), (8)): the rule walked and selected %s zeros before any onset (relay data/b725_onset_mass_rule.txt); '
         'the five-zero control, POST HOC, read M/A < 1 at every radius, so a*_pred = log 4 at every zero (relay '
         'data/b725_onset_mass_control.txt); %s; %s; the hypothesis %s, no successor registered -- the banked products and these onsets are '
         'the data a successor is written from (relay data/b725_onset_mass.txt).' % (f['on_zeros'], ons, brk, f['on_word']), '',
         '**H-DIAL** ((R335)(4)(ii), `308326d8`): the controls (c0) and (id) as wanted, the onsets at c = 0.6, 0.8, 1.0 computed %s of 3 on '
         'b707’s template at zeta’s lowest ordinate; the products (c/2) a* %s, mean %s, spread %s against %s: the hypothesis %s (relay '
         'data/b725_dial.txt).' % (f['dl_onsets'], f['dl_products'].replace("'", ''), f['dl_mean'], f['dl_spread'], f['dl_bar'], f['dl_word']), '',
         '**H-INTERFERENCE** ((R335)(9)): the identities (C1) exact to n = 3000 and (C2)-(C4) as wanted before any figure; at %s of %s '
         'certified off-line zeros of Z_Q0 (discriminant -23, Q0 = x^2 + xy + 6y^2) to height 445, Z_Q1 (Q1 = 2x^2 + xy + 3y^2) excludes 0 '
         'beyond its ball at %s -- the hypothesis %s at %s of %s zeros, each such '
         'zero a cancellation zeta_K(rho) = -2 L(rho, psi); the |Z_Q1| table read beside, not a test (relay data/b725_interference.txt).' % (
             f['it_read'], f['it_zeros'], f['it_excl'], f['it_word'], f['it_read'], f['it_zeros']), '',
         '**lambda_2** ((R335)(4)(iii), N1, N5): on keiper-b725 (`%s`), two dispatches each read by its run id -- the first failing at one step '
         '(defect (r)), the second (run %s) building: the closed form LiCoeff 2 = 1 + gamma - log 4 pi - gamma^2 - 2 Re gamma_1 + pi^2/8 and the '
         'sign compiled with the standard three, no sorryAx, on two named premises, %s, both printed as sorry-free statements of what remains; '
         'graded DERIVES %s, INTERFACES %s (relay data/b725_lambda2.txt, data/b725_dispatch_rows.json).' % (
             f['l2_tip'], f['l2_run'], f['l2_premises'], f['l2_derives'], f['l2_interfaces']), '',
         '**The C2 theorem** ((R335)(4)(iv), N1, N5): the statement graded E0 DERIVES before any proof; route (B) mirrored against the '
         'statement’s own values, equal at %s of 18 fields; on c2-b725 (`%s`), the third and last dispatch (run %s): the build stopped under '
         'the runner’s hold with exit 143 and no log line, its memory falling through four kernel checks to %s MB; certificates by decide '
         '+kernel read %s of 18; carried with its tree state: %s remain, a memory-bounded route priced, not registered (relay data/b725_c2.txt, '
         'data/b725_dispatch_rows.json).' % (
             f['c2_mirror'], f['c2_tip'], f['c2_run'], f['c2_low'], f['c2_certs'], f['c2_remains'].replace('THE 18 CERTIFICATES', 'the 18 certificates')
             .replace('THE THEOREM', 'the theorem')), '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b725_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R332)(9), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b725_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b725_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b725 -- %s, %s, %s, %s -- against b724’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b725_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed; over the addendum %s cites, %s OK, '
         'the %s miss (a route phrase for Z_Q1) struck by the author’s word and closed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', f['acit_n'], f['acit_ok'], num_word(int(f['acit_miss'])),
             checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): H-DIAL and H-INTERFERENCE meet at the off-line zero -- the dial’s onsets do not scale '
         'as one product (c/2) a*, and at every certified off-line zero of Z_Q0 to height 445 the non-principal form does not vanish, so each is a '
         'cancellation between zeta_K and L(s, psi), not a zero of either; lambda_2 and the C2 theorem meet at what a kernel run leaves -- the '
         'one built on two named premises, the other stopped under the hold, each carried at the line where it fell short.', '',
         '**Carried to:** %s, each from its bank: H-ONSET-MASS’s carried zeros with their ladder brackets, and its successor written from the '
         'banked onsets at b726 or later (relay data/b725_onset_mass.txt); lambda_2’s two premises (relay data/b725_lambda2.txt); the C2 '
         'theorem’s certificates, (L1) and (L2) at c2-b725, a memory-bounded route priced (relay data/b725_c2.txt); b723’s routes (A) and (B) '
         'and the three RE-SCOPE orders as the author rules them; the six orders of (R335)(10), entered with the trail and none acted on; the '
         'instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b724():
    """b724's form over b724's objects, kept for the record and not called (Component 4)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 4, the Edit tool, over b725's objects; b724's composer over b724's objects kept below as _trail_text_b724,
    not called, and in git at b724's record tool); (R335)(10)'s six orders entered, each line carrying the addendum's sentence, then the
    open-orders line written from tools/standing/orders.py's output over the trail at HEAD with those lines beneath it, each of the six read
    OPEN by the generator's rule."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    six = _six_lines()
    op = ORD.report(ORD.read(ORD.trail('HEAD') + six), 'HEAD')[1]
    shut = [n for n in SIX_ORDERS if n not in op]
    if shut:
        sys.exit('### THE TRAIL: (R335)(10)`S ORDERS NOT OPEN BY THE GENERATOR`S RULE OVER THEIR LINES: %s -- NOTHING COMPOSED' % shut)
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R335) ratified.** With its addendum (8)-(10); its components as the ferry orders them (relay data/b725_ferry.txt, '
             'data/b725_addendum.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b724’s weight), :%s (the corrigendum), :%s (the entry); no ERRATA; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders entered** ((R335)(10); none acted on, no result claimed by any entry; %d):' % len(six), '']
    rows_ += six + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the line above from tools/standing/orders.py`s '
             'output; the three RE-SCOPE orders read, %s, each trigger written, for the author’s word (relay data/b725_rescope.txt).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + six)), ', '.join('%s %s' % x for x in f['rs'])), '',
             '**The carried items and b723’s row:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b725_standing_v150.txt); '
             'b723’s row in b680’s form at act_roots :%s, verify %s, routes (A) and (B) for the author (relay data/b725_root_row.txt).' % (
                 f['ver'], f['v150_cases'], f['v150_wanted'], f['rr_row'], f['rr_verify']), '',
             '**The registrations:** relay data/b725_registrations.txt at `%s`, its amendments %s, each before any figure at it.' % (
                 K.C2_RELAY[:8], ', '.join('`%s`' % c for c in K.C2_AMEND)), '',
             '**H-ONSET-MASS:** %s at %s of %s zeros; %s (relay data/b725_onset_mass.txt; the five-zero control POST HOC, '
             'data/b725_onset_mass_control.txt).' % (f['on_word'], f['on_computed'], f['on_zeros'],
                                                    '; '.join('%s carried, not computed' % z for z, _b in f['on_brackets']) or 'none carried'), '',
             '**H-DIAL:** %s, the products (c/2) a* %s, spread %s against %s (relay data/b725_dial.txt).' % (
                 f['dl_word'], f['dl_products'].replace("'", ''), f['dl_spread'], f['dl_bar']), '',
             '**H-INTERFERENCE:** %s at %s of %s zeros, Z_Q1 excluding 0 at %s (relay data/b725_interference.txt).' % (
                 f['it_word'], f['it_read'], f['it_zeros'], f['it_excl']), '',
             '**lambda_2:** on keiper-b725 (`%s`), run %s, compiled with the standard three on two named premises, printed as what remains; '
             'of its declarations %s derive and %s interface (relay data/b725_lambda2.txt).' % (f['l2_tip'], f['l2_run'], f['l2_derives'], f['l2_interfaces']), '',
             '**The C2 theorem:** E0 DERIVES; the route equal at %s of 18; on c2-b725 (`%s`), run %s stopped under the runner’s hold at %s MB, '
             'certificates read %s of 18; carried with its tree state (relay data/b725_c2.txt).' % (
                 f['c2_mirror'], f['c2_tip'], f['c2_run'], f['c2_low'], f['c2_certs']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b725_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b725_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b725_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b725 `%s` (previous `%s`, b724’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b725_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b725_standing_v150.txt); the standing '
             'report tool (relay data/b725_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; SIDE-explicit-formula’s %s, each cut from main `%s`, the act’s %d '
              'dispatches each read by its run id (relay data/b725_dispatch_rows.json); the %s branches as b724 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  ' and '.join('%s at `%s`' % (b, t[:8]) for b, t in K.EF_BRANCHES), K.EF_BASE[:8], len(K.EF_RUNS), K.REBUILD_BRANCH,
                  K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b725_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b724’s %s, %s, %s, %s (relay data/b725_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b725_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b724():
    """b724's trail record over b724's objects, kept for the record and not called (Component 4)."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R335)(4)(iii)-(iv)`s three, each by `gh workflow run build-module.yml`; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: three, each read by its id; MEASURED off data/b725_dispatch_rows.json against the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b725*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches cut on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### (R335)(4)(iii)-(iv), N5: keiper-b725 and c2-b725, each from main badaccc; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b724 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b724`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b725*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b724`s; MEASURED off each branch against its pin.'),
    ('Lean files written on SIDE-explicit-formula`s two branches', 'EFLEAN', 'EFLEAN', 'files', '### (R335)(4)(iii)-(iv): KeiperTwo.lean on keiper-b725, C2Walk.lean on c2-b725; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: no main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R335)(5): relay push-b724-closing, push-b724-preroot, push-b724-record; PLACE-papers push-b724-preroot, push-b724-record; each local, by name, after --merged listed it (data/b725_stepzero.txt :19-:20).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: the branches carry their Lean files and print_targets.txt alone, the workflow main`s.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b724`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R335) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (a6d363b6) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R335)(1)-(2): FINDINGS :11683.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R335)(1)-(2): one row, b724`s (45).'),
    ('root-chain corrigendum rows written', 0, 0, 'rows', '### none: b723`s row read at data/act_roots.txt :102 as b724 wrote it ((R335)(2)); no second root line.'),
    ('orders entered with the trail', 6, 6, 'orders', '### (R335)(10): the six, each with its sentence, none acted on.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b725_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R335)(2)-(4), (9): the price table, v1.5.0`s controls, b723`s row, the RE-SCOPE reads, the stop rule, H-ONSET-MASS`s control, rule and onsets, H-DIAL, H-INTERFERENCE, lambda_2, the C2 theorem, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 1, 1, 'commits', '### (R335)(3): 22210d4b, its one file data/b725_registrations.txt; its amendments 390b7894, 706b4ca1, 2531aad5 and dc0d4133, each before any figure at its object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### N2: the onset bank and its units, H-DIAL`s and its units, H-INTERFERENCE`s, lambda_2`s, the C2 bank and the dispatch rows; MEASURED off each bank`s first commit against 22210d4b.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 2, 2, 'modules', '### (R335)(4)(iii)-(iv): SIDEExplicitFormula/KeiperTwo.lean on keiper-b725, SIDEExplicitFormula/C2Walk.lean on c2-b725.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R335)(2): tools/standing/ to v1.5.0 -- the short names, the plant needle, the legacy copy and the mirror citations, each with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 2, 2, 'banks', '### data/act_current.json at step zero; data/b675_corrigenda.txt`s row (45), appended; data/act_roots.txt written by the root alone; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation, push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R332)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b725_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs, the three dispatches and the run reads ((R335)(4)(iii)-(iv)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### N2 (Component 4, the Edit tool): the figure banks of the registered objects, each first committed after the registrations
    fig_banks = [p for p in ('data/b725_onset_mass.txt', 'data/b725_onset_mass_units.jsonl', 'data/b725_dial.txt', 'data/b725_dial_units.jsonl',
                             'data/b725_interference.txt', 'data/b725_lambda2.txt', 'data/b725_c2.txt', 'data/b725_dispatch_rows.json')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=jcount('b725_dispatch_rows.json', lambda j: len([x for x in j if x.get('kind') == 'read'
                                                                            and int(x.get('run') or 0) in set(int(r) for _i, r in K.EF_RUNS)])),
                    REPROWS=jcount('b725_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b725_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('price', 'standing_v150', 'root_row', 'rescope', 'stop_rule', 'onset_mass_control', 'onset_mass_rule',
                                               'onset_mass', 'dial', 'interference', 'lambda2', 'c2', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b725_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b725_registration_%s.txt -- b725, THE RESEARCH ACT: b724 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.5.0 AND "
                             "b723`S ROW; THE REGISTRATIONS; H-ONSET-MASS, H-DIAL AND H-INTERFERENCE; lambda_2 ON keiper-b725 AND THE C2 "
                             "THEOREM ON c2-b725, THREE DISPATCHES AT MOST, UNDER (R335)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b724's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten at Component 4: b724's lines (the
lv negation, v1.4.0, the triage, b724's corrigendum row, the reproduction, the ledger split, the legacy imports) read banks this act does
not write, and are not carried; the lines are b725's: lambda_2 on keiper-b725 and the C2 theorem on c2-b725, each run by its id (KERNEL),
tools/standing/ v1.5.0 by its controls (CERTIFIED), H-ONSET-MASS, H-DIAL, H-INTERFERENCE and b723's row (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b725's lines (Component 4, the Edit tool), each from the record tool's figures over b725's banks
    # ------------------------------------------------------------------ KERNEL: lambda_2 ((R335)(4)(iii)) and THE C2 THEOREM ((R335)(4)(iv)),
    # ------------------------------------------------------------------ each run read by its id (N1: no lean on the host, three dispatches)
    sk = seat('%s_lambda2.txt' % ACT, '**lambda_2 > 0 -- ')
    keys['L2'] = ('KERNEL -- lambda_2 ON keiper-b725 (%s): the closed form and the sign compiled with the standard three, no sorryAx, run %s read '
                  'by its id, on two named premises printed as what remains (%s); DERIVES %s, INTERFACES %s; dispatches %s of 3; no main, no tag. '
                  'SOURCE %s.' % (f['l2_tip'], f['l2_run'], f['l2_premises'], f['l2_derives'], f['l2_interfaces'], f['l2_dispatches'], sk['text']))
    seats.append(sk)
    sk = seat('%s_c2.txt' % ACT, '**THE C2 THEOREM: ')
    keys['C2'] = ('KERNEL -- THE C2 THEOREM ON c2-b725 (%s): the statement E0 DERIVES, route (B) equal at %s of 18; run %s read by its id, the '
                  'build stopped under the runner`s hold at %s MB, certificates read %s of 18; carried with its tree state, %s remaining; '
                  'dispatches %s of 3; no main, no tag. SOURCE %s.' % (
                      f['c2_tip'], f['c2_mirror'], f['c2_run'], f['c2_low'], f['c2_certs'], f['c2_remains'], f['c2_dispatches'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.5.0 ((R335)(2)), by its controls (N2)
    sw = seat('%s_standing_v150.txt' % ACT, '**v1.5.0: CONTROLS ')   # ### appended by the template after this section
    keys['V150'] = ('CERTIFIED -- tools/standing/ v1.5.0: the short names, the plant needle, the legacy copy and the mirror citations, controls '
                    '%s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v150_ctl'], f['v150_cases'], f['v150_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: H-ONSET-MASS ((R335)(4)(i), (8)); H-DIAL ((R335)(4)(ii));
    # ------------------------------------------------------------------ H-INTERFERENCE ((R335)(9)); b723'S ROW ((R335)(2))
    so = seat('%s_onset_mass.txt' % ACT, '**H-ONSET-MASS: ')
    keys['ONSET'] = ('REGISTERED -- H-ONSET-MASS: %s at %s of %s zeros computed, within 0.05 %s; carried, not computed: %s; the five-zero control '
                     'POST HOC; no successor registered. SOURCE %s.' % (
                         f['on_word'], f['on_computed'], f['on_zeros'], f['on_within'],
                         ', '.join(x for x in (f['on_beyond_names'], f['on_notrun_names']) if x != 'none') or 'none', so['text']))
    seats.append(so)
    sd = seat('%s_dial.txt' % ACT, '**H-DIAL: ')
    keys['DIAL'] = ('REGISTERED -- H-DIAL: %s, onsets %s of 3 at c = 0.6, 0.8, 1.0, the products (c/2) a* %s spreading %s against %s. SOURCE %s.' % (
        f['dl_word'], f['dl_onsets'], f['dl_products'].replace("'", ''), f['dl_spread'], f['dl_bar'], sd['text']))
    seats.append(sd)
    si = seat('%s_interference.txt' % ACT, '**H-INTERFERENCE: ')
    keys['ITF'] = ('REGISTERED -- H-INTERFERENCE: %s at %s of %s certified off-line zeros of Z_Q0 to height 445, Z_Q1 excluding 0 at %s. '
                   'SOURCE %s.' % (f['it_word'], f['it_read'], f['it_zeros'], f['it_excl'], si['text']))
    seats.append(si)
    sc = seat('%s_root_row.txt' % ACT, "**b723'S ROW IN b680'S FORM: ")
    keys['ROOTROW'] = ('REGISTERED -- b723`S ROW: standing at act_roots :%s in b680`s form; verify %s; the hashed bytes rebuilt (%s), no commit '
                       'carrying them; routes (A) and (B) for the author. SOURCE %s.' % (f['rr_row'], f['rr_verify'], f['rr_bytes'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R335)(6))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['L2', 'C2']), ('CERTIFIED', ['V150']), ('REGISTERED', ['ONSET', 'DIAL', 'ITF', 'ROOTROW']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b725 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
