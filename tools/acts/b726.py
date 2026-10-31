# -*- coding: utf-8 -*-
# b726 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R336)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R336)(2) repair it carries. Edited by the Edit tool. Carried at b726 by tools/b726_fold.py (`carry`) from tools/acts/b725.py,
# b725`s names substituted; the citation`s sections adopted from tools/b726_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b725`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b725`s carried till
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
# ### b726, Component 1 (the Edit tool): THE c1 ROUTE FOR b725'S WEIGHT LINE AND ITS CORRIGENDUM, (R336)(1)-(2). Carried from b725's
# ### override and rewritten here against b725's own banks: the closing's lines by needle, the events (10), the defects (28), the refusals
# ### (9 at e2246a8e), the v1.6.0 controls. `c1 weight|corrigendum [dry|write]`;
# ### dry prints the text and the screens and writes nothing; any needle that does not meet its line once: nothing composed.
#⟪OVERRIDE record 1428 1435 REPAIR (c1)⟫
C1_PREV_CLOSE = 'e2246a8e'          # ### b725's closing commit (relay main at b726's step zero): its refusal bank read at it
C1_NOTED = '2026-10-30'
C1_CORRIGENDA_LAST = 45
C1_V140 = 'b726_standing_v160.txt'  # ### the name kept for the routes below: b726's controls bank is v1.6.0's
C1_WEIGHT_HEAD = '*Appended 2026-10-30 by b726 to b725’s entry (:%d), under `(R336)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## H-ONSET-MASS at 1 of 3 zeros REFUTED, two carried; H-DIAL at c = 0.6, 0.8, 1.0 REFUTED'
C1_TRAIL_NEEDLE = '### b725 — lane two, act one hundred and fifty-two, the research act under (R335)'
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
    for l in _c1_rd('b725_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b725_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_weight():
    c = 'b725_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    q = re.search(r'^\(1\) b725 AT ITS WEIGHT\. Its closing head line, quoted from data/b725_closing\.txt :1 as the public relay carries it at '
                  r'e2246a8e: "([^"]+)"', _c1_rd('b726_ferry.txt'), re.M)
    if not q or q.group(1) != head:
        sys.exit('### data/b725_closing.txt :1 IS NOT THE HEAD LINE (R336)(1) QUOTES -- NOTHING COMPOSED')
    steps = json.load(open(os.path.join(D, 'b725_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or clo[-1:] != [C1_PREV_CLOSE] or K.B714_RECORD[:8] not in head:
        sys.exit('### data/b725_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    (cc, cd, rp, rn), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+)$', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    (gi, gc, gl, gr), l_cg = _c1_fl(c, r'ITEMS (\d+): EVENTS 18, DEFECTS 19 ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ;', 'the corrigendum for b724')
    (vc,), l_v = _c1_fl(c, r'v1\.5\.0: CONTROLS .* ; CASES (\d+) ; AS WANTED \1 ; ALL AS WANTED', 'v1.5.0`s controls')
    _x, l_rw = _c1_fl(c, r"b723'S ROW IN b680'S FORM: STANDING AT :102, READ BY THE CHAIN'S READER \(corrected 1\) ; VERIFY b722 AGREE, b723 DISAGREE \(ONE BANK\)", 'b723`s row')
    (ni,), l_in = _c1_fl(c, r'H-INTERFERENCE: \(C1\) AS WANTED ; \(C2\)-\(C4\) AS WANTED ; ZEROS (\d+) ; READ \1 ; Z_Q1 EXCLUDES 0 AT \1 ; THE HYPOTHESIS HELD', 'H-INTERFERENCE')
    _x, l_on = _c1_fl(c, r'H-ONSET-MASS: C1 AS WANTED ; ZEROS 3 ; ONSETS COMPUTED 1 ; WITHIN 0\.05 0 ; BEYOND REACH 0 ; NOT RUN 2 ; THE HYPOTHESIS REFUTED', 'H-ONSET-MASS')
    _x, l_di = _c1_fl(c, r'H-DIAL: \(c0\) AS WANTED ; \(id\) AS WANTED ; ONSETS 3 OF 3 ; THE HYPOTHESIS REFUTED', 'H-DIAL')
    (lc_, lr_), l_la = _c1_fl(c, r'lambda_2 > 0 -- NOT COMPILED OUTRIGHT: .*keiper-b725 \(([0-9a-f]{8}), RUN (\d+)\) WITH THE STANDARD THREE, NO sorryAx, ON TWO NAMED PREMISES', 'lambda_2')
    (cc_, cr_, cl_), l_c2 = _c1_fl(c, r'THE C2 THEOREM: E0 DERIVES ; .*ON c2-b725 \(([0-9a-f]{8}), RUN (\d+)\) THE BUILD STOPPED .*LOW (\d+) MB.*CERTIFICATES BY decide \+kernel 0 OF 18 READ', 'the C2 theorem')
    (ap_,), l_ad = _c1_fl(c, r'PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; PLACES (\d+) ; CONTROLS 4 OF 4 AS WANTED ;', 'the name and address')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) '
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (ca, cb), l_cl = _c1_fl(c, r'^\s*pre-push, \(R335\)\(2\) : THE CLAIM ARMS PASSING (\d+) OF (\d+) \(failing ', 'the claim arms')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    (msha,), l_mi = _c1_fl(c, r'^### THE MIRROR .*mirror-refresh-2026-10-30-b725\.zip ; \d+ bytes ; sha256 ([0-9a-f]{16}) ; .*Act root: b725 '
                           + K.B714_ROOT + r' ; CLEAN ON ALL THREE CLAUSES', 'the mirror')
    (np_,), l_an = _c1_fl(c, r'^### THE AUTHOR`S ANSWERS AND WORDS .*: (\d+) prompt\(s\) put by the seat', 'the prompts')
    n4 = (json.load(open(os.path.join(D, 'b725_scores_close.json'), encoding='utf-8')).get('scores') or {}).get('N4') or \
        json.load(open(os.path.join(D, 'b725_scores_close.json'), encoding='utf-8')).get('N4')
    if not n4 or n4[0] != 'REFUTED':
        sys.exit('### data/b725_scores_close.json: N4 %s -- NOTHING COMPOSED' % (n4,))
    # ### each figure (R336)(1) cites, read at its bank and line, not trusted
    for bank, line, needle in (('b725_onset_mass.txt', 14, 'at a = 10.20248033'), ('b725_onset_mass.txt', 12, 'a*_pred 1.386294361'),
                               ('b725_onset_mass.txt', 22, 'FIRED at [\'off18\']'), ('b725_onset_mass.txt', 8, '6.838396011'), ('b725_onset_mass.txt', 9, '10.38532711'),
                               ('b725_dial.txt', 33, 'at a = 3.039966598'), ('b725_dial.txt', 35, 'at a = 2.888826162'),
                               ('b725_dial.txt', 37, 'rung16 (grid point 17 of 393 in (log2, 32]) at a = 2.772588722'),
                               ('b725_dial.txt', 39, "['0.911990', '1.155530', '1.386294']"), ('b725_interference.txt', 106, 'Z_Q1 EXCLUDES 0 AT 69')):
        if needle not in _c1_rd(bank).split(NL)[line - 1]:
            sys.exit('### data/%s :%d DOES NOT CARRY %r -- NOTHING COMPOSED' % (bank, line, needle))
    ar = json.load(open(os.path.join(D, 'b725_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b725_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 11)) or len(dr) != 28:
        sys.exit('### EVENTS %s ; DEFECTS %d -- NOTHING COMPOSED' % (sorted(ev), len(dr)))
    return (C1_WEIGHT_HEAD + ' -- b725 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b725_closing.txt):* “%s” (data/b725_closing.txt :1); its '
            'relay commit the record’s %s, the closing’s %s (data/b725_steps.json, the record and closing rows). As its rows read: '
            'H-INTERFERENCE HELD, Z_Q1 excluding 0 at %s of %s certified off-line zeros of Z_Q0 to height 445 (:%d; data/b725_interference.txt '
            ':106); H-ONSET-MASS REFUTED at off18, a* = 10.20248033 against a*_pred = log 4, the two remaining zeros not run (:%d; '
            'data/b725_onset_mass.txt :14, :22); H-DIAL REFUTED, onsets a*(0.6) = 3.039966598, a*(0.8) = 2.888826162, a*(1.0) = 2.772588722, the '
            'products 0.912, 1.156, 1.386 (:%d; data/b725_dial.txt :33-:39); lambda_2 > 0 INTERFACES on two named premises on keiper-b725 (%s, '
            'run %s read by its id) (:%d); the C2 theorem DERIVES at its statement, its one build stopped under the runner’s hold (low %s MB, run '
            '%s, %s on c2-b725), 0 of 18 certificates read, carried (:%d); the six orders of `(R335)`(10) entered (OPEN_TRAILS :16589-:16594); the '
            'local user.email of five clones set to the noreply form on the author’s word (data/b725_events.txt row (2)). The corrigendum for '
            'b724 at %s items, CLAIM %s, CLOSE %s, REPEAT %s, and v1.5.0’s %s controls AS WANTED (:%d, :%d); b723’s row read at act_roots :102, '
            'verify b723 DISAGREE on one bank (:%d), since carried on its branch below; the name and address 0 and 0 (:%d, %s places). The sealed '
            'tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push, NOT CLEAN both, the claim arms %s of %s (:%d, :%d, :%d); '
            'the counter CLAIM %s, CLOSE %s, REPEAT %s of %s (:%d); N4 REFUTED, the rest HELD, 7 of 8 (data/b725_scores_close.json). The root %s over '
            '%s banks, chained from %s (data/b725_act_root.json; :%d); the mirror (sha256 %s…) CLEAN on all three clauses with the root line '
            '(:%d); %s prompts answered (:%d); %d events in data/b725_events.txt, rows (1)-(%d), the tenth filed after the closing’s counter; %d '
            'defects, (a)–(z), (a’), (b’) (data/b725_defects.txt). Nothing deposited, nothing published; the corrigendum for these rows follows, under '
            '`(R336)`(1)-(2).' % (
                head, K.B714_RECORD[:8], C1_PREV_CLOSE, ni, ni, l_in, l_on, l_di, lc_, lr_, l_la, cl_, cr_, cc_, l_c2, gi, gc, gl, gr, vc, l_cg, l_v,
                l_rw, l_ad, ap_, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], ca, cb, l_pre, l_post, l_cl, cc, cd, rp, rn, l_cn,
                K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, msha, l_mi, np_, l_an, len(ev), max(ev), len(dr))
            + NL + NL + C1_OBSERVATION)


# ### (R336)(1): an observation, POST HOC, entered with its banks and no hypothesis; no sentence calls it a law
C1_OBSERVATION = ('*An observation of b725’s runs, POST HOC and not a law, entered under `(R336)`(1) with its banks and no hypothesis:* the '
                  'size-broken control’s onsets sit at the ladder’s foot, 2.77 to 3.04 across c = 0.6 to 1.0, with a*(1.0) at the rung log 16 exactly '
                  '(relay data/b725_dial.txt :33-:37), while Q0’s cosh failures onset at 6.84 to 10.39 and rise with gamma (data/b725_onset_mass.txt '
                  ':8, :9, :14). The onset’s place on the ladder separates the two mechanisms in these runs.')
# ### the refusals: b725's bank at its closing commit, one a line, and the row recording each (line, kind, time, row)
C1_REFUSALS = [(1, 'READ', '13:42:02Z', 'defect (b)'), (2, 'PIPE', '14:07:06Z', 'defect (f)'), (3, 'PIPE', '14:14:34Z', 'defect (g)'),
               (4, 'READ', '14:25:23Z', 'defect (k)'), (5, 'PIPE', '16:21:51Z', 'defect (q)'), (6, 'REDIR', '17:02:55Z', 'defect (s)'),
               (7, 'REDIR', '17:30:13Z', 'defect (t)'), (8, 'READ', '18:16:54Z', 'defect (u)'), (9, 'READ', '18:29:25Z', 'defect (v)')]
C1_CORR_TITLE = ('## Corrigendum to b725’s record (relay data/b725_events.txt rows (1)-(10) and data/b725_defects.txt): ten events and '
                 'twenty-eight defects, each CLAIM or CLOSE and NEW or REPEAT; a dated note, in this section, naming the line that reads stale; '
                 'G-CLOSING-SENTENCE and G-RULE-SCORES-BEFORE-SEAL repaired at tools/standing/ v1.6.0, each controlled on b725’s banks; b723’s row '
                 'carried on its branch, under (R336)(1)-(2)')
C1_CONFIG_FIX = ('true of the act’s kernel commits, all made before the author’s word at b725’s root, and stale as of the close: on that word the local '
                 'user.email of five clones, SIDE-explicit-formula among them, was set to the noreply form (relay data/b725_events.txt, rows (2) and '
                 '(10); OPEN_TRAILS :16644). The sentence stands as written')
C1_NOTES = [
    ('the closing’s kernels paragraph, event (10)’s stale parenthesis', None, 'data/b725_closing.txt', 352, 'the local configuration not edited', 'READS STALE', 'config'),
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
    fixes = dict(config=C1_CONFIG_FIX)
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
    rl = _c1_git('show', '%s:data/b725_hook_refusals.txt' % C1_PREV_CLOSE).replace(chr(13), '').strip(NL).split(NL)
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
    (cc, cd), _l = _c1_fl('b725_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V140)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.6.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=_c1_notes())
    nc, nl_, _rep, _n = _c1_counts(s)
    # ### the closing's counter read 37 items: event (10) is about the closing and was filed after it, a CLOSE, so CLOSE reads one more here
    bad = [k_ for k_, ok_ in (('the event rows (1)-(10)', sorted(ev) == list(range(1, 11))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 28', len(dr) == 28), ('the refusals 9, each answered as listed', len(rl) == 9 and not bad_ref),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.6.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter the closing`s (CLAIM %s, CLOSE %s) with event (10) added' % (cc, cd), (nc, nl_) == (int(cc), int(cd) + 1))) if not ok_]
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


# ### the repairs each event or defect is met by at v1.4.0 (the ten classes of (R336)(2) and the root route)
C1_EV_EXTRA = {1: '; this act’s face writes the arm’s words', 2: '; the rule stands, this act one git write per message',
               5: '; repair (closing)', 7: '; the two plants still inert, no clause of (R336) orders their repair, carried',
               8: '; repair (scores)', 10: '; the dated note above'}
C1_DF_EXTRA = {}
C1_REFUSAL_LETTERS = set(row.split('(', 1)[1].rstrip(')') for _l, _k, _a, row in C1_REFUSALS if row.startswith('defect'))
C1_CLASSES = (
    ('closing', 'G-CLOSING-SENTENCE (`(R336)`(2)(iii), event (5))', 'closing_sentence_ok reads the closing’s render unwrapped, so the sentence hard-wrapped '
                'between “in any” and “outbound” matches; the arm’s plant cut to “in any”, since the old plant changed nothing on a wrapped render'),
    ('scores', 'G-RULE-SCORES-BEFORE-SEAL (`(R336)`(2)(iii), event (8))', 'tools/rule_arms.py :458 reads the fold’s route `fold.py record scores` beside the '
               'old form: b725’s calls 0 on the old reader and 7 on the new, the first before the seal; a seal planted before every call fails it'),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v140_foot'])
    L = ['*b725’s events bank (relay data/b725_events.txt) carries ten rows, entered after its lock and not lettered, each tagged in its '
         'own bracket (%s); its defects bank twenty-eight lettered rows, (a)-(z), (a’), (b’), each tagged in its own bracket (%s); its '
         'refusal bank nine lines at b725’s closing commit %s, each recorded by a letter. Each item is tagged CLAIM, where it '
         'touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the '
         'banks’ own; this entry edits none of them.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_PREV_CLOSE), '',
         '**The dated note** (`(R336)`(2)(iv)), in the form `(R335)`(1) ruled, written in this act’s section, no line rewritten, the line named here by its '
         'place and number, dated %s:' % C1_NOTED, '']
    for x in s['notes']:
        L += ['- **%s :%d** (%s; written %s at %s; %s, noted %s): "%s" -- %s.' % (
            x['place'], x['line'], x['where'], x['written'], x['commit'], x['cls'], C1_NOTED, _c1_q(x['quote']), x['fix'])]
    L += ['', '**The repairs of `(R336)`(2)(iii), at tools/standing/ v1.6.0, each with a control on b725’s banks, failing on the route before the repair '
          'and passing after, both instances printed** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V140, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (:%d).' % (k_, name, what, _c1_v140_line('### (%s) ' % k_)), '']
    L += ['**b723’s row** (`(R336)`(2)(ii)): relay branch corrigendum-b723 (16caad10) off 2be0135c carries data/b723_bank_hashes.json at the bytes b723’s '
          'root hashed, sha 133004c8, and nothing else, pushed and read back, main untouched; the row appended at relay data/act_roots.txt :105 in '
          'b680’s form, no row edited; verify re-read b722 AGREE, b723 AGREE at 106 of 106 banks, b724 AGREE, b725 AGREE, after a first read '
          'failed on one remote read that the direct read then found equal (relay data/b726_root_row.txt). **The author’s word on user.name** '
          '(`(R336)`(2)(i)): banked at relay data/b726_author_words_preseal.txt, run at SIDE-grh-transfer and the patent repository, one git write per '
          'message, the scan’s PREVIOUS NAME arm 0 after.', '',
          '**b725’s events (1)-(10):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE NAVIGATOR'S|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_]).split(': ', 1)[0]
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b725_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s'), t, _c1_col(r), C1_EV_EXTRA.get(k_, '').replace('`', '’'))]
    L += ['', '**b725’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        extra = '; a hook refusal, its line below' if x in C1_REFUSAL_LETTERS else C1_DF_EXTRA.get(x, '')
        L += ['**(%s)** (relay data/b725_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c), extra)]
    L += ['', '**b725’s refusals** (relay data/b725_hook_refusals.txt at %s, one a line): ' % C1_PREV_CLOSE + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**The counter:** CLAIM %d, CLOSE %d over the %d items (ten events, twenty-eight defects); b725’s closing’s counter reads 37 items (relay '
          'data/b725_closing.txt :5), event (10) filed after it and a CLOSE; REPEAT %d of %d; the CLAIM items %s.' % (nc, nl_, n, rep, n, ', '.join(claims)), '',
          '*Filed at b726 on the author’s ruling `(R336)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 '
          'corrigendum`, the act’s override in relay tools/acts/b726.py) from b725’s events, defects and refusal banks read unedited, the '
          'lines noted read at their repositories’ HEAD, and the v1.6.0 controls bank; banked as relay `data/b726_corrigendum.txt`, the '
          'corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b725’s record; no sealed tool, face, trail or '
          'root-named bank of b725 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    return (['b726 -- THE CORRIGENDUM FOR b725, (R336)(1)-(2) (%s)' % utc(), '',
             '### the banks read unedited: data/b725_events.txt rows (1)-(10), data/b725_defects.txt 28 rows, data/b725_hook_refusals.txt 9 '
             'lines at %s; the noted lines at their repositories` HEAD; data/%s (the v1.6.0 controls); the corrigenda bank`s last row (%d).' % (
                 C1_PREV_CLOSE, C1_V140, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 10, DEFECTS 28 ; CLAIM %d, CLOSE %d ; REPEAT %d ; DATED NOTES %d ; v1.6.0: G-CLOSING-SENTENCE, '
               'G-RULE-SCORES-BEFORE-SEAL ; b723`S ROW ON ITS BRANCH ; THE ENTRY AT FINDINGS :%s.**' % (n, nc, nl_, rep, len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b725 at its weight after its entry, and the corrigendum for b725, landed through b698's guarded
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
                                                   notes=s['notes'], repairs=dict(version='v1.6.0', bank='data/' + C1_V140),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b726, Component 4 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S THREE DISPATCHES. The template's three
# ### runner functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b726 ran three
# ### ((R336)(4)(iii)-(iv), N1), rowed in data/b726_dispatch_rows.json. Replaced for b726 alone; the arms' names stand, their plants on b726's rows.
#⟪OVERRIDE checks 1126 1138⟫
def rebuild_wf_ok(S):
    """(R335)(7), as b725 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """(R336)(3), N1, b726: the per-field dispatches read by their run ids -- SIDE-explicit-formula's build-module.yml at main with the ref
    input, each at a commit of c2-b725 pushed with its remote equal before it, its run the worklist's EF_RUNS in order, each read once with the
    built ref its commit; dispatch 1 (c9add92f) BUILD EXIT 1, FAILS on the elaboration; every other at the repair, its tip; every KERNEL row
    exit 0 with its one axiom line printed and no sorryAx; the C2 bank's foot naming the count of dispatches."""
    rows = S['drows'] or []
    cm = [r for r in rows if r.get('kind') == 'commit']
    pu = [r for r in rows if r.get('kind') == 'push']
    dp = [r for r in rows if r.get('kind') == 'dispatch']
    rd_ = [r for r in rows if r.get('kind') == 'read']
    by = dict((str(r.get('run')), r) for r in rd_)
    runs = [str(r) for _i, r in K.EF_RUNS]
    ok = len(cm) == len(pu) == 2 and len(dp) == len(rd_) == len(runs) <= K.MAX_DISPATCHES \
        and runs == [str(r.get('run')) for r in dp] == [str(r.get('run')) for r in rd_] \
        and [r.get('sha') for r in cm] == [r.get('sha') for r in pu] and [r.get('sha') for r in dp] == [r.get('built_ref') for r in rd_] \
        and cm[1].get('sha') == K.EF_BRANCHES[1][1] and all(r.get('sha') == cm[1].get('sha') for r in dp[1:]) and dp[0].get('sha') == cm[0].get('sha') \
        and all(r.get('remote_equal') is True for r in pu) and all(r.get('at_ref') == 'main' and r.get('workflow') == 'build-module.yml' for r in dp) \
        and all(r.get('status') == 'completed' for r in rd_)
    r1 = by.get(runs[0]) or {}
    kn = [r for r in rd_ if r.get('verdict') == 'KERNEL']
    return ok and str(r1.get('build_exit')) == '1' and r1.get('verdict') == 'FAILS' and bool(kn) \
        and all(str(r.get('build_exit')) == '0' and r.get('sorryAx') is False and len(r.get('axioms_lines') or []) == 1
                and not any('sorryAx' in x for x in r.get('axioms_lines')) for r in kn) \
        and ('DISPATCHES %d OF 18' % len(runs)) in _vlast(S['c2'])
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
# ### b726, Component 6 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b725's record has eighteen
#⟪OVERRIDE checks 980 980⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 11)) \
#⟪END⟫
# ### b726, Component 4 (the Edit tool): b726's step-zero bank landed in the step-zero commit after the banks' (7afce313, STEPZERO_BANK_COMMIT),
# ### not in STEPZERO_BANKS (afea78a4); the arm reads it there. (b725's override of checks 526 -- no registration commit -- removed: b726
# ### registers at 22210d4b and the template's line reads it.)
#⟪OVERRIDE checks 751 751⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b726_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b726, Component 6 (the Edit tool): b726's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b725's wording
#⟪OVERRIDE checks 776 776⟫
        and 'THE DELETES, each after its --merged listing' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b726, Component 4 (the Edit tool): b725's overrides of checks 1516 and 1659 (hook.py edited by b725's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b726 as it stands
# ### b726, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks 985 985⟫
        and 'data/b726_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b726, Component 4 (the Edit tool): b725's override of checks 1476-1482 (one ERRATA entry at b725's (R335)(5)) removed -- (R336)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b726 as it stands
# ### b726, Component 6 (the Edit tool): G-BRANCHES-DELETED's needle 'KEPT' was b725's step-zero wording; b726's bank (committed
# ### d5432f23) writes "Kept: port-b707," (:16), read in its own wording
#⟪OVERRIDE checks 742 742⟫
        and 'port-b707' in z and 'KEPT as (R336)(8) lists them: port-b707' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b726, Component 4 (the Edit tool): G-RUNNER-READ's plant on b726's dispatch rows -- run 2's axiom lines carrying sorryAx (b725's
# ### plant read the lv rows' closure log, which b726 does not write)
#⟪OVERRIDE checks 1686 1686⟫
     lambda S: runner_ok(S), lambda S: put(S, 'drows', [dict(r, axioms_lines=['planted depends on axioms: [sorryAx]']) if r.get('verdict') == 'KERNEL' else r for r in (S['drows'] or [])])),
#⟪END⟫
# ### b726, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b726, Component 6 (the Edit tool): the fold bank was b725's own route
# ### (tools/b725_fold.py); b726's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b726_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks 1005 1005 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b725.py -> tools/acts/b726.py' in (rd('b726_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b726, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b726_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 256 263 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b726_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b726, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R336): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 339 340⟫
    rows = [l for n_ in ('b726_defects.txt', 'b726_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R336) Component 4, the act`s events and defects together; relay data/b726_defects.txt, data/b726_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b726, Component 4 (the Edit tool): the template's item (b) names an old order list by hand; b726's orders are (R336)(10)'s six,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-SILENT-SENTENCES DISCHARGED by (R336)(5)`s list, W-ORD-MECHANISM-TABLE',
    '        left OPEN for its fourth row, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b726, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b725's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b726_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b726_registration_%s.txt' % __import__('b726_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b726, Component 4 (the Edit tool, before the face): b725's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b726, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b726's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's two branches
#⟪OVERRIDE regspec 52 52⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b726, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R336)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b726 does not have
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)
#⟪END⟫
# ### b726, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b725's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b726 scorer reads; the needles set to the banks b726's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks 903 904 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_FIGURE_BANKS' in n and '_first_add(' in n \
        and "_onset_mass_control.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b726, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b725's ruling's form "port-b707 kept;", where (R336)(9)
# ### writes "kept: port-b707, …" (data/b726_ferry.txt :34), so the arm failed on the act's real deletes; both forms read as written
#⟪OVERRIDE checks 764 767 REPAIR (needle)⟫
    # ### (R335)(9) wrote "port-b707 kept;" and (R336)(9) writes "kept: port-b707, …"; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or bool(re.search(r'\bkept: [^.;]*\b%s\b' % re.escape(K.PORT_BRANCH), S['ferry']))) \
#⟪END⟫
# ### b726, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b726_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record 671 671 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuv'))   # ### (a)-(v), entered before the lock, every one the seat's (data/b726_defects.txt); a letter entered after them read beyond this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b726_price.txt', 'data/b726_corrigendum.txt', 'data/b726_standing_v160.txt', 'data/b726_root_row.txt',
                  'data/b726_edition_diff.txt', 'data/b726_frontdoors.txt', 'data/b726_zenodo_read.json', 'data/b726_mechanisms.txt',
                  'data/b726_beurling_read.txt', 'data/b726_c2.txt', 'data/b726_dispatch_rows.json',
                  'data/b726_author_words_preseal.txt', 'data/b726_reproduce.txt', 'data/b726_reproduce.json', 'data/b726_address_scan.txt',
                  'data/b726_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b726 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R336)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b726_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R336)(2)-(7), Component 6 (b725's keys over b725's objects in git at b725's suite): the components' order by ancestry; the price
        # ### table, v1.6.0's controls and b723's row (2); the edition (4); the front-door list and the LLM line (5)-(6); the mechanism table (7);
        # ### the C2 build per field on c2-b725, its dispatches by their rows (3); v8 and v9; the address scan; the reproduction under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### b725's registrations at their commit and at HEAD; b726 registers nothing
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v160', K.STANDING_COMMIT, K.C1_STANDING), ('v160_c1', K.C1_STANDING, K.C1_RELAY),
                                 ('c1_corr', K.C1_RELAY, K.C1_CORR), ('corr_c3', K.C1_CORR, K.C3_RELAY[0]), ('c3_c2', K.C3_RELAY[0], K.C2_RELAY))),
        price=rd('b726_price.txt'), v160=rd('b726_standing_v160.txt'), root_row=rd('b726_root_row.txt'),
        edition_diff=rd('b726_edition_diff.txt'), frontdoors=rd('b726_frontdoors.txt'), mechanisms=rd('b726_mechanisms.txt'), beurling=rd('b726_beurling_read.txt'),
        ws_now=_s(blob(PP, 'HEAD:day1/Which_Structure_Confines.md')) or None, ws_pre=_s(blob(PP, '%s:day1/Which_Structure_Confines.md' % PRE['pp'])) or None,
        ws_edition=_s(blob(PP, 'HEAD:day1/Which_Structure_Confines_v2_4_0.md')) or None,
        c2=rd('b726_c2.txt'), drows=json.loads(rd('b726_dispatch_rows.json') or '[]'),
        reproduce=rd('b726_reproduce.txt'), reproducej=jl('b726_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b726_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read THIS ACT'S per-field dispatches ((R336)(3), N1): the dispatch rows (commit, push, dispatch, read), the
        # ### C2 bank beside them; the wave 1 kernels' rebuild-b721 branches, main and tags as b725 left them (its axiom rows read for the
        # ### workflows there, no commit on those kernels this act)
        rebuild=rd('b726_c2.txt'), rebuild_rows=json.loads(rd('b726_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows: the act shift had moved this name to b725, which has no such bank (defect (y))
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
# ### b726's read-first bank's items by path, as its step zero wrote them (data/b726_readfirst.txt :15-:38)
READFIRST_NEEDLES = ('relay data/b725_closing.txt |', 'relay data/b725_events.txt |', 'relay data/b725_defects.txt |',
                     'relay data/b725_interference.txt |', 'relay data/b725_onset_mass.txt |', 'relay data/b725_dial.txt |',
                     'relay data/b725_root_row.txt |', 'relay data/b723_zetak.txt |', 'relay data/b723_c2_closed_form.txt |',
                     'relay data/b722_c2_price.txt |', 'relay data/b721_frozen_line.txt |', 'relay data/b721_frozen_line_drafts.txt |',
                     'PLACE-papers day1/Which_Structure_Confines.md |', 'PLACE-papers day1/A_Place_to_Stand.md |', 'PLACE-papers OPEN_TRAILS.md |',
                     'relay data/b726_ferry.txt |', 'relay data/standing_clauses_v9.txt |', 'relay tools/standing/VERSION | :1 v1.5.0 |',
                     'relay data/act_roots.txt |', 'relay data/b725_c2.txt |', 'relay data/b577_ferry.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R336)(1)-(2))', 'C2 BUILD PER FIELD ((R336)(3))', 'EDITION ((R336)(4))', 'FRONT-DOOR LIST AND THE LLM LINE ((R336)(5)-(6))',
                    'MECHANISM TABLE ((R336)(7))', 'NAME AND ADDRESS ((R332)(9))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (89 = 89 + 0, data/b726_citation_check.txt :98); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 89 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b725's figures, read at FINDINGS :11797 as Component 1 landed them
    return landed(S, 0, ['b725 AT ITS WEIGHT', 'suite 110 of 116; root d85513caeb001601…', 'the closing’s e2246a8e', '28 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b726's title in the ferry's Component 6 form adjusted to what the act did (the record tool's _title over the banks), cut at its objects
TITLE_NEEDLES = ('## Which Structure Confines v2.4.0 carrying the zeta_K figure and the closed form', '; the front-door list, 46 items, 3 load-bearing and 20 silent',
                 '; the LLM line read at 25 papers and READMEs, 23 differing', '; the C2 certificates compiled at ', ' of 18 fields', '; b723’s row carried on its branch, the chain AGREE',
                 '; the mechanism table’s 3 rows', '; the onset signature entered as an observation')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R336)(1)-(2): the generated entry for b725's ten events and twenty-eight defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(10), the defects by the one lettering ((a)-(z), (a'), (b')), no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 7, CLOSE 31 over 38, REPEAT 23); the repairs at tools/standing/ v1.6.0 by their controls
    bank; event (10)'s line READS STALE the one dated note; the corrigenda bank appended at row (46) and nothing before it changed; in
    Component 1's commits (the figures read from data/b726_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 28 and len(items) == j.get('items') == 38 and j.get('row') == 46 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 38 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 7 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 23 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.6.0' and (j.get('repairs') or {}).get('bank') == 'data/b726_standing_v160.txt' \
        and [n.get('cls') for n in (j.get('notes') or [])] == ['READS STALE'] \
        and '  (46) ' in S['corrigenda'] and '  (47) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b726_rules.txt and data/b727_rules.txt, by form in (R336)(8)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (the line above is b725's form, its names b726's); no author's word of b726 orders a rules row (its one word before the seal,
    data/b726_author_words_preseal.txt, is the user.name word and orders runs), so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b726_rules.txt')) and not os.path.exists(os.path.join(D, 'b727_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b726's keys, the report sections' own heads
REPORT_KEYS = ('KERNEL -- THE C2 CERTIFICATES ON c2-b725', 'CERTIFIED -- tools/standing/ v1.6.0', 'REGISTERED -- WHICH STRUCTURE CONFINES v2.4.0',
               'REGISTERED -- THE FRONT-DOOR LIST', 'REGISTERED -- THE LLM LINE', 'REGISTERED -- THE MECHANISM TABLE', 'REGISTERED -- b723`S ROW',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over THIS ACT'S per-field dispatches ((R336)(3), data/b726_dispatch_rows.json): every push, dispatch and read row with the
    host's free memory at or above the hold (each figure read as an integer); each dispatch with one push of its commit before it and one read
    of its run after it; the dispatches eighteen at most, none push-triggered; the capture's dispatch commands (gh workflow run
    build-module.yml at main with the ref input) one per dispatch row, at the rows' commits; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run build-module\.yml -R psinary-sketch/SIDE-explicit-formula --ref main '
                       r'-f ref=([0-9a-f]{40}) -f target=SIDEExplicitFormula\.\w+', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 18 \
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
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS, OPEN_TRAILS and the edition; (R336) orders no ERRATA, REGISTRY or
    archive write), the ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b726's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**b723’s row**', '**The C2 build per field**', '**The edition**',
                 '**The front-door list and the LLM line**', '**The mechanism table**', '**The research instruments reproduced**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b726_corrigendum.txt', 'data/b726_standing_v160.txt', 'data/b726_root_row.txt', 'data/b726_edition_diff.txt',
                 'data/b726_frontdoors.txt', 'data/b726_mechanisms.txt', 'data/b726_c2.txt', 'data/b726_dispatch_rows.json',
                 'data/b726_reproduce.txt', 'data/b726_address_scan.txt', 'data/b726_touch.txt',
                 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b726: no row of the defects bank the navigator's ((a)-(o) the seat's)
#⟪END⟫
#⟪SECTION checks 31⟫
    """the name the frozen run list carries: b726 registers nothing ((R336) orders no registration; the next stands at b727, its M and A read
    before it): no data/b726_registrations.txt; b725's registrations at HEAD their text at their last commit; the components committed in
    their order, each the ancestor of the next; the earlier acts' registrations at HEAD their blobs at their commits."""
    reg, head = S['reg_now']
    return not os.path.exists(os.path.join(D, 'b726_registrations.txt')) and S['files']['reg'] == [K.REGISTRATIONS] and bool(reg) and reg == head \
        and bool(S['anc']) and all(v is True for v in S['anc'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R332)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 6, the Edit tool): tools/b726_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address and name read from history and held in memory -- the address 0, the author's name 0, the previous name 0, its
    four controls as wanted; the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R336)(4), N2 (the name the frozen run list carries): the edition by THE FORM OF AN EDITION -- the diff bank's foot its last line, H28a,
    H28b and H28c each HELD, the stems and the ceiling 0, H28a's VACUOUS beside its verdict; the edition at PLACE-papers HEAD its digest in
    the bank, the current version at HEAD byte-equal to its blob at the act's base; every ruled figure's read printed; the edition committed."""
    d = S['edition_diff'] or ''
    last = ((d.rstrip(NL).split(NL)) or [''])[-1]
    m = re.match(r'^### ### \*\*WHICH STRUCTURE CONFINES v2\.4\.0: WRITTEN BESIDE v2\.3\.1, UNEDITED ; H28a HELD \(0 WORK-LIST ROWS\) ; H28b HELD \((\d+) AGAINST (\d+)\) ; '
                 r'H28c HELD ; STEMS 0 ; CEILING 0 ; NOT DEPOSITED\.\*\*$', last)
    sha = lambda s: __import__('hashlib').sha256((s or '').encode('utf-8')).hexdigest()[:16]
    return bool(m) and int(m.group(1)) <= int(m.group(2)) and 'VACUOUS on the work-list' in d and bool(S['ws_edition']) \
        and ('the edition sha256 %s' % sha(S['ws_edition'])) in d and bool(S['ws_now']) and S['ws_now'] == S['ws_pre'] \
        and ('(sha256 %s)' % sha(S['ws_now'])) in d and '(21 reads, all as wanted)' in d
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R336)(5)-(6), N5 (the name the frozen run list carries): the front-door list assembled and not applied -- its foot its last line, the
    load-bearing and the silent summing to the EXCEEDS, the sweep's three controls as wanted, the LLM line's reads and its differing; each item
    naming its file, line, current words and drafted words; its parts A to G printed; no README, GitHub description or Zenodo record written."""
    t = S['frontdoors'] or ''
    last = ((t.rstrip(NL).split(NL)) or [''])[-1]
    m = re.match(r'^### ### \*\*THE FRONT-DOOR LIST: (\d+) ITEMS ; (\d+) LOAD-BEARING AND (\d+) SILENT OF (\d+) EXCEEDS ; THE LLM LINE READ AT (\d+) PAPERS AND (\d+) READMES, (\d+) DIFFERING ; '
                 r'SWEEP CONTROLS 3 OF 3 AS WANTED ; ASSEMBLED AND NOT APPLIED ;', last)
    return bool(m) and int(m.group(2)) + int(m.group(3)) == int(m.group(4)) and int(m.group(7)) <= int(m.group(5)) + int(m.group(6)) \
        and all(('## PART %s' % c) in t for c in 'ABCDEFG') and 'data/b726_frontdoors.txt' in S['files']['c3']
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R336)(3), N1, N3, N5 (the name the frozen run list carries): the E0 grade at the unchanged header before the branch and the fields; c2-b725
    of SIDE-explicit-formula at its tip locally and at origin, cut from the worklist's base, its files against the base C2Walk.lean, the
    C2Field modules and print_targets.txt alone, off main and in no tag; the bank's last line naming the tip, the certificates compiled out of 18
    equal to the fields the rows read KERNEL, what remains and the dispatches of 18, NO MAIN, NO TAG; every field not compiled printed."""
    t = S['c2'] or ''
    b = S['ef_branches'].get('c2-b725') or {}
    tip = K.EF_BRANCHES[1][1]
    v = _vlast(t)
    i1, i2, i3, i4 = (t.find(x) for x in ('## (1) THE E0 GRADE', '## (2) THE BRANCH', '## (3) THE FIELDS', '## (4) WHAT THE GRADE COVERS'))
    m = re.search(r'CERTIFICATES COMPILED AT (\d+) OF 18 BY decide \+kernel', v)
    rds = [r for r in (S['drows'] or []) if r.get('kind') == 'read']
    kn = set(r.get('item') for r in rds if r.get('verdict') == 'KERNEL')
    return 0 <= i1 < i2 < i3 < i4 and '  THE GRADE: DERIVES -- ' in t[i1:i2] and b.get('local') == tip == b.get('remote') and b.get('base') == K.EF_BASE \
        and b.get('on_main') is False and b.get('tags') == [] \
        and all(f == 'SIDEExplicitFormula/C2Walk.lean' or f == 'print_targets.txt' or f.startswith('SIDEExplicitFormula/C2Field/') for f in b.get('files') or ['x']) \
        and v.startswith('THE C2 THEOREM: E0 DERIVES') and ('ON c2-b725 (%s)' % tip[:8]) in v and m is not None and int(m.group(1)) == len(kn) \
        and 'WHAT REMAINS: (L1), (L2), THE THEOREM' in v and v.endswith('OF 18 ; NO MAIN, NO TAG.') \
        and (int(m.group(1)) == 18 or 'NOT COMPILED: D=-' in v)


def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.6.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v160') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED as b725
    left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since b725's v1.3.0;
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
    """(R336)(7), N3 (the name the frozen run list carries): the mechanism table from the banks, no computation -- its foot its last line, every
    read as wanted, its rows printed, the Beurling instance NO INSTANCE FOUND in the sources read, the order left OPEN, the table asserting
    nothing about zeta; the literature read's reading beside it; the bank in the components' commit."""
    t = S['mechanisms'] or ''
    last = ((t.rstrip(NL).split(NL)) or [''])[-1]
    m = re.match(r'^### ### \*\*THE MECHANISM TABLE: (\d+) ROWS ; READS (\d+) OF \2 AS WANTED ; THE BEURLING INSTANCE WITH A FUNCTIONAL EQUATION: NO INSTANCE FOUND ; '
                 r'ASSERTS NOTHING ABOUT ZETA ; THE ORDER OPEN\.\*\*$', last)
    return bool(m) and t.count('## ROW ') == int(m.group(1)) and 'NO INSTANCE FOUND' in (S['beurling'] or '') and 'data/b726_mechanisms.txt' in S['files']['c3']


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b725's (R335)(7), carried in the run list): tools/research/reproduce.py's full run banked this
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
    """standing clauses v9 (Component 7 of (R336): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b726_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b725's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R336-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b725's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R336) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b725's standing arm, carried in the run list of 116 (Component 6, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R335)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from f4ab9491',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 89 = 89 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b725-closing (f4ab9491)', 'push-b725-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the edition; the front-door list and its counts; the LLM line; the C2 certificates; b723`s row and the chain; the mechanism table; the onset signature an observation), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R336)(1)-(2): the generated corrigendum for b725`s record, landed at FINDINGS :11801: its ten events and twenty-eight defects, 38 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 7 CLOSE 31, REPEAT 23; event (10)`s line READS STALE the one dated note; v1.6.0`s repairs by data/b726_standing_v160.txt; the corrigenda bank appended at row (46)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b726 and no b727 rules bank: no author`s word of b726 orders a row; v9 binds the act)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b726's objects
    ('G-REGISTRATIONS-FIRST', 'b726 registers nothing: no data/b726_registrations.txt; b725`s registrations at HEAD their text at dc0d4133; the components each the ancestor of the next (0dc805b2, 5f46a6a3, fe20cd09, then the components` commits); the earlier acts` registrations at HEAD their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(corr_c3=False))),
    ('G-PREDICTION-FIRST', '(R332)(9)(i), (R336)(8), N5, the scan arm: tools/b726_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, the bank`s counts the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R336)(4), N2: the edition by THE FORM OF AN EDITION -- the diff bank`s foot, H28a, H28b and H28c each HELD, stems and ceiling 0, H28a VACUOUS on its work-list rows said beside it; the digests of the edition and of the current version in the bank, the current version byte-equal to its blob at the act`s base',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'edition_diff', (S['edition_diff'] or '').replace('H28c HELD ; STEMS', 'H28c REFUTED ; STEMS'))),
    ('G-DERIVATION-GRADED', '(R336)(5)-(6), N5: the front-door list assembled and not applied -- its foot, load-bearing and silent summing to the EXCEEDS, the three sweep controls as wanted, the LLM line`s reads and differing, parts A to G, the bank in the components` commit',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'frontdoors', (S['frontdoors'] or '').replace('SWEEP CONTROLS 3 OF 3', 'SWEEP CONTROLS 2 OF 3'))),
    ('G-OFFSET-POST-HOC', '(R336)(3), N1, N3, N5: the C2 build per field -- the E0 grade at the unchanged header before the branch and the fields; c2-b725 at its tip locally and at origin, cut from main badaccc, its files C2Walk.lean, the C2Field modules and print_targets.txt, off main and untagged; the bank`s last line naming the certificates compiled equal to the rows` KERNEL fields, what remains and the dispatches, NO MAIN, NO TAG',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'ef_branches', lambda d: d['c2-b725'].update(tags=['v0.38']))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at e2246a8e, VERSION 9; v8 at HEAD its blob at e2246a8e; no v10; v9`s commit an ancestor of v1.6.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- the file byte-equal at e2246a8e, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R336)(7), N3: the mechanism table from the banks -- its foot, every read as wanted, its rows, the Beurling instance NO INSTANCE FOUND in the sources read, the order OPEN, nothing asserted about zeta; the bank in the components` commit',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'mechanisms', (S['mechanisms'] or '').replace('ASSERTS NOTHING ABOUT ZETA', 'BEARS ON ZETA'))),
    ('G-DIFFERS-ERRATA', '(R336)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at 06af23f0, no b726 differs or errata bank, the worklist naming no line or id for either; the weight line and the corrigendum in e3818db7, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b726_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R336-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b725`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at e2246a8e (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R336)(3): the per-field runs, each read once by its id -- the two commits and pushes, each dispatch at its commit, each read at its built ref; dispatch 1 FAILS with exit 1 on the elaboration; every KERNEL row exit 0 with its axiom line and no sorryAx; the C2 bank`s foot naming the count of dispatches',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: the dispatches` order and hold -- free memory at or above 2,560 MB at each push, dispatch and read; for each dispatch its commit`s push before it and its read after; eighteen dispatches at most, each by `gh workflow run build-module.yml` at main with the ref input the commit, none by push; no b721-b725 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 as b725 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, keiper-b725 and c2-b725 off it; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s three (FINDINGS, OPEN_TRAILS and the edition, (R336)(8)); no ERRATA, no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b725`s trail record on OPEN_TRAILS (:16581) and its root in the chain', lambda S: '### b725 — lane two, act one hundred and fifty-two, the research act under (R335)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the edition): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b725`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: (R336)(3)`s, each by gh workflow run, each read by its id in data/b726_dispatch_rows.json; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b726: (R336)'s rows, b725's (R335) rows pruned. The quote read from the bank (data/b726_ferry.txt :7)
    hq = _quote(rd(p('data', 'b726_ferry.txt')) or '', '"b725 closed: relay 14593dda', '". Its rows')
    add('ruling (1)', 'data/b725_closing.txt :1, the head line as the ruling quotes it (data/b726_ferry.txt)', bool(hq) and hq[1:] == at(cl, 1),
        at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', 'e2246a8e', 'data/b725_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'the head line as the public relay carries it at e2246a8e', bool(pub) and pub[0] == at(cl, 1),
        'remote main %s' % rm[:8], '1')
    ar_ = [l.split() for l in lines_of(p('data', 'act_roots.txt'))]
    add('ruling (1)', 'data/act_roots.txt :104, b725`s root d85513ca chained from b724`s e09d0fac', at(ar_, 104)[:1] == ['b725']
        and at(ar_, 104)[1].startswith('d85513ca') and at(ar_, 104)[2].startswith('e09d0fac'), ' '.join(x[:8] for x in at(ar_, 104)), '1')
    add('ruling (2)(ii)', 'data/act_roots.txt :102, the corrigendum row for b723', at(ar_, 102)[:2] == ['corrigendum', 'b723'],
        ' '.join(x[:12] for x in at(ar_, 102)), '1')
    fi_ = lines_of(p('data', 'b725_interference.txt'))
    add('ruling (1)', 'data/b725_interference.txt, its foot: Z_Q1 excludes 0 at 69, HELD', 'ZEROS 69' in at(fi_, 106) and 'Z_Q1 EXCLUDES 0 AT 69' in at(fi_, 106) and 'HELD' in at(fi_, 106), at(fi_, 106)[:70], '1')
    om_ = lines_of(p('data', 'b725_onset_mass.txt'))
    add('ruling (1)', 'data/b725_onset_mass.txt :14, off18`s onset a = 10.20248033', 'a = 10.20248033' in at(om_, 14), at(om_, 14)[:60], '1')
    add('ruling (1)', 'data/b725_onset_mass.txt :22, the falsifier FIRED at off18', at(om_, 22).endswith("FIRED at ['off18']"), at(om_, 22)[-30:], '1')
    dl_ = lines_of(p('data', 'b725_dial.txt'))
    for n_, w_ in ((33, 'a = 3.039966598'), (35, 'a = 2.888826162'), (37, 'a = 2.772588722')):
        add('ruling (1)', 'data/b725_dial.txt :%d, %s' % (n_, w_), w_ in at(dl_, n_), at(dl_, n_)[:60], '1')
    add('ruling (1)', 'data/b725_dial.txt :39, the products', "['0.911990', '1.155530', '1.386294']" in at(dl_, 39), at(dl_, 39)[:60], '1')
    for f_, w_ in (('b725_lambda2.txt', 'lambda_2'), ('b725_c2.txt', 'C2 THEOREM')):
        add('ruling (1)', 'data/%s, its foot' % f_, any(w_ in l for l in lines_of(p('data', f_))[-3:]), 'present', '1')
    er_ = rd(os.path.join(PP, 'ERRATA.md')) or ''
    add('ruling (5)', 'ERRATA.md: E-2026-10-29-1 entered', 'E-2026-10-29-1' in er_, 'present' if 'E-2026-10-29-1' in er_ else 'ABSENT', '4')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), ferry (read first)', 'events (1)-(10) and 28 defects (data/b725_events.txt, data/b725_defects.txt; the head line`s "28 defects")',
        starts == list(range(1, 11)) and len(letters) == 28, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    for n_, e_, w_ in ((4, 1, 'CLOSE ; REPEAT b724 event (1)'), (22, 4, 'CLOSE ; NEW'), (30, 5, 'CLOSE ; REPEAT b720 event (3)'), (36, 6, 'CLOSE ; REPEAT b723 event (15)'),
                       (44, 8, 'CLOSE ; REPEAT b724 event (15)'), (59, 10, 'CLOSE ; NEW')):
        add('ferry (read first)', 'event (%d) at data/b725_events.txt :%d' % (e_, n_), at(ev, n_).startswith('    (%d) ' % e_) and w_ in at(ev, n_)[:60],
            at(ev, n_)[:50], '0')
    add('ferry (read first)', 'data/b725_closing.txt :1, the carried items beneath it', bool(at(cl, 1)) and any('CARRIED' in l for l in cl), at(cl, 1)[:30], '0')
    for f_ in ('b725_interference.txt', 'b723_zetak.txt', 'b723_c2_closed_form.txt', 'b722_c2_price.txt', 'b721_frozen_line.txt', 'b721_frozen_line_drafts.txt', 'b709_grid.txt'):
        add('ferry (read first)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '0')
    rr_ = lines_of(p('data', 'b725_root_row.txt'))
    add('ferry (read first), ruling (2)(ii)', 'data/b725_root_row.txt :33-:39, the routes', at(rr_, 33).startswith('## THE ROUTES') and at(rr_, 34).startswith('  (A) a commit on a side branch'), at(rr_, 33)[:50], '1')
    add('ruling (2)(ii)', 'data/b725_root_row.txt :22, sha256 133004c8', '133004c8f910b786' in at(rr_, 22), at(rr_, 22)[:80], '1')
    add('ruling (2)(ii)', '2be0135c, the commit the branch is cut from', gr('D:/relay', 'cat-file', '-t', '2be0135c') == 'commit', gr('D:/relay', 'log', '--format=%s', '-1', '2be0135c')[:60], '1')
    zk_ = lines_of(p('data', 'b723_zetak.txt'))
    for n_, w_ in ((10, 'banked -0.0037191321 (data/b709_grid.txt :441)'), (14, 'banked -3.5300862e-5 (data/b709_grid.txt :4501)'),
                   (59, 'lambda_min 0.6888118560'), (65, 'lambda_min 2.995245235')):
        add('ruling (4)(a)', 'data/b723_zetak.txt :%d, %s' % (n_, w_), w_ in at(zk_, n_), at(zk_, n_)[:70], '3')
    gd_ = lines_of(p('data', 'b709_grid.txt'))
    for n_, w_ in ((441, '-0.0037191321'), (4501, '-3.5300862e-5')):
        add('ruling (4)(a)', 'data/b709_grid.txt :%d, %s' % (n_, w_), w_ in at(gd_, n_), at(gd_, n_)[:70], '3')
    cf_ = lines_of(p('data', 'b723_c2_closed_form.txt'))
    add('ruling (4)(b)', 'data/b723_c2_closed_form.txt :21, the statement', 'log(Z_Q / 2) = log zeta_K - S + log cosh S' in at(cf_, 21), at(cf_, 21)[:60], '3')
    cp_ = lines_of(p('data', 'b722_c2_price.txt'))
    add('ferry (read first), ruling (3)', 'data/b722_c2_price.txt (B), the certificate route', any(l.startswith('### (B) the certificate route') for l in cp_),
        next((l[:50] for l in cp_ if l.startswith('### (B)')), 'NONE'), '2')
    fl_ = lines_of(p('data', 'b721_frozen_line.txt'))
    add('ferry (read first), ruling (5)', 'data/b721_frozen_line.txt lines 282 at least', len(fl_) >= 282, 'lines %d' % len(fl_), '4')
    ws_ = lines_of(os.path.join(PP, 'day1', 'Which_Structure_Confines.md'))
    add('ruling (4)', 'day1/Which_Structure_Confines.md, present', bool(ws_), 'lines %d' % len(ws_), '3')
    add('ruling (4)', 'day1/Which_Structure_Confines.md at v2.3.1', any(l.startswith('*v2.3.1') for l in ws_[:30]), next((l[:30] for l in ws_[:30] if l.startswith('*v2.3.1')), 'NONE'), '3')
    add('ferry (read first), ruling (4)', 'day1/Which_Structure_Confines.md, its Correspondence section', any(l.startswith('#') and 'Correspondence' in l for l in ws_),
        next((l[:50] for l in ws_ if l.startswith('#') and 'Correspondence' in l), 'NONE'), '3')
    mg_ = rd(os.path.join(PP, 'day1', 'A_Place_to_Stand.md')) or ''
    llm_ = '*Computational workflow assisted by various LLM instances. Mathematical content, strategies of argument, and editorial decisions are the author' + chr(8217) + 's.*'
    add('ruling (6)', 'day1/A_Place_to_Stand.md, the LLM line', llm_ in mg_ or llm_.replace(chr(8217), "'") in mg_, 'present', '4')
    add('ferry (read first), ruling (4)', 'OPEN_TRAILS :11864, THE FORM OF AN EDITION', 'THE FORM OF AN EDITION' in at(ot, 11864), at(ot, 11864)[60:150], '3')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    add('ruling (4)', 'phase1.5/method/INSTRUMENTS.md :388, I-16 THE FORM OF AN EDITION, provenance OPEN_TRAILS :11864', at(ins_, 388).startswith('## I-16') and 'OPEN_TRAILS :11864' in at(ins_, 388), at(ins_, 388)[:60], '3')
    add('ferry (read first), ruling (4)', 'OPEN_TRAILS :12228, THE PRECEDENCE ORDER (I-33, INSTRUMENTS :456)', 'THE PRECEDENCE ORDER' in at(ot, 12228) and at(ins_, 456).startswith('## I-33'), at(ins_, 456)[:60], '3')
    add('ruling (7)', 'OPEN_TRAILS :16589, W-ORD-MECHANISM-TABLE', 'W-ORD-MECHANISM-TABLE' in at(ot, 16589), at(ot, 16589)[:50], '5')
    add('ruling (5)', 'OPEN_TRAILS :16593, W-ORD-SILENT-SENTENCES', 'W-ORD-SILENT-SENTENCES' in at(ot, 16593), at(ot, 16593)[:50], '4')
    add('PATHS', 'SIDE-explicit-formula at the path its clone has on this host', os.path.isdir(os.path.join(K.EF_DIR, '.git')), K.EF_DIR, '0')
    add('PATHS', 'SIDE-lv-conservation at D:/SIDE-lv-conservation', os.path.isdir(os.path.join(K.LV_DIR, '.git')), K.LV_DIR, '0')
    add('PATHS', 'SIDE-grh-transfer at D:/SIDE-grh-transfer', os.path.isdir('D:/SIDE-grh-transfer/.git'), 'D:/SIDE-grh-transfer', '0')
    add('PATHS', 'the patent repository', os.path.isdir('D:/MY-DOwnloads/patent-package-BACKUP-2026-08-29/.git'), 'D:/MY-DOwnloads/patent-package-BACKUP-2026-08-29', '0')
    add('ruling (3)', 'c2-b725 at 52cbbc11 on SIDE-explicit-formula', gr(K.EF_DIR, 'rev-parse', 'c2-b725').startswith('52cbbc11'), gr(K.EF_DIR, 'rev-parse', 'c2-b725')[:12], '2')
    cs_ = rd(p('tools', 'standing', 'fold', 'checks.tpl')) or ''
    add('ruling (2)(iii)', 'tools/standing/fold/checks.tpl, G-CLOSING-SENTENCE`s predicate', 'closing_sentence_ok' in cs_, 'present', '1')
    ra_ = lines_of(p('tools', 'rule_arms.py'))
    add('ruling (2)(iii)', 'tools/rule_arms.py :458, the scores reader', '_record.py' in at(ra_, 458) or 'scores' in at(ra_, 458), at(ra_, 458).strip()[:70], '1')
    add('ferry', 'tools/standing/ at v1.5.0 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.5.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ruling (8), ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R336)(8): b725's export, the mirror's last
    add('ruling (8)', 'D:/MY-DOwnloads/mirror-refresh-2026-10-30-b725.zip, b725`s export', os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '6')
    # ### PATHS: the kernels at the paths data/b716_federation_pin_price.txt names
    add('PATHS', 'the kernels data/b716_federation_pin_price.txt names, each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R336)(8): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (8)', 'the push-b725-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R336)(8): act_current alone, then b725's step row 40 and its closing capture, each committed alone
    for c_, f_ in ((K.ACT_CURRENT_COMMIT, 'data/act_current.json'), (K.STEPZERO_STEPS, 'data/b725_steps.json'),
                   (K.STEPZERO, 'data/b725_relay_push-b725-closing_push_out.txt')):
        if not c_:
            add('ruling (8)', '%s -- TO BE COMMITTED at step zero after this check' % f_, True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (8)', '%s committed alone at %s' % (f_, c_), nm_ == [f_], ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (8)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (8)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (8)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b726_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b726_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b726 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b725_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R336)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with v1.6.0's controls and b723's row, the C2 build per field, the edition, the front-door list and
the LLM line, the mechanism table, the name and address scan, the reproduction run, the touch read of v9 and
the standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R336)'s counter line beneath
the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section; the author's word after the
seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next act ((R336)(10)). The
standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act on SIDE-explicit-formula's c2-b725 alone ((R336)(3), N5): no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b727 and the release sitting ((R336)(10)); the open orders by tools/standing/orders.py's output over the trail,
    not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b726 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY-THREE, THE WAVE 1 ACT: WHICH STRUCTURE CONFINES v2.4.0 BESIDE v2.3.1; '
              'THE FRONT-DOOR LIST ASSEMBLED AND NOT APPLIED; THE LLM LINE READ; THE C2 BUILD SPLIT PER FIELD ON c2-b725; b723`S ROW CARRIED ON ITS BRANCH; '
              'THE MECHANISM TABLE; v1.6.0 LANDED, UNDER (R336).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b725's sections over b725's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.6.0: G-CLOSING-SENTENCE and G-RULE-SCORES-BEFORE-SEAL, each case failing before its repair and passing after', 'b726_standing_v160.txt'),
                ('b723`s row on corrigendum-b723, the chain`s verify, main untouched', 'b726_root_row.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE C2 BUILD PER FIELD ((R336)(3))', [
                ('one job per discriminant, each read by its run id, the free memory read before each', 'b726_c2.txt', r'\*\*THE C2 THEOREM: [^*]*')]),
            ('THE EDITION ((R336)(4))', [
                ('Which Structure Confines v2.4.0 against v2.3.1, sentence by sentence, and its scores', 'b726_edition_diff.txt')]),
            ('THE FRONT-DOOR LIST AND THE LLM LINE ((R336)(5)-(6))', [
                ('every EXCEEDS classed load-bearing or silent, the drafts, the deposited records, the LLM reads; assembled, not applied', 'b726_frontdoors.txt')]),
            ('THE MECHANISM TABLE ((R336)(7))', [
                ('three rows from the banks, no computation', 'b726_mechanisms.txt'),
                ('the literature read for the Beurling row', 'b726_beurling_read.txt', r'(?m)^  A Beurling system[^\n]*')]),
            ('THE NAME AND ADDRESS ((R332)(9))', [
                ('the scan over every commit and bank of the act, the previous address and name held in memory, the counts alone', 'b726_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b725`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b726_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: SIDE-explicit-formula`s c2-b725 alone ((R336)(3), N5), two tree states on b725`s tip (c9add92f the split, ea95a8d0 the',
    '    binders; SIDEExplicitFormula/C2Walk.lean, the C2Field modules, print_targets.txt), each pushed alone through push_gated.sh and read',
    '    back equal, the commits under the noreply identity ; %d dispatches of build-module.yml at main, eighteen at most, each read by its' % len(WL.EF_RUNS),
    '    run id (relay data/b726_dispatch_rows.json) ; no kernel`s main touched, no tag cut (N5) ; the rebuild-b721 branches of the wave 1 kernels',
    '    as b725 left them ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, keiper-b725 and the challenge branch',
    '    challenge-b720-h2-sign-iff-rh standing ; port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ;',
    '    SIDE-lv-conservation`s main and its deposit v0.10.0 unmoved ; SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; on the',
    '    author`s word the local user.name of SIDE-grh-transfer and the patent repository set to the login ; N1: no lean or lake process on',
    '    this host ; free memory read before each suite part, computation, push and dispatch ; the push-b725-* branches of relay and',
    '    PLACE-papers deleted at step zero by name, one per command and each its own message ; relay branch corrigendum-b723 cut off 2be0135c,',
    '    pushed, main untouched ; N2: every figure the edition carries read at its bank and line before composition, the current version',
    '    unedited beside it ; N3: every grade at its bank`s end, the observation called an observation wherever named ; (R332)(9), (R336)(8):',
    '    no new occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay data/b726_address_scan.txt),',
    '    the commits under the GitHub login and its noreply address ; no identifier of the author in any outbound request header, URL, input',
    '    or payload, or in any workflow file ; no secret added ; the outbound reads: the seat`s plain requests to github.com, six anonymous',
    '    Zenodo record reads (data/b726_zenodo_read.json) and three public arXiv papers (data/b726_beurling_read.txt) ; the deposit route',
    '    untouched, publish never called, the draft held at v5, no Zenodo record or description edited ; no README or GitHub description',
    '    changed ; on PLACE-papers main FINDINGS (the weight line, the observation, the corrigendum, the entry), OPEN_TRAILS (the trail) and',
    '    day1/Which_Structure_Confines_v2_4_0.md written ; no ERRATA, no paper cut, moved or renamed ; no FOUNDATIONS, REGISTRY, README or',
    '    faces page byte ; data/act_roots.txt (b723`s corrigendum row at :105 and b726`s root) and the corrigenda bank appended ;',
    '    data/act_current.json written at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.6.0 by (R336)(2)(iii) ; the hook in',
    '    D:/.claude/settings.json unedited ; the per-act tools of b698-b725 unedited ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ;',
    '    nothing of TECHNE or any patent written beyond the one configuration word',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, (R336)(10)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the release sitting and b727, each from its bank: the front-door list as the agenda, its byline item and the SPIRAL_MAP item read at',
    '        their parts (relay data/b726_frontdoors.txt); the C2 fields not compiled, (L1), (L2) and the theorem (relay data/b726_c2.txt); the',
    '        Beurling row`s instance and the mechanism table`s fourth row (relay data/b726_mechanisms.txt); the reproduction`s NOT RUN rows, each with its',
    '        price (relay data/b726_reproduce.txt); the onset successor, its M and A read from computed form before any registration; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 and c2-b725 (at ' + WL.EF_BRANCHES[1][1][:8] + ') of',
    '        SIDE-explicit-formula, off main, untagged; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b725 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, SIDE-explicit-formula`s c2-b725 carrying (R336)(3)`s commits, no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b726: the standing repairs are v1.6.0's ((R336)(2)(iii), relay data/b726_standing_v160.txt, read in the corrigendum section); the
    # ### carry's diffs here (b726 carried at step zero before the fold; its tools since are the templates and tools/acts/b726.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act; '
          'SIDE-explicit-formula`s %s ((R336)(3)), cut from main %s; the %s branches of the wave 1 kernels as b725 left them; '
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
    b726's form over b726's objects (b725's form in git at b725's record tool): the corrigendum's foot and v1.6.0's controls; b723's row on its
    branch and the chain's verify; the C2 bank; the edition's scores; the front-door list; the mechanism table; the citation check; the
    reproduction run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v160.txt' % ACT, r'\*\*v1\.6\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.6.0`s controls')
    rr = _bfig('%s_root_row.txt' % ACT, r"\*\*b723'S ROW CARRIED ON corrigendum-b723 \(([0-9a-f]{8}), sha ([0-9a-f]{8})\) ; THE ROW AT act_roots :(\d+) ; VERIFY ([^;]+?) ; MAIN UNTOUCHED\.\*\*", 'b723`s row`s foot')
    ed = _bfig('%s_edition_diff.txt' % ACT, r'\*\*WHICH STRUCTURE CONFINES v2\.4\.0: WRITTEN BESIDE v2\.3\.1, UNEDITED ; H28a HELD \((\d+) WORK-LIST ROWS\) ; H28b HELD \((\d+) AGAINST (\d+)\) ; H28c HELD ; STEMS (\d+) ; CEILING (\d+) ; NOT DEPOSITED\.\*\*', 'the edition`s foot')
    ed_stands = _bfig('%s_edition_diff.txt' % ACT, r'STANDS: (\d+) of (\d+) sentences', 'the edition`s STANDS line')
    fd = _bfig('%s_frontdoors.txt' % ACT, r'\*\*THE FRONT-DOOR LIST: (\d+) ITEMS ; (\d+) LOAD-BEARING AND (\d+) SILENT OF (\d+) EXCEEDS ; THE LLM LINE READ AT (\d+) PAPERS AND (\d+) READMES, (\d+) DIFFERING ;', 'the front-door list`s foot')
    me = _bfig('%s_mechanisms.txt' % ACT, r'\*\*THE MECHANISM TABLE: (\d+) ROWS ; READS (\d+) OF \2 AS WANTED ;', 'the mechanism table`s foot')
    c2 = _bfig('%s_c2.txt' % ACT, r"\*\*THE C2 THEOREM: E0 DERIVES ; ROUTE \(B\) EQUAL TO THE STATEMENT AT (\d+) OF 18 ; ON c2-b725 \(([0-9a-f]{8})\) CERTIFICATES COMPILED AT (\d+) OF 18 BY decide \+kernel, ([^;]+?) ; "
               r"NOT COMPILED: ([^;]+?) ; WHAT REMAINS: ([^;]+?) ; DISPATCHES (\d+) OF 18 ; NO MAIN, NO TAG\.\*\*", 'the C2 theorem`s foot')
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
                v160_ctl=v5[0], v160_cases=v5[1], v160_wanted=v5[2],
                rr_tip=rr[0], rr_sha=rr[1], rr_row=rr[2], rr_verify=rr[3],
                ed_rows=ed[0], ed_diff=ed[1], ed_bound=ed[2], ed_stems=ed[3], ed_ceiling=ed[4], ed_stands=ed_stands[0], ed_of=ed_stands[1],
                fd_items=fd[0], fd_load=fd[1], fd_silent=fd[2], fd_exceeds=fd[3], fd_papers=fd[4], fd_readmes=fd[5], fd_differ=fd[6],
                me_rows=me[0], me_reads=me[1],
                c2_mirror=c2[0], c2_tip=c2[1], c2_k=c2[2], c2_ax=c2[3], c2_left=c2[4], c2_remains=c2[5], c2_dispatches=c2[6],
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                drows=drows,
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R336)(3): the kernel rows of one kind as banked (data/b726_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R336): no lean process runs on this host; the runner dispatches are those of (R336)(3), eighteen at most, each read by its
    run id. From the command bank (the seat's commands, read live from the capture by the `commands` route: local lean none; the dispatch
    commands `gh workflow run`) and the dispatch rows (relay data/b726_dispatch_rows.json: each dispatch by command and each read by its run
    id), against the worklist's EF_RUNS."""
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
        'the seat`s commands running lean or lake on this host (relay data/b726_commands.json): %s; dispatch commands in the capture: %s against '
        'the rows` dispatches %d; the runs dispatched (relay data/b726_dispatch_rows.json) %d of %d at most, equal to the worklist`s EF_RUNS: %s '
        '(%s); each read by its id: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(dsp), len(ran), K.MAX_DISPATCHES, ran == want,
            ', '.join('%s %s' % x for x in ran) or 'NONE', read_ids == [r for _i, r in want]))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b726's objects; b725's over its registrations in git at b725's record tool): each tool's controls before its figures, (bank, the
# ### controls' line, the first figure's line)
N2_CONTROLS = (('data/b726_edition_diff.txt', '## THE ADDITIONS, EACH FIGURE READ', '## THE SCORES'),
               ('data/b726_frontdoors.txt', '## THE CONTROLS, BEFORE ANY SENTENCE', '## PART A'),
               ('data/b726_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R336): every figure the edition carries cited at bank and line and equal to the bank; the scores printed by the form's clauses; the
    current version unedited beside it. From the diff bank's rows, each re-read here at its bank and line; its clause lines; and git's diff of
    the current version against the act's base."""
    d = rdn('%s_edition_diff.txt' % ACT)
    reads = re.findall(r'(?m)^  data/(\S+) :(\d+) carries: (.+)$', d)
    miss = []
    for b_, n_, w_ in reads:
        ls = rdn(b_).split(NL)
        l_ = ls[int(n_) - 1] if int(n_) <= len(ls) else ''
        if w_ not in l_ and w_.replace('`', "'") not in l_:
            miss.append('%s :%s' % (b_, n_))
    clauses = [c for c in ('H28a:', 'H28b (I-21):', 'H28c:', 'STANDS:', 'THE PAGE CLAUSE (I-28):', 'THE LLM LINE:') if c not in d]
    edited = g(K.PP, 'diff', '--name-only', K.PRE_PP, 'HEAD', '--', 'day1/Which_Structure_Confines.md').strip()
#⟪END⟫
#⟪SECTION record 12⟫
    ok = len(reads) == 21 and not miss and not clauses and not edited and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the edition`s figures read at their banks and lines by this reader: %d, unequal %s; the form`s clauses printed, absent %s; the current '
        'version changed against the act`s base: %s; each tool`s controls before its figures: %s' % (
            len(reads), miss or 'NONE', clauses or 'NONE', edited or 'NO', ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b726's objects; b725's in git at b725's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b726_standing_v160.txt', ('ALL AS WANTED',)), ('b726_root_row.txt', ('VERIFY', 'MAIN UNTOUCHED')),
             ('b726_c2.txt', ('THE C2 THEOREM', 'DISPATCHES', 'OF 18')), ('b726_edition_diff.txt', ('H28a', 'H28b', 'H28c')),
             ('b726_frontdoors.txt', ('ASSEMBLED AND NOT APPLIED',)), ('b726_mechanisms.txt', ('ASSERTS NOTHING ABOUT ZETA',)),
             ('b726_citation_check.txt', ('CITES CHECKED',)), ('b726_reproduce.txt', ('REPRODUCES',)))
# ### N3: a sentence saying a module compiles, and the words that carry its axiom print; a negation before the verb
N3_COMPILES = re.compile(r'(?i)\bcompil(?:es|ed)\b')
N3_AXIOMS = re.compile(r'(?i)standard three|propext|axioms?\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|nothing|no)\b[^.;]{0,24}$')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R336): every grade prints at its end; the observation is called an observation wherever named; no sentence says the onset signature
    is a law or that any statement here bears on zeta's zeros; no sentence calls a compile complete without its axiom print. From the banks'
    last lines and the entry as composed (the findings bank's text, or the composer before it is written)."""
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
    bare = []
    for s in sents:
        for m in N3_COMPILES.finditer(s):
            if not N3_NEGATED.search(s[:m.start()]) and not N3_AXIOMS.search(s):
                bare.append(s.strip()[:120])
                break
    obs = [s for s in sents if re.search(r'(?i)onset signature|onset’s place', s)]
    unlabelled = [s.strip()[:120] for s in obs if 'observation' not in s.lower()]
    lawsaid = [s.strip()[:120] for s in obs if re.search(r'(?i)\bis a law\b', s)]
    zeta = [s.strip()[:120] for s in sents if re.search(r'(?i)bears? on zeta|zeta’s zeros (?:lie|are)|zeros of zeta (?:lie|are)', s) and not re.search(r'(?i)\b(?:no|not|nothing|nor)\b', s)]
    ok = all(o for _n, o in graded) and not bare and not unlabelled and not lawsaid and not zeta
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the sentences of %s saying a module compiles, not in negation, without its '
        'axioms: %s; the onset signature named %d time%s, unlabelled an observation: %s; called a law: %s; a statement here bearing on zeta`s zeros: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), src, bare or 'NONE', len(obs), '' if len(obs) == 1 else 's', unlabelled or 'NONE', lawsaid or 'NONE', zeta or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R336) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R336)(5))
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
    # ### (R336) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b725's form, carried) -- read from git,
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
    # ### (R336)(9), N5: no kernel's main touched and no tag cut, every Lean file of the act on c2-b725 alone -- every ref of every kernel carrying a
    # ### commit made after the act's opening commit is that branch at its tip (the worklist's EF_BRANCHES), over the base by its own commits, off
    # ### main and untagged; no .lean file changed or untracked in a kernel's tree; the rebuild-b721 branches kept as b725 left them; the address
    # ### scan's count from its bank (relay data/b726_address_scan.txt), the suite's arm recounting it live
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
    ef_scr_ok = sorted(ef_new) == ['c2-b725'] and all(o for _b, o in ef_scr)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and ef_scr_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b726_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s %s, or a .lean file in a kernel`s tree (%d kernels read): %s; each of those branches over '
            'the base %s, off main, untagged, its files against the base Lean files and the print list alone: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', ' and '.join('%s at %s' % (b, t[:8]) for b, t in K.EF_BRANCHES), len(K.KERNEL_PATHS),
                lean_w or 'NONE', K.EF_BASE[:8], ', '.join('%s %s' % x for x in ef_scr), K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b726 — lane two, act one hundred and fifty-three, the wave 1 act under (R336): b725 at its weight and its corrigendum; '
            'v1.6.0 and b723’s row on its branch; the C2 build per field; Which Structure Confines v2.4.0; the front-door list and the LLM line; the mechanism table')
#⟪END⟫
#⟪SECTION record 29⟫
def _mech_table():
    """(R336)(7): the mechanism table as FINDINGS carries it, each cell read from data/b726_mechanisms.txt's rows, refusing where a row is short."""
    t = rdn('%s_mechanisms.txt' % ACT)
    cell = lambda s: s.strip().replace('`', '’').replace('|', '/')
    rows = []
    for m in re.finditer(r'(?m)^## ROW (\d+) -- (.+)\n  FAMILY:\s+(.+)\n  INGREDIENTS:\s+(.+)\n  MECHANISM:\s+(.+)\n  INSTANCE:\s+(.+)\n  ONSET:\s+(.+)$', t):
        rows.append('| %s | %s | %s | %s | %s | %s |' % tuple(cell(x) for x in m.groups()[1:]))
    if len(rows) != int(_figs()['me_rows']):
        sys.exit('### THE MECHANISM TABLE: %d ROWS READ -- NOTHING COMPOSED' % len(rows))
    return ['| Mechanism | Family | Ingredients | Mechanism read | Instance | Onset |', '| --- | --- | --- | --- | --- | --- |'] + rows


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 6 form adjusted to what the act did: the C2 grade reads certificates, not the
    theorem, whose (L1) and (L2) stand unproved; the LLM count is papers and READMEs; every figure from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    chain = re.findall(r'(b\d{3}) (AGREE|DISAGREE)', f['rr_verify'])
    bad = [a for a, v in chain if v == 'DISAGREE']
    return ('## Which Structure Confines v2.4.0 carrying the zeta_K figure and the closed form; the front-door list, %s items, %s load-bearing and %s silent; '
            'the LLM line read at %d papers and READMEs, %s differing; the C2 certificates compiled at %s of 18 fields; b723’s row carried on its branch, the chain %s; '
            'the mechanism table’s %s rows; the onset signature entered as an observation' % (
                f['fd_items'], f['fd_load'], f['fd_silent'], int(f['fd_papers']) + int(f['fd_readmes']), f['fd_differ'], f['c2_k'],
                'AGREE' if not bad else 'DISAGREE at %s' % ', '.join(bad), f['me_rows']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the edition`s byline and two self-citations reading the author, no name carried under (R336)(8), the deposit`s wording for the release sitting '
            '(relay data/b726_frontdoors.txt part G); (2) SPIRAL_MAP :104 listed by its digest, not quoted, PLACE-papers being private and the relay public '
            '(relay data/b726_frontdoors.txt part B); (3) b722`s statement text repaired on the branch alone, its binders, every term unchanged, the bank not edited '
            '(relay data/b726_c2.txt (2)); (4) the C2 fields not compiled: %s (relay data/b726_c2.txt); (5) the Beurling row`s instance scoped to the sources read '
            '(relay data/b726_beurling_read.txt); (6) the sweep`s matcher written this act, no standing tool carrying one (relay data/b726_frontdoors.txt); '
            '(7) %s and the seat’s %s '
            'defect%s as lettered' % (
                f['c2_left'],
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
            'author beside the next act of (R336)(10)): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b726's objects; b725's composer in git at
    b725's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    chain = re.findall(r'(b\d{3}) (AGREE|DISAGREE)', f['rr_verify'])
    left = 'and every field compiled' if f['c2_left'] == 'NONE' else 'with %s not compiled' % f['c2_left']
    e = ['', _title(), '',
         'Which Structure Confines stands at v2.4.0 beside v2.3.1, unedited, with the zeta_K figure and the closed form added and its ceiling sentences corrected; '
         'the front-door list holds %s items, %s load-bearing and %s silent of %s EXCEEDS, assembled and not applied; the LLM line reads differently at %s of the %d papers and READMEs read; '
         'the C2 certificates compile by decide +kernel at %s of 18 fields, %s, %s, while (L1), (L2) and the theorem stay unproved; b723’s row is carried on its branch and the chain reads %s; '
         'the mechanism table has %s rows, the Beurling row without an instance carrying a functional equation; the onset signature stands as an observation, POST HOC, not a law.' % (
             f['fd_items'], f['fd_load'], f['fd_silent'], f['fd_exceeds'], f['fd_differ'], int(f['fd_papers']) + int(f['fd_readmes']), f['c2_k'], left,
             f['c2_ax'].lower(), ', '.join('%s %s' % x for x in chain), f['me_rows']), '',
         '*Filed at b726 on the author’s ruling `(R336)`; %d question%s put before the root. Banks: relay '
         '`data/b726_corrigendum.txt`, `data/b726_standing_v160.txt`, `data/b726_root_row.txt`, `data/b726_c2.txt`, `data/b726_dispatch_rows.json`, `data/b726_edition_diff.txt`, '
         '`data/b726_frontdoors.txt`, `data/b726_zenodo_read.json`, `data/b726_mechanisms.txt`, `data/b726_beurling_read.txt`, `data/b726_reproduce.txt`, `data/b726_address_scan.txt`, '
         '`data/b726_touch.txt`, `data/b726_standing_figures.txt`, `data/b726_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R336)(1)-(2), `%s`, `%s`, `%s`, `%s`): b725 entered at its weight and the observation POST HOC (FINDINGS :%s); '
         'the corrigendum of b725’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b726_corrigendum.txt); tools/standing/ at %s, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after: G-CLOSING-SENTENCE and G-RULE-SCORES-BEFORE-SEAL '
         '(relay data/b726_standing_v160.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v160_ctl'], f['v160_cases'],
             f['v160_wanted']), '',
         '**b723’s row** ((R336)(2)(ii), `%s`): relay branch corrigendum-b723 (`%s`) off 2be0135c carries data/b723_bank_hashes.json at the bytes b723’s root hashed, sha %s, and nothing else; '
         'the row at act_roots :%s in b680’s form; verify reads %s; main untouched (relay data/b726_root_row.txt).' % (K.C1_RELAY[:8], f['rr_tip'], f['rr_sha'], f['rr_row'], f['rr_verify']), '',
         '**The C2 build per field** ((R336)(3), N1, N3, N5): the E0 grade DERIVES at the unchanged header; on c2-b725 (`%s`) one job per discriminant, %s dispatches of eighteen at most, each read by its run id, '
         'the free memory read before each. The first dispatch failed: the statement’s text as b722 banked it does not elaborate at rQ and bL, which b725’s empty log had hidden, and the repair on the branch is binder annotations alone, every term and C2ValueLaw’s header unchanged. '
         'The certificates compiled at %s of 18 by decide +kernel, %s; not compiled: %s. Compiled here means the certificate `cert D n0 v q = true`: what remains is %s, so the module’s statement stays graded DERIVES and C2ValueLaw is not compiled at any field '
         '(relay data/b726_c2.txt, data/b726_dispatch_rows.json).' % (
             f['c2_tip'], f['c2_dispatches'], f['c2_k'], f['c2_ax'].lower(), f['c2_left'], f['c2_remains'].replace('THE THEOREM', 'the theorem')), '',
         '**The edition** ((R336)(4), N2, PLACE-papers `%s`): day1/Which_Structure_Confines_v2_4_0.md beside v2.3.1 by THE FORM OF AN EDITION: H28a HELD, VACUOUS on its %s work-list rows and carried on the ruled additions; H28b HELD, %s against the bound %s; H28c HELD, stems %s, ceiling %s; '
         '%s of %s sentences carried unchanged; the zeta_K figure and the closed form each read at bank and line (relay data/b726_edition_diff.txt). Committed to PLACE-papers, deposited nowhere.' % (
             K.C3_PP[:8], f['ed_rows'], f['ed_diff'], f['ed_bound'], f['ed_stems'], f['ed_ceiling'], f['ed_stands'], f['ed_of']), '',
         '**The front-door list and the LLM line** ((R336)(5)-(6), N5): relay data/b726_frontdoors.txt, %s items, each naming its file, line, current words and drafted words, the SPIRAL_MAP item by its digest; of the %s EXCEEDS sentences %s load-bearing, repaired at the release sitting, and %s silent, carried with notes, which acts W-ORD-SILENT-SENTENCES; '
         'the LLM line read against day1/A_Place_to_Stand.md :2178 at %s papers and %s kernel READMEs, %s differing, the edition carrying the monograph’s words. Assembled and not applied: no README, GitHub description or Zenodo record written.' % (
             f['fd_items'], f['fd_exceeds'], f['fd_load'], f['fd_silent'], f['fd_papers'], f['fd_readmes'], f['fd_differ']), '',
         '**The mechanism table** ((R336)(7), W-ORD-MECHANISM-TABLE), from the banks, no computation, %s reads as wanted; it lists the mechanisms the record and the cited literature show and asserts nothing about zeta; left OPEN for its fourth row (relay data/b726_mechanisms.txt, data/b726_beurling_read.txt):' % f['me_reads'], ''] + _mech_table() + ['',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b726_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R332)(9), (R336)(8), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b726_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b726_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b726 -- %s, %s, %s, %s -- against b725’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b726_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the edition’s closed form and the mechanism table’s first row are one statement read twice, the h = 2 identity in the paper and in the table, each citing the same bank; '
         'the C2 certificates and the front-door list meet at what a word claims -- the certificates compile while the theorem does not, and the list’s EXCEEDS sentences are where words ran past what compiled.', '',
         '**Carried to:** the release sitting on the author’s word, the front-door list as its agenda; then %s, the research act: the onset successor from the six banked products and off18’s, M and A read from computed form before any registration; the Beurling row’s instance if found; '
         'lambda_2’s two premises; W-ORD-VISIBILITY from H-INTERFERENCE’s table; the C2 fields not compiled, (L1) and (L2); the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b725():
    """b725's form over b725's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b726's objects; b725's composer in git at b725's record tool): W-ORD-SILENT-SENTENCES discharged and
    W-ORD-MECHANISM-TABLE annotated with the table's line and carried OPEN, each by its own line, then the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD with those lines beneath it, the discharge read CLOSED and the table read OPEN
    by the generator's rule."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = ['**`W-ORD-SILENT-SENTENCES` DISCHARGED at b726, (R336)(5):** every EXCEEDS sentence classed against the corpus, %s load-bearing at the head of the list and %s silent carried with notes (relay data/b726_frontdoors.txt).' % (f['fd_load'], f['fd_silent']),
           '**`W-ORD-MECHANISM-TABLE` CARRIED at b726, (R336)(7):** the table of %s rows at FINDINGS :%s, the order standing OPEN for its fourth row (relay data/b726_mechanisms.txt).' % (f['me_rows'], fj.get('entry_line'))]
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    if 'W-ORD-SILENT-SENTENCES' in op or 'W-ORD-MECHANISM-TABLE' not in op:
        sys.exit('### THE TRAIL: THE TWO ORDERS NOT READ AS RULED BY THE GENERATOR`S RULE -- NOTHING COMPOSED')
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R336) ratified.** Its components as the ferry orders them (relay data/b726_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b725’s weight and the observation), :%s (the corrigendum), :%s (the entry); no ERRATA; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The orders acted** ((R336)(5), (7)):', '']
    rows_ += two + ['',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the line above from tools/standing/orders.py`s output.' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The dated note** ((R336)(2)(iv)): relay data/b725_closing.txt :352, “the local configuration not edited”, READS STALE as of b725’s close: on the author’s word the local user.email of five clones was set to the noreply form. The note stands in the corrigendum at FINDINGS :%s and here, the line not rewritten.' % f['corr_line'], '',
             '**The carried items and b723’s row:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b726_standing_v160.txt); '
             'b723’s row on corrigendum-b723 at act_roots :%s, verify %s (relay data/b726_root_row.txt).' % (
                 f['ver'], f['v160_cases'], f['v160_wanted'], f['rr_row'], f['rr_verify']), '',
             '**The C2 build per field:** on c2-b725 (`%s`), certificates compiled at %s of 18, %s, %s dispatches each read by its run id; not compiled: %s; what remains %s (relay data/b726_c2.txt).' % (
                 f['c2_tip'], f['c2_k'], f['c2_ax'].lower(), f['c2_dispatches'], f['c2_left'], f['c2_remains'].replace('THE THEOREM', 'the theorem')), '',
             '**The edition:** Which Structure Confines v2.4.0 at PLACE-papers `%s`, H28a HELD, VACUOUS on its work-list rows, H28b %s against %s, H28c HELD (relay data/b726_edition_diff.txt).' % (K.C3_PP[:8], f['ed_diff'], f['ed_bound']), '',
             '**The front-door list and the LLM line:** %s items, %s load-bearing and %s silent, the LLM line differing at %s of %d, assembled and not applied (relay data/b726_frontdoors.txt).' % (
                 f['fd_items'], f['fd_load'], f['fd_silent'], f['fd_differ'], int(f['fd_papers']) + int(f['fd_readmes'])), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b726_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b726_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b726_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b726 `%s` (previous `%s`, b725’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b726_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b726_standing_v160.txt); the standing '
             'report tool (relay data/b726_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; SIDE-explicit-formula’s c2-b725 at `%s`, cut from main `%s`, the act’s %d '
              'dispatches each read by its run id (relay data/b726_dispatch_rows.json); the %s branches as b725 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_BRANCHES[1][1][:8], K.EF_BASE[:8], len(K.EF_RUNS), K.REBUILD_BRANCH,
                  K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b726_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b725’s %s, %s, %s, %s (relay data/b726_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b726_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b725():
    """b725's trail record over b725's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R336)(3)`s, eighteen at most, each by `gh workflow run build-module.yml`; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: each read by its id; MEASURED off data/b726_dispatch_rows.json against the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b726*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### (R336)(3), N5: keiper-b725 and c2-b725, kept, none cut; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b725 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b726*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s two branches', 'EFLEAN', 'EFLEAN', 'files', '### (R336)(3): KeiperTwo.lean on keiper-b725, C2Walk.lean and the eighteen C2Field modules on c2-b725; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: no main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R336)(8): relay push-b725-closing, push-b725-preroot, push-b725-record; PLACE-papers push-b725-preroot, push-b725-record; each local, by name, after --merged listed it (data/b726_stepzero.txt :18-:19).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: the branch carries its Lean files and print_targets.txt alone, the workflow main`s.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R336) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (06af23f0) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R336)(1)-(2): FINDINGS :11801.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R336)(1)-(2): one row, b725`s (46).'),
    ('root-chain corrigendum rows written', 1, 1, 'rows', '### (R336)(2)(ii): b723`s row at data/act_roots.txt :105, on its branch corrigendum-b723; no row edited.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: W-ORD-SILENT-SENTENCES discharged, W-ORD-MECHANISM-TABLE annotated and carried OPEN.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b726_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R336)(2)-(7): the price table, v1.6.0`s controls, b723`s row, the C2 bank, the edition`s diff, the front-door list, the mechanism table, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none: b726 registers nothing; the next stands at b727, its M and A read before it.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 19, 19, 'modules', '### (R336)(3): C2Walk.lean edited and the eighteen C2Field modules on c2-b725.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R336)(2)(iii): tools/standing/ to v1.6.0 -- G-CLOSING-SENTENCE and G-RULE-SCORES-BEFORE-SEAL, each with its control; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; data/b675_corrigenda.txt`s row (46), appended; data/act_roots.txt at b723`s row and the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation, push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R332)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b726_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, the dispatches and run reads, six anonymous Zenodo record reads and the arXiv reads; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b726 registers nothing: no figure bank of a registered object this act
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=jcount('b726_dispatch_rows.json', lambda j: len([x for x in j if x.get('kind') == 'read'
                                                                            and int(x.get('run') or 0) in set(int(r) for _i, r in K.EF_RUNS)])),
                    REPROWS=jcount('b726_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b726_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('price', 'standing_v160', 'root_row', 'c2', 'edition_diff', 'frontdoors', 'mechanisms', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b726_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b726_registration_%s.txt -- b726, THE WAVE 1 ACT: b725 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.6.0 AND "
                             "b723`S ROW ON ITS BRANCH; THE C2 BUILD PER FIELD ON c2-b725, EIGHTEEN DISPATCHES AT MOST; WHICH STRUCTURE CONFINES v2.4.0; "
                             "THE FRONT-DOOR LIST AND THE LLM LINE; THE MECHANISM TABLE, UNDER (R336)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b725's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b726: b725's lines read banks this
act does not write, and are not carried; the lines are b726's: the C2 certificates on c2-b725, each run by its id (KERNEL), tools/standing/ v1.6.0
by its controls (CERTIFIED), the edition, the front-door list, the LLM line, the mechanism table and b723's row (REGISTERED), and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b726's lines, each from the record tool's figures over b726's banks
    # ------------------------------------------------------------------ KERNEL: THE C2 CERTIFICATES ((R336)(3)), each run read by its id
    sk = seat('%s_c2.txt' % ACT, '**THE C2 THEOREM: ')
    keys['C2'] = ('KERNEL -- THE C2 CERTIFICATES ON c2-b725 (%s): compiled at %s of 18 by decide +kernel, %s, each run read by its id; not compiled: %s; what remains %s; '
                  'the statement E0 DERIVES; dispatches %s of 18; no main, no tag. SOURCE %s.' % (
                      f['c2_tip'], f['c2_k'], f['c2_ax'].lower(), f['c2_left'], f['c2_remains'], f['c2_dispatches'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.6.0 ((R336)(2)(iii)), by its controls
    sw = seat('%s_standing_v160.txt' % ACT, '**v1.6.0: CONTROLS ')   # ### appended by the template after this section
    keys['V160'] = ('CERTIFIED -- tools/standing/ v1.6.0: G-CLOSING-SENTENCE and G-RULE-SCORES-BEFORE-SEAL, controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v160_ctl'], f['v160_cases'], f['v160_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the edition, the list, the LLM line, the table, b723's row
    se = seat('%s_edition_diff.txt' % ACT, '**WHICH STRUCTURE CONFINES v2.4.0: ')
    keys['ED'] = ('REGISTERED -- WHICH STRUCTURE CONFINES v2.4.0: H28a HELD, VACUOUS on its work-list rows; H28b %s against %s; H28c HELD; beside v2.3.1, unedited; deposited nowhere. SOURCE %s.' % (
        f['ed_diff'], f['ed_bound'], se['text']))
    seats.append(se)
    sf = seat('%s_frontdoors.txt' % ACT, '**THE FRONT-DOOR LIST: ')
    keys['FD'] = ('REGISTERED -- THE FRONT-DOOR LIST: %s items, %s load-bearing and %s silent of %s EXCEEDS; assembled and not applied. SOURCE %s.' % (
        f['fd_items'], f['fd_load'], f['fd_silent'], f['fd_exceeds'], sf['text']))
    seats.append(sf)
    keys['LLM'] = ('REGISTERED -- THE LLM LINE: read at %s papers and %s READMEs against the monograph`s, %s differing, listed; the edition carries it. SOURCE %s.' % (
        f['fd_papers'], f['fd_readmes'], f['fd_differ'], sf['text']))
    sm = seat('%s_mechanisms.txt' % ACT, '**THE MECHANISM TABLE: ')
    keys['MECH'] = ('REGISTERED -- THE MECHANISM TABLE: %s rows from the banks, %s reads as wanted, asserting nothing about zeta, the order OPEN for its fourth row. SOURCE %s.' % (
        f['me_rows'], f['me_reads'], sm['text']))
    seats.append(sm)
    sc = seat('%s_root_row.txt' % ACT, "**b723'S ROW CARRIED ON ")
    keys['ROOTROW'] = ('REGISTERED -- b723`S ROW: carried on corrigendum-b723 (%s, sha %s), the row at act_roots :%s; verify %s; main untouched. SOURCE %s.' % (
        f['rr_tip'], f['rr_sha'], f['rr_row'], f['rr_verify'], sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R336)(9))
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['C2']), ('CERTIFIED', ['V160']), ('REGISTERED', ['ED', 'FD', 'LLM', 'MECH', 'ROOTROW']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b726 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
