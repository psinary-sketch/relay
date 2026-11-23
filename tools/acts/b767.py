# -*- coding: utf-8 -*-
# b767 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R377)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R377)(2) repair it carries. Edited by the Edit tool. Carried at b767 by tools/b767_fold.py (`carry`) from tools/acts/b766.py,
# b766`s names substituted; the citation`s sections adopted from tools/b767_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b766`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b766`s carried till
# then); the loader prints them at every load, and the seal wants every PENDING line empty.
#⟪DEAD checks ⟫
#⟪DEAD citation ⟫
#⟪DEAD closing ⟫
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
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
# ### b765, Component 1: THE c1 ROUTE FOR b764'S SHORT CORRIGENDUM, (R375)(1), written by the Edit tool against b764's banks (69 events, 15
# ### post-seal events, 13 defects, 7 refusals as the bank stands; its post-seal rows (70)-(84) appended at step [21] by their route and
# ### committed with its closing, relay e9893630), the three findings after b764's lock, entered as this act's events from the seat's own
# ### closing message (data/b765_events.txt (19)-(21)), and the navigator's claims (i)-(vi), entered as the navigator's, CLAIM (rows
# ### (22)-(27)), printed in full in the ruling's words read from the ferry bank (data/b765_ferry.txt :11), each row read against them.
# ### b764's banks carry five CLAIM rows (its events (25)-(29)), each printed in full in its bank's words. (1) states b764's weight from its
# ### closing message and its report and orders no line of its own, so the weight route refuses; it orders no [I1] and no next line. b764's
# ### route (tools/acts/b764.py :28-:284) carried by hand in place of the stub, the post-seal bank read beside the events and defects banks
# ### (b755's form of the foot, read by this module's citation reader); nothing composed by the stub. The title under the title rule: no
# ### backtick (titlerule.py, v1.35.8).
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
# ### b766, Component 1 (the Edit tool): b765's route (tools/acts/b765.py :38-:284) carried by hand in place of the stub for (R376)(1), set to
# ### b765's banks: its events (1)-(79), its post-seal rows (80)-(91) appended at step [21] and committed with its closing c90a62d7, its
# ### defects (a)-(w), its refusals bank as it stands; its seven CLAIM rows (events (10) and (22)-(27); the counter at data/b765_closing.txt
# ### :5, CLAIM 7) printed in full; b766's events (20)-(23) as the four findings after b765's lock and (24)-(31) as the navigator's claims
# ### (i)-(viii), each read against the ferry bank's :11. The navigator's sums and the nine defects of one class printed as the navigator's.
# ### b767, Component 1 (the Edit tool): b766's route (tools/acts/b766.py :38-:300) carried by hand in place of the stub for (R377)(1), set to
# ### b766's banks: its events (1)-(131), its post-seal rows (132)-(147) appended at step [21] and committed with its closing b635bc94, its
# ### defects (a)-(v), its refusals bank as it stands; its eight CLAIM rows (events (24)-(31); the counter at data/b766_closing.txt :5, CLAIM
# ### 8) printed in full; b767's events (20)-(30) as the eleven findings after b766's lock, in the closing message's order, and (31)-(39) as
# ### the navigator's claims (i)-(ix), each read against the ferry bank's :11. The navigator's five figures of (R377)(1) printed as the
# ### navigator's; (R377)(1) gives no letters of one class, so b766's C1_NAV_NINE is not carried. A '<' in a bank's words escaped for the
# ### ledger, as '*' and '_' are (claim (ix) names push-<act>-*).
C1_WRITTEN = True
C1_NOTED = '2026-11-23'
C1_CORRIGENDA_LAST = 86
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b766_events.txt'), ('postseal', 'b766_events_postseal.txt'), ('defects', 'b766_defects.txt'))
C1_EVENTS_N = 131
C1_AFTER_LOCK = (132, 147)   # ### b766's post-seal rows, appended at step [21] by tools/standing/append.py (07:33:33Z) and committed with its closing, b635bc94
C1_AFTER_LOCK_COMMIT = 'b635bc94'
C1_LOCK_COMMIT = '9ae3ed95'   # ### b766's lock (step 96, 02:09:38Z; data/b766_events_postseal.txt (132))
C1_DEFECTS = (22, 'v')
C1_REFUSALS = 5   # ### the bank as it stands, its working change uncommitted while it holds a profile path
C1_CLAIMS = tuple(('events', str(i_)) for i_ in range(24, 32))   # ### b766's banks: eight CLAIM rows, its events (24)-(31), the navigator's claims of (R376)(1) (the counter at data/b766_closing.txt :5, CLAIM 8)
C1_HEAD = ('b766 closed: relay 603451cf, PLACE-papers 29de083; suite 109 of 116;', '5 prompts answered; scores 4 of 8 HELD; 22 defects')   # ### data/b766_closing.txt :1, read by the state
C1_FINDINGS_BANK = 'b767_events.txt'
C1_FINDINGS_IDS = tuple(str(i_) for i_ in range(20, 31))
C1_FINDINGS_REPEAT = 8   # ### the seat's tags: (20), (23) and (29) NEW; the other eight REPEAT, those held by b766's post-seal rows tagged from them
C1_NAV_IDS = tuple(str(i_) for i_ in range(31, 40))
C1_NAV_MARKS = ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix')
C1_RULED = (('20', ('04:09:43Z', '02:03Z', '(138)')), ('21', ('03:37:22Z', '06:14:05Z', '07:30:18Z')), ('22', ('04:45:11Z', '04:46:24Z', '04:47:50Z')),
            ('23', ('04:48:23Z',)), ('24', ('04:52:23Z', 'limits.py')), ('25', ('04:52:34Z', '04:53:45Z')),
            ('26', ('06:17:52Z', '06:19:13Z', '06:21:00Z')), ('27', ('05:28:12Z', '06:26:43Z', '11.14 s', 'twelve')),
            ('28', ('07:30:18Z', '--rerun-postpush')), ('29', ('07:41:56Z', '07:42:08Z', 'private')), ('30', ('07:44:56Z',)))   # ### the closing message's "Found after the lock", its eleven items in its order
C1_NAV_SUMS = ('21.43', '8.61', '12.82', '11.02', '13.70')   # ### (R377)(1), the navigator's reading of the closing message's table, printed as the navigator's
C1_CORR_TITLE = ('## Corrigendum to b766’s record, short (relay data/b766_events.txt rows (1)-(131), data/b766_events_postseal.txt rows (132)-(147) and '
                 'data/b766_defects.txt (a)-(v)): its events and defects by count from their banks, its eight CLAIM items printed in full, the eleven '
                 'findings after the lock entered as events with their times, and the navigator’s claims entered as CLAIM')
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
    """a bank's own words for the ledger (b754's form, carried): markdown's marks escaped, '<' among them (b767); a pair of backticks quoting a
    span read as quotes, every other backtick as an apostrophe; the template's placeholder brackets as angles."""
    s = s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('<', '\\<')
    s = re.sub(r'(^|[\s(\[])`([^`]{1,60}?)`', r'\1‘\2’', s)
    return (s.replace('`', '’')
            .replace('\u27ea', '\u2039').replace('\u27eb', '\u203a'))


def _c1_sq(s):
    """straight single quotes for the ledger: a pair around a short span read as ‘…’, every other one as an apostrophe (b761, Component 1)."""
    return re.sub(r"(^|[\s(\[])'([^'\s]{1,40})'", '\\1‘\\2’', s).replace("'", '’')


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


def _c1_nav():
    """the navigator's claims, (i)-(ix), in (R377)(1)'s words: the ferry bank's one line opening "(1) b766 AT ITS WEIGHT.", its text after
    "CLAIM items: " cut at each mark, the marks standing after a full stop and a space; [(mark, words)], the words with their closing ";"
    or "." removed. Any other count exits, nothing composed."""
    (t_,), _l = _c1_fl('%s_ferry.txt' % ACT, r"^\(1\) b766 AT ITS WEIGHT\..*?THE NAVIGATOR'S CLAIMS, entered in it as CLAIM items: (.*)$", 'the navigator`s claims')
    parts = re.split(r'(?:^|(?<=\. ))\((i|ii|iii|iv|v|vi|vii|viii|ix)\) ', t_)
    items = [(parts[i], parts[i + 1].rstrip().rstrip(';.').rstrip()) for i in range(1, len(parts) - 1, 2)]
    if [m_ for m_, _w in items] != list(C1_NAV_MARKS):
        sys.exit('### THE NAVIGATOR`S CLAIMS: MARKS %s, NOT (i)-(ix) -- NOTHING COMPOSED' % [m_ for m_, _w in items])
    return items, _l


def _c1_state():
    s = dict((k_, _c1_rows(n_)) for k_, n_ in C1_BANKS)
    ev, ps, df = s['events'], s['postseal'], s['defects']
    tot = _c1_tally(ev + ps + df)
    cnt, l_cn = _c1_fl('b766_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    head = _c1_rd('b766_closing.txt').split(NL)[0]
    rf = [l for l in _c1_rd('b766_hook_refusals.txt').split(NL) if l.strip()]
    kinds = {}
    for l in rf:
        m = re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ \| ([A-Z]+) \| ', l)
        kinds[m.group(1) if m else '?'] = kinds.get(m.group(1) if m else '?', 0) + 1
    cr_ = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    own = dict((r[0], r) for r in _c1_rows(C1_FINDINGS_BANK))
    fnd = [own.get(i_) for i_ in C1_FINDINGS_IDS]
    nav_rows = [own.get(i_) for i_ in C1_NAV_IDS]
    nav, l_nav = _c1_nav()
    nav_bad = [i_ for i_, r, (m_, w_) in zip(C1_NAV_IDS, nav_rows, nav)
               if not (r and r[1] == "THE NAVIGATOR'S" and r[2] == 'CLAIM' and r[4].startswith('(%s) %s' % (m_, w_)))]
    claims = [(k_, r) for k_, _n in C1_BANKS for r in s[k_] if r[2] == 'CLAIM']
    ruled = [(i_, w_) for i_, ws_ in C1_RULED for w_ in ws_ if not (own.get(i_) and w_ in own[i_][4])]
    ferry11 = _c1_rd('%s_ferry.txt' % ACT).split(NL)[l_nav - 1]
    bad = [k_ for k_, ok_ in (
        ('the closing`s head as (1) reads it', all(h_ in head for h_ in C1_HEAD)),
        ('the event rows (1)-(%d)' % C1_EVENTS_N, [int(r[0]) for r in ev] == list(range(1, C1_EVENTS_N + 1))),
        ('the post-seal rows (%d)-(%d)' % C1_AFTER_LOCK, [int(r[0]) for r in ps] == list(range(C1_AFTER_LOCK[0], C1_AFTER_LOCK[1] + 1))),
        ('the defect rows %d, the last (%s)' % C1_DEFECTS, len(df) == C1_DEFECTS[0] and df[-1][0] == C1_DEFECTS[1]),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev) + len(ps)) == tuple(int(x) for x in cnt)),
        ('the CLAIM rows %s' % [(k_, r[0]) for k_, r in claims], [(k_, r[0]) for k_, r in claims] == list(C1_CLAIMS)),
        ('the refusals %d, each by its kind' % C1_REFUSALS, len(rf) == C1_REFUSALS and '?' not in kinds),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the eleven findings, each with its date and time', all(fnd) and all(_c1_time(r[4]) for r in fnd)),
        ('the findings` REPEAT %d as the sentence prints it' % C1_FINDINGS_REPEAT, all(fnd) and _c1_tally(fnd)['repeat'] == C1_FINDINGS_REPEAT),
        ('the findings, each in its row: missing %s' % ruled, not ruled),
        ('the navigator`s claims, each a CLAIM row in the ruling`s words: off %s' % nav_bad, not nav_bad),
        ('the navigator`s five figures, each in (1)`s line', all(('%s hours' % x_ in ferry11) or ((' %s ' % x_) in ferry11) for x_ in C1_NAV_SUMS)),
    ) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (the tally %s)' % (bad, tot))
    s.update(tally=tot, l_counter=l_cn, refusals=len(rf), kinds=kinds, findings=fnd, claims=claims, nav=nav, l_nav=l_nav, nav_rows=nav_rows)
    return s


def _c1_lines(s):
    t = s['tally']
    per = dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS)
    kinds = ', '.join('%s %d' % kv for kv in sorted(s['kinds'].items(), key=lambda kv: (-kv[1], kv[0])))
    pe, pp, pd = per['events'], per['postseal'], per['defects']
    ft = _c1_tally(s['findings'])
    L = ['*b766 closed at relay b635bc94 and PLACE-papers 29de0836, suite 109 of 116, scores 4 of 8 HELD, 22 defects, 5 prompts answered, the act '
         'root 1f57b5d3 (relay data/b766_closing.txt :1, its head naming 603451cf, the tip of push-b766-record when the head was written); the '
         'relay’s main read back at a0bc04cd after the closing push. Its events bank (relay data/b766_events.txt) carries %d rows, (1)-(%d): CLAIM %d, '
         'CLOSE %d, REPEAT %d; it stood as committed from its lock (relay %s). Its post-seal events bank (relay data/b766_events_postseal.txt) carries '
         '%d rows, (%d)-(%d), appended at step [21] of the close order by its route and committed with its closing (relay %s): CLAIM %d, CLOSE %d, '
         'REPEAT %d. Its defects bank (relay data/b766_defects.txt) %d lettered rows, (a)-(%s): CLAIM %d, CLOSE %d, REPEAT %d. Together CLAIM %d, '
         'CLOSE %d, REPEAT %d of %d, as b766’s closing counter prints it (relay data/b766_closing.txt :%d). Its refusals bank %d lines as it stands '
         '(relay data/b766_hook_refusals.txt, its working change uncommitted while it holds a profile path, not among the files `(R377)`(3) names), '
         'by kind %s. Each item is tagged in its own bracket; the tags are the banks’ own and this entry edits none of them. Its %d CLAIM items are '
         'printed in full below.*' % (
             pe['total'], pe['total'], pe['claim'], pe['close'], pe['repeat'], C1_LOCK_COMMIT, pp['total'], C1_AFTER_LOCK[0], C1_AFTER_LOCK[1],
             C1_AFTER_LOCK_COMMIT, pp['claim'], pp['close'], pp['repeat'], pd['total'], C1_DEFECTS[1], pd['claim'], pd['close'], pd['repeat'],
             t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds, len(s['claims'])), '']
    L += ['**b766’s CLAIM items**, each printed in full in its bank’s words (relay data/b766_events.txt rows (24)-(31), the navigator’s claims of '
          '`(R376)`(1)): %s.' % '; '.join(
              '(%s) %s [CLAIM ; %s]' % (r[0], _c1_sq(_c1_q(r[4]).rstrip('.')), _c1_col(r[3])) for _k, r in s['claims']), '']
    L += ['**The findings after b766’s lock**, entered as events of b767 from the seat’s closing message (transcript line 297219, '
          '2026-11-23T07:52:51Z), each time as the message gives it (relay data/b767_events.txt rows (20)-(30)), each on 2026-11-23; b766’s '
          'post-seal rows (133), (138), (141), (142) and (144) to (146) hold the first eight and are not edited, the last three standing in the '
          'message alone. CLAIM %d, CLOSE %d, REPEAT %d of %d, the seat’s tags. %s.' % (
              ft['claim'], ft['close'], ft['repeat'], ft['total'],
              '; '.join('(%s) %s, %s [%s ; %s]' % (r[0], _c1_sq(_c1_q(_c1_head(r[4]))), _c1_time(r[4]), r[2], _c1_col(r[3])) for r in s['findings'])), '']
    L += ['**The navigator’s claims**, each entered as the navigator’s, CLAIM, in the words of `(R377)`(1) (relay data/%s_ferry.txt :%d; relay '
          'data/b767_events.txt rows (31)-(39)), printed in full: %s.' % (
              ACT, s['l_nav'], '; '.join('(%s) %s [CLAIM ; %s]' % (m_, _c1_sq(_c1_q(w_)), _c1_col(r[3])) for (m_, w_), r in zip(s['nav'], s['nav_rows']))), '']
    L += ['**The navigator’s figures**, printed as the navigator’s and banked nowhere by the seat (`(R377)`(1)): by the navigator’s reading of the '
          'closing message’s table, of %s hours of step rows, %s stand under Component 3 and %s under step zero, Components 1, 2 and 5, the gate, '
          'the lock, the seal and the pre-root; the prompt on the two stops was put %s hours after the opening row and the closing came %s hours '
          'after that prompt.' % C1_NAV_SUMS, '']
    L += ['*Filed at b767 on the author’s ruling `(R377)`(1): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b767.py) from b766’s events, post-seal events, defects and refusals banks read unedited and b767’s events '
          'rows (20)-(39); banked as relay `data/b767_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers '
          'b766’s record; no sealed tool, face, trail or root-named bank of b766 is edited. No weight line is written: `(R377)`(1) states b766’s weight '
          'from its closing message and its closing bank. `(R377)`(8) orders one key in Component 1, [K25], the kernel route opened for b767, its row '
          'in relay data/b767\\_repairs.txt; the lettered defects of b766, and G-DELETES-ONE-BRANCH failing beyond the face (its cause read at b767’s '
          'step zero, relay data/b767\\_misses.txt (1)), are read for their classes at the next reading of the close.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    ft = _c1_tally(s['findings'])
    return (['b767 -- THE CORRIGENDUM FOR b766, SHORT, (R377)(1) (%s)' % utc(), '',
             '### the banks read unedited: data/b766_events.txt rows (1)-(%d), data/b766_events_postseal.txt rows (%d)-(%d), data/b766_defects.txt %d '
             'rows, data/b766_hook_refusals.txt %d lines as it stands; data/b766_closing.txt :1 (the head) and :%d (the counter); data/%s rows (20)-(30) '
             '(the findings after the lock) and (31)-(39) (the navigator`s claims, read against data/%s_ferry.txt :%d); the corrigenda bank`s last row '
             '(%d).' % (len(s['events']), C1_AFTER_LOCK[0], C1_AFTER_LOCK[1], len(s['defects']), s['refusals'], s['l_counter'], C1_FINDINGS_BANK, ACT,
                        s['l_nav'], C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, POST-SEAL %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEMS OF b766`S BANKS %d, PRINTED '
               'IN FULL ; THE FINDINGS AFTER THE LOCK %d: CLAIM %d, CLOSE %d, REPEAT %d ; THE NAVIGATOR`S CLAIMS %d, CLAIM %d ; THE NAVIGATOR`S FIGURES '
               'PRINTED AS THE NAVIGATOR`S ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['postseal']), len(s['defects']), t['claim'], t['close'], t['repeat'], len(s['claims']),
                   ft['total'], ft['claim'], ft['close'], ft['repeat'], len(s['nav']), sum(1 for r in s['nav_rows'] if r[2] == 'CLAIM'), ln)])


def c1(*a):
    """`c1 corrigendum [dry|write]`: the short corrigendum for b766, landed through b698's guarded landing (the title rule of v1.35.8 in front of
    it); dry prints and writes nothing. (R377)(1) orders no weight line and no next line: `c1 weight` and `c1 next` refuse."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        sys.exit('### (R377)(1) ORDERS NO WEIGHT LINE FOR b766 -- NOTHING COMPOSED')
    if route == 'next':
        sys.exit('### (R377)(1) ORDERS NO NEXT LINE -- NOTHING COMPOSED HERE')
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
                                                   after_lock=dict(bank='data/b766_events_postseal.txt', rows=[str(n_) for n_ in range(C1_AFTER_LOCK[0], C1_AFTER_LOCK[1] + 1)], commit=C1_AFTER_LOCK_COMMIT),
                                                   claims=[dict(bank=k_, id=r[0], owner=r[1], column=r[3]) for k_, r in s['claims']], in_full=len(s['claims']),
                                                   findings=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_FINDINGS_IDS), claim=ft['claim'],
                                                                 close=ft['close'], repeat=ft['repeat'], ruling_counts_repeat=None,
                                                                 times=dict((r[0], _c1_time(r[4])) for r in s['findings']),
                                                                 claims=[dict(id=r[0], owner=r[1], column=r[3]) for r in s['findings'] if r[2] == 'CLAIM']),
                                                   navigator=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_NAV_IDS), ferry_line=s['l_nav'],
                                                                  marks=list(C1_NAV_MARKS), claim=sum(1 for r in s['nav_rows'] if r[2] == 'CLAIM'),
                                                                  sums=list(C1_NAV_SUMS)),
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   weight_line=None, row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEMS OF b766`S BANKS %d, IN FULL ; THE FINDINGS %d, CLAIM %d, REPEAT %d ; THE NAVIGATOR`S CLAIMS %d ; FINDINGS :%s' % (
            t['claim'], t['close'], t['total'], t['repeat'], len(s['claims']), ft['total'], ft['claim'], ft['repeat'], len(s['nav']), ln))
        return
    sys.exit('usage: fold.py record c1 corrigendum  [dry | write]')
#⟪END⟫
# ### b754, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b754, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b754's name.
# ### b754's own changes are marked "b754, Component 3". The runner overrides read the act's dispatch rows: (R364)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b754_dispatch_rows.json absent) and the runner arms read VACUOUS.
# ### b765, Component 5 (the Edit tool, defect (s)): SIDE-explicit-formula's workflow read at the act's entering main K.EF_BASE (819e4a83), not
# ### at HEAD -- (4)'s HELD moved main to 0ba9cd61 with the workflow's key, restore and planted input (281 lines against 147), so the diff of
# ### rebuild-b721's tip against HEAD read 137 lines where b721 copied the workflow b764 entered with; against 819e4a83 the wanted three
# ### (scratch wfcmp765.py, read-only, 20:54:22Z); the standing-a2 probe (flag 20:39:23Z) read G-WORKFLOW-FILES FAIL where b764's read PASS
# ### b766, Component 5 (the Edit tool, before any run): b766's K.EF_BASE is main entering b766, 0ba9cd61, the workflow b765 moved there with
# ### its key and restore; b721 copied the workflow of 819e4a83, b765's entering main, so the comparison is read at that commit by its name
# ### here and not through K.EF_BASE, which a carried meaning would have read at 0ba9cd61 (the class (R376)(1) names)
# ### b766 (the standing-a2 probe, 21:10:58Z, defect (q)): the constant first written on this line, between the blocks, which the fold does
# ### not render, so the override raised a NameError at the probe; the override reads the worklist's K.EF_BASE_B765 (819e4a83, b765's
# ### entering main, whose workflow rebuild-b721 copied) in its place
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R363)(7), as b753 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
    than SIDE-frobenius carrying build-module.yml on main; SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's at the
    act's entering main with b721's two lines (the push trigger to the branch, the target fixed) and nothing else, the hold kept; SIDE-kernel's
    tip carrying main's build-module.yml changed in the four places of b723's kdraft4_clear row (data/b723_axiom_rows.json) and nothing else;
    no identifier of the author and no secret at either tip."""
    import difflib
    st = S['rebuild_state'] or {}
    fr, kn = st.get('SIDE-frobenius') or {}, st.get('SIDE-kernel') or {}
    src = read_blob(EF, K.EF_BASE_B765 + ':.github/workflows/build-module.yml') or ''   # ### b766: b721's base by its name, the worklist's EF_BASE_B765 (the note above; defect (q))
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
# ### b765, Component 5 (the Edit tool, defect (r)): the cap read as (R375)(4)'s 13 where b764's override pinned (R374)(7)'s 3 -- `carry.py
# ### ruled` named this override among the readers of MAX_DISPATCHES at step zero (events (7)), and the seat set the arm's description
# ### (checks 56) and not its predicate; the standing-a2 probe (flag 20:39:23Z) read G-RUNNER-READ FAIL, its other six clauses true over
# ### the 22 dispatch rows (scratch runcl765.py, read-only, 20:55:05Z)
# ### b766, Component 5 (the Edit tool, before any run): the cap read as (R376)(4)'s 20 where b765's override pinned (R375)(4)'s 13, `carry.py
# ### ruled` naming this override among the readers of MAX_DISPATCHES at step zero (events (16)); the restore-on kind at most 18 beside it
# ### b767, Component 4 (the Edit tool, before any run; `carry.py ruled` R2 at 09:15:19Z and 12:02:32Z, data/b767_events.txt (17), (51)):
# ### the cap read as (R377)(4)'s 40 where b766's override pinned (R376)(4)'s 20; the restore-on kind at most 36; with the restore off the
# ### trial, the closing build and one repeat of each, the items trial-off, closing and repeat alone (MAX_DISPATCHES_KINDS)
#⟪OVERRIDE checks MARK aed8852d751b 16⟫
def runner_ok(S):
    """N1, b767 ((R377)(4), N1: "the dispatches of SIDE-explicit-formula number at most 40 and are those of (4) and (5)"; b766's form, its cap
    set to the ruled figure MAX_DISPATCHES 40, at most 36 of them with the restore on, and with the restore off the trial, the closing build
    and one repeat of each, and EF_RUNS the run ids as dispatched): every dispatch of the act a row of the dispatch bank, its kernel named,
    its free memory read before the send at or above the hold; the run ids the worklist's, EF_RUNS in SIDE-explicit-formula within
    MAX_DISPATCHES (40) and none in SIDE-dirichlet-mod-24 (M24_RUNS empty, its cap 0), no dispatch row of another kernel; a dispatch row
    present exactly when the worklist names a run; each read once after it by that id, the read's free memory at or above the hold; the
    plant a dispatch row with no kernel and no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    ef_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-explicit-formula']
    m4_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-dirichlet-mod-24']
    on_ = [r for r in ds if r.get('kernel') == 'SIDE-explicit-formula' and str(r.get('restore')).lower() in ('true', 'on')]   # ### b767: the restore-on kind, at most 36
    off_ = [r for r in ds if r.get('kernel') == 'SIDE-explicit-formula' and str(r.get('restore')).lower() not in ('true', 'on')]   # ### b767: the restore-off kind, its items
    kinds_ = dict(K.MAX_DISPATCHES_KINDS)
    return bool(ds) == bool(K.EF_RUNS) and ef_ == list(K.EF_RUNS) and len(ef_) <= K.MAX_DISPATCHES == 40 and m4_ == list(K.M24_RUNS) and len(m4_) <= K.MAX_DISPATCHES_M24 \
        and len(on_) <= kinds_['restore'] == 36 \
        and all(r.get('item') in ('trial-off', 'closing', 'repeat') for r in off_) \
        and sum(1 for r in off_ if r.get('item') == 'trial-off') <= kinds_['trial'] and sum(1 for r in off_ if r.get('item') == 'closing') <= kinds_['closing'] \
        and sum(1 for r in off_ if r.get('item') == 'repeat') <= kinds_['repeat'] \
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
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit (the act named here drifted one act at each carry, b753 at b754 to b758 at b766; the name dropped at b767), naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b766-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b767_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b754, Component 6 (the Edit tool), carried: the step-zero bank words the row "THE --MERGED LISTING, PRINTED BEFORE THE DELETES"
# ### (data/b755_stepzero.txt :55); b758: "THE --MERGED LISTING, before the deletes" (data/b758_stepzero.txt :54); b759, before the lock:
# ### b759's bank words it "THE --MERGED LISTING (18:41Z)" and its deletes "THE DELETES, AFTER THE CHECK" (data/b759_stepzero.txt :60, :62);
# ### b760, Component 6: "THE --MERGED LISTING (08:42:28Z)" and "THE DELETES, AFTER THE CHECK" (data/b760_stepzero.txt :59, :61)
# ### b761, Component 6: "THE --MERGED LISTING (21:59:32Z, scratch merged761.py)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b761_stepzero.txt :63, :65)
# ### b762, Component 6: "THE --MERGED LISTING (10:12:5xZ)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b762_stepzero.txt :64, :66)
# ### b763, Component 3 (the Edit tool): "THE --MERGED LISTING (19:08:17Z)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b763_stepzero.txt :65, :67)
# ### b764, Component 5 (the Edit tool, the act part's probe at 00:56:39Z failing the arm on b763's carried time): "THE --MERGED LISTING
# ### (17:04:09Z, scratch merged764.py)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b764_stepzero.txt :24, :63)
# ### b765, Component 5 (the Edit tool): "THE --MERGED LISTING (10:03:33Z, scratch merged765.py)" and "THE DELETES, AFTER THE CHECK, ONE PER
# ### MESSAGE" (data/b765_stepzero.txt :32, :71), where the carry left b764's time and scratch name
# ### b766, Component 5 (the Edit tool, before any run): "THE --MERGED LISTING (07:00:57Z, scratch merged766.py)" and "THE REMOVALS, AFTER THE
# ### CHECK, ONE PER MESSAGE" (data/b766_stepzero.txt :32, :67), b766's bank naming the deletes by (R376)(3)'s word, "THE REMOVALS"
# ### b767, Component 4 (the Edit tool, before any run): "THE --MERGED LISTING (08:27:50Z, scratch merged767.py)" and "THE REMOVALS, AFTER
# ### THE CHECK, ONE PER MESSAGE" (data/b767_stepzero.txt :27, :58), where the carry left b766's time and scratch name
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING (08:27:50Z, scratch merged767.py)' in z and 'THE REMOVALS, AFTER THE CHECK' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's overrides of checks 1516 and 1659 (hook.py edited by b753's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b754 as it stands
# ### b754, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b767_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b756, Component 6 (the Edit tool): the corrigendum's json (data/b756_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 46, CLAIM 0, CLOSE 46, REPEAT 20, the CLAIM items 0, the corrigenda row (76); the rows stand in the bank by
# ### their banks (data/b756_corrigendum.txt); the template's row range read as the json's counts
# ### b764, Component 5 (the Edit tool, the act part's probe at 00:56:39Z failing the arm): the items set to b764's corrigendum's 127
# ### (data/b764_corrigendum.json; its foot :15), where the carry left b763's 70
# ### b765, Component 5 (the Edit tool): the items set to b765's corrigendum's 97 (CLAIM 5, CLOSE 92; data/b765_events.txt (28)), where the
# ### carry left b764's 127
# ### b766, Component 5 (the Edit tool, before any run): the items set to b766's corrigendum's 114 (CLAIM 7, CLOSE 107; data/b766_events.txt
# ### (32)), where the carry left b765's 97
# ### b767, Component 4 (the Edit tool, before any run): the items set to b767's corrigendum's 169 (CLAIM 8, CLOSE 161; data/b767_corrigendum.json
# ### :5-:8; data/b767_events.txt (41)), where the carry left b766's 114
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 169 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
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
# ### b759, before the lock (the Edit tool): five refs at b759's step zero (the relay's push-b758-closing, -preroot and -record; PLACE-papers'
# ### -preroot and -record, data/b759_events.txt (9)); b759's citation check carries the kept row under (R369)(3), data/b759_citation_check.txt
# ### :56, "| ruling (3) | port-b707 kept on SIDE-lv-conservation | local |"
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and '| ruling (3), N5 | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP   # ### b767: data/b767_citation_check.txt :68
#⟪END⟫
# ### b759, before the lock (the Edit tool): G-DELETES-ONE-BRANCH over b759's deletes -- the five step-zero refs, each by the one-call tool's
# ### delete route, and (3)'s five kernel branches, each removed at its kernel's remote by (4)(i)'s route `<repo> rdelete <branch>`
# ### (data/b759_events.txt (24)), which the standing capture reader (tools/standing/delread.py v1.30.0, its TOOL_ARGS) does not read: the
# ### act's reader below reads them segment by segment as delread reads the delete route, wanted equal to the worklist's KERNEL_DELETES; every
# ### delete of either route read against the ruling's own delete clauses through the standing allowance reader; port-b707 undeleted at its tip
# ### b765, Component 5 (the Edit tool): (R375)(4) sends push-b765-planted's delete from the kernel's clone to the one-call tool's delete route (the
# ### worklist's KERNEL_DELETES, names alone; refused there at 19:19:48Z, not fully merged, KERNEL_DELETES_REFUSED), no rdelete route run for b765:
# ### the deletes the capture holds beyond the step-zero five are KERNEL_DELETES exactly
# ### b766, Component 5 (the Edit tool, before any run): (R376)(7) [K22] removes push-b765-planted at the kernel's remote by the rdelete route
# ### and in its clone by the delete route, [K22] forcing the local delete for that one name (data/b766_events.txt (37)): the rdelete route's
# ### deletes are KERNEL_DELETES exactly, and the delete route's beyond the step-zero five likewise; none refused (KERNEL_DELETES_REFUSED empty)
# ### b767, Component 4 (the Edit tool, before any run): (R377)(12) and N5 remove no kernel branch, so KERNEL_DELETES is empty, no rdelete
# ### route ran and the delete route ran the step-zero five alone (data/b767_events.txt (11)); the predicate reads both as empty beyond the five
#⟪OVERRIDE checks MARK 61379f7e4609 2⟫
        and _rdeletes(S) == list(K.KERNEL_DELETES) and sorted(b for b in got if b not in NAMED_PUSH) == sorted(K.KERNEL_DELETES) and not K.KERNEL_DELETES_REFUSED \
        and STW.deletes_read([('-', b) for b in got + _rdeletes(S)], S['ferry'], STW.words_of(ACTN))['ok'] \
        and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP \
#⟪END⟫
#⟪OVERRIDE checks MARK 23e17a97edcc 1⟫
    ('G-DELETES-ONE-BRANCH', '(⟪RUL⟫)(3), (12): the command capture`s branch deletes, each one branch, no glob, no variable, nothing chained after; the five step-zero deletes of the push-b766-* branches of the relay and PLACE-papers by the tool`s delete route, and no kernel branch removed (the worklist`s KERNEL_DELETES empty, no rdelete route run), each allowed by the ruling`s own delete clause read through tools/standing/allow.py; port-b707 undeleted at its tip; push-b766-proof and push-b767-proof kept; the command bank`s count',
#⟪END⟫
# ### b759, before the lock: b758's override of the plant (plant_every_kept, after b758's lock on the author's word) retired -- v1.36.4
# ### (relay 4622b017, (R369)(4)(ii)) gave tools/standing/allow.py's plant_kept the reading of every covering clause, so the template's
# ### plant line reads b759 as it stands (data/b759_events.txt (25)); the reader of (4)(i)'s rdelete route put in its slot
#⟪OVERRIDE checks MARK 48a0f0acd92b 0⟫
def _rdeletes(S):
    """b759, (R369)(3), (4)(i): the kernel branches removed at a remote by the one-call tool's rdelete route, read from the command capture
    segment by segment as tools/standing/delread.py reads the delete route (gitwrite's RUNS_COMMIT over the segment's commands, quoted strings
    blanked; the words `<repo> rdelete <branch>` closing the segment); an interpreter program or an echo quoting the route reads none."""
    DR = __import__('standing.delread', fromlist=['segments'])
    out = []
    for r in S['cmds']:
        if r['tool'] not in ('Bash', 'PowerShell'):
            continue
        for seg in DR.segments(r['cmd']):
            if any(DR.GW.RUNS_COMMIT.match(c) for c in DR.GW.commands(seg)):
                m = re.search(r'\bcommit\.py[\'"]?\s+(\S+)\s+rdelete\s+(\S+)\s*$', seg.rstrip())
                if m:
                    out.append(m.group(2).strip('\'"'))
    return out


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
                                                                          or (bool(S['report_tool']) and 'tools/acts/b766.py -> tools/acts/b767.py' in (rd('b767_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b767_report.py' not in (S['sealj'].get('tools') or {})   # ### b767, Component 4 (the Edit tool): the carried stub set for the act, b766's body (tools/acts/b766.py :498) with the act's name
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b767_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:   # ### b767, Component 4 (the Edit tool): the carried stub set for the act, b766's body (tools/acts/b766.py :504-:511) with the act's name
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b767')
    return '### THE COUNTER ((R377) Component 5, the act`s events and defects together; relay data/b767_defects.txt, data/b767_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-LI-ARITH carried by [P2] in part, W-ORD-WINDOW-CERTIFY open beside it; W-ORD-SOURCE-BUILD entered by [S1], its route held by [S2], main and v0.45 moved on the closing build from source, no [C7] and no [C8]; W-ORD-NOVEMBER-RIDERS entered by [R1]; W-ORD-RUNNER-CACHE as [C5] left it; [G1] and [A2] entered ((R377)(4)-(7));',   # ### b767, Component 4 (the Edit tool, found carrying b766's orders while the carried readers were read): b767's orders and texts
    '        none entered or retired by the seat; the orders before this act as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged|merged767\.py', c) is not None)   # ### b767, Component 4 (the Edit tool): b766's body, and the scratch that made b767's listing (08:27:50Z, data/b767_stepzero.txt :27), whose git branch --merged runs inside it
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b767_author_answers.txt', 'b767_answer_check.txt', 'b767_events.txt'))   # noqa: E731,E702
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
REG = os.path.join(ROOT, 'data', 'b767_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b767_registration_%s.txt' % __import__('b767_worklist').DATE)   # ### the gate imports no worklist of its own
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
    ('commits on any kernel`s main', 'EFMAINCOMMITS', 'EFMAINCOMMITS', 'commits', (('### (R377)(4): SIDE-explicit-formula`s main moved by the gated push from 0ba9cd61 to the closing Lean commit %s by fast-forward, push-b766-proof`s commits and push-b767-proof`s on it, the closing build from source exiting 0 with the restored build`s axioms file; ' % K.RUNNER_COMMIT[:8])
                                                                                 if K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8] else '### (R377)(4): none -- SIDE-explicit-formula`s main stays at 0ba9cd61, no build from source exiting 0 with the restored build`s axioms file at the closing commit; ') + 'SIDE-dirichlet-mod-24`s main unmoved; MEASURED off git rev-list --count 0ba9cd61..main.'),   # ### b767, Component 4 (the Edit tool): each case of (R377)(4) by the worklist's EF_MAIN
#⟪END⟫
#⟪OVERRIDE regspec MARK 18c1a19a6cb6 1⟫
    ('scratch branches cut on a kernel', 0, 0, 'branches', '### none: no planted build at this act ((R377)(4)), and the standing controls read in the relay`s own tools and scratch repositories (data/b767_repair_controls.txt), no scratch branch of a kernel.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK a2b9535083e6 1⟫
    ('push branches cut on a kernel for the push procedure', 1, 1, 'branches', '### (R377)(4), (9): push-b767-proof cut from push-b766-proof at 3c67b8b5 in SIDE-explicit-formula by the one-call tool`s kernel branch route (12:16:44Z, data/b767_events.txt (58)) and pushed by the gated push`s branch mode, fifteen commits to 89fd5b54; kept at its remote and in its clone, no route removing it; push-b766-proof kept at 3c67b8b5.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 42ab3bdb112d 1⟫
    ('kernel merges made', 0, 0, 'merges', '### none: ' + ('main moved by fast-forward alone, no merge commit ((R377)(4)).' if K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8] else 'main not moved ((R377)(4)).')),
#⟪END⟫
#⟪OVERRIDE regspec MARK 63e5424dd90e 1⟫
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', (('### N5, (R377)(4): %s cut at the closing Lean commit %s after main`s read-back, on the run with the restore off and on no other' % (K.WEIL_TAG[0], K.RUNNER_COMMIT[:8])) if K.WEIL_TAG else '### N5, (R377)(4): none -- v0.45 not cut') + '; v0.38 to v0.44 and v0.2.0 unmoved; MEASURED off SIDE-explicit-formula`s tags past v0.44, SIDE-dirichlet-mod-24`s past v0.2.0, and the template`s other kernels as before.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 5381b10a2ae6 1⟫
    ef_tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() not in ('v0.37', 'v0.38', 'v0.39', 'v0.40', 'v0.41', 'v0.42', 'v0.43', 'v0.44')] + [t for t in _git(K.M24_DIR, 'tag', '--list').split(chr(10)) if t.strip() and t.strip() not in ('v0.1.0', 'v0.2.0')]   # ### b766: v0.38 b745`s, v0.39 and v0.40 b758`s, v0.41 b759`s, v0.42 and v0.43 b763`s, v0.44 b765`s, v0.2.0 b757`s; the tags past them, the act`s own
#⟪END⟫
#⟪OVERRIDE regspec MARK 100638d8d84e 1⟫
    ('kernel branches deleted', len(K.KERNEL_REMOVED), len(K.KERNEL_REMOVED), 'branches', '### (R377)(12), N5: none -- no kernel branch removed; push-b766-proof kept at 3c67b8b5 and push-b767-proof at its remote and in its clone; port-b707, the pin, challenge and rebuild branches and the held branches kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 51acd0ac8ef1 1⟫
    ('branches deleted beyond the step zero`s list', len(K.KERNEL_REMOVED), len(K.KERNEL_REMOVED), 'branches', '### none ((R377)(3), (12), N5): the five push-b766-* refs of the relay and PLACE-papers deleted at step zero by name, and no other; port-b707 kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK b6204f4e0fa8 1⟫
    ('census editions written on main', 0, 0, 'editions', '### none: no census written this act ((R377)(12)).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 0daf7a1cb287 1⟫
    ('papers moved, renamed or written beyond FINDINGS, OPEN_TRAILS and REGISTRY', 0, 0, 'papers', '### none ((R377)(12), N3): no paper written beyond FINDINGS and OPEN_TRAILS, REGISTRY not written; none moved or renamed.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 46160108b751 1⟫
    ('README edits', 0, 0, 'edits', '### none this act: no kernel`s README written.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 2d7a99569826 1⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 'OTBLOCK', 'OTBLOCK', 'lines', '### (R377)(4)-(7): blocks at the file`s end, no line moving, each under its dated head by the rulings tool`s groups -- c2 [S1] with W-ORD-SOURCE-BUILD`s entry line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS` entry line, [A2]; c5 [P2], [S2] -- by two PLACE-papers commits (ba23945a and adadfd62)' + (', and the closing pair`s text by a third' if os.path.exists(os.path.join(ROOT, 'data', 'b767_ledgers_c6.json')) else '') + '; MEASURED off relay data/b767_ledgers_c2.json and _c5.json`s OPEN_TRAILS rows.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 44ff8bc9f5d4 1⟫
    ('faces ledger update blocks appended', 0, 0, 'blocks', '### none: FACES_LEDGER not written this act ((R377)(13)`s (W) list).'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b767_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
#⟪END⟫
# ### b755, Component 6 (the Edit tool): G-SCORER-READS-BANKS's needles set to the banks b755's N1-N4 read (the command bank and the
# ### dispatch rows, N2's controls and first adds, the walk among the figure banks, the seal and step banks), the carried stub's refusal
# ### removed; the ledger exclusion unchanged. The arm stands in tools/standing/arms.py's RETIRED and is not in the run list; read so, its
# ### template line :971 would fire on N3's label of the landed entry (record.tpl :2444, a string naming FINDINGS.md), not edited here
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    # ### b764, Component 2 (the Edit tool), at [K5]'s needle call: the carried stub's refusal taken out, b763's body kept as it stood (the arm RETIRED);
    # ### b765, Component 5 (the Edit tool): the carried stub's refusal taken out again, the body as it stood; b766, Component 3 (the Edit tool): again;
    # ### b767, Component 4 (the Edit tool): again
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmno'))   # ### b767, Component 4 (the Edit tool, before any run): the rows of data/b767_defects.txt as the template's reader takes them, (a) to (o), each THE SEAT'S ((a)-(d) at step zero, (e)-(h) at Component 2, (i)-(n) at Component 3, (o) at Component 4), where the carry left b766's (a) to (u); set again at the seal where a row is added; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b767_misses.txt', 'data/b767_price.txt', 'data/b767_price.json', 'data/b767_ceiling.txt',          # ### step zero, (3); the ceiling read before the lock
                  'data/b767_author_words_preseal.txt',                                                                  # ### the author's words, step zero to the close
                  'data/b767_corrigendum.txt', 'data/b767_corrigendum.json',                                             # ### Component 1, (1)
                  'data/b767_repairs.txt', 'data/b767_repair_controls.txt', 'data/b767_standing_dry.txt', 'data/b767_kernel_bases.json',   # ### Component 1, (8)
                  'data/b767_certificate.txt', 'data/b767_certificate.json', 'data/b767_plan.txt',                       # ### (4)(a)
                  'data/b767_source_build.txt',                                                                          # ### (5)(a), (b)
                  'data/b767_registration.txt', 'data/b767_window.txt', 'data/b767_window.json',                         # ### (6)
                  'data/b767_controls_control.txt', 'data/b767_dispatch_rows.json', 'data/b767_controls.txt',            # ### (4)'s and (5)'s dispatches and the tool's bank
                  'data/b767_logdata.txt', 'data/b767_natdata.txt',                                                      # ### (4)(c) and (d), the data files of L10a and L11b
                  'data/b767_ledgers_c2.txt', 'data/b767_ledgers_c5.txt',                                                # ### the lines of (4)-(7); c6 joins where [C7] or [C8] is entered
                  'data/b767_orders.txt',
                  'data/b767_reproduce.txt', 'data/b767_reproduce.json',                                                 # ### (12)
                  'data/b767_author_answers.txt', 'data/b767_address_scan.txt', 'data/b767_touch.txt',   # ### b767, Component 4 (the Edit tool, before any run): the act's banks by its components, in place of b766's carried names (its captures' mask, seven data files, three readings and groups c3 and c4, none written by b767); no rules bank this act; the template's standing banks follow
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b767_address_scan.py'), 'scan'], capture_output=True, text=True,
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
    """(R372)(1)-(12): the act's relay commits after step zero in their order, (key, commit) -- v9, then the worklist's CHAIN (the ceiling
    tool, the c1 route, the corrigendum banks, the registration alone, the map tool and its two repairs and its bank, the page tool and its
    bank, the rulings tool and its banks with the roster, the reproduce run), then the handoff page and the lock gate where each is made and
    not already in CHAIN, in
    that order; read from the worklist at the call. A lock gate tool committed inside CHAIN is read at its place there and not again (N2's
    "each act tool commits before it runs" read there)."""
    # ### b765, (R375)(8) [K21] (the Edit tool): the tail placed by its commit time among CHAIN by tools/standing/act.py chain_in_time()
    # ### (v1.38.20), where b764's form appended it in a fixed order after CHAIN and read its lock gate's carry after its handoff
    return STANDING_ACT.chain_in_time(('v9', K.STANDING_COMMIT), K.CHAIN,
                                      (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT), ('lockgate', K.C1_LOCKGATE)),
                                      lambda h_: _ct(ROOT, h_))


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


# ### b767, Component 4 (the Edit tool): the data files' banks of L10a and L11b, neither closing on a bold foot, each read by its controls
# ### line (feet767.py, read-only, 19:51:17Z: no `### ### **` line in either), and the rulings tool's groups c2 and c5, each a bank and a
# ### json of its own; a group c6 joins where [C7] or [C8] is entered, by the Edit that gives the rulings tool that group
DATA_BANKS = (('logdata', r'(?m)^  CONTROLS (\d+) OF (\d+) AS WANTED'), ('natdata', r'(?m)^  CONTROLS (\d+) OF (\d+) AS WANTED'))
LEDGER_GROUPS = ('c2', 'c5') + (('c6',) if os.path.exists(os.path.join(D, 'b767_ledgers_c6.json')) else ())
# ### each group's keys as (R377)'s texts enter them (data/b767_ledgers_c2.json and _c5.json `entered`), group c2 with its two orders'
# ### entry lines beside [S1] and [R1]
LEDGER_KEYS = dict(c2=['A2', 'G1', 'R1', 'S1'], c5=['P2', 'S2'])
LEDGER_ENTRY_LINES = dict(c2=2, c5=0)


def _gwb_state():
    """b766, N2: each row of K.GENS_WITH_BANK -- the tool's first add, the files of the commit carrying both, the bank in the working
    tree and its blob at that commit, the bank's last commit, and the times of the first add and of that commit."""
    out = {}
    for n_, tool_, data_, both_, _k in K.GENS_WITH_BANK:
        fa_ = [h_ for h_ in gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', tool_).split() if h_.strip()][-1:]
        out[n_] = dict(tool=tool_, data=data_, both=both_, first=fa_, both_files=files_of(ROOT, both_), bank=rd(data_.split('/', 1)[1]),
                       blob=_s(blob(ROOT, '%s:%s' % (both_, data_))), last=gs(ROOT, 'log', '-1', '--format=%H', '--', data_).strip(),
                       t_first=_ct(ROOT, fa_[0]) if fa_ else None, t_both=_ct(ROOT, both_))
    return out


def _gwb_ok(S):
    """each row of K.GENS_WITH_BANK: the tool first added by a commit before the one carrying both, that commit carrying the tool and
    the bank, the bank last committed there and at HEAD its blob there; (name, ok) each."""
    out = []
    for n_, d_ in sorted((S['gwb'] or {}).items()):
        b_ = _txt(d_.get('bank'))
        out.append((n_, bool(b_) and b_ == _txt(d_.get('blob')) and bool(d_.get('first')) and d_['tool'] in (d_.get('both_files') or [])
                    and d_['data'] in (d_.get('both_files') or []) and (d_.get('last') or '')[:8] == d_['both'][:8]
                    and bool(d_.get('t_first')) and bool(d_.get('t_both')) and d_['t_first'] < d_['t_both']))
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
        # ### b764: each standing version of STANDING_REPAIRS -- the files of its commit and of its row's commit, VERSION's text at its commit,
        # ### and its control's verdict line in the controls bank at HEAD and in that bank's blob at the row's commit
        strepairs=dict((k_, dict(vfiles=files_of(ROOT, c_), rfiles=files_of(ROOT, r_), ver=(_s(blob(ROOT, '%s:tools/standing/VERSION' % c_)) or '').strip(),
                                 line=(_txt(rd('b767_repair_controls.txt')).split(NL) + [''] * (l_ + 1))[l_ - 1],
                                 line_at=(_txt(blob(ROOT, '%s:%s' % (r_, K.REPAIR_CONTROLS_BANK))).split(NL) + [''] * (l_ + 1))[l_ - 1]))
                       for k_, _v, c_, r_, l_ in K.STANDING_REPAIRS),
        st_commits=[h_ for h_ in gs(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()],
        r366_chain=_chain(),
        gens=_gens_state(),
        # ### b767, Component 4 (the Edit tool): the act's banks its arms read -- the repairs bank and its planted control, the certificate
        # ### and the plan, the source-build read, the registration and the window, the dispatch tool's controls and its bank, the data files'
        # ### banks (DATA_BANKS), the rulings tool's groups (LEDGER_GROUPS, each its bank and json), the roster, the price and the ceiling, the
        # ### answers and the author's words; the sha256 (16 hex) of each PLACE-papers file's blob at the commit that wrote it (the worklist's
        # ### PP_WRITES), against which the groups' digests are read; and the row of GENS_WITH_BANK. b766's captures' mask and three readings
        # ### have no counterpart here
        repairst=rd('b767_repairs.txt'), rctlt=rd('b767_repair_controls.txt'),
        trialt=rd('b767_controls.txt'), cctlt=rd('b767_controls_control.txt'), certt=rd('b767_certificate.txt'), certj=jl('b767_certificate.json'),
        plant=rd('b767_plan.txt'), datat=dict((n_, rd('b767_%s.txt' % n_)) for n_, _w in DATA_BANKS),
        sbt=rd('b767_source_build.txt'), regt=rd('b767_registration.txt'), wint=rd('b767_window.txt'), winj=jl('b767_window.json'),
        ledgersj=dict((g_, jl('b767_ledgers_%s.json' % g_)) for g_ in LEDGER_GROUPS),
        ledgerst=dict((g_, rd('b767_ledgers_%s.txt' % g_)) for g_ in LEDGER_GROUPS), orderst=rd('b767_orders.txt'),
        pricej=jl('b767_price.json'), pricet=rd('b767_price.txt'), ceilt=rd('b767_ceiling.txt'),
        answerst=rd('b767_author_answers.txt'), wordst=rd('b767_author_words_preseal.txt'), gwb=_gwb_state(),
        pp_shas=dict(('%s:%s' % (c_[:8], f_), hashlib.sha256(blob(PP, '%s:%s' % (c_, f_)) or b'').hexdigest()[:16]) for _k, f_, c_ in K.PP_WRITES),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        pp_files=dict((k_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        numstat=dict((k_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        kst=_kernel_state(),   # ### b757: the two kernels' refs, tags and the kernel commits' containing refs (G-OFFSET-POST-HOC)
        drows=json.loads(rd('b767_dispatch_rows.json') or '[]'),
        reproduce=rd('b767_reproduce.txt'), reproducej=jl('b767_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b767_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (b759's form); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b767_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [(k_, _ct(PP, h_)) for k_, h_ in K.PP_CHAIN]
               + [('c1', _ct(ROOT, K.C1_RELAY)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)), ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=sorted(set(x_ for h_ in ((K.C1_STANDING,) if isinstance(K.C1_STANDING, str) else (K.C1_STANDING or ())) for x_ in files_of(ROOT, h_))), lockgate=files_of(ROOT, K.C1_LOCKGATE) if K.C1_LOCKGATE else [], c2=[],   # ### b757: the lock gate set when made; no Component 2 relay bank of b756's kind ; ### b765 (the touch read's arm call, 20:03:57Z): C1_STANDING names (8)'s two commits, a tuple where b764's was None, files_of taking one commit; each commit's files read and joined
                   v9=files_of(ROOT, K.STANDING_COMMIT), handoff=files_of(ROOT, K.HANDOFF_COMMIT) if K.HANDOFF_COMMIT else [],
                   **dict([('rc_' + k_, files_of(ROOT, h_)) for k_, h_ in K.CHAIN] + [('pp_' + k_, files_of(PP, h_)) for k_, h_ in K.PP_CHAIN]),   # ### b756: each commit of the two chains by its key
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b755's read-first bank's items by path, the ferry's read-first list in its order (data/b755_readfirst_rows.json); b755 step zero: the
# ### carried stub replaced, one needle for each item of the ferry's list (:44) and for the act's own reads beside it
# ### b756 step zero: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b756_ferry.txt :46), in its order
# ### b757, Component 6: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b757_ferry.txt :41), in its
# ### order, as data/b757_readfirst.txt :14-:35 holds them
# ### b758, Component 5: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b758_ferry.txt :37), in its
# ### order, as data/b758_readfirst.txt :14-:26 holds them
# ### b759, before the lock: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b759_ferry.txt :43), in
# ### its order, as data/b759_readfirst.txt :16-:35 holds them
# ### b760, Component 6: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b760_ferry.txt :43), in
# ### its order, as data/b760_readfirst.txt :16-:37 holds them
# ### b761, Component 6: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b761_ferry.txt :83), in
# ### its order, as data/b761_readfirst.txt :16-:33 holds them
# ### b762, Component 6: the carried stub replaced, one needle for each item of the ferry's read-first list (data/b762_ferry.txt :161), in
# ### its order, as data/b762_readfirst.txt :18-:35 holds them
# ### b763, Component 3 (the Edit tool): the carried stub replaced, one needle for each item of the ferry's read-first list
# ### (data/b763_ferry.txt :135), in its order, as data/b763_readfirst.txt :18-:36 holds them
# ### b764, step zero (the Edit tool): the carried stub replaced, one needle for each item of the ferry's read-first list
# ### (data/b764_ferry.txt :148), in its order, as data/b764_readfirst.txt :18-:37 holds them
# ### b766, step zero (the Edit tool): the carried stub replaced, one needle for each item of the ferry's read-first list
# ### (data/b766_ferry.txt :118), in its order, as data/b766_readfirst.txt holds them under THE FERRY'S READ-FIRST LIST
# ### b767, Component 4 (the Edit tool, the carried stub found while the checks sections were read for their constants): the stub replaced,
# ### one needle for each item of the ferry's read-first list (data/b767_ferry.txt :113), in its order, as data/b767_readfirst.txt :19-:48
# ### holds them, each row by its opening up to its first bar (b766's form)
READFIRST_NEEDLES = (
    'relay data/b766_closing.txt |',
    'relay data/b766_defects.txt |',
    'relay data/b766_events.txt |',
    'relay data/b766_events_postseal.txt |',
    'relay data/b766_misses.txt |',
    'relay data/b766_author_answers.txt |',
    'relay data/b766_author_words_preseal.txt |',
    'relay data/b766_price.txt |',
    'relay data/b766_controls.txt |',
    'relay data/b766_repairs.txt |',
    'relay data/b766_plan.txt |',
    'relay data/b766_certificate.txt |',
    'relay data/b766_certificate.json by its head |',
    'relay data/b766_ledgers_c5.txt |',
    'relay data/b765_registration.txt |',
    'relay data/b765_window.txt |',
    'relay tools/b765_window.py |',
    'relay tools/b766_certificate.py |',
    'relay tools/b766_controls.py |',
    'relay tools/push_gated.sh |',
    'relay tools/project_set.py |',
    'relay tools/standing/commit.py |',
    'relay tools/standing/orders.py |',
    'relay tools/standing/orderstate.py |',
    'PLACE-papers OPEN_TRAILS.md :19221-:19271 |',
    'SIDE-explicit-formula at 3c67b8b5 (push-b766-proof), SIDEExplicitFormula/Window/ |',
    'SIDE-explicit-formula at 3c67b8b5, .github/workflows/build-module.yml |',
    'SIDE-explicit-formula at 0ba9cd61, SIDEExplicitFormula/ControlFailureExists.lean :23-:25 |',
    'SIDE-explicit-formula at 0ba9cd61, SIDEExplicitFormula/GaussArchQ.lean :27-:32 |',
    'SIDE-explicit-formula at 0ba9cd61, SIDEExplicitFormula/GaussArchQSteps.lean :630 |',
)
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R377)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'PRICE AND THE CEILING ((R377)(3))', 'KEY [K25] ((R377)(8))', 'PLAN AND THE CERTIFICATE`S THREE FORMS ((R377)(4)(a))',
 'BUILD FROM SOURCE READ AND ITS ROUTE ((R377)(5)(a), (b))', 'WINDOW AT KNOTS GRADED BY OCTAVE ((R377)(6))',
 'STEPS IN LEAN AND THE TRIAL ((R377)(4)(b)-(e), (5)(c))', 'LINES OF (4) TO (7) ((R377)(4)-(7))',
 'RESEARCH INSTRUMENTS REPRODUCED ((R377)(12), the standing arm G-RESEARCH-REPRODUCES)',
 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')   # ### b767, Component 4 (the Edit tool, where b766's headings stood): closing 7's headings as written over b767's banks, in its order, each without the "THE " the arms prefix
#⟪END⟫
#⟪SECTION checks 12⟫
    """b767, Component 4 (the Edit tool, where b766's figures stood): the citation check's bank: every cite checked, OK and misses summing
    (98 = 98 + 0), no miss; the ferry's paths 53, OK 46, NONE 0, the seven OWN rows apart; the check CLEAN (halts 0: Lean paths and nouns
    0, comparatives 0), banked at 08:55:22Z, as the step-zero bank enters it (data/b767_stepzero.txt :56-:57, after the read-first bank at
    :54-:55, before the removals at :58); the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 98 \
        and '### ### **THE FERRY`S PATHS 53 ; OK 46 ; NONE 0.**' in c \
        and '### ### **THE CHECK CLEAN** (halts 0: Lean paths and nouns 0, comparatives 0)' in c \
        and 'BANKED (08:55:22Z, data/b767_citation_check.txt, .json): CITES CHECKED 98 ; OK 98 ; MISSES 0 ;' in (S['stepz'] or '') \
        and "OK 46 ; NONE 0 ; THE CHECK CLEAN (halts 0) (events (10))" in (S['stepz'] or '') \
        and 'THE REMOVALS, AFTER THE CHECK, ONE PER MESSAGE' in (S['stepz'] or '') \
#⟪END⟫
# ### b754, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b753's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b754, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386).
# ### v1.38.17, (R374)(5) [K4]: the override of :2665-:2667 removed with the retained body it patched (record.tpl :2664-:2750, the MARK
# ### override df786768d1d9 below record 35); the one of :2876-:2878 stands
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b767_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b767, Component 4 (the Edit tool, found carrying b766's needles for b765's record while the carried readers were read), (R377)(1):
    # ### no weight line ordered (data/b767_corrigendum.txt's foot NO WEIGHT LINE), so the record-lines bank holds none; b766 at its weight
    # ### stands in the corrigendum's line, FINDINGS :16080 (PLACE-papers 216d9715, step 7), read through the corrigendum's landing bank, its
    # ### head through conv. The needles are phrases of the head line (the corrigendum json's title, data/b767_corrigendum.json, read by
    # ### the Grep tool at 20:59Z), which `landed` reads alone, in b762's form
    return landed(S if S['rl'] else dict(S, rl=jl('b767_corrigendum_landing.json')), 0,
                  ['b766’s record, short', 'data/b766_events.txt rows (1)-(131)', 'data/b766_events_postseal.txt rows (132)-(147)',
                   'data/b766_defects.txt (a)-(v)', 'its eight CLAIM items printed in full', 'the eleven findings after the lock entered as events with their times',
                   'the navigator’s claims entered as CLAIM'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b767's title by its objects, the ferry's ACT line (data/b767_ferry.txt :109) adjusted to what the act did (record 31's _title over the
# ### banks: b766 at its weight; the one key (data/b767_repairs.txt); the plan amended and the certificate's three forms; the steps by the
# ### keys the rulings tool's groups entered; the source-build read and its trial, the closing build and main and the tag by the dispatch
# ### tool's foot (data/b767_controls.txt); the window at graded knots; the rulings (data/b767_ledgers_c2.txt); the roster
# ### (data/b767_orders.txt); the dispatches); each needle a fixed part of the composed title, with the typographic apostrophe, no
# ### backtick, conv(title) == title; a figure or a verdict a bank gives at the close left out of the needles; read against the composed
# ### title at the dry. No roster token: tools/standing/armnorm.py roster_at_close reads data/<act>_ledgers.json's roster, which b767's
# ### groups do not write (group c2's json holds it). b767, Component 4 (the Edit tool): set to record 31's b767 title, where b766's
# ### needles stood (its three repairs and three readings, none b767's)
TITLE_NEEDLES = ('## The proof by the banked window continued, under (R377): b766 ',
                 ' (b767_corrigendum); one key, with its planted control (b767_repairs); ',
                 'the plan amended and the certificate’s three forms (b767_plan, b767_certificate); the archimedean term in the B-spline basis, '
                 'the enclosures and the pole term’s data half compiled, the proof ',
                 ' (b767_ledgers_c5); the build from source read and its route ', ' at the trial (b767_source_build, b767_controls); the closing build from source at ',
                 ' (b767_controls); the window at knots graded by octave ', ' (b767_registration, b767_window); the author’s rulings entered (b767_ledgers_c2); ',
                 ' (b767_orders); ', ' dispatches')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R377)(1): the generated corrigendum for b766's record landed, short (its line in the json, FINDINGS :16080, the title at that line
    through conv): b766's 131 events, 16 post-seal rows and 22 defects by count from their banks, 169 items, CLAIM 8 and CLOSE 161, REPEAT
    126 (the ruling's counter, data/b767_ferry.txt :11), the eight CLAIM items (b766's events (24)-(31)) printed in full; the eleven
    findings after b766's lock entered as b767's events (20)-(30) (CLAIM 0, CLOSE 11, REPEAT 8), each with its time; the navigator's nine
    claims of (1) entered as b767's events (31)-(39), CLAIM 9; no weight line; the corrigenda bank appended at row (87) and nothing before
    it changed; in Component 1's commits (the figures read from data/b767_corrigendum.json and the bank's foot; b767, Component 4, the Edit
    tool, where b766's figures for b765's record stood)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 87 and j.get('claim') == 8 == len(j.get('claims') or []) and j.get('close') == 161 and j.get('repeat') == 126 and j.get('items') == 169 \
        and '### ### **ITEMS 169: EVENTS 131, POST-SEAL 16, DEFECTS 22 ; CLAIM 8, CLOSE 161 ; REPEAT 126 ; THE CLAIM ITEMS OF b766`S BANKS 8, PRINTED IN FULL ; THE FINDINGS AFTER THE LOCK 11: CLAIM 0, CLOSE 11, REPEAT 8 ; ' in (S['corrt'] or '') \
        and 'THE NAVIGATOR`S CLAIMS 9, CLAIM 9 ; THE NAVIGATOR`S FIGURES PRINTED AS THE NAVIGATOR`S ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :16080.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and [(c_.get('bank'), c_.get('id')) for c_ in (j.get('claims') or [])] == [('events', str(n_)) for n_ in range(24, 32)] and j.get('in_full') == 8 \
        and (j.get('findings') or {}).get('rows') == [str(n_) for n_ in range(20, 31)] \
        and [(j.get('findings') or {}).get(k_) for k_ in ('claim', 'close', 'repeat')] == [0, 11, 8] \
        and (j.get('navigator') or {}).get('rows') == [str(n_) for n_ in range(31, 40)] and (j.get('navigator') or {}).get('claim') == 9 \
        and j.get('weight_line') is None and j.get('entry_line') == K.CORR_LINE == 16080 \
        and '  (87) ' in S['corrigenda'] and '  (88) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R377) orders no rules bank for this act; the rule it works by is b756's, data/b756_rules.txt,
    its rows (a) to (c) in force from b757 by (R366)(2), with b760's row (a) (data/b760_rules.txt); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here b756's rows (a) to (c), lettered as (R366)(2) letters them, in b756's Component 1 commit (relay 0a151012) and no other, the working
    tree its blob at HEAD; no data/b767_rules.txt written (the worklist's C1_RULES None); data/b760_rules.txt and data/b754_rules.txt not
    rewritten by this act."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and re.findall(r'(?m)^  \(([a-z])\) ', rd('b756_rules.txt') or '') == ['a', 'b', 'c'] \
        and not r1 and K.C1_RULES is None and not os.path.exists(os.path.join(D, 'b767_rules.txt')) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', 'data/b754_rules.txt').split()][:1] == [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', K.PRE_RELAY, '--', 'data/b754_rules.txt').split()][:1] \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', 'data/b760_rules.txt').split()][:1] == [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', K.PRE_RELAY, '--', 'data/b760_rules.txt').split()][:1] \
        and _txt(rd('b756_rules.txt')) == _txt(blob(ROOT, 'HEAD:' + K.B756_RULES[0])) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', K.B756_RULES[0]).split()] == [K.B756_RULES[1][:8]] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b767's report lines (report sections 2-5, rewritten at Component 4 by the Edit tool, after the reports' keys were found still b766's
# ### in this section): each key a phrase its line carries, the tier word with it, each line's tier fixed by its key (report 5's order):
# ### the steps compiled and the build from source with main and the tag KERNEL; the one key, the certificate's three forms, the
# ### source-build read, the data files, the dispatch tool and the reproduction run CERTIFIED; the corrigendum, the price, the plan amended,
# ### the window at graded knots and the lines REGISTERED; the proof carried by [P2] and the draft HELD
REPORT_KEYS = ('KERNEL -- THE STEPS OF (4)(b) TO (4)(d) COMPILED', 'KERNEL -- THE BUILD FROM SOURCE TRIED, THE CLOSING PAIR, MAIN AND THE TAG',
               'CERTIFIED -- THE ONE KEY OF (8), BY ITS PLANTED CONTROL', 'CERTIFIED -- THE CERTIFICATE’S THREE FORMS OF (4)(a)',
               'CERTIFIED -- THE READ OF THE TWO STOPPED RUNS AND THE ROUTE OF (5)(a) AND (b)', 'CERTIFIED -- THE DATA FILES OF (4)(c) AND (4)(d)',
               'CERTIFIED -- tools/b767_controls.py BY ITS OWN CONTROLS', 'CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED',
               'REGISTERED -- THE CORRIGENDUM FOR b766, SHORT', 'REGISTERED -- THE PRICE AND THE CEILING OF (3)', 'REGISTERED -- THE PLAN AMENDED OF (4)(a)',
               'REGISTERED -- THE WINDOW AT KNOTS GRADED BY OCTAVE OF (6)', 'REGISTERED -- THE LINES OF (4) TO (7) IN OPEN_TRAILS',
               'HELD -- THE PROOF BY THE BANKED WINDOW, CARRIED BY [P2]',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b767 ((R377)(4), (9), N1; b759's form): every runner dispatch of the act sent by tools/b767_controls.py's dispatch route,
    each command of that route in the capture a dispatch row's or a refused send's -- refused at the network and rowed dispatch_refused
    with its number, or refused by the tool before any send and pinned by its time and number -- (one to MAX_DISPATCHES, forty, at most
    thirty-six with the restore on, and with the restore off the trial, the closing build and one repeat of each, each in
    SIDE-explicit-formula, none in SIDE-dirichlet-mod-24; no cap by price row), each read once after it by its run id, every dispatch and
    read row's free memory at or above the hold; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### b766: the act's own rows, each dispatch and its read; the order read by the loop above, by run id
    order = order and len(seq_) == 2 * len([r for r in rows if r.get('kind') == 'dispatch'])
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b767_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
    # ### b767, Component 4 (the Edit tool, found by scratch cmd767.py at 20:56:57Z, before any run of the checks): the capture holds 25
    # ### commands of the dispatch route against 17 dispatch rows -- five sends refused at the network, each rowed dispatch_refused with its
    # ### number (2, 7, 11, and 15 twice), and three refused by the tool before any send with no row (dispatch 6: at 14:31:36Z the checks'
    # ### false refusal of names in block comments, defect (l); at 14:39:58Z and 14:43:17Z "not the remote tip", data/b767_events.txt (78));
    # ### b766's predicate, one command for each dispatch row, read none of them. Each command read by its number: a dispatch's by its row,
    # ### a rowed refusal by its row, the tool's three by the pins here (the command's time and number)
    TOOL_REFUSED_ = (('2026-11-23T14:31:36', 6), ('2026-11-23T14:39:58', 6), ('2026-11-23T14:43:17', 6))
    dnum_ = lambda c_: (re.search(r'b767_controls\.py"? dispatch \S+ (\d+)\b', c_['cmd']) or [None, None])[1]
    refused_ = [r for r in rows if r.get('kind') == 'dispatch_refused']
    sends_ok_ = len(cmds) == len([r for r in rows if r.get('kind') == 'dispatch']) + len(refused_) + len(TOOL_REFUSED_) \
        and all(any(str(c_.get('ts') or '').startswith(t_) and dnum_(c_) == str(n_) for c_ in cmds) for t_, n_ in TOOL_REFUSED_) \
        and sorted(int(dnum_(c_) or 0) for c_ in cmds) == sorted([int(r.get('n') or 0) for r in rows if r.get('kind') in ('dispatch', 'dispatch_refused')]
                                                              + [n_ for _t, n_ in TOOL_REFUSED_])
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) + len(K.M24_RUNS) and sends_ok_ \
        and len(K.EF_RUNS) <= K.MAX_DISPATCHES == 40 and len(K.M24_RUNS) == K.MAX_DISPATCHES_M24 == 0 \
        and len([r for r in rows if r.get('kind') == 'dispatch' and r.get('restore') == 'on']) <= dict(K.MAX_DISPATCHES_KINDS)['restore'] == 36 \
        and (lambda ro_: set(ro_) <= {'trial-off', 'closing', 'repeat'} and ro_.count('trial-off') <= dict(K.MAX_DISPATCHES_KINDS)['trial'] == 1
             and ro_.count('closing') <= dict(K.MAX_DISPATCHES_KINDS)['closing'] == 1 and ro_.count('repeat') <= dict(K.MAX_DISPATCHES_KINDS)['repeat'] == 2)(
            [r.get('item') for r in rows if r.get('kind') == 'dispatch' and r.get('restore') != 'on']) \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b767, N1 (Component 4, the Edit tool, where b766's cap of 20 and 18 and its restore-off items stood): the runs those of (4) and (5), forty at most, thirty-six at most with the restore on, the restore off for the trial, the closing build and one repeat of each, none in SIDE-dirichlet-mod-24
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N3, N5, (R377)(1), (4)-(7), (10), (12): PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the corrigendum and
    the entry; OPEN_TRAILS: the texts of (4) to (7) in the rulings tool's groups, each under its dated head, and the trail), the ledgers
    changed; REGISTRY, ERRATA, the census, the register and the two files of the map not written; no rename; no other paper written this
    act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b767, Component 4 (the Edit tool): b767's headings and banks, as its _finding_text_b767 (record 34) writes them (each heading read
# ### there by the search tool, 19:5xZ); the last the INTEGRATION line as (R377)(10) gives it, bare, read from the ferry's :47 alone
# ### (_integ_line, written by no reader of the act's banks)
ENTRY_NEEDLES = ('**b766 at its weight and the corrigendum**', '**The price and the ceiling**', '**One key**',
                 '**The plan amended and the certificate’s three forms, before any dispatch**', '**The build from source given its order**',
                 '**The steps in Lean**', '**The closing build from source, main and the tag**', '**The window at knots graded by octave**',
                 '**The rulings entered**', '**The ledgers**',
                 '**The research instruments reproduced**', '**The order of the act**', '**What this act is not**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**',
                 '**The report of (10)**', '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b767_misses.txt', 'data/b767_price.txt', 'data/b767_ceiling.txt', 'data/b767_corrigendum.txt', 'data/b767_repairs.txt',
                 'data/b767_repair_controls.txt', 'data/b767_certificate.json', 'data/b767_certificate.txt', 'data/b767_plan.txt',
                 'data/b767_source_build.txt', 'data/b767_registration.txt', 'data/b767_window.txt', 'data/b767_window.json',
                 'data/b767_controls_control.txt', 'data/b767_dispatch_rows.json', 'data/b767_controls.txt', 'data/b767_logdata.txt', 'data/b767_natdata.txt',
                 'data/b767_ledgers_c2.txt', 'data/b767_ledgers_c5.txt', 'data/b767_orders.txt', 'data/b767_reproduce.txt', 'data/b767_events.txt',
                 'data/b767_address_scan.txt', 'data/b767_touch.txt',
                 'W-ORD-LI-ARITH', 'W-ORD-WINDOW-CERTIFY', 'W-ORD-SOURCE-BUILD', 'W-ORD-NOVEMBER-RIDERS',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: cluster The Epstein instance ; keystone phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md ; stage CLUSTERED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R377)(1), (4)-(7), (12), N3, N4, N5 (the name the frozen run list carries): PLACE-papers written by the worklist's PP_CHAIN in
    its order and by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone, the act's first on its base
    (no weight line, (1) ordering none), removing no line; each of the rulings tool's groups (c2: [S1] with W-ORD-SOURCE-BUILD's entry
    line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS' entry line, [A2]; c5: [P2], [S2]; c6 where [C7] or [C8] is entered) in one commit
    touching OPEN_TRAILS alone, removing no line, the file's bytes before a prefix of its new bytes, its blob at that commit the sha256
    that group's json wrote, each group's sha before the previous group's sha after; REGISTRY and ERRATA in no commit ((R377)(12), N3);
    the changed files since the base within PP_WRITTEN; by ancestry the base, each commit of the chain and HEAD; the earlier acts'
    registrations at HEAD their blobs."""
    pf_, ns_, sh_ = S['pp_files'] or {}, S['numstat'] or {}, S['pp_shas'] or {}
    pc_ = dict(K.PP_CHAIN)
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    def fj_(g_):
        j_ = lj_.get(g_) if isinstance(lj_.get(g_), dict) else {}
        return j_.get('file') if isinstance(j_.get('file'), dict) else {}
    def sha_(c_, f_, w_):
        return bool(w_) and sh_.get('%s:%s' % (c_[:8], f_)) == w_
    want_ = [('c1pp', ['FINDINGS.md'], True)]
    prev_ = None
    for g_ in LEDGER_GROUPS:   # ### b767: each group's OPEN_TRAILS commit, its file fields under `file` (tools/b767_rulings.py)
        f_ = fj_(g_)
        want_.append((g_ + 'pp', ['OPEN_TRAILS.md'], f_.get('path') == 'OPEN_TRAILS.md' and f_.get('prefix') is True
                      and sha_(pc_.get(g_ + 'pp') or '-', 'OPEN_TRAILS.md', f_.get('sha_after')) and (prev_ is None or f_.get('sha_before') == prev_)))
        prev_ = f_.get('sha_after')
    rows_ = [(k_, sorted(pf_.get(k_) or []) == sorted(fs_) and bool(ns_.get(k_))
              and all(x_ == '0' for x_ in (ns_.get(k_) or [])[1::3]) and ok_) for k_, fs_, ok_ in want_]
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:len(K.PP_CHAIN)]] == [h_[:8] for _k, h_ in K.PP_CHAIN]
    return len(rows_) == len(K.PP_CHAIN) == 1 + len(LEDGER_GROUPS) and set(k_ for k_, _o in rows_) == set(pc_) and all(o_ for _k, o_ in rows_) and order_ \
        and 'REGISTRY.md' not in S['pp_head_files'] and not any('REGISTRY.md' in (fs_ or []) for fs_ in pf_.values()) \
        and 'ERRATA.md' not in S['pp_head_files'] and not any('ERRATA.md' in (fs_ or []) for fs_ in pf_.values()) \
        and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b767_address_scan.py run live over every commit of the act (relay,
    PLACE-papers and SIDE-explicit-formula's commits from its base, the kernel's commits and tag messages among them; fields, messages and
    added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the
    address 0, the author's name 0, the previous name 0, the ORCID 0; no byline excepted, (R377)'s N5 writing none (the tool given it at
    step zero, events (7)), the bank's exception line NONE TAKEN; its eight controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 8 OF 8 AS WANTED' in out \
        and '## THE EXCEPTION, THE BYLINE UNDER I-23: NONE TAKEN: R377`S N5' in out and '## THE EXCEPTION, THE BYLINE UNDER I-23: NONE TAKEN: R377`S N5' in (S['address'] or '') \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R377)(1)-(12), N2, N4 (the name the frozen run list carries): the act's order by time -- the worklist's TIME_ORDER, relay and
    PLACE-papers together (the act_current commit, step zero's banks, the c1 route, PLACE-papers' corrigendum and the corrigendum banks,
    the one standing commit of (8) before its row, the certificate and the plan before the dispatch tool and the opening dispatch, the
    registration before the window's tool, each act tool before its bank, each group of the rulings tool's OPEN_TRAILS commit and its
    relay banks after it), then the handoff page and the lock gate where made, each placed by its time ([K21]); by ancestry within the
    relay through each commit of _chain; the act's commits under tools/standing/ the one of K.STANDING_REPAIRS and no other ((R377)(11):
    (8) alone moves tools/standing/), moving tools/standing/VERSION to its version, its row's commit carrying the controls bank, and the
    control's verdict line, "[K] THE CONTROL AS WANTED: THE FAULT READ BEFORE AND CLEAN AFTER: True.", at its line in the controls bank at
    HEAD and in that bank's blob at the row's commit."""
    t_ = S['t']
    ks_ = STANDING_ACT.keys_in_time(K.TIME_ORDER, [k_ for k_, _h in S['r366_chain'] if k_ in ('passed', 'handoff', 'lockgate')], t_)   # ### b765, [K21] (v1.38.20): the tail keys by their times
    sr_ = []
    for k_, v_, c_, r_, l_ in K.STANDING_REPAIRS:
        d_ = (S['strepairs'] or {}).get(k_) or {}
        w_ = '### ### **%s THE CONTROL AS WANTED: THE FAULT READ BEFORE AND CLEAN AFTER: True.**' % k_
        sr_.append('tools/standing/VERSION' in (d_.get('vfiles') or []) and d_.get('ver') == v_ and K.REPAIR_CONTROLS_BANK in (d_.get('rfiles') or [])
                   and (d_.get('line') or '').rstrip() == w_ == (d_.get('line_at') or '').rstrip())
    st_ = [h_[:8] for h_ in S['st_commits'] or []] == [c_[:8] for _k, _v, c_, _r, _l in K.STANDING_REPAIRS]
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and len(S['anc']) == len(S['r366_chain']) - 1 and all(v is True for v in S['anc'].values()) \
        and len(sr_) == len(K.STANDING_REPAIRS) == 1 and all(sr_) and st_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R377)(3)-(8), (12), N2, N3 (the name the frozen run list carries): each tool of K.GENS first added by a commit of its own, every
    one of its commits carrying it and not its bank, the bank's commit carrying the bank and not the tool and after every tool commit, the
    bank at HEAD its blob there (the repairs' planted controls, the certificate, the source-build read, the window at graded knots, the
    groups c2 and c5, the prime table of L10, the factor runs of L11b and the dispatch tool's bank: nine); the one row of
    K.GENS_WITH_BANK, the dispatch tool's controls riding once with its tool's repair, its tool first added before it; the ceiling read
    before the lock banked at C1_CEILING, its blob there, its foot in the record's form; the plan at its commit before the first dispatch,
    its blob there; the feet as the entry reads them -- the dispatch tool's controls 29 of 29, the price table, the corrigendum, the
    certificate's three forms and the source-build read, each its fixed words; the two data files' controls lines whole; the window's
    reading the key its group entered and its control as wanted; the dispatch tool's foot within (R377)(4)'s caps, its main by the
    worklist's main and tag, its controls whole; each group's foot one file appended with its keys, its entry lines and controls whole, and
    group c2's roster after figure the orders bank's OPEN; the reproduction run's foot, its rows summing and its planted controls whole.
    (b767, Component 4, the Edit tool: the feet read by feet767.py, read-only, 19:51:17Z.)"""
    gk_ = _gens_ok(S)
    wk_ = _gwb_ok(S)
    feet_ = [('b767_controls_control.txt', 'THE TOOL`S CONTROLS: 29 OF 29 AS WANTED ; ALL AS WANTED.'),
             ('b767_price.txt', 'THE PRICE TABLE: STEP ZERO 0.91 h ; THE LOWER SUM 25.78 h AGAINST THE CEILING 30 h ; THE UPPER SUM 63.58 h ; '
                                'DISPATCHES 9-25 OF AT MOST 40, WITH THE RESTORE ON 8-21 OF AT MOST 36 ; THE LEAN 1610-5730 LINES ; THE LAST STEP DISPATCH BY 22:34:03Z.'),
             ('b767_corrigendum.txt', 'ITEMS 169: EVENTS 131, POST-SEAL 16, DEFECTS 22 ; CLAIM 8, CLOSE 161 ; REPEAT 126 ; THE CLAIM ITEMS OF b766`S BANKS 8, PRINTED IN FULL ; '
                                      'THE FINDINGS AFTER THE LOCK 11: CLAIM 0, CLOSE 11, REPEAT 8 ; THE NAVIGATOR`S CLAIMS 9, CLAIM 9 ; THE NAVIGATOR`S FIGURES PRINTED AS THE NAVIGATOR`S ; '
                                      'NO WEIGHT LINE ; THE ENTRY AT FINDINGS :16080.'),
             ('b767_certificate.txt', 'THE THREE FORMS READ: 10 OF 10 CONTROLS AS WANTED ; THE PRIMES` ONE WIDTH 21 DIGITS, THE INTEGERS` 22, BY PARTS AT ITS LEAST 22 (ORDER 1).'),
             ('b767_source_build.txt', 'THE READ MADE: 16 OF 16 CONTROLS AS WANTED ; THE ROUTE STATED.')]
    ft_ = [_vlast(_txt(rd(n_))) == w_ for n_, w_ in feet_]
    dt_ = [bool(m_) and m_.group(1) == m_.group(2) for m_ in (re.search(p_, _txt((S['datat'] or {}).get(n_))) for n_, p_ in DATA_BANKS)]
    wm_ = re.search(r'(?m)^  H-GRADED-WINDOW: (HELD|REFUTED|NOT SCORED), \[(G[123])\] ;', _txt(S['wint']))
    wn_ = bool(wm_) and wm_.group(2) == dict(HELD='G1', REFUTED='G2').get(wm_.group(1), 'G3') \
        and wm_.group(2) in (((S['ledgersj'] or {}).get('c2') or {}).get('entered') or {}) and re.search(r'(?m)^  THE CONTROL AS WANTED \(unit at ', _txt(S['wint'])) is not None
    cer_ = re.match(r'^THE CEILING READ BEFORE THE LOCK \(\(R377\)\(3\), read-only, \d\d:\d\d:\d\dZ\): SPENT [\d.]+ h FROM THE OPENING ROW ; THE LAST STEP DISPATCH AT '
                    r'\d\d:\d\d:\d\dZ, [\d.]+ h FROM THE OPENING ROW ; LEFT -?[\d.]+ h OF 30 h, THE RESERVE 16 h ; THE CLOSE AT b766`S [\d.]+ h FROM ITS LOCK, [\d.]+ h FROM '
                    r'THE OPENING ROW ; (WITHIN THE CEILING|THE ACT WOULD PASS 30 h AT ITS CLOSE)\.$', _vlast(_txt(S['ceilt'])))
    ce_ = bool(K.C1_CEILING) and bool(_txt(S['ceilt'])) and _txt(S['ceilt']) == _txt(blob(ROOT, '%s:data/b767_ceiling.txt' % K.C1_CEILING)) \
        and gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b767_ceiling.txt').strip()[:8] == K.C1_CEILING[:8] and bool(cer_)
    pl_ = bool(_txt(S['plant'])) and _txt(S['plant']) == _txt(blob(ROOT, '%s:data/b767_plan.txt' % PLAN_COMMIT)) \
        and gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b767_plan.txt').strip()[:8] == PLAN_COMMIT
    tv_ = re.match(r'^DISPATCHES (\d+) OF AT MOST (\d+) \(WITH THE RESTORE ON (\d+) OF AT MOST (\d+)\) ; THE TRIAL (\S+) ; THE PAIR (.+?) ; MAIN AND THE TAG: (.+) ; '
                   r'THE TOOL`S CONTROLS (\d+) OF (\d+)\.$', _vlast(_txt(S['trialt'])))
    moved_ = K.EF_MAIN == K.RUNNER_COMMIT
    tr_ = bool(tv_) and int(tv_.group(1)) <= int(tv_.group(2)) == K.MAX_DISPATCHES and int(tv_.group(3)) <= int(tv_.group(4)) == dict(K.MAX_DISPATCHES_KINDS)['restore'] \
        and int(tv_.group(1)) == len(K.EF_RUNS) and tv_.group(8) == tv_.group(9) and tv_.group(5) == '[S2]' and tv_.group(7) != 'PENDING' \
        and tv_.group(7).startswith('MAIN MOVES TO %s' % K.RUNNER_COMMIT[:8]) == moved_ and (K.WEIL_TAG is not None) == moved_ \
        and (moved_ or K.EF_MAIN == K.EF_BASE)
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    lt_ = S['ledgerst'] if isinstance(S['ledgerst'], dict) else {}
    led_ = []
    for g_ in LEDGER_GROUPS:
        j_ = lj_.get(g_) if isinstance(lj_.get(g_), dict) else {}
        en_ = sorted(j_.get('entered') or {})
        lv_ = re.match(r'^THE LEDGERS, GROUP (C\d): OPEN_TRAILS APPENDED, NO LINE MOVING ; (\d+) LINES? UNDER ONE HEAD \((.+?)\) ;'
                       r'(?: THE E0 GATE \d+ OF \d+ (?:DERIVES|READ) ;)? CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.$', _vlast(_txt(lt_.get(g_))))
        led_.append(bool(lv_) and lv_.group(1) == g_.upper() and lv_.group(4) == lv_.group(5) == str(len(j_.get('controls') or []))
                    and bool(j_.get('controls')) and all(o_ for _w, o_ in j_['controls']) and isinstance(j_.get('file'), dict)
                    and en_ == LEDGER_KEYS.get(g_) and len(j_.get('entry_lines') or {}) == LEDGER_ENTRY_LINES.get(g_, 0)
                    and int(lv_.group(2)) == len(en_) + len(j_.get('entry_lines') or {}))   # ### [S1] and [R1] each carry their order's entry line beside them
    lr_ = (lj_.get('c2') or {}).get('roster') or {}
    om_ = re.match(r'^ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', _vlast(_txt(S['orderst'])))
    ro_ = bool(om_) and int(om_.group(2)) == lr_.get('after_open') and int(om_.group(1)) == int(om_.group(2)) + int(om_.group(3)) \
        and not any((lj_.get(g_) or {}).get('roster') for g_ in LEDGER_GROUPS[1:])   # ### b767: groups after c2 move no order
    rp_ = re.match(r'^ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS 0 ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ; \d+ s\.$', _vlast(_txt(S['reproduce'])))
    rep_ = bool(rp_) and int(rp_.group(1)) == int(rp_.group(2)) + int(rp_.group(3)) and rp_.group(4) == rp_.group(5)
    return len(gk_) == len(K.GENS) == 9 and all(o_ for _n, o_ in gk_) and len(wk_) == len(K.GENS_WITH_BANK) == 1 and all(o_ for _n, o_ in wk_) \
        and ce_ and pl_ and all(ft_) and len(dt_) == 2 and all(dt_) and wn_ and tr_ and len(led_) == len(LEDGER_GROUPS) and all(led_) and ro_ and rep_


PLAN_COMMIT = 'b7d31fb8'   # ### b767: data/b767_plan.txt by the Write tool and two Edits (10:05:59Z-10:06Z), committed with the certificate's banks at step 16, before any dispatch (feet767.py, 19:51:17Z: its last commit b7d31fb8)


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N1, N5, (R377)(4), (9), (12) (the name the frozen run list carries): the two kernels as the act left them, read locally with no
    remote read -- SIDE-explicit-formula's main locally and at its tracking ref at the worklist's EF_MAIN: the closing Lean commit
    89fd5b54 with v0.45 on it where the closing build from source exited 0 with the restored build's axioms file, else the act's entering
    main 0ba9cd61 (v0.44's peel), unmoved and no tag cut ([C7] or [C8]); the tags past v0.38 v0.39 to v0.44, each object and peel the
    worklist's (v0.39 to d1afb4fc, v0.40 to 630cba16, v0.41's object 390506fc to a3aad4cc, v0.42's 001e94ff to 4964e957, v0.43's
    bcd4d481 to 819e4a83, v0.44's bd024837 to 0ba9cd61), and v0.45 where cut, v0.38's object 21c6edaf and peel 14ca5725; its four held
    branches at their entering tips locally and at origin, zq-b730 at 1e658870; push-b767-proof at the closing Lean commit 89fd5b54,
    push-b766-proof at 3c67b8b5, push-b765-centre at 0ba9cd61, push-b764-runner and b763's four push-b763-* branches at their tips, each
    locally and at origin; no kernel branch removed (the worklist's KERNEL_DELETES, KERNEL_REMOVED and KERNEL_DELETES_REFUSED none);
    push-b759-weil absent from its tracking refs as b760 left it, its local branch kept at a3aad4cc; the act's fifteen kernel commits each
    on push-b767-proof at origin, on the remote main where main moved and not otherwise; SIDE-dirichlet-mod-24's main at e5ebdd15 at its
    tracking ref and locally, v0.2.0's object e5c84316 peeling to e5ebdd15, v0.1.0 at 597b0869 and no other tag, push-b757-mod24 absent
    from its tracking refs; no sitting kernel. (b767, Component 4, the Edit tool.)"""
    ks_ = S['kst'] or {}
    ef_, m4_, ct_ = ks_.get('ef') or {}, ks_.get('m24') or {}, ks_.get('contains') or {}
    def h_(d_, r_):
        return (d_.get(r_) or ('', ''))[0]
    def p_(d_, r_):
        return (d_.get(r_) or ('', ''))[1]
    mn_ = h_(ef_, 'refs/heads/main')
    moved_ = K.EF_MAIN == K.RUNNER_COMMIT
    tags_ = [K.WEIL_TAG_B759, K.WEIL_TAG_B763] + list(K.ORDER_TAGS_B763) + [K.WEIL_TAG_B765] + ([K.WEIL_TAG] if K.WEIL_TAG else [])
    tg_ = sorted(r for r in ef_ if re.match(r'^refs/tags/v0\.(39|[4-9]\d)', r))
    ef_ok = mn_ == h_(ef_, 'refs/remotes/origin/main') == K.EF_MAIN \
        and (moved_ or K.EF_MAIN == K.EF_BASE == K.WEIL_TAG_B765[2]) and bool(K.WEIL_TAG) == moved_ \
        and (not K.WEIL_TAG or (K.WEIL_TAG[0] == 'v0.45' and K.WEIL_TAG[2] == K.RUNNER_COMMIT)) and K.ORDER_TAGS == () \
        and all(h_(ef_, 'refs/heads/' + b) == t == h_(ef_, 'refs/remotes/origin/' + b) for b, t in K.EF_BRANCHES) and K.ZQ_TIP == K.ZQ_ENTERING \
        and h_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[1] and p_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[2] \
        and tg_ == sorted(['refs/tags/v0.39', 'refs/tags/v0.40'] + ['refs/tags/' + t_[0] for t_ in tags_]) \
        and p_(ef_, 'refs/tags/v0.39') == K.LAND_BRANCH[1] and p_(ef_, 'refs/tags/v0.40') == K.COEFF_LAND_BRANCH[1] \
        and all(h_(ef_, 'refs/tags/' + n_) == o_ and p_(ef_, 'refs/tags/' + n_) == pl_ for n_, o_, pl_ in tags_) \
        and K.WEIL_BRANCH[0] == 'push-b767-proof' and K.WEIL_BRANCH[1] == K.RUNNER_COMMIT \
        and all(h_(ef_, 'refs/heads/' + b_) == t_ == h_(ef_, 'refs/remotes/origin/' + b_)
                for b_, t_ in (K.WEIL_BRANCH, K.WEIL_BRANCH_B766, K.WEIL_BRANCH_B765, K.WEIL_BRANCH_B764, K.WEIL_BRANCH_B763, K.ARITH_BRANCH_B763)
                + tuple(K.ORDER_BRANCHES_B763)) \
        and K.WEIL_BRANCH_B766[1] == K.WEIL_BRANCH_BASE \
        and K.KERNEL_DELETES == () and K.KERNEL_REMOVED == () and K.KERNEL_DELETES_REFUSED == () \
        and 'refs/remotes/origin/' + K.WEIL_BRANCH_B759[0] not in ef_ \
        and h_(ef_, 'refs/heads/' + K.WEIL_BRANCH_B759[0]) == K.WEIL_BRANCH_B759[1]
    kc_ = len(K.KERNEL_COMMITS) == 15 and all(b == K.WEIL_BRANCH[0] for _k, _kn, _c, b in K.KERNEL_COMMITS) \
        and all(('refs/remotes/origin/' + b) in ct_.get(k, []) for k, _kn, _c, b in K.KERNEL_COMMITS) \
        and all(('refs/remotes/origin/main' in ct_.get(k, [])) == moved_ for k, _kn, _c, b in K.KERNEL_COMMITS)
    m4_ok = h_(m4_, 'refs/remotes/origin/main').startswith(K.M24_MAIN) and h_(m4_, 'refs/heads/main')[:8] == K.M24_MAIN[:8] \
        and h_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[1]) and p_(m4_, 'refs/tags/' + K.M24_TAG[0]).startswith(K.M24_TAG[2]) \
        and p_(m4_, 'refs/tags/v0.1.0').startswith(K.M24_BASE) and sorted(r for r in m4_ if r.startswith('refs/tags/')) == ['refs/tags/v0.1.0', 'refs/tags/v0.2.0'] \
        and 'refs/remotes/origin/push-b757-mod24' not in m4_
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
    arm list since b766's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R377)(4)-(7), (12), N1, N3 (the name the frozen run list carries): the counts the entry and the root prompt carry, each read from
    its bank -- the rulings tool's groups, each OPEN_TRAILS alone appended, its bytes before a prefix, under its own dated head: c2 [S1]
    with W-ORD-SOURCE-BUILD's entry line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS' entry line, [A2]; c5 [P2] and [S2]; c6 [C7] or [C8]
    where entered; no [P1], [S3], [G2] or [G3]; each group's controls whole; group c2's roster adding the two orders of (5) and (7)(c)
    and moving none, the groups after it moving none; the orders bank's foot at c2's after figure; the dispatch rows' runs EF_RUNS in
    order within MAX_DISPATCHES, the run group c5 cites for [P2] and the two its [S2] cites among them; b746's draft unchanged; no Zenodo
    tool. (b767, Component 4, the Edit tool: the groups' jsons read by led767.py, read-only, 19:52:47Z.)"""
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    gj_ = dict((g_, lj_.get(g_) if isinstance(lj_.get(g_), dict) else {}) for g_ in LEDGER_GROUPS)
    ro_ = gj_['c2'].get('roster') or {}
    led_ = all((j_.get('file') or {}).get('path') == 'OPEN_TRAILS.md' and (j_.get('file') or {}).get('prefix') is True
               and sorted(j_.get('entered') or {}) == LEDGER_KEYS.get(g_) and bool(j_.get('controls')) and all(o_ for _w, o_ in j_['controls'])
               for g_, j_ in gj_.items()) \
        and not set(['P1', 'S3', 'G2', 'G3']) & set(k_ for j_ in gj_.values() for k_ in (j_.get('entered') or {})) \
        and sorted(ro_.get('added') or []) == ['W-ORD-NOVEMBER-RIDERS', 'W-ORD-SOURCE-BUILD'] and list(ro_.get('moved') or []) == [] \
        and not any(j_.get('roster') for g_, j_ in gj_.items() if g_ != 'c2')
    om_ = re.match(r'^ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', _vlast(_txt(S['orderst'])))
    ord_ = bool(om_) and int(om_.group(2)) == ro_.get('after_open')
    s2_ = gj_['c5'].get('s2') if isinstance(gj_['c5'].get('s2'), dict) else {}
    xr_ = ([int(gj_['c5']['run'])] if gj_['c5'].get('run') else []) + [int(s2_[k_]) for k_ in ('on_run', 'off_run') if str(s2_.get(k_) or '').isdigit()]   # ### s2's keys by s2k767.py, 19:57:10Z
    disp_ = [int(r_.get('run')) for r_ in S['drows'] or [] if r_.get('kind') == 'dispatch'] == list(K.EF_RUNS) and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES \
        and len(xr_) == 3 and set(xr_) <= set(K.EF_RUNS)
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b767_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return led_ and ord_ and disp_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b767_steps.json', 'data/b767_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order, the tool's own list at the act's base 38024feb (I-109, entered at
    b753, and I-110 and I-111, entered at b756 on the author's pass, stand in no row of it, and this act changes no research tool). Run at
    b762 as (R372)(12) orders it, in the foreground (data/b762_reproduce.txt, 352 s, events (39)). Each row REPRODUCES,
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
    """standing clauses v9 (the ferry's Component 5 under (R377), data/b767_ferry.txt :120: the close "as the standing clauses and [K24] order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b767_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b766's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R377-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b766's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R377) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b766's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base; run at b767 as (R377)(11) orders it, in the foreground',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 98 = 98 OK + 0 misses; the ferry`s paths 53, OK 46, NONE 0, the seven OWN rows apart; the check CLEAN (halts 0), banked at 08:55:22Z, as the step-zero bank enters it after the read-first bank and before the removals; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b766-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b767: the tip cut from "(was a0bc04cd1)" and the four after it (data/b767_stepzero.txt :59-:60), each tip then unreadable; b766's form, the carried plant having wanted the tip closed by its paren
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s ACT line adjusted to what the act did: the proof by the banked window continued under (R377); b766 at its weight; one key with its planted control; the plan amended and the certificate`s three forms; the archimedean term, the enclosures and the pole term`s data half compiled and the proof by its outcome; the build from source read, its route and its trial by its outcome; the closing build from source, main and the tag by its outcome; the window at knots graded by octave by its outcome; the author`s rulings entered; the roster at the close; the dispatches; each object`s bank in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R377)(1): the generated corrigendum for b766`s record, short, landed at FINDINGS :16080: b766`s 131 events, 16 post-seal rows and 22 defects by count from their banks, 169 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 8 CLOSE 161, REPEAT 126, the eight CLAIM items (b766`s events (24)-(31)) printed in full; the eleven findings after b766`s lock entered as b767`s events (20)-(30), CLAIM 0 CLOSE 11 REPEAT 8, each with its time; the navigator`s nine claims as events (31)-(39), CLAIM 9, the navigator`s figures printed as the navigator`s; no weight line; the corrigenda bank appended at row (87)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R366)(2), data/b756_rules.txt`s rows (a) to (c), in force from b757, in b756`s commit 0a151012 and no other, the working tree its blob at HEAD; no data/b767_rules.txt, (R377) ordering no rules row; data/b760_rules.txt and data/b754_rules.txt not rewritten',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b767's objects
    ('G-REGISTRATIONS-FIRST', '(R377)(1), (4)-(7), (12), N3, N4, N5: PLACE-papers written by the worklist`s chain in its order and by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone (216d9715), no weight line; each of the rulings tool`s groups in one commit appending to OPEN_TRAILS alone (c2 ba23945a, c5 adadfd62, and c6 where [C7] or [C8] is entered), its bytes before a prefix, removing no line, its blob at that commit the sha its group`s json wrote, each group following the last; REGISTRY and ERRATA in no commit; the changed files within the act`s list; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('phase1.5/method/INSTRUMENTS.md'))),   # ### b767: a file outside the list (SPIRAL_MAP.md, the carried plant, is in b767's)
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b767_address_scan.py run live over every commit of the act in the relay, PLACE-papers and SIDE-explicit-formula, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, no byline excepted, (R377)`s N5 writing none (the exception read from this act`s ferry at step zero, [K2]), eight controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R377)(1)-(13), N2, N4: the act`s order by time across the relay and PLACE-papers -- the act_current commit and step zero`s banks, the c1 route and the corrigendum, the one standing commit of (8) before its row, the certificate and the plan before the dispatch tool and the opening dispatch, the registration before the window`s tool, each act tool before its bank, each group of the rulings tool`s OPEN_TRAILS commit before its relay banks, then the handoff page and the lock gate, each placed by its time ([K21]) -- and by ancestry within the relay; the act`s commits under tools/standing/ the one of the worklist`s STANDING_REPAIRS and no other, moving VERSION to v1.38.25, its planted control`s verdict line AS WANTED at its line ((R377)(11))',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update({next(iter(d), 'none'): False}))),   # ### b767: the first pair of the chain's ancestry set False (b766's planted key stood in no state of b767's)
    ('G-DERIVATION-GRADED', '(R377)(3)-(8), (12), N2, N3: each of the act`s nine generator rows (the repairs` planted control, the certificate, the source-build read, the window at graded knots, the rulings tool`s groups c2 and c5, the prime table of L10, the factor runs of L11b and the dispatch tool`s bank) first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; the dispatch tool`s controls riding once with its tool`s repair, its tool added before; the ceiling bank before the lock and the plan at their commits; the feet of the controls, the price, the corrigendum, the certificate`s three forms, the source-build read, the two data files, the window`s reading, the dispatch tool, the groups, the roster and the reproduction run',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'trialt', (S['trialt'] or '').replace('THE TOOL`S CONTROLS', 'THE TOOLS CONTROLS'))),   # ### b767: the dispatch tool's foot made unreadable
    ('G-OFFSET-POST-HOC', 'N1, N5, (R377)(4), (9), (12): the two kernels as the act left them -- SIDE-explicit-formula`s main locally and at origin at the worklist`s EF_MAIN, the closing Lean commit 89fd5b54 with v0.45 on it where the closing build from source exited 0 with the restored build`s axioms file, else 0ba9cd61 unmoved with no tag cut ([C7] or [C8]); v0.39 to v0.44 each at its object and peel, v0.38 peeling to 14ca5725; its four held branches at their tips; push-b767-proof at 89fd5b54, push-b766-proof at 3c67b8b5, push-b765-centre, push-b764-runner and b763`s four push-b763-* branches at their tips locally and at origin; no kernel branch removed; push-b759-weil absent at origin, its local branch kept; the act`s fifteen kernel commits on push-b767-proof at origin, on the remote main where main moved and not otherwise; SIDE-dirichlet-mod-24`s main at e5ebdd15 at origin, push-b757-mod24 absent there, v0.2.0 peeling to main, v0.1.0 at 597b0869 and no other tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'kst', lambda d: d['ef'].update({'refs/tags/v0.40': ('0' * 40, K.WEIL_TAG_B759[2])}))),   # ### b767: v0.40's peel planted at b759's main a3aad4cc, a tag moved
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R377)(4)-(7), (12), N1, N3: the counts read from their banks -- the rulings tool`s groups, each OPEN_TRAILS alone appended, a prefix: c2 [S1] with W-ORD-SOURCE-BUILD`s entry line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS` entry line, [A2]; c5 [P2], [S2]; c6 [C7] or [C8] where entered; no [P1], [S3], [G2] or [G3]; each group`s controls whole; the two orders of (5) and (7)(c) added and none moved, at c2 alone; the roster`s foot; the dispatch rows` runs EF_RUNS in order, the run [P2] cites and the two [S2] cites among them; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'ledgersj', lambda d: (d.get('c2') or {}).get('roster', {}).update(added=['W-ORD-NOVEMBER-RIDERS', 'W-ORD-PLANTED', 'W-ORD-SOURCE-BUILD']))),   # ### b767: an order planted as added beside the two added
    ('G-DIFFERS-ERRATA', '(R377)(1), (12): no ERRATA entry and no DIFFERS entry -- ERRATA.md at HEAD its bytes at the act`s base, in no commit of the act; the worklist`s ERRATA_LINE none; no differs bank; the corrigendum in 216d9715, FINDINGS the one file there, its head at FINDINGS :16080; no weight line, (R377)(1) ordering none',
#⟪END⟫
# ### b767, Component 4 (the Edit tool): G-DIFFERS-ERRATA for (R377), which writes no ERRATA entry ((12): REGISTRY, ERRATA and the
# ### register not written) and orders no weight line -- the template's predicate (checks.tpl :1562-:1567) wants a weight line in
# ### FINDINGS; replaced whole here, b766's form, its groups LEDGER_GROUPS
#⟪OVERRIDE checks MARK dd4dd9cb3d4b 6⟫
    """(R377)(1), (12): no ERRATA entry this act and no DIFFERS entry -- ERRATA.md's bytes at HEAD its bytes at the act's base, in no
    commit of the act; the worklist's ERRATA_LINE none, every group of the rulings tool writing OPEN_TRAILS alone; no differs bank and no
    errata bank; the corrigendum at FINDINGS in Component 1's PLACE-papers commit, FINDINGS the one file there, its head at the
    worklist's CORR_LINE; no weight line, (R377)(1) ordering none."""
    pre_, now_ = S['errata_pp_pre'] or b'', S['errata_pp_now'] or b''
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    ec_ = sorted(k_ for k_, fs_ in (S['pp_files'] or {}).items() if 'ERRATA.md' in (fs_ or []))
    return bool(pre_) and now_ == pre_ and ec_ == [] and K.ERRATA_LINE is None \
        and all(((lj_.get(g_) or {}).get('file') or {}).get('path') == 'OPEN_TRAILS.md' for g_ in LEDGER_GROUPS) \
        and not S['differs'] and not S['errata'] and K.DIFFERS_LINE is None and K.WEIGHT_LINE is None and S['files']['c1pp'] == ['FINDINGS.md'] \
        and fline(S, K.CORR_LINE).startswith('## Corrigendum to b766')
#⟪END⟫
# ### b760, Component 5 (the Edit tool), defect (f): v1.36.2 taught the kernels face's writer to name SIDE-dirichlet-mod-24 (record.tpl :634)
# ### and not the suite's reader of the face (checks.tpl :611, its list without it), so G-KERNELS-UNTOUCHED's first clause (the face's
# ### kernels equal the kernels read) failed at the standing-a2 probe (05:51:52Z), 24 against 23; the reader takes the writer's own list, in
# ### the act's module for this act, the standing line carried to the next act's standing change (the misses read before the lock)
#⟪OVERRIDE checks MARK f8d771e18f03 1 REPAIR (face)⟫
        kern_face=(jl('b767_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns() + ['SIDE-faces-join', 'SIDE-dirichlet-mod-24'])),
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b767_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R377-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal to its blob at the act`s base 15f762dd (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R377)(4) and (5): every dispatch of the act a row of the dispatch bank, its kernel SIDE-explicit-formula, its free memory before the send at or above the hold; the run ids the worklist`s EF_RUNS within MAX_DISPATCHES, none in SIDE-dirichlet-mod-24; each read once after it by that id; the plant a dispatch row with no kernel and no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4, (R377)(4) and (9): each dispatch sent by tools/b767_controls.py`s dispatch route, each command of that route in the capture a dispatch row`s or a refused send`s (rowed dispatch_refused at the network, or refused by the tool before any send and pinned by its time and number), each read once after it by its run id, every dispatch and read row`s free memory at or above the hold, the runs within the act`s cap of 40 and its kinds (36 at most with the restore on; with it off the trial, the closing build and one repeat of each), no cap by price row (b759`s form); no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel written beyond SIDE-explicit-formula ((R377)(4), (12); its main and tags read by G-OFFSET-POST-HOC): each repaired wave 1 kernel`s rebuild-b721 as b766 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at the worklist`s EF_MAIN, moved under (4) alone, to the closing Lean commit where its build from source exited 0 with the restored build`s axioms file and not otherwise, and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS: the corrigendum and the entry; OPEN_TRAILS: the texts of (4) to (7) in the rulings tool`s groups, and the trail; (R377)(1), (4)-(7), (10), (12)); REGISTRY and ERRATA not written (N3); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    # ### b767, Component 4 (the Edit tool): the carried stub replaced -- b766's trail head as OPEN_TRAILS :19273 carries it, read by the
    # ### citation check at step zero (data/b767_citation_check.txt :22, OK; K.B711_TRAIL), the needle b766's own title's opening (tools/acts/
    # ### b766.py :3424), the dash typographic as the landed file holds it, in place of the carried needle, which named b765's head under
    # ### b766's name and b765's ordinal
    ('G-PRIOR-CLOSED-PUSHED', 'b766`s trail record on OPEN_TRAILS (:19273) and its root in the chain', lambda S: '### b766 — lane two, act one hundred and ninety-three, The proof by the banked window, in steps, under (R376)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved; v0.38 to v0.45, b760`s removed branch and SIDE-dirichlet-mod-24 read by G-OFFSET-POST-HOC) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: each a row of the dispatch bank, within MAX_DISPATCHES; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b760 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b758's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b767: (R377)'s rows, written at step zero in place of b766's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch facts767.py a-c and facts767b.py, read-only, 08:38Z-08:44Z;
    # ### PLACE-papers lines through qrule760.py, rule [Q] (3)'s heading found by its digest; kernel lines read as predicates, none printed). A
    # ### place is named by its role or its file name, never by a folder of the host (N5). A PLACE-papers file is read at the act's start
    # ### (K.PRE_PP) where a row asserts its text, so a later run reads the same; REGISTRY's protected section by predicate and digest alone.
    import hashlib as _h
    EF_ = 'D:/SIDE-explicit-formula'
    MOD_ = 'D:/SIDE-dirichlet-mod-24'
    KN_ = 'D:/SIDE-kernel'
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling SCOPE, (1)', 'relay main at the act`s start a0bc04cd, read back by b766 after its closing b635bc94 (an ancestor of it), and read back at the remote (or an ancestor of the remote`s main)',
        gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('a0bc04cd') and gr('D:/relay', 'merge-base', 'b635bc94', 'a0bc04cd').startswith('b635bc94') and bool(rm)
        and gr('D:/relay', 'merge-base', 'a0bc04cd', rm).startswith('a0bc04cd'), 'remote main %s' % rm[:8], '0')
    npp_, tpp_ = gr(PP, 'rev-list', '--count', K.PRE_PP), gr(PP, 'tag', '--list').split()
    add('ruling SCOPE, (1)', 'PLACE-papers main at the act`s start 29de0836, b766`s closing: 2,237 commits and 2 tags there', gr(PP, 'rev-parse', K.PRE_PP).startswith('29de0836') and npp_ == '2237' and len(tpp_) == 2,
        '%s ; %s commits ; %d tags' % (K.PRE_PP[:8], npp_, len(tpp_)), '0')
    TAGS_ = (('v0.38', '21c6edaf', '14ca5725'), ('v0.39', '69da6cd7', 'd1afb4fc'), ('v0.40', 'd86d8cf5', '630cba16'), ('v0.41', '390506fc', 'a3aad4cc'),
             ('v0.42', '001e94ff', '4964e957'), ('v0.43', 'bcd4d481', '819e4a83'), ('v0.44', 'bd024837', '0ba9cd61'))
    er_ = _remote_heads(EF_)
    erm_ = er_.get('refs/heads/main') or ''
    # ### the kernel's branches kept at its remote (b766's list (f), data/b766_closing.txt :2363); push-b765-planted removed at b766 under [K22]
    KB_ = (('push-b766-proof', '3c67b8b5'), ('push-b765-centre', '0ba9cd61'), ('push-b764-runner', '38a57e02'), ('push-b763-arith', 'ec14e9d9'), ('push-b763-keiper', 'a59632eb'),
           ('push-b763-form', '4964e957'), ('push-b763-squares', '819e4a83'))
    op_ = [b_ for b_ in ('push-b763-arith', 'push-b763-keiper') if gr(EF_, 'rev-list', '--count', '0ba9cd61..' + b_) == '1']
    p6_ = gr(EF_, 'rev-list', '--count', '0ba9cd61..3c67b8b5')
    add('ruling SCOPE, (4), (9), (12), N5', 'SIDE-explicit-formula: main 0ba9cd61 (v0.44) at the act`s start, b766 having moved neither main nor a tag; v0.38 to v0.44 the tag objects 21c6edaf, 69da6cd7, d86d8cf5, 390506fc, 001e94ff, bcd4d481 and bd024837 peeling to 14ca5725, d1afb4fc, 630cba16, a3aad4cc, 4964e957, 819e4a83 and 0ba9cd61 (to peel so at the close; v0.45 cut under (4) alone); the remote`s main 0ba9cd61 or its descendant ((4) moves it to the closing Lean commit alone); push-b766-proof at 3c67b8b5, 14 commits past main, the commit push-b767-proof is cut from, kept and read there at the close; push-b765-centre (0ba9cd61), push-b764-runner (38a57e02), push-b763-arith (ec14e9d9), push-b763-keiper (a59632eb), push-b763-form (4964e957) and push-b763-squares (819e4a83) at the remote, kept, the two of b763 one commit past main; push-b765-planted absent, removed at b766 under [K22]',
        K.EF_BASE.startswith('0ba9cd61') and all(gr(EF_, 'rev-parse', t_).startswith(o_) and gr(EF_, 'rev-parse', t_ + '^{commit}').startswith(c_) for t_, o_, c_ in TAGS_)
        and bool(erm_) and gr(EF_, 'merge-base', '0ba9cd61', erm_).startswith('0ba9cd61') and all((er_.get('refs/heads/' + b_) or '').startswith(t_) for b_, t_ in KB_) and len(op_) == 2
        and p6_ == '14' and 'refs/heads/push-b765-planted' not in er_,
        'remote main %s ; kernel branches at the remote %d of 7 ; one past main %d of 2 ; push-b766-proof past main %s ; push-b765-planted %s ; v0.44 peel %s' % (
            erm_[:8] or '-', sum(1 for b_, t_ in KB_ if (er_.get('refs/heads/' + b_) or '').startswith(t_)), len(op_), p6_, 'PRESENT' if 'refs/heads/push-b765-planted' in er_ else 'absent',
            gr(EF_, 'rev-parse', 'v0.44^{commit}')[:8]), '0')
    mr_ = _remote_heads(MOD_)
    add('ruling (12), N5', 'SIDE-dirichlet-mod-24: the remote`s main e5ebdd15 with v0.2.0, the tag object e5c84316, peeling to it (to peel so at the close; no kernel beyond SIDE-explicit-formula touched)',
        gr(MOD_, 'rev-parse', 'v0.2.0').startswith('e5c84316') and gr(MOD_, 'rev-parse', 'v0.2.0^{commit}').startswith('e5ebdd15') and (mr_.get('refs/heads/main') or '').startswith('e5ebdd15'),
        'remote main %s ; v0.2.0 peel %s' % ((mr_.get('refs/heads/main') or '-')[:8], gr(MOD_, 'rev-parse', 'v0.2.0^{commit}')[:8]), '0')
    add('ruling (12), N5', 'SIDE-kernel`s clone: v1.5 the tag object 922c0fc7 peeling to 0e5233f0, its main at f8534ef2, nothing changed (no kernel beyond SIDE-explicit-formula touched)',
        gr(KN_, 'rev-parse', 'v1.5').startswith('922c0fc7') and gr(KN_, 'rev-parse', 'v1.5^{commit}').startswith('0e5233f0') and gr(KN_, 'rev-parse', 'main').startswith('f8534ef2')
        and not gr(KN_, 'status', '--porcelain', '-uno'), 'v1.5 peel %s ; main %s' % (gr(KN_, 'rev-parse', 'v1.5^{commit}')[:8], gr(KN_, 'rev-parse', 'main')[:8]), '0')
    mi_ = lines_of(p('data', 'b766_mirror.txt'))
    add('ruling (9) [K24]', 'data/b766_mirror.txt :3 and :6, b766`s export of 2026-11-22, the one carrying the root line: MANIFEST md5 48ac7d57b54f82c1f644e7c56d9bcd7e, 84 files with MANIFEST; the root line naming b766 1f57b5d3',
        'md5 48ac7d57b54f82c1f644e7c56d9bcd7e' in at(mi_, 3) and 'files 84 + MANIFEST' in at(mi_, 3) and 'Act root: b766 1f57b5d368f905c7' in at(mi_, 6), at(mi_, 3)[:60], '1')
    # ### (R377)(1): b766 at its weight, from its closing bank's head line and its counter; (3): its carried list (f) and (g)
    add('ruling (1)', 'data/b766_closing.txt :1, the head line: relay 603451cf (the record`s commit; the ruling names the closing b635bc94 and main a0bc04cd), PLACE-papers 29de083, suite 109 of 116, the root 1f57b5d3, 5 prompts answered, scores 4 of 8 HELD, 22 defects; :5, the counter CLAIM 8, CLOSE 161, REPEAT 126 OF 169',
        at(cl, 1).startswith('b766 closed: relay 603451cf, PLACE-papers 29de083; suite 109 of 116; root 1f57b5d368f905c7') and '5 prompts answered; scores 4 of 8 HELD; 22 defects' in at(cl, 1)
        and 'CLAIM 8, CLOSE 161, REPEAT 126 OF 169' in at(cl, 5), at(cl, 1)[:60], '1')
    add('ruling (3), (4), (12)', 'data/b766_closing.txt :2345-:2366, CARRIED FORWARD, (f) and (g): the push-b766* branches of relay and PLACE-papers left for this step zero; the kept branches by name, push-b766-proof at 3c67b8b5 kept by the author`s word, push-b764-runner at 38a57e02, push-b765-planted removed after [K22]; the closing push-out bank for this act to commit',
        at(cl, 2345).startswith('### CARRIED FORWARD.') and at(cl, 2360).lstrip().startswith('(f) Branches left for the next act`s step zero: the push-b766* branches of relay and PLACE-papers. KEPT, not for deletion:')
        and 'port-b707 of SIDE-lv-conservation' in at(cl, 2361) and 'push-b759-weil' in at(cl, 2362) and 'push-b766-proof at 3c67b8b5' in at(cl, 2363) and 'push-b764-runner at 38a57e02' in at(cl, 2363)
        and 'push-b765-planted removed after [K22]' in at(cl, 2363) and 'push-b757-workflow of SIDE-dirichlet-mod-24' in at(cl, 2364) and 'corrigendum-b723' in at(cl, 2364)
        and 'challenge-b720-h2-sign-iff-rh' in at(cl, 2365) and at(cl, 2366).lstrip().startswith('(g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.'), 'present', '0')
    # ### N3, N5: REGISTRY's heading of rule [Q] (3) by its digest alone, at the act's start (REGISTRY not written this act)
    rg0_ = _blob(PP, K.PRE_PP, 'REGISTRY.md').split(NL)
    hq_ = [k_ for k_, l_ in enumerate(rg0_, 1) if _h.sha256(l_.encode('utf-8')).hexdigest().startswith('53d53060a58f6b9b')]
    add('N3, N5, (12)', 'REGISTRY at the act`s start: rule [Q] (3)`s heading found by the sha256 of its line, opening 53d53060a58f6b9b, at one line (:374); no line of the section printed; REGISTRY not written this act',
        hq_ == [374], 'lines carrying the digest %d, at %s' % (len(hq_), hq_), '5')
    # ### (12), N3: REGISTRY, the census and the map's two files at the act's start, by their lengths (no line of any printed or written)
    sm0_ = _blob(PP, K.PRE_PP, 'SPIRAL_MAP.md').split(NL)
    sm7_ = _blob(PP, K.PRE_PP, 'SPIRAL_MAP_v0_7.md').split(NL)
    cs0_ = _blob(PP, K.PRE_PP, 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md').split(NL)
    add('ruling (12), N3', 'REGISTRY (1,338 lines) with :1002 the pointer of SPIRAL_MAP.md, no cell; SPIRAL_MAP.md (547 lines) and SPIRAL_MAP_v0_7.md (616 lines); the census v0.8.3 (1,576 lines) -- each at the act`s start, none written ([M4]`s order merges the map at a later act)',
        at(rg0_, 1002).startswith('**`SPIRAL_MAP.md`, a pointer, no cell:**') and len(rg0_) == 1339 and len(sm0_) == 548 and len(sm7_) == 617 and len(cs0_) == 1577,
        'REGISTRY %d ; map %d ; v0.7 %d ; census %d' % (len(rg0_) - 1, len(sm0_) - 1, len(sm7_) - 1, len(cs0_) - 1), '5')
    # ### (10): the INTEGRATION line's cluster and keystone at the act's start -- SPIRAL_MAP's cluster table naming The Epstein instance
    ce0_ = [k_ for k_ in range(247, 294) if 'The Epstein instance' in at(sm0_, k_)]
    add('ruling (10)', 'SPIRAL_MAP`s cluster table (:247-:293) naming The Epstein instance at :276, the INTEGRATION line`s cluster; phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, its keystone, present by its blob`s type',
        at(sm0_, 247).startswith('### Clusters') and at(sm0_, 294).startswith('### Cross-cluster bridges') and ce0_ == [276]
        and gr(PP, 'cat-file', '-t', K.PRE_PP + ':phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md') == 'blob', 'cluster rows naming it %s' % (ce0_ or 'none'), '5')
#⟪END⟫
#⟪SECTION citation 2⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
    # ### b761: no row between the events bank's read and its numbers
#⟪END⟫
#⟪SECTION citation 3⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
    # ### b761: no row between the events' numbers and the defects bank's read
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b767 step zero: (R377)(1)'s counts over b766's banks, written in place of the carried rows over b765's (the carry's refusal removed,
    # ### the body rewritten): its events (1)-(131), its post-seal events (132)-(147) and its defects (a)-(v), each row tagged by the reader's
    # ### owner form -- the events 123 CLOSE and 8 CLAIM (101 REPEAT), the post-seal 16 CLOSE and 0 CLAIM (15 REPEAT), the defects 22 CLOSE and
    # ### 0 CLAIM (10 REPEAT), as the banks read at 08:38Z (scratch facts767.py a), together b766's counter of 169 with REPEAT 126
    # ### (data/b766_closing.txt :5); the navigator's claims (i)-(ix) of (1), CLAIM, enter b767's corrigendum
    ps_ = lines_of(p('data', 'b766_events_postseal.txt'))
    pst_ = [int(m_.group(1)) for m_ in (re.match(r'^    \((\d+)\) ', l_) for l_ in ps_) if m_]
    add('ruling (1), ferry (read first)', 'b766`s events (1)-(131), its post-seal events (132)-(147) and its 22 lettered defects (a)-(v) (data/b766_events.txt, data/b766_events_postseal.txt, data/b766_defects.txt)',
        starts == list(range(1, 132)) and pst_ == list(range(132, 148)) and letters == list('abcdefghijklmnopqrstuv'),
        'events %s ; post-seal %s-%s ; letters %d (%s-%s)' % (starts[-1:], pst_[:1], pst_[-1:], len(letters), letters[:1], letters[-1:]), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_, ncl_, nrp_ in (('data/b766_events.txt', ev, 131, 8, 101), ('data/b766_events_postseal.txt', ps_, 16, 0, 15), ('data/b766_defects.txt', dl, 22, 0, 10)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_ for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        cn_ = [m_.group(2) for m_ in tg_].count
        rp_ = [m_.group(3) for m_ in tg_].count('REPEAT')
        add('ruling (1), (10), ferry (read first)', '%s: %d rows, each tagged by the reader`s owner form, CLAIM %d, CLOSE %d and REPEAT %d' % (f_, nr_, ncl_, nr_ - ncl_, nrp_),
            len(rr_) == nr_ and len(tg_) == nr_ and cn_('CLAIM') == ncl_ and cn_('CLOSE') == nr_ - ncl_ and rp_ == nrp_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d ; REPEAT %d' % (len(rr_), len(tg_), cn_('CLAIM'), cn_('CLOSE'), rp_), '1')
    fi0_ = _blob(PP, K.PRE_PP, 'FINDINGS.md').split(NL)
    ot0_ = _blob(PP, K.PRE_PP, 'OPEN_TRAILS.md').split(NL)
    add('ruling (1)', 'FINDINGS :%d, b766`s entry, the proof by the banked window in steps under (R376); :%d, b765 at its weight inside it' % (K.B711_ENTRY, 16017),
        at(fi0_, K.B711_ENTRY).startswith('## The proof by the banked window, in steps, under (R376): b765 at its weight') and at(fi0_, 16017).startswith('**b765 at its weight and the corrigendum** ((R376)(1))'),
        'present', '1')
    add('ruling (1), (10), Component 5', 'FINDINGS :%d, b766`s corrigendum to b765`s record, short, the form b767`s follows ((1): data/b766_corrigendum.txt`s form); no weight line of its own; FINDINGS` last non-blank line :16078 at the act`s start, b766`s bare INTEGRATION line, the one (10) gives this act' % K.B711_CORRIGENDUM,
        at(fi0_, K.B711_CORRIGENDUM).startswith('## Corrigendum to b765’s record, short') and K.B711_WEIGHT is None and max([k_ for k_, l_ in enumerate(fi0_, 1) if l_.strip()] or [0]) == 16078
        and at(fi0_, 16078) == 'INTEGRATION: cluster The Epstein instance ; keystone phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md ; stage CLUSTERED', 'present', '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b766`s trail record' % K.B711_TRAIL, at(ot0_, K.B711_TRAIL).startswith('### b766 — lane two, act one hundred and ninety-three, The proof by the banked window, in steps, under (R376)'),
        'present', '1')
    add('ruling (1), (12)', 'OPEN_TRAILS :%d, b766`s open-orders line, 70 open; :19333, its scores line (N1 to N4 REFUTED); :19335, its Next line, the file`s last non-blank at the act`s start' % K.TRAIL_ORDERS,
        at(ot0_, K.TRAIL_ORDERS).startswith('**The open orders:** 70 open') and at(ot0_, 19333).startswith('**N1 REFUTED · N2 REFUTED · N3 REFUTED · N4 REFUTED · N5 HELD')
        and at(ot0_, 19335).startswith('**Next:**') and max([k_ for k_, l_ in enumerate(ot0_, 1) if l_.strip()] or [0]) == 19335, 'present', '1')
    # ### (R377)(4), (5), (7) and the ferry's read-first list (OPEN_TRAILS :19221-:19271): the entries of the orders and lines they name, each by
    # ### its line at the act's start; the two orders that [S1] and [R1] enter, absent there
    ORD_ = ((19271, '`W-ORD-LI-ARITH` CARRIED under `(R376)`(4)(d), THE PROOF IN PART'), (19223, '`W-ORD-WINDOW-CERTIFY`, ITS CERTIFICATE BANKED at b766 under `(R376)`(4)(a)'),
            (19257, '`W-ORD-LI-ARITH`, THE PRIME SIDE AS A FINITE SUM, entered at b766 under `(R376)`(4)(b)'), (19259, '`W-ORD-LI-ARITH`, THE WINDOW IN LEAN, entered at b766 under `(R376)`(4)(c)'),
            (19225, "THE FEDERATION MAP'S NAME RULED at b766 under `(R376)`(6)(a)"), (19253, "THE AUTHOR'S WORD OF 2026-11-21 ON THE DEPOSITS AND THE KEYSTONES, entered at b766 under `(R376)`(6)(d)"),
            (19221, '**Dated head, 2026-11-22, b766, `(R376)`(4)(a) and (6)'), (19255, '**Dated head, 2026-11-22, b766, `(R376)`(4)(b) and (4)(c)'),
            (19261, '**Dated head, 2026-11-22, b766, `(R376)`(5)'), (19269, '**Dated head, 2026-11-22, b766, `(R376)`(4)(d)'),
            (19135, '`W-ORD-RUNNER-CACHE` DISCHARGED at b765 under `(R375)`(4)'), (18959, '`W-ORD-WINDOW-CERTIFY` CARRIED under `(R373)`(9)'),
            (19137, '`W-ORD-LI-ARITH`, ITS STATEMENT OF RECORD, entered at b765 under `(R375)`(5)(a)'), (19141, '`W-ORD-LI-ARITH`, ITS WINDOW BANKED at b765 under `(R375)`(5)(c)'))
    nb_ = [k_ for k_, n_ in ORD_ if not at(ot0_, k_).startswith(n_)]
    ab_ = [o_ for o_ in ('W-ORD-SOURCE-BUILD', 'W-ORD-NOVEMBER-RIDERS') if any(o_ in l_ for l_ in ot0_)]
    add('ruling (4), (5), (7)(c), ferry (read first)', 'OPEN_TRAILS at the act`s start, the entries the ruling names: LI-ARITH :19271 ([P2] at b766, compiled at 3c67b8b5), :19257 and :19259, its statement :19137 and its window :19141; WINDOW-CERTIFY :19223 (its certificate, [E1]) and :18959; RUNNER-CACHE :19135, which [C7] re-enters; the map`s name :19225; the author`s word :19253; b766`s dated heads :19221, :19255, :19261 and :19269; W-ORD-SOURCE-BUILD and W-ORD-NOVEMBER-RIDERS absent, [S1] and [R1] entering them',
        len(ORD_) == 14 and not nb_ and '3c67b8b5' in at(ot0_, 19271) and not ab_, 'unfound %s ; present before their entry %s' % (nb_ or 'none', ab_ or 'none'), '2')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula (the files of (4) in the kernel`s source folder and print_targets.txt alone written, (4), (12)), SIDE-kernel and SIDE-dirichlet-mod-24 (each read at its tag, no touch)', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git') and os.path.isdir('D:/SIDE-dirichlet-mod-24/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry, (8), (11), N2', 'tools/standing/ at v1.38.24 entering the act, moved by (8) alone, one commit, the key [K25], VERSION moved by it ((R377)(11), N2, read at the act`s start)', (_blob('D:/relay', K.PRE_RELAY, 'tools/standing/VERSION') or '').strip() == 'v1.38.24',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### b766's mirror the last built, by its file name and hash, the folder that holds it not printed (N5)
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    add('ruling (9) [K24]', 'b766`s mirror, the last built: %s (sha256 %s, 5,116,095 bytes), the export carrying the root line; this act`s mirror built after its last PLACE-papers push, the Project set built from that export under [K24], as at b766' % (os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest()[:8]),
        _h.sha256(mz_).hexdigest().startswith('653fb57a93eff862') and len(mz_) == 5116095 and 'b766' in K.MIRROR_ZIP, '%d bytes' % len(mz_), '5')
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R377)(4), (12), N5: the three kernels' clones with nothing changed or staged, as b766 left them (SIDE-explicit-formula on main at
    # ### v0.44, to be switched to push-b767-proof by (4)'s route; SIDE-dirichlet-mod-24 on push-b757-mod24 at its main's commit; SIDE-kernel on main)
    kc2_ = [(os.path.basename(r_), gr(r_, 'rev-parse', '--abbrev-ref', 'HEAD'), gr(r_, 'status', '--porcelain', '-uno')) for r_ in (EF_, MOD_, KN_)]
    add('ruling (4), (12), N5', 'the three kernels` clones with nothing changed or staged: SIDE-explicit-formula on main (or push-b767-proof), SIDE-dirichlet-mod-24 on push-b757-mod24 (or main), SIDE-kernel on main',
        kc2_[0][1] in ('main', 'push-b767-proof') and kc2_[1][1] in ('push-b757-mod24', 'main') and kc2_[2][1] == 'main' and not any(s_ for _n, _h2, s_ in kc2_),
        ' ; '.join('%s %s %s' % (n_, h_, 'clean' if not s_ else 'CHANGED') for n_, h_, s_ in kc2_), '0')
#⟪END⟫
#⟪SECTION citation 6⟫
    # ### b767: (R377)(1)-(13)'s rows beyond b766's closing and counted banks. A relay tool is read at the act's start (K.PRE_RELAY); a kernel
    # ### file at main's pin 0ba9cd61 (v0.44) or at push-b766-proof's 3c67b8b5, by predicate (no kernel line printed); a PLACE-papers file at
    # ### K.PRE_PP, by predicate (no line printed)
    rr0_ = lambda path_: _blob('D:/relay', K.PRE_RELAY, path_).replace(chr(13), '').split(NL)   # noqa: E731
    kn0_ = lambda path_: _blob(EF_, '0ba9cd61', path_).replace(chr(13), '')   # noqa: E731
    kp6_ = lambda path_: _blob(EF_, '3c67b8b5', path_).replace(chr(13), '')   # noqa: E731
    pp0_ = lambda path_: _blob(PP, K.PRE_PP, path_).replace(chr(13), '').split(NL)   # noqa: E731
    # ### (R377)(8) [K25]: the one-call tool's kernel tables at the act's start
    cm_ = rr0_('tools/standing/commit.py')
    add('ruling (8) [K25], (11)', 'tools/standing/commit.py :160-:166 KERNEL_ACTS and :171-:176 FF_ACTS at the act`s start: SIDE-explicit-formula opened for b757 to b766, b767 named by neither; :179 PUSHTO_ACTS empty; :183-:189 RDELETE_ACTS naming b759, b760 and b766; :194 FORCED_DELETES naming b766 alone -- [K25] admits b767 to the two tables at SIDE-explicit-formula and names nothing for it in RDELETE_ACTS, VERSION moved and a planted control',
        at(cm_, 160).startswith('KERNEL_ACTS = {') and "'b766': ('SIDE-explicit-formula',)}" in at(cm_, 166) and at(cm_, 171).startswith('FF_ACTS = {') and "'b766': ('SIDE-explicit-formula',)}" in at(cm_, 176)
        and at(cm_, 179).startswith('PUSHTO_ACTS = {}') and at(cm_, 183).startswith("RDELETE_ACTS = {'b759':") and "'b766': {'SIDE-explicit-formula': ('push-b765-planted',)}}" in at(cm_, 189)
        and at(cm_, 194).startswith("FORCED_DELETES = {'b766':") and not any("'b767'" in l_ for l_ in cm_), 'b767 named %s ; %d lines' % (any("'b767'" in l_ for l_ in cm_), len(cm_) - 1), '1')
    # ### (R377)(4), (9): the act's Lean branch and the cap's constants as the worklist holds them
    wb_ = K.WEIL_BRANCH[0]
    wl_ = gr(EF_, 'rev-parse', '--verify', '--quiet', wb_)
    add('ruling (4), (9), N1', 'the worklist`s WEIL_BRANCH push-b767-proof at 3c67b8b5, cut from push-b766-proof and not from main (absent at the act`s start, or descending from 3c67b8b5); MAX_DISPATCHES 40, its kinds restore 36, trial 1, closing 1 and repeat 2; no planted branch; REG_COMMIT a string, a commit again once the registration of (6) is made',
        wb_ == 'push-b767-proof' and K.WEIL_BRANCH[1].startswith('3c67b8b5') and (not wl_ or gr(EF_, 'merge-base', '3c67b8b5', wl_).startswith('3c67b8b5'))
        and K.MAX_DISPATCHES == 40 and dict(K.MAX_DISPATCHES_KINDS) == {'restore': 36, 'trial': 1, 'closing': 1, 'repeat': 2} and K.PLANTED_BRANCH == ('', '') and isinstance(K.REG_COMMIT, str),
        '%s %s ; cap %d ; kinds %s' % (wb_, wl_[:8] or 'NOT YET CUT', K.MAX_DISPATCHES, dict(K.MAX_DISPATCHES_KINDS)), '3')
    # ### (R377)(1): the banks the navigator's claims cite
    ms_ = lines_of(p('data', 'b766_misses.txt'))
    add('ruling (1) (iii)-(v), (3)', 'data/b766_misses.txt, the seat`s read of what (R376) missed (20 lines): :3 item (1) the captures, :4 (2) the account`s pattern, :5 (3) N5`s wording, :6 (4) a restore hit, :10 (8) named in neither list of (3), which claims (iii) to (v) cite; :17 the second printing before the lock, its items at :18-:20; the form of this act`s read',
        at(ms_, 3).startswith('  (1) THE CAPTURES ARE EIGHT.') and at(ms_, 4).startswith("  (2) THE ACCOUNT'S PATTERN.") and at(ms_, 5).startswith("  (3) N5'S WORDING.")
        and at(ms_, 6).startswith('  (4) A RESTORE HIT IN THE TOOL.') and at(ms_, 10).startswith('  (8) NAMED IN NEITHER LIST OF (3).') and at(ms_, 17).startswith('## THE SECOND PRINTING, BEFORE THE LOCK')
        and len(ms_) == 21, '%d lines' % (len(ms_) - 1), '1')
    add('ruling (1), (4), (10)', 'data/b766_defects.txt, the lettered defects the ruling cites by letter: (d), (p) and (r), the class a carried constant read with its previous meaning; (h), (t) and (u), on which N1 to N4 were refuted; (m), claim (ii); (r), claim (iv); (g), (j), (k) and (l), the checks before a dispatch',
        all(x_ in letters for x_ in 'dghjklmprtu'), 'missing %s' % ([x_ for x_ in 'dghjklmprtu' if x_ not in letters] or 'none'), '1')
    aa_ = lines_of(p('data', 'b766_author_answers.txt'))
    add('ruling (1) (i), (6), ferry (read first)', 'data/b766_author_answers.txt, the author`s answers to b766`s five prompts (33 lines): :33 the answer at the root, the window at knots graded by octave that (6) registers named in it',
        len(aa_) == 34 and at(aa_, 33).startswith('RESULT (transcript line 294913, 2026-11-23T04:26:45.004Z): The user answered: "b766, the proof by the banked window in steps under (R376), is sealed')
        and 'graded by octave' in at(aa_, 33), '%d lines' % (len(aa_) - 1), '2')
    aw_ = lines_of(p('data', 'b766_author_words_preseal.txt'))
    add('ferry (read first), (5)(a)', 'data/b766_author_words_preseal.txt (32 lines), six words appended by append.py, heads at :1, :8, :22, :25, :28 and :31; :32 the author`s word on the two stops, Option 1, no [C7], main at 0ba9cd61 and no tag cut, the finding to which (5) gives its order',
        len(aw_) == 33 and [k_ for k_, l_ in enumerate(aw_, 1) if l_.startswith('## APPENDED')] == [1, 8, 22, 25, 28, 31] and at(aw_, 32).startswith('Option 1, no [C7]. Main stays at 0ba9cd61 and no tag is cut'),
        '%d lines' % (len(aw_) - 1), '2')
    # ### (R377)(9), (13): the gated push's capture and the builder's step at the act's start
    pg_, ps0_ = rr0_('tools/push_gated.sh'), rr0_('tools/project_set.py')
    add('ruling (9), (13), ferry (read first)', 'tools/push_gated.sh at the act`s start (284 lines), the capture named from the act, the repository and the branch and written masked since [K23] (:63-:67 the mask of the account); tools/project_set.py :2 (669 lines), the builder`s step of b765, the Project set built at the close from the close`s own export under [K24], as at b766',
        len(pg_) == 285 and '_push_out.txt' in NL.join(pg_) and any('account' in at(pg_, k_).lower() for k_ in range(63, 68))
        and at(ps0_, 2).startswith('"""tools/project_set.py -- b765, (R375)(7): THE PROJECT') and len(ps0_) == 670, '%d ; %d lines' % (len(pg_) - 1, len(ps0_) - 1), '5')
    # ### (R377)(4), (9), N1: the dispatch tool and the certificate tool carried
    bc_, bce_ = rr0_('tools/b766_controls.py'), rr0_('tools/b766_certificate.py')
    add('ruling (4), (9), N1, ferry (read first)', 'tools/b766_controls.py :2 (995 lines at the act`s start), the dispatch and the read b766 used, carried as this act`s dispatch tool with the cap of 40 and the kinds of (9), no cap by price row, committed before the first dispatch; tools/b766_certificate.py :2 (576 lines), the certificate tool, carried for the three forms of (4)(a) and committed before its run',
        at(bc_, 2).startswith('"""tools/b766_controls.py -- (R376)(4): THE DISPATCHES OF THE PROOF BY THE BANKED WINDOW') and len(bc_) == 996
        and at(bce_, 2).startswith('"""b766_certificate.py -- (R376)(4)(a): THE CERTIFICATE, BANKED AS DATA BEFORE ANY DISPATCH') and len(bce_) == 577, '%d ; %d lines' % (len(bc_) - 1, len(bce_) - 1), '2')
    # ### (R377)(3), (5)(a): the price table's form and the three runs (5)(a) reads, each by its line in b766's dispatch bank
    pr_, ct_ = lines_of(p('data', 'b766_price.txt')), lines_of(p('data', 'b766_controls.txt'))
    add('ruling (3), (5)(a), ferry (read first)', 'data/b766_price.txt (68 lines), the price table`s form: :1 its head, :16 the table, :44 its rates by the kind of build, :57 the dispatches against the cap of 20, :60 its ceiling of 24 hours against the lower figures; data/b766_controls.txt (1,756 lines): :31 the 16 dispatches of 20, :32 the first (run 45009051176), :174 run 45027497489 (KFast on a restored build), :1275 run 45047352154 and :1434 run 45051503982 (the closing build from source and its repeat, each stopped under the hold), the three runs of (5)(a)',
        at(pr_, 1).startswith('b766 -- STEP ZERO, (R376)(3): THE PRICE TABLE, FROM BANKED TIMINGS') and at(pr_, 16).startswith('## THE TABLE') and at(pr_, 44).startswith('## THE PRICE`S RATE BY THE KIND OF BUILD')
        and at(pr_, 57).startswith('## THE DISPATCHES AGAINST THE CAP ((R376)(4), (8), N1: SIDE-explicit-formula at most 20') and at(pr_, 60).startswith('## THE CEILING ((R376)(3)): 24 hours against the lower figures')
        and len(pr_) == 69 and at(ct_, 31).startswith('## SIDE-explicit-formula: 16 DISPATCHES OF AT MOST 20') and 'run 45009051176' in at(ct_, 32) and '45027497489' in at(ct_, 174)
        and '45047352154' in at(ct_, 1275) and '45051503982' in at(ct_, 1434) and len(ct_) == 1757, '%d ; %d lines' % (len(pr_) - 1, len(ct_) - 1), '0')
    # ### (R377)(4)(a): b766's plan and certificate, the lines the amended plan reads
    pl_, ce_ = lines_of(p('data', 'b766_plan.txt')), lines_of(p('data', 'b766_certificate.txt'))
    cj_ = open(p('data', 'b766_certificate.json'), 'rb').read() if os.path.exists(p('data', 'b766_certificate.json')) else b''
    add('ruling (4)(a), ferry (read first)', 'data/b766_plan.txt (75 lines): the lemmas b766 did not send at :46 L9, :50 L10, :56 L11 and :59 L12 (the span :46-:61 that (4)(a) amends), :67-:75 the note priced and not built; data/b766_certificate.txt (28 lines): :17 S -6.62468014575 by balls, :18 THE BUDGET, 1902 constants and one width of 21 digits, beside which the Lean`s share is printed; data/b766_certificate.json by its head (226,890 bytes, sha256 4bfd9e780d9af63f; its keys budget, primes, window and S among them)',
        at(pl_, 46).startswith('  (d) L9 the archimedean term as the combination') and at(pl_, 50).startswith('  (d) L10 the enclosures') and at(pl_, 56).startswith('  (d) L11 window_arith_neg')
        and at(pl_, 59).startswith('  (d) L12 controlFailureExists') and at(pl_, 67).startswith('## THE NOTE, PRICED AND NOT BUILT') and len(pl_) == 76
        and 'S -6.62468014575' in at(ce_, 17) and at(ce_, 18).startswith('  THE BUDGET: constants 1902, each an equal share of |S| / 2') and 'one width for all, 21' in at(ce_, 18) and len(ce_) == 29
        and len(cj_) == 226890 and _h.sha256(cj_).hexdigest().startswith('4bfd9e780d9af63f') and all(k_ in json.loads(cj_ or b'{}') for k_ in ('budget', 'primes', 'window', 'S')),
        '%d ; %d lines ; json %d bytes' % (len(pl_) - 1, len(ce_) - 1, len(cj_)), '2')
    # ### (R377)(4)(b), (6): the window's bank, its tool and the registration's form
    wt_ = lines_of(p('data', 'b765_window.txt'))
    wj_ = open(p('data', 'b765_window.json'), 'rb').read() if os.path.exists(p('data', 'b765_window.json')) else b''
    add('ruling (4)(b), (6), ferry (read first)', 'data/b765_window.txt :19, the registered cell M 16 d 3: S -6.62468014575 (the value the control of (6) prints again), PR 657.637691719, k(0) 128.956888485, 16,365 coefficients; :26, the json bank`s sha256 4cbe7be1203883a6, the digest of data/b765_window.json less its final line end (778,941 bytes; the file whole bd228144d213356c)',
        'M 16 d 3 (REGISTERED): S -6.62468014575 ' in at(wt_, 19) and 'PR 657.637691719 ' in at(wt_, 19) and 'k(0) 128.956888485 ' in at(wt_, 19) and 'nonzero c_j 16365 of 16365' in at(wt_, 19)
        and at(wt_, 26).strip() == 'data/b765_window.json: written, 16365 coefficients as rationals, sha256 4cbe7be1203883a6' and len(wj_) == 778941 and wj_.endswith(b'\n')
        and _h.sha256(wj_[:-1]).hexdigest().startswith('4cbe7be1203883a6') and _h.sha256(wj_).hexdigest().startswith('bd228144d213356c'),
        '%d bytes ; less its LF %s ; whole %s' % (len(wj_), _h.sha256(wj_[:-1]).hexdigest()[:16], _h.sha256(wj_).hexdigest()[:16]), '2')
    bw_ = rr0_('tools/b765_window.py')
    add('ruling (4)(b), (6), ferry (read first)', 'tools/b765_window.py :2 (793 lines at the act`s start), the window`s tool: :18-:19 the integral J that (4)(b) writes in the B-spline basis, :23-:32 its closed forms on uniform knots, :33-:34 its own control and the second route by exact piecewise integration in y, the route (6) takes at knots graded by octave; carried as this act`s window tool and committed before its run',
        at(bw_, 2).startswith('"""b765_window.py -- THE SPLINE WINDOW, COMPUTED AND BANKED AS DATA') and len(bw_) == 794 and 'J  = INT_0^inf' in at(bw_, 18) and 'the knots uniform' in at(bw_, 23)
        and at(bw_, 32).startswith('### F_l(0) = -1/(l + 1)^2') and 'by exact piecewise integration in y' in at(bw_, 34), '%d lines' % (len(bw_) - 1), '2')
    rg5_ = lines_of(p('data', 'b765_registration.txt'))
    add('ruling (6)', 'data/b765_registration.txt (5 lines), the form of data/b767_registration.txt: :1 its head, :3 PART ONE H-RUNNER-RESTORE, :5 PART TWO H-SPLINE-WINDOW, the object this act`s registration carries',
        at(rg5_, 1).startswith('b765 -- THE REGISTRATION, WRITTEN BEFORE ANY DISPATCH AND ANY CELL') and at(rg5_, 3).startswith('PART ONE, H-RUNNER-RESTORE.') and at(rg5_, 5).startswith('PART TWO, H-SPLINE-WINDOW. THE OBJECT:')
        and len(rg5_) == 6, '%d lines' % (len(rg5_) - 1), '2')
    # ### (R377)(4)(b)-(e): the declarations each step rests on at 0ba9cd61, as predicates, and the read-first spans
    DQ_ = lambda n_: r'(?m)^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*(theorem|lemma|def|abbrev|structure|inductive|instance)\s+(\S+\.)?' + re.escape(n_) + r'\b'   # noqa: E731
    NC_ = (('ControlFailureExists', 'SIDEExplicitFormula/ControlFailureExists.lean', 29), ('primeTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 170),
           ('archTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 170), ('bracketQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 170), ('cQ', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 408),
           ('poleTerm', 'SIDEExplicitFormula/B321Identity.lean', 62), ('classK', 'SIDEExplicitFormula/H2Sign.lean', 41), ('weilTest', 'Zeta23/ExplicitFormula.lean', 751),
           ('gaussArchQ', 'SIDEExplicitFormula/GaussArchQSteps.lean', 680))
    ncm_ = [n_ for n_, f_, l_ in NC_ if not (re.search(DQ_(n_), kn0_(f_)) and len(kn0_(f_).split(NL)) == l_)]
    seg_ = NL.join(kn0_('SIDEExplicitFormula/ControlFailureExists.lean').split(NL)[22:25])
    add('ruling (4)(b)-(e), ferry (read first)', 'SIDE-explicit-formula at 0ba9cd61 (v0.44), the declarations (4) rests on, each declared in the file the ruling names, by predicate: ControlFailureExists (ControlFailureExists.lean, 28 lines, :23-:25 naming classK, primeTermQ, archTermQ, poleTerm and cQ), primeTermQ, archTermQ and bracketQ (Schema/EpsteinZQ.lean, 169), cQ (Schema/ZQ/LogDeriv.lean, 407), poleTerm (B321Identity.lean, 61), classK (H2Sign.lean, 40), weilTest (Zeta23/ExplicitFormula.lean, 750) and gaussArchQ (GaussArchQSteps.lean, 679)',
        not ncm_ and all(re.search(r'\b' + n_ + r'\b', seg_) for n_ in ('classK', 'primeTermQ', 'archTermQ', 'poleTerm', 'cQ')) and gr(EF_, 'rev-parse', 'v0.44^{commit}').startswith('0ba9cd61'),
        'misses %s' % (ncm_ or 'none'), '3')
    SP_ = (('SIDEExplicitFormula/GaussArchQ.lean', 27, 32, ('archTermQ',)), ('SIDEExplicitFormula/GaussArchQSteps.lean', 630, 630, ('gaussArchQ',)))
    spm_ = [f_ for f_, a_, b_, ns_ in SP_ if not all(re.search(r'\b' + n_ + r'\b', NL.join(kn0_(f_).split(NL)[a_ - 1:b_])) for n_ in ns_)]
    gs_ = re.sub(r'/-.*?-/', '', kn0_('SIDEExplicitFormula/GaussArchQSteps.lean'), flags=re.S)
    gso_ = len(re.findall(r'\bsorry\b', NL.join(l_.split('--')[0] for l_ in gs_.split(NL))))
    add('ferry (read first), (4)(b)', 'the read-first spans on main at 0ba9cd61, each naming what the ruling reads there, by predicate: GaussArchQ.lean :27-:32 archTermQ (35 lines); GaussArchQSteps.lean :630 gaussArchQ, the word sorry in no line outside a comment',
        not spm_ and gso_ == 0 and len(kn0_('SIDEExplicitFormula/GaussArchQ.lean').split(NL)) == 36, 'spans missing a name %s ; sorry outside comments %d' % (spm_ or 'none', gso_), '3')
    DLM_ = r'(?m)^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*(theorem|lemma|def|abbrev|structure|inductive|instance)\s+'
    cs6_ = kn0_('SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean').split(NL)
    op6_ = kn0_('SIDEExplicitFormula/OnePageStatement.lean')
    add('ruling (1) (viii), SCOPE', 'SIDE-explicit-formula at 0ba9cd61: SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean (306 lines), declarations at :281 and :291 and the index 48 named in :281-:301, the least index claim (viii) cites as compiled on main; SIDEExplicitFormula/OnePageStatement.lean (142 lines, 19 declarations), read by its theorem lines; by predicate',
        len(cs6_) == 307 and bool(re.match(DLM_[4:], at(cs6_, 281))) and bool(re.match(DLM_[4:], at(cs6_, 291))) and bool(re.search(r'\b48\b', NL.join(cs6_[280:301])))
        and len(op6_.split(NL)) == 143 and len(re.findall(DLM_, op6_)) == 19, 'CoeffSign %d ; OnePageStatement %d lines' % (len(cs6_) - 1, len(op6_.split(NL)) - 1), '1')
    # ### (R377)(4), (5)(b): push-b766-proof at 3c67b8b5 -- the Window files by their imports, print_targets.txt and the workflow's file
    wf_ = [f_ for f_ in gr(EF_, 'ls-tree', '-r', '--name-only', '3c67b8b5', '--', 'SIDEExplicitFormula/Window/').split(NL) if f_.strip()]
    imp_ = lambda f_: re.findall(r'(?m)^import\s+(\S+)', kp6_(f_))   # noqa: E731
    kf_ = [n_ for n_ in ('CQValues', 'PoleSum', 'Arch') if 'SIDEExplicitFormula.Window.KFast' in imp_('SIDEExplicitFormula/Window/%s.lean' % n_)]
    dt_ = [n_ for n_ in ('ArchBlocks', 'ArchData', 'CQData', 'Coeffs', 'KData', 'PoleData') if imp_('SIDEExplicitFormula/Window/%s.lean' % n_) == ['Mathlib.Data.Real.Basic']]
    pt6_ = kp6_('print_targets.txt').split(NL)
    wy_ = kp6_('.github/workflows/build-module.yml').split(NL)
    add('ruling (4), (5)(b), ferry (read first)', 'push-b766-proof at 3c67b8b5, 14 commits past main and 18 files changed: the 17 files under SIDEExplicitFormula/Window/ by their imports -- CQValues, PoleSum and Arch each importing KFast (the navigator`s reading of (5)(b), checked against (5)(a)), the six data files ArchBlocks, ArchData, CQData, Coeffs, KData and PoleData each importing Mathlib.Data.Real.Basic alone (each data file read to begin with its import); print_targets.txt 752 lines, its last the qualified archTermQ_windowK_k0; .github/workflows/build-module.yml 280 lines, the restore named in 25 and the hold in 11; by predicate',
        len(wf_) == 17 and len(kf_) == 3 and len(dt_) == 6 and len(pt6_) == 753 and [l_ for l_ in pt6_ if l_.strip()][-1:] and [l_ for l_ in pt6_ if l_.strip()][-1].endswith('archTermQ_windowK_k0')
        and len(wy_) == 281 and sum(1 for l_ in wy_ if 'restore' in l_.lower()) == 25 and sum(1 for l_ in wy_ if '2560' in l_ or 'hold' in l_.lower()) == 11
        and gr(EF_, 'rev-list', '--count', '0ba9cd61..3c67b8b5') == '14' and len([l_ for l_ in gr(EF_, 'diff', '--name-only', '0ba9cd61', '3c67b8b5').split(NL) if l_.strip()]) == 18,
        'Window files %d ; KFast importers %d of 3 ; data files %d of 6 ; print_targets %d ; workflow %d' % (len(wf_), len(kf_), len(dt_), len(pt6_) - 1, len(wy_) - 1), '3')
    c5_ = lines_of(p('data', 'b766_ledgers_c5.txt'))
    add('ruling (1), (4), ferry (read first)', 'data/b766_ledgers_c5.txt (193 lines): :18 the E0 gate, each of the 157 theorems found once by its declaration line among the 17 Window files at the commit and read at its statement; :162 a theorem`s row by its file and line; the gate this act`s theorems pass',
        at(c5_, 18).startswith('  THE E0 GATE: each of the 157 theorems found once by its declaration line among the 17 Window files at the commit') and at(c5_, 162).lstrip().startswith('SIDEExplicitFormula.Window.')
        and len(c5_) == 194, '%d lines' % (len(c5_) - 1), '3')
    # ### (R377)(7)(c), [R1]: the passages W-ORD-NOVEMBER-RIDERS names, each line present at the act's start, none printed or written
    PS_ = (('phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 702, (179, 181, 558)), ('phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md', 799, (97,)),
           ('phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 314, (116, 118, 157, 161)), ('phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 712, (82, 144, 156, 236, 240, 349)),
           ('day1/Silence_of_Foundations.md', 266, (15,)))
    psm_ = [(os.path.basename(f_), k_) for f_, n_, ks_ in PS_ for k_ in ks_ if not at(pp0_(f_), k_).strip()]
    psl_ = [os.path.basename(f_) for f_, n_, ks_ in PS_ if len(pp0_(f_)) != n_ + 1]
    add('ruling (7)(c), [R1], SCOPE', 'PLACE-papers at the act`s start, the passages W-ORD-NOVEMBER-RIDERS names, each line present and none printed or written: PATHS_TO_THE_CRITICAL_LINE.md :179, :181 and :558 (702 lines); INDEX_ARITY_AT_THE_CRITICAL_LINE.md :97 (799); THE_UNCONDITIONAL_SURROUND.md :116-:118 and :157-:161 (314); SIMPLICITY_OF_RIEMANN_ZEROS.md :82, :144, :156, :236-:240 and :349 (712); day1/Silence_of_Foundations.md :15 (266)',
        not psm_ and not psl_, 'empty %s ; lengths off %s' % (psm_ or 'none', psl_ or 'none'), '2')
    # ### (R377)(1) (vii), (12): ERRATA at the act's start and the two fetch-backs the claim cites
    er0_ = pp0_('ERRATA.md')
    fbk_ = [(f_, os.path.getsize(p('data', f_)) if os.path.exists(p('data', f_)) else 0, _h.sha256(open(p('data', f_), 'rb').read()).hexdigest()[:16] if os.path.exists(p('data', f_)) else '')
            for f_ in ('b575_fetchback_21539167.json', 'b575_fetchback_21520474.json')]
    add('ruling (1) (vii), (12)', 'ERRATA at the act`s start (1,161 lines, not written): :375 E-2026-09-14-1 on the deposited descriptions, :773 E-2026-10-01-1 on the descriptions as edited, :787 what is not corrected; data/b575_fetchback_21539167.json (12,846 bytes, sha256 d046d422aa46a75a) and data/b575_fetchback_21520474.json (8,563 bytes, 4a2c8e21aa5e2edb), the fetch-backs claim (vii) cites, by their sizes and hashes',
        at(er0_, 375).startswith('## E-2026-09-14-1 — The deposited descriptions say') and at(er0_, 773).startswith('## E-2026-10-01-1 — The descriptions of the deposit and of SIDE-kernel v1.5 now')
        and at(er0_, 787).startswith('**What is not corrected.**') and len(er0_) == 1162
        and fbk_ == [('b575_fetchback_21539167.json', 12846, 'd046d422aa46a75a'), ('b575_fetchback_21520474.json', 8563, '4a2c8e21aa5e2edb')],
        '%d lines ; %s' % (len(er0_) - 1, [(s_, h_) for _f, s_, h_ in fbk_]), '1')
    # ### (R377)(5) [S1], (7)(c) [R1]: the orders reader's entry form
    os0_, od0_ = rr0_('tools/standing/orderstate.py'), rr0_('tools/standing/orders.py')
    add('ruling (5) [S1], (7)(c) [R1], ferry (read first)', 'tools/standing/orderstate.py :26, the entry form the orders reader takes (103 lines), the form of the entry lines of [S1] and [R1]; tools/standing/orders.py :2 (435 lines), the open orders generated from the record',
        at(os0_, 26).startswith('ENTRYFORM = re.compile(') and 'THE ORDER' in at(os0_, 26) and len(os0_) == 104 and at(od0_, 2).startswith('"""standing/orders.py -- THE OPEN ORDERS GENERATED FROM THE RECORD') and len(od0_) == 436,
        '%d ; %d lines' % (len(os0_) - 1, len(od0_) - 1), '2')
    # ### (R377)(9), (10): the measure's two repairs banks and b766's step rows
    r5_, r6_ = lines_of(p('data', 'b765_repairs.txt')), lines_of(p('data', 'b766_repairs.txt'))
    add('ruling (9), (10)', 'the measure`s two repairs banks: data/b765_repairs.txt (41 lines; [K20] REPAIRED at :13, [K21] REPAIRED v1.38.20 at :30) and data/b766_repairs.txt (80 lines; [K22] REPAIRED v1.38.22 at :13, [K23] v1.38.23 at :33, [K24] v1.38.24 at :53); data/b766_steps.json, b766`s step rows, present; the measure`s figures 5.645 and 5.13 hours as (1) and (9) give them',
        len(r5_) == 42 and 'STATE: REPAIRED' in at(r5_, 13) and 'REPAIRED ; VERSION: v1.38.20' in at(r5_, 30) and len(r6_) == 81 and 'STATE: REPAIRED ; VERSION: v1.38.22' in at(r6_, 13)
        and 'REPAIRED ; VERSION: v1.38.23' in at(r6_, 33) and 'STATE: REPAIRED ; VERSION: v1.38.24' in at(r6_, 53) and os.path.exists(p('data', 'b766_steps.json')),
        '%d ; %d lines' % (len(r5_) - 1, len(r6_) - 1), '5')
    add('ruling (12)', 'tools/research/reproduce.py, the reproduction the standing clauses order run in full', os.path.exists(p('tools', 'research', 'reproduce.py')), 'present', '5')
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), ferry Component 0', 'the push-b766-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R377)(3): act_current alone, then b766's three left files through the one-call tool (K.STEPZERO_CARRIED), each alone -- the closing
    # ### push capture as left, the scan bank, the command bank as N4 read it; tools/mirror_prevbuild.json NOT CARRIED, its working bytes equal to
    # ### HEAD's; data/b764_hook_refusals.txt and data/b765_hook_refusals.txt tracked with their working change uncommitted, b766's and b767's
    # ### untracked, each holding a profile path, none staged
    WANT_ = {'ef89f425': ['data/b766_relay_push-b766-closing_push_out.txt'], '7ef61c6b': ['data/b767_address_scan_commits.txt'],
             'f9c59718': ['data/b766_commands.json', 'data/b766_commands.txt']}
    if not K.ACT_CURRENT_COMMIT:
        add('ruling (3)', 'data/act_current.json -- TO BE COMMITTED at step zero', False, 'NOT COMMITTED', '0')
    else:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', K.ACT_CURRENT_COMMIT).split()
        add('ruling (3)', 'data/act_current.json committed alone at %s, an ancestor of HEAD' % K.ACT_CURRENT_COMMIT, nm_ == ['data/act_current.json']
            and gr('D:/relay', 'merge-base', K.ACT_CURRENT_COMMIT, 'HEAD').startswith(K.ACT_CURRENT_COMMIT), ' '.join(nm_)[:90], '0')
    for c_, s_, w_ in K.STEPZERO_CARRIED:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3)', 'b766`s left file, %s, committed alone at %s (step %d), an ancestor of HEAD' % (w_, c_, s_), sorted(nm_) == sorted(WANT_.get(c_, ['?']))
            and gr('D:/relay', 'merge-base', c_, 'HEAD').startswith(c_), '%d files' % len(nm_), '0')
    add('ruling (3), (9)', 'the three files of (3) committed at step zero, each alone: the closing push capture as left (masked by the gated push since [K23]), data/b767_address_scan_commits.txt, and data/b766_commands.json with data/b766_commands.txt, the command bank as N4 read it; the capture reading unmodified at HEAD; tools/mirror_prevbuild.json not carried, its working bytes equal to HEAD`s',
        sorted(f_ for c_, _s, _w in K.STEPZERO_CARRIED for f_ in WANT_.get(c_, [])) == sorted(f_ for v_ in WANT_.values() for f_ in v_) and K.STEPZERO_SCAN == '7ef61c6b'
        and K.STEPZERO_PREVBUILD is None and not gr('D:/relay', 'status', '--porcelain', '--', 'tools/mirror_prevbuild.json')
        and not gr('D:/relay', 'status', '--porcelain', '--', 'data/b766_relay_push-b766-closing_push_out.txt'), '%d commits' % len(K.STEPZERO_CARRIED), '0')
    # ### gr strips the whole print, so each line is stripped before it is compared
    RF_ = ('data/b764_hook_refusals.txt', 'data/b765_hook_refusals.txt', 'data/b766_hook_refusals.txt', 'data/b767_hook_refusals.txt')
    hr_ = gr('D:/relay', 'status', '--porcelain', '--', *RF_)
    add('ruling (3)', 'data/b764_hook_refusals.txt and data/b765_hook_refusals.txt tracked, the working change of each uncommitted; data/b766_hook_refusals.txt and data/b767_hook_refusals.txt untracked; each holding a profile path, none staged',
        bool(gr('D:/relay', 'ls-files', '--', RF_[0])) and bool(gr('D:/relay', 'ls-files', '--', RF_[1])) and not gr('D:/relay', 'ls-files', '--', RF_[2]) and not gr('D:/relay', 'ls-files', '--', RF_[3])
        and sorted(l_.strip() for l_ in hr_.split(NL)) == ['?? data/b766_hook_refusals.txt', '?? data/b767_hook_refusals.txt', 'M data/b764_hook_refusals.txt', 'M data/b765_hook_refusals.txt'],
        hr_.replace(NL, ' | ') or 'clean', '0')
    # ### the scan bank is appended by the scan before every later commit (the one-call tool's own rows), so the row reads its committed bytes at
    # ### 7ef61c6b as a prefix of its working bytes
    sb0_ = _blob('D:/relay', '7ef61c6b', 'data/b767_address_scan_commits.txt').replace(chr(13), '').encode('utf-8')
    sbw_ = (open(p('data', 'b767_address_scan_commits.txt'), 'rb').read() if os.path.exists(p('data', 'b767_address_scan_commits.txt')) else b'').replace(b'\r', b'')
    add('ruling (3)', 'the scan bank, its bytes at 7ef61c6b a prefix of its working bytes (each later commit`s scan appending its rows by design)',
        bool(sb0_) and sbw_.startswith(sb0_), 'scan bank %d bytes at 7ef61c6b, %d now, prefix %s' % (len(sb0_), len(sbw_), sbw_.startswith(sb0_)), '0')
    fb_ = open(p('data', 'b767_ferry.txt'), 'rb').read() if os.path.exists(p('data', 'b767_ferry.txt')) else b''
    fbl_ = fb_.split(b'\n')
    add('ruling PATHS, (3)', 'data/b767_ferry.txt, the ruling, its texts and its ferry banked from the delivery`s one part: 124 lines, LF line ends, sha256 f4681dd8eec1cf96..., RULING (R377) BEGIN at :1, RULING (R377) END at :105, FERRY BEGIN at :107 and FERRY END at :124',
        len(fbl_) >= 124 and b'\r' not in fb_ and _h.sha256(fb_).hexdigest().startswith('f4681dd8eec1cf96') and fbl_[0] == b'RULING (R377) BEGIN' and fbl_[104] == b'RULING (R377) END'
        and fbl_[106].startswith(b'FERRY BEGIN') and fbl_[123] == b'FERRY END', '%d bytes ; %d line ends ; sha256 %s' % (len(fb_), fb_.count(b'\n'), _h.sha256(fb_).hexdigest()[:8]), '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3), N5', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for b_, t_ in KB_:
        add('ruling (4), (12), N5', '%s kept on SIDE-explicit-formula`s clone at %s and at the remote at its tip (b766`s list (f), data/b766_closing.txt :2360-:2365), no kernel branch removed' % (b_, t_),
            gr(EF_, 'rev-parse', '--verify', '--quiet', b_).startswith(t_) and (er_.get('refs/heads/' + b_) or '').startswith(t_), 'local and remote', '0')
    add('ruling (12), N5', 'push-b759-weil kept on SIDE-explicit-formula`s clone at a3aad4cc, absent at the remote (b766`s list (f), :2362)',
        gr(EF_, 'rev-parse', '--verify', '--quiet', 'push-b759-weil').startswith('a3aad4cc') and 'refs/heads/push-b759-weil' not in er_, 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (12)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3)', 'tools/mirror_prevbuild.json, the builder`s state file the mirror reads, present and tracked (not carried at this step zero, its working bytes equal to HEAD`s)', os.path.exists(p('tools', 'mirror_prevbuild.json'))
        and bool(gr('D:/relay', 'ls-files', '--', 'tools/mirror_prevbuild.json')), 'present', '0')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (3), ferry (read first)', 'data/b767_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b767_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b767_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 5) are the corrigendum with b766 at its weight and the seat's read of what the ruling misses, the price table and the
ceiling of (3), the key [K25] of (8) with its planted control, the plan and the certificate's three forms of (4)(a), the read of the two
stopped runs and the route of (5)(a) and (b), the registration and the window at graded knots of (6), the steps in Lean of (4)(b) to
(4)(d) and the trial of (5)(c) with the dispatch tool's controls, the two data banks and the dispatch bank, the lines of (4) to (7) in
two groups with the roster, the reproduction run of (12), the name and address scan, the touch read of v9 and the standing arms, each row
by its bank's verdict line or by the line its pattern names (section_reading);
(R377)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section;
the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next
act ((R377)(13)); the report and THE MEASURE of (10). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. SIDE-explicit-formula alone written this act ((R377)(4), (12), N5): the commits by the one-call
tool on push-b767-proof cut from push-b766-proof at 3c67b8b5, each pushed by the gated push's branch mode, each dispatch sent by
tools/b767_controls.py and read by its run id from its artifact, the exit file governing; main and the tag by the closing build from
source's outcome under (4), read from the dispatch tool's verdict and the worklist's EF_MAIN and WEIL_TAG; push-b766-proof kept at
3c67b8b5 and push-b767-proof kept at the remote and in the clone; no kernel branch removed; no other kernel written, no tag moved, no pin
moved.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for the act after b767 ((R377)(13)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R365)(2)(iv)(c): the outbound sentence from the one clause
# ### b766's comment here named its own title's banks; b767's stands with TITLE_LINE below
_FT5 =lambda n_: ([l_ for l_ in (rd(n_) or '').split(NL) if l_.startswith('### ### **')] or [''])[-1]
_PM5 = re.search(r'; THE PAIR (.+?) ; MAIN AND THE TAG: (.+?) ; THE TOOL`S CONTROLS', _FT5('b767_controls.txt'))
_LE5 = {}
for _g5 in ('c2', 'c5', 'c6'):   # ### b767: groups c2 and c5 written; c6 where the closing pair enters [C7] or [C8]
    _LE5.update((jl('b767_ledgers_%s.json' % _g5) or {}).get('entered') or {})
_LT5 = [WL.WEIL_TAG[0]] if WL.WEIL_TAG else []   # ### b767: v0.45 where the closing build from source exits 0 with the restored build's axioms file ((R377)(4))
# ### b767, Component 4 (the Edit tool): the carried stub replaced -- the title line from the ferry's ACT line (data/b767_ferry.txt :109)
# ### adjusted to what the act did, each part read at import from its bank: the keys the rulings tool's groups entered (data/b767_ledgers_c2.json,
# ### _c5.json: [S1], [G1] to [G3], [R1], [A2]; [P1] or [P2], [S2] or [S3]; [C7] or [C8] where entered) and the dispatch tool's foot
# ### (data/b767_controls.txt: THE PAIR, MAIN AND THE TAG)
TITLE_LINE = ('b767 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND NINETY-FOUR, THE PROOF BY THE BANKED WINDOW CONTINUED: b766 AT ITS WEIGHT; '
              'THE PLAN AMENDED; THE ARCHIMEDEAN TERM AS THE COMBINATION, THE ENCLOSURES, THE INEQUALITY AND THE CLOSING THEOREM %s; '
              'THE BUILD FROM SOURCE GIVEN ITS ORDER AND TRIED, %s; THE CLOSING BUILD FROM SOURCE %s, %s; '
              'THE WINDOW AT KNOTS GRADED BY OCTAVE REGISTERED AND COMPUTED, %s; THE AUTHOR’S RULINGS ENTERED; ONE KEY; UNDER (R377).**' % (
                  'PROVED WHOLE, [P1]' if 'P1' in _LE5 else ('IN PART, [P2]' if 'P2' in _LE5 else 'NOT ENTERED'),
                  'ITS ROUTE HELD, [S2]' if 'S2' in _LE5 else ('ITS ROUTE DID NOT HOLD, [S3]' if 'S3' in _LE5 else 'NOT ENTERED'),
                  _PM5.group(1) if _PM5 else 'NOT YET READ', re.sub(r' \([^()]*\)$', '', _PM5.group(2)) if _PM5 else 'NOT YET READ',
                  'H-GRADED-WINDOW HELD, [G1]' if 'G1' in _LE5 else ('REFUTED, [G2]' if 'G2' in _LE5 else ('NOT SCORED, [G3]' if 'G3' in _LE5 else 'NOT ENTERED'))))
_K5_MAIN = ('moved to the closing Lean commit %s, %s' % (WL.RUNNER_COMMIT[:8], ('%s cut on the run with the restore off' % WL.WEIL_TAG[0]) if WL.WEIL_TAG else 'no tag cut')) \
    if WL.EF_MAIN[:8] == WL.RUNNER_COMMIT[:8] else ('unmoved, no tag cut, the build from source and the restored build printing different axioms files, [C7]' if 'C7' in _LE5
                                                    else ('unmoved, no tag cut, the closing build from source and its repeat each stopped under the hold, [C8]' if 'C8' in _LE5
                                                          else 'unmoved, no tag cut'))   # ### b767: each case of (R377)(4) by its key
_K5_DEL = ('%s removed at the kernel`s remote and in its clone after [K22], by the one-call tool`s two routes, its listing printed before and its absence read after ((R377)(7))' % ', '.join(WL.KERNEL_REMOVED)) if WL.KERNEL_REMOVED \
    else ('no kernel branch removed by this act: %s ((R377)(7))' % '; '.join(
        '%s`s delete refused by the one-call tool`s route at %s, %s, the branch kept in the clone and at its remote, its name its warning, named here for removal by the author`s word' % r_
        for r_ in WL.KERNEL_DELETES_REFUSED)) if WL.KERNEL_DELETES_REFUSED \
    else 'no kernel branch removed by this act; push-b766-proof kept at 3c67b8b5 and push-b767-proof kept ((R377)(4), (12))'   # ### b767: no removal ordered (KERNEL_DELETES empty)
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b766's sections over b766's objects not carried, b767's set at Component 5), headed as CLOSING_SECTIONS names them. A row
    of two reads its bank's verdict line by vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('b766 at its weight, as its closing record`s head line gives it ((R377)(1))', 'b766_closing.txt', r'(?m)^b766 closed: [^\n]*'),
                ('the seat`s read of what the ruling misses, made after the citation check and the deletes ((R377)(3)), its head', 'b767_misses.txt', r'(?m)^b767 -- [^\n]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            # ### b767, Component 4 (the Edit tool): the act's sections over b767's banks, each verdict line read present (the search tool,
            # ### 19:1xZ: a foot in the price, repair controls, certificate, source-build, controls-control and two ledgers' banks; the window's
            # ### reading line, the two data banks' controls line and the plan's, registration's and repairs' head lines by pattern)
            ('THE PRICE AND THE CEILING ((R377)(3))', [
                ('the price table from banked timings, banked before Component 1, the seat`s own readings printed as the seat`s', 'b767_price.txt'),
                ('the ceiling read before the lock, read-only over the price table`s figures and the step rows', 'b767_ceiling.txt')]),
            ('THE KEY [K25] ((R377)(8))', [   # ### "THE " as G-CLOSING-SENTENCE prefixes each CLOSING_SECTIONS name, b763 defect (o)
                ('the key`s planted control, read at the commit before its repair and at the repair`s commit', 'b767_repair_controls.txt'),
                ('the repairs bank, its one row with its state, its version, its control and its sentence', 'b767_repairs.txt', r'(?m)^b767 -- [^\n]*')]),
            ('THE PLAN AND THE CERTIFICATE`S THREE FORMS ((R377)(4)(a))', [
                ('the certificate`s three forms and the budget in the Lean, banked before any dispatch, its controls', 'b767_certificate.txt'),
                ('the plan amended, L9`s remainder, L10, L11 and L12, each with its kind, its datum and its price', 'b767_plan.txt', r'(?m)^b767 -- [^\n]*')]),
            ('THE BUILD FROM SOURCE READ AND ITS ROUTE ((R377)(5)(a), (b))', [
                ('the two stopped runs read from their artifacts over the target`s closure, the route stated, a larger runner priced', 'b767_source_build.txt')]),
            ('THE WINDOW AT KNOTS GRADED BY OCTAVE ((R377)(6))', [
                ('the registration of H-GRADED-WINDOW, committed alone before the tool`s run', 'b767_registration.txt', r'(?m)^b767 -- [^\n]*'),
                ('the control at the uniform window, the cell at graded knots and its reading', 'b767_window.txt', r'(?m)^  H-GRADED-WINDOW: [^\n]*')]),
            ('THE STEPS IN LEAN AND THE TRIAL ((R377)(4)(b)-(e), (5)(c))', [
                ('the dispatch and read tool`s controls, the tool committed before its opening dispatch', 'b767_controls_control.txt'),
                ('the table of the logarithms of the primes for L10, written and read back by its control', 'b767_logdata.txt', r'(?m)^  CONTROLS \d+ OF \d+ AS WANTED'),
                ('the factorization of each integer to 16,390 for L11b, written and read back by its control', 'b767_natdata.txt', r'(?m)^  CONTROLS \d+ OF \d+ AS WANTED'),
                ('each dispatch read by its run id from its artifact, the exit file governing; the trial, the pair, and main with the tag', 'b767_controls.txt')]),
            ('THE LINES OF (4) TO (7) ((R377)(4)-(7))', [
                ('group c2: [S1] with W-ORD-SOURCE-BUILD`s entry line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS` entry line and [A2] under one dated head', 'b767_ledgers_c2.txt'),
                ('group c5: [P2] and [S2] under their own head, the E0 gate over every compiled name of SIDEExplicitFormula.Window before it', 'b767_ledgers_c5.txt'),
                ('the roster read after them by tools/standing/orders.py, its count at PLACE-papers HEAD', 'b767_orders.txt', r'(?m)(?<=^### ### \*\*)ORDERS \d+ ; OPEN \d+ ; CLOSED \d+')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED ((R377)(12), the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run in the foreground', 'b767_reproduce.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b767_address_scan.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R365)(2)(vi): composed, not carried
    '    SIDE-explicit-formula as (R377)(4) opens it: ' + str(len(WL.KERNEL_COMMITS)) + ' commits on ' + WL.WEIL_BRANCH[0] + ' cut from ' + WL.WEIL_BRANCH_B766[0] + ' at ' + WL.WEIL_BRANCH_BASE[:8] + ', its tip ' + WL.WEIL_BRANCH[1][:8] + ', each pushed by the gated push`s branch mode and read back ; main entering at ' + WL.EF_BASE[:8] + ', ' + _K5_MAIN + ', never forced ; ' + WL.ZQ_TAG[0] + ' to ' + WL.WEIL_TAG_B765[0] + ' peeling as before, ' + (('%s cut at the closing Lean commit after main`s read-back' % WL.WEIL_TAG[0]) if WL.WEIL_TAG else 'no ' + WL.WEIL_TAG_CEILING) + ' ;',
    '    ' + ('the local main of SIDE-explicit-formula fast-forwarded to the closing Lean commit by the one-call tool, read back equal' if WL.EF_MAIN[:8] == WL.RUNNER_COMMIT[:8] else 'the local main of SIDE-explicit-formula unmoved') + ' ; SIDE-dirichlet-mod-24`s main ' + WL.M24_MAIN + ' and ' + WL.M24_TAG[0] + ' peeling to ' + WL.M24_TAG[2][:8] + ', unmoved, nothing pushed there ;',
    '    the held branches of SIDE-explicit-formula at their tips, none removed, zq-b730 at ' + WL.ZQ_TIP[:8] + ' unmoved ; ' + ', '.join(b_ for b_, _t in (WL.WEIL_BRANCH_B766, WL.WEIL_BRANCH_B765, WL.WEIL_BRANCH_B764, WL.ARITH_BRANCH_B763, WL.ORDER_BRANCHES_B763[1], WL.WEIL_BRANCH_B763, WL.ORDER_BRANCHES_B763[0])) + ' kept, ' + WL.WEIL_BRANCH_B766[0] + ' at ' + WL.WEIL_BRANCH_B766[1][:8] + ' as b766`s [P2] cites it ; ' + WL.WEIL_BRANCH[0] + ' kept at the remote and in the clone ; ' + _K5_DEL + ' ; the rebuild-b721 branches of the wave 1 kernels as b767 found them ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches in SIDE-explicit-formula of at most ' + str(WL.MAX_DISPATCHES) + ' that (4) caps (N1), with the restore on at most ' + str(dict(WL.MAX_DISPATCHES_KINDS)['restore']) + ', with the restore off the trial, the closing build and one repeat of each where it stopped under the hold, each read by its run id from its artifact, the exit file governing (relay data/b767_dispatch_rows.json, data/b767_controls.txt) ; none in SIDE-dirichlet-mod-24 (' + str(len(WL.M24_RUNS)) + ' rows) ; no pin moved ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each record route, suite part and dispatch ;',
    '    the push-b766-* branches of relay and PLACE-papers deleted at step zero by name, one per message, the --merged listing printed before them as captured shell commands ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ moved by the one commit of (8), ' + WL.STANDING_VERSION_ENTERING + ' to ' + WL.STANDING_VERSION + ', VERSION moved by it, its planted control printed before and after (relay data/b767_repair_controls.txt) ; each act tool committed before its run ; the plan amended of (4)(a) committed before any dispatch and the registration of (6) before the tool`s run at graded knots ; the kernel`s main moved under (4) and at no other time ; the (W) regeneration and the pre-lock dry before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at ' + WL.PRE_PP[:8] + ' ; REGISTRY, ERRATA, the census, the register and the two files of the map not written ; OPEN_TRAILS and FINDINGS each a prefix of its new bytes ; each text of the ruling as entered equal to the ruling`s text with its fields filled (relay data/b767_ledgers_c2.txt, data/b767_ledgers_c5.txt' + (', data/b767_ledgers_c6.txt' if os.path.exists(os.path.join(ROOT, 'data', 'b767_ledgers_c6.txt')) else '') + ') ; no sentence of the act saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved ; a sentence about the control naming the side ; a theorem of a step entered as its own statement and nowhere as the closing theorem ; no figure of the navigator`s workspace printed as a banked figure, the navigator`s sums printed as the navigator`s ; the entry`s INTEGRATION line as (10) gives it ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; the reproduction run as (12) orders it ; no identifier of the author in anything the act wrote, committed or pushed, the kernel`s commits among them, and no byline, the copies of the papers in the Project`s repository carrying theirs as written (relay data/b767_address_scan.txt, data/b767_address_scan_postlock.txt, data/b767_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ; nothing fetched from the web by the seat ((R377)(12)) ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no anchor edited ; in OPEN_TRAILS, each group under its own dated head, [S1] with W-ORD-SOURCE-BUILD`s entry line, [G1], [R1] with W-ORD-NOVEMBER-RIDERS` entry line and [A2] ; [P2] and [S2]' + ''.join(' ; [%s]' % k_ for k_ in ('C7', 'C8') if k_ in _LE5) + ' ; the trail ; no order entered, retired or closed by the seat beyond those lines and the roster`s reading of them ;',
    '    on PLACE-papers main FINDINGS (the corrigendum, the entry) and OPEN_TRAILS (the lines of (4) to (7) and the trail) ; no sentence of a paper written or edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b767`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; no rules bank written, data/b754_rules.txt not rewritten ; the standing clauses` bank not rewritten ;',
    '    tools/standing/ ' + WL.STANDING_VERSION_ENTERING + ' to ' + WL.STANDING_VERSION + ', ' + str(len(WL.STANDING_REPAIRS)) + ' version commit with its planted control (relay data/b767_repairs.txt, data/b767_repair_controls.txt) ; ' + (('HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay ' + WL.HANDOFF_COMMIT[:8]) if WL.HANDOFF_COMMIT else 'HANDOFF.md not written') + ' ; act_current`s shared_edits as standing/carry.py shared reads them, tools/push_gated.sh and tools/project_set.py among them ; the Project`s repository written by its builder alone at [23a] from the close`s own export ([K24]) ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R377)(12) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one ((R377)(13)), the outcome of (6) with its reported figures and prices, the two prices of (7)(d)' + (', the larger runner`s price' if ('S3' in _LE5 or 'C8' in _LE5) else '') + ' and the three forms of the combination with their digits printed beside it, its answer in relay data/b767_author_answers.txt ;',
    '        W-ORD-LI-ARITH as [P2] carries it, the proof to continue at L9c, the band and lambda parts of the combination in the integer form, then L11c, L11d and L12, none of them sent at this act (relay data/b767_plan.txt, data/b767_ledgers_c5.txt) ; W-ORD-WINDOW-CERTIFY open, the certificate`s three forms banked (relay data/b767_certificate.json) ;',
    '        W-ORD-SOURCE-BUILD as [S1] entered it, its route held at the trial by [S2] ; main and the tag: ' + _K5_MAIN + ' (relay data/b767_controls.txt) ; W-ORD-NOVEMBER-RIDERS as [R1] entered it, its trigger the act after [P1] ; the author`s rulings of 2026-11-22 and 2026-11-23 as [A2] places them (relay data/b767_ledgers_c2.txt) ;',
    '        the window at knots graded by octave, H-GRADED-WINDOW as its group entered it, no step of the proof moved to it (relay data/b767_window.txt) ;',
    '        THE MEASURE of (10): this act`s hours from the lock to the closing beside b766`s 5.645 and b765`s 5.13 ; its lettered defects tagged REPEAT whose class is a key that data/b765_repairs.txt or data/b766_repairs.txt reads REPAIRED, wanted 0 ; its lettered defects of the class a carried constant read with its previous meaning, beside b766`s three ; each printed in this message ;',
    '        the items of the seat`s read of what the ruling misses, printed again before the lock (relay data/b767_misses.txt) ; the defects of relay data/b767_defects.txt for the next corrigendum ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; ' + WL.WEIL_BRANCH_B759[0] + ', removed at the kernel`s remote by b760, its local branch on the clone kept at ' + WL.WEIL_BRANCH_B759[1][:8] + ';',
    '        ' + ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (WL.ARITH_BRANCH_B763, WL.ORDER_BRANCHES_B763[1], WL.WEIL_BRANCH_B763, WL.ORDER_BRANCHES_B763[0])) + ' of SIDE-explicit-formula, b763`s, ' + WL.WEIL_BRANCH_B764[0] + ' at ' + WL.WEIL_BRANCH_B764[1][:8] + ', b764`s, ' + WL.WEIL_BRANCH_B765[0] + ' at ' + WL.WEIL_BRANCH_B765[1][:8] + ', b765`s, and ' + WL.WEIL_BRANCH_B766[0] + ' at ' + WL.WEIL_BRANCH_B766[1][:8] + ', b766`s, kept ; ' + WL.WEIL_BRANCH[0] + ' at ' + WL.WEIL_BRANCH[1][:8] + ', this act`s, at the remote and on the clone, kept, its Lean cited there by commit ;',
    '        push-b757-workflow of SIDE-dirichlet-mod-24, a local branch of its clone, merged into its main at ' + WL.M24_MAIN + '; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b767 found them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'beyond SIDE-explicit-formula written ((R377)(12)), there the files of (4) in SIDEExplicitFormula/Window/, print_targets.txt and, under (5), the workflow`s file on ' + WL.WEIL_BRANCH[0] + ' alone ; '
          'SIDE-explicit-formula main %s (' + _K5_MAIN + '), v0.37 %s, v0.17 %s, v0.38 peeling to ' + WL.ZQ_TAG[2][:12] + ', v0.39 to ' + WL.WEIL_TAG_B765[0] + ' as b758, b759, b763 and b765 cut them, ' + (('%s cut by this act' % WL.WEIL_TAG[0]) if WL.WEIL_TAG else 'no ' + WL.WEIL_TAG_CEILING) + ', '
          + 'the held branches off main, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b767: one standing commit, v1.38.24 to v1.38.25, the key [K25] of (8), with its planted control in data/b767_repair_controls.txt
    # ### (the worklist's STANDING_REPAIRS)
#⟪END⟫
#⟪SECTION record 1⟫
    # ### b767 (R377)(4), (12), N5, Component 4 (the Edit tool): SIDE-explicit-formula written on push-b767-proof alone, cut from
    # ### push-b766-proof at 3c67b8b5; main and the tag by the closing build from source's outcome (the worklist's EF_MAIN and WEIL_TAG, the
    # ### groups' [C7] or [C8] where entered); no kernel branch removed; push-b766-proof, push-b765-centre, b764's and b763's branches kept;
    # ### SIDE-dirichlet-mod-24 untouched, as b759 left it
    _le1_ = {}
    for _g1_ in N3_GROUPS:
        _le1_.update((jl('%s_ledgers_%s.json' % (ACT, _g1_)) or {}).get('entered') or {})
    print('  kernels read: %d (SIDE-explicit-formula at main %s, %s, %s peeling to %s as b765 cut it, %s by this act; this act`s branch '
          '%s at %s, the closing Lean commit, cut from %s at %s; no kernel branch removed; the earlier branches kept: %s; '
          'SIDE-dirichlet-mod-24 at main %s with %s peeling to %s, untouched)' % (
              len(ks), K.EF_MAIN[:8], 'moved to the closing Lean commit' if K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8] else (
                  'unmoved, [C7]' if 'C7' in _le1_ else 'unmoved, [C8]' if 'C8' in _le1_ else 'unmoved'),
              K.WEIL_TAG_B765[0], K.WEIL_TAG_B765[2][:8], ('%s cut at %s' % (K.WEIL_TAG[0], K.WEIL_TAG[2][:8])) if K.WEIL_TAG else 'no tag cut',
              K.WEIL_BRANCH[0], K.WEIL_BRANCH[1][:8], K.WEIL_BRANCH_B766[0], K.WEIL_BRANCH_BASE[:8],
              ', '.join('%s at %s' % (b_, s_[:8]) for b_, s_ in (K.WEIL_BRANCH_B766, K.WEIL_BRANCH_B765, K.WEIL_BRANCH_B764, K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1],
                                                                  K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0])),
              K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8]))
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
    b767's form over b767's objects ((R377)(1)-(13)): the corrigendum's foot and json; the price table and the ceiling read before the
    lock (3); the repairs bank's one row, its state and sentence, beside the worklist's standing versions and its control's verdict line
    (8); the certificate's three forms by its foot and its FORMS lines, and the plan's eleven parts (4)(a); the source-build read and its
    route (5)(a), (b); the registration and the window at graded knots (6); the dispatch tool's control bank, the dispatch rows with each
    run's kind, lane, minutes and route (i)'s parts, and its bank with the trial's, the pair's, main's and the last step's lines ((4),
    (5)(c)); the data files of L10a and L11b by their controls; the rulings tool's groups, their files, entered lines, entry lines and
    controls, and group c2's roster; the roster at HEAD by tools/standing/orders.py; (12)'s reproduction run; b766's scores close; the
    citation check; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure, the json
    banks read whole and refused where they are not the act's; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    # ### b767, Component 4 (the Edit tool): this section rewritten for b767's own banks; b766's reads of its three repairs, its data files of
    # ### (4)(c)-(d), its masking and its three readings read banks b767 does not write, and are not carried. Read here: the price table and
    # ### the ceiling read before the lock of (3); the repairs bank's one key of (8) beside the worklist's STANDING_REPAIRS; the certificate's
    # ### three forms and the plan amended of (4)(a); the source-build read and its route of (5)(a)-(b); the registration and the window at
    # ### graded knots of (6); the dispatch tool's controls, the dispatch rows and its bank with the trial's, the pair's and main's lines
    # ### ((4), (5)(c)); the data files of L10 and L11b by their controls; the rulings tool's groups and the roster at HEAD; (12)'s
    # ### reproduction run; b766's close; the citation check; the address scan. Each refuses by name where its bank does not carry its figure.
    prj_ = jl('%s_price.json' % ACT)
    if not isinstance(prj_, dict) or not prj_.get('rows'):
        sys.exit('### data/%s_price.json DOES NOT CARRY ITS ROWS -- NOTHING COMPOSED' % ACT)
    prow_ = dict((r_['key'], r_) for r_ in list(prj_['rows']) + list(prj_.get('beside') or []))
    # ### b767, Component 1 (the Edit tool, after [K25]'s first standing dry, 09:38:32Z, NOT CLEAN on this line): the price table's foot read
    # ### in b767's own form (data/b767_price.txt :54), where the carried pattern read b766's "AGAINST THE CEILING 24 h, NOTHING CARRIED" --
    # ### (R377)(3) carries no rows past the ceiling, its reserve standing in place of them; thirteen figures in the foot's order, the carried
    # ### word read as none (pr_carried None), the texts after that print it rewritten with section 4 at Component 5.
    prf_ = _bfig('%s_price.txt' % ACT, r'\*\*THE PRICE TABLE: STEP ZERO ([\d.]+) h ; THE LOWER SUM ([\d.]+) h AGAINST THE CEILING (\d+) h ; THE UPPER SUM '
                 r'([\d.]+) h ; DISPATCHES (\d+)-(\d+) OF AT MOST (\d+), WITH THE RESTORE ON (\d+)-(\d+) OF AT MOST (\d+) ; THE LEAN (\d+)-(\d+) LINES ; '
                 r'THE LAST STEP DISPATCH BY (\d\d:\d\d:\d\dZ)\.\*\*', 'the price table`s foot')
    # ### b767, Component 1 (the Edit tool, the same dry): the comment carried here put b766's words in (R377)(3)'s mouth ("reads the ceiling
    # ### at step zero and after (4)(c)"); (R377)(3) orders no reading after (4)(c) -- its ceiling of 30 h with 16 in reserve, no step
    # ### dispatch after 14 h, and the act's passing 30 h printed before the lock.
    # ### b767, Component 4 (the Edit tool): the ceiling read before the lock as (R377)(3) orders it, data/b767_ceiling.txt's foot: the
    # ### hours spent from the opening row at the read, the last step dispatch and its hour from the opening row, the hours left of 30 with
    # ### the reserve, the close forecast at b766's hours from its lock, and the word WITHIN THE CEILING or THE ACT WOULD PASS 30 h AT ITS CLOSE
    ce_ = _bfig('%s_ceiling.txt' % ACT, r'\*\*THE CEILING READ BEFORE THE LOCK \(\(R377\)\(3\), read-only, (\d\d:\d\d:\d\dZ)\): SPENT ([\d.]+) h FROM THE OPENING ROW ; '
                r'THE LAST STEP DISPATCH AT (\d\d:\d\d:\d\dZ), ([\d.]+) h FROM THE OPENING ROW ; LEFT (-?[\d.]+) h OF (\d+) h, THE RESERVE (\d+) h ; THE CLOSE AT '
                r'b766`S ([\d.]+) h FROM ITS LOCK, ([\d.]+) h FROM THE OPENING ROW ; (WITHIN THE CEILING|THE ACT WOULD PASS \d+ h AT ITS CLOSE)\.\*\*',
                'the ceiling`s reading before the lock')
    # ### (5): each key's row of the repairs bank -- its class and state from its head, its sentence the quoted lines after it, from its
    # ### opening quote to the first line that ends in a quote -- beside the worklist's STANDING_REPAIRS (version, commit, row commit,
    # ### control line) and each control's verdict line in its bank
    rp_l_ = rdn('%s_repairs.txt' % ACT).replace(chr(13), '').split(NL)
    reps_, i_ = [], 0
    while i_ < len(rp_l_):
        m_ = re.match(r'^    \[(K\d+)\] (CLASS [A-Z]+), ', rp_l_[i_])
        if not m_:
            i_ += 1
            continue
        j_ = i_ + 1
        while j_ < len(rp_l_) and not rp_l_[j_].startswith('     "[%s] ' % m_.group(1)):
            j_ += 1
        k_ = j_
        while k_ < len(rp_l_) and not rp_l_[k_].rstrip().endswith('"'):
            k_ += 1
        head_ = ' '.join(l_.strip() for l_ in rp_l_[i_:j_])
        sent_ = ' '.join(l_.strip() for l_ in rp_l_[j_:k_ + 1])
        st_ = re.search(r'; STATE: (REPAIRED|READ AS DESIGNED|REMOVED|CARRIED)\b', head_)   # ### a state may carry a parenthetical ([K13]'s head :142)
        reps_.append(dict(key=m_.group(1), cls=m_.group(2), state=st_.group(1) if st_ else None,
                          sentence=sent_[1:-1] if sent_.startswith('"[') and sent_.endswith('"') else None))
        i_ = k_ + 1
    srep_ = dict((k_.strip('[]'), (v_, c_, r_, l_)) for k_, v_, c_, r_, l_ in K.STANDING_REPAIRS)
    rctl_ = rdn(K.REPAIR_CONTROLS_BANK.split('/', 1)[1]).replace(chr(13), '').split(NL)
    if [r_['key'] for r_ in reps_] != ['K25'] \
            or any(r_['state'] is None or r_['sentence'] is None or not r_['sentence'].startswith('[%s] ' % r_['key']) for r_ in reps_) \
            or any((r_['key'] in srep_) != (r_['state'] in ('REPAIRED', 'REMOVED')) for r_ in reps_) \
            or any(not (rctl_ + [''] * (l_ + 1))[l_ - 1].startswith('### ### **%s THE CONTROL AS WANTED: ' % k_) for k_, _v, _c, _r, l_ in K.STANDING_REPAIRS) \
            or any(('%s at %s:' % ({'REPAIRED': 'repaired', 'REMOVED': 'removed'}[r_['state']], srep_[r_['key']][0])) not in r_['sentence'] for r_ in reps_ if r_['key'] in srep_):
        sys.exit('### data/%s_repairs.txt DOES NOT CARRY THE ONE KEY OF (8) WITH ITS STATE, ITS SENTENCE, ITS VERSION AND ITS '
                 'CONTROL AS WANTED -- NOTHING COMPOSED' % ACT)
    # ### (4), (5)(c): the dispatch tool's controls and its bank, its foot and its trial's, pair's and main's lines and the last step's
    # ### dispatch, each line as its foot gives it (tools/b767_controls.py cmd_bank, verdict_lines)
    cc_ = _bfig('%s_controls_control.txt' % ACT, r'\*\*THE TOOL`S CONTROLS: (\d+) OF (\d+) AS WANTED ; ALL AS WANTED\.\*\*', 'the dispatch tool`s control bank')
    tr_ = _bfig('%s_controls.txt' % ACT, r'\*\*DISPATCHES (\d+) OF AT MOST (\d+) \(WITH THE RESTORE ON (\d+) OF AT MOST (\d+)\) ; THE TRIAL (\S+) ; THE PAIR (.+?) ; '
                r'MAIN AND THE TAG: (.+) ; THE TOOL`S CONTROLS (\d+) OF (\d+)\.\*\*', 'the dispatch tool`s foot')
    trt_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  THE TRIAL: (.+)$', 'the trial`s line')
    trp_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  THE PAIR: (.+)$', 'the pair`s line')
    trm_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  MAIN AND THE TAG: (.+)$', 'main`s line')
    trl_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  THE LAST STEP`S DISPATCH: (\S+) \(the hour (\S+)\)$', 'the last step`s dispatch')
    if not trt_[0].startswith(tr_[4]) or not trp_[0].startswith(tr_[5]) or trm_[0] != tr_[6]:
        sys.exit('### data/%s_controls.txt DOES NOT CARRY ITS TRIAL`S, PAIR`S AND MAIN`S LINES AS ITS FOOT GIVES THEM -- NOTHING COMPOSED' % ACT)
    # ### (4)(a): the certificate's three forms by its foot and its FORMS lines (the constants, the sum of the |r| and the one width; no r,
    # ### no K(n) and no coefficient read), and the plan amended's eleven parts in the order of sending, each by its name, its commit by git
    cf_ = _bfig('%s_certificate.txt' % ACT, r'\*\*THE THREE FORMS READ: (\d+) OF (\d+) CONTROLS AS WANTED ; THE PRIMES` ONE WIDTH (\d+) DIGITS, THE INTEGERS` (\d+), '
                r'BY PARTS AT ITS LEAST (\d+) \(ORDER (\d+)\)\.\*\*', 'the certificate`s foot')
    cfm_ = re.findall(r'(?m)^  \((p|i|ii)\) (.+?) +N +(\d+) ; SUM \|r\| (\S+) \(10\^[\d.]+\) ; numerator (\d+) digits ;.*; ONE WIDTH (\d+) DIGITS$', rdn('%s_certificate.txt' % ACT))
    if len(cfm_) != 4 or [x_[0] for x_ in cfm_] != ['p', 'i', 'ii', 'ii'] or int(cfm_[0][5]) != int(cf_[2]) or int(cfm_[1][5]) != int(cf_[3]) or cf_[0] != cf_[1]:
        sys.exit('### data/%s_certificate.txt DOES NOT CARRY ITS THREE FORMS AS ITS FOOT GIVES THEM -- NOTHING COMPOSED' % ACT)
    pl_ = re.findall(r'(?m)^  (?:\(4\)\(e\) )?(L\d+[a-d]?) (\w+) -- ', rdn('%s_plan.txt' % ACT))
    if [l_ for l_, _n in pl_] != ['L9a', 'L9b', 'L9c', 'L10a', 'L10b', 'L10c', 'L11a', 'L11b', 'L11c', 'L11d', 'L12']:
        sys.exit('### data/%s_plan.txt DOES NOT CARRY ITS ELEVEN PARTS IN THE ORDER OF SENDING -- NOTHING COMPOSED' % ACT)
    plc_ = g(ROOT, 'log', '-1', '--format=%h', '--abbrev=8', '--', 'data/%s_plan.txt' % ACT).strip()
    # ### (5)(a), (b): the source-build read's foot, the route chosen in its own words and part one's figures
    sbf_ = _bfig('%s_source_build.txt' % ACT, r'\*\*THE READ MADE: (\d+) OF (\d+) CONTROLS AS WANTED ; THE ROUTE STATED\.\*\*', 'the source-build read`s foot')
    sbr_ = _bfig('%s_source_build.txt' % ACT, r'(?m)^  THE ROUTE CHOSEN, \((i{1,3})\): ([^.]+)\.', 'the route chosen')
    sbp_ = _bfig('%s_source_build.txt' % ACT, r'PART ONE, THE TARGET`S MODULES OUTSIDE THE FOLDER [^:]*: [^:]*?: by name (\d+) ; their closure (\d+) ;', 'part one`s figures')
    # ### (6): the window at graded knots -- its reading with the registration's commit, the cell, the figures reported beside it, the
    # ### control's uniform cell and its verdict, the json's line (no coefficient read)
    wv_ = _bfig('%s_window.txt' % ACT, r'(?m)^  H-GRADED-WINDOW: (HELD|REFUTED|NOT SCORED), \[(G[123])\] ; ([\d.]+) h from the registration`s commit \((\w+)\) to this bank, '
                r'the price`s upper ([\d.]+) h$', 'the window`s reading')
    wc_ = _bfig('%s_window.txt' % ACT, r'(?m)^  (\d+) knots, (\d+) coefficients \((\d+) nonzero\) ; S (\S+) \+- (\S+) ;', 'the cell at graded knots')
    wr_ = _bfig('%s_window.txt' % ACT, r'(?m)^  REPORTED BESIDE IT, unregistered: (\d+) coefficients ; rational products (\d+) ; the combination`s primes (\d+), constants (\d+) ; '
                r'the sum of the \|r\| (\S+) ; the budget`s one width (\d+) digits', 'the window`s figures reported beside it')
    wu_ = _bfig('%s_window.txt' % ACT, r'; the uniform window M 16, d 3: S (\S+) \+- ', 'the control`s uniform cell')
    wk_ = _bfig('%s_window.txt' % ACT, r'(?m)^  (THE CONTROL AS WANTED) \(unit at ', 'the control`s verdict')
    wj_ = _bfig('%s_window.txt' % ACT, r'(?m)^  data/b767_window\.json: written, (\d+) coefficients as rationals, sha256 ([0-9a-f]{16})$', 'the window json`s line')
    if not str(K.REG_COMMIT or '-').startswith(wv_[3][:8]) or wj_[0] != wc_[1] or wr_[0] != wc_[1] or not isinstance(jl('%s_window.json' % ACT), dict):
        sys.exit('### data/%s_window.txt DOES NOT CARRY THE REGISTRATION`S COMMIT, ITS CELL`S COEFFICIENTS AND ITS JSON ALIKE -- NOTHING COMPOSED' % ACT)
    # ### (4)(c), (4)(d): the data files of L10a and L11b, each by its controls and its table's line
    ldc_ = _bfig('%s_logdata.txt' % ACT, r'(?m)^  CONTROLS (\d+) OF (\d+) AS WANTED$', 'L10a`s controls')
    ldt_ = _bfig('%s_logdata.txt' % ACT, r'(?m)^  keys (\d+) \(the primes up to ([\d,]+)\) ;.*; the series` lengths the most (\d+), the sum (\d+)$', 'L10a`s table')
    ldw_ = _bfig('%s_logdata.txt' % ACT, r'(?m)^  blocks \[([\d, ]+)\] and three top entries ; the widest interval (\S+) against 2/10\^22$', 'L10a`s blocks')
    ndc_ = _bfig('%s_natdata.txt' % ACT, r'(?m)^  CONTROLS (\d+) OF (\d+) AS WANTED$', 'L11b`s controls')
    ndt_ = _bfig('%s_natdata.txt' % ACT, r'(?m)^  lists (\d+) \(m from 1 to ([\d,]+)\) ; factor pairs (\d+), the most in one list (\d+) ;', 'L11b`s data')
    _B766_READS_C4 = r'''
    # ### (4)(a): the certificate's foot and json, read by keys and counts alone (no value printed), and the plan's twelve lemmas in the order
    # ### of sending, each by its letter of (4) and its name as the plan gives it, the plan's commit by git
    cf_ = _bfig('%s_certificate.txt' % ACT, r'\*\*THE CERTIFICATE BANKED, \[(E[12])\]: (\d+) OF (\d+) CONTROLS AS WANTED ; ([^*]+?)\.\*\*', 'the certificate`s foot')
    cj_ = jl('%s_certificate.json' % ACT)
    cctl_ = [c_ for c_ in ((cj_.get('controls') if isinstance(cj_, dict) else None) or []) if isinstance(c_, dict)]
    if not isinstance(cj_, dict) or cj_.get('act') != ACT or not isinstance(cj_.get('K'), dict) or not isinstance(cj_.get('primes'), int) \
            or not isinstance(cj_.get('budget'), dict) or len(cctl_) != int(cf_[2]) or sum(1 for c_ in cctl_ if c_.get('as_wanted') is True) != int(cf_[1]):
        sys.exit('### data/%s_certificate.json DOES NOT CARRY ITS K VALUES, PRIMES, BUDGET AND CONTROLS AS ITS FOOT GIVES THEM -- NOTHING COMPOSED' % ACT)
    pl_ = re.findall(r'(?m)^  \(([bcd])\) (L\d+) ([^(\n]+?)(?= --| \(|$)', rdn('%s_plan.txt' % ACT))
    if [l_ for _c, l_, _n in pl_] != ['L%d' % i_ for i_ in range(1, 13)]:
        sys.exit('### data/%s_plan.txt DOES NOT CARRY ITS TWELVE LEMMAS IN THE ORDER OF SENDING -- NOTHING COMPOSED' % ACT)
    plc_ = g(ROOT, 'log', '-1', '--format=%h', '--abbrev=8', '--', 'data/%s_plan.txt' % ACT).strip()
    # ### (4)(c) and (4)(d): each data file's bank by its foot, its control's count; [K23]: the captures' masking, its foot and its control
    dfoot_ = r'\*\*THE (?:DATA|BLOCKS) FILE WRITTEN AND READ BACK ; THE CONTROL (\d+) OF (\d+) AS WANTED ; NO [^*]+? PRINTED\.\*\*'
    dt_ = [(n_,) + tuple(int(x_) for x_ in _bfig('%s_%s.txt' % (ACT, n_), dfoot_, 'the %s bank`s foot' % n_))
           for n_ in ('window_data', 'kdata', 'cqdata', 'poledata', 'poledata_rewrite', 'k0data', 'k0blocks')]
    mk_ = _bfig('%s_capture_mask.txt' % ACT, r'\*\*FILES (\d+) ; HITS (\d+) \+ (\d+) ; THE NAME (\d+) BEFORE, (\d+) AFTER ; MASKED WHOLE\.\*\*', 'the masking`s foot')
    mkc_ = _bfig('%s_capture_mask.txt' % ACT, r'\*\*THE MASK`S CONTROL: (\d+) OF (\d+) AS WANTED\.\*\*', 'the masking`s control')
    # ### (5)(a)-(c): each reading's foot and the fields line its text of (X1)-(X3) was filled from
    x1f_ = _bfig('%s_registry_cells.txt' % ACT, r'\*\*THE REGISTRY`S ROWS: (\d+) ROWS OF (\d+) TABLES READ ; KEYSTONE (\d+) ; UNPLACED (\d+) ; CONTROLS (\d+) OF (\d+) AS WANTED ; '
                 r'WRITTEN\.\*\*', 'the registry`s rows` foot')
    x1s_ = _bfig('%s_registry_cells.txt' % ACT, r'(?m)^## \[X1\]`S FIELDS: (.+)$', '[X1]`s fields')
    x2f_ = _bfig('%s_lean_join.txt' % ACT, r'\*\*THE LEAN JOINED TO THE PAPERS: DECLARATIONS (\d+) ; PAPER (\d+) ; PAGE ALONE (\d+) ; NEITHER (\d+) ; THE CANDIDATE '
                 r'(DIFFERING AS PRINTED|REPRODUCED) ; CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.\*\*', 'the join`s foot')
    x2s_ = _bfig('%s_lean_join.txt' % ACT, r'(?m)^## \[X2\]`S FIELDS: (.+)$', '[X2]`s fields')
    x3f_ = _bfig('%s_sweep.txt' % ACT, r'\*\*THE LEDGER AGAINST THE KEYSTONES: ENTRIES (\d+) ; WITH A NAME (\d+) \(CARRIED (\d+), NOT (\d+)\) ; NO KEYSTONE (\d+) ; '
                 r'NO SUCH NAME (\d+) OF (\d+) LINES ; CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.\*\*', 'the sweep`s foot')
    x3s_ = _bfig('%s_sweep.txt' % ACT, r'(?m)^## \[X3\]`S FIELDS: (.+)$', '[X3]`s fields')
'''   # ### b767, Component 4: b766's reads of its certificate, plan, data files, masking and three readings above, kept as a string, not run
    # ### b766's reads of its trial's verdict, its registration, its window, its gate, its four readings and its builder, kept below as a
    # ### string, not run: their banks are b766's alone
    _B765_READS = r'''
    trh_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  H-RUNNER-RESTORE: (HELD|REFUTED|NOT SCORABLE)(?: ; (.+))?$', 'the trial`s verdict line')
    trl_ = _bfig('%s_controls.txt' % ACT, r'(?m)^  THE PLANTED BUILD: (.+)$', 'the planted build`s line')
    trm2_ = re.search(r'(?m)^  THE SECOND SAVE ON MAIN \(the author`s word on the save on main\): (.+)$', rdn('%s_controls.txt' % ACT))   # ### b767: the second save of the author`s word on the save on main (dispatch 11, the bank`s :72), read where sent; the entry had printed the first alone
    trm_ = (trm_[0] + (('; the second, by the author`s word on the save on main: %s' % trm2_.group(1)) if trm2_ else ''),) + tuple(trm_[1:])
    trs_ =re.findall(r'(?m)^  THE STATEMENT, run (\d+) at ([0-9a-f]{8}): (COMPILED|NOT COMPILED) \((.*)\)$', rdn('%s_controls.txt' % ACT))
    if trh_[0] != tr_[6] or not trs_:
        sys.exit('### data/%s_controls.txt DOES NOT CARRY ITS VERDICT LINE BY ITS FOOT AND THE STATEMENT`S READS -- NOTHING COMPOSED' % ACT)
    # ### [G2], its two parts: the registration's head and its date
    rg_ = _bfig('%s_registration.txt' % ACT, r'(?m)^b767 -- THE REGISTRATION, WRITTEN BEFORE ANY DISPATCH AND ANY CELL \((\d{4}-\d\d-\d\d)\), under \(R377\)\(4\) and \(5\)\(c\)\.$', 'the registration`s head')
    # ### (5)(c): the window's reading, its sentence, the three cells and its json
    wv_ = _bfig('%s_window.txt' % ACT, r'(?m)^  H-SPLINE-WINDOW: (HELD|REFUTED|NOT SCORABLE)$', 'the window`s reading')
    ws_ = _bfig('%s_window.txt' % ACT, r'(?m)^  THE SENTENCE: (.+)$', 'the window`s sentence')
    wc_ = dict((m_.group(1), m_.groups()[1:]) for m_ in re.finditer(r'(?m)^  M (\d+) d 3 \((?:REGISTERED|REPORTED, unregistered)\): S (\S+) \+- (\S+) ; .*?; nonzero c_j (\d+) of (\d+) ; '
                                                                  r'rational products (\d+) ;', rdn('%s_window.txt' % ACT)))
    wj_ = _bfig('%s_window.txt' % ACT, r'(?m)^  data/b767_window\.json: written, (\d+) coefficients as rationals, sha256 ([0-9a-f]{16})$', 'the window json`s line')
    wjj_ = jl('%s_window.json' % ACT)
    if sorted(wc_) != ['16', '32', '8'] or not isinstance(wjj_, dict) or wjj_.get('M') != 16 or wjj_.get('d') != 3 or wjj_.get('ncoef') != int(wj_[0]) \
            or len(wjj_.get('coefficients') or []) != int(wj_[0]) or wc_['16'][3] != wj_[0]:
        sys.exit('### data/%s_window.txt AND ITS JSON DISAGREE ON THE REGISTERED CELL OR ITS COEFFICIENTS -- NOTHING COMPOSED' % ACT)
    # ### (5)(b)'s gate: its reading and its two cells
    gv_ = _bfig('%s_gauss_gate.txt' % ACT, r'(?m)^  THE GATE (PASSES|FAILS)', 'the gate`s reading')
    gc_ = re.findall(r'(?m)^  (rung983|mid1021_1024) \(data/b709_grid\.txt :(\d+), index \d+\): S by the right side (\S+) \+- \S+ ; banked S_NN \S+ \+- \S+ ; difference (\S+) \+- \S+ ; to 6 digits (True|False) ;',
                     rdn('%s_gauss_gate.txt' % ACT))
    if len(gc_) != 2:
        sys.exit('### data/%s_gauss_gate.txt DOES NOT CARRY ITS TWO CELLS -- NOTHING COMPOSED' % ACT)
    # ### (6)(a)-(d): the premise positions' foot, the map's counts and acts, the held branches' readings, the reading of (6)(d)
    pp6_ = _bfig('%s_premise_positions.txt' % ACT, r'\*\*PREMISES (\d+): A HYPOTHESIS BY DESIGN (\d+), DERIVED (\d+), OF THE HYPOTHESIS`S STRENGTH (\d+), NONE OF THESE COMPILED (\d+) ; '
                 r'THE CONTROL (AS WANTED|NOT AS WANTED) ; NO ORDER RETIRED\.\*\*', 'the premise positions` foot')
    mp_ = _bfig('%s_map_pair.txt' % ACT, r'(?m)^  the two files differ in (\d+) lines \((\d+) of SPIRAL_MAP_v0_7\.md and (\d+) of SPIRAL_MAP\.md\), in (\d+) ranges$', 'the map`s count')
    ma_ = _bfig('%s_map_pair.txt' % ACT, r'(?m)^  a reader of SPIRAL_MAP_v0_7\.md alone does not see the \d+ lines of SPIRAL_MAP\.md in them, written by (.+)$', 'the map`s acts')
    hb_ = re.findall(r'(?m)^  (detection-region-b559|vendor-bulka-backport-b566|grh-weil-b569-held|challenge-b720-h2-sign-iff-rh): (.+)$',
                     rdn('%s_held_branches.txt' % ACT).split('## THE READING')[-1])
    if [b_ for b_, _w in hb_] != ['detection-region-b559', 'vendor-bulka-backport-b566', 'grh-weil-b569-held', 'challenge-b720-h2-sign-iff-rh'] \
            or '  no branch removed' not in rdn('%s_held_branches.txt' % ACT).split(NL):
        sys.exit('### data/%s_held_branches.txt DOES NOT CARRY ITS FOUR READINGS AND NO BRANCH REMOVED -- NOTHING COMPOSED' % ACT)
    pi_ = _bfig('%s_pi01_reading.txt' % ACT, r'\*\*ADDRESSES NAMED (\d+) ; REACHED AND READ (\d+) ; NOT REACHED (\d+)\.\*\*', 'the reading of (6)(d)`s foot')
    # ### (7): the builder's controls and the repository's bank (the account masked in it)
    pc7_ = _bfig('%s_project_set_control.txt' % ACT, r'\*\*THE CONTROLS: (\d+) OF (\d+) AS WANTED\*\*', 'the builder`s controls')
    psj_ = jl('%s_project_set_repo.json' % ACT)
    if not isinstance(psj_, dict) or (psj_.get('create') or {}).get('as_wanted') is not True or ((psj_.get('create') or {}).get('view') or {}).get('visibility') != 'PRIVATE' \
            or (psj_.get('clone') or {}).get('as_wanted') is not True:
        sys.exit('### data/%s_project_set_repo.json DOES NOT CARRY THE REPOSITORY CREATED PRIVATE AND CLONED -- NOTHING COMPOSED' % ACT)
    psb_ = jl('%s_project_set_build.json' % ACT)   # ### (7)'s build at the close, between [12] and [14]; absent before it
'''
    dr_rows_ = json.loads(rdn('%s_dispatch_rows.json' % ACT)) or []
    # ### b767: each run of the trial by its dispatch row and its read row -- its item, number, id, commit, restore input, verdict and the
    # ### run's and the build's minutes as the read takes them from the artifact -- for (11)'s "what each item took"
    rdr_ = dict((str(r_.get('run')), r_) for r_ in dr_rows_ if r_.get('kind') == 'read')
    runs_ = [dict(item=r_.get('item'), n=int(r_.get('n')), run=str(r_.get('run')), sha=r_.get('sha', '')[:8], restore=r_.get('restore'), at=r_.get('at'),
                  verdict=(rdr_.get(str(r_.get('run'))) or {}).get('verdict'), run_min=(rdr_.get(str(r_.get('run'))) or {}).get('run_min'),
                  build_min=(rdr_.get(str(r_.get('run'))) or {}).get('build_min'),
                  # ### the exit file, the axioms file's digest and lines and the cache's from-source word, for the seat's reading beside the verdict
                  exit=(rdr_.get(str(r_.get('run'))) or {}).get('build_exit'), ax_sha=str((rdr_.get(str(r_.get('run'))) or {}).get('axioms_sha256') or '')[:16],
                  ax_lines=(rdr_.get(str(r_.get('run'))) or {}).get('axioms_file_lines'),
                  from_source=((rdr_.get(str(r_.get('run'))) or {}).get('cache') or {}).get('from_source'),
                  # ### b767: the cache record's restore line (true an exact key, false a key by the prefix, none nothing restored) and the save
                  hit=((rdr_.get(str(r_.get('run'))) or {}).get('cache') or {}).get('hit'),
                  saved=((rdr_.get(str(r_.get('run'))) or {}).get('cache') or {}).get('saved'),
                  # ### b766, (R376)(6)(c) [H5], carried: the kind recorded beside each run, and the runner's lowest free memory from its memory log
                  kind=(rdr_.get(str(r_.get('run'))) or {}).get('restore_kind'), low_mb=(rdr_.get(str(r_.get('run'))) or {}).get('runner_low_mb'),
                  # ### b767, Component 4 (the Edit tool): the lane, and route (i)'s part one -- its exit and the two parts' lows -- where the run read it
                  lane=r_.get('lane'), p1_exit=(rdr_.get(str(r_.get('run'))) or {}).get('part_one_exit'), p1_mods=(rdr_.get(str(r_.get('run'))) or {}).get('part_one_modules'),
                  low_p1=(rdr_.get(str(r_.get('run'))) or {}).get('low_part_one'), low_p2=(rdr_.get(str(r_.get('run'))) or {}).get('low_part_two'))
             for r_ in dr_rows_ if r_.get('kind') == 'dispatch' and r_.get('kernel') == 'SIDE-explicit-formula']
    # ### the lines of (4)-(7): the rulings tool's groups (N3_GROUPS), each its foot and its json -- the file and its bytes before and after,
    # ### the entered lines, the head, the E0 gate where the group reads one -- the files chained group to group, and group c2's roster
    lfoot_ = (r'\*\*THE LEDGERS, GROUP (C\d): OPEN_TRAILS APPENDED, NO LINE MOVING ; (\d+) LINES? UNDER ONE HEAD \((.+?)\) ;'
              r'(?: THE E0 GATE (\d+) OF (\d+) (?:DERIVES|READ) ;)? CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.\*\*')
    lg_ = []
    for g_ in N3_GROUPS:
        ft_ = _bfig('%s_ledgers_%s.txt' % (ACT, g_), lfoot_, 'group %s`s foot' % g_)
        j_ = jl('%s_ledgers_%s.json' % (ACT, g_))
        fi_ = (j_.get('file') or {}) if isinstance(j_, dict) else {}
        en_ = (j_.get('entered') or {}) if isinstance(j_, dict) else {}
        if ft_[0] != g_.upper() or not isinstance(j_, dict) or fi_.get('path') != 'OPEN_TRAILS.md' or not en_ or not j_.get('head') \
                or int(ft_[1]) != len(en_) + len(j_.get('entry_lines') or {}) or int(ft_[5]) != int(ft_[6]):   # ### b767: an order's entry line beside its text (c2's [S1], [R1])
            sys.exit('### data/%s_ledgers_%s.json DOES NOT CARRY ITS FOOT`S FILE, LINES, HEAD AND CONTROLS -- NOTHING COMPOSED' % (ACT, g_))
        lg_.append(dict(group=g_, lines=int(ft_[1]), heads=ft_[2].replace('`', '’'), e0=(int(ft_[3]), int(ft_[4])) if ft_[3] else None,
                        ctl=(int(ft_[5]), int(ft_[6])), file=fi_, entered=en_, head=j_.get('head'), date=j_.get('date')))
    if any(lg_[i_]['file'].get('sha_before') != lg_[i_ - 1]['file'].get('sha_after') for i_ in range(1, len(lg_))):
        sys.exit('### THE GROUPS` FILES DO NOT CHAIN, EACH GROUP`S BYTES BEFORE THE PREVIOUS GROUP`S AFTER -- NOTHING COMPOSED')
    ro_ = (jl('%s_ledgers_c2.json' % ACT) or {}).get('roster') or {}
    if not isinstance(ro_.get('before_open'), int) or not isinstance(ro_.get('after_open'), int):
        sys.exit('### data/%s_ledgers_c2.json DOES NOT CARRY THE ROSTER BEFORE AND AFTER -- NOTHING COMPOSED' % ACT)
    od_ = _bfig('%s_orders.txt' % ACT, r'(?m)^### ### \*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', 'the roster at HEAD')
    rp_ = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ; (\d+) s\.\*\*', 'the reproduction run`s foot')
    rpj_ = jl('%s_reproduce.json' % ACT)
    rp_notruns_ = [r_.get('id') for r_ in (rpj_ or {}).get('rows') or [] if r_.get('grade') == 'NOT RUN']
    b7c_ = jl('b766_scores_close.json') or {}
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS (\d+) OF (\d+) '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                corr_postseal=_bfig('%s_corrigendum.txt' % ACT, r'\*\*ITEMS \d+: EVENTS \d+, POST-SEAL (\d+), DEFECTS \d+ ;', 'the corrigendum`s post-seal count')[0],
                corr_findings=((co.get('findings') or {}).get('claim'), (co.get('findings') or {}).get('close'), (co.get('findings') or {}).get('repeat')),
                # ### b767, Component 4 (the Edit tool): the figures of (1) to (13) over b767's banks, read in record 4
                pr_rows=prow_, pr_step0=prf_[0], pr_lower=prf_[1], pr_ceiling=int(prf_[2]), pr_carried=None, pr_upper=prf_[3], pr_last=prf_[12],
                pr_minutes=(prj_.get('closure_min'), prj_.get('whole_min')), pr_disp=(int(prf_[4]), int(prf_[5])), pr_cap=int(prf_[6]),
                pr_on=(int(prf_[7]), int(prf_[8])), pr_oncap=int(prf_[9]), pr_lean=(int(prf_[10]), int(prf_[11])), pr_reserve=prj_.get('reserve_h'),
                ce_at=ce_[0], ce_spent=ce_[1], ce_last=ce_[2], ce_last_h=ce_[3], ce_left=ce_[4], ce_ceiling=int(ce_[5]), ce_reserve=int(ce_[6]),
                ce_b766=ce_[7], ce_close=ce_[8], ce_word=ce_[9],
                reps=reps_, rep_states=dict((s_, [r_['key'] for r_ in reps_ if r_['state'] == s_]) for s_ in ('REPAIRED', 'READ AS DESIGNED', 'REMOVED', 'CARRIED')),
                srep=srep_, st_entering=K.STANDING_VERSION_ENTERING, st_version=K.STANDING_VERSION,
                cc_ctl=(int(cc_[0]), int(cc_[1])),
                # ### (4), (5)(c): the dispatch tool's foot and its lines, the tool's backticks read as apostrophes (its words otherwise as banked)
                tr_disp=(int(tr_[0]), int(tr_[1])), tr_on=(int(tr_[2]), int(tr_[3])), tr_trial=tr_[4], tr_pair=tr_[5], tr_main=tr_[6], tr_ctl=(int(tr_[7]), int(tr_[8])),
                tr_trial_line=trt_[0].replace('`', '’'), tr_pair_line=trp_[0].replace('`', '’'), tr_main_line=trm_[0].replace('`', '’'),
                tr_last=trl_[0], tr_last_hour=trl_[1],
                # ### (4)(a): the certificate's three forms by its foot and its FORMS lines, the plan's eleven parts and its commit
                cert_ctl=(int(cf_[0]), int(cf_[1])), cert_widths=(int(cf_[2]), int(cf_[3]), int(cf_[4]), int(cf_[5])),
                cert_forms=[(k_, w_.strip(), int(n_), s_, int(nd_), int(wd_)) for k_, w_, n_, s_, nd_, wd_ in cfm_],
                plan_lemmas=list(pl_), plan_commit=plc_,
                # ### (5)(a), (b): the source-build read
                sb_ctl=(int(sbf_[0]), int(sbf_[1])), sb_route=(sbr_[0], sbr_[1]), sb_part1=(int(sbp_[0]), int(sbp_[1])),
                # ### (6): the window at graded knots
                win_reading=wv_[0], win_key=wv_[1], win_hours=wv_[2], win_reg=wv_[3], win_upper=wv_[4], win_knots=int(wc_[0]), win_ncoef=int(wc_[1]),
                win_S=wc_[3], win_rad=wc_[4], win_products=int(wr_[1]), win_primes=int(wr_[2]), win_constants=int(wr_[3]), win_sumr=wr_[4],
                win_digits=int(wr_[5]), win_uniform=wu_[0], win_control=wk_[0], win_json=(int(wj_[0]), wj_[1]),
                # ### (4)(c), (4)(d): the data files of L10a and L11b
                ld_ctl=(int(ldc_[0]), int(ldc_[1])), ld_keys=int(ldt_[0]), ld_upto=ldt_[1], ld_most=int(ldt_[2]), ld_sum=int(ldt_[3]),
                ld_blocks=ldw_[0], ld_widest=ldw_[1], nd_ctl=(int(ndc_[0]), int(ndc_[1])), nd_lists=int(ndt_[0]), nd_upto=ndt_[1], nd_pairs=int(ndt_[2]),
                nd_most=int(ndt_[3]),
                runs=runs_, disp_ef=len(runs_), read_ef=sum(1 for r_ in dr_rows_ if r_.get('kind') == 'read' and r_.get('kernel') == 'SIDE-explicit-formula'),
                disp_m24=sum(1 for r_ in dr_rows_ if r_.get('kind') == 'dispatch' and r_.get('kernel') == 'SIDE-dirichlet-mod-24'),
                # ### (4)-(7): the groups, their entered keys in the order of their lines, their files, the roster and the controls
                led_groups=lg_, led_entered=dict((k_, v_) for x_ in lg_ for k_, v_ in x_['entered'].items()),
                led_keys=[k_ for x_ in lg_ for k_ in sorted(x_['entered'], key=lambda k2_, e_=x_['entered']: e_[k2_][0])],
                led_files=[(x_['file'].get('path'), x_['file'].get('lines_before'), x_['file'].get('lines_after'), x_['file'].get('first_new'),
                            x_['file'].get('sha_before'), x_['file'].get('sha_after')) for x_ in lg_],
                led_roster=(ro_.get('before_open'), ro_.get('after_open'), list(ro_.get('added') or []), list(ro_.get('moved') or [])),
                led_ctl=[x_['ctl'] for x_ in lg_],
                ord_head=(int(od_[0]), int(od_[1]), int(od_[2])),
                close_word='at its weight' if rdn('b766_closing.txt', optional=True) and b7c_ else 'carried',
                b7_held=sum(1 for v_ in b7c_.values() if (v_ or [''])[0] == 'HELD'), b7_refuted=[k_ for k_, v_ in sorted(b7c_.items()) if (v_ or [''])[0] != 'HELD'],
                disp=len(runs_),
                rp_rows=int(rp_[0]), rp_repro=int(rp_[1]), rp_differs=int(rp_[2]), rp_notrun=int(rp_[3]), rp_ctl=(int(rp_[4]), int(rp_[5])), rp_secs=int(rp_[6]),
                rp_notruns=rp_notruns_,
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4], addr_ctl=(int(ad[5]), int(ad[6])),
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R377), data/b767_ferry.txt :122: "no lean process runs on this host; each build is a runner dispatch read by its run id from the
    artifact, the exit file governing; the dispatches of SIDE-explicit-formula number at most 40 and are those of (4) and (5); nothing is
    fetched from the web by the seat; each record route and dispatch under the holds." Read (b759's form, b767's items): no seat command
    running lean or lake; each dispatch row with one read row of its run, the read's exit read; the dispatch counts within the worklist's
    caps, MAX_DISPATCHES (40) in SIDE-explicit-formula and 0 in SIDE-dirichlet-mod-24, the worklist's EF_RUNS and M24_RUNS each the runs of
    its kernel's dispatch and read rows; the dispatch rows' items those of tools/b767_controls.py's ITEMS for (4) and (5) -- the trial with
    the restore on and the steps of (4)(b) to (4)(e) (trial-on, b, c, d, e), at most 36 by MAX_DISPATCHES_KINDS, and with the restore off
    the trial (trial-off) and the closing build once each and a repeat of each at most, no planted build ((R377)(4), (9)); each dispatch
    under the memory hold (free_mb at or above 2,560 MB) and the disk hold (each volume at or above 5,000 MB) as its row banks them, each
    read row carrying free_mb; each dispatch row naming its licence: step zero's banks at the ferry's line, the line its item's clause
    (:19-:22 the steps, :25 the cap for a repeat, :26 main and the tag for the closing build, :31 the trial) and its needle on it; the
    dispatch commands in the capture as many as the dispatch rows and the sends refused; no suite part in the background.
    From the command bank (the seat's commands, read live from the capture by the `commands` route), the dispatch rows beside the
    worklist's runs, and the hook's refusal bank (a suite part sent in the background refused BACKGROUND)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    per_ = []
    for kn_, runs_w_, cap_ in (('SIDE-explicit-formula', K.EF_RUNS, K.MAX_DISPATCHES), ('SIDE-dirichlet-mod-24', K.M24_RUNS, K.MAX_DISPATCHES_M24)):
        d_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'dispatch') if r.get('kernel') == kn_)
        r_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read') if r.get('kernel') == kn_)
        per_.append((kn_, len(d_), cap_, d_ == r_ == sorted(str(x) for x in runs_w_)))
    runs_ = all(o_ for _k, _n, _c, o_ in per_) and all(n_ <= c_ for _k, n_, c_, _o in per_)
    twice_ = sorted(set(x for x in reads_ if reads_.count(x) > 1))
    dk_ = lambda r: r.get('disk_mb') if r.get('disk_mb') is not None else r.get('disk_mb_at_row')
    dmin_ = lambda r: min(dk_(r).values()) if isinstance(dk_(r), dict) and dk_(r) else (dk_(r) if isinstance(dk_(r), int) else -1)
    free_ = [r.get('n') for r in _ef_kind(rows_, 'dispatch') if not isinstance(r.get('free_mb'), int) or r['free_mb'] < 2560 or dmin_(r) < 5000] \
        + [r.get('n') for r in _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    exits_ = ['%s %s exit %s %s' % (r.get('kernel', '')[5:], r.get('run'), r.get('build_exit'), r.get('verdict')) for r in _ef_kind(rows_, 'read')]
    unexit_ = [r.get('run') for r in _ef_kind(rows_, 'read') if str(r.get('build_exit') if r.get('build_exit') is not None else '') == '']
    bg_ = [l for l in rdn('%s_hook_refusals.txt' % ACT).split(NL) if '| BACKGROUND |' in l]
    bgc_ = [r['n'] for r in ((cm.get('rows') or []) if cm else []) if r.get('bg') and re.search(r'fold\.py"? checks\b|_checks\.py', r.get('cmd') or '')]
    refused_ = _ef_kind(rows_, 'dispatch_refused')
    # ### b767, Component 4 (the Edit tool): a licence is step zero's banks (K.STEPZERO_BANKS, f6225683) at the ferry's line, the line its
    # ### item's clause (tools/b767_controls.py ITEMS: :19 (b), :20 (c), :21 (d), :22 (e), :25 the cap for a repeat, :26 main and the tag
    # ### for the closing build, :31 the trial) and its needle standing on it
    fl_ = rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL)
    wlic_ = (K.STEPZERO_BANKS[:8],)
    licd_ = lambda r: r.get('licence') if isinstance(r.get('licence'), dict) else {'commit': r.get('licence') or ''}
    lic_ = [r for r in _ef_kind(rows_, 'dispatch')
            if not (licd_(r).get('bank') == 'data/%s_ferry.txt' % ACT and str(licd_(r).get('commit') or '').startswith(K.STEPZERO_BANKS[:8])
                    and licd_(r).get('line') in (19, 20, 21, 22, 25, 26, 31) and bool(licd_(r).get('needle'))
                    and str(licd_(r).get('needle')) in (fl_ + [''] * 40)[int(licd_(r).get('line')) - 1])]
    its_ = [r.get('item') for r in _ef_kind(rows_, 'dispatch') if r.get('kernel') == 'SIDE-explicit-formula']   # ### b767: (4)'s and (5)'s items (tools/b767_controls.py ITEMS)
    off_ = ('trial-off', 'closing', 'repeat')   # ### (R377)(4), (9): the trial from source, the closing build and a repeat of each, the restore off
    on_ = ('trial-on', 'b', 'c', 'd', 'e')   # ### the trial with the restore on and the steps of (4)(b)-(e), at most 36 ((R377)(4))
    non_ = sum(1 for x_ in its_ if x_ in on_)
    kd_ = dict(K.MAX_DISPATCHES_KINDS)
    rs_ok_ = all(r.get('restore') == ('off' if r.get('item') in off_ else 'on') for r in _ef_kind(rows_, 'dispatch') if r.get('kernel') == 'SIDE-explicit-formula')
    items_ok_ = set(its_) <= set(off_ + on_) and all(its_.count(x_) <= 1 for x_ in ('trial-on', 'trial-off', 'closing')) \
        and its_.count('repeat') <= kd_['repeat'] and non_ <= kd_['restore'] and rs_ok_
    ok = bool(cm) and not seat_lean and len(disp or []) == len(_ef_kind(rows_, 'dispatch')) + len(refused_) and runs_ and not twice_ \
        and not free_ and not unexit_ and not lic_ and not bg_ and not bgc_ and items_ok_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b767_commands.json): %s; dispatch commands in the capture: %s, against the dispatch rows %d and the sends refused by the host (no run) %d; by kernel, dispatches against the worklist`s cap ((R377)(4)`s 40, N1) and the worklist`s runs each a dispatch row`s and a read row`s: %s; the items of SIDE-explicit-formula`s dispatches: %s; those of (4) and (5), the trial and the steps with the restore on %d of at most %d, and with the restore off the trial and the closing build once each and a repeat of each at most: %s; reads %d, a run read twice: %s; each read`s exit file: %s; a read with no exit read: %s; dispatch rows under the memory hold 2,560 MB or the disk hold 5,000 MB, or a row without free_mb: %s; dispatch rows not naming their licence (step zero`s banks %s at a line of (4) in the ferry, its needle on that line): %s (relay data/b767_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(_ef_kind(rows_, 'dispatch')), len(refused_),
            ', '.join('%s %d of %d, the runs %s' % (k_, n_, c_, o_) for k_, n_, c_, o_ in per_),
            ', '.join(r.get('item') + ' (restore ' + str(r.get('restore')) + ')' for r in _ef_kind(rows_, 'dispatch') if r.get('kernel') == 'SIDE-explicit-formula') or 'none',
            non_, dict(K.MAX_DISPATCHES_KINDS)['restore'], items_ok_,
            len(reads_), ', '.join(twice_) or 'none', '; '.join(exits_),
            unexit_ or 'NONE', free_ or 'NONE', ' or '.join(wlic_), len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b767's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line).
# ### The ceiling's (data/b767_ceiling.txt :3 before :13), the outcomes' (:3 before :19), the IMP2-TAU reading's (:6 before :14), each
# ### pre-send bank's (its controls before its salt check) and the ledgers' banks print their controls before their figures; the dispatch
# ### tool's and v1.37.2's controls stand in banks of their own, read by time against the opening dispatch and the first kernel commit. The
# ### author-rulings, orders and corrigendum banks carry no controls section (the rulings copy the ferry, the roster reads, the corrigendum
# ### screens at its landing): each is read by its foot at N3; the reproduction run's planted controls stand per row
# ### b767, Component 5 (the Edit tool): b767's banks that print their controls under a heading before their figures, each heading read from
# ### the bank (scratch facts766t.py, read-only, 19:01:45Z): the scan and the path refusal (standing), the dispatch tool's bank (:3 before
# ### :31), the ceiling after (4)(c) (:3 before :9) and the rulings tool's four groups (c2 :7 before :23, c3 :7 before :23, c4 :7 before
# ### :21, c5 :7 before :25). The certificate, the seven data files and the three readings print their controls after their figures, each
# ### read by its foot at N3 and by G-DERIVATION-GRADED; b766's window, premise-position and single ledgers banks have no b767 counterpart
# ### b767, Component 4 (the Edit tool): b767's banks with their headings read (Grep, 19:4xZ): the rulings tool's groups c2 (:7 before
# ### :24) and c5 (:7 before :34), the dispatch tool's bank by its writer (tools/b767_controls.py :1458-:1463), the ceiling bank written
# ### before the lock in b766's form; a group c6 joins where [C7] or [C8] is entered, by the Edit that gives the rulings tool that group
N2_CONTROLS = (('data/b767_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b767_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b767_controls.txt', '## THE CONTROLS', '## SIDE-explicit-formula: '),
               ('data/b767_ceiling.txt', '## THE CONTROLS', '## THE ROWS DONE, BY NAME'),
               ('data/b767_ledgers_c2.txt', '## THE CONTROLS', '## THE ROSTER BY tools/standing/orders.py'),
               ('data/b767_ledgers_c5.txt', '## THE CONTROLS', '## THE E0 GATE'))
# ### the repairs' planted controls stand per key in data/b767_repair_controls.txt, read by N2's standing clause below (each read at the
# ### commit before its repair and at the repair's commit); the dispatch tool's controls in their own bank, read by time against the opening
# ### dispatch
N2_USES = ()
N2_GENS_N = 10   # ### b767: K.GENS nine (the repairs' planted controls, the certificate, the source-build read, the window at graded knots, the groups c2 and c5, the prime table of L10, the factor runs of L11b, and the dispatch tool's bank, which joins GENS at its commit) and K.GENS_WITH_BANK one (the dispatch tool's controls, which rode once with its tool's repair)
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
N2_SECTIONS = ()
N2_RIDERS = ('data/b767_steps.json', 'data/b767_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


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


def _cmd_epoch(ts):
    """b761: a command bank's time (2026-11-18T22:08:01.234Z) as an epoch, to the second; None where unread."""
    import calendar
    try:
        return calendar.timegm(time.strptime(ts[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R377), data/b767_ferry.txt :122: "the step-zero reads, the chain read and the carry print before any write, a scratch file among
    the writes; each tool this act writes commits before its run in any form; tools/standing/ at the close differs from tools/standing/ at
    b766's close by the commit of (8) and by no other, VERSION moved by it; the amended plan of (4)(a) is committed before any dispatch and
    the registration of (6) before the tool's run at graded knots; the kernel's main moves under (4) and at no other time." Read: the chain
    read, the step-zero reads and the carry by the step-zero bank's times, in that order, before the act_current commit; the act's commits
    in the worklist's TIME_ORDER by time, relay and PLACE-papers together; tools/standing/ moved by the commit of K.STANDING_REPAIRS alone
    ([K25]), VERSION at it that row's version and at HEAD K.STANDING_VERSION, moved from b766's close; the repairs bank's one row in one of
    the four states, its control AS WANTED in its bank at its row's commit; each tool of K.GENS first added by a commit of its own carrying
    it and not its bank, its commits before the bank's, the bank's commit not the tool; each act tool committed before its first run, read
    from the command bank; the certificate's banks and the plan in one commit (the certificate's row of K.GENS) before the first dispatch's
    time, and the registration's commit (K.REG_COMMIT) carrying it alone before tools/b767_window.py's first run; SIDE-explicit-formula's
    main the closing Lean commit with v0.45 at it where a build from source read exit 0 with its axioms file equal to the restored read's,
    the dispatch tool's line MAIN MOVES TO the closing commit, and the entering main with no tag otherwise; no kernel branch removed
    (KERNEL_DELETES, KERNEL_REMOVED and KERNEL_DELETES_REFUSED none); the standing commit admitting b767 ([K25]) before the kernel's first
    commit; each tool's controls before its figures; the (W) regeneration, the pre-lock comparison and the probe-path refusal before the
    lock gate."""
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
    # ### b762's step-zero bank: the chain read at :6 ("THE CHAIN READ the first route after the delivery (09:41:43Z)"), the reads at
    # ### :7-:8 ("THE STEP-ZERO READS: restart key none; ... (system 26,830 MB, data 615,846 MB at 09:41:43Z)"), the carry at :11
    # ### (09:42:33Z); the first match of each, the later chain reads after summaries standing below them; the reads' time the first after
    # ### their head, b761's form ("... 2,560 MB (21:32:16Z)") not b762's
    szt_ = [(n_, re.search(p_, sz_, re.S)) for n_, p_ in (('the chain read', r'THE CHAIN READ[^(\n]*\((\d\d:\d\d:\d[\dx])Z'),
                                                          ('the step-zero reads', r'THE STEP-ZERO READS: .*?(\d\d:\d\d:\d\d)Z'),
                                                          ('the carry', r'THE CARRY before any (?:other )?write of the relay: .*?(\d\d:\d\d:\d\d)Z'))]
    sze_ = [(n_, _hms_epoch(m_.group(1).replace('x', '0')) if m_ else None) for n_, m_ in szt_]
    stepzero_ = all(e_ for _n, e_ in sze_) and [e_ for _n, e_ in sze_] == sorted(e_ for _n, e_ in sze_) and sze_[-1][1] < tm_[0]
    # ### b764: tools/standing/ moved by the commits of K.STANDING_REPAIRS alone, in their order ((5)'s eighteen and (7)'s one), its tree
    # ### at HEAD the last one's, VERSION at each commit that row's version, moved from b763's close; each control AS WANTED in its bank at
    # ### its row's commit
    st_commits_ = [h_ for h_ in g(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()]
    st_last_ = K.STANDING_REPAIRS[-1][2]
    st_tree_ = (g(ROOT, 'rev-parse', 'HEAD:tools/standing').strip(), g(ROOT, 'rev-parse', '%s:tools/standing' % st_last_).strip())
    st_ver_ = (g(ROOT, 'show', 'HEAD:tools/standing/VERSION') or '').strip()
    st_ver0_ = (g(ROOT, 'show', '%s:tools/standing/VERSION' % K.PRE_RELAY) or '').strip()
    st_each_ = [(k_, (g(ROOT, 'show', '%s:tools/standing/VERSION' % c_) or '').strip() == v_
                 and ((g(ROOT, 'show', '%s:%s' % (r_, K.REPAIR_CONTROLS_BANK)) or '').replace(chr(13), '').split(NL) + [''] * (l_ + 1))[l_ - 1].startswith(
                     '### ### **%s THE CONTROL AS WANTED: ' % k_)) for k_, v_, c_, r_, l_ in K.STANDING_REPAIRS]
    standing_ = [h_[:8] for h_ in st_commits_] == [c_[:8] for _k, _v, c_, _r, _l in K.STANDING_REPAIRS] and bool(st_tree_[0]) and st_tree_[0] == st_tree_[1] \
        and st_ver_ == K.STANDING_VERSION and bool(st_ver0_) and st_ver0_ == K.STANDING_VERSION_ENTERING and st_ver0_ != st_ver_ and all(o_ for _k, o_ in st_each_)
    # ### each tool before its bank (K.GENS); each tool of K.GENS_WITH_BANK first added before its bank, the bank beside it at the commit
    # ### the worklist names and standing at the bank's commit
    gens_ok_ = []
    for n_, tool_, gens_, data_, bank_ in K.GENS:
        fa_ = _first_add(tool_)
        gens_ok_.append((n_, bool(fa_) and fa_ == g(ROOT, 'rev-parse', gens_[0]).strip() and all(tool_ in files_(h_) and data_ not in files_(h_) for h_ in gens_)
                         and data_ in files_(bank_) and tool_ not in files_(bank_) and max(ct_(ROOT, h_) for h_ in gens_) < ct_(ROOT, bank_)))
    for n_, tool_, data_, c_, k_ in K.GENS_WITH_BANK:
        ft_, fd_ = _first_add(tool_), _first_add(data_)
        gens_ok_.append((n_, bool(ft_) and bool(fd_) and ct_(ROOT, ft_) < ct_(ROOT, fd_) and tool_ in files_(c_) and data_ in files_(c_)
                         and data_ in files_(k_) and ct_(ROOT, c_) <= ct_(ROOT, k_)))
    gen_ = len(gens_ok_) == len(K.GENS) + len(K.GENS_WITH_BANK) == N2_GENS_N and all(o_ for _n, o_ in gens_ok_)   # ### b764: the generator rows of the worklist, N2_GENS_N
    # ### each act tool committed before it runs ((N2)'s third clause, as written, a dry run among the runs, defect (h)): each seat command
    # ### running a tools/<act>_*.py of K.GENS (a program argument, not a one-line program, not the one-call tool's add), its time against
    # ### the tool's first commit; read from the command bank. The Edits between a commit and a run are not read by this arm
    cmr_ = ((jl('%s_commands.json' % ACT) or {}).get('rows') or [])
    tools_ = sorted(set([t_ for _n, t_, _g, _d, _b in K.GENS] + [t_ for _n, t_, _d, _c, _k in K.GENS_WITH_BANK]))
    runs_ = []
    for t_ in tools_:
        fa_ = _first_add(t_)
        rx_ = re.compile(r'(?:^|[\s"])(?:D:/relay/)?%s(?=["\s]|$)' % re.escape(t_))
        hits_ = [r_ for r_ in cmr_ if r_.get('src') == 'seat' and 'python' in (r_.get('cmd') or '') and 'commit.py' not in (r_.get('cmd') or '')
                 and ' -c ' not in (r_.get('cmd') or '') and rx_.search(r_.get('cmd') or '')]
        es_ = [e_ for e_ in (_cmd_epoch(r_.get('ts') or '') for r_ in hits_) if e_]
        first_ = min(es_) if es_ else None
        runs_.append((t_, fa_[:8] if fa_ else 'NONE', ct_(ROOT, fa_) if fa_ else 0, first_, bool(fa_) and bool(first_) and ct_(ROOT, fa_) <= first_))
    runs_ok_ = bool(cmr_) and len(runs_) == len(tools_) and all(o_ for *_x, o_ in runs_)
    # ### b766, (R376)(4), N2: the kernel's main moved under (4) and at no other time -- where a read of the closing Lean commit with the
    # ### restore off (the closing item or its repeat) exits 0 and KERNEL with its axioms file equal by sha256 to the restored read's at the
    # ### same commit, main the closing commit and v0.45 the one tag at it; otherwise the entering main and no tag (b766: the pair stopped,
    # ### the dispatch tool's verdict MAIN NOT MOVED, NO TAG CUT, no [C7] by the author's word at :32); push-b765-planted removed by [K22]'s
    # ### routes (KERNEL_DELETES and KERNEL_REMOVED that name, KERNEL_DELETES_REFUSED none); ORDER_TAGS empty
    drw_ = jl('%s_dispatch_rows.json' % ACT) or []
    rd_ = _ef_kind(drw_, 'read')
    on_sha_ = set(str(r_.get('axioms_sha256') or '') for r_ in rd_ if (r_.get('built_ref') or '')[:8] == K.RUNNER_COMMIT[:8] and r_.get('restore_input') == 'on'
                  and r_.get('verdict') == 'KERNEL' and str(r_.get('build_exit')) == '0')
    built_ = set((r_.get('built_ref') or '')[:8] for r_ in rd_ if r_.get('verdict') == 'KERNEL' and str(r_.get('build_exit')) == '0'
                 and r_.get('item') in ('closing', 'repeat') and r_.get('restore_input') == 'off' and str(r_.get('axioms_sha256') or '') in on_sha_)
    tv_ = (re.search(r'(?m)^  MAIN AND THE TAG: (.+)$', rdn('%s_controls.txt' % ACT, optional=True) or '') or re.search('(x)?', '')).group(1)
    efm_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/main').strip()
    tags_at_ = sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--points-at', K.RUNNER_COMMIT).split() if t_.strip())
    moved_ = K.RUNNER_COMMIT[:8] in built_
    # ### b767, Component 4 (the Edit tool, found carried with b766's meaning while the record sections were read for their constants):
    # ### (R377)(4), (12), N2 -- main moved under (4) alone, its line in the dispatch tool's words (MAIN MOVES TO <commit> ..., where b766's
    # ### predicate read 'MAIN MOVED' and no b767 line begins so); no kernel branch removed, where b766's predicate wanted [K22]'s one name
    # ### (KERNEL_DELETES == (K.PLANTED_BRANCH[0],), a tuple of one empty name at b767 against b767's empty KERNEL_DELETES)
    before_kw_ = K.KERNEL_DELETES == () == K.KERNEL_REMOVED and not K.KERNEL_DELETES_REFUSED and not K.ORDER_TAGS and (
        (efm_ == K.EF_MAIN == K.RUNNER_COMMIT and bool(K.WEIL_TAG) and K.WEIL_TAG[2] == K.RUNNER_COMMIT and tags_at_ == [K.WEIL_TAG[0]]
         and str(tv_ or '').startswith('MAIN MOVES TO %s ' % K.RUNNER_COMMIT[:8])) if moved_ else
        (efm_ == K.EF_MAIN == K.EF_BASE and K.WEIL_TAG is None and not tags_at_ and str(tv_ or '').startswith('MAIN NOT MOVED')))
    # ### the standing commit that admits b767 at SIDE-explicit-formula ([K25], v1.38.25) before the kernel's first commit
    anc_ = 0 < ct_(ROOT, K.STANDING_REPAIRS[0][2]) < ct_(K.EF_DIR, K.KERNEL_COMMITS[0][2])
    # ### (R377) N2: "the amended plan of (4)(a) is committed before any dispatch and the registration of (6) before the tool's run at graded
    # ### knots" -- the certificate's two banks and the plan in one relay commit, the certificate's row of K.GENS (b766's typed f4a7744b not
    # ### carried), each bank's last commit, its time before the first dispatch row's; the registration's commit carrying it alone, its time
    # ### before tools/b767_window.py's first run as the command bank reads it (runs_ above)
    plan_c_ = [b_ for _n, _t, _g, d_, b_ in K.GENS if d_ == 'data/b767_certificate.txt'][0]
    pc_files_ = files_(plan_c_)
    d0_ = min((_cmd_epoch(r_.get('at') or '') or 0) for r_ in _ef_kind(drw_, 'dispatch')) if _ef_kind(drw_, 'dispatch') else 0
    plan_first_ = all(p_ in pc_files_ for p_ in ('data/b767_certificate.json', 'data/b767_certificate.txt', 'data/b767_plan.txt')) \
        and all(g(ROOT, 'log', '-1', '--format=%h', '--abbrev=8', '--', p_).strip()[:8] == plan_c_[:8] for p_ in ('data/b767_certificate.json', 'data/b767_plan.txt')) \
        and 0 < ct_(ROOT, plan_c_) < d0_
    wrun_ = [r_ for t_, _f, _c, r_, _o in runs_ if t_ == 'tools/b767_window.py']
    reg_first_ = bool(K.REG_COMMIT) and [x for x in g(ROOT, 'show', '--name-only', '--format=', K.REG_COMMIT).split() if x.strip()] == ['data/b767_registration.txt'] \
        and bool(wrun_) and bool(wrun_[0]) and 0 < ct_(ROOT, K.REG_COMMIT) < wrun_[0]
    # ### b767: the repairs bank's one row ([K25]) in one of the four states
    rst_ = re.findall(r'; STATE: (REPAIRED|READ AS DESIGNED|REMOVED|CARRIED)\b', ' '.join(l_.strip() for l_ in rdn('%s_repairs.txt' % ACT).replace(chr(13), '').split(NL)))
    states_ok_ = len(rst_) == len(K.STANDING_REPAIRS) == 1
    sect_ = stepzero_ and standing_ and gen_ and before_kw_ and runs_ok_ and states_ok_ and plan_first_ and reg_first_
    route_ = sect_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT, optional=True)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the chain read, the step-zero reads and the carry printed before any write, in that order (%s, each by the step-zero bank, before the act_current commit %s): %s; tools/standing/ moved by the %d commit of (8) alone, the last %s, its tree at HEAD that commit`s (trees %s and %s), the act`s commits under it %s, VERSION %s against %s, moved from %s, each commit`s VERSION its row`s and each control AS WANTED at its row`s commit (%s): %s; SIDE-explicit-formula`s main %s, the dispatch tool`s verdict on main and the tag %s, the closing commit %s, its builds from source read exit 0 with the restored read`s axioms file %s, tags at the closing commit %s, kernel branches removed at the remote and from the clone %d: %s; the standing commit admitting b767 ([K25]) before the kernel`s first commit: %s; the repairs bank`s rows by state (%d of 1 read, %s): %s; the certificate`s banks and the plan in %s before the first dispatch, the registration alone at %s before the window tool`s first run: %s; each tool first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the tool (%s): %s; each act tool committed before its first run, a dry run of its controls among its runs (tool, its first commit and time, its first run read from the command bank): %s: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; the act`s %d commits in the worklist`s order by time, relay and PLACE-papers together: %s (%s); the tools` controls before their figures: %s' % (
            ', '.join('%s %s' % (n_, ('%sZ' % m_.group(1)) if m_ else 'unread') for n_, m_ in szt_), K.ACT_CURRENT_COMMIT, stepzero_,
            len(K.STANDING_REPAIRS), st_last_[:8], st_tree_[0][:12] or 'NONE', st_tree_[1][:12] or 'NONE', ' '.join(h_[:8] for h_ in st_commits_) or 'none', st_ver_ or 'unread',
            K.STANDING_VERSION, st_ver0_ or 'unread', ', '.join('%s %s' % x_ for x_ in st_each_), standing_,
            efm_[:8] or 'NONE', tv_ or 'unread', K.RUNNER_COMMIT[:8], ' '.join(sorted(built_)) or 'none', ' '.join(tags_at_) or 'none', len(K.KERNEL_REMOVED), before_kw_, anc_,
            len(rst_), ', '.join('%s %d' % (s_, rst_.count(s_)) for s_ in ('REPAIRED', 'READ AS DESIGNED', 'REMOVED', 'CARRIED')), states_ok_,
            plan_c_[:8], (K.REG_COMMIT or '-')[:8], plan_first_ and reg_first_,
            ', '.join('%s %s' % x_ for x_ in gens_ok_), gen_,
            ', '.join('%s %s@%d first run %s %s' % (t_, f_, c_, time.strftime('%H:%M:%SZ', time.gmtime(r_)) if r_ else 'unread', o_) for t_, f_, c_, r_, o_ in runs_) if cmr_ else 'the command bank unread', runs_ok_,
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(), '**THE PROBE-PATH REFUSAL : CLEAR' in fg_,
            len(chain_), order_, ' '.join('%s %s@%d' % (k_, h_[:8], c_) for k_, (_r, h_), c_ in zip([k_ for k_ in okeys_ if k_ in keyed_], chain_, tm_)),
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
# ### b760: (R370)'s N3 reads five clauses -- (a) the edition equal to v2.4.0's bytes with BLOCK W's keys applied and BLOCK V appended, its
# ### fields filled from the banks; (b) the Epstein document differing from its bytes at d711a5d6 by BLOCK X's five keys alone; (c) each
# ### sentence of (6) to (9) entered in a ledger equal to the ruling's text with its fields filled; (d) no sentence of zeta, RH, GRH or Weil
# ### positivity on classK for zeta holding, failing or moving; (e) the side named under (R368)(9). (R369)'s catalogue clause stands in no
# ### clause of (R370): printed with its yield and graded by none. The act's own sentences are its banks', the entry's and its PLACE-papers
# ### writes' (the edition's lines that v2.4.0 does not carry, the Epstein document's changed lines, the four ledgers' appended texts), each
# ### matcher over all three; the edition's diff bank, which prints v2.4.0's sentences beside the edition's, read through the PLACE-papers
# ### units and not as a bank of the act's own sentences; the places and rules banks the ruling's and the author's words, read by neither.
# ### The graded feet: each bank closing on a `### ### **` line
# ### b761: (R371)'s N3 reads five clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at
# ### 91b69bf1 but THE_METHOD_CANON.md, its bytes there a prefix of its new bytes; (b) REGISTRY, OPEN_TRAILS and FINDINGS each a byte
# ### prefix of its new bytes; (c) [A1] to [A3], [B1] and [B2] as entered equal to the ruling's texts with their fields filled; (d) after (8)
# ### the two orders CLOSED and no other order's status moved by those two lines; (e) no sentence of zeta, RH, GRH or Weil positivity on
# ### classK for zeta holding, failing or moving. (R368)(9)'s side rule and (R369)'s catalogue clause stand in no clause of (R371): printed
# ### with their yields and graded by none. The act's own sentences are its banks', the entry's and its PLACE-papers writes' (the three
# ### ledgers' appended texts and the cells' block), each matcher over all three, the quoted spans dropped; the author-rulings bank (the
# ### author's words and the ruling's texts) and the orders bank (the roster's lines of OPEN_TRAILS, quoted) read by neither
# ### b762: (R372)'s N3 reads seven clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at
# ### da82a9d5, the new file of (6) alone added; (b) REGISTRY, OPEN_TRAILS and FINDINGS each a byte prefix of its new bytes; (c) the page
# ### equal to BLOCK P with its one field filled; (d) each text of the ruling as entered equal to the ruling's text with its fields filled;
# ### (e) after (7) the roster as WANTED; (f) the registration committed alone and before the map's tool; (g) no sentence of the act beyond
# ### the page's own text saying anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved. (R368)(9)'s side
# ### rule and (R369)'s catalogue clause stand in no clause of (R372): printed with their yields and graded by none. The act's own
# ### sentences are its banks', the entry's and its PLACE-papers writes' beyond the page (the trail lines' appended text and [G1] and [G2]),
# ### each matcher over all three, the quoted spans dropped; the author-rulings bank (the author's word and the navigator's rendering), the
# ### registration ([H], the ruling's text, read by its digest at (d)) and the orders bank (the roster's lines of OPEN_TRAILS, quoted) read
# ### by neither. The orders bank's foot stands at its :236, not its last line, so it is graded at G-COUNT-ROUTE-PRICED and not here
# ### b763: (R373)'s N3 reads eleven clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at
# ### 87cab4f2 but the canon, by an appended section; (b) REGISTRY not written; (c) OPEN_TRAILS and FINDINGS each a byte prefix of its new
# ### bytes; (d) each text of the ruling as entered equal to its text with its fields filled; (e) each sentence of (6) and (7) as entered
# ### equal to the ruling's with its fields filled from a run; (f) (7)'s statement committed and compiled before a line of its proof; (g) the
# ### file that carries its proof passing the control that no zero is used; (h) after (9) the roster as WANTED; (i) no sentence of the act
# ### beyond the canon's section saying anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; (j) no
# ### sentence about the control speaking of positivity without naming the side; (k) no figure of the navigator's workspace printed as a
# ### banked figure. (R369)'s catalogue clause and the novelty matcher stand in no clause of (R373): printed with their yields, graded by
# ### none. The act's own sentences are its banks', the entry's and its PLACE-papers writes' (OPEN_TRAILS' appended text and the canon's
# ### section), the quoted spans dropped; the canon's section, the ruling's [C1] entered verbatim, is read by (i)'s words by no centre
# ### matcher, and by the side matcher with its hits pinned by hand where they are the ruling's own text; the author-rulings bank (the
# ### author's word and the navigator's renderings) and the orders bank (the roster's lines, quoted) read by neither
# ### b764: (R374)'s N3 reads eight clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at
# ### 7db9a66c; (b) REGISTRY not written; (c) OPEN_TRAILS, FINDINGS and ERRATA each a byte prefix of their new bytes; (d) each text of the
# ### ruling as entered equal to the ruling's text with its fields filled; (e) [P1] and [G1] each committed alone, [G1] before the tool's
# ### run; (f) no sentence of the act saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; (g)
# ### no sentence about the control speaking of positivity without naming the side; (h) no figure of the navigator's workspace printed as a
# ### banked figure, the figures of (9)(c) and of [P1] standing as the navigator's and so named. No paper is edited, so no section is set
# ### apart from (f); the roster is read beside, graded by no clause; (R369)'s catalogue clause and the novelty matcher printed with their
# ### yields, graded by none. The act's own sentences are its banks', the entry's and its PLACE-papers writes' (the three ledgers' appended
# ### text), the quoted spans dropped; the registration and the predictions bank (the ruling's texts, read at (d) by their bytes), the
# ### author's word's bank and the orders bank (the roster's lines, quoted) read by none of the matchers
# ### b765: (R375)'s N3 reads eight clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at
# ### 1198a637; (b) REGISTRY and ERRATA not written; (c) OPEN_TRAILS and FINDINGS each a byte prefix of its new bytes; (d) each text of the
# ### ruling as entered equal to the ruling's text with its fields filled; (e) no sentence of the act saying that anything of zeta, RH, GRH or
# ### Weil positivity on classK for zeta holds, fails or moved; (f) no sentence about the control speaking of positivity without naming the
# ### side; (g) the statement of (5)(a) entered as a definition and nowhere as a result; (h) no figure of the navigator's workspace printed as
# ### a banked figure. No paper is edited, so no section is set apart from (e); the roster read beside, graded by no clause; (R369)'s
# ### catalogue clause and the novelty matcher printed with their yields, graded by none. The texts of (d): [C5] as the dispatch tool's
# ### reading and the author's word on the save on main give it, [S1], [S2], [W1], [Q1], [M3], [B2], [H4] (the author's word of Route A), [T1],
# ### [T2] and [T3] (its clause on W-ORD-H2-PI1 the word's), each a line of OPEN_TRAILS by the ledgers tool's digest; [G2] the registration's
# ### bytes; [R1] a line of the act's trail, the account written <account>. The graded feet: each bank closing on a `### ### **` line, its words
# ### fixed where the bank stands written and the run's figures left free; the window, the gate, the held branches and the map's pair, whose
# ### banks close on a sentence, are read by their own arms
# ### b767, Component 4 (the Edit tool): (R377)'s N3 reads eight clauses -- (a) no file under day1/, phase1.5/, phase2/ or internal/
# ### differing from its bytes at 29de0836; (b) REGISTRY, ERRATA, the census and the two files of the map not written; (c) OPEN_TRAILS and
# ### FINDINGS each a byte prefix of its new bytes; (d) each text of the ruling as entered equal to the ruling's text with its fields
# ### filled; (e) no sentence of the act saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved;
# ### (f) no sentence about the control speaking of positivity without naming the side; (g) a theorem of a step entered as its own
# ### statement and nowhere as the closing theorem; (h) no figure of the navigator's workspace printed as a banked figure. No paper is
# ### edited; the roster read beside, graded by no clause; (R369)'s catalogue clause and the novelty matcher printed with their yields,
# ### graded by none. The texts of (d): the rulings tool's groups, [S1] and [R1] each with its order's entry line, [G1] and [A2]; [P2] and
# ### [S2]; [C7] or [C8] where entered; each a line of OPEN_TRAILS by the group's digest, and [P1], [S3], [G2] and [G3] entered nowhere.
# ### The graded feet: each bank closing on a `### ### **` line, its words fixed where the bank stands written and the run's figures left
# ### free; the registration, the window, the plan and the two data files of L10a and L11b close on no such line and are read by the arms
# ### of checks 34 (feet767.py, read-only, 19:51:17Z)
N3_GRADED = (('b767_corrigendum.txt', ('ITEMS 169', 'NO WEIGHT LINE', 'FINDINGS :16080')),
             ('b767_price.txt', ('THE PRICE TABLE: STEP ZERO', 'THE UPPER SUM', 'THE LAST STEP DISPATCH BY 22:34:03Z')),
             ('b767_ceiling.txt', ('THE CEILING READ BEFORE THE LOCK', 'THE RESERVE 16 h')),
             ('b767_repair_controls.txt', ('THE CONTROL AS WANTED: THE FAULT READ BEFORE AND CLEAN AFTER: True.',)),
             ('b767_certificate.txt', ('THE THREE FORMS READ: ', 'CONTROLS AS WANTED', 'THE PRIMES` ONE WIDTH')),
             ('b767_source_build.txt', ('THE READ MADE: ', 'CONTROLS AS WANTED', 'THE ROUTE STATED.')),
             ('b767_controls_control.txt', ('THE TOOL`S CONTROLS: ', 'ALL AS WANTED')),
             ('b767_controls.txt', ('DISPATCHES ', ' ; THE TRIAL ', ' ; THE PAIR ', ' ; MAIN AND THE TAG: ', 'THE TOOL`S CONTROLS ')),
             ('b767_ledgers_c2.txt', ('THE LEDGERS, GROUP C2: OPEN_TRAILS APPENDED, NO LINE MOVING', 'CONTROLS ', 'WRITTEN.')),
             ('b767_ledgers_c5.txt', ('THE LEDGERS, GROUP C5: OPEN_TRAILS APPENDED, NO LINE MOVING', 'CONTROLS ', 'WRITTEN.'))) \
    + ((('b767_ledgers_c6.txt', ('THE LEDGERS, GROUP C6: OPEN_TRAILS APPENDED, NO LINE MOVING', 'CONTROLS ', 'WRITTEN.')),)
       if os.path.exists(os.path.join(D, 'b767_ledgers_c6.txt')) else ()) \
    + (('b767_reproduce.txt', ('ROWS ', 'PLANTED CONTROLS AS WANTED ')),
       ('b767_citation_check.txt', ('### ### **THE CHECK ', '** (halts ')), ('b767_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### N3 (R367): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word; the centre
# ### matcher over the clause's own words, "anything of zeta, RH, GRH or Weil positivity on classK for zeta" (data/b757_ferry.txt :51): zeta
# ### (the symbol, Riemann's, or a zeta function not the Epstein's), RH, GRH and Weil positivity on classK -- b756's bare `classK` not carried,
# ### the clause naming classK only inside Weil positivity for zeta, and (R367)(7)'s outcome a test function in classK at the control; the
# ### side matcher over (R367)'s "no sentence about the control speaks of positivity without naming the side"
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
# ### b759: "Weil positivity on classK" read as the clause's "for zeta" unless its sentence places it at the control -- (5)'s ruled sentence
# ### opens "Weil positivity on classK fails at the control on the arithmetic side of its explicit formula", a statement about the Epstein
# ### function, and N3's side clause asks that very sentence to name its side; one control of each kind in record 20 (the planted zeta
# ### sentence caught, (5)'s sentence passed)
N3_LOC = (r'(?:\b(?:RH|GRH)\b|ζ|\bRiemann(?:`s|\'s)? zeta\b|(?<!Epstein )\bzeta function\b|\bWeil positivity on classK\b(?![^.;]*\bat the control\b)).*'
          r'\b(?:holds|hold|fails|fail|proved|refuted|moved)\b')
# ### b759, N3's last clause: "no sentence says the mechanism catalogue has or has not met the zero" -- a negation does not pass it
N3_CAT = r'\bcatalogue\b[^.;]*\b(?:has|have|had)(?: not)? met\b'
N3_SIDE = r'\bpositivity\b'
N3_BANKS = ('stepzero', 'misses', 'corrigendum', 'price', 'ceiling', 'repairs', 'repair_controls', 'certificate', 'plan', 'source_build',
            'registration', 'window', 'controls_control', 'controls', 'logdata', 'natdata', 'ledgers_c2', 'ledgers_c5', 'reproduce', 'events',
            'defects')   # ### b767, Component 4 (the Edit tool): the act's own banks in place of b766's carried names
N3_BANKS_OPTIONAL = ('ledgers_c6',)   # ### b767: written only where the closing pair enters [C7] or [C8]
# ### N3 (h), (R374): no figure of the navigator's workspace printed as a banked figure, the figures of (9)(c) and of [P1] standing as the
# ### navigator's and so named -- the workspace figures of (9)(c) (data/b764_ferry.txt :33: the form -7.775, its prime-power side 659.93,
# ### its archimedean term 652.15, k(0) 129.18, -7.491189 and 0.259399 at b709's rows, -3.36 at the step function) and of [P1] (:125-:137:
# ### 0.93 at height 16.2902, t* 0.1018, room- 0.0271, the births' ten-digit heights and turning values, 14.7040 and 0.0876 at -24), each
# ### to the digits the ruling prints, the mirror export's MANIFEST md5 the navigator read (SCOPE READ, :3, "opening 4db5bf2c"); [G1]'s
# ### Gaussian control (-2.5251491414, F = -0.1100564101) is computed by this act's tool and banked as its own (data/b764_imp2tau.txt) and
# ### is not one. In the act's own sentences and the entry's, each occurrence wants the navigator named in its sentence
# ### b765, N3 (h), (R375): the figures of the navigator's workspace are [G2] PART TWO's WHAT THE NAVIGATOR HAD SEEN (data/b765_ferry.txt
# ### :50): +6.75 at M = 4, -3.78 at M = 8, -6.70 at M = 16; at M = 8 rounded -3.36 and +0.27; at the kernel's window -7.7753, its prime side
# ### 659.925 and its archimedean term 652.150 -- each to the digits the ruling prints, the signed ones with their sign; the act's banked
# ### figures (data/b765_window.txt, data/b765_gauss_gate.txt) carry more digits and differ in them, so none is read as one
N3_NAV_FIGS_B765 = r'(?<![\d.])(?:\+6\.75|-3\.78|-6\.70|-3\.36|\+0\.27|-7\.7753|659\.925|652\.150?)(?![\d])'   # ### b765's, kept beside
# ### b766, N3 (h), (R376): the figures of the navigator's workspace are (5)(b)'s candidate (data/b766_ferry.txt :27: 1,990 declarations,
# ### 152 named by a paper's table, 870 on the two generated pages alone, 968 by neither; [X2]'s "152, 870 and 968 of 1,990") and (1)'s
# ### sums of b765's step rows printed as the navigator's (:11: 3.89 hours, 2.48, 13.15) -- each in the form the ruling prints it; the bare
# ### 152 and 52 not read, each standing in the act's own counts (this act's 152 names at dispatch 13, step 52), the candidate's 152 read
# ### beside its 870; (5)(a)'s "52 by the navigator's count" names the navigator in its own words and is read by G-COUNT's figures
N3_NAV_FIGS_B766 = r'(?<![\d.,])(?:1,990|3\.89|2\.48|13\.15)(?![\d])|\b152,? (?:named by a paper|870)\b|\b870 on the two generated pages\b|\b968 by neither\b'   # ### b766's, kept beside
# ### b767, Component 4 (the Edit tool, found carried with b766's figures while the record sections were read for their constants): N3 (h),
# ### (R377): the figures of the navigator's workspace are (1)'s readings of b766's closing table printed as the navigator's
# ### (data/b767_ferry.txt :11: "of 21.43 hours of step rows, 8.61 stand under Component 3 and 12.82 under ...; the prompt on the two stops
# ### was put 11.02 hours after the opening row and the closing came 13.70 hours after that prompt") -- each in the form the ruling prints
# ### it; the bare 8.61 not read, standing in the act's own reading of b766's step rows (data/b767_price.txt :9, :26), and read only in the
# ### navigator's form; claim (viii)'s bare 48 not read, the kernel's main holding it compiled and the act's own counts carrying the number
N3_NAV_FIGS = r'(?<![\d.,])(?:21\.43|12\.82|11\.02|13\.70)(?![\d])|\b8\.61 stand under Component 3\b'
# ### b762, N3 (a) to (f): the trees the act may not change but for the page of (6), added; the three files that take appended bytes alone;
# ### the page against BLOCK P; each of the ruling's texts by the file it is entered in -- the trail's twenty-two by the trail tool's digests
# ### (data/b762_ledgers.json entered, sha256 of the filled text, as tools/b762_rulings.py writes them), [G1] and [G2] in REGISTRY, [H] the
# ### registration's bytes, [W1] in the author-rulings bank; the roster as (7) wants it; the registration alone and before the map's tool
N3_TREES = ('day1', 'phase1.5', 'phase2', 'internal')
N3_CANON = None   # ### b764: no paper edited ((R374)(13)), so no section is set apart from the centre matcher
N3_PREFIXED = ('OPEN_TRAILS.md', 'FINDINGS.md')   # ### (R376) N3 (c); the five unwritten read apart at (b)
N3_UNWRITTEN = ('REGISTRY.md', 'ERRATA.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md')   # ### (R376) N3 (b), (11): the census v0.8.3 by its path (data/b766_readfirst.txt :48) and the map's two files, each tracked at HEAD and at 5638a9ad (scratch unw766.py, 19:05:30Z)
# ### b766, N3 (g): "a theorem of a step is entered as its own statement and nowhere as the closing theorem" -- a sentence naming the
# ### closing theorem (ControlFailureExists, the closing theorem, L12, [P1]) with a word of a result (proved, proven, compiled, holds,
# ### established, discharged, a proof of it given), outside a negation, the plan's prices and the not-sent carry passing by their negation
N3_DEF_SUBJ = r'\bControlFailureExists\b|\b(?i:the closing theorem)\b|\bL12\b|\[P1\]'   # ### b766 defect (u): the phrase in any case, the control's "The closing theorem compiled at 3c67b8b5." caught as its words say
N3_DEF_RES = r'\b(?:proved|proven|compiled|holds|established|DISCHARGED|discharged|is true)\b'
# ### a hit of the matchers over the act's PLACE-papers writes passes only by a hand verdict pinned here by (path, line, the sentence's
# ### digest (sha256, 16 hex)) -> the verdict, each read before the lock; the words not quoted. b764: none pinned until the scores dry
# ### reads the act's writes (b763's one pin, a line of the canon, not carried: no paper is edited at b764)
N3_HAND = {}
N3_CONTROL = r'\b(?:control|Epstein|zq_\w+)\b|x\^2 \+ xy \+ 6y\^2'   # ### a sentence about the control: the control named, the Epstein function, a zq_ name, the form
N3_SIDE_NAMED = r'\b(?:arithmetic|spectral|zero|prime-power) side\b'
import hashlib as _hs   # noqa: E402  ### the notes' digests, sha256 of each line (16 hex), as tools/b757_notes.py writes them; _hs, not _h, which record.tpl :2633 binds to its height formatter (defect (t))


def _side_bad(x):
    """N3 (R367): a sentence about the control that speaks of positivity and names no side of the explicit formula."""
    return bool(re.search(N3_SIDE, x, re.I) and re.search(N3_CONTROL, x) and not re.search(N3_SIDE_NAMED, x))


def _def_bad(x):
    """N3 (g), (R376): a sentence entering the closing theorem as compiled -- its subject and a result's word, outside a negation, the
    ruling's own outcome sentences of [P1] (read as the ruling's, "where the closing theorem compiles") passing by their condition."""
    # ### b766 defect (u): the condition word read in either case, so the control's "Where the closing theorem is proved, [P1] is
    # ### entered." passes as its own words say, and the subject's phrase in any case (N3_DEF_SUBJ), so its "The closing theorem compiled
    # ### at 3c67b8b5." is caught; at the score routes' dry of 23:37:03Z each read lower case alone and defn read False on both
    return bool(re.search(N3_DEF_SUBJ, x) and re.search(N3_DEF_RES, x) and not re.search(N3_NEG, x)
                and not re.search(r'\b(?:where|if|unless|until|whether)\b', x, re.I))


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
    # ### b767, Component 4 (the Edit tool): a prose line naming the navigator and carrying one of its figures read whole beside the rows --
    # ### the corrigendum's line of the navigator's figures (data/b767_corrigendum.txt :13) names the navigator at its head and parts the
    # ### figures by semicolons, where the cut at each read the later parts as figures unnamed (defect (w)'s case in a prose line); a line
    # ### naming the navigator with no figure of N3_NAV_FIGS stays in the sentences' flow, so no sentence wrapped over lines is parted
    ls_ = (t or '').replace(chr(13), '').split(NL)
    whole_ = lambda l_: not l_.startswith('### ') and (' | ' in l_ or bool(re.search(r'\bnavigator', l_) and re.search(N3_NAV_FIGS, l_)))
    rows_ = [l_.strip() for l_ in ls_ if whole_(l_)]
    return _own_sentences(NL.join(l_ for l_ in ls_ if not whole_(l_))) + rows_


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


_INTEG = {}
# ### the act's findings named by their banks, the names the entry's heading carries (_title), read as b761 read its own line
# ### (tools/b761_lines.py :106-:109: the heading '## ' and the names joined)
INTEG_NAMES = ('b767_corrigendum', 'b767_repairs', 'b767_certificate', 'b767_plan', 'b767_source_build', 'b767_registration', 'b767_window',
               'b767_controls', 'b767_dispatch_rows', 'b767_logdata', 'b767_natdata', 'b767_ledgers_c2', 'b767_ledgers_c5', 'b767_orders')   # ### b767, Component 4 (the Edit tool): the act's finding banks in place of b766's
INTEG_KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'   # ### (R377)(10): the keystone the ruling's line names
INTEG_TABLE_NAME = 'THE_EPSTEIN_CONTROL_OBJECT'                          # ### the cluster table's row naming the keystone, read against the ruling's cluster
INTEG_DEFAULT = None                                                     # ### b766: the ruling gives the line whole; no default
INTEG_FERRY_LINE = 47                                                    # ### b767, Component 4 (the Edit tool): data/b767_ferry.txt :47, (R377)(10): the line between its backticks (b766's :40, (R376)(9))


def _integ_line(f):
    """b767, (R377)(10): the entry's last line, bare, the ruling's own: `INTEGRATION: cluster The Epstein instance ; keystone
    phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md ; stage CLUSTERED`, read from the ferry's bank at :47 between its backticks and
    refused where it is not that one line of the canon's shape. Beside it, read and not used to compose: SPIRAL_MAP's cluster table at
    PLACE-papers HEAD (between its '### Clusters' and '### Cross-cluster bridges' heads), the one row whose cells name the keystone, its bold
    name against the ruling's cluster; the canon's form (THE_METHOD_CANON.md :351) as the line's shape. b764's composer (the cluster read
    from the table, the stage BANKED) stands below, not called. The reading kept in _INTEG for the record's N3 sentence."""
    if 'line' not in _INTEG:
        fl_ = (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * INTEG_FERRY_LINE)[INTEG_FERRY_LINE - 1]
        ms_ = re.findall(r'`(INTEGRATION: cluster ([^;`]+?) ; keystone ([^;`]+?) ; stage ([A-Z]+))`', fl_)
        if len(ms_) != 1 or ms_[0][2] != INTEG_KEYSTONE:
            sys.exit('### THE FERRY`S :%d DOES NOT CARRY ONE INTEGRATION LINE NAMING THE KEYSTONE -- NOTHING COMPOSED' % INTEG_FERRY_LINE)
        sm_ = g(PP, 'show', 'HEAD:SPIRAL_MAP.md').replace(chr(13), '').split(NL)
        a_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Clusters')), None)
        b_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Cross-cluster bridges')), None)
        rows_ = [(i_ + 1, re.match(r'^\| \*\*([^*]+)\*\*', sm_[i_])) for i_ in range(a_ or 0, b_ or 0) if INTEG_TABLE_NAME in sm_[i_]] if a_ is not None and b_ is not None else []
        rows_ = [(n_, m_.group(1).strip()) for n_, m_ in rows_ if m_]
        form_ = g(PP, 'show', 'HEAD:phase1.5/method/THE_METHOD_CANON.md').replace(chr(13), '').split(NL)
        form_ok_ = len(form_) > 351 and all(w_ in form_[350] for w_ in ('INTEGRATION: cluster <', ' ; keystone <', ' ; stage <'))
        _INTEG.update(line=ms_[0][0], cluster=ms_[0][1], cluster_line=rows_[0][0] if len(rows_) == 1 else None, stage=ms_[0][3], form=form_ok_,
                      table=[n_ for _l, n_ in rows_],
                      why='the ruling`s line (data/%s_ferry.txt :%d); SPIRAL_MAP`s cluster table`s rows naming %s: %d%s' % (
                          ACT, INTEG_FERRY_LINE, INTEG_TABLE_NAME, len(rows_), (', its cluster %s' % ('the ruling`s' if [n_ for _l, n_ in rows_] == [ms_[0][1]] else 'another'))
                          if rows_ else ''), names=list(INTEG_NAMES))
    if not _INTEG['form']:
        sys.exit('### THE CANON`S FORM AT :351 IS NOT THE INTEGRATION LINE`S -- NOTHING COMPOSED')
    return _INTEG['line']


def _integ_line_b766(f):
    """b764's composer, kept for the record and not called (b765, Component 5)."""
    if 'line' not in _INTEG:
        sm_ = g(PP, 'show', 'HEAD:SPIRAL_MAP.md').replace(chr(13), '').split(NL)
        a_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Clusters')), None)
        b_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Cross-cluster bridges')), None)
        if a_ is None or b_ is None or b_ <= a_:
            sys.exit('### SPIRAL_MAP AT HEAD CARRIES NO CLUSTER TABLE BETWEEN ITS TWO HEADS -- NOTHING COMPOSED')
        rows_ = [(i_ + 1, re.match(r'^\| \*\*([^*]+)\*\*', sm_[i_])) for i_ in range(a_, b_) if INTEG_TABLE_NAME in sm_[i_]]
        rows_ = [(n_, m_.group(1).strip()) for n_, m_ in rows_ if m_]
        if len(rows_) > 1:
            sys.exit('### SPIRAL_MAP`S CLUSTER TABLE: %d ROWS NAMING THE KEYSTONE, NOT ONE OR NONE -- NOTHING COMPOSED' % len(rows_))
        cl_ = rows_[0][1] if rows_ else INTEG_DEFAULT
        form_ = g(PP, 'show', 'HEAD:phase1.5/method/THE_METHOD_CANON.md').replace(chr(13), '').split(NL)
        form_ok_ = len(form_) > 351 and all(w_ in form_[350] for w_ in ('INTEGRATION: cluster <', ' ; keystone <', ' ; stage <'))   # ### the form held within :351 (read by predicate, 03:3xZ)
        st_ = 'BANKED'
        _INTEG.update(line='INTEGRATION: cluster %s ; keystone %s ; stage %s' % (cl_, INTEG_KEYSTONE, st_), cluster=cl_, cluster_line=rows_[0][0] if rows_ else None,
                      stage=st_, form=form_ok_, why='the table`s rows naming %s: %d, so the cluster %s; the stage the rule`s word' % (
                          INTEG_TABLE_NAME, len(rows_), 'its row`s' if rows_ else 'the rule`s default'), names=list(INTEG_NAMES))
    if not _INTEG['form']:
        sys.exit('### THE CANON`S FORM AT :351 IS NOT THE INTEGRATION LINE`S -- NOTHING COMPOSED')
    return _INTEG['line']


N3_KEYS = {}   # ### (carried name, unread at b759)


def _blob(ref, path):
    """a PLACE-papers file's bytes at a ref (b'' where the ref does not carry it)."""
    return subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (ref, path)], capture_output=True).stdout or b''


def _sha16(b_):
    return _hs.sha256(b_ if isinstance(b_, bytes) else b_.encode('utf-8')).hexdigest()[:16]


def _added_lines(old_b, new_b):
    """the lines of new_b that old_b does not carry, by difflib's opcodes over the two files' lines (CR removed): [(line in new, text)], and
    the old lines replaced or removed [line in old]."""
    import difflib
    a_ = old_b.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    b_ = new_b.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    add_, rem_ = [], []
    for op_, i1_, i2_, j1_, j2_ in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
        if op_ in ('replace', 'insert'):
            add_ += [(j_ + 1, b_[j_]) for j_ in range(j1_, j2_)]
        if op_ in ('replace', 'delete'):
            rem_ += [i_ + 1 for i_ in range(i1_, i2_)]
    return add_, rem_


def _trees_n3():
    """N3 (a) to (c), (R376): the files under day1/, phase1.5/, phase2/ and internal/ differing at PLACE-papers HEAD from the act's base
    (K.PRE_PP, 5638a9ad), none; REGISTRY's, ERRATA's, the census's and the map's two files' bytes at HEAD their bytes at the base (not
    written); OPEN_TRAILS and FINDINGS each a byte prefix of its bytes at HEAD. Returns (the files changed, all five unwritten, [(file, a
    prefix)], [(file, unwritten)])."""
    ch_ = [p_.strip() for p_ in g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD', '--', *N3_TREES).split(NL) if p_.strip()]
    un_ = [(p_, bool(_blob('HEAD', p_)) and _blob(K.PRE_PP, p_) == _blob('HEAD', p_)) for p_ in N3_UNWRITTEN]
    rg_ = len(un_) == len(N3_UNWRITTEN) == 5 and all(o_ for _p, o_ in un_)
    pre_ = []
    for p_ in N3_PREFIXED:
        b_, h_ = _blob(K.PRE_PP, p_), _blob('HEAD', p_)
        pre_.append((p_, bool(b_) and h_.startswith(b_) and len(h_) > len(b_)))
    return ch_, rg_, pre_, un_


def _alone_n3_b766():
    """b764's, kept for the record and not called at b765 ((R375)'s N3 has no clause of a commit made alone; [G2]'s is N2's).
    N3 (e), (R374): [P1] and [G1] each committed alone, [G1] before the tool's run -- the commit of [P1] (K.STEPZERO_PREDICTIONS) carrying
    data/b764_navigator_predictions.txt alone and the commit of [G1] (K.REG_COMMIT) data/b764_registration.txt alone, the riders set aside;
    [G1]'s commit before tools/b764_imp2tau.py's first run in the command bank and before the finite part's bank's commit; each bank's bytes
    at HEAD its bytes at its commit. Returns [(name, ok, the reading)]."""
    ct_ = lambda h_: int((g(ROOT, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0)
    files_ = lambda h_: sorted(x for x in g(ROOT, 'show', '--name-only', '--format=', h_).split() if x.strip() and x not in N2_RIDERS)
    rows_ = []
    for n_, c_, p_ in (('[P1]', K.STEPZERO_PREDICTIONS, 'data/%s_navigator_predictions.txt' % ACT), ('[G1]', K.REG_COMMIT, K.REG_BANK)):
        fs_ = files_(c_) if c_ else []
        same_ = bool(c_) and _blob_relay(c_, p_) == _blob_relay('HEAD', p_) and bool(_blob_relay('HEAD', p_))
        rows_.append((n_, fs_ == [p_] and same_, '%s %s, files %s, its bytes at HEAD its commit`s %s' % (n_, (c_ or 'NONE')[:8], fs_ or 'none', same_)))
    cmr_ = ((jl('%s_commands.json' % ACT) or {}).get('rows') or [])
    rx_ = re.compile(r'(?:^|[\s"/])tools/%s_imp2tau\.py(?=["\s]|$)' % ACT)
    es_ = [e_ for e_ in (_cmd_epoch(r_.get('ts') or '') for r_ in cmr_ if r_.get('src') == 'seat' and 'commit.py' not in (r_.get('cmd') or '')
                         and rx_.search(r_.get('cmd') or '')) if e_]
    ib_ = [h_ for n_, _t, _g, _d, h_ in K.GENS if _d == 'data/%s_imp2tau.txt' % ACT]
    first_ = min(es_) if es_ else None
    ok_ = bool(K.REG_COMMIT) and bool(first_) and bool(ib_) and ct_(K.REG_COMMIT) < first_ and ct_(K.REG_COMMIT) < ct_(ib_[0])
    rows_.append(('[G1] before the tool`s run', ok_, '[G1] at %s against the tool`s first run %s and the bank`s commit %s' % (
        time.strftime('%H:%M:%SZ', time.gmtime(ct_(K.REG_COMMIT))) if K.REG_COMMIT else 'NONE',
        time.strftime('%H:%M:%SZ', time.gmtime(first_)) if first_ else 'unread', (ib_ or ['NONE'])[0][:8])))
    return rows_


def _blob_relay(rev, path):
    """the bytes of a relay path at a revision, carriage returns set aside; b'' where absent."""
    try:
        return subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (rev, path)], capture_output=True).stdout.replace(b'\r', b'')
    except Exception:
        return b''


def _g1_composed(X_):
    """[G1] as the ruling's text with <DATE> the registration's own date and the author's word's (i) to (iii) of 2026-11-20 applied, each
    once, as scratch g1764.py composed it at Component 4 (data/b764_author_words_preseal.txt :6-:8); None where a part is not read."""
    reg_ = (rdn('%s_registration.txt' % ACT, optional=True) or '').replace(chr(13), '')
    dm_ = re.search(r'WRITTEN BEFORE ANY CELL IS COMPUTED \((\d{4}-\d\d-\d\d)\)', reg_)
    W_ = (rdn('%s_author_words_preseal.txt' % ACT, optional=True) or '').replace(chr(13), '').split(NL)
    # ### defect (l): the word is banked twice, its repeat at :15-:34 (events (53)); equal copies read once, unequal copies refuse
    q_ = lambda pre_, lead_: list(dict.fromkeys(l_[l_.index(lead_) + len(lead_):l_.rindex('"')] for l_ in W_ if l_.startswith(pre_)))
    r1_ = q_('(i) In [G1], THE GROUNDS reads: "', 'THE GROUNDS reads: "')
    r2_ = q_('(ii) In [G1], WHAT THE NAVIGATOR HAD SEEN gains this sentence at its end: "', 'gains this sentence at its end: "')
    r3_ = q_('(iii) In [G1], the closing sentence of HELD, from "b232\'s reading" to "the author\'s fetch", reads: "', 'to "the author\'s fetch", reads: "')
    t_ = X_.get('G1') or ''
    if not (dm_ and len(r1_) == len(r2_) == len(r3_) == 1 and t_):
        return None
    t_ = t_.replace('<DATE>', dm_.group(1))
    gl_ = [l_ for l_ in t_.split(NL) if l_.startswith('THE GROUNDS: ')]
    sl_ = [l_ for l_ in t_.split(NL) if l_.startswith('WHAT THE NAVIGATOR HAD SEEN: ')]
    m_ = re.search(r"b232's reading .*?the author's fetch", t_)
    if len(gl_) != 1 or len(sl_) != 1 or not m_:
        return None
    t_ = t_.replace(gl_[0], 'THE GROUNDS: ' + r1_[0], 1).replace(sl_[0], sl_[0] + ' ' + r2_[0], 1)
    return t_.replace(m_.group(0), r3_[0], 1)


def _ferry_texts():
    """the ruling's texts from the ferry's bank, each the lines between '---- [K] ...' and '---- end [K]' joined, as tools/b762_rulings.py
    reads them (its texts(), :128-:140: a key of a capital and any digits, [H] and [T10] to [T14] among them)."""
    L_ = rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL)
    out_ = {}
    for i_, l_ in enumerate(L_):
        m_ = re.match(r'^---- \[([A-Z]\d*)\] ', l_)
        if m_ and ('---- end [%s]' % m_.group(1)) in L_[i_:]:
            out_[m_.group(1)] = NL.join(L_[i_ + 1:L_.index('---- end [%s]' % m_.group(1), i_)])
    return out_


def _tpl_rx(t_, date_, swap=()):
    """a ruling's text as a pattern of itself with its fields filled: each <field> a group, <DATE> the date, every other byte as written;
    swap, (old words, new words) pairs applied to the text first, the author's word's replacements. Returns (the pattern, its fields in
    order, <DATE> apart)."""
    for a_, b_ in swap:
        t_ = t_.replace(a_, b_, 1)
    parts_ = re.split(r'(<[^<>\n]+>)', t_)
    fl_ = [p_ for p_ in parts_ if re.fullmatch(r'<[^<>\n]+>', p_) and p_ != '<DATE>']
    rx_ = ''.join(((re.escape(date_) if p_ == '<DATE>' else '(.+?)') if re.fullmatch(r'<[^<>\n]+>', p_) else re.escape(p_)) for p_ in parts_)
    return re.compile(rx_, re.S), fl_


N3_T3_OLD = "`W-ORD-H2-PI1` (:16563), the word given, the reading waiting on the author's choice of its source"   # ### [T3]'s clause the word replaces
N3_B2_OUTER = '<for each of the four, carried on main by <declaration> | still owed under <order>>'                 # ### [B2]'s nested field, read as one
N3_ACCT_RX = r'[A-Za-z0-9][A-Za-z0-9-]*/PLACE-project-set'                                                         # ### [R1]'s account, by its pattern (record 35's)


N3_GROUPS_B766 = ('c2', 'c3', 'c4', 'c5')   # ### b766: the rulings tool's four groups, each a json of its own (data/b766_ledgers_c2.json to _c5.json)
N3_NOT_ENTERED_B766 = ('E2', 'F3', 'P1', 'C7')   # ### (R376)'s texts entered at no outcome of b766
# ### b767, Component 4 (the Edit tool): the rulings tool's groups c2 and c5, and c6 where the closing pair enters [C7] or [C8]
# ### (tools/b767_rulings.py); the texts of (R377) entered at no outcome of this act: [P1] (the closing theorem not compiled), [S3] ([S2]
# ### entered), [G2] and [G3] ([G1] entered), and of [C7] and [C8] those c6 does not enter
N3_GROUPS = ('c2', 'c5') + (('c6',) if os.path.exists(os.path.join(ROOT, 'data', 'b767_ledgers_c6.json')) else ())
N3_NOT_ENTERED = ('P1', 'S3', 'G2', 'G3') + tuple(k_ for k_ in ('C7', 'C8') if not ('c6' in N3_GROUPS and k_ in ((jl('b767_ledgers_c6.json') or {}).get('entered') or {})))


def _pfx(a_, b_):
    """two commit names the same commit: one a prefix of the other, seven characters at least."""
    a_, b_ = str(a_ or ''), str(b_ or '')
    return min(len(a_), len(b_)) >= 7 and (a_.startswith(b_) or b_.startswith(a_))


def _texts_n3(f):
    """N3 (d), (R377): each text of the ruling as entered equal to the ruling's text with its fields filled -- the rulings tool's groups
    (data/b767_ledgers_c2.json, _c5.json, and _c6.json where written; each `entered` a key's line at HEAD and its digest, each group's
    date): [S1], [G1], [R1] and [A2]; [P2] and [S2]; [C7] or [C8] where entered; each line of OPEN_TRAILS at HEAD matching its template
    from the ferry's bank with each field a group, no field left unfilled, its sha256 the group's; the fields read where a bank gives them:
    [P2]'s, [C7]'s and [C8]'s commit the closing Lean commit, [S2]'s commit the act's opening Lean commit and its two runs the trial's by
    the dispatch rows, [G1]'s commit the registration's; group c2's two order entry lines at their lines and digests, each naming its
    order; and the texts entered at no outcome (N3_NOT_ENTERED) opening no line of the appended text. Returns [(key, file, ok, the
    reading)]. (b767, Component 4, the Edit tool; b766's form kept below as _texts_n3_b766c, not called.)"""
    X_ = _ferry_texts()
    otl_ = _blob('HEAD', 'OPEN_TRAILS.md').decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    gj_ = dict((g_, jl('%s_ledgers_%s.json' % (ACT, g_)) or {}) for g_ in N3_GROUPS)
    kc_ = [c_ for _k, _n, c_, _b in K.KERNEL_COMMITS]
    tr_ = dict((r_.get('item'), str(r_.get('run'))) for r_ in (json.loads(rdn('%s_dispatch_rows.json' % ACT)) or [])
               if r_.get('kind') == 'dispatch' and r_.get('item') in ('trial-on', 'trial-off'))
    rc_ = lambda v_: _pfx(v_, K.RUNNER_COMMIT)   # noqa: E731
    want_ = {'P2': {0: rc_}, 'C7': {0: rc_}, 'C8': {0: rc_}, 'G1': {0: lambda v_: _pfx(v_, K.REG_COMMIT)},
             'S2': {1: lambda v_: _pfx(v_, kc_[0] if kc_ else ''), 2: lambda v_: v_ == tr_.get('trial-off'), 4: lambda v_: v_ == tr_.get('trial-on')}}
    rows_ = []
    for g_ in N3_GROUPS:
        j_ = gj_[g_]
        en_ = j_.get('entered') or {}
        date_ = str(j_.get('date') or K.DATE)
        for k_ in sorted(en_, key=lambda x_: int((en_.get(x_) or [0])[0])):
            rx_, fl_ = _tpl_rx(X_.get(k_) or '', date_)
            ln_, sh_ = (en_.get(k_) or [0, ''])[:2]
            got_ = otl_[ln_ - 1] if 0 < ln_ <= len(otl_) else ''
            m_ = rx_.fullmatch(got_) if X_.get(k_) else None
            gs_ = list(m_.groups()) if m_ else []
            fok_ = all(i_ < len(gs_) and p_(gs_[i_]) for i_, p_ in (want_.get(k_) or {}).items())
            ok_ = bool(m_) and not re.search(r'<[a-z][^<>\n]*>', got_) and fok_ and _sha16(got_) == sh_
            rows_.append((k_, 'OPEN_TRAILS.md', ok_, ':%s, group %s, fields %d, %s' % (ln_, g_, len(fl_), 'the fields as their banks give them' if fok_ else 'A FIELD NOT AS ITS BANK GIVES IT')))
    for k_, o_ in (('S1', 'W-ORD-SOURCE-BUILD'), ('R1', 'W-ORD-NOVEMBER-RIDERS')):
        el_ = (gj_['c2'].get('entry_lines') or {}).get(k_) or [0, '']
        eg_ = otl_[int(el_[0]) - 1] if 0 < int(el_[0] or 0) <= len(otl_) else ''
        rows_.append(('%s entry line' % k_, 'OPEN_TRAILS.md', bool(eg_) and o_ in eg_ and _sha16(eg_) == el_[1], ':%s, the order`s entry line by its digest' % el_[0]))
    c2f_, lf_ = gj_['c2'].get('file') or {}, gj_[N3_GROUPS[-1]].get('file') or {}
    app_ = otl_[int(c2f_.get('first_new') or 1) - 1:int(lf_.get('lines_after') or 0)]
    opens_ = dict((k_, (X_.get(k_) or '').split('<')[0][:60]) for k_ in N3_NOT_ENTERED)
    found_ = [k_ for k_, o_ in opens_.items() if not o_ or any(l_.startswith(o_) for l_ in app_)]
    rows_.append(('the texts not entered', 'OPEN_TRAILS.md', not found_ and len(app_) > 0,
                  '%s opening none of the %d appended lines: %s' % (', '.join('[%s]' % k_ for k_ in N3_NOT_ENTERED), len(app_), found_ or 'NONE OPENING ONE')))
    return rows_


def _texts_n3_b766c(f):
    """b766's, kept for the record and not called at b767.
    N3 (d), (R376): each text of the ruling as entered equal to the ruling's text with its fields filled -- the rulings tool's four
    groups (data/b766_ledgers_c2.json to _c5.json, each `entered` a key's line at HEAD and its digest, each group's date): [E1], [M4], [Q2]
    for each of the eleven, [H5] and [A1]; [F1] and [F2]; [X1], [X2] and [X3]; [P2]; each line of OPEN_TRAILS at HEAD matching its template
    from the ferry's bank with each field a group, no field left unfilled, its sha256 the group's; the fields read where a bank gives them:
    [F1]'s commit the act's first kernel commit and [F2]'s its second, [P2]'s lemmas 12 (the plan's) and its commit the closing Lean
    commit, [Q2]'s orders the eleven group c2's roster moved; [M4]'s order entry line at its line and digest; and [E2], [F3], [P1] and [C7]
    opening no line of the appended text. Returns [(key, file, ok, the reading)]."""
    X_ = _ferry_texts()
    otl_ = _blob('HEAD', 'OPEN_TRAILS.md').decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    gj_ = dict((g_, jl('%s_ledgers_%s.json' % (ACT, g_)) or {}) for g_ in N3_GROUPS)
    kc_ = [c_ for _k, _n, c_, _b in K.KERNEL_COMMITS]
    moved_ = sorted(m_[0] for m_ in ((gj_['c2'].get('roster') or {}).get('moved') or []))
    want_ = {'F1': {1: lambda v_: _pfx(v_, kc_[0] if kc_ else '')}, 'F2': {0: lambda v_: _pfx(v_, kc_[1] if len(kc_) > 1 else '')},
             'P2': {0: lambda v_: v_ == '12', 1: lambda v_: _pfx(v_, K.RUNNER_COMMIT)}}
    rows_, q2o_ = [], []
    for g_ in N3_GROUPS:
        j_ = gj_[g_]
        date_ = str(j_.get('date') or K.DATE)
        for k_ in sorted(j_.get('entered') or {}, key=lambda x_: (x_.split('.')[0], int(x_.split('.')[1]) if '.' in x_ else 0)):
            tk_ = k_.split('.')[0]
            rx_, fl_ = _tpl_rx(X_.get(tk_) or '', date_)
            ln_, sh_ = (j_['entered'].get(k_) or [0, ''])[:2]
            got_ = otl_[ln_ - 1] if 0 < ln_ <= len(otl_) else ''
            m_ = rx_.fullmatch(got_) if X_.get(tk_) else None
            gs_ = list(m_.groups()) if m_ else []
            if tk_ == 'Q2' and gs_:
                q2o_.append(gs_[0])
            fok_ = all(i_ < len(gs_) and p_(gs_[i_]) for i_, p_ in (want_.get(tk_) or {}).items())
            ok_ = bool(m_) and not re.search(r'<[a-z][^<>\n]*>', got_) and fok_ and _sha16(got_) == sh_
            rows_.append((k_, 'OPEN_TRAILS.md', ok_, ':%s, group %s, fields %d, %s' % (ln_, g_, len(fl_), 'the fields as their banks give them' if fok_ else 'A FIELD NOT AS ITS BANK GIVES IT')))
    q2_ok_ = sorted(q2o_) == moved_ and len(moved_) == 11
    rows_ = [(k_, p_, o_ and (not k_.startswith('Q2') or q2_ok_), r_ + ('' if not k_.startswith('Q2') or q2_ok_ else ', THE ELEVEN NOT THE ROSTER`S MOVED'))
             for k_, p_, o_, r_ in rows_]
    el_ = gj_['c2'].get('entry_line') or [0, '']
    eg_ = otl_[el_[0] - 1] if 0 < int(el_[0] or 0) <= len(otl_) else ''
    rows_.append(('M4 entry line', 'OPEN_TRAILS.md', bool(eg_) and 'W-ORD-MAP-MERGE' in eg_ and _sha16(eg_) == el_[1], ':%s, the order`s entry line by its digest' % el_[0]))
    c2f_, c5f_ = gj_['c2'].get('file') or {}, gj_['c5'].get('file') or {}
    app_ = otl_[int(c2f_.get('first_new') or 1) - 1:int(c5f_.get('lines_after') or 0)]
    opens_ = dict((k_, (X_.get(k_) or '').split('<')[0][:60]) for k_ in N3_NOT_ENTERED)
    found_ = [k_ for k_, o_ in opens_.items() if not o_ or any(l_.startswith(o_) for l_ in app_)]
    rows_.append(('the texts not entered', 'OPEN_TRAILS.md', not found_ and len(app_) > 0,
                  '%s opening none of the %d appended lines: %s' % (', '.join('[%s]' % k_ for k_ in N3_NOT_ENTERED), len(app_), found_ or 'NONE OPENING ONE')))
    return rows_


def _texts_n3_b766b(f):
    """b765's, kept for the record and not called at b766.
    N3 (d), (R375): each text of the ruling as entered equal to the ruling's text with its fields filled. In OPEN_TRAILS, each a line at
    HEAD by the ledgers tool's line and digest (data/b765_ledgers.json entered), matching its template with each field a group: [C5] the
    ferry's with the clause of the word of 2026-11-21 on the runner's cache, (iv), at its end where the ledgers tool's runner key reads C5 (a
    save on main read) and the ferry's as written where it reads C5R (the second save stopped; the author's word on the save on main), its
    first commit the closing Lean commit and its third main's; [S1]; [S2], its name gaussArchQ's and its commit the closing commit; [W1];
    [Q1], its four counts the positions' foot's; [M3]; [B2], its nested field one group; [H4] the word of Route A's line, its reason "an
    address was not reached"; [T1]; [T2]; [T3], its clause on W-ORD-H2-PI1 the word's and its upstream field "present at its pin". [G2] the
    registration's bytes, the ferry's text with <DATE> the act's date. [R1] the act's trail's line, the ferry's text with the account written
    <account> and its fields filled, equal to the trail composer's (_r1_line); VACUOUS, and so named, while the trail is not yet written.
    Returns [(key, file, ok, the reading)]."""
    X_ = _ferry_texts()
    lj_ = jl('%s_ledgers.json' % ACT) or {}
    ej_ = lj_.get('entered') or {}
    date_ = str(lj_.get('date') or K.DATE)
    otl_ = _blob('HEAD', 'OPEN_TRAILS.md').decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    W_ = (rdn('%s_author_words_preseal.txt' % ACT, optional=True) or '').replace(chr(13), '').split(NL)
    q_ = lambda pre_: list(dict.fromkeys(l_[l_.index('"') + 1:l_.rindex('"')] for l_ in W_ if l_.startswith(pre_)))   # noqa: E731
    c5g_ = q_('(iv) [C5] gains at its end: "')
    t3c_ = q_('In [T3] of (R377), the clause on W-ORD-H2-PI1 reads: "')
    h4i_ = [i_ for i_, l_ in enumerate(W_) if l_.startswith('---- [H4] for OPEN_TRAILS')]
    rk_ = (lj_.get('runner') or {}).get('key')
    tp_ = dict((k_, X_.get(k_) or '') for k_ in ('C5', 'C6', 'S1', 'S2', 'S3', 'S4', 'W1', 'W2', 'Q1', 'M3', 'B2', 'T1', 'T2', 'T3'))
    form_ok_ = {'C5': (rk_ == 'C5' and len(c5g_) == 1) or rk_ == 'C5R', 'T3': len(t3c_) == 1 and N3_T3_OLD in tp_['T3'], 'H4': len(h4i_) == 1}
    if rk_ == 'C5' and len(c5g_) == 1 and tp_['C5'].endswith('.'):
        tp_['C5'] = tp_['C5'][:-1] + '; ' + c5g_[0] + '.'
    if form_ok_['T3']:
        tp_['T3'] = tp_['T3'].replace(N3_T3_OLD, t3c_[0], 1)
    tp_['H4'] = W_[h4i_[0] + 1] if form_ok_['H4'] else ''
    qc_ = [str(x_) for x_ in (f.get('q_counts') or ())[1:5]]
    want_ = {'C5': {0: K.RUNNER_COMMIT[:8], 2: (K.EF_MAIN or '')[:8]}, 'S2': {0: 'SIDEExplicitFormula.B321.GaussArchQSteps.gaussArchQ', 1: K.RUNNER_COMMIT[:8]},
             'Q1': dict(enumerate(qc_)) if len(qc_) == 4 else {0: 'UNREAD'}, 'H4': {0: 'an address was not reached'}, 'T3': {0: 'present at its pin'}}
    rows_ = []
    for k_ in f['led_keys']:
        rx_, fl_ = _tpl_rx(tp_.get(k_) or '', date_, ((N3_B2_OUTER, '<the four>'),) if k_ == 'B2' else ())
        ln_, sh_ = (ej_.get(k_) or [0, ''])[:2]
        got_ = otl_[ln_ - 1] if 0 < ln_ <= len(otl_) else ''
        m_ = rx_.fullmatch(got_) if tp_.get(k_) else None
        gs_ = list(m_.groups()) if m_ else []
        fok_ = all(i_ < len(gs_) and gs_[i_] == v_ for i_, v_ in (want_.get(k_) or {}).items())
        ok_ = bool(m_) and not re.search(r'<[a-z][^<>\n]*>', got_) and fok_ and _sha16(got_) == sh_ and form_ok_.get(k_, True)
        rows_.append((k_, 'OPEN_TRAILS.md', ok_, ':%s, fields %d, %s%s' % (ln_, len(fl_), 'the fields as their banks give them' if fok_ else 'A FIELD NOT AS ITS BANK GIVES IT',
                                                                       (', [C5] %s' % ('with the word`s (iv)' if rk_ == 'C5' else 'as the ruling gives it')) if k_ == 'C5' else '')))
    reg_ = (rdn('%s_registration.txt' % ACT, optional=True) or '').replace(chr(13), '')
    g2_ = (X_.get('G2') or '').replace('<DATE>', K.DATE, 1)
    rows_.append(('G2', K.REG_BANK, bool(X_.get('G2')) and reg_.rstrip(NL) == g2_, 'the registration the ruling`s [G2] with <DATE> %s: %s' % (K.DATE, reg_.rstrip(NL) == g2_)))
    t1_ = X_.get('R1') or ''
    a_ = re.search(N3_ACCT_RX, t1_)
    t1q_ = (t1_[:a_.start()] + 'QQACCTQQ' + t1_[a_.end() - len('/PLACE-project-set'):]) if a_ else ''
    rx1_, fl1_ = _tpl_rx(t1q_, date_)
    rx1_ = re.compile(rx1_.pattern.replace('QQACCTQQ', re.escape('<account>')), re.S)
    hits1_ = [(i_ + 1, l_) for i_, l_ in enumerate(otl_) if l_.startswith("THE PROJECT'S MIRROR REPOSITORY, built at b767")]
    trail_ = any(l_.startswith('### b767 — ') for l_ in otl_)
    if not trail_ and not hits1_:
        rows_.append(('R1', 'OPEN_TRAILS.md', True, 'VACUOUS: the act`s trail not yet written, [R1] entered in it at [15]'))
    else:
        c1_ = _r1_line()
        ok1_ = len(hits1_) == 1 and bool(rx1_.fullmatch(hits1_[0][1])) and c1_ is not None and hits1_[0][1] == c1_ \
            and not re.search(r'<(?!account>)[a-z][^<>\n]*>', hits1_[0][1]) and not re.search(N3_ACCT_RX, hits1_[0][1])
        rows_.append(('R1', 'OPEN_TRAILS.md', ok1_, 'lines %s, fields %d, the trail composer`s line %s' % ([n_ for n_, _l in hits1_] or 'none', len(fl1_), c1_ is not None and bool(hits1_) and hits1_[0][1] == c1_)))
    return rows_


def _texts_n3_b766(f):
    """b764's, kept for the record and not called at b765.
    N3 (d), (R374): each text of the ruling as entered equal to the ruling's text with its fields filled -- [E1] at ERRATA's end from the
    line the trail tool banked, [F1], [C1], the trial's line, [D1], [D2], [M1] (its closing sentence the author's word's (iv)), [L1] and
    [B1] each whole as the line of OPEN_TRAILS at HEAD the tool banked, by its digest (data/b764_ledgers.json entered), each matching the
    ruling's text with each field a group and <DATE> the ledgers' date, nothing else changed; the trial's fields those of data/b764_xlines.json
    and [M1]'s the finite part's cells and digits; [G1] the registration's bytes, the ruling's text with the word's (i) to (iii) applied;
    [P1] the predictions bank's bytes, verbatim. Returns [(key, file, ok, the reading)]."""
    X_ = _ferry_texts()
    lj_ = jl('%s_ledgers.json' % ACT) or {}
    ej_ = lj_.get('entered') or {}
    date_ = str(lj_.get('date') or K.DATE)
    otl_ = _blob('HEAD', 'OPEN_TRAILS.md').decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    erl_ = _blob('HEAD', 'ERRATA.md').decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    W_ = (rdn('%s_author_words_preseal.txt' % ACT, optional=True) or '').replace(chr(13), '').split(NL)
    w4_ = list(dict.fromkeys(l_[l_.index('reads: "') + 8:l_.rindex('"')] for l_ in W_ if l_.startswith('(iv) In [M1], the closing sentence reads: "')))   # ### defect (l)
    xf_ = dict((p_, str(v_)) for p_, v_ in ((f.get('xline') or {}).get('fields') or []))
    want_f_ = dict(M1={'<n>': str(f['it_cells']), '<d>': str(f['it_digits'])}, C2=xf_, C3=xf_)
    rows_ = []
    for k_ in ['E1'] + list(f['led_keys']):
        t_ = X_.get(k_) or ''
        sw_ = (("The source's appendix is read by the author's fetch.", w4_[0]),) if k_ == 'M1' and len(w4_) == 1 else ()
        rx_, fl_ = _tpl_rx(t_, date_, sw_)
        ln_, sh_ = (ej_.get(k_) or [0, ''])[:2]
        if k_ == 'E1':
            got_ = NL.join(erl_[ln_ - 1:]).strip() if ln_ else ''
            where_ = 'ERRATA.md'
        else:
            got_ = otl_[ln_ - 1] if 0 < ln_ <= len(otl_) else ''
            where_ = 'OPEN_TRAILS.md'
        m_ = rx_.fullmatch(got_)
        filled_ = dict(zip(fl_, m_.groups())) if m_ else {}
        fok_ = all(filled_.get(p_) == v_ for p_, v_ in (want_f_.get(k_) or {}).items())
        ok_ = bool(t_) and bool(m_) and not re.search(r'<[a-z][^<>\n]*>', got_) and fok_ and (k_ == 'E1' or _sha16(got_) == sh_) and (k_ != 'M1' or len(w4_) == 1)
        rows_.append((k_, where_, ok_, ':%s, fields %d, %s' % (ln_, len(fl_), 'the fields as their banks give them' if fok_ else 'A FIELD NOT AS ITS BANK GIVES IT')))
    g1_ = _g1_composed(X_)
    reg_ = (rdn('%s_registration.txt' % ACT, optional=True) or '').replace(chr(13), '')
    rows_.append(('G1', K.REG_BANK, bool(g1_) and reg_.rstrip(NL) == g1_, 'the registration the ruling`s [G1] with the word`s (i) to (iii) applied: %s' % (bool(g1_) and reg_.rstrip(NL) == g1_)))
    pr_ = (rdn('%s_navigator_predictions.txt' % ACT, optional=True) or '').replace(chr(13), '')
    rows_.append(('P1', 'data/%s_navigator_predictions.txt' % ACT, bool(X_.get('P1')) and pr_.rstrip(NL) == X_['P1'], 'verbatim: %s' % (pr_.rstrip(NL) == X_.get('P1'))))
    return rows_


def _orders_n3():
    """the roster read beside N3, graded by no clause of (R376): the rulings tool's roster in memory before and after group c2's write
    (data/b766_ledgers_c2.json roster; groups c3 to c5 move none) and tools/standing/orders.py's foot at HEAD after them
    (data/b766_orders.txt), its open count the roster's after. Returns (agree, the reading)."""
    ro_ = (jl('%s_ledgers_c2.json' % ACT) or {}).get('roster') or {}
    ft_ = re.search(r'(?m)^### ### \*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', rdn('%s_orders.txt' % ACT, optional=True) or '')
    ok_ = bool(ft_) and int(ft_.group(2)) == ro_.get('after_open')
    return ok_, 'open %s -> %s, added %s, moved %s ; the foot at HEAD %s' % (ro_.get('before_open'), ro_.get('after_open'), ro_.get('added') or 'none',
                                                                            ', '.join(str(m_[0]) for m_ in ro_.get('moved') or []) or 'none', ft_.group(0)[10:] if ft_ else 'UNREAD')


def _pp_units():
    """N3 (i) and (j) over the act's PLACE-papers writes: the appended text at HEAD of OPEN_TRAILS and of the canon (each from the trail
    json's first_new to lines_after), each line's quoted spans dropped as _own_sentences drops them, each line cut at . ; ? before a space,
    for the centre matcher (outside a negation; the canon's section left out by (i)'s own words, "beyond the canon's section"), the side
    matcher (a line a dated record heads left out, (R368)(9)) and the catalogue matcher (printed); a hit named by path, line and the
    sentence's digest, never by its words, passing only by a hand verdict of N3_HAND. Returns (units read, hits (place, digest, kinds,
    verdict or None), the catalogue's hits by place)."""
    lines_ = []
    # ### b766: the rulings tool's four groups, each its file's record under 'file' (b765's one json, b764's three under 'files')
    for x_ in [(jl('%s_ledgers_%s.json' % (ACT, g_)) or {}).get('file') for g_ in N3_GROUPS]:
        if not isinstance(x_, dict):
            continue
        hl_ = _blob('HEAD', x_['path']).decode('utf-8', 'replace').replace(chr(13), '').split(NL)
        lines_ += [(x_['path'], n_, hl_[n_ - 1]) for n_ in range(x_['first_new'], x_['lines_after'] + 1) if 0 < n_ <= len(hl_)]
    units_, hits_, cat_ = 0, [], []
    for p_, n_, l_ in lines_:
        dated_ = _dated_line(l_)
        for x_ in _own_sentences(l_):
            units_ += 1
            kinds_ = [k_ for k_, bad_ in (('centre', p_ != N3_CANON and bool(re.search(N3_LOC, x_)) and not re.search(N3_NEG, x_)),
                                          ('side', not dated_ and _side_bad(x_)), ('definition', _def_bad(x_))) if bad_]
            d_ = _sha16(x_)
            if re.search(N3_CAT, x_):
                cat_.append('%s :%s %s' % (p_, n_, d_))
            if kinds_:
                hits_.append(('%s :%s' % (p_, n_), d_, '+'.join(kinds_), N3_HAND.get((p_, n_, d_))))
    return units_, hits_, cat_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R377), data/b767_ferry.txt :122: "no file under day1/, phase1.5/, phase2/ or internal/ differs from its bytes at 29de0836;
    REGISTRY, ERRATA, the census and the two files of the map are not written; OPEN_TRAILS and FINDINGS are each a byte prefix of their new
    bytes; each text of this ruling as entered equals the ruling's text with its fields filled; no sentence of the act says that anything of
    zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; no sentence about the control speaks of positivity without
    naming the side; a theorem of a step is entered as its own statement and nowhere as the closing theorem; no figure of the navigator's
    workspace is printed as a banked figure." Read: (a) the files changed under the four trees, none; (b) REGISTRY's, ERRATA's, the
    census's and the map's two files' bytes at HEAD their bytes at the base; (c) OPEN_TRAILS and FINDINGS each a byte prefix; (d) the
    rulings tool's groups' texts in OPEN_TRAILS ([S1] with its order's entry line, [G1], [R1] with its order's entry line, [A2]; [P2] and
    [S2]; [C7] or [C8] where entered), each matching its template with its fields filled and by its group's line and digest, and the texts
    entered at no outcome of b767 opening no appended line; (e) the centre matcher over the act's own sentences -- its banks', the entry's
    and its PLACE-papers writes' -- a PLACE-papers hit passing by a pinned hand verdict alone; (f) the side matcher over the same; (g) the
    closing-theorem matcher over the same, a sentence entering ControlFailureExists, the closing theorem, L12 or [P1] as compiled outside a
    negation; (h) a figure of the navigator's workspace ((1)'s readings of b766's closing table) with no navigator named, each table row and
    each prose line naming the navigator with its figure read whole; each bank's foot carrying its grade; each matcher's control caught;
    the entry's last line (10)'s INTEGRATION line; the banks' nouns in the entry; the root prompt's sentences about the entry the
    composer's ((R377)(13), "composed from the banks"). The roster, the novelty and catalogue matchers printed with their yields and graded
    by no clause of (R377)."""
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
    # ### b767, Component 4 (the Edit tool): the rows and the controls set to (R377)(1)'s figures, b766's (1,990 and its candidate) read nowhere
    row_n_ = '  reserve navigator  AS THE NAVIGATOR READ IT: the close after the prompt; its hours | 13.70\n'
    row_x_ = '  reserve  THE HOURS: the close after the prompt; its hours | 13.70\n'
    line_n_ = 'the navigator’s figures, printed as the navigator’s: of 21.43 hours of step rows; the closing came 13.70 hours after that prompt.\n'
    line_x_ = 'the figures as read: of 21.43 hours of step rows; the closing came 13.70 hours after that prompt.\n'
    ctl3_ = dict(lit=bool(re.search(N3_LIT, 'The join is a new result.', re.I)), loc=bool(re.search(N3_LOC, 'RH holds at every height.')),
                 loc_k=bool(re.search(N3_LOC, 'Weil positivity on classK holds.')), loc_e=not re.search(N3_LOC, 'The Epstein zeta function holds no zero there.'),
                 # ### b759: (5)'s ruled sentence, its head as the ruling writes it, passed; the same words for zeta caught
                 loc_w=not re.search(N3_LOC, 'Weil positivity on classK fails at the control on the arithmetic side of its explicit formula, in the form h2_sign has for zeta.')
                 and bool(re.search(N3_LOC, 'Weil positivity on classK fails for zeta, in the form h2_sign has.')),
                 # ### b759: the catalogue clause, either way caught, a negation not passing it; a sentence of the order left open passed
                 cat=bool(re.search(N3_CAT, 'The mechanism catalogue has met the zero.')) and bool(re.search(N3_CAT, 'The catalogue has not met the zero.'))
                 and not re.search(N3_CAT, 'The order stays open on the author`s word, T0 and T1 entered beside it.'),
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
                 # ### b767, (h): (1)'s readings of b766's table caught where no navigator is named, passed where one is; the act's own 8.61
                 # ### of the price bank, the seat's 13.75 and a longer number passed; the navigator's form of 8.61 caught
                 nav=_nav_bad('The closing came 13.70 hours after that prompt.') and not _nav_bad('By the navigator`s reading the closing came 13.70 hours after that prompt.')
                 and not _nav_bad('Component 3 took 8.61 h at b766`s rate.') and _nav_bad('Of the step rows, 8.61 stand under Component 3.')
                 and _nav_bad('The prompt was put 11.02 hours after the opening row.') and not _nav_bad('The seat`s first Component 5 row took 13.75 h.')
                 and not _nav_bad('The run took 11.021 minutes.'),
                 nav_row=any(_nav_bad(x_) for x_ in _own_sentences(row_n_)) and not any(_nav_bad(x_) for x_ in _nav_units(row_n_))
                 and any(_nav_bad(x_) for x_ in _nav_units(row_x_)),
                 # ### b767: a prose line naming the navigator read whole, its later parts passed; the same line with no navigator caught
                 nav_line=any(_nav_bad(x_) for x_ in _own_sentences(line_n_)) and not any(_nav_bad(x_) for x_ in _nav_units(line_n_))
                 and any(_nav_bad(x_) for x_ in _nav_units(line_x_)),
                 # ### b766, (g): the closing theorem entered as compiled caught twice; the carry not sent, the ruling's conditional outcome and a
                 # ### step's own theorem passed
                 defn=_def_bad('ControlFailureExists is proved at 3c67b8b5.') and _def_bad('The closing theorem compiled at 3c67b8b5.')
                 and not _def_bad('L12, the closing theorem, was not sent.')
                 and not _def_bad('Where the closing theorem is proved, [P1] is entered.')
                 and not _def_bad('archTermQ_windowK_k0 compiled at 3c67b8b5, a theorem of L9.'))
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    side_ = [x[:80] for x in sents + nsides_ if _side_bad(x)]   # ### (R368)(9): the banks' sentences with the dated records' lines left out; (R373) N3 (j), graded
    cat_ = [x[:80] for x in sents + nsents_ if re.search(N3_CAT, x)]   # ### (R369)'s catalogue clause: printed, graded by no clause of (R373)
    # ### (a) to (c) the trees, REGISTRY and ERRATA unwritten, the prefixed files; (d) the ruling's texts; (e), (f), (g) the matchers over the
    # ### act's own sentences and the PLACE-papers writes; (h) the navigator; the roster beside, graded by none
    tr_ch_, reg_ok_, tr_pre_, tr_un_ = _trees_n3()
    trees_ok_ = tr_ch_ == []
    pre_ok_ = len(tr_pre_) == 2 and all(o_ for _p, o_ in tr_pre_)
    tx_rows_ = _texts_n3(f)
    ord_ok_, ord_read_ = _orders_n3()
    ppn_, pph_, ppcat_ = _pp_units()
    ppbad_ = [h_ for h_ in pph_ if not h_[3] and 'centre' in h_[2]]
    ppside_ = [h_ for h_ in pph_ if not h_[3] and 'side' in h_[2]]
    ppdef_ = [h_ for h_ in pph_ if not h_[3] and 'definition' in h_[2]]
    def_ = [x[:80] for x in sents + nsents_ if _def_bad(x)]
    navfig_ = [x[:80] for x in navs_ + sents if _nav_bad(x)]
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    # ### b767, Component 4 (the Edit tool): the entry's nouns b767's -- its banks and the four orders the entry composer names (scratch
    # ### nouns767.py over _finding_text_b767, 20:50:01Z) -- in place of b766's three readings' banks, W-ORD-RUNNER-CACHE and W-ORD-MAP-MERGE
    nouns_ = [w_ for w_ in ('data/%s_corrigendum.txt' % ACT, 'data/%s_price.txt' % ACT, 'data/%s_repairs.txt' % ACT, 'data/%s_controls.txt' % ACT,
                            'data/%s_certificate.txt' % ACT, 'data/%s_plan.txt' % ACT, 'data/%s_source_build.txt' % ACT,
                            'data/%s_window.txt' % ACT, 'data/%s_reproduce.txt' % ACT,
                            'W-ORD-LI-ARITH', 'W-ORD-WINDOW-CERTIFY', 'W-ORD-SOURCE-BUILD', 'W-ORD-NOVEMBER-RIDERS')
              if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    # ### b766: (R376)'s eight clauses and the carried ones beside them; more_, first_, cat_ and the roster printed, graded by no clause of (R376)
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not loc_ and not side_ and trees_ok_ and reg_ok_ and pre_ok_ \
        and len(tx_rows_) == len(f['led_keys']) + 2 and all(r_[2] for r_ in tx_rows_) and not def_ and not ppdef_ \
        and not ppbad_ and not ppside_ and not navfig_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence and (7)`s classK sentence passed, (5)`s ruled sentence passed and its words for zeta caught, the catalogue clause caught either way and a sentence of the open order passed, a negation read, a sentence of positivity at the control naming no side caught and one naming the arithmetic side passed, a quotation wrapped over two lines dropped and the text after it kept, (1)`s readings of b766`s closing table caught where no navigator is named, passed where one is, the act`s own 8.61 of the price bank, the seat`s 13.75 and a longer number passed, the navigator`s form of 8.61 caught, a table row and a prose line naming the navigator before a semicolon each caught by the sentence cut and passed read whole, and a row and a line naming none caught, the closing theorem entered as compiled caught twice and passed as not sent, as the ruling`s condition and as a step`s own theorem): %s; '
        '(a) the files under day1/, phase1.5/, phase2/ and internal/ differing at PLACE-papers HEAD from the act`s base %s: %s: %s; '
        '(b) REGISTRY`s, ERRATA`s, the census`s and the map`s two files` bytes at HEAD their bytes at the base, not written: %s (%s); (c) OPEN_TRAILS and FINDINGS each a byte prefix of its bytes at HEAD: %s: %s; '
        '(d) each text of the ruling as entered equal to the ruling`s text with its fields filled (the rulings tool`s groups, dates %s; [S1] and [R1] each with its order`s entry line; the texts of the outcomes b767 did not reach entered nowhere): %s; '
        'the roster beside (graded by no clause of (R377)), the rulings tool`s group c2 (relay data/%s_ledgers_c2.json) and tools/standing/orders.py`s foot at HEAD (relay data/%s_orders.txt) agreeing %s: %s; '
        'over %d of the act`s own sentences in its banks and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation (graded by no clause of (R377)): %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant (graded by no clause of (R377)): %s; (e) a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; (f) a sentence about the control speaking of positivity with no side named, the lines a dated record heads left out ((R368)(9)): %s; (g) a sentence entering the closing theorem (ControlFailureExists, the closing theorem, L12, [P1]) as compiled outside a negation: %s; a sentence saying the mechanism catalogue has or has not met the zero ((R369)`s clause, graded by no clause of (R377)): %s, in the PLACE-papers writes %s; '
        'over %d units of the act`s PLACE-papers writes (the groups` appended text, the quoted spans dropped), the hits of the centre, side and closing-theorem matchers by place and digest, the words not quoted: %s, of the centre matcher passed by no hand verdict: %s, of the side matcher passed by no hand verdict: %s, of the closing-theorem matcher passed by no hand verdict: %s; '
        '(h) a sentence printing a figure of the navigator`s workspace with no navigator named: %s; the entry`s last line (10)`s INTEGRATION line (%s; %s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            K.PRE_PP[:8], tr_ch_ or 'NONE', trees_ok_,
            reg_ok_, ', '.join('%s %s' % x_ for x_ in tr_un_), ', '.join('%s %s' % x_ for x_ in tr_pre_), pre_ok_,
            ', '.join(sorted(set(str((jl('%s_ledgers_%s.json' % (ACT, g_)) or {}).get('date')) for g_ in N3_GROUPS))), ', '.join('%s in %s %s (%s)' % x_ for x_ in tx_rows_),
            ACT, ACT, ord_ok_, ord_read_,
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', side_ or 'NONE', def_ or 'NONE', cat_ or 'NONE', ppcat_ or 'NONE',
            ppn_, '; '.join('%s %s %s%s' % (p_, d_, k_, (' HAND: %s' % v_) if v_ else '') for p_, d_, k_, v_ in pph_) or 'NONE', ppbad_ or 'NONE', ppside_ or 'NONE',
            ppdef_ or 'NONE',
            navfig_ or 'NONE', il_, _INTEG.get('why') or '-', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
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
    # ### b766, (R376)(4), (11), N5: SIDE-explicit-formula's main against b765's face moved by (4) alone -- main at the closing Lean commit
    # ### (K.RUNNER_COMMIT) where a build from source exited 0 with the restored read's axioms file and v0.45 was cut there (K.WEIL_TAG), and
    # ### at the entering main (K.EF_BASE, b765's v0.44 at 0ba9cd61) otherwise -- b766: the pair stopped, main unmoved and no tag cut by the
    # ### author's word (data/b766_author_words_preseal.txt :32); the tags b765's face read and no other; the tags containing v0.37 v0.37 to
    # ### v0.44, and v0.45 where cut; v0.38 peeling to 14ca5725, v0.41 to a3aad4cc, v0.43 to 819e4a83 and v0.44 to 0ba9cd61
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    _held5 = bool(K.WEIL_TAG) and K.WEIL_TAG[2] == K.RUNNER_COMMIT and K.EF_MAIN == K.RUNNER_COMMIT
    _main5 = K.RUNNER_COMMIT if _held5 else K.EF_BASE
    _want_tags5 = dict(_ef_prev[1] or {})
    if _held5:
        _want_tags5[K.WEIL_TAG[0]] = K.RUNNER_COMMIT[:7]
    tag_one = _ef_now[0] == _main5[:7] and dict(_ef_now[1] or {}) == _want_tags5
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    _contains5 = set(['v0.37', 'v0.38', 'v0.39', 'v0.40', 'v0.41', 'v0.42', 'v0.43', 'v0.44'] + ([K.WEIL_TAG[0]] if _held5 else []))
    ef_ok = ef_main.startswith(_main5[:8]) and _main5 == K.EF_MAIN \
        and set(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) == _contains5 \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.41^{commit}').strip().startswith(K.WEIL_TAG_B759[2][:8]) \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.43^{commit}').strip().startswith(K.ORDER_TAGS_B763[-1][2][:8]) \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.44^{commit}').strip() == K.WEIL_TAG_B765[2] \
        and (not _held5 or g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % K.WEIL_TAG[0]).strip() == K.RUNNER_COMMIT) and ch_ok \
        and bool(prev) and tag_one and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main against b766`s face moved by (4) alone and its tags as b766`s face read them ((R377)(4), (11): main at the closing Lean commit with v0.45 where a build from source exited 0 with the restored read`s axioms file, and at v0.44`s 0ba9cd61 otherwise -- the pair stopped, main unmoved and no tag cut by the author`s word; v0.38 to v0.44 as before; read in full in N5`s kernel clause below), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R373)(5), N5: "no kernel beyond SIDE-explicit-formula is touched"; "the branches removed are those of (4) and no other" -- every
    # ### ref of every kernel carrying a commit made after the act's opening commit is a fault but the act's own: in SIDE-explicit-formula a
    # ### push-b763-* branch, its main at the last tag's peel and the act's tags; SIDE-dirichlet-mod-24 none; a listed branch of the face's
    # ### list excepted as before; no .lean file changed or untracked in a kernel's tree; the rebuild-b721 branches kept as b756 found them;
    # ### the address scan's count from its bank (b759's form, the landings read from the worklist's tags)
    # ### b766 (R376)(4), N5: SIDE-explicit-formula written on push-b766-proof alone, its main the closing Lean commit and v0.45 there where
    # ### a build from source exited 0 with the restored read's axioms file (b766: neither, the pair stopped); SIDE-dirichlet-mod-24 none
    land5_ = [dict(tag=K.WEIL_TAG[0])] if K.WEIL_TAG else []
    main5_ = K.EF_MAIN
    moved5_ = K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8]
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R354)(2)(v): the face's branch list
    own_k_ = ('SIDE-explicit-formula',)
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
                if kn in own_k_ and (r_[0].startswith('refs/heads/push-b767-')
                                     or (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/main' and moved5_ and r_[1].startswith(K.RUNNER_COMMIT[:8]))
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
    # ### N5 (R370): "v0.38 to v0.41 and v0.2.0 peel as before at the close"; "the branches removed are those of (4) and no other".
    # ### SIDE-dirichlet-mod-24: v0.2.0 peeling to e5ebdd15 by its tag object, the local main there as b758 left it. SIDE-explicit-formula:
    # ### the tags v0.39* to v0.42* exactly v0.39, v0.40 and v0.41, v0.38 at 14ca5725, v0.39 at d1afb4fc, v0.40 at 630cba16, v0.41 at
    # ### a3aad4cc by its tag object 390506fc; (4)'s branch removed at the remote by the removal route, its tracking ref absent in the clone
    # ### and the clone's own branch kept at its tip; read locally, no remote read at the record (events (49) holds the route's read-back)
    m24_loc_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % K.M24_TAG[0]).strip()
    m24_main_ = g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'main').strip()
    m24_ok = m24_loc_.startswith(K.M24_TAG[2]) and m24_main_ == m24_loc_ \
        and g(K.M24_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s' % K.M24_TAG[0]).strip().startswith(K.M24_TAG[1])
    # ### b766: where main moved, the gated push's default-mode capture (appended to the branch's capture) reading main back at the remote at
    # ### the closing commit, the local main equal to it, and no such read where it did not; the tags v0.39* to v0.45* exactly v0.39 to v0.44
    # ### and v0.45 where cut, each at its peel
    cap5_ = rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, K.WEIL_BRANCH[0]), optional=True) or ''
    rbm5_ = re.findall(r'(?m)^push_gated: main read back at the remote: ([0-9a-f]{40})$', cap5_)
    efl_ = [('main', (rbm5_[-1:] or ['NONE'])[0][:8], (rbm5_[-1:] == [K.RUNNER_COMMIT] and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/main').strip() == K.RUNNER_COMMIT)
             if moved5_ else not rbm5_)]
    ef_new_tags_ = sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--list', 'v0.39*', 'v0.40*', 'v0.41*', 'v0.42*', 'v0.43*', 'v0.44*', 'v0.45*').split() if t_.strip())
    v038_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip()
    v039_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.39^{commit}').strip()
    v040_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.40^{commit}').strip()
    v041_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.41^{commit}').strip()
    v041o_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/v0.41').strip()
    v042_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.42^{commit}').strip()
    v043_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.43^{commit}').strip()
    v044_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.44^{commit}').strip()
    v044o_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/v0.44').strip()
    v045_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.45^{commit}').strip()
    v045o_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/v0.45').strip()
    # ### b766, (R376)(7) [K22]: push-b765-planted removed at the remote by the removal route and in the clone by the local delete
    # ### (KERNEL_DELETES and KERNEL_REMOVED, that one name): absent from the clone and from its tracking refs (events (37) holds the
    # ### route's read-back); b760's removal of push-b759-weil as b760 left it, its tracking ref absent in the clone and the clone's own branch
    # ### kept at its tip; b763's four branches, push-b764-runner and push-b765-centre on the clone at their tips; push-b766-proof read back at
    # ### the remote in its capture at its tip
    pl5_ = [(b_, b_ in K.KERNEL_REMOVED and not g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s' % b_).strip()
             and not g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/%s' % b_).strip()) for b_ in K.KERNEL_DELETES]
    rm_trk_ = [b_ for b_, _t in (K.WEIL_BRANCH_B759,) if g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/%s' % b_).strip()]
    rm_loc_ = [(b_, g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s' % b_).strip()[:8] or 'NONE') for b_, _t in (K.WEIL_BRANCH_B759,)]
    ef_rb_ = [(b_, b_ not in rm_trk_ and l_ == t_[:8]) for (b_, t_), (_b, l_) in zip((K.WEIL_BRANCH_B759,), rm_loc_)]
    ef_rb_ += [(b_, g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s' % b_).strip().startswith(t_[:8]))
               for b_, t_ in (K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1], K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0], K.WEIL_BRANCH_B764, K.WEIL_BRANCH_B765)]
    ef_rb_ += [(b_, bool(re.search(r'(?m)^push_gated: branch %s read back at the remote: %s' % (re.escape(b_), t_ or '-'), cap5_))) for b_, t_ in (K.WEIL_BRANCH,)]
    # ### b767, Component 4 (the Edit tool, found carried with b766's meaning while the record sections were read for their constants):
    # ### (R377)(4), (12), N5 -- no kernel branch removed (KERNEL_DELETES, KERNEL_REMOVED and KERNEL_DELETES_REFUSED none), where b766's
    # ### predicate below wanted [K22]'s one name removed; push-b766-proof on the clone at 3c67b8b5 as b766's [P2] cites it
    ef_rb_ += [(b_, g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s' % b_).strip() == t_) for b_, t_ in (K.WEIL_BRANCH_B766,)]
    efb_ok = ef_new_tags_ == ['v0.39', 'v0.40', 'v0.41', 'v0.42', 'v0.43', 'v0.44'] + ([K.WEIL_TAG[0]] if K.WEIL_TAG else []) and all(o_ for _t, _l, o_ in efl_) \
        and v038_.startswith('14ca5725') and v039_.startswith('d1afb4fc') and v040_.startswith('630cba16') \
        and v041_.startswith(K.WEIL_TAG_B759[2][:8]) and v041o_.startswith(K.WEIL_TAG_B759[1][:8]) and v042_.startswith(K.WEIL_BRANCH_B763[1][:8]) \
        and v043_.startswith(K.ORDER_TAGS_B763[-1][2][:8]) \
        and v044_ == K.WEIL_TAG_B765[2] and v044o_ == K.WEIL_TAG_B765[1] \
        and ((v045_ == K.WEIL_TAG[2] and v045o_ == K.WEIL_TAG[1]) if K.WEIL_TAG else not v045_) \
        and K.KERNEL_DELETES == () == K.KERNEL_REMOVED and not K.KERNEL_DELETES_REFUSED and all(o_ for _b, o_ in pl5_) and all(o_ for _b, o_ in ef_rb_)
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
            'the address scan (relay data/b767_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel, the act owning push-b767-proof and, where a build from source exited 0 with the restored read`s axioms file, SIDE-explicit-formula`s main (at %s, the closing commit %s) and v0.45, or a .lean file in a kernel`s tree (%d kernels read): %s; the act`s own refs read: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; SIDE-dirichlet-mod-24`s tag %s peeling locally to %s, its local main %s: %s; SIDE-explicit-formula: main read back at the remote in the branch`s capture %s; the tags v0.39* to v0.45* %s, v0.38 at %s, v0.39 at %s, v0.40 at %s, v0.41 at %s by its tag object %s, v0.42 at %s, v0.43 at %s, v0.44 at %s by its tag object %s, v0.45 at %s; kernel branches removed by this act, none ruled ((R377)(12)): %s (%s), b760`s removal of %s as b760 left it, its tracking ref absent in the clone and its local branch kept at its tip, b763`s four branches, push-b764-runner and push-b765-centre at their tips, push-b767-proof read back in its capture and push-b766-proof on the clone at 3c67b8b5 (%s): %s;'
            'gh repo edit run by a captured command (the carried reader): %s; gh repo edit sent from inside a tool, read by its rows bank (the taught reader, tools/b757_ghcalls.py): %s, none wanted: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (main5_[:8], K.RUNNER_COMMIT[:8], len(kps_), lean_w or 'NONE', ', '.join(own_r) or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                K.M24_TAG[0], m24_loc_[:8] or 'NONE', m24_main_[:8] or 'NONE', m24_ok,
                ', '.join('%s %s %s' % x_ for x_ in efl_),
                ef_new_tags_ or 'NONE', v038_[:8] or 'NONE', v039_[:8] or 'NONE', v040_[:8] or 'NONE', v041_[:8] or 'NONE', v041o_[:8] or 'NONE', v042_[:8] or 'NONE', v043_[:8] or 'NONE',
                v044_[:8] or 'NONE', v044o_[:8] or 'NONE', v045_[:8] or 'NONE',
                ', '.join('%s %s' % (b_, 'REMOVED' if b_ in K.KERNEL_REMOVED else 'REFUSED, KEPT') for b_ in K.KERNEL_DELETES) or 'none', ', '.join('%s %s' % x_ for x_ in pl5_) or 'none', K.WEIL_BRANCH_B759[0],
                ', '.join('%s %s' % x_ for x_ in rm_loc_) + '; tracking refs left %s; ' % (rm_trk_ or 'NONE') + ', '.join('%s %s' % x_ for x_ in ef_rb_), efb_ok,
                'UNREAD (no command bank)' if gho_ is None else (ghr_ or 'NONE'), '; '.join('tools/%s.py %s' % (s_, v_) for s_, v_ in ghs_.items()) or ('UNREAD (no command bank)' if gho_ is None else 'NONE'), gh_ok,   # ### defect (x): NONE printed unread
                ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b767, Component 4 (the Edit tool): the carried stub replaced -- the ruling's ordinal and title (the ferry's ACT line, data/b767_ferry.txt
    # ### :109) as the act did it, read from the banks: the ledgers' entered keys by group (data/b767_ledgers_c2.json and _c5.json, and _c6.json
    # ### where the closing pair enters [C7] or [C8]), the worklist's tag and the standing version; the dash and apostrophe typographic, (R368)(3).
    # ### Its opening to "under (R377)" is the next act's needle for b767's trail record
    le_ = {}
    for g_ in ('c2', 'c5', 'c6'):
        le_.update((jl('%s_ledgers_%s.json' % (ACT, g_)) or {}).get('entered') or {})
    return ('### b767 — lane two, act one hundred and ninety-four, The proof by the banked window continued, under (R377): b766 at its weight; '
            'the plan amended; the archimedean term as the combination, the enclosures and the inequality %s; the build from source given its '
            'order, its route %s; main and the tag %s; the window at knots graded by octave %s; the author’s rulings entered; one key; '
            'tools/standing/ from %s to %s' % (
                'with the closing theorem, the proof whole' if 'P1' in le_ else ('the proof in part' if 'P2' in le_ else 'not entered'),
                'held' if 'S2' in le_ else ('not held' if 'S3' in le_ else 'not tried'),
                ('moved to the closing commit with %s' % K.WEIL_TAG[0]) if K.WEIL_TAG else ('unmoved, [C7]' if 'C7' in le_ else ('unmoved, [C8]' if 'C8' in le_ else 'unmoved')),
                'held' if 'G1' in le_ else ('refuted' if 'G2' in le_ else ('not scored' if 'G3' in le_ else 'not entered')),
                K.STANDING_VERSION_ENTERING, K.STANDING_VERSION))
#⟪END⟫
#⟪SECTION record 29⟫
# ### b756: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict
# ### b759, before the lock: the guard over (R369)(1)-(11)'s feet


def _guard(f):
    """the composer's refusals before any sentence, where the banks' feet disagree with one another (never on a verdict), b767's: the one
    key's row of the repairs bank against the worklist's standing versions, VERSION at HEAD the last; the dispatch tool's foot equal to the
    worklist's cap and its kind with the restore on, the dispatch rows each read once and as many as the foot counts, those with the restore
    on as many as it counts; the dispatch tool's, the certificate's, the source-build read's, the two data files' and the groups' controls
    whole; the groups' files each OPEN_TRAILS; the roster's counts summing at HEAD; the reproduction run's rows summing. A verdict otherwise
    than wanted is printed, never refused here. (b767, Component 4, the Edit tool: b766's three keys, data files, masking and readings out.)"""
    if len(f['reps']) != 1 or sum(len(v_) for v_ in f['rep_states'].values()) != 1 or f['ver'] != K.STANDING_VERSION \
            or sorted(f['rep_states']['REPAIRED'] + f['rep_states']['REMOVED']) != sorted(k_ for k_ in f['srep'] if k_.startswith('K')):
        sys.exit('### THE REPAIRS BANK`S ONE ROW, THE STANDING VERSIONS OR VERSION AT HEAD DISAGREE -- NOTHING COMPOSED')
    on_ = ('trial-on', 'b', 'c', 'd', 'e')   # ### tools/b767_controls.py's items with the restore on (ON_ITEMS)
    if f['disp_m24'] != 0 or f['read_ef'] != f['disp_ef'] or f['tr_disp'] != (f['disp_ef'], K.MAX_DISPATCHES) \
            or f['tr_on'] != (sum(1 for r_ in f['runs'] if r_['item'] in on_), dict(K.MAX_DISPATCHES_KINDS)['restore']):
        sys.exit('### THE DISPATCH TOOL`S FOOT, THE CAP, OR THE DISPATCH ROWS AND THEIR READS, DISAGREE -- NOTHING COMPOSED')
    if any(a_ != b_ for a_, b_ in [f['cc_ctl'], f['tr_ctl'], f['cert_ctl'], f['sb_ctl'], f['ld_ctl'], f['nd_ctl']] + list(f['led_ctl'])):
        sys.exit('### THE DISPATCH TOOL`S, THE CERTIFICATE`S, THE SOURCE-BUILD READ`S, A DATA FILE`S OR A GROUP`S CONTROLS ARE NOT WHOLE -- NOTHING COMPOSED')
    if len(f['led_files']) != len(N3_GROUPS) or any(p_ != 'OPEN_TRAILS.md' for p_, _b, _a, _n, _s, _t in f['led_files']):
        sys.exit('### THE GROUPS` FILES DISAGREE -- NOTHING COMPOSED')
    if f['ord_head'][1] + f['ord_head'][2] != f['ord_head'][0]:
        sys.exit('### THE ROSTER`S COUNTS DO NOT SUM -- NOTHING COMPOSED')
    if f['rp_repro'] + f['rp_differs'] + f['rp_notrun'] != f['rp_rows'] or f['rp_ctl'][0] != f['rp_ctl'][1]:
        sys.exit('### THE REPRODUCTION RUN`S ROWS DO NOT SUM -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects (the ferry's ACT line, data/b767_ferry.txt :109, adjusted to what the act did): b766 at its weight
    (b767_corrigendum); the one key of (8) (b767_repairs); the plan amended and the certificate's three forms of (4)(a) (b767_plan,
    b767_certificate); the steps of (4)(b) to (4)(e) by [P1] or [P2] (b767_ledgers_c5); the source-build read and the trial of (5)
    (b767_source_build, b767_controls); the closing build from source and main and the tag of (4) (b767_controls); the window at graded
    knots of (6) (b767_registration, b767_window); the rulings of (7) (b767_ledgers_c2); the roster read after the lines (b767_orders); the
    dispatches. Each object's name in the heading, the act's FINDINGS names for the line reader; every figure from the banks' feet, in
    digits; the apostrophe typographic and no backtick, (R368)(3)'s rule, which tools/standing/titlerule.py refuses at the landing."""
#⟪END⟫
#⟪SECTION record 31⟫
    # ### b767, Component 4 (the Edit tool): b767's title by its objects, each outcome read from the groups' entered keys and the dispatch
    # ### tool's foot; the closing build's outcome in words of the ruling: main moved with the tag, [C7] or [C8]
    _guard(f)
    le_ = f['led_entered']
    mn_ = ('main moved to the closing commit with %s' % K.WEIL_TAG[0]) if K.WEIL_TAG else ('main unmoved, [C7]' if 'C7' in le_ else ('main unmoved, [C8]' if 'C8' in le_ else 'main unmoved'))
    return ('## The proof by the banked window continued, under (R377): b766 %s (b767_corrigendum); one key, with its planted control (b767_repairs); '
            'the plan amended and the certificate’s three forms (b767_plan, b767_certificate); the archimedean term in the B-spline basis, the enclosures and the '
            'pole term’s data half compiled, the proof %s (b767_ledgers_c5); the build from source read and its route %s at the trial (b767_source_build, '
            'b767_controls); the closing build from source at %s, %s (b767_controls); the window at knots graded by octave %s, %s (b767_registration, b767_window); '
            'the author’s rulings entered (b767_ledgers_c2); %d open to %d (b767_orders); %d dispatches' % (
                f['close_word'], 'whole' if 'P1' in le_ else ('in part' if 'P2' in le_ else 'not entered'),
                'held' if 'S2' in le_ else ('not held' if 'S3' in le_ else 'not tried'), (K.RUNNER_COMMIT or '-')[:8], mn_,
                f['win_reading'].lower(), '[%s]' % f['win_key'], f['led_roster'][0], f['ord_head'][1], f['disp']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    # ### b761: the seat's read of what (R371) misses (data/b761_misses.txt, its first printing and the second, before the lock, below it),
    # ### each item by its number once and its line, in the bank's own words to its first semicolon; then the navigator's and the seat's own
    ml_ = rdn('%s_misses.txt' % ACT).replace(chr(13), '').split(NL)
    items_, seen_ = [], {}
    for i_, l_ in enumerate(ml_):
        m_ = re.match(r'^  \((\d+)\) (.+)$', l_)
        # ### b763, Component 6 (the touch read): an item the second printing restates ((2), superseded for FORM B) is read at its latest
        # ### line, in its first printing's place; the first printing's line stood against the entry's centre, FORM B committed at a named window
        if m_ and m_.group(1) in seen_:
            items_[seen_[m_.group(1)]] = (i_ + 1, _first_clause(m_.group(2)).rstrip('.;'))
        elif m_:
            seen_[m_.group(1)] = len(items_)
            items_.append((i_ + 1, _first_clause(m_.group(2)).rstrip('.;')))
    # ### b761, Component 6 (the record read before its commit): the first clause cut at a semicolon outside quotation marks (item (6)'s
    # ### quoted form carries " ; "), and the template's count word read so that no navigator miss prints "no", not "the none"
    return _no_none('; '.join('(%d) %s (relay data/%s_misses.txt :%d)' % (k_ + 1, t_, ACT, n_) for k_, (n_, t_) in enumerate(items_)) + '; '
            '(%d) %s and the seat’s %s defect%s as lettered' % (len(items_) + 1,
#⟪END⟫
#⟪SECTION record 33⟫
def _first_clause(s):
    """b761: a misses item to its first semicolon standing outside double quotation marks (the whole item where it has none)."""
    q_ = False
    for i_, c_ in enumerate(s):
        if c_ == '"':
            q_ = not q_
        elif c_ == ';' and not q_:
            return s[:i_]
    return s


def _no_none(s):
    """b761: the line as the template composes it, "the none navigator misses" kept: the standing readers take "(\\d+) the (\\w+) navigator
    (?:miss|misses)" (record.tpl's dry-run step through _trail_resolved; checks.tpl's trail_resolved_ok), so the rewording of events (63)
    is withdrawn (defect (m))."""
    return s


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
    """v9 row (83): "a class that repeats in three acts running is the next act's opening component". v1.38.14, (R374)(5) [K18]: read by
    tools/standing/repeat.py runs3 -- the act's lettered rows and the findings after a lock (the previous act's, under the corrigendum's
    FINDINGS AFTER ITS LOCK head, and the act's own after its lock), a row of any actor, each followed back through its tags: a list of
    (the row's label, 'b<n-2> ... -> b<n-1> ... -> <label>'). The carried form read the defects bank alone, the seat's and the navigator's
    rows alone, and read 0 rows in 0 classes at b763 (OPEN_TRAILS :19027)."""
    return [(lab, ch) for lab, _own, ch in __import__('standing.repeat', fromlist=['runs3']).runs3(act, lambda n_: rdn(n_, optional=True) or '')]


def _report10():
    """(R371)(10), ONE REPORT: the hours from the opening row to the lock and from the lock to the closing, read from the step rows as
    data/b754_close_yield.txt (A) reads them (each span from its two rows, rounded to 0.01 h); and, tools/standing/ being unmoved, which
    parts of each pass ran and which were read from a bank under the cadence (tools/standing/cadence.py), read from each part's bank under
    the mode's name: READ FROM A BANK BY THE CADENCE, NOT RUN BY THE CADENCE, or run. The pass after the push and the closing come after the
    entry: where their rows or banks are not yet written the report says so, and the closing message prints them."""
    from standing import lockdate as LD
    from standing import cadence as CAD
    sj_ = jl('%s_steps.json' % ACT) or {}
    rows_ = sj_.get('rows') if isinstance(sj_, dict) else sj_
    rows_ = [r_ for r_ in rows_ or [] if r_.get('repo') == 'relay']
    ep_ = lambda r_: calendar_gm(r_.get('at'))
    lc_ = LD.lock_of(ACT, D)
    lock_ = next((r_ for r_ in rows_ if lc_ and str(r_.get('commit') or '').startswith(lc_[:8])), None)
    clo_ = next((r_ for r_ in reversed(rows_) if r_.get('phase') == 'closing'), None)
    op_ = rows_[0] if rows_ else None
    h_ = lambda a_, b_: '%.2f h' % ((ep_(b_) - ep_(a_)) / 3600.0) if a_ and b_ and ep_(a_) and ep_(b_) else 'not yet read'
    at_ = lambda r_, w_: '%s at %s' % (str(r_.get('commit') or '-')[:8], r_.get('at') or '-') if r_ else w_
    hours_ = 'from the opening row (%s) to the lock (%s) %s ; from the lock to the closing (%s) %s ; from the opening row to the closing %s' % (
        at_(op_, 'no row'), at_(lock_, 'not yet made'), h_(op_, lock_), at_(clo_, 'not yet a row'), h_(lock_, clo_), h_(op_, clo_))
    by_ = []
    for mode_ in ('prerun', 'prev', 'pre-push', 'post-push'):
        cls_ = {}
        for p_ in K.PARTS:
            t_ = rdn(CAD.text_name(ACT, mode_, p_), optional=True) or ''
            k_ = 'not yet written' if not t_ else 'read from a bank' if 'READ FROM A BANK BY THE CADENCE' in t_[:2000] else 'not run' if 'NOT RUN BY THE CADENCE' in t_[:2000] else 'ran'
            cls_.setdefault(k_, []).append(p_)
        by_.append('%s: %s' % (mode_, '; '.join('%s %s' % (k_, ', '.join(v_)) for k_, v_ in sorted(cls_.items()))))
    return hours_, by_


def _b7_head():
    """b760's closing head line (data/b760_closing.txt :1) read by its form: relay, PLACE-papers, suite, of, prompts, scores, of, defects."""
    m_ = re.match(r'^b766 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root \w+…; (\d+) prompts? answered; scores (\d+) of (\d+) HELD; (\d+) defects',
                  rdn('b766_closing.txt').split(NL)[0])
    if not m_:
        sys.exit('### b766`S CLOSING HEAD LINE NOT READ -- NOTHING COMPOSED')
    return m_


def calendar_gm(at):
    """a step row's time (2026-11-18T21:42:28Z) as an epoch; None where unread."""
    import calendar
    try:
        return calendar.timegm(time.strptime(str(at)[:19], '%Y-%m-%dT%H:%M:%S'))
    except Exception:
        return None


def _runs3_line():
    """the rows of _runs3 grouped by the class's row two acts back, each class once with this act's rows under it."""
    r = _runs3()
    by = {}
    for l, c in r:
        by.setdefault(c.split(' -> ')[0], []).append(l)
    return ('the classes repeating three acts running, by the tags of the lettered rows and of the findings after a lock (v9 row (83), each the '
            'next act’s opening component, printed for the author beside the next act of %s): %d rows in %d classes -- %s' % (
                __import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R377)(13)', len(r), len(by), '; '.join(
                    '%s as %s' % (k, ', '.join(v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b767's objects; b766's composer in git at
    b766's record tool). Its last line the INTEGRATION line of (R377)(9), bare, the ruling's own, read from the ferry's bank (_integ_line).
    b767's paragraphs composed by _finding_text_b767; b766's kept below it, not called."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    return _finding_text_b767(f, S, rep, tot)


def _finding_text_b766_kept(f, S, rep, tot):
    """b766's paragraphs over b766's objects, kept for the record and not called (b767, Component 5)."""
    # ### b766: its closing head line, the corrigendum's rows, the report of (11), the repairs' rows, the trial's runs and the ledgers'
    # ### lines by key, read once for the paragraphs below
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    r10h_, r10p_ = _report10()
    rs_, le_ = f['rep_states'], f['led_entered']
    ldate_ = (jl('%s_ledgers.json' % ACT) or {}).get('date') or '-'
    ln_ = lambda k_: ('OPEN_TRAILS :%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    pw_ = lambda k_: '%s to %s h' % (f['pr_rows'][k_]['lo_h'], f['pr_rows'][k_]['hi_h'])
    pd_ = lambda k_: '%s over %s to %s dispatches' % (pw_(k_), f['pr_rows'][k_]['dispatches'][0], f['pr_rows'][k_]['dispatches'][1])
    rnw_ = '; '.join('dispatch %d, the %s with the restore %s, run %s at %s, %s, %s minutes of run and %s of build' % (
        r_['n'], r_['item'], r_['restore'], r_['run'], r_['at'], r_['verdict'] or 'not read', '-' if r_['run_min'] is None else r_['run_min'],
        '-' if r_['build_min'] is None else r_['build_min']) for r_ in f['runs']) or 'none'
    took7_ = round(sum(r_['run_min'] or 0 for r_ in f['runs']), 1)
    moved_ = (K.EF_MAIN or '')[:8] == (K.RUNNER_COMMIT or '-')[:8]
    sv7_ = next((r_ for r_ in f['runs'] if r_['item'] == 'save'), None)       # ### the save's and the restore's read rows, for the seat's reading
    rr7_ = next((r_ for r_ in f['runs'] if r_['item'] == 'restore'), None)    # ### beside the verdict (relay data/b767_events.txt (50))
    xk_ = (f['xline'] or {}).get('key')
    held_ = f['it_verdict'] == 'HELD'
    sti_ = lambda s_: '%d %s (%s)' % (len(rs_[s_]), s_.lower(), ', '.join(rs_[s_]) or 'none')
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    cl_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)   # ### the order line's commits by key, PLACE-papers and relay (the worklist's chains)
    e = ['', _title(), '',
         ' '.join(s_.rstrip('.') + '.' for s_ in (f['y_sentence'], f['tr_sentence'], f['it_sentence'])) + (
             ' Each sentence is the ruling`s for the outcome its bank reads, its fields filled from that bank (relay data/b767_close_yield.txt, data/b767_controls.txt, '
             'data/b767_imp2tau.txt); the nineteen keys of (5) each with its row and its sentence below (relay data/b767_repairs.txt); every build a runner dispatch '
             'read by its run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b767_dispatch_rows.json); no lean process on this host.' % f['disp_ef']), '',
         '*Filed at b767 on the author’s ruling `(R377)` and the author’s word of 2026-11-20 on its (9)(b); %d question%s put before the root%s. Banks: relay '
         '`data/b767_misses.txt`, `data/b767_price.txt`, `data/b767_navigator_predictions.txt`, `data/b767_corrigendum.txt`, `data/b767_repairs.txt`, '
         '`data/b767_repair_controls.txt`, `data/b767_standing_dry.txt`, `data/b767_kernel_bases.json`, `data/b767_close_yield.txt`, `data/b767_ceiling.txt`, '
         '`data/b767_controls_control.txt`, `data/b767_targets.json`, `data/b767_dispatch_rows.json`, `data/b767_controls.txt`, `data/b767_xlines.json`, the gated '
         'push`s capture `data/b767_SIDE-explicit-formula_push-b767-runner_push_out.txt`, `data/b767_registration.txt`, `data/b767_author_words_preseal.txt`, '
         '`data/b767_imp2tau.txt`, `data/b767_orders_reading.txt`, `data/b767_deposit_read.txt`, `data/b767_ledgers.txt`, `data/b767_orders.txt`, '
         '`data/b767_reproduce.txt`, `data/b767_author_answers.txt`, `data/b767_events.txt`, `data/b767_defects.txt`, `data/b767_prelock.txt`, '
         '`data/b767_pathrefusal.txt`, `data/b767_address_scan.txt`, `data/b767_touch.txt`, `data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's', (' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record`s head line gives it; the relay`s main read back at %s after its closing push (relay data/b766_closing.txt, data/b766_scores_close.json). '
         'The corrigendum, short: b766’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items printed in full; '
         'what the seat found after b766`s lock entered as this act`s events (%s) to (%s) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; the navigator`s own %d entered as the navigator`s, CLAIM, events (%s) to (%s); at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8), K.PRE_RELAY[:8],
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], len(nr_), nr_[0], nr_[-1], f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The price and the ceiling** ((R377)(3)): the price table banked at step zero, before Component 1, from banked timings, each item with its lines, its dispatches and its hours, a dispatch priced by its kind -- a build of the kernel whole at %s to %s minutes and a module`s closure at %s -- the seat`s own readings printed as the seat`s: the lower sum %s h against %d h, %s, the upper sum %s h (relay data/b767_price.txt). '
         'Read again after Component 2 by tools/b767_ceiling.py, committed before its run, at %s: %s h spent from the delivery, %s h at the lower figures against %d h, %s; its plan %s; dispatches %d of %d at that reading (relay data/b767_ceiling.txt). '
         'The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             f['pr_minutes'][1][0], f['pr_minutes'][1][1], f['pr_minutes'][0], f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['pr_upper'],
             f['ce_at'], f['ce_reading']['spent'], f['ce_sum'], f['ce_ceiling'], f['ce_word'].lower(), f['ce_verdict'], f['ce_disp'][0], f['ce_disp'][1]), '',
         '**The repairs, by class** ((R377)(5)), in the order of repair, each with its planted control read at the commit before the repair and at the repair`s commit, both printed (relay data/b767_repairs.txt, data/b767_repair_controls.txt): tools/standing/ moved from %s to %s by %d commits, one a key of (5) repaired or removed and one for (7), VERSION moved by each, the standing dry before each (relay data/b767_standing_dry.txt); %s, %s, %s and %d carried. %s' % (
             f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), sti_('REPAIRED'), sti_('READ AS DESIGNED'), sti_('REMOVED'), len(rs_['CARRIED']),
             ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps'])), '',
         '**The close’s hours and yield** ((R377)(6)): tools/b754_yield.py carried as tools/b767_yield.py, committed before its run, its controls printed before its figures, %d of %d as wanted, over b754 to b766: (A) the hours by the step rows with each phase`s beside them; (C) each standing arm with the number of the ten acts at which it read a fault. %s. The %d that read a fault at none stand listed for the author`s strike and are printed beside the root`s question; nothing is removed on them by this act (relay data/b767_close_yield.txt).' % (
             f['y_ctl'][0], f['y_ctl'][1], f['y_sentence'].rstrip('.'), f['y_arms'][2]), '',
         '**The runner on a restored build** ((R377)(7)): on push-b767-runner made at main %s (v0.43), one commit %s, the workflow`s file alone: the kernel`s own build directory restored from the runner`s cache before the build and saved after, keyed by the toolchain and the manifest as (7) words it, a third input turning the restore off and off where the input is absent; the seat`s printed read of the key departed from and the departure entered (relay data/b767_defects.txt (g)); the dispatch route of (R376)(5) carried, no change under tools/standing/ for it. '
         'The dispatch and the read by tools/b767_controls.py, committed before its opening dispatch, its controls %d of %d (relay data/b767_controls_control.txt); the three dispatches of the branch`s tip, each read by its run id from the downloaded artifact, the exit file governing: %s (relay data/b767_dispatch_rows.json). The trial %s: %s; its controls %d of %d (relay data/b767_controls.txt). '
         '%sThe rule it enters, in either outcome: a tag is cut on a run with the restore off and on no other. %s W-ORD-RUNNER-CACHE entered by [C1] at %s and %s by [%s] at %s.' % (
             K.EF_BASE[:8], (K.RUNNER_COMMIT or '-')[:8], f['cc_ctl'][0], f['cc_ctl'][1], rnw_, f['tr_verdict'].lower(), f['tr_where'], f['tr_ctl'][0], f['tr_ctl'][1],
             ('Beside the verdict and not in it, the seat`s reading: the save, the restore on with no key held, built from source at the same commit and exited 0, '
              'and its axioms file of %s lines has the restoring run`s sha256 %s; (7) names the run with the restore off the reference, and the save is not read in its place '
              '(relay data/b767_events.txt (50)). ' % (sv7_['ax_lines'], sv7_['ax_sha'])) if f['tr_verdict'] != 'REPRODUCES' and sv7_ and rr7_ and sv7_['exit'] == '0' == rr7_['exit']
             and sv7_['from_source'] is True and sv7_['ax_sha'] and sv7_['ax_sha'] == rr7_['ax_sha'] else '',
             ('Main moved from %s to the branch`s tip %s by the gated push`s default mode after the trial`s success, never forced, and read back at the remote (relay data/b767_SIDE-explicit-formula_push-b767-runner_push_out.txt); the kernel`s local main fast-forwarded by the one-call tool and read back equal; no tag cut, no declaration having changed.' % (
                 K.EF_BASE[:8], (K.RUNNER_COMMIT or '-')[:8])) if moved_ else 'The workflow`s change stays on its branch; main stands at %s; no tag cut; builds stay from source.' % K.EF_BASE[:8],
             ln_('C1'), 'DISCHARGED' if xk_ == 'C2' else 'CARRIED', xk_ or '-', ln_(xk_ or '-')), '',
         '**The orders the upkeep carries** ((R377)(8)): each priced in the table from its entry (relay data/b767_price.txt) and taken after Component 2 in ascending order of its upper hours. %s; %s; %s (relay data/b767_orders_reading.txt).' % (
             ('W-ORD-E0-RANK-PROPAGATION built as one appended line, [D2] at %s, naming the E0 table of b332 and b333`s re-rank and editing neither' % ln_('D2')) if 'D2' in le_
             else 'W-ORD-E0-RANK-PROPAGATION not built, carried by name at %s' % pw_('(8) E0-RANK-PROPAGATION'),
             ('W-ORD-BIBLIOGRAPHY-LINK built, the register BIBLIOGRAPHY.md brought current by its section 6, five works at :%s, [D1] at %s' % (f['led_bib'], ln_('D1'))) if 'D1' in le_
             else 'W-ORD-BIBLIOGRAPHY-LINK not built, carried by name at %s' % pw_('(8) BIBLIOGRAPHY-LINK'),
             ('W-ORD-LATE-BANKS at %s, W-ORD-MATCHER-SHAPE at %s and W-ORD-CORRESPONDENCE-BEHIND-SCOPE at %s read and not built, each carried by name with its price, no line written for any' % (
                 pw_('(8) LATE-BANKS'), pw_('(8) MATCHER-SHAPE'), pw_('(8) CORRESPONDENCE-BEHIND-SCOPE'))) if 'EACH CARRIED BY NAME' in f['or_words']
             else 'the three others as the reading`s foot gives them: %s' % f['or_words'].lower()), '',
         '**What b766’s landings trigger** ((R377)(9)). (a) The erratum: the deposit read over PLACE-papers outputs/ first, %d files read, %s, its controls %d of %d (relay data/b767_deposit_read.txt); [E1] at ERRATA`s end from :%s, E-%s-1, its fields filled, no entry above it edited; [F1] at %s; no line of the paper edited. '
         '(b) The finite part of the archimedean term, under W-ORD-IMP2-TAU: [G1], %s, committed alone at relay %s (%s) before the tool`s run, the author`s word of 2026-11-20 in its words (relay data/b767_registration.txt, data/b767_author_words_preseal.txt); tools/b766_imp2tau.py carried as tools/b767_imp2tau.py with the limit F added, committed before its run, its controls %d of %d printed before any cell, [G1]’s among them; %s at %d cells to %d digits in %d s (relay data/b767_imp2tau.txt); %s at %s%s. '
         '(c) The centre, priced anew and not built, in four readings, each the seat`s own, beside the table and not summed: [L-i] FORM B through the archimedean term`s integral over a bounded interval at %s; [L-ii] the statement with no number of a zero in it at %s; [L-iii] a spline window in the multiplicative variable, its three terms exact, at %s; [L-iv] the numerics moved out of the barred directory at %s; the cheapest by its upper figure %s (relay data/b767_price.txt); [L1] at %s, W-ORD-LI-ARITH carried; the navigator`s workspace figures stand in the ruling`s text as the navigator`s and in no bank of this act. '
         '(d) W-ORD-LI-WEIL-BRIDGE, its trigger met at b766: its next step a reading at the act that sends the centre`s proof; [B1] at %s.' % (
             f['dep_files'], 'no deposited artifact holding the paper' if f['dep_found'] == 0 else '%d holding it' % f['dep_found'], f['dep_ctl'][0], f['dep_ctl'][1],
             le_['E1'][0] if 'E1' in le_ else '-', ldate_, ln_('F1'),
             f['reg_name'], f['reg_commit'], f['reg_date'], f['it_ctl'][0], f['it_ctl'][1], f['it_verdict'], f['it_cells'], f['it_digits'], f['it_secs'],
             '[M1]' if held_ else '[M2]', ln_('M1' if held_ else 'M2'), ', its closing sentence the author`s word`s (iv)' if held_ else ', its trigger the author`s word`s (v)',
             pd_('(9)(c) [L-i]'), pd_('(9)(c) [L-ii]'), pd_('(9)(c) [L-iii]'), pd_('(9)(c) [L-iv]'), f['pr_cheapest'], ln_('L1'), ln_('B1')), '',
         '**The ledgers** ((R377)(7)-(9)): by tools/b767_rulings.py, committed before its run, each file`s bytes at HEAD a prefix of its new bytes, no line moving: %s; in OPEN_TRAILS under one dated head at :%d, %s; controls %d of %d (relay data/b767_ledgers.txt). '
         'The roster by tools/standing/orders.py`s rule: open %d before and %d after; at PLACE-papers HEAD orders %d, open %d, closed %d (relay data/b767_orders.txt).' % (
             '; '.join('%s %d to %d lines, from :%d' % (p_, b_, a_, n_) for p_, b_, a_, n_, _s, _t in f['led_files']), f['led_head'][0],
             ', '.join('[%s] at :%d' % (k_, le_[k_][0]) for k_ in f['led_keys'] if k_ in le_), f['led_ctl'][0], f['led_ctl'][1],
             f['led_roster'][0], f['led_roster'][1], f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The navigator’s predictions** ((R377)(10)): [P1] banked verbatim from the ferry as relay data/b767_navigator_predictions.txt and committed alone at %s before Component 1, its subject read back equal; a bank of texts, nothing of it computed here and no verdict reading it. The change by which tools/b667_epstein_certify.py takes its form as data priced at %s and not built.' % (
             K.STEPZERO_PREDICTIONS[:8], pw_('(10)')), '',
         '**The research instruments reproduced** ((R377)(13), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (%s), the planted controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; tools/standing/ moved by the commits of (5) and (7) alone, from %s to %s, VERSION moved by each and each with its planted control; each act tool committed before its run; the kernel`s one commit by the one-call tool and its push by the gated push, %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_).replace(']`s', ']’s'), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), f['st_entering'], f['st_version'],
             'SIDE-explicit-formula`s main moved after the trial`s success and at no other time' if moved_ else 'SIDE-explicit-formula`s main not moved, the trial having failed'), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula, and there the workflow`s file alone; no push forced; no tag cut or moved, v0.38 to v0.43 and v0.2.0 among them; no pin moved; no sentence of any paper written or edited, ERRATA and the register BIBLIOGRAPHY.md the two files of PLACE-papers written beside FINDINGS and OPEN_TRAILS; REGISTRY not written; no statement and no line of a proof of the centre sent; nothing computed at a zero and no row of a bank of zeros opened by the seat`s hand: the reproduction run`s row I-88, which (13) orders run in full, reads one figure at data/b694_witness_zeros.txt :5 by its tool, and two reads of banks that carry an explicit formula`s zero side as a column, each entered for the author`s strike (relay data/b767_events.txt (40), (48)); nothing fetched from the web by the seat; no lean process on this host; no byline; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel`s commit among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (11)**: the hours by the step rows, as relay data/b754_close_yield.txt (A) reads them: %s (the closing comes after this entry and its row is printed in the closing message). '
         'The parts of each pass by the cadence (tools/standing/cadence.py %s), tools/standing/ at %s: %s; the pass after the push runs after this entry, its parts printed in the closing message. '
         'The price table`s figures beside what each item took: (5) each key with its price and what it took in its row of relay data/b767_repairs.txt; (7)`s three dispatches priced %s and %s, taking %d dispatches and %s minutes of runs; (9)(b) priced %s, its tool`s run %d s (relay data/b767_price.txt, data/b767_dispatch_rows.json). '
         'The repairs bank`s rows by state: %s, %s, %s and %d carried. '
         'THE MEASURE, written here and read at the close of the act after this one, where it is entered in that act`s corrigendum: the hours from its lock to its closing beside b766`s 4.59; and the number of its lettered defects tagged REPEAT whose class is a key of (5) that this act`s bank reads REPAIRED, wanted 0.' % (
             r10h_, __import__('standing.cadence', fromlist=['VERSION']).VERSION, K.STANDING_VERSION, ' ; '.join(r10p_),
             pd_('(7) reference+save'), pd_('(7) restore'), f['disp_ef'], took7_, pw_('(9)(b)'), f['it_secs'],
             sti_('REPAIRED'), sti_('READ AS DESIGNED'), sti_('REMOVED'), len(rs_['CARRIED'])), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the repairs and the yield read the close two ways -- the repairs by the faults that two rulings carried, each now with a control that reads it, and the yield by the standing arms that read a fault at none of ten acts -- so that a step can be struck by what it yields and a guard kept by what it catches; the runner`s trial reads whether a dispatch of the kernel can take its own build from a cache, the centre`s proof being priced in dispatches; and the finite part of (9)(b) sets the archimedean term in the form the lemma of [L-i] states, the step the readings of (9)(c) lean on. Each is a statement about the record, its tools or the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(14), as the author answers the one question at the root: the proof of the control`s failure from its coefficients in the reading the table of (9)(c) prices cheapest by its upper figure, %s, opened by the trial of (7) where carried; or the registration H-ONSET-DENSITY, with W-ORD-ADMISSIBLE-CONE joined to it by [A2] of (R376); or the reading of the eighteen named premises under W-ORD-PREMISE-POSITIONS; or another the author names; the %d standing arms of (6) that read a fault at none of ten acts printed beside the question for the author`s strike. '
         'W-ORD-LI-ARITH carried with its four readings priced; W-ORD-IMP2-TAU %s; W-ORD-RUNNER-CACHE %s; the orders of (8) not built carried by name with their prices. Orders open after the act: %d (relay data/b767_orders.txt); push-b767-runner and the four push-b766-* branches of SIDE-explicit-formula kept for the next act`s step zero; the draft held at v5.' % (
             K.NEXT_ACT, f['pr_cheapest'], f['y_arms'][2], 'restated by [M1]' if held_ else 'carried by [M2]', 'discharged by [C2]' if xk_ == 'C2' else 'carried by [C3]', f['ord_head'][1]), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


# ### b767: the dispatch items of tools/b767_controls.py (ITEMS) by their price rows, for (9)'s "the price table's figures beside what each
# ### item took"; the rows of (4)(d) not sent printed with their price and no dispatch
ITEM_ROWS = (('b', '(4)(b)'), ('c', '(4)(c) theorems'), ('d-k', '(4)(d) K values'), ('d-pole', '(4)(d) pole term'), ('d-arch', '(4)(d) archimedean'),
             ('closing', '(4) closing build'), ('repeat', '(4) closing build'))
ITEM_PRICE_ORDER = ('(4)(b)', '(4)(c) theorems', '(4)(d) K values', '(4)(d) pole term', '(4)(d) archimedean', '(4)(d) enclosures', '(4)(d) inequality',
                    '(4)(d) closing', '(4) closing build')


def _row_raises():
    """the rows of (4)(d) raised by the author's words (data/b767_author_words_preseal.txt :23, :26), read from the dispatch tool's own
    ROW_RAISES line (tools/b767_controls.py) as committed, by its text and not by an import; refused where the line is not one dict."""
    import ast
    t_ = g(ROOT, 'show', 'HEAD:tools/b767_controls.py')
    m_ = re.search(r'(?m)^ROW_RAISES = (\{[^\n]+\})$', t_)
    if not m_:
        sys.exit('### tools/b767_controls.py AT HEAD CARRIES NO ROW_RAISES LINE -- NOTHING COMPOSED')
    return ast.literal_eval(m_.group(1))


def _stops():
    """(R377)(4) and the author's word at data/b767_author_words_preseal.txt :32: the closing build from source and its repeat, each stopped
    under the hold, by their read rows (data/b767_dispatch_rows.json: build and run minutes, the runner's lowest free memory, the axioms
    file's lines and sha256) and by the events bank's rows (94) and (97), which read their build logs (the jobs built of the jobs, the
    seconds of Coeffs and KData in each, the Window files built in neither), each matched over the bank's text with its line ends read as
    spaces, refused where a matcher does not find its figure once. Returns a dict."""
    ev_ = ' '.join(rdn('%s_events.txt' % ACT).split())
    jobs_ = re.findall(r'(\d[\d,]*) of (\d[\d,]*) jobs built', ev_)
    c94_ = re.findall(r'Coeffs \((\d+) s\), KData \((\d+) s\)', ev_)
    c97_ = re.findall(r'Coeffs (\d+) s here, (\d+) s there; KData (\d+) s and (\d+) s', ev_)
    nei_ = re.findall(r'((?:\w+, )+\w+ and \w+) built in neither', ev_)
    if len(jobs_) != 2 or jobs_[0] != jobs_[1] or len(c94_) != 1 or len(c97_) != 1 or len(nei_) != 1 or c97_[0][1] != c94_[0][0] or c97_[0][3] != c94_[0][1]:
        sys.exit('### THE EVENTS BANK`S ROWS (94) AND (97) DO NOT CARRY THE TWO BUILD LOGS` FIGURES ONCE EACH -- NOTHING COMPOSED')
    return dict(jobs=jobs_[0], coeffs=(c94_[0][0], c97_[0][0]), kdata=(c94_[0][1], c97_[0][2]), neither=nei_[0])


def _step_hours():
    """(R377)(9): the hours of the step rows summed by component, as a table -- the act's step rows of every repository
    (data/b767_steps.json) in the order of their commit times, each row's span from the row before it given to its own phase, the opening
    row's span 0; the sum of the spans the hours from the opening row to the last. Returns ([(phase, rows, hours)], the total, the rows)."""
    sj_ = jl('%s_steps.json' % ACT) or {}
    rows_ = sorted((sj_.get('rows') if isinstance(sj_, dict) else sj_) or [], key=lambda r_: int(r_.get('ct') or 0))
    by_, order_ = {}, []
    for i_, r_ in enumerate(rows_):
        p_ = str(r_.get('phase') or '-')
        if p_ not in by_:
            by_[p_] = [0, 0.0]
            order_.append(p_)
        by_[p_][0] += 1
        by_[p_][1] += (int(r_['ct']) - int(rows_[i_ - 1]['ct'])) / 3600.0 if i_ else 0.0
    tot_ = (int(rows_[-1]['ct']) - int(rows_[0]['ct'])) / 3600.0 if rows_ else 0.0
    return [(p_, by_[p_][0], round(by_[p_][1], 2)) for p_ in order_], round(tot_, 2), len(rows_)


def _measure_b767(act=ACT):
    """(R376)(9), THE MEASURE: (i) the act's lettered defects tagged REPEAT whose class is a key that data/b764_repairs.txt or
    data/b765_repairs.txt reads REPAIRED, wanted 0 -- a REPEAT row counted where its own FOR THE MEASURE sentence reads "reads REPAIRED:
    COUNTED"; (ii) its lettered defects of the class clause (1) names, a carried constant, cap or predicate read with the meaning the
    previous ruling gave it -- a row counted where that sentence reads "clause (1)'s class ...: COUNTED" and not "not clause (1)'s class",
    beside b765's nine. Each row read by its own sentence (the defects bank's head, :6-:8), its line ends read as spaces. Returns (the
    REPEAT rows counted, the REPEAT rows, the clause (1) rows counted, the lettered rows), each by letter."""
    rows_ = re.split(r"(?m)^(?=    \([a-z]'*\) )", rdn('%s_defects.txt' % act).replace(chr(13), ''))
    rep_, cnt_, c1_, all_ = [], [], [], []
    for r_ in rows_:
        m_ = re.match(r"^    \(([a-z]'*)\) THE [A-Z ]+'S \[(?:CLAIM|CLOSE) ; (NEW|REPEAT)\b", r_)
        if not m_:
            continue
        all_.append(m_.group(1))
        fm_ = re.search(r'FOR THE MEASURE: (.+?)(?: The defective step|$)', ' '.join(r_.split()))
        t_ = fm_.group(1) if fm_ else ''
        if m_.group(2) == 'REPEAT':
            rep_.append(m_.group(1))
            if re.search(r'reads REPAIRED: COUNTED\b', t_):
                cnt_.append(m_.group(1))
        if re.search(r"(?<!not )clause \(1\)'s class[^.;]*?: COUNTED\b", t_):
            c1_.append(m_.group(1))
    return cnt_, rep_, c1_, all_


def _measure(act=ACT):
    """(R376)(10), THE MEASURE OF (R375)(11): the act's lettered defects tagged REPEAT whose class is a key that data/b765_repairs.txt reads
    REPAIRED, wanted 0. Each REPEAT row read by its own FOR THE MEASURE sentence (the defects bank's head, :6-:7): counted where that sentence
    names a key's evidence that reads REPAIRED and the seat counts it in the measure; not where it reads no key's evidence. Returns the rows
    counted and the REPEAT rows read, by letter."""
    rows_ = re.split(r"(?m)^(?=    \([a-z]'*\) )", rdn('%s_defects.txt' % act).replace(chr(13), ''))
    rep_, cnt_ = [], []
    for r_ in rows_:
        m_ = re.match(r"^    \(([a-z]'*)\) THE [A-Z ]+'S \[(?:CLAIM|CLOSE) ; REPEAT ", r_)
        if not m_:
            continue
        rep_.append(m_.group(1))
        fm_ = re.search(r'FOR THE MEASURE: (.+?)(?: The defective step|$)', ' '.join(r_.split()))
        if fm_ and 'reads REPAIRED' in fm_.group(1) and "no key's evidence" not in fm_.group(1) and 'counts it in the measure' in fm_.group(1):
            cnt_.append(m_.group(1))
    return cnt_, rep_


def _ot_line(n, sha16):
    """the OPEN_TRAILS line at PLACE-papers HEAD at :n, refused unless its sha256 is the one the rulings tool's group entered
    (data/b766_ledgers_c2.json to data/b766_ledgers_c5.json)."""
    ls_ = g(PP, 'show', 'HEAD:OPEN_TRAILS.md').replace(chr(13), '').split(NL)
    l_ = ls_[n - 1] if 0 < n <= len(ls_) else ''
    if __import__('hashlib').sha256(l_.encode('utf-8')).hexdigest()[:16] != sha16:
        sys.exit('### OPEN_TRAILS :%d AT HEAD IS NOT THE LINE THE LEDGERS ENTERED -- NOTHING COMPOSED' % n)
    return l_


ITEM_PROSE = {'b': 'L1, the prime side as a finite sum', 'c': 'L2 to L5, the window in Lean', 'd-k': 'the K values row of L6 and L7',
              'd-pole': 'the pole term row of L8', 'd-arch': 'the archimedean row of L9', 'closing': 'the closing build from source', 'repeat': 'its one repeat'}
# ### b766 touch read (20:2xZ): each dispatch of (4)(d) named by the price row it was charged to, where 'L6 and L7, the K values and the
# ### values of cQ' stood beside dispatches 3 to 7, which built L6 alone (data/b766_events.txt (54)-(66)); the lemmas each built stand in [P2]
DATA_FILES = {'window_data': 'Coeffs.lean', 'kdata': 'KData.lean', 'cqdata': 'CQData.lean', 'poledata': 'PoleData.lean', 'poledata_rewrite': 'PoleData.lean rewritten',
              'k0data': 'ArchData.lean', 'k0blocks': 'ArchBlocks.lean'}


# ### b767, Component 4 (the Edit tool): the dispatch tool's items in words (tools/b767_controls.py ITEMS), each item's price row of
# ### data/b767_price.json, and each priced row's span by the act's step rows (data/b767_steps.json, by number in the bank's order, from the
# ### row before its first commit to its last; steps767r.py, 19:31:58Z), read for (R377)(10)'s "the price table's figures beside what each
# ### item took"; L9's work and L10's and L11's interleaved, so L9's row reads two spans
ITEM_PROSE7 = {'trial-on': 'the trial with the restore on', 'trial-off': 'the trial from source by route (i)', 'b': 'L9’s remainder',
               'c': 'L10, the enclosures', 'd': 'L11’s parts', 'e': 'L12, the closing theorem', 'closing': 'the closing build from source',
               'repeat': 'its repeat'}
ITEM_PRICE7 = {'trial-on': '(5)(c) trial', 'trial-off': '(5)(c) trial', 'b': '(4)(b) L9`s remainder', 'c': '(4)(c) L10', 'd': '(4)(d) L11',
               'e': '(4)(e) L12', 'closing': '(4) closing build', 'repeat': '(4) closing build'}
TOOK_SPANS7 = {'(1)': ((5, 8),), '(8) [K25]': ((8, 12),), '(4)(a) plan': ((13, 16),), '(5)(a) read': ((16, 19),), '(6)': ((19, 23),),
               '(7)': ((23, 26),), '(4) branch and tool': ((26, 32),), '(4)(b) L9`s remainder': ((32, 40), (51, 60)), '(4)(c) L10': ((40, 43),),
               '(4)(d) L11': ((43, 51),)}
TOOK_NOTES7 = {'(4)(a) plan': 'the stop of data/b767_events.txt (48), 1.39 h, among them',
               '(4) branch and tool': 'the frontier read again and route (i) written in the workflow among them (data/b767_events.txt (59), (60))',
               '(5)(a) read': 'with (5)(b), the route stated in the same bank'}


def _measure_r377(act=ACT):
    """(R377)(10), THE MEASURE: (i) the act's lettered defects tagged REPEAT whose class is a key that data/b765_repairs.txt or
    data/b766_repairs.txt reads REPAIRED, wanted 0 -- a REPEAT row counted where its own FOR THE MEASURE sentence names a key reading
    REPAIRED and not "no key's evidence"; (ii) its lettered defects of the class a carried constant read with its previous meaning -- a row
    counted where that sentence names "the class of a carried constant" and not "not the class of a carried constant", beside b766's three.
    Each row read by its own sentence (the defects bank's head, :6-:8), its line ends read as spaces; a lettered row with no such sentence
    refused. Returns (the REPEAT rows counted, the REPEAT rows, the carried-constant rows, the lettered rows), each by letter."""
    rows_ = re.split(r"(?m)^(?=    \([a-z]'*\) )", rdn('%s_defects.txt' % act).replace(chr(13), ''))
    rep_, cnt_, cc_, all_ = [], [], [], []
    for r_ in rows_:
        m_ = re.match(r"^    \(([a-z]'*)\) THE [A-Z ]+'S \[(?:CLAIM|CLOSE) ; (NEW|REPEAT)\b", r_)
        if not m_:
            continue
        all_.append(m_.group(1))
        fm_ = re.search(r'FOR THE MEASURE: (.+?)(?: The defective step|$)', ' '.join(r_.split()))
        if not fm_:
            sys.exit('### DEFECT (%s) CARRIES NO FOR THE MEASURE SENTENCE -- NOTHING COMPOSED' % m_.group(1))
        t_ = fm_.group(1)
        if m_.group(2) == 'REPEAT':
            rep_.append(m_.group(1))
            if 'reads REPAIRED' in t_ and "no key's evidence" not in t_:
                cnt_.append(m_.group(1))
        if re.search(r'(?<!not )the class of a carried constant', t_):
            cc_.append(m_.group(1))
    return cnt_, rep_, cc_, all_


def _finding_text_b767(f, S, rep, tot):
    """b767's paragraphs over b767's objects ((R377)(1)-(13)): every figure from a bank's foot or line as _figs reads it, each outcome by the
    groups' entered lines read at PLACE-papers HEAD by their digests (_ot_line), nothing typed but the ruling's own words; (10)'s report
    from the step rows, the dispatch rows and the price table, the measure's figures beside it read from the ferry's :47; every possessive
    the typographic apostrophe, a backtick only in a pair; the entry's last line the INTEGRATION line of (10). b766's form stands below as
    _finding_text_b766_form, not called. (b767, Component 4, the Edit tool.)"""
    from collections import Counter as _Cn
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    r10h_, _r10p = _report10()
    rs_, le_ = f['rep_states'], f['led_entered']
    if any(k_ not in le_ for k_ in ('S1', 'G1', 'R1', 'A2', 'P2', 'S2')) or any(k_ in le_ for k_ in N3_NOT_ENTERED):
        sys.exit('### THE GROUPS DO NOT CARRY THIS ACT`S ENTERED LINES, [P2] THE PROOF`S OUTCOME AND [S2] THE TRIAL`S -- NOTHING COMPOSED')
    ln_ = lambda k_: ('OPEN_TRAILS :%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and str(a_) == '1') else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    ap_ = lambda s_: str(s_).replace('`', '’')
    cm_ = lambda x_: '{:,}'.format(int(x_)) if (isinstance(x_, (int, float)) and float(x_).is_integer()) or str(x_).isdigit() else str(x_)
    sti_ = lambda s_: '%d %s (%s)' % (len(rs_[s_]), s_.lower(), ', '.join(rs_[s_]) or 'none')
    # ### (10)'s measure: b766's and b765's hours and b766's count of the carried-constant class, the ruling's own figures at the ferry's :47
    m10_ = re.search(r"beside b766's ([\d.]+) and b765's ([\d.]+);.*?beside b766's (\w+)\.", (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * 47)[46])
    if not m10_:
        sys.exit('### THE FERRY`S :47 DOES NOT CARRY THE MEASURE`S TWO HOURS AND b766`S COUNT -- NOTHING COMPOSED')
    # ### [P2] and [S2] at HEAD by their digests: the commit, what compiled and what was not sent; the route, the run, the low, the restored run
    p2m_ = re.search(r"compiled at (\w+) on push-b767-proof: (.+); the step that did not compile, or was not sent within the hours of \(3\): (.+), "
                     r"(not sent|[^;,]+); the proof continues there\.", _ot_line(*le_['P2']))
    if not p2m_ or p2m_.group(1)[:8] != (K.RUNNER_COMMIT or '-')[:8]:
        sys.exit('### OPEN_TRAILS`S [P2] AT HEAD DOES NOT CARRY THE CLOSING LEAN COMMIT -- NOTHING COMPOSED')
    s2m_ = re.search(r"by (.+?) the build from source at (\w+) exits 0, run (\d+), its low ([\d,]+) MB against the hold.s 2,560, and prints the axioms file of "
                     r"the restored run (\d+), sha256 (\w+); the closing build takes this route\.", _ot_line(*le_['S2']))
    if not s2m_:
        sys.exit('### OPEN_TRAILS`S [S2] AT HEAD DOES NOT CARRY ITS ROUTE, ITS RUNS AND ITS DIGEST -- NOTHING COMPOSED')
    g_ = dict((x_['group'], x_) for x_ in f['led_groups'])
    j2_ = jl('%s_ledgers_c2.json' % ACT) or {}
    el2_ = j2_.get('entry_lines') or {}
    e5_ = (jl('%s_ledgers_c5.json' % ACT) or {}).get('e0') or []
    axn_ = {'[]': 'no axiom', '[propext, Classical.choice, Quot.sound]': 'the standard three'}
    gr5_ = ' and '.join('%s %d' % (k_, v_) for k_, v_ in sorted(_Cn(str(x_.get('grade')) for x_ in e5_).items()))
    ax5_ = ', '.join('%s %d' % (axn_.get(k_, k_), v_) for k_, v_ in sorted(_Cn(str(x_.get('axioms')) for x_ in e5_).items(), key=lambda kv_: -kv_[1]))
    runs_ = sorted(f['runs'], key=lambda r_: r_['n'])
    ru_ = lambda it_: [r_ for r_ in runs_ if r_['item'] == it_]
    t_on_, t_off_ = (ru_('trial-on') or [None])[0], (ru_('trial-off') or [None])[0]
    if not t_on_ or not t_off_ or t_off_['restore'] != 'off' or str(t_off_['exit']) != '0' or t_off_['ax_sha'] != t_on_['ax_sha'] or str(t_off_['run']) != s2m_.group(3):
        sys.exit('### THE DISPATCH ROWS DO NOT CARRY THE TRIAL PAIR AS [S2] READS IT -- NOTHING COMPOSED')
    cl_ = ru_('closing') + ru_('repeat')
    if not cl_ or any(r_['restore'] != 'off' for r_ in cl_):
        sys.exit('### THE DISPATCH ROWS DO NOT CARRY THE CLOSING BUILD FROM SOURCE WITH THE RESTORE OFF -- NOTHING COMPOSED')
    last_on_ = next((r_ for r_ in reversed(runs_) if r_['restore'] == 'on' and str(r_['exit']) == '0' and r_['sha'][:8] == (K.RUNNER_COMMIT or '-')[:8]), None)
    if not last_on_:
        sys.exit('### NO RESTORED RUN READ EXIT 0 AT THE CLOSING LEAN COMMIT -- NOTHING COMPOSED')
    vs_ = lambda r_: 'exit 0' if r_['verdict'] == 'KERNEL' else 'exit %s, %s' % (r_['exit'], r_['verdict'] or 'not read')
    dfr_ = [x_ for x_ in re.split(r"(?m)^(?=    \([a-z]'*\) )", rdn('%s_defects.txt' % ACT).replace(chr(13), '')) if re.match(r"^    \([a-z]'*\) ", x_)]
    dl_ = lambda run_: ', '.join('(%s)' % re.match(r"^    \(([a-z]'*)\)", x_).group(1) for x_ in dfr_ if str(run_) in ' '.join(x_.split()))
    lw_ = lambda x_: cm_(x_) if x_ is not None else '-'
    p1_ = lambda r_: (', route (i)’s part one %s modules, its exit %s, the lows %s and %s MB' % (r_['p1_mods'], r_['p1_exit'], lw_(r_['low_p1']), lw_(r_['low_p2']))) if r_['p1_exit'] is not None else ''
    rnw_ = '; '.join('dispatch %d, run %s, %s at %s, the restore %s%s, %s%s, build %s min and run %s min, the runner’s low %s MB%s' % (
        r_['n'], r_['run'], ITEM_PROSE7.get(r_['item'], r_['item']), r_['sha'], r_['restore'], (' by %s' % r_['kind']) if r_['restore'] == 'on' and r_['kind'] else '',
        vs_(r_), (' (defect %s)' % dl_(r_['run'])) if r_['verdict'] != 'KERNEL' and dl_(r_['run']) else '',
        '-' if r_['build_min'] is None else r_['build_min'], '-' if r_['run_min'] is None else r_['run_min'], lw_(r_['low_mb']), p1_(r_)) for r_ in runs_)
    # ### main and the tag, by the worklist's EF_MAIN and WEIL_TAG as set after the gated push and the tag's read-back, or the group c6 line
    if K.WEIL_TAG and K.EF_MAIN[:8] == (K.RUNNER_COMMIT or '-')[:8]:
        mw_ = 'main moved to %s by the gated push and %s cut there after main’s read-back' % (K.EF_MAIN[:8], K.WEIL_TAG[0])
    else:
        mw_ = 'main not moved and no tag cut, %s' % ('[C7] at %s' % ln_('C7') if 'C7' in le_ else '[C8] at %s' % ln_('C8') if 'C8' in le_ else 'by the dispatch tool’s reading')
    # ### the price beside what each item took: the step rows' spans of TOOK_SPANS7 and the dispatches charged to each row
    sj_ = jl('%s_steps.json' % ACT) or {}
    srows_ = (sj_.get('rows') if isinstance(sj_, dict) else sj_) or []

    def _span_(a_, b_):
        if not (0 < a_ <= len(srows_) and 0 < b_ <= len(srows_)):
            sys.exit('### THE STEP ROWS DO NOT HOLD STEP %d OR %d OF A PRICED SPAN -- NOTHING COMPOSED' % (a_, b_))
        return (int(srows_[b_ - 1]['ct']) - int(srows_[a_ - 1]['ct'])) / 3600.0, str(srows_[a_ - 1]['commit'])[:8], str(srows_[b_ - 1]['commit'])[:8]
    took_, past_ = [], []
    for pk_, pr_ in f['pr_rows'].items():
        rr_ = [r_ for r_ in runs_ if ITEM_PRICE7.get(r_['item']) == pk_]
        lo_, hi_, dlo_, dhi_ = float(pr_['lo_h']), float(pr_['hi_h']), int(pr_['dispatches'][0]), int(pr_['dispatches'][1])
        sp_ = [_span_(a_, b_) for a_, b_ in TOOK_SPANS7.get(pk_, ())]
        h_ = sum(x_[0] for x_ in sp_)
        parts_ = []
        if sp_:
            parts_.append('%.2f h by the step rows (%s)%s' % (h_, ', '.join('%s to %s' % (x_[1], x_[2]) for x_ in sp_), (', ' + TOOK_NOTES7[pk_]) if pk_ in TOOK_NOTES7 else ''))
            if h_ > hi_:
                past_.append('%s %.2f h against %.2f h' % (ap_(pk_), h_, hi_))
        if pk_ == '(6)':
            parts_.append('the window bank’s own %s h from the registration’s commit' % f['win_hours'])
        if rr_:
            parts_.append('%d dispatch%s (%s), %s minutes of run' % (len(rr_), '' if len(rr_) == 1 else 'es', ', '.join(str(r_['n']) for r_ in rr_),
                                                             round(sum(float(r_['run_min'] or 0) for r_ in rr_), 1)))
            if len(rr_) > dhi_:
                past_.append('%s %d dispatches against %d' % (ap_(pk_), len(rr_), dhi_))
        if pk_ == '(5)(b) route':
            parts_.append('within the span of (5)(a), the route stated in the read’s bank')
        elif pk_ == '(4) main':
            parts_.append(mw_)
        elif pk_ == 'close':
            parts_.append('read in the closing message, the close coming after this entry')
        elif not parts_:
            parts_.append('not sent')
        took_.append('%s priced %s over %s, took %s' % (ap_(pk_), rg_('%.2f' % lo_, '%.2f' % hi_, 'h'), rg_(dlo_, dhi_, 'dispatches'), '; '.join(parts_)))
    sh_, sht_, shn_ = _step_hours()
    cnt_, repl_, cc_, all_ = _measure_r377()
    kl_ = lambda x_: ', '.join('[%s] at :%d' % (k_, x_['entered'][k_][0]) for k_ in sorted(x_['entered'], key=lambda k2_: x_['entered'][k2_][0]))
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
    cl2_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl2_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl2_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)
    on_max_ = dict(K.MAX_DISPATCHES_KINDS)['restore']
    c6_ = os.path.exists(os.path.join(ROOT, 'data', '%s_ledgers_c6.txt' % ACT))
    tg_ = ('%s cut at %s under (4) after main’s read-back, no other tag cut or moved' % (K.WEIL_TAG[0], K.EF_MAIN[:8])) if K.WEIL_TAG else 'no tag cut or moved, v0.45 not cut'
    cf_ = f['cert_forms']
    e = ['', _title(), '',
         'The plan amended and the combination’s three forms banked with their controls as wanted; the proof in part, [P2] at %s: compiled at %s on push-b767-proof: %s; not '
         'sent within the hours of (3): %s. The build from source given its order, [S1] at %s, its route held at the trial, [S2] at %s; the closing build from source at %s: %s. '
         'The window at knots graded by octave registered and computed with no dispatch, H-GRADED-WINDOW %s, [%s] at %s. The author’s rulings of 2026-11-22 and 2026-11-23 entered, '
         '[R1] and [A2]. Every build a runner dispatch read by its run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b767_dispatch_rows.json); no lean process on '
         'this host.' % (
             ln_('P2'), p2m_.group(1)[:8], p2m_.group(2), p2m_.group(3), ln_('S1'), ln_('S2'), (K.RUNNER_COMMIT or '-')[:8], mw_, f['win_reading'], f['win_key'], ln_(f['win_key']),
             f['disp_ef']), '',
         '*Filed at b767 on the author’s ruling `(R377)`; %d question%s put before the root%s. Banks: relay `data/b767_misses.txt`, `data/b767_price.txt`, `data/b767_ceiling.txt`, '
         '`data/b767_corrigendum.txt`, `data/b767_repairs.txt`, `data/b767_repair_controls.txt`, `data/b767_standing_dry.txt`, `data/b767_kernel_bases.json`, '
         '`data/b767_certificate.json`, `data/b767_certificate.txt`, `data/b767_plan.txt`, `data/b767_source_build.txt`, `data/b767_registration.txt`, `data/b767_window.txt`, '
         '`data/b767_window.json`, `data/b767_controls_control.txt`, `data/b767_dispatch_rows.json`, `data/b767_controls.txt`, `data/b767_logdata.txt`, `data/b767_natdata.txt`, '
         '`data/b767_ledgers_c2.txt`, `data/b767_ledgers_c5.txt`, %s`data/b767_orders.txt`, `data/b767_reproduce.txt`, `data/b767_author_answers.txt`, `data/b767_events.txt`, '
         '`data/b767_defects.txt`, `data/b767_prelock.txt`, `data/b767_pathrefusal.txt`, `data/b767_address_scan.txt`, `data/b767_touch.txt`, `data/b767_standing_figures.txt`, '
         '`data/b767_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's', (' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else '',
             '`data/b767_ledgers_c6.txt`, ' if c6_ else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record’s '
         'head line gives it; the relay’s main read back at %s after its closing push (relay data/b766_closing.txt, data/b766_scores_close.json). The corrigendum, short, in the form of b766’s: '
         'b766’s %s events, %s rows after its seal and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM '
         'items printed in full; what the seat found after b766’s lock entered as this act’s events (%s) to (%s) from the seat’s closing message, each with its time, CLAIM %s, CLOSE %s, '
         '%s; the navigator’s %d claims entered as the navigator’s, CLAIM, events (%s) to (%s), the navigator’s sums printed as the navigator’s; at FINDINGS :%s, the corrigenda bank '
         'appended at row (%s); no weight line (relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8),
             K.PRE_RELAY[:8], f['corr_events'], f['corr_postseal'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1],
             '%s repeat%s' % (f['corr_findings'][2], '' if str(f['corr_findings'][2]) == '1' else 's'), len(nr_), nr_[0], nr_[-1], f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The price and the ceiling** ((R377)(3)): the price table banked at step zero before Component 1, each item of (4) to (7) with its lines, its dispatches and its hours, each row '
         'priced beside what b766’s like row took, a build from source at %s minutes and a restored build at %s: step zero %s h, the lower sum %s h against the ceiling %d h from the '
         'opening row with %s h in reserve, the upper sum %s h; dispatches %s of at most %d, with the restore on %s of at most %d; the Lean %s lines; no step dispatch after %s (relay '
         'data/b767_price.txt). Read before the lock, read-only, at %s: %s h spent from the opening row, the last step dispatch at %s, %s h from the opening row; %s h left of %d, the '
         'reserve %d h; the close at b766’s %s h from its lock, %s h from the opening row: %s (relay data/b767_ceiling.txt). The seat’s read of what the ruling misses printed to the '
         'author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             *[(lambda m_: ('%s to %s' % (m_[0], m_[1]) if m_[0] != m_[1] else '%s' % m_[0]) if isinstance(m_, (list, tuple)) else '%s' % m_)(f['pr_minutes'][i_]) for i_ in (1, 0)],
             f['pr_step0'], f['pr_lower'], f['pr_ceiling'], cm_(f['pr_reserve']), f['pr_upper'], rg_(*f['pr_disp'], 'dispatches').rsplit(' ', 1)[0], f['pr_cap'],
             rg_(*f['pr_on'], 'dispatches').rsplit(' ', 1)[0], f['pr_oncap'], rg_(cm_(f['pr_lean'][0]), cm_(f['pr_lean'][1]), 'lines').rsplit(' ', 1)[0], f['pr_last'],
             f['ce_at'], f['ce_spent'], f['ce_last'], f['ce_last_h'], f['ce_left'], f['ce_ceiling'], f['ce_reserve'], f['ce_b766'], f['ce_close'], f['ce_word'].lower()), '',
         '**One key** ((R377)(8)), in Component 1 before the opening pass, with its planted control read at the commit before the repair and at the repair’s commit, both printed (relay '
         'data/b767_repairs.txt, data/b767_repair_controls.txt): tools/standing/ moved from %s to %s by %d commit, VERSION moved by it, the standing dry before it (relay '
         'data/b767_standing_dry.txt); %s, %s, %s and %d carried. %s' % (
             f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), sti_('REPAIRED'), sti_('READ AS DESIGNED'), sti_('REMOVED'), len(rs_['CARRIED']),
             ' '.join(ap_(r_['sentence']).rstrip('.') + '.' for r_ in f['reps'])), '',
         '**The plan amended and the certificate’s three forms, before any dispatch** ((R377)(4)(a)): tools/b767_certificate.py, importing tools/b766_certificate.py unedited and '
         'committed before its run, wrote the combination in three forms with no dispatch, its controls %d of %d as wanted: %s; the primes’ form’s one width %d digits, the integers’ %d, '
         'by parts at its least %d (order %d) (relay data/b767_certificate.txt, data/b767_certificate.json). No r, no K(n) and no coefficient printed. The plan, %d parts of the four '
         'lemmas b766 left in the order of sending, each in ordinary terms with its statement’s opening, its kind, the datum it consumes and its price, the budget in the Lean beside '
         'the certificate’s and the form L10 encloses with its reason, committed at relay %s before the first dispatch (relay data/b767_plan.txt): %s.' % (
             f['cert_ctl'][0], f['cert_ctl'][1], '; '.join('(%s) %s, %s constants, the sum of the |r| %s, the largest numerator %d digits, one width %d digits' % (
                 k_, w_, cm_(n_), s_, nd_, wd_) for k_, w_, n_, s_, nd_, wd_ in cf_),
             f['cert_widths'][0], f['cert_widths'][1], f['cert_widths'][2], f['cert_widths'][3], len(f['plan_lemmas']), f['plan_commit'],
             '; '.join('%s %s' % (l_, n_) for l_, n_ in f['plan_lemmas'])), '',
         '**The build from source given its order** ((R377)(5), under W-ORD-SOURCE-BUILD, entered by [S1] at %s with its entry line at :%s): (a) the read, no dispatch, by '
         'tools/b767_source_build.py committed before its run, from the artifacts of runs 45047352154 and 45051503982 and of run 45027497489 read as text: its controls %d of %d '
         'as wanted; (b) the route stated before its trial, (%s), %s; part one the target’s %d modules outside SIDEExplicitFormula/Window/ by name, their closure %d, a larger runner '
         'priced and not ordered (relay data/b767_source_build.txt); the workflow’s file changed on push-b767-proof alone, at %s. (c) The trial at that commit, beside the steps: '
         'dispatch %d with the restore on, run %s, %s, its axioms file sha256 %s; dispatch %d with the restore off, run %s, %s, build %s min, run %s min%s, its axioms file sha256 %s, '
         'equal: [S2] at %s, by %s, the closing build taking this route.' % (
             ln_('S1'), (el2_.get('S1') or ['-'])[0], f['sb_ctl'][0], f['sb_ctl'][1], f['sb_route'][0], f['sb_route'][1].lower(), f['sb_part1'][0], f['sb_part1'][1],
             (K.KERNEL_COMMITS[0][2] if K.KERNEL_COMMITS else '-')[:8], t_on_['n'], t_on_['run'], vs_(t_on_), t_on_['ax_sha'], t_off_['n'], t_off_['run'], vs_(t_off_),
             t_off_['build_min'], t_off_['run_min'], p1_(t_off_), t_off_['ax_sha'], ln_('S2'), s2m_.group(1)), '',
         '**The steps in Lean** ((R377)(4)(b)-(e), under W-ORD-LI-ARITH and W-ORD-WINDOW-CERTIFY): push-b767-proof cut from push-b766-proof at %s, which stays there; the dispatch tool '
         'tools/b767_controls.py committed before its opening dispatch, its controls %d of %d (relay data/b767_controls_control.txt); each dispatch of a step with the restore on, read '
         'by its run id from the downloaded artifact, the exit file governing, the restore’s kind recorded beside each run; the checks before each dispatch, each newly used Mathlib '
         'name found by a text search of the pinned Mathlib or printed, each data file opening with its imports, each kernel evaluation within the act’s cap. (b) L9’s remainder: %s. '
         '(c) L10, the enclosures, the table of the logarithms of the %s primes up to %s generated by tools/b767_logdata.py committed before its run, its controls %d of %d, the widest '
         'interval %s against 2/10^22, the series’ lengths the most %d and the sum %s: %s. (d) L11’s parts, the pole term’s data half and the logarithms of the integers to %s by '
         'tools/b767_natdata.py committed before its run, its controls %d of %d, %s factor pairs: %s. (e) L12: %s. [P2] at %s, by the rulings tool’s group c5: the %d theorems of '
         'SIDEExplicitFormula.Window at %s, each read at its statement by the E0 gate, %s, each compiled at dispatch %d with its axioms within the standard three (%s), sorryAx in none; '
         'their names in print_targets.txt (relay data/b767_ledgers_c5.txt).' % (
             K.WEIL_BRANCH_BASE[:8], f['cc_ctl'][0], f['cc_ctl'][1],
             ', '.join('dispatch %d %s%s' % (r_['n'], vs_(r_), (' (defect %s)' % dl_(r_['run'])) if r_['verdict'] != 'KERNEL' and dl_(r_['run']) else '') for r_ in ru_('b')) or 'not sent',
             cm_(f['ld_keys']), f['ld_upto'], f['ld_ctl'][0], f['ld_ctl'][1], f['ld_widest'], f['ld_most'], cm_(f['ld_sum']),
             ', '.join('dispatch %d %s' % (r_['n'], vs_(r_)) for r_ in ru_('c')) or 'not sent', f['nd_upto'], f['nd_ctl'][0], f['nd_ctl'][1], cm_(f['nd_pairs']),
             ', '.join('dispatch %d %s%s' % (r_['n'], vs_(r_), (' (defect %s)' % dl_(r_['run'])) if r_['verdict'] != 'KERNEL' and dl_(r_['run']) else '') for r_ in ru_('d')) or 'not sent',
             ', '.join('dispatch %d %s' % (r_['n'], vs_(r_)) for r_ in ru_('e')) or 'not sent', ln_('P2'), len(e5_), (K.RUNNER_COMMIT or '-')[:8], gr5_, last_on_['n'], ax5_), '',
         '**The closing build from source, main and the tag** ((R377)(4)): at the act’s closing Lean commit %s, the last at which a restored build read exit 0 (dispatch %d, run %s, '
         'its axioms file sha256 %s), built from source by route (i) with the restore off: %s. THE PAIR: %s. MAIN AND THE TAG: %s. So %s; the Lean on push-b767-proof at %s, cited by '
         'commit; push-b766-proof at %s; %s (relay data/b767_controls.txt, the tool’s controls %d of %d).' % (
             (K.RUNNER_COMMIT or '-')[:8], last_on_['n'], last_on_['run'], last_on_['ax_sha'],
             '; '.join('dispatch %d, run %s, %s, %s, build %s min, run %s min, the runner’s low %s MB%s, its axioms file %s' % (
                 r_['n'], r_['run'], ITEM_PROSE7.get(r_['item'], r_['item']), vs_(r_), '-' if r_['build_min'] is None else r_['build_min'],
                 '-' if r_['run_min'] is None else r_['run_min'], lw_(r_['low_mb']), p1_(r_), ('sha256 %s' % r_['ax_sha']) if r_['ax_sha'] else 'not printed') for r_ in cl_),
             ap_(f['tr_pair_line']), ap_(f['tr_main_line']), mw_, (K.RUNNER_COMMIT or '-')[:8], K.WEIL_BRANCH_B766[1][:8], tg_, f['tr_ctl'][0], f['tr_ctl'][1]), '',
         '**The window at knots graded by octave** ((R377)(6), the author’s answer at b766’s root): the registration committed alone at relay %s before the tool’s run (relay '
         'data/b767_registration.txt); tools/b767_window.py committed before its run, by exact piecewise integration in y; THE CONTROL first, the uniform window at M 16, d 3 printing %s '
         'to 10 digits and a planted coefficient read as a difference: %s; THE CELL, %d knots and %d coefficients: the control’s arithmetic side %s with its ball of radius %s %s, '
         'H-GRADED-WINDOW %s, [%s] at %s. REPORTED BESIDE IT, unregistered: %d coefficients; rational products %d; the combination’s primes %d and constants %d, the sum of the |r| %s; '
         'the budget’s one width %d digits; %s h from the registration’s commit against the price’s upper %s h (relay data/b767_window.txt; data/b767_window.json, %d coefficients as '
         'rationals, sha256 %s). No step of the proof moved to it; nothing computed at a zero; the window’s frequency read by name and printed nowhere.' % (
             f['win_reg'], f['win_uniform'], f['win_control'].lower(), f['win_knots'], f['win_ncoef'], f['win_S'], f['win_rad'],
             'below 0' if f['win_reading'] == 'HELD' else 'not below 0', f['win_reading'], f['win_key'], ln_(f['win_key']), f['win_ncoef'], f['win_products'], f['win_primes'],
             f['win_constants'], f['win_sumr'], f['win_digits'], f['win_hours'], f['win_upper'], f['win_json'][0], f['win_json'][1]), '',
         '**The rulings entered** ((R377)(7)), each by the author’s ratification of its clause, by the rulings tool’s group c2: [R1] at %s, the order W-ORD-NOVEMBER-RIDERS with its entry '
         'line at :%s, its trigger the act after [P1]; [A2] at %s, one line for (a), (b), (d) and (e); no line of ERRATA or of a paper written. The roster by tools/standing/orders.py’s '
         'rule: open %d before and %d after, %s added, none moving; at PLACE-papers HEAD orders %d, open %d, closed %d (relay data/b767_orders.txt). The two prices of (7)(d) are put '
         'at the root.' % (
             ln_('R1'), (el2_.get('R1') or ['-'])[0], ln_('A2'), f['led_roster'][0], f['led_roster'][1], ', '.join(f['led_roster'][2]) or 'none',
             f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The ledgers** ((R377)(4)-(7)): by tools/b767_rulings.py in %d groups, each committed before its run, OPEN_TRAILS’s bytes at HEAD a prefix of its new bytes at each, no line '
         'moving, each group’s bytes before the previous group’s after: %s (relay %s); REGISTRY, ERRATA, the census, the register and the two files of the map not written.' % (
             len(f['led_groups']), '; '.join('group %s, %s to %s lines, its head at :%s, %s, controls %d of %d%s' % (
                 x_['group'], cm_(x_['file'].get('lines_before')), cm_(x_['file'].get('lines_after')), (x_['head'] or ['-'])[0], kl_(x_), x_['ctl'][0], x_['ctl'][1],
                 (', the E0 gate %d of %d' % x_['e0']) if x_['e0'] else '') for x_ in f['led_groups']),
             ', '.join('data/b767_ledgers_%s.txt' % x_['group'] for x_ in f['led_groups'])), '',
         '**The research instruments reproduced** ((R377)(12), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py’s full run in the foreground, nothing else writing to '
         'tools/ or data/ while it ran, the rows of a bank of zeros that the run reads read by it and by nothing else: rows %d, reproducing %d, differing %d, not run %d (%s), the planted '
         'controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its '
         'banks at %s; then, by time, %s; tools/standing/ moved by the commit of (8) alone, from %s to %s, VERSION moved by it, with its planted control; each act tool committed before '
         'its run; the plan committed before any dispatch and the registration of (6) before the tool’s run at graded knots; the kernel’s %d commits on push-b767-proof by the one-call '
         'tool and their pushes by the gated push, each capture masked; the kernel’s main moved under (4) and at no other time; the per-commit scan at every commit; the pre-lock '
         'comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt); the Project set built at the close from the '
         'close’s own export by [K24].' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (ap_(K.CHAIN_WORDS.get(k_, k_)), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), f['st_entering'], f['st_version'], len(K.KERNEL_COMMITS)), '',
         '**What this act is not** ((R377)(12)): nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula; no push forced; %s, v0.38 to v0.44 and v0.2.0 '
         'peeling as before; no kernel branch removed, push-b766-proof kept at %s; no sentence of any paper written or edited; REGISTRY, ERRATA, the census, the register and the two '
         'files of the map not written, FINDINGS and OPEN_TRAILS the two files of PLACE-papers written; nothing fetched from the web by the seat; nothing computed at a zero, the '
         'window’s frequency read by name and printed nowhere, the reproduction run’s rows of a bank of zeros read by it alone; no lean process on this host; no byline; the draft '
         'held at v5.' % (tg_, K.WEIL_BRANCH_B766[1][:8]), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel’s commits among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (10)**: the hours by the step rows: %s (the closing comes after this entry and its row is printed in the closing message). The step rows summed by component, each '
         'row’s span from the row before it given to its own phase, the act’s step rows of every repository to this entry (relay data/b767_steps.json):' % r10h_, '',
         '| component | step rows | hours |', '| --- | ---: | ---: |'] + ['| %s | %d | %.2f |' % (p_, n_, h_) for p_, n_, h_ in sh_] + ['| all | %d | %.2f |' % (shn_, sht_), ''] + [
         'Each dispatch by its run id, its kind and its minutes: %s (relay data/b767_dispatch_rows.json). The price table’s figures beside what each item took: %s (relay '
         'data/b767_price.txt, data/b767_steps.json); the rows past their upper figure: %s, printed and asking no question ((R377)(3)). The last step dispatch at %s, the hour of (3) '
         '%s; the hours from it to the closing printed in the closing message. THE MEASURE, read at this act’s close: the hours from the lock to the closing, beside b766’s %s and '
         'b765’s %s, printed in the closing message; the lettered defects tagged REPEAT whose class is a key that data/b765_repairs.txt or data/b766_repairs.txt reads REPAIRED, %d of '
         'the %d tagged REPEAT (%s), wanted 0; the lettered defects of the class a carried constant read with its previous meaning, %d of %d (%s), beside b766’s %s; each row’s own '
         'sentence giving its reading (relay data/b767_defects.txt).' % (
             rnw_, '; '.join(took_), '; '.join(past_) or 'none', f['tr_last'], f['tr_last_hour'], m10_.group(1), m10_.group(2), len(cnt_), len(repl_),
             ', '.join('(%s)' % x_ for x_ in cnt_) or 'none', len(cc_), len(all_), ', '.join('(%s)' % x_ for x_ in cc_) or 'none', m10_.group(3)), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the certificate’s three forms and the Lean of L10 read the one combination two ways, the forms’ widths outside Lean and the '
         'enclosures’ widths checked by kernel reduction, so that the form the plan chose is the one the Lean encloses; the window at graded knots reads the same arithmetic side at 157 '
         'coefficients beside 16,365, by the same exact route, its control the uniform window’s banked value; the trial and the closing build from source read what a restored build '
         'does not, the kernel with the Window files built under the runner’s hold. Each is a statement about the record, its tools or the Epstein zeta function of x^2 + xy + 6y^2, '
         'promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(13), as the author answers the one question at the root: where [P1] stands, the registry’s block and the map’s merge under the author’s strikes, '
         'W-ORD-NOVEMBER-RIDERS, and The Epstein Control Object brought to the deposit rubric with the proof in it; where [P2] stands, the act after this one continues the proof at the '
         'step that did not compile or was not sent, %s; or another the author names; printed beside it for the author’s ruling, the outcome of (6) with its reported figures and '
         'prices, the two prices of (7)(d)%s and the three forms of the combination with their digits. W-ORD-LI-ARITH carried by [P2]; W-ORD-WINDOW-CERTIFY open; W-ORD-SOURCE-BUILD '
         'entered by [S1], its route held by [S2]; W-ORD-NOVEMBER-RIDERS entered by [R1]. Orders open after the act: %d (relay data/b767_orders.txt); push-b767-proof at %s at the '
         'kernel’s remote and in its clone, push-b766-proof at %s, no kernel branch removed; the draft held at v5.' % (
             K.NEXT_ACT, p2m_.group(3).split(',')[0], ', the larger runner’s price' if ('S3' in le_ or 'C8' in le_) else '', f['ord_head'][1], (K.RUNNER_COMMIT or '-')[:8],
             K.WEIL_BRANCH_B766[1][:8]), '',
         '**Next.** %s.' % ap_(K.next_line()), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b766_form(f, S, rep, tot):
    """b766's paragraphs over b766's objects ((R376)(1)-(12), the author's three words of 2026-11-22 and word of 2026-11-21 on the deposits
    and the keystones, and the four words of the act at data/b766_author_words_preseal.txt :23, :26, :29 and :32): every figure from a
    bank's foot or line as _figs reads it, each outcome by the four groups' entered lines read at PLACE-papers HEAD by their digests
    (_ot_line), nothing typed but the ruling's own words; (9)'s report from the step rows, the dispatch rows and the price table, the
    measure's figures beside it read from the ferry's :40; every possessive the typographic apostrophe, a backtick only in a pair; the
    entry's last line the INTEGRATION line of (9). b765's form, carried, stands below as _finding_text_b766_carried, not called."""
    from collections import Counter as _Cn
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    r10h_, _r10p = _report10()
    rs_, le_ = f['rep_states'], f['led_entered']
    if 'P2' not in le_ or any(k_ in le_ for k_ in N3_NOT_ENTERED) or any(k_ not in le_ for k_ in ('E1', 'F1', 'F2', 'M4', 'H5', 'A1', 'X1', 'X2', 'X3')):
        sys.exit('### THE FOUR GROUPS DO NOT CARRY THIS ACT`S ENTERED LINES, [P2] THE PROOF`S ONE OUTCOME -- NOTHING COMPOSED')
    ln_ = lambda k_: ('OPEN_TRAILS :%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    pw_ = lambda k_: rg_('%.2f' % float(f['pr_rows'][k_]['lo_h']), '%.2f' % float(f['pr_rows'][k_]['hi_h']), 'h')   # ### b766 touch read: two places, as the bank prints them
    pd_ = lambda k_: '%s over %s' % (pw_(k_), rg_(f['pr_rows'][k_]['dispatches'][0], f['pr_rows'][k_]['dispatches'][1], 'dispatches'))
    sti_ = lambda s_: '%d %s (%s)' % (len(rs_[s_]), s_.lower(), ', '.join(rs_[s_]) or 'none')
    ap_ = lambda s_: str(s_).replace('`', '’')
    cm_ = lambda x_: '{:,}'.format(int(x_)) if isinstance(x_, (int, float)) or str(x_).isdigit() else str(x_)
    # ### (9)'s measure: b765's and b764's hours and b765's count of clause (1)'s class, the ruling's own figures at the ferry's :40
    m9_ = re.search(r"beside b766's ([\d.]+) and b764's ([\d.]+);.*?beside b766's (\w+)\.", (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * 40)[39])
    if not m9_:
        sys.exit('### THE FERRY`S :40 DOES NOT CARRY THE MEASURE`S TWO HOURS AND b766`S COUNT -- NOTHING COMPOSED')
    # ### [P2] at HEAD by its digest: the plan's count, the commit, the branch and the run, what compiled and what was not sent
    p2m_ = re.search(r"of the plan's (\d+) lemmas, compiled at (\w+) on (\S+) \(built by runner run (\d+) [^)]*\): (.+?); the step that did not compile, or was "
                     r"not sent under the ceiling: (.+?), not sent; the proof continues there\.", _ot_line(*le_['P2']))
    if not p2m_ or p2m_.group(2)[:8] != (K.RUNNER_COMMIT or '-')[:8] or int(p2m_.group(1)) != len(f['plan_lemmas']):
        sys.exit('### OPEN_TRAILS`S [P2] AT HEAD DOES NOT CARRY THE PLAN`S LEMMAS AT THE CLOSING LEAN COMMIT -- NOTHING COMPOSED')
    kc_ = dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS)
    g_ = dict((x_['group'], x_) for x_ in f['led_groups'])
    j2_ = jl('%s_ledgers_c2.json' % ACT) or {}
    e5_ = (jl('%s_ledgers_c5.json' % ACT) or {}).get('e0') or []
    axn_ = {'[]': 'no axiom', '[propext, Classical.choice, Quot.sound]': 'the standard three'}
    gr5_ = ' and '.join('%s %d' % (k_, v_) for k_, v_ in sorted(_Cn(str(x_.get('grade')) for x_ in e5_).items()))
    ax5_ = ', '.join('%s %d' % (axn_.get(k_, k_), v_) for k_, v_ in sorted(_Cn(str(x_.get('axioms')) for x_ in e5_).items(), key=lambda kv_: -kv_[1]))
    st_ = _stops()
    runs_ = sorted(f['runs'], key=lambda r_: r_['n'])
    off_ = [r_ for r_ in runs_ if r_['item'] in ('closing', 'repeat')]
    if len(off_) != 2 or any(r_['restore'] != 'off' or str(r_['exit']) != '143' or r_['ax_lines'] != 1 for r_ in off_) or off_[0]['ax_sha'] != off_[1]['ax_sha']:
        sys.exit('### THE DISPATCH ROWS DO NOT CARRY THE BUILD FROM SOURCE AND ITS REPEAT, EACH STOPPED WITH A ONE-LINE AXIOMS FILE -- NOTHING COMPOSED')
    last_on_ = next((r_ for r_ in reversed(runs_) if r_['restore'] == 'on' and str(r_['exit']) == '0'), None)
    vs_ = lambda r_: {'KERNEL': 'exit 0'}.get(r_['verdict'], 'exit %s, %s' % (r_['exit'], r_['verdict'] or 'not read'))
    dfr_ = [x_ for x_ in re.split(r"(?m)^(?=    \([a-z]'*\) )", rdn('%s_defects.txt' % ACT).replace(chr(13), '')) if re.match(r"^    \([a-z]'*\) ", x_)]
    dl_ = lambda run_: ', '.join('(%s)' % re.match(r"^    \(([a-z]'*)\)", x_).group(1) for x_ in dfr_ if str(run_) in ' '.join(x_.split()))
    ru_ = lambda it_: [r_ for r_ in runs_ if r_['item'] == it_]
    dd_ = '; '.join('%s, %s' % (ITEM_PROSE[it_], ', '.join('dispatch %d %s%s' % (r_['n'], vs_(r_), (' (defect %s)' % dl_(r_['run'])) if r_['verdict'] != 'KERNEL' and dl_(r_['run']) else '')
                                                           for r_ in ru_(it_))) for it_ in ('d-k', 'd-pole', 'd-arch'))
    rz_ = _row_raises()
    rnw_ = '; '.join('dispatch %d, run %s, %s at %s, the restore %s and its kind %s, %s, build %s min and run %s min, the runner’s low %s MB' % (
        r_['n'], r_['run'], ITEM_PROSE.get(r_['item'], r_['item']), r_['sha'], r_['restore'], r_['kind'] or 'unread', vs_(r_),
        '-' if r_['build_min'] is None else r_['build_min'], '-' if r_['run_min'] is None else r_['run_min'], cm_(r_['low_mb']) if r_['low_mb'] is not None else '-') for r_ in runs_)
    took_ = []
    for pk_ in ITEM_PRICE_ORDER:
        rr_ = [r_ for r_ in runs_ if r_['item'] in [it_ for it_, k_ in ITEM_ROWS if k_ == pk_]]
        hi_ = int(f['pr_rows'][pk_]['dispatches'][1])
        took_.append('%s priced %s%s, %s' % (pk_, pd_(pk_), (', raised to %d by the author’s words' % rz_[pk_]) if pk_ in rz_ else '', (
            '%d dispatch%s (%s), %s minutes of run, %s' % (len(rr_), '' if len(rr_) == 1 else 'es', ', '.join(str(r_['n']) for r_ in rr_),
                                                         round(sum(float(r_['run_min'] or 0) for r_ in rr_), 1),
                                                         ('the priced upper %d overrun by %d' % (hi_, len(rr_) - hi_)) if len(rr_) > hi_ else 'within the priced upper %d' % hi_))
            if rr_ else 'not sent'))
    sh_, sht_, shn_ = _step_hours()
    cnt_, repl_, c1_, all_ = _measure_b767()
    fd_ = re.search(r"cQ\(n\) is 0 exactly at (\d+) of the n from 2 to 1023 and not 0 at (\d+), where b766's ball loop counted (\d+)", ' '.join(rdn('%s_events.txt' % ACT).split()))
    if not fd_:
        sys.exit('### THE EVENTS BANK`S ROW (42) DOES NOT CARRY THE CERTIFICATE`S FINDING ON cQ -- NOTHING COMPOSED')
    q2_ = sorted(le_[k_][0] for k_ in le_ if k_.split('.')[0] == 'Q2')
    kl_ = lambda x_: ', '.join(('[Q2] x %d at :%d to :%d' % (len(q2_), q2_[0], q2_[-1])) if k_.split('.')[0] == 'Q2' else '[%s] at :%d' % (k_, x_['entered'][k_][0])
                               for k_ in sorted(x_['entered'], key=lambda k2_: x_['entered'][k2_][0]) if k_.split('.')[0] != 'Q2' or x_['entered'][k_][0] == q2_[0])
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
    cl_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)
    on_max_ = dict(K.MAX_DISPATCHES_KINDS)['restore']
    e = ['', _title(), '',
         'The certificate banked with its controls as wanted, [%s]; the prime side as a finite sum compiled, [F1]; the data file and the three theorems of the window in Lean compiled, [F2]; '
         'the proof in part, [P2]: of the plan’s %s lemmas, compiled at %s on %s: %s; not sent: %s (%s). The closing build from source at %s and its one repeat each stopped under the hold, '
         'the exit file 143 and no axioms print; main not moved and no tag cut; no [C7] line, by the author’s word of 2026-11-22 (relay data/b767_author_words_preseal.txt :32). '
         'Every build a runner dispatch read by its run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b767_dispatch_rows.json); no lean process on this host.' % (
             f['cert_key'], p2m_.group(1), p2m_.group(2)[:8], p2m_.group(3), p2m_.group(5), p2m_.group(6), ln_('P2'), (K.RUNNER_COMMIT or '-')[:8], f['disp_ef']), '',
         '*Filed at b767 on the author’s ruling `(R377)`, the author’s three words of 2026-11-22 and word of 2026-11-21 on the deposits and the keystones, and the author’s four words '
         'during the act (relay data/b767_author_words_preseal.txt :23, :26, :29, :32); %d question%s put before the root%s. Banks: relay `data/b767_misses.txt`, `data/b767_price.txt`, '
         '`data/b767_ceiling.txt`, `data/b767_author_words_preseal.txt`, `data/b767_corrigendum.txt`, `data/b767_repairs.txt`, `data/b767_repair_controls.txt`, `data/b767_standing_dry.txt`, '
         '`data/b767_capture_mask.txt`, `data/b767_kernel_bases.json`, `data/b767_certificate.json`, `data/b767_certificate.txt`, `data/b767_plan.txt`, `data/b767_controls_control.txt`, '
         '`data/b767_dispatch_rows.json`, `data/b767_controls.txt`, `data/b767_window_data.txt`, `data/b767_kdata.txt`, `data/b767_cqdata.txt`, `data/b767_poledata.txt`, '
         '`data/b767_poledata_rewrite.txt`, `data/b767_k0data.txt`, `data/b767_k0blocks.txt`, `data/b767_registry_cells.txt`, `data/b767_lean_join.txt`, `data/b767_sweep.txt`, '
         '`data/b767_ledgers_c2.txt`, `data/b767_ledgers_c3.txt`, `data/b767_ledgers_c4.txt`, `data/b767_ledgers_c5.txt`, `data/b767_orders.txt`, `data/b767_reproduce.txt`, '
         '`data/b767_author_answers.txt`, `data/b767_events.txt`, `data/b767_defects.txt`, `data/b767_prelock.txt`, `data/b767_pathrefusal.txt`, `data/b767_address_scan.txt`, '
         '`data/b767_touch.txt`, `data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's', (' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record’s '
         'head line gives it; the relay’s main read back at %s after its closing push (relay data/b766_closing.txt, data/b766_scores_close.json). The corrigendum, short, in the form of b766’s: '
         'b766’s %s events, %s rows after its seal and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM '
         'items printed in full; what the seat found after b766’s lock entered as this act’s events (%s) to (%s) from the seat’s closing message, each with its time, CLAIM %s, CLOSE %s, '
         '%s; the navigator’s own %d claims entered as the navigator’s, CLAIM, events (%s) to (%s); at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line '
         '(relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8),
             K.PRE_RELAY[:8], f['corr_events'], f['corr_postseal'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1],
             '%s repeat%s' % (f['corr_findings'][2], '' if str(f['corr_findings'][2]) == '1' else 's'), len(nr_), nr_[0], nr_[-1], f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The price and the ceiling** ((R377)(3)): the price table banked at step zero before Component 1, each item of (4) to (7) with its lines, its dispatches and its hours, a dispatch '
         'priced by its kind, a build from source at %s minutes and a restored build at %s, each as b766 banked it: step zero %s h, the lower sum %s h against %d h, %s, the upper sum %s h; '
         'dispatches %s of at most %d, with the restore on %s of at most %d; the Lean %s lines (relay data/b767_price.txt). Read again after (4)(c), read-only, at %s: %s h spent from the '
         'delivery and %s h of the rows left at their lower figures, %s h against %d h, under by %s h, %s (relay data/b767_ceiling.txt). The seat’s read of what the ruling misses printed '
         'to the author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             *[(lambda m_: ('%s to %s' % (m_[0], m_[1]) if m_[0] != m_[1] else '%s' % m_[0]) if isinstance(m_, (list, tuple)) else '%s' % m_)(f['pr_minutes'][i_]) for i_ in (1, 0)],
             f['pr_step0'], f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['pr_upper'], rg_(*f['pr_disp'], 'dispatches').rsplit(' ', 1)[0], K.MAX_DISPATCHES,
             rg_(*f['pr_on'], 'dispatches').rsplit(' ', 1)[0], on_max_, rg_(cm_(f['pr_lean'][0]), cm_(f['pr_lean'][1]), 'lines').rsplit(' ', 1)[0],
             f['ce_at'], f['ce_spent'], f['ce_left'], f['ce_sum'], f['ce_ceiling'], f['ce_under'], f['ce_word'].lower()), '',
         '**The three repairs** ((R377)(7)), in Component 1 before the opening pass, each with its planted control read at the commit before the repair and at the repair’s commit, both printed '
         '(relay data/b767_repairs.txt, data/b767_repair_controls.txt): tools/standing/ moved from %s to %s by %d commits, VERSION moved by each, the standing dry before each (relay '
         'data/b767_standing_dry.txt); %s, %s, %s and %d carried. %s The masking’s figures: files %d, the mask’s control %d of %d (relay data/b767_capture_mask.txt); the removal’s '
         'listing before and its absence after (relay data/b767_events.txt (37)).' % (
             f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), sti_('REPAIRED'), sti_('READ AS DESIGNED'), sti_('REMOVED'), len(rs_['CARRIED']),
             ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps']), f['mask'][0], f['mask_ctl'][0], f['mask_ctl'][1]), '',
         '**The plan and the certificate, banked as data before any dispatch** ((R377)(4)(a)): tools/b767_certificate.py, carried from tools/b766_window.py and committed before its run, read '
         'data/b766_window.json, its sha256 equal to data/b766_window.txt :26, and wrote the certificate: K(n) as exact rationals at the %d n from 2 to 1023 at which cQ(n) is not 0; k(0), '
         'the integral of H and the sum of the |c_j|; the arithmetic side as one combination of 1, Euler’s constant, log pi and the logarithms of %s primes, each coefficient an exact '
         'rational, its largest numerator %s digits; the budget %s constants in equal shares, one width for all of %s digits; its controls %d of %d as wanted, the planted numerator read as '
         'the one difference; %s, [%s] at %s (relay data/b767_certificate.json, data/b767_certificate.txt). A finding of the certificate: cQ(n) is 0 exactly at %s of the n from 2 to 1023 '
         'and not 0 at %s, where b766’s ball loop counted %s rational products, the %d that cancel exactly standing there as balls about 0 and adding nothing to its prime side (relay '
         'data/b767_events.txt (42)). The plan, %d lemmas in the order of sending, each with its kind, its datum and its price, committed with the certificate at relay %s before the first '
         'dispatch (relay data/b767_plan.txt): %s.' % (
             f['cert_k'], cm_(f['cert_primes']), f['cert_digits'], cm_(f['cert_budget'][0]), f['cert_budget'][1], f['cert_ctl'][0], f['cert_ctl'][1], f['cert_form'],
             f['cert_key'], ln_(f['cert_key']), fd_.group(1), fd_.group(2), fd_.group(3), int(fd_.group(3)) - int(fd_.group(2)), len(f['plan_lemmas']), f['plan_commit'],
             '; '.join('%s %s' % (l_, n_) for l_, n_ in f['plan_lemmas'])), '',
         '**The steps in Lean** ((R377)(4)(b)-(d), under W-ORD-LI-ARITH and W-ORD-WINDOW-CERTIFY): push-b767-proof cut from main at %s; the dispatch tool tools/b767_controls.py committed '
         'before its opening dispatch, its controls %d of %d (relay data/b767_controls_control.txt); each dispatch of a step with the restore on, read by its run id from the downloaded '
         'artifact, the exit file governing, the restore’s kind recorded beside each run by [H5]; each dispatched commit’s Window files read for a decimal literal and a barred word before '
         'its send, none refused; each data file written by a relay tool committed before its run and read back by its control (%s). (b) %s and its reading at cQ, of SIDE-explicit-formula '
         'at %s: compiled at dispatch %s, [F1] at %s. (c) The 16,365 coefficients in Coeffs.lean, its head naming the bank’s sha256, and the three theorems, at %s: compiled at dispatch %s, '
         '[F2] at %s; the E0 gate %d of %d before the two lines (relay data/b767_ledgers_c3.txt). (d) In the plan’s order: %s; each row raised by the author’s words where it reached its '
         'figure (relay data/b767_author_words_preseal.txt :23, :26). [P2] at %s, by the rulings tool’s group c5: the %d theorems of SIDEExplicitFormula.Window at %s, each read at its '
         'statement by the E0 gate, %s, each compiled at dispatch %s with its axioms within the standard three (%s), sorryAx in none (relay data/b767_ledgers_c5.txt).' % (
             K.EF_BASE[:8], f['cc_ctl'][0], f['cc_ctl'][1], '; '.join('%s %d of %d' % (DATA_FILES.get(n_, n_), a_, b_) for n_, a_, b_ in f['data_ctl']),
             f['plan_lemmas'][0][1], kc_.get('prime', '-')[:8], ', '.join(str(r_['n']) for r_ in ru_('b')), ln_('F1'),
             kc_.get('window', '-')[:8], ', '.join(str(r_['n']) for r_ in ru_('c')), ln_('F2'), (g_['c3']['e0'] or (0, 0))[0], (g_['c3']['e0'] or (0, 0))[1],
             dd_, ln_('P2'), len(e5_), (K.RUNNER_COMMIT or '-')[:8], gr5_, last_on_['n'] if last_on_ else '-', ax5_), '',
         '**The closing build from source and its repeat** ((R377)(4) and the author’s word of 2026-11-22, relay data/b767_author_words_preseal.txt :32): at the closing Lean commit %s, '
         'whose restored build exited 0 (dispatch %s, run %s), the build from source, dispatch %d, run %s, the restore off and nothing restored: build %s min, run %s min, the runner’s low '
         '%s MB, Coeffs %s s and KData %s s; its one repeat, dispatch %d, run %s: build %s min, run %s min, the runner’s low %s MB, Coeffs %s s and KData %s s; each stopped under the hold, '
         'the exit file 143, at %s of %s jobs, %s built in neither, each axioms file one line, sha256 %s (relay data/b767_dispatch_rows.json; data/b767_events.txt (94), (97)). THE FINDING, '
         'by the author’s word: a build from source with the Window files does not pass the hold, the two runs’ figures as above; b766’s closing build from source stopped and its repeat '
         'built, and here the stop recurred at the same job; the next ruling names its order and prices the closing build against it. THE PAIR: %s. MAIN AND THE TAG: %s; main stands at '
         '%s with %s on it, no tag cut; the Lean on push-b767-proof at %s, cited by commit, standing at the kernel’s remote and in its clone, no route removing it; no [C7] line written, '
         'no axioms file differing since the build from source printed none, W-ORD-RUNNER-CACHE as [C5] left it; the four dispatches with the restore on unspent (relay '
         'data/b767_controls.txt, the tool’s controls %d of %d).' % (
             (K.RUNNER_COMMIT or '-')[:8], last_on_['n'] if last_on_ else '-', last_on_['run'] if last_on_ else '-', off_[0]['n'], off_[0]['run'], off_[0]['build_min'], off_[0]['run_min'],
             cm_(off_[0]['low_mb']), st_['coeffs'][0], st_['kdata'][0], off_[1]['n'], off_[1]['run'], off_[1]['build_min'], off_[1]['run_min'], cm_(off_[1]['low_mb']),
             st_['coeffs'][1], st_['kdata'][1], st_['jobs'][0], st_['jobs'][1], st_['neither'], off_[0]['ax_sha'], ap_(f['tr_pair_line']), ap_(f['tr_main_line']),
             K.EF_MAIN[:8], K.WEIL_TAG_B765[0], (K.RUNNER_COMMIT or '-')[:8], f['tr_ctl'][0], f['tr_ctl'][1]), '',
         '**Three readings toward the keystone set** ((R377)(5)), each a reading and no build, under items (5) to (8) of the author’s word of 2026-11-21; no line of REGISTRY, of the census or '
         'of a paper written by them. (a) The registry’s rows, by tools/b767_registry_cells.py committed before its run: %s; its controls %d of %d (relay data/b767_registry_cells.txt); read '
         'after dispatch 7 had completed, where the clause names the slot while a dispatch runs (relay data/b767_defects.txt (i)); [X1] at %s. (b) The Lean joined to the papers, by '
         'tools/b767_lean_join.py committed before its run: %s; its controls %d of %d (relay data/b767_lean_join.txt); [X2] at %s. (c) The findings ledger against the keystones, the tool’s '
         'pass, by tools/b767_sweep.py committed before its run: %s; its controls %d of %d; [X3] at %s.' % (
             f['x1_fields'].rstrip('.'), f['x1'][4], f['x1'][5], ln_('X1'), f['x2_fields'].rstrip('.'), f['x2'][5], f['x2'][6], ln_('X2'),
             f['x3_fields'].rstrip('.'), f['x3'][7], f['x3'][8], ln_('X3')), '',
         '**The rulings entered** ((R377)(6)), each by the author’s ratification of its clause, by the rulings tool’s group c2: [M4] at %s, SPIRAL_MAP.md carrying the map, with the order '
         'W-ORD-MAP-MERGE’s entry line at :%s; [Q2] for the %d orders retired, each a hypothesis by design of the theorem its row names, at :%d to :%d; [H5] at %s, a restore hit by the '
         'author’s word, the kind recorded beside each run; [A1] at %s, the author’s word of 2026-11-21 on the deposits and the keystones placed; no line of the two files of the map written. '
         'The roster by tools/standing/orders.py’s rule: open %d before and %d after, %d moving OPEN to CLOSED, %s added; at PLACE-papers HEAD orders %d, open %d, closed %d (relay '
         'data/b767_orders.txt).' % (
             ln_('M4'), (j2_.get('entry_line') or ['-'])[0], len(q2_), q2_[0], q2_[-1], ln_('H5'), ln_('A1'), f['led_roster'][0], f['led_roster'][1],
             sum(1 for x_ in f['led_roster'][3] if list(x_[1:]) == ['OPEN', 'CLOSED']), ', '.join(f['led_roster'][2]) or 'none', f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The ledgers** ((R377)(4)-(6)): by tools/b767_rulings.py in four groups, each committed before its run, OPEN_TRAILS’s bytes at HEAD a prefix of its new bytes at each, no line '
         'moving, each group’s bytes before the previous group’s after: %s (relay data/b767_ledgers_c2.txt to data/b767_ledgers_c5.txt); REGISTRY, ERRATA, the census, the register and the '
         'two files of the map not written.' % '; '.join('group %s, %s to %s lines, its head at :%s, %s, controls %d of %d%s' % (
             x_['group'], cm_(x_['file'].get('lines_before')), cm_(x_['file'].get('lines_after')), (x_['head'] or ['-'])[0], kl_(x_), x_['ctl'][0], x_['ctl'][1],
             (', the E0 gate %d of %d' % x_['e0']) if x_['e0'] else '') for x_ in f['led_groups']), '',
         '**The research instruments reproduced** ((R377)(11), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py’s full run in the foreground, nothing else writing to '
         'tools/ or data/ while it ran, the rows of a bank of zeros that the run reads read by it and by nothing else: rows %d, reproducing %d, differing %d, not run %d (%s), the planted '
         'controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its '
         'banks at %s; then, by time, %s; tools/standing/ moved by the commits of (7) alone, from %s to %s, VERSION moved by each and each with its planted control; each act tool committed '
         'before its run; the plan and the certificate committed before any dispatch; the kernel’s %d commits by the one-call tool and their pushes by the gated push, each capture masked by '
         '[K23]; SIDE-explicit-formula’s main not moved; the per-commit scan at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay '
         'data/b767_prelock.txt, data/b767_pathrefusal.txt); the Project set built at the close from the close’s own export at step [23a] and its banks committed at [25] by [K24].' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (ap_(K.CHAIN_WORDS.get(k_, k_)), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), f['st_entering'], f['st_version'], len(K.KERNEL_COMMITS)), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula; no push forced; no tag cut or moved, v0.45 not cut under (4) and v0.38 to '
         'v0.44 and v0.2.0 unmoved; no pin moved; no sentence of any paper written or edited; REGISTRY, ERRATA, the census, the register and the two files of the map not written, FINDINGS '
         'and OPEN_TRAILS the two files of PLACE-papers written; nothing fetched from the web by the seat; nothing computed at a zero, the window’s frequency read by name and printed nowhere, '
         'the reproduction run’s rows of a bank of zeros read by it alone; no lean process on this host; no byline; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel’s commits among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (9)**: the hours by the step rows: %s (the closing comes after this entry and its row is printed in the closing message). The step rows summed by component, each '
         'row’s span from the row before it given to its own phase, the act’s step rows of every repository to this entry (relay data/b767_steps.json):' % r10h_, '',
         '| component | step rows | hours |', '| --- | ---: | ---: |'] + ['| %s | %d | %.2f |' % (p_, n_, h_) for p_, n_, h_ in sh_] + ['| all | %d | %.2f |' % (shn_, sht_), ''] + (
         [] if any(p_ == 'component 4' for p_, _n4, _h4 in sh_) else [
             'Component 4, the closing build from source, holds no step row of its own: its two dispatches sent, and the first read, within the spans of component 3’s rows, the second '
             'read within component 5’s (relay data/b767_events.txt (91), (94), (97)).', '']) + [
         'Each dispatch by its run id, its kind and its minutes: %s (relay data/b767_dispatch_rows.json). The price table’s figures beside what each item took: %s (relay data/b767_price.txt; '
         'tools/b767_controls.py ROW_RAISES). THE MEASURE, read at this act’s close: the hours from the lock to the closing, beside b766’s %s and b764’s %s, printed in the closing message; '
         'the lettered defects tagged REPEAT whose class is a key that data/b764_repairs.txt or data/b766_repairs.txt reads REPAIRED, %d of the %d tagged REPEAT (%s), wanted 0; the lettered '
         'defects of the class clause (1) names, a carried constant, cap or predicate read with the meaning the previous ruling gave it, %d of %d (%s), beside b766’s %s; each row’s own '
         'sentence giving its reading (relay data/b767_defects.txt).' % (
             rnw_, '; '.join(took_), m9_.group(1), m9_.group(2), len(cnt_), len(repl_), ', '.join('(%s)' % x_ for x_ in cnt_) or 'none', len(c1_), len(all_),
             ', '.join('(%s)' % x_ for x_ in c1_) or 'none', m9_.group(3)), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the certificate of (4)(a) and the Lean of (4)(c) and (4)(d) read the one window two ways, the certificate’s exact rationals outside '
         'Lean and the kernel’s data files checked by kernel reduction against the same bank’s digests, so that each value a lemma consumes is the certificate’s; the two builds from source '
         'read what a restored build does not, the price of the whole kernel with the Window files under the runner’s hold; the three readings of (5) set the registry’s rows, the kernels’ '
         'declarations and the findings ledger against the keystones beside the proof without building anything; the rulings of (6) place the map, the premise rows, the restore’s kind and '
         'the author’s word. Each is a statement about the record, its tools or the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(12), as the author answers the one question at the root: where [P2] stands, the act after this one continues the proof at the step that did not '
         'compile or was not sent, L9’s remainder, the registry’s block and the map’s merge beside its dispatches; or another the author names; printed beside it for the author’s strike, '
         'the four lists of (5)(a), the figures of (5)(b) and (5)(c) and the two prices of (4)(a)’s note; and the finding of the two builds from source, whose order and price the next ruling '
         'names. W-ORD-LI-ARITH carried by [P2]; W-ORD-WINDOW-CERTIFY with its certificate by [E1]; W-ORD-RUNNER-CACHE as [C5] left it; W-ORD-MAP-MERGE open. Orders open after the act: %d '
         '(relay data/b767_orders.txt); push-b767-proof at %s at the kernel’s remote and in its clone, no route removing it; no kernel branch removed but push-b766-planted under [K22]; the '
         'draft held at v5.' % (K.NEXT_ACT, f['ord_head'][1], (K.RUNNER_COMMIT or '-')[:8]), '',
         '**Next.** %s.' % ap_(K.next_line()), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b767_carried(f, S, rep, tot):
    """b765's form carried into b766 before Component 5, over b765's objects; kept for the record and not called (b766, Component 5)."""
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    r10h_, r10p_ = _report10()
    rs_, le_ = f['rep_states'], f['led_entered']
    ln_ = lambda k_: ('OPEN_TRAILS :%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)   # ### b766: one dispatch singular, as the closing's and the report's rg_ (the touch read, 19:4xZ)
    pw_ = lambda k_: rg_(f['pr_rows'][k_]['lo_h'], f['pr_rows'][k_]['hi_h'], 'h')
    pd_ = lambda k_: '%s over %s' % (pw_(k_), rg_(f['pr_rows'][k_]['dispatches'][0], f['pr_rows'][k_]['dispatches'][1], 'dispatches'))
    kc_ = dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS)
    xk_ = (f['xline'] or {}).get('key')
    held_ = f['tr_verdict'] == 'HELD'
    moved_ = held_ and (K.EF_MAIN or '')[:8] == (K.RUNNER_COMMIT or '-')[:8]
    tag_ = K.WEIL_TAG if moved_ and K.WEIL_TAG else None
    off_ = next((r_ for r_ in reversed(f['runs']) if r_['item'] in ('closing', 'repeat') and r_['exit'] == '0'), None)
    sti_ = lambda s_: '%d %s (%s)' % (len(rs_[s_]), s_.lower(), ', '.join(rs_[s_]) or 'none')
    hw_ = lambda h_: {'true': 'an exact key', 'false': 'a key by the prefix', 'none': 'no key'}.get(str(h_).lower(), 'not read')
    rnw_ = '; '.join('dispatch %d, the %s at %s with the restore %s, run %s, %s, %s minutes of run, its record restoring %s' % (
        r_['n'], r_['item'], r_['sha'], r_['restore'] or 'as the stopped run`s', r_['run'], r_['verdict'] or 'not read',
        '-' if r_['run_min'] is None else r_['run_min'], hw_(r_['hit'])) for r_ in f['runs']) or 'none'
    took_ = []
    for pk_ in ITEM_PRICE_ORDER:
        its_ = [it_ for it_, k_ in ITEM_ROWS if k_ == pk_]
        rr_ = [r_ for r_ in f['runs'] if r_['item'] in its_]
        took_.append('%s priced %s, %s' % (pk_, pd_(pk_) if pk_ in f['pr_rows'] else 'by the author`s two words of 2026-11-21 at one dispatch each', (
            '%d dispatch%s, %s minutes of run' % (len(rr_), '' if len(rr_) == 1 else 'es', round(sum(r_['run_min'] or 0 for r_ in rr_), 1))) if rr_ else 'no dispatch'))
    st_ = next((x_ for x_ in f['statement_reads'] if x_[2] == 'COMPILED'), None)
    s2p_ = re.search(r'its axioms print (\[[^\]]*\])', _ot_line(*le_['S2'])) if 'S2' in le_ else None
    cnt_, repl_ = _measure()
    mv_ = '; '.join('%s %s to %s' % (n_, a_, b_) for n_, a_, b_ in f['led_roster'][3]) or 'no status moving'
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
    cl_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)
    wc_ = f['w_cells']
    e = ['', _title(), '',
         ' '.join(s_.rstrip('.') + '.' for s_ in (f['w_sentence'], 'H-RUNNER-RESTORE %s%s' % (f['tr_verdict'], (': ' + f['tr_why']) if f['tr_why'] else ''))) + (
             ' Each sentence is the ruling`s for the outcome its bank reads, its fields filled from that bank (relay data/b767_window.txt, data/b767_controls.txt); '
             'the statement of the control`s failure compiled as a definition and Gauss`s integral for its archimedean term %s, each by its run`s axioms print; every '
             'build a runner dispatch read by its run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b767_dispatch_rows.json); no lean process on this host.' % (
                 'proved whole' if 'S2' in le_ else 'not proved whole', f['disp_ef'])), '',
         '*Filed at b767 on the author’s ruling `(R377)` and the author’s three words of 2026-11-21, Route A on W-ORD-H2-PI1, the runner’s cache and the save on main; %d question%s put '
         'before the root%s. Banks: relay `data/b767_misses.txt`, `data/b767_price.txt`, `data/b767_registration.txt`, `data/b767_author_words_preseal.txt`, '
         '`data/b767_amendments.json`, `data/b767_corrigendum.txt`, `data/b767_repairs.txt`, `data/b767_repair_controls.txt`, `data/b767_standing_dry.txt`, '
         '`data/b767_kernel_bases.json`, `data/b767_controls_control.txt`, `data/b767_dispatch_rows.json`, `data/b767_controls.txt`, `data/b767_window.txt`, '
         '`data/b767_window.json`, `data/b767_gauss_gate.txt`, `data/b767_held_branches.txt`, `data/b767_map_pair.txt`, `data/b767_premise_positions.txt`, '
         '`data/b767_pi01_reading.txt`, `data/b767_project_set_control.txt`, `data/b767_project_set_repo.json`, `data/b767_ledgers.txt`, `data/b767_orders.txt`, '
         '`data/b767_reproduce.txt`, `data/b767_author_answers.txt`, `data/b767_events.txt`, `data/b767_defects.txt`, `data/b767_prelock.txt`, '
         '`data/b767_pathrefusal.txt`, `data/b767_address_scan.txt`, `data/b767_touch.txt`, `data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's', (' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record`s head line gives it; the relay`s main read back at %s after its closing push (relay data/b766_closing.txt, data/b766_scores_close.json). '
         'The corrigendum, short, in the form of b766`s: b766’s %s events, %s rows after its seal and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items printed in full; '
         'what the seat found after b766`s lock entered as this act`s events (%s) to (%s) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; the navigator`s own %d claims entered as the navigator`s, CLAIM, events (%s) to (%s); at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8), K.PRE_RELAY[:8],
             f['corr_events'], f['corr_postseal'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], len(nr_), nr_[0], nr_[-1], f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The price and the ceiling** ((R377)(3)): the price table banked at step zero, before Component 1, each item of (4) to (9) with its lines, its dispatches and its hours, a dispatch priced by its kind -- a build from source at %s minutes and a restored build at %s, each as b766 banked it -- the seat`s own readings printed as the seat`s: step zero %s h, the lower sum %s h against %d h, %s, the upper sum %s h; the reading of the author`s word of 2026-11-21 on W-ORD-H2-PI1 priced in it as (6)(d) (relay data/b767_price.txt). '
         'Read again after Component 2 by a read-only reading at %s, entered in the events bank: %s h spent from the delivery, the lower sum %s h against %d h, under by %s h, %s (relay data/b767_events.txt (52)). '
         'The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             *[(lambda m_: ('%s to %s' % (m_[0], m_[1]) if m_[0] != m_[1] else '%s' % m_[0]) if isinstance(m_, (list, tuple)) else '%s' % m_)(f['pr_minutes'][i_]) for i_ in (1, 0)],   # ### b766: a kind's range printed as its figures, not as a list (the touch read, 19:4xZ)
             f['pr_step0'], f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['pr_upper'],
             f['ce_at'], f['ce_spent'], f['ce_sum'], f['ce_ceiling'], f['ce_under'], f['ce_word'].lower()), '',
         '**The two repairs** ((R377)(8)), in Component 1 before the opening pass, each with its planted control read at the commit before the repair and at the repair`s commit, both printed (relay data/b767_repairs.txt, data/b767_repair_controls.txt): tools/standing/ moved from %s to %s by %d commits, the two keys of (8) and the kernel route that (4) and (11) allow (relay data/b767_events.txt (30)), VERSION moved by each, the standing dry before each (relay data/b767_standing_dry.txt); %s, %s, %s and %d carried. %s' % (
             f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), sti_('REPAIRED'), sti_('READ AS DESIGNED'), sti_('REMOVED'), len(rs_['CARRIED']),
             ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps'])), '',
         '**The runner’s cache, tried again** ((R377)(4) and the author’s word of 2026-11-21 on it): push-b767-centre cut from push-b766-runner at 38a57e02; the workflow`s key at %s, the save keyed by the toolchain, the manifest and the commit and the restore by the prefix of the toolchain and the manifest; the planted input of the word`s (i), off by default, at %s; [G2] PART ONE committed alone at relay %s before any dispatch (relay data/b767_registration.txt). '
         'The dispatch and the read by tools/b767_controls.py, committed before its opening dispatch, its controls %d of %d (relay data/b767_controls_control.txt); every dispatch read by its run id from the downloaded artifact, the exit file governing: %s (relay data/b767_dispatch_rows.json). '
         'THE PLANTED BUILD: %s. THE PAIR: %s. H-RUNNER-RESTORE %s%s; the tool`s controls %d of %d (relay data/b767_controls.txt). The seat`s reading of "a restore hit", printed before the planted dispatch: the record`s restore line other than none, an exact key or a key by the prefix (relay data/b767_events.txt (48)). '
         '%s W-ORD-RUNNER-CACHE %s at %s. %s' % (
             kc_.get('workflow', '-')[:8], kc_.get('planted_input', '-')[:8], (K.REG_COMMIT or '-')[:8], f['cc_ctl'][0], f['cc_ctl'][1], rnw_,
             f['tr_planted_line'], f['tr_pair_line'], f['tr_verdict'], ('; ' + f['tr_why']) if f['tr_why'] else '', f['tr_ctl'][0], f['tr_ctl'][1],
             ('Main moved from %s to the closing Lean commit %s by the gated push, never forced, and read back at the remote; the kernel`s local main fast-forwarded by the one-call tool and read back equal; %s. The save on main of the word`s (iii): %s.' % (
                 K.EF_BASE[:8], (K.RUNNER_COMMIT or '-')[:8], ('the tag %s cut after main`s read-back, on run %s with the restore off and on no other' % (tag_[0], off_['run'] if off_ else '-')) if tag_ else 'no tag cut',
                 f['tr_main_line'])) if moved_ else 'Main stands at %s; no tag cut; the Lean stands on push-b767-centre, cited by commit; builds stay from source; the save on main of the word`s (iii) not sent.' % K.EF_BASE[:8],
             'DISCHARGED by [C5]' if xk_ == 'C5' else 'CARRIED by [C6]', ln_(xk_ or '-'),
             ('push-b767-planted deleted from the kernel`s clone before the lock by the one-call tool`s route; at the remote it stays, its name its warning, named in the closing message.'
              if K.PLANTED_BRANCH[0] in K.KERNEL_REMOVED else
              'push-b767-planted`s delete sent by the one-call tool`s route before the lock and refused there, %s (%s): the branch stays in the kernel`s clone and at its remote, its name its warning, named in the closing message for removal by the author`s word ((R377)(4)).' % (
                  (dict((r_[0], r_[2]) for r_ in K.KERNEL_DELETES_REFUSED).get(K.PLANTED_BRANCH[0]) or 'refused'), (dict((r_[0], r_[1]) for r_ in K.KERNEL_DELETES_REFUSED).get(K.PLANTED_BRANCH[0]) or '-')))), '',   # ### b766: the route refused it at 19:19:48Z
         '**The statement of the control’s failure** ((R377)(5)(a)): SIDEExplicitFormula/ControlFailureExists.lean at %s, a definition of a Prop in a file of its own: there is a k in classK, vanishing outside [-log 1024, log 1024], at which the real part of the control`s arithmetic side, poleTerm k - primeTermQ cQ k + archTermQ k, is below 0; it names no frequency and no zero; its imports H2Sign, Schema.EpsteinZQ and the module that defines cQ, the control of (R373)(7) reading its import closure PASSED before its dispatch; its name joining print_targets.txt. %s; entered as a definition and not a result, its position DEFINITION, the proof carried; [S1] at %s. The statement file of b763 stays on push-b763-arith, unmerged.' % (
             kc_.get('statement', '-')[:8], ('Compiled at run %s, its axioms %s' % (st_[0], st_[3])) if st_ else 'Not compiled', ln_('S1')), '',
         '**Gauss’s integral for the archimedean term** ((R377)(5)(b)): the gate before any dispatch of it, a control and no registration, by tools/b767_gauss_gate.py committed before its run: the form computed with the navigator`s right side in place of the kernel`s integral at the kernel`s window, %s; THE GATE %s, its first runs printed beside the readings entered, the first failing at :426 by the tool`s own radius (relay data/b767_gauss_gate.txt; data/b767_defects.txt (h)). '
         'The lemma`s statement GaussArchQ in a file of its own at %s, stated apart from its proof; its proof in steps, each a theorem compiled with no sorry, in SIDEExplicitFormula/GaussArchQSteps.lean at %s, %s, %s and %s, each read by its dispatch; %s; [S2] at %s. The verified quadrature of reading [L-i] not sent at this act.' % (
             '; '.join('at data/b709_grid.txt :%s (%s) S %s against the banked S_NN, the difference %s, to 6 digits %s' % (l_, n_, s_, d_, t_) for n_, l_, s_, d_, t_ in f['g_cells']),
             f['g_verdict'], kc_.get('gauss_statement', '-')[:8], kc_.get('steps14', '-')[:8], kc_.get('step5', '-')[:8], kc_.get('steps69', '-')[:8], kc_.get('step10', '-')[:8],
             ('SIDEExplicitFormula.B321.GaussArchQSteps.gaussArchQ at %s, a proof of GaussArchQ, its axioms print %s: proved whole' % ((K.RUNNER_COMMIT or '-')[:8], s2p_.group(1))) if s2p_ else 'not proved whole',
             ln_('S2')), '',
         '**The spline window, computed and banked as data** ((R377)(5)(c)): [G2] PART TWO committed with PART ONE at relay %s before any dispatch and before the tool`s run; tools/b767_window.py, carried in form from tools/b667_epstein_certify.py and committed before its run, the constants exact and every value a ball, its own control and the registration`s controls as wanted before any cell. H-SPLINE-WINDOW %s: %s Reported beside it, unregistered: at M 8 the arithmetic side %s and at M 32 %s, with d 3; nonzero coefficients %s, %s and %s of %s, %s and %s at M 16, 8 and 32; the prime side`s rational products %s each (relay data/b767_window.txt; data/b767_window.json, %d coefficients as rationals, its text sha256 %s as the tool printed it, taken before its writer`s final newline, the file`s bytes sha256 %s). [W%s] at %s. No figure of the navigator`s workspace printed as a banked figure.' % (
             (K.REG_COMMIT or '-')[:8], f['w_verdict'], f['w_sentence'].rstrip('.') + '.', wc_['8'][0], wc_['32'][0], wc_['16'][2], wc_['8'][2], wc_['32'][2], wc_['16'][3], wc_['8'][3], wc_['32'][3],
             wc_['16'][4], f['w_json'][0], f['w_json'][1], f['w_json'][2], '1' if f['w_verdict'] == 'HELD' else '2', ln_('W1' if f['w_verdict'] == 'HELD' else 'W2')), '',
         '**Four readings beside the dispatches** ((R377)(6) and the author’s word of 2026-11-21 on W-ORD-H2-PI1), each a reading and no build. '
         '(a) W-ORD-PREMISE-POSITIONS: the eighteen open premises, each at its statement at its pin, given its position under canon XXV by tools/b767_premise_positions.py, committed before its run, its rule in its head: A HYPOTHESIS BY DESIGN %d, DERIVED %d, OF THE HYPOTHESIS’S STRENGTH %d, none of these compiled %d; its control %s; no order retired, the rows whose consequence is retirement printed beside the root`s question (relay data/b767_premise_positions.txt); [Q1] at %s. '
         '(b) The federation map`s files: SPIRAL_MAP.md and SPIRAL_MAP_v0_7.md differ in %d lines, %d of SPIRAL_MAP_v0_7.md and %d of SPIRAL_MAP.md, in %d ranges, each by path, line and digest; the lines of SPIRAL_MAP.md alone written by %s; the seat`s recommendation beside the root`s question; no line of either file written (relay data/b767_map_pair.txt); [M3] at %s. '
         '(c) The held branches of SIDE-explicit-formula, by local git alone: %s; no branch removed (relay data/b767_held_branches.txt); [B2] at %s. '
         '(d) W-ORD-H2-PI1, Route A: the two addresses of the word fetched, one request each and no other address, each text kept in the act`s local bank untracked: addresses named %d, reached and read %d, not reached %d; by the word`s outcomes the order stands, no paragraph drafted, the two named papers cited as the origin, NOT READ AT SOURCE (relay data/b767_pi01_reading.txt); [H4] at %s.' % (
             f['q_counts'][1], f['q_counts'][2], f['q_counts'][3], f['q_counts'][4], f['q_ctl'].lower(), ln_('Q1'),
             f['m_lines'][0], f['m_lines'][1], f['m_lines'][2], f['m_lines'][3], f['m_acts'], ln_('M3'),
             '; '.join('%s %s' % (b_, w_) for b_, w_ in f['b_readings']), ln_('B2'),
             f['pi_counts'][0], f['pi_counts'][1], f['pi_counts'][2], ln_('H4')), '',
         '**The project’s mirror repository** ((R377)(7)): tools/project_set.py, the builder`s step under tools/ outside tools/standing/, committed before its run, its controls %d of %d as wanted, a planted byte in one copy read as that copy alone differing (relay data/b767_project_set_control.txt); the private repository created by the host`s tools under the account of (7), read back PRIVATE, and cloned outside every repository of the record, the account written <account> in the bank (relay data/b767_project_set_repo.json). Its build once at this act`s close, after the entry`s push to PLACE-papers and before the root, from an export verified CLEAN under its own tag (the misses read`s item (9)); [R1] entered in this act`s trail with that build`s commits.' % f['ps_ctl'], '',
         '**The author’s word of 2026-11-20 placed** ((R377)(9)): items (4), (8), (9) and (10) by (6) and (7); [T1] at %s, W-ORD-DETECTION-DUAL`s trigger rewritten; [T2] at %s, W-ORD-ROUTE-DE-EQUIV`s trigger written; [T3] at %s for items (1), (2), (3) and (5), its upstream field read present at its pin -- the clone data/b596_lemmas.txt :2 names stands on the host and holds the pin`s commit, read by local git alone with no fetch (relay data/b767_events.txt (10)) -- and its clause on W-ORD-H2-PI1 as the word of 2026-11-21 gives it. The three orders b766 carried by name stand as data/b766_orders_reading.txt :56 leaves them.' % (
             ln_('T1'), ln_('T2'), ln_('T3')), '',
         '**The ledgers** ((R377)(4)-(9) and the author`s words of 2026-11-21): by tools/b767_rulings.py, committed before its run, OPEN_TRAILS`s bytes at HEAD a prefix of its new bytes, no line moving: %s; under one dated head at :%d, %s; controls %d of %d (relay data/b767_ledgers.txt); REGISTRY, ERRATA and the register not written. '
         'The roster by tools/standing/orders.py`s rule: open %d before and %d after, %s; at PLACE-papers HEAD orders %d, open %d, closed %d (relay data/b767_orders.txt).' % (
             '; '.join('%s %d to %d lines, from :%d' % (p_, b_, a_, n_) for p_, b_, a_, n_, _s, _t in f['led_files']), f['led_head'][0],
             ', '.join('[%s] at :%d' % (k_, le_[k_][0]) for k_ in f['led_keys'] if k_ in le_), f['led_ctl'][0], f['led_ctl'][1],
             f['led_roster'][0], f['led_roster'][1], mv_, f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The research instruments reproduced** ((R377)(12), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran, the rows of a bank of zeros that the run reads read by it and by nothing else: rows %d, reproducing %d, differing %d, not run %d (%s), the planted controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; tools/standing/ moved by the commits of (8) and (4) alone, from %s to %s, VERSION moved by each and each with its planted control; each act tool committed before its run; the kernel`s %d commits by the one-call tool and their pushes by the gated push; %s; the gated push`s captures standing uncommitted for the author`s word, each holding the remote`s address (relay data/b767_events.txt (35)); the per-commit scan at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_).replace(']`s', ']’s').replace('s` ', 's’ '), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])   # ### b766: a plural possessive`s backtick read as an apostrophe (the entry`s dry, 19:04:03Z, odd backticks)
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), f['st_entering'], f['st_version'], len(K.KERNEL_COMMITS),
             'SIDE-explicit-formula`s main moved under HELD after the pair and at no other time' if moved_ else 'SIDE-explicit-formula`s main not moved'), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula; no push forced; no tag cut or moved beyond v0.44 under (4)%s, v0.38 to v0.43 and v0.2.0 among those unmoved; no pin moved; no sentence of any paper written or edited; REGISTRY, ERRATA and the register not written, FINDINGS and OPEN_TRAILS the two files of PLACE-papers written; nothing computed at a zero, the reproduction run`s rows of a bank of zeros read by it alone; nothing fetched from the web by the seat but the two addresses of the author`s word of 2026-11-21; no lean process on this host; no byline; the draft held at v5.' % (
             ', and v0.44 cut' if tag_ else ', and no tag cut at all'), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel`s commits among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (10)**: the hours by the step rows, as relay data/b754_close_yield.txt (A) reads them: %s (the closing comes after this entry and its row is printed in the closing message). '
         'The parts of each pass by the cadence (tools/standing/cadence.py %s), tools/standing/ at %s: %s; the pass after the push runs after this entry, its parts printed in the closing message. '
         'Each dispatch by its run id, its kind and its minutes, as above; the price table`s figures beside what each item took: %s; the items with no dispatch by their rows in relay data/b767_events.txt (relay data/b767_price.txt, data/b767_dispatch_rows.json). '
         'THE MEASURE OF (R376)(11), read at this act`s close and printed in the closing message: the hours from the lock to the closing beside b766`s 4.32 and b763`s 4.59; and the lettered defects tagged REPEAT whose class is a key that data/b766_repairs.txt reads REPAIRED, %d of the %d tagged REPEAT (%s), wanted 0, each row`s own sentence giving its reading (relay data/b767_defects.txt).' % (
             r10h_, __import__('standing.cadence', fromlist=['VERSION']).VERSION, K.STANDING_VERSION, ' ; '.join(r10p_), '; '.join(took_),
             len(cnt_), len(repl_), ', '.join('(%s)' % x_ for x_ in cnt_) or 'none'), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the window of (5)(c) and the lemma of (5)(b) read the one archimedean term two ways, the window`s tool taking it by Gauss`s integral in closed forms over the spline basis and the kernel proving that integral from its own definitions, so that the proof by the banked window can cite a compiled lemma for the term it computes; the statement of (5)(a) names what that proof would prove, and no more; the runner`s cache reads whether each step of that proof can be dispatched at a restored build`s price; the four readings set the premises, the map, the held branches and the order on the Pi-0-1 form beside the centre without building them. Each is a statement about the record, its tools or the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(13), as the author answers the one question at the root: the proof of the control`s failure by the banked window, where [W1] stands%s; or the registration H-ONSET-DENSITY with W-ORD-ADMISSIBLE-CONE and the navigator`s predictions, the search for a window carried in it; or another the author names; printed beside it for the author`s strike, the rows of (6)(a) whose consequence is retirement and the recommendation of (6)(b). '
         'W-ORD-LI-ARITH with its statement, its lemma and its window as entered; W-ORD-RUNNER-CACHE %s; W-ORD-H2-PI1 carried by [H4]. Orders open after the act: %d (relay data/b767_orders.txt); push-b767-centre, push-b766-runner and the four push-b763-* branches of SIDE-explicit-formula kept, push-b767-planted in the clone and at the remote, the delete route refusing it, named in the closing message; the draft held at v5.' % (
             K.NEXT_ACT, ' (it stands)' if f['w_verdict'] == 'HELD' else ' (it does not stand)', 'discharged by [C5]' if xk_ == 'C5' else 'carried by [C6]', f['ord_head'][1]), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b766_live(f, S):
    """b765's paragraphs over b765's objects, kept for the record and not called (b766, Component 5)."""
    rep, tot = _repeats()
    # ### b765: b761's closing head line (data/b761_closing.txt :1), the corrigendum's rows, the trail lines' paragraphs by line, the
    # ### report of (10)
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    pl_ = f['led_lines']
    r10h_, r10p_ = _report10()
    # ### b766, Component 3 (the Edit tool): the outcomes, the runs and the prices read once for the paragraphs below
    fo_, ar_, sf_ = f['oc_form'], f['oc_arith'], f['oc_sf']
    st6_ = [s_ for s_ in fo_.get('statements') or [] if s_.get('compiled')]
    true_ = [s_['sentence'] for s_ in st6_] + ([ar_['sentence']] if ar_.get('sentence') else [])
    # ### b766, Component 6 (the Edit tool): a range printed once where its ends are equal ("0 dispatches", "1 dispatch", "0.33 hours")
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    pw_ = lambda k_: '%s over %s' % (rg_(f['pr_rows'][k_]['lo_h'], f['pr_rows'][k_]['hi_h'], 'hours'), rg_(f['pr_rows'][k_]['dispatches'][0], f['pr_rows'][k_]['dispatches'][1], 'dispatches'))
    # ### b766, Component 6 (the Edit tool): each run's state worded for the reader -- the read row's verdict where the run broke or stopped, and what
    # ### compiled where it compiled (the outcomes tool's FORM, FILE and COMPILED)
    sw_ = {'FORM': 'KERNEL, the five statements compiled', 'FILE': 'KERNEL, the five statements and the statement file compiled', 'COMPILED': 'KERNEL'}
    rw_ = lambda it_: '; '.join('dispatch %d, run %s at %s, %s h, %s' % (n_, r_, s_, h_ if h_ is not None else 'not read', (lambda st_: sw_.get(st_) or (
        f['rd_rows'].get(r_) or {}).get('verdict') or st_)(next(
        (x_.get('state') for x_ in (fo_.get('runs') if it_ == 'form' else ar_.get('runs') if it_ == 'arith' else []) or [] if str(x_.get('run')) == r_), 'read')))
        for i_, n_, r_, s_, _a, _b, h_ in f['runs'] if i_ == it_)
    # ### b766, Component 6 (the Edit tool): what each order of (8) not built in full did build, named; the IMP2-TAU reading from its bank's foot
    i2_ = re.search(r'(?m)^### ### \*\*THE IMP2-TAU READING: ([^\n]*?) ; CONTROLS (\d+) OF (\d+) ; ', rdn('%s_imp2tau.txt' % ACT))
    nb8_ = {'W-ORD-KEIPER-FACE': lambda o_: 'its first file, SIDEExplicitFormula/KeiperPolygamma.lean, %d declarations on Mathlib`s digamma -- its analyticity on the right half-plane, its functional equation at every order and N times, its value from its partial sums where the tail tends to 0, the tail a named premise -- compiled on push-b767-keiper at %s, run %s, %s; the order in full needs the Keiper-Taylor identity`s fourth obligation at every index and the bounds on the Stieltjes constants, so main did not move to its branch' % (
        max([(f['rd_rows'].get(str(x_.get('run'))) or {}).get('new_n', 0) for x_ in o_.get('runs') or []] or [0]), kc_.get('keiper', '-')[:8],
        ', '.join(str(x_.get('run')) for x_ in o_.get('runs') or []) or 'no run',
        'each name within the standard three' if all((f['rd_rows'].get(str(x_.get('run'))) or {}).get('new_within') for x_ in o_.get('runs') or []) and o_.get('runs') else 'its names not all within')}
    kc_ = dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS)
    c2_, c3_ = f['ce_readings'][0], f['ce_readings'][1]
    i1_ = re.search(r'\[I1\] CLUSTER ([^;]+?) ;', rdn('%s_corrigendum.txt' % ACT))
    p6_ = [r_ for k_, r_ in f['pr_rows'].items() if k_.startswith('(6) ')]
    tk_ = lambda it_: (sum(1 for x_ in f['runs'] if x_[0] == it_), round(sum(x_[6] or 0 for x_ in f['runs'] if x_[0] == it_), 2))
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    # ### b758 touch read: the comparative read's own line in the citation bank (banks, words, rows), cited by its line; step zero records none
    cl_ = rdn(K.CITATION_BANK).replace('\r', '').split(NL)
    cwl_ = next((i_ for i_, l_ in enumerate(cl_, 1) if l_.startswith('### THE COMPARATIVE SENTENCES AGAINST THE TABLES THEY CITE')), 0)
    cw_ = re.search(r': banks (\d+), words (\d+), rows (\d+) ;', cl_[cwl_ - 1]) if cwl_ else None
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    pc_, ch_ = dict(K.PP_CHAIN), dict(K.CHAIN)   # ### the order line's commits by key, PLACE-papers and relay (the worklist's chains)
    ppw_ = dict((k_, c_) for k_, _p, c_ in K.PP_WRITES)
    e = ['', _title(), '',
         '. '.join(s_.rstrip('.') for s_ in true_) + '. ' + (
             'Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from a run (relay data/b767_outcomes.txt); One Page`s 19 rows of '
             'SIDE-explicit-formula stated in one file, each closed by the name that proves it, %s (the author`s word of 2026-11-19); every build a runner dispatch read by its '
             'run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b767_dispatch_rows.json); no lean process on this host.' % (
                 ('built at run %s' % (sf_.get('runs') or ['-'])[-1]) if f['oc_words'][1] == 'BUILT' else 'the file not built', f['disp_ef'])), '',
         '*Filed at b767 on the author’s ruling `(R377)` and the author’s word of 2026-11-19 on the statement file; %d question%s put before the root%s. Banks: relay '
         '`data/b767_misses.txt`, `data/b767_corrigendum.txt`, `data/b767_price.txt`, `data/b767_ceiling.txt`, `data/b767_standing_v1372.txt`, '
         '`data/b767_controls_control.txt`, `data/b767_presend_s123.txt`, `data/b767_presend_s4.txt`, `data/b767_presend_s5.txt`, `data/b767_presend_sf.txt`, '
         '`data/b767_presend_s7.txt`, `data/b767_presend_s24.txt`, `data/b767_presend_skp.txt`, `data/b767_imp2tau.txt`, '
         '`data/b767_dispatch_rows.json`, `data/b767_outcomes.txt`, `data/b767_xlines.json`, the gated push`s captures '
         '`data/b767_SIDE-explicit-formula_push-b767-*_push_out.txt`, `data/b767_author_words_preseal.txt`, `data/b767_author_rulings.txt`, `data/b767_ledgers.txt`, '
         '`data/b767_orders.txt`, `data/b767_reproduce.txt`, `data/b767_recut_inputs.txt`, '
         '`data/b767_author_answers.txt`, `data/b767_events.txt`, `data/b767_defects.txt`, `data/b767_prelock.txt`, `data/b767_pathrefusal.txt`, '
         '`data/b767_address_scan.txt`, `data/b767_touch.txt`, `data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record`s head line gives it; the relay`s main read back at %s after its closing push (relay data/b766_closing.txt, data/b766_scores_close.json). '
         'The corrigendum, short: b766’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items printed in full; '
         'what the seat found after b766`s lock entered as this act`s events (%s) to (%s) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; the navigator`s own %d entered as the navigator`s, CLAIM, events (%s) to (%s), the fourth corrected by [I1], b766`s integration read from REGISTRY`s row d1-8 with the cluster %s; the repairs of (11) carried, each named, to one act of the record`s upkeep, none made here; at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8), K.PRE_RELAY[:8],
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], len(nr_), nr_[0], nr_[-1], i1_.group(1) if i1_ else 'unread', f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The route for kernel writes** ((R377)(5)): tools/standing/ %s at relay %s, the one change that admits this act`s branch names: commit.py`s KERNEL_ACTS and FF_ACTS each a row for b767 at SIDE-explicit-formula alone, VERSION moved from v1.37.1, its planted control among %d cases, %d as wanted (relay data/b767_standing_v1372.txt); its first commit refused, the standing dry not staged, and committed with the dry after (relay data/b767_defects.txt (f)). '
         'The dispatch and the read by tools/b767_controls.py, carried from tools/b759_controls.py, each item capped at its upper dispatches in the price table, committed before its opening dispatch, its controls %d of %d (relay data/b767_controls_control.txt); the pre-send reads of (R368)(4) and each send`s salt check by tools/b767_presend.py, committed before its run. '
         'Each kernel commit by the one-call tool with the scan over the staged set, its author and committer the noreply identity; each branch pushed by the gated push`s branch mode and read back; no kernel beyond SIDE-explicit-formula written.' % (
             f['vers'][0][0], K.C1_STANDING[:8], f['vers'][0][2], f['vers'][0][3], f['cc_ctl'][0], f['cc_ctl'][1]), '',
         '**Build one** ((R377)(6)), on push-b767-form made at main %s (v0.41): commit %s, (S1) to (S3) in SIDEExplicitFormula/FormFinite.lean and PoleAutocorrelation.lean, the six names of [P1] and the new names in print_targets.txt; commit %s, (S4) in ParitySplit.lean and (S5) in AdmissibleWeights.lean with the import that run 1 lacked; commit %s, the statement file and its 19 names. '
         'Each send`s salt check printed before it, each statement beside the definitions it rests on, binding no hypothesis beyond its sentence`s: %s (relay data/b767_presend_s123.txt, data/b767_presend_s4.txt, data/b767_presend_s5.txt, data/b767_presend_sf.txt). '
         'The runs: %s. Run 1 broke on three lemma names that Mathlib holds outside its file`s import closure, read in Mathlib`s tree in place of the closure (relay data/b767_defects.txt (i)); run 3 stopped under the runner`s memory hold upstream of the statement file, a reading of the runner, and run 4 built the same commit (relay data/b767_events.txt (52), (53)). '
         'Each statement of (6) compiled: the exit file 0, 0 error lines, each new name`s axioms line within propext, Classical.choice and Quot.sound, no line naming sorryAx. %s The grade read against (6) from each compiled statement before it was written: %s, binding no premise.' % (
             K.EF_BASE[:8], kc_.get('form13', '-')[:8], kc_.get('form45', '-')[:8], kc_.get('statement', '-')[:8],
             '; '.join('%s %s, %d of %d statements' % (s_, f['ps'][s_]['salt'], f['ps'][s_]['salt_n'][0], f['ps'][s_]['salt_n'][1]) for s_ in ('s123', 's4', 's5', 'sf') if s_ in f['ps']),
             rw_('form'),
             ('Main moved from %s to %s by the gated push`s default mode after run %s`s success, never forced; %s cut at main`s read-back, its tag object %s, its peel read back equal at the remote (relay data/b767_SIDE-explicit-formula_push-b767-form_push_out.txt); the kernel`s local main fast-forwarded by the one-call tool, read back equal.' % (
                 K.EF_BASE[:8], (fo_.get('peel') or '')[:8], fo_.get('run'), fo_.get('tag'), (fo_.get('tag_object') or '')[:8])) if f['oc_words'][0] == 'LANDED, COMPILED' else 'Main stands at %s, no tag cut.' % K.EF_BASE[:8],
             ', '.join(sorted(set(s_.get('grade') or '-' for s_ in st6_))) or '-'), '',
         '**The statement file** (the author`s word of 2026-11-19, amending (R376)(8) and (R377)(6) in this one matter; relay data/b767_author_words_preseal.txt :2-:7): SIDEExplicitFormula/OnePageStatement.lean, written on the seat`s defect (j) in the form of the vendored Zeta23/Statement.lean: One Page v2.0`s 19 rows of SIDE-explicit-formula at v0.41, each stated apart from its proof and closed by the name its row cites, the three rows of SIDE-kernel v1.5 named in its header with their file and lines and stated nowhere; its salt check %s, %d of %d; %s. '
         'W-ORD-STATEMENT-FILE CARRIED by the word: its 19 rows of SIDE-explicit-formula closed by the file at %s, its object from here the same file for the three rows in SIDE-kernel, its trigger the next runner build of SIDE-kernel (relay data/b767_outcomes.txt, data/b767_xlines.json).' % (
             f['ps']['sf']['salt'], f['ps']['sf']['salt_n'][0], f['ps']['sf']['salt_n'][1],
             ('built at run %s at %s, the exit file 0, each of its 19 names within the standard three' % ((sf_.get('runs') or ['-'])[-1], kc_.get('statement', '-')[:8])) if f['oc_words'][1] == 'BUILT' else 'not built: %s' % f['oc_words'][1],
             (fo_.get('tag') or kc_.get('statement', '-')[:8])), '',
         '**The centre** ((R377)(7)), on push-b767-arith made at main %s (v0.42): SIDEExplicitFormula/ControlFailureStatement.lean committed at %s before any line of a proof. FORM B, ControlFailureB: a named test function k in classK, the autocorrelation of a cosine-modulated B-spline of order six whose frequency is read from b709`s banked family (relay data/b709_grid.txt :46), vanishing outside [-log 1024, log 1024], at which the real part of poleTerm k - primeTermQ cQ k + archTermQ k is below 0. FORM A, ControlFailureA n: Wide.liCoeff zqZeroConfig n < 0. Each a definition of a Prop with no proof and no sorry. '
         'The control that no zero is used %s over the file: its imports 4, none under Schema/ZQ/OffZero, neither Schema/Detector nor a detector of Schema/Wide, none of the five names; its salt check %s, %d of %d (relay data/b767_presend_s7.txt). The run: %s (relay data/b767_outcomes.txt). '
         'The ceiling after Component 2: spent %s h from the delivery, %s h at the lower figures against 24 h, carried by name %s; what it left for the proof %s h, where FORM B`s upper %s h and FORM A`s %s h each do not fit; so no line of a proof was written, and [X2] is the line (relay data/b767_ceiling.txt).' % (
             (fo_.get('peel') or K.EF_BASE)[:8], kc_.get('arith', '-')[:8], f['ps']['s7']['nozero'], f['ps']['s7']['salt'], f['ps']['s7']['salt_n'][0], f['ps']['s7']['salt_n'][1],
             rw_('arith') + ('; the exit file 0, its ten names within the standard three' if f['oc_words'][2] == 'STATEMENT COMPILED, NO PROOF SENT' else ''),
             c2_['spent'], c2_['total'], ', '.join(k_[4:] for k_ in c2_['carried']) or 'none', f['ce_proof_left'], f['pr_rows']['(7) B']['hi_h'], f['pr_rows']['(7) A']['hi_h']), '',
         '**The orders priced beside it** ((R377)(8)): each priced in the table from its entry and its statements (relay data/b767_price.txt). The ceiling after Component 3: spent %s h from the delivery; left for (8), (9) and the close at their lower figures %s h; in ascending order of upper hours, %s (relay data/b767_ceiling.txt). %s' % (
             c3_['spent'], f['ce_left8'], '; '.join('%s, upper %s h against %s h left, %s' % (k_[4:], h_, l_, w_.lower()) for k_, w_, h_, l_ in f['ce_plan']),
             ' '.join(('%s BUILT IN FULL at %s = %s, run %s, its line [X3] (relay data/b767_outcomes.txt).' % (o_['order'], o_.get('tag'), (o_.get('peel') or '')[:8], o_.get('run')))
                      if o_.get('outcome') == 'BUILT IN FULL' else ('%s not built in full: %s; carried by name with its price, %s, no line written for it.' % (
                          o_['order'], nb8_[o_['order']](o_) if o_['order'] in nb8_ else ('its runs %s' % ', '.join(str(x_.get('run')) for x_ in o_.get('runs') or []) if o_.get('runs') else 'no run sent'),
                          pw_('(8) ' + o_['order'][6:])))
                      for o_ in f['oc_orders']) + ' ' + ' '.join(
                 '%s carried by name with its price, %s%s.' % ('W-ORD-' + k_[4:], pw_(k_), {'(8) IMP2-TAU': (': built as a relay computation of this act and banked -- the transcribed principal value diverges at every test function with f(1) not 0, its step a decade -f(1) ln 10 (read %s at f(1) = 1/2 against -1.1512925465), and each test function the order names is an autocorrelation with f(1) the square of its norm, above 0, so its comparison with -A is not made and no regularization is put in place of CC`s; its controls %s of %s (relay data/b767_imp2tau.txt). Not built in full, and as a relay computation and no kernel build it takes no line [X3], which carries a kernel`s fields' % (
                     (re.search(r'\(TRI (-?[\d.]+)\)', i2_.group(1)) or re.search(r'()', '')).group(1) or 'unread', i2_.group(2), i2_.group(3))) if i2_ else ': its bank`s foot unread',
                                                                                         '(8) BESSEL-BOUND-TIGHTEN': ': its every run computes at zeros, which (12) forbids',
                                                                                         '(8) E2-SEPARATION': ': its test opens a bank of zeros, which (12) forbids'}.get(k_, ''))
                 for k_, w_, _h, _l in f['ce_plan'] if not any(('(8) ' + o_['order'][6:]) == k_ for o_ in f['oc_orders']))), '',
         '**The author’s words** ((R377)(9)): [W1], the author`s word of 2026-11-19 on the form of a statement, banked verbatim from the ferry beside the navigator`s renderings of the author`s words on the orders, %d of them, each verbatim, nothing changed (relay data/b767_author_rulings.txt). '
         'By tools/b767_rulings.py, committed before its run, each file`s bytes at HEAD a prefix of its new bytes, no line moving: THE_METHOD_CANON.md took [C1] as section XXV at :%d, the one paper this act edits; OPEN_TRAILS took, under one dated head at :%d after b766`s trail and before this act`s own, the line naming the bank at :%d, [A1] to [A12] at :%d to :%d, [B1] at :%d and [B2] at :%d, then the build lines %s; controls %d of %d (relay data/b767_ledgers.txt). '
         'The roster by tools/standing/orders.py`s rule: open %d before, %d with the lines up to [B2], wanted %d, the rows %d of %d as wanted; W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE RETIRED by [A11] and [A12], W-ORD-PREMISE-POSITIONS ENTERED by [B2]; %d with the build lines beside, %s; at PLACE-papers HEAD orders %d, open %d, closed %d (relay data/b767_orders.txt). Three orders held as they stand and two keeping their entries’ events took no line.' % (
             f['rl_renders'], f['led_xv'], f['led_head'], pl_['W1 line'], pl_['A1'], pl_['A12'], pl_['B1'], pl_['B2'],
             ', '.join('%s at :%d' % (x_.get('key'), pl_.get(x_.get('key'), 0)) for x_ in f['xlines']) or 'none', f['led_ctl'][0], f['led_ctl'][1],
             f['led_roster'][0], f['led_roster'][1], f['led_roster'][3], f['led_rows'][0], f['led_rows'][1], f['led_roster'][2],
             ('the statuses moving after [B2] ' + ', '.join(f['led_moved_after'])) if f['led_moved_after'] else 'no status moving after [B2]',
             f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The research instruments reproduced** ((R377)(12), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (%s, as at b766), the planted controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The price and the ceiling** ((R377)(3)): the price table banked before Component 1 from 100 banked runs over 18 dispatch-row banks and zq-b730`s rate, %s lines an hour and %s h a dispatch, each item with its lines, its dispatches and its hours, the seat`s own readings printed as the seat`s: the lower sum %s h against %d h at step zero, carried by name %s, the upper sum %s h (relay data/b767_price.txt). '
         'Read again by tools/b767_ceiling.py, committed before its run: after Component 2 at %s, %s h, %s; after Component 3 at %s, %s h, %s; dispatches %d against the worklist`s %d (relay data/b767_ceiling.txt). '
         'The runs took %s h of wall time each against the table`s %s h a dispatch, the runner rebuilding the kernel from source at each dispatch; the table`s figures governed the ceiling as (3) orders, and the report of (10) prints each item beside what it took. The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             f['pr_rate'][0], f['pr_rate'][1], f['pr_lower'], f['pr_ceiling'], f['pr_carried'], f['pr_upper'],
             c2_['at'], c2_['total'], ('carried ' + ', '.join(k_[4:] for k_ in c2_['carried'])) if c2_['carried'] else 'nothing carried',
             c3_['at'], c3_['total'], ('carried ' + ', '.join(k_[4:] for k_ in c3_['carried'])) if c3_['carried'] else 'nothing carried',
             f['ce_disp'][0], f['ce_disp'][1], ', '.join('%s' % h_ for *_x, h_ in f['runs'] if h_ is not None) or 'none', f['pr_rate'][1]), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; tools/standing/ moved once, to %s, where (5) required it, VERSION moved with it and its controls banked; each act tool committed before its run, a dry run of its controls among its runs; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after a run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), K.STANDING_VERSION), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula; no push forced; no tag moved, v0.38 to v0.41 and v0.2.0 among them; no pin moved; no sentence of any paper written or edited beyond the canon`s section XXV; REGISTRY not written; no line of a proof of (7) written; nothing computed at a zero and no row of a bank of zeros opened, b709`s banked family read for (7)`s window alone; nothing fetched from the web; no lean process on this host; no byline; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel`s commits and tag messages among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (10)**: the hours by the step rows, as relay data/b754_close_yield.txt (A) reads them: %s (the closing comes after this entry and its row is printed in the closing message). '
         'The parts of each pass by the cadence (tools/standing/cadence.py %s), tools/standing/ at %s: %s; the pass after the push runs after this entry, its parts printed in the closing message. '
         'The price table`s figures beside what each item took, by its runs’ dispatch and read rows (relay data/b767_price.txt, data/b767_dispatch_rows.json): %s.' % (
             r10h_, __import__('standing.cadence', fromlist=['VERSION']).VERSION, K.STANDING_VERSION, ' ; '.join(r10p_),
             '; '.join(['(6) priced %s to %s h over %d to %d dispatches, took %d dispatches and %s h of runs' % ((
                 round(sum(r_['lo_h'] for r_ in p6_), 2), round(sum(r_['hi_h'] for r_ in p6_), 2), sum(r_['dispatches'][0] for r_ in p6_), sum(r_['dispatches'][1] for r_ in p6_)) + tk_('form')),
                        '(7)`s statement priced %s, took %d dispatch and %s h of runs' % ((pw_('(7) statements'),) + tk_('arith')),
                        '(7)`s proof priced %s for FORM B and %s for FORM A, took none, no line sent' % (pw_('(7) B'), pw_('(7) A'))]
                       + ['(8) %s priced %s, took %d dispatch%s and %s h of runs' % ((k_[4:], pw_(k_)) + tk_(i_)[:1] + ('' if tk_(i_)[0] == 1 else 'es',) + tk_(i_)[1:])
                          for i_, k_ in ((o_.get('item'), '(8) ' + o_['order'][6:]) for o_ in f['oc_orders']) if tk_(i_)[0]]
                       + ['each other order of (8) priced in the table and taking none'])), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): (S1) makes the prime-power side on a window a finite sum over n up to e^L for any weights, which is what lets FORM B of (7) be stated and proved from finitely many coefficients; (S3) puts the pole term`s sign on the parity of h, negative at an odd window in classK, and (S4) splits each term of the form on the even and the odd part, so the sign of the form at a real test function is read part by part; (S5) makes the weights at which the form stands at or above 0 on each window of a width a convex set fixed by the pole and archimedean terms and decided by finitely many weights, the reading canon XXV gives a width; and the control`s failure is now stated from its coefficients at a named window with no zero in it, compiled before its proof. Each is a statement about the explicit formula`s terms and about the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(13), as the author answers the one question at the root: one act of the record`s upkeep, carrying the repairs of (11), the orders [T8] to [T10] of (R376), [A5] and [A6]; or the act that computes the registration H-ONSET-DENSITY, with W-ORD-ADMISSIBLE-CONE joined to it by [A2]; or the reading of the eighteen named premises under W-ORD-PREMISE-POSITIONS; or another the author names. '
         'W-ORD-LI-ARITH carried with its statement compiled and both forms priced; the orders of (8) not built carried by name with their prices; W-ORD-STATEMENT-FILE with its object the same file for the three rows of SIDE-kernel. Orders open after the act: %d (relay data/b767_orders.txt); the push-b767-* branches of SIDE-explicit-formula kept for the next act`s step zero; the draft held at v5.' % (
             K.NEXT_ACT, f['ord_head'][1]), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b766_rest(f, sc_, sv_, vw_, pc_, ch_, n_ans, n_ref, cc, cw_, cwl_, checks, S, rep, tot):
    """b759's paragraphs over b759's objects, kept for the record and not called (b761, Component 6)."""
    w5_ = f['oc']['weil']
    nl_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_ in f['notes'])
    el_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_, _x in f['errata'])
    true5_ = [s_ for s_ in (w5_['sentence'], f['c6_sentence'], f['c8_sentence'], f['c9_sentence']) if s_]
    lp5_ = ('Main moved to the tip %s by the gated push`s default mode after the run`s success, v0.41 cut at main`s read-back (tag object %s) and its peel read back at '
            'the remote equal to main (relay data/b767_SIDE-explicit-formula_push-b767-weil_push_out.txt); the kernel`s local main fast-forwarded to it by the one-call tool, '
            'read back equal.' % (w5_['peel'], w5_['tag_object'])) if f['weil_word'].startswith('LANDED') else 'Main stands at %s, no tag cut.' % K.EF_BASE[:8]
    e = ['', _title(), '',
         ' '.join(true5_) + (
             ' Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from them (relay data/b767_outcomes.txt, data/b767_c3table.txt, '
             'data/b767_compose.txt, data/b767_corpus.txt); every build a runner dispatch read by its run id, %d in SIDE-explicit-formula of the 3 (5) allows and '
             'none elsewhere (relay data/b767_dispatch_rows.json); no lean process on this host.' % f['disp_ef']), '',
         '*Filed at b767 on the author’s ruling `(R377)`; %d question%s put before the root%s. Banks: relay '
         '`data/b767_misses.txt`, `data/b767_corrigendum.txt`, `data/b767_standing_v1363.txt` to `data/b767_standing_v1367.txt`, `data/b767_presend.txt`, '
         '`data/b767_controls_control.txt`, `data/b767_controls.txt`, `data/b767_dispatch_rows.json`, `data/b767_outcomes.txt`, the gated push`s capture '
         '`data/b767_SIDE-explicit-formula_push-b767-weil_push_out.txt`, `data/b767_c3table.txt`, `data/b767_costlaw.txt`, `data/b767_fields.txt`, '
         '`data/b767_fields_corpus.txt`, `data/b767_compose.txt`, `data/b767_notes.json`, `data/b767_corpus.txt`, `data/b767_errata.json`, `data/b767_reproduce.txt`, '
         '`data/b767_ceiling.txt`, `data/b767_author_answers.txt`, `data/b767_events.txt`, `data/b767_defects.txt`, `data/b767_prelock.txt`, `data/b767_pathrefusal.txt`, '
         '`data/b767_address_scan.txt`, `data/b767_touch.txt`, `data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b766 at its weight and the corrigendum** ((R377)(1)): b766 closed at relay c25f8b53 and PLACE-papers 4ea41948, its scores %d of 8 HELD (%s), as its closing record`s head line gives it (relay data/b766_closing.txt, data/b766_scores_close.json); N4 stays REFUTED on the plant`s repair after its lock and is not argued. '
         'The corrigendum of b766’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- no CLAIM item among them; '
         'what the seat found after b766`s lock entered as this act`s events (17) to (21) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b767_corrigendum.txt, route %s, banks %s; PLACE-papers %s). The version at the close %s.' % (
             f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted',
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'],
             f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], f['corr_line'], f['corr_row'], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['ver']), '',
         '**The four standing changes** ((R377)(4)), each a commit of its own moving VERSION, its planted controls printed before its use: (i) the route that removes a named branch at a kernel`s remote, refused for main, for a kept name and for a tip that is no ancestor of the remote`s main, read back absent, %s (relay data/b767_standing_v1363.txt); '
         '(ii) the plant of G-DELETES-ONE-BRANCH reading kept each clause that covers a named ref, (R376) replayed with its clauses (2) and (5) both read, %s (relay data/b767_standing_v1364.txt); '
         '(iii) the row writer taking the phase repair, b766`s repair commit f401a81e replayed, %s (relay data/b767_standing_v1365.txt); '
         '(iv) the suite`s reader of the kernels face naming SIDE-dirichlet-mod-24, made on checks.tpl :663 where the ruling named :611, b766`s face read as 24 kernels, %s (relay data/b767_standing_v1366.txt). '
         'The changes: %d of 4. The kernel route, the one-call tool opened for this act in SIDE-explicit-formula before its first kernel write, a standing change (4) does not name, %s, counted apart (relay data/b767_standing_v1367.txt). '
         'The branches of (3): at the relay and PLACE-papers the five push-b766-* branches by the tool`s route after the merged listing; at the kernels’ remotes %s, each by (i)`s route after its controls, each an ancestor of its remote`s main; each read absent after, one a message (relay data/b767_stepzero.txt, data/b767_events.txt (13), (24)); no clone`s branch removed; push-b767-weil kept for the next act`s step zero.' % (
             vw_('v1.36.3'), vw_('v1.36.4'), vw_('v1.36.5'), vw_('v1.36.6'), f['changes'], vw_('v1.36.7'), ', '.join('%s (was %s)' % (b_, t_[:8]) for b_, t_ in K.KERNEL_DELETES)), '',
         '**The statement and the print lines** ((R377)(5)): push-b767-weil made at main %s; commit one %s, the four lines rQ_one, cQ_eq, detector and h2_sign_iff_rh after print_targets.txt :484, none of them there before; commit two %s, zq_weil_positivity_fails with its docstring in Schema/Wide/HalfScaleControl.lean :37-:51 after zq_arith_side_re_neg, no line above it moved, ComplexOrder opened for it alone, and its line at print_targets.txt :489. '
         'The salt check printed before the send, h2_sign`s body taken into the control`s names under a negation equal to the statement, no binder before its colon: %s; the pre-send reads at %s: duplicates %d; refused by the filter %d (%s), the two known; anonymous pairs %d of %d (%d unread); %d modules for %d names, %d refused; controls %d of %d (relay data/b767_presend.txt). '
         'The dispatch and the read by tools/b767_controls.py, carried from b766`s and set for this act`s one item and its cap, committed before its opening dispatch, its own controls %d of %d (relay data/b767_controls_control.txt); dispatch 1 of 3 at the branch`s tip, run %s: the exit file 0, 0 error lines, %s axioms lines each within the standard three, the five new names among them, no line naming sorryAx (relay data/b767_controls.txt, data/b767_outcomes.txt). '
         'The grade read against the clause from the compiled statement before it was written anywhere: %s, binding no premise. %s' % (
             K.EF_BASE[:8], K.KERNEL_COMMITS[0][2][:8], K.KERNEL_COMMITS[1][2][:8], f['ps_salt'].lower(), f['ps_rev'], f['ps_dup'], f['ps_refused'], f['ps_refused_lines'],
             f['ps_anon'][0], f['ps_anon'][1], f['ps_anon'][2], f['ps_modules'], f['ps_names'], f['ps_names_refused'], f['ps_ctl'][0], f['ps_ctl'][1],
             f['cc_ctl'][0], f['cc_ctl'][1], w5_['run'], w5_['axiom_lines'], w5_['grade'], lp5_), '',
         '**The table of Appendix A** ((R377)(6)), a reproduction and no registered prediction, by tools/b767_c3table.py committed before its run: the plant printed first, the wanted table with beta at (3,2) read -2 reported unequal by each route at that cell and no other, %s; route one, the group-ring model of INSTRUMENTS I-105, %d of %d cells agreeing; route two, the form`s own count at -23 by the recursion of tools/b750_cq_sign.py, the primes 2, 3, 13 and 29 read as wanted and b(n) = c(n)/log n exact at each instance, %d of %d; route three, (a) the closed form of Step 4 for e from 1 to 24, %s, and (b) over every pattern of at most 8 prime factors counted with multiplicity, beta negative at none of the patterns containing none of (4,1), (3,2), (2,1,1) and (1,1,1,1), %s: %s, the law entering as %s (relay data/b767_c3table.txt).' % (
             f['c3_plant'].lower(), f['c3_one'][0], f['c3_one'][1], f['c3_two'][0], f['c3_two'][1], f['c3_a'].lower(), f['c3_b'].lower(), f['c3_word'], f['law_word']), '',
         '**The fields** ((R377)(7)), filled by tools/b767_fields.py from the banks and from no recall: %d filled, then N and DEPOSITS by its corpus route after (9), N %d and DEPOSITS %s; the pin %s, read equal to the run`s built ref; %d AX cells, each the axioms line of its name from the run that printed it, units24_iso_signs from b757`s; BLOCK F`s texts by (5)`s outcome and the law and the appendix by (6)`s; the six module md5s at 14ca5725 agreeing with data/b742_offlinezero.txt :68; HISTORY, v0.1 :3-:19 byte for byte; controls %d of %d and the route`s %d of %d (relay data/b767_fields.txt, data/b767_fields_corpus.txt). '
         'F1 and F2 by tools/b767_costlaw.py committed before its run: F1 = %s beside the quotient of the two banked figures, %s, %s, the sentence %s, its first figure read at data/b744_zetabox_plan.txt :135 where (7) cites :134; F2 = %s, INSTRUMENTS :556 carrying both heights; controls %d of %d (relay data/b767_costlaw.txt).' % (
             f['fd_filled'], f['fc_n'], f['fc_word'].lower(), f['fd_pin'], f['fd_ax'], f['fd_ctl'][0], f['fd_ctl'][1], f['fc_ctl'][0], f['fc_ctl'][1],
             f['cl_f1'], f['cl_quot'], f['cl_agree'].lower(), f['cl_word'].lower(), f['cl_f2'], f['cl_ctl'][0], f['cl_ctl'][1]), '',
         '**The document** ((R377)(8)): phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md composed by tools/b767_compose.py, committed before its run, beside v0.1, which is not edited: %d lines; BLOCK B %d of %d, each OLD once in v0.1 at its line; %d cites read, %d corrected where the name or figure stands once, %d listed where it does not; section 9.9 %s; brackets left %d; the banned stems %s; v0.1 %s, its sha256 equal before and after; controls %d of %d (relay data/b767_compose.txt); one PLACE-papers commit, %s. '
         'Written where else it is by tools/b767_notes.py, each note read back equal and committed alone: %s (relay data/b767_notes.json) -- REGISTRY`s row %s at :%s after 1.5c-23, its status "REVIEW; entered at v0.2 by b767; not deposited", no cell blank and no grade conferred, and a dated note at the file`s end giving v0.41 with its tag object and peel and closing "The tags confer no deposit."; FACES_LEDGER`s and the census`s each made of the document`s own dated head and the sentences of (5) and (8) that came true.' % (
             f['cp_lines'], f['cp_b'][0], f['cp_b'][1], f['cp_cites'], f['cp_corrected'], f['cp_listed'], f['cp_99'].lower(), f['cp_left'], f['cp_stems'].lower(), f['cp_v01'].lower(),
             f['cp_ctl'][0], f['cp_ctl'][1], K.C3_DOC_PP[1][:8], nl_, f['notes_reg'].get('id', '-'), f['notes_reg'].get('row_line', '-')), '',
         '**The corpus lines** ((R377)(9)): the hold on a paper`s sentences lifted for the fourteen lines of BLOCK D alone; each OLD read once at its line and replaced by its NEW by tools/b767_corpus.py, committed before its run, one PLACE-papers commit a document through the one-call tool, each confirmed at HEAD: %s; re-cut %d of %d, left %d, orders %d; REGISTRY`s deposit pins read for the nine documents, one deposited copy, A Place to Stand at REGISTRY :83, not read and not touched, C4 and C5 standing there as deposited; controls %d of %d (relay data/b767_corpus.txt, data/b767_corpus.json).' % (
             '; '.join('%s at %s' % (p_, c_) for p_, c_ in f['corpus_docs']), f['cr_recut'], f['cr_of'], f['cr_left'], f['cr_orders'], f['cr_ctl'][0], f['cr_ctl'][1]), '',
         '**ERRATA and the orders** ((R377)(10)), by tools/b767_errata.py committed before its run, each write read back equal and committed alone: %s (relay data/b767_errata.json) -- ERRATA`s entries %s at the file`s end in the form of E-2026-11-09-1, E-2026-11-06-1 not edited; OPEN_TRAILS’ block under one dated head after b766`s trail, no line moving: b766`s root answer; W-ORD-MECHANISM-ATTRIBUTION`s condition as the navigator read it, not met, T0 and T1 entered beside it and the order left open on the author`s word; the five orders W-ORD-WSC-KERNEL-CITES, W-ORD-LI-INDEX, W-ORD-CAPACITY-ATTRIBUTION, W-ORD-BIBLIOGRAPHY-LINK and W-ORD-EPSTEIN-SECTIONS-3-4 entered by name, each priced by no build; no order of a re-cut left, (9) leaving no line.' % (
             el_, ', '.join(((dict((r_[0], r_[4]) for r_ in f['errata']).get('errata')) or {}).get('entries') or [])), '',
         '**The research instruments reproduced** ((R377)(11), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (I-56, I-57, I-61 and I-107, as at b755), the planted controls %d of %d as wanted, %d s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The ceiling** ((R377)(2)): %d reading%s against 16 hours from the delivery, each before the work of a component began, the last at %s, %s h, %s, dispatches %d of %d (relay data/b767_ceiling.txt). The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b767_misses.txt).' % (
             f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower(), f['ce_disp'][0], f['ce_disp'][1]), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; each standing change a commit of its own moving VERSION with its controls bank, before its use; each act tool committed before it ran; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after its run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero'))), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula`s tree and the five branches of (3); no push forced; no tag moved, v0.38, v0.39, v0.40 and v0.2.0 among them; no toolchain or Mathlib pin moved; no sentence of any paper edited beyond (8)`s new file and (9)`s fourteen lines, v0.1 byte-equal before and after; no ledger row edited; no lean process on this host; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b767_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the control now stands in one document read from its coefficients and from its zeros -- on its arithmetic side the failure of positivity compiled at v0.41 beside the statement it negates, the coefficient law at class number 3 by written proof with its table reproduced by two routes, and the corpus`s sentences about it re-cut to what is proved, compiled and observed; each is a statement about the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R377)(11), as the author answers the one question at the root: the same re-cut, map before write, for the keystone the author names, Which Structure Confines standing nearest with three of this act`s orders on it; or the class-number-3 law priced for a kernel; or W-ORD-BIBLIOGRAPHY-LINK; or another the author names. W-ORD-MECHANISM-ATTRIBUTION and the five orders of (10) open; push-b767-weil kept; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b766_body():
    """b755's paragraphs over b755's objects, kept for the record and not called (b756, Component 6): held as text, their names b755's
    locals, which the gate's report dry (tools/standing/reportdry.py unbound) read as live unbound globals beside _finding_text's own (defect (j))."""
    return r"""
    e = [
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b767_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b767_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b767_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b767_zeros_from_primes_59.txt, data/b767_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b767 on the author’s ruling `(R377)` and its two amendment rows (relay data/b767_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b767_corrigendum.txt`, `data/b767_carried_faults.txt`, `data/b767_standing_v1346.txt`, `data/b767_walk.txt`, `data/b767_coeffs_controls.json`, `data/b767_literature.txt`, '
         '`data/b767_cand_a.txt` to `data/b767_cand_l_plant.txt`, `data/b767_candidates.txt`, `data/b767_ceiling.txt`, `data/b767_registrations.txt`, `data/b767_roots_59.txt`, '
         '`data/b767_list_59.txt`, `data/b767_list_59_controls.txt`, `data/b767_zeros_from_primes_59.txt`, `data/b767_recur_59.txt`, `data/b767_recur_control.txt`, '
         '`data/b767_census_from_primes.txt`, `data/b767_l16.json`, `data/b767_put_1.json`, `data/b767_put_2.json`, `data/b767_author_answers.txt`, `data/b767_events.txt`, '
         '`data/b767_defects.txt`, `data/b767_prelock.txt`, `data/b767_pathrefusal.txt`, `data/b767_reproduce.txt`, `data/b767_address_scan.txt`, `data/b767_touch.txt`, '
         '`data/b767_standing_figures.txt`, `data/b767_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R377)(1), (2); relay %s, %s, PLACE-papers %s): b766 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b766’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b767_corrigendum.txt). Its three repairs: the lock gate carried as tools/b767_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b767_standing_v1346.txt; the amendment row 1). '
         'The open items of b766`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b767_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R377)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b767_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b767_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b767_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b767_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R377)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b767_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b767_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R377)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b767_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes’ phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b767_candidates.txt, data/b767_cand_a.txt to data/b767_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R377)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b767_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b767_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b767_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b767_zeros_from_primes_59.txt, data/b767_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b767_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b767_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R377)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b767_defects.txt (l)); its generator committed at relay %s before its run (relay data/b767_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R377)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b767_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R377)(8)): the price table at step zero from banked timings where a bank held one (relay data/b767_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b767_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b767_stepzero.txt); step zero from %s (data/act_current.json) through b766`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]’s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b767_prelock.txt, data/b767_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b767_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b767_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b767_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b760: [U3] in force, the counter's line as it prints (its event in data/b760_events.txt (22))
         '**The standing arms**: the four figures at b767 -- %s, %s, %s, %s -- against b766’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b767_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b767_citation_check.txt, data/b767_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R377)(8), as the author answers the one question at the root: the clearing act as b767 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]’s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b767 with the clearing act after it; defects (b), (e) and the tools’ (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)
"""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b767's objects, _trail_text_b767): the writes; b766 at its weight; the one key of (8) with its row's sentence;
    the plan and the certificate; the build from source and its trial; the steps in Lean and [P2]; the closing build from source, main and
    the tag; the window at graded knots; the rulings of (7); the Project set at [23a]; the dispatches; the reproduction run; the ceiling; the
    report of (10); the open-orders line from tools/standing/orders.py's output over the trail at HEAD; the standing versions; the kernels.
    (R377)'s [R1] is an order's entry line, entered by the rulings tool's group c2; b765's [R1] reader (_r1_line) not called."""
    return _trail_text_b767()


R1_FERRY_LINE = 98   # ### data/b765_ferry.txt :98, [R1] between its two lines (:97, :99)


def _r1_line():
    """[R1] from the ferry's bank at :98, its fields filled from data/b765_project_set_build.json (the commit, the set's files, PLACE-papers'
    and the relay's commits) where the build's read-back is as wanted, the account before /PLACE-project-set written <account> by its
    pattern; None where the build is not read back as wanted."""
    t_ = (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * R1_FERRY_LINE)[R1_FERRY_LINE - 1]
    b_ = jl('%s_project_set_build.json' % ACT) or {}
    c_, w_, r_ = b_.get('commit') or {}, b_.get('write') or {}, b_.get('readback') or {}
    if not t_.startswith("THE PROJECT'S MIRROR REPOSITORY, built at b767 under `(R377)`(7): ") or t_.count('<commit>') != 3 or t_.count('<n>') != 1:
        sys.exit('### THE FERRY`S :%d IS NOT [R1] WITH ITS FOUR FIELDS -- NOTHING COMPOSED' % R1_FERRY_LINE)
    if r_.get('as_wanted') is not True or not c_.get('sha') or not w_.get('meta'):
        return None
    t_ = re.sub(r'[A-Za-z0-9][A-Za-z0-9-]*/PLACE-project-set', '<account>/PLACE-project-set', t_, count=1)
    for v_ in (c_['sha'][:8], w_['meta']['pp'][:8], (w_['meta'].get('relay') or '-')[:8]):
        t_ = t_.replace('<commit>', v_, 1)
    return t_.replace('<n>', str(w_['meta']['files']), 1)


def _trail_text_b767():
    """b767's trail record over b767's objects ((R377)): the ruling; the lines entered in the rulings tool's groups; b766 at its weight; the
    one key of (8) with its row's sentence; the plan amended and the certificate's three forms; the build from source read, its route and
    the trial, [S1] and [S2]; the steps in Lean and [P2] by its line at HEAD; the closing build from source, main and the tag; the window at
    graded knots, [G1]; the rulings of (7), [R1] and [A2]; the Project set at [23a]; the dispatches; the reproduction run; the ceiling; the
    report of (10) and its measure; the open-orders line from tools/standing/orders.py's output over the trail at HEAD; the standing
    versions; the kernels. Every possessive the typographic apostrophe. b766's form stands below as _trail_text_b766_form, not called.
    (b767, Component 4, the Edit tool.)"""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    _r, _n, sh = seal_hashes()
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    b7h_ = _b7_head()
    r10h_, _r10p = _report10()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    nr_ = (cj_.get('navigator') or {}).get('rows') or []
    rs_, le_ = f['rep_states'], f['led_entered']
    ln_ = lambda k_: (':%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    ap_ = lambda s_: str(s_).replace('`', '’')
    cm_ = lambda x_: '{:,}'.format(int(x_)) if (isinstance(x_, (int, float)) and float(x_).is_integer()) or str(x_).isdigit() else str(x_)
    keys_ = ', '.join('[%s] at %s' % (k_, ln_(k_)) for k_ in f['led_keys'])
    p2m_ = re.search(r"compiled at (\w+) on push-b767-proof: (.+); the step that did not compile, or was not sent within the hours of \(3\): (.+), "
                     r"(not sent|[^;,]+); the proof continues there\.", _ot_line(*le_['P2'])) if 'P2' in le_ else None
    m10_ = re.search(r"beside b766's ([\d.]+) and b765's ([\d.]+);.*?beside b766's (\w+)\.", (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * 47)[46])
    if not p2m_ or not m10_:
        sys.exit('### [P2] AT HEAD OR THE FERRY`S :47 NOT READ -- NOTHING COMPOSED')
    g_ = dict((x_['group'], x_) for x_ in f['led_groups'])
    el2_ = (jl('%s_ledgers_c2.json' % ACT) or {}).get('entry_lines') or {}
    runs_ = sorted(f['runs'], key=lambda r2_: r2_['n'])
    cl_ = [r_ for r_ in runs_ if r_['item'] in ('closing', 'repeat')]
    tr2_ = [r_ for r_ in runs_ if r_['item'] in ('trial-on', 'trial-off')]
    cnt_, repl_, cc_, all_ = _measure_r377()
    on_max_ = dict(K.MAX_DISPATCHES_KINDS)['restore']
    moved_ = bool(K.WEIL_TAG) and K.EF_MAIN[:8] == (K.RUNNER_COMMIT or '-')[:8]
    mw_ = ('main moved to %s by the gated push and %s cut there after main’s read-back' % (K.EF_MAIN[:8], K.WEIL_TAG[0])) if moved_ else (
        'main not moved and no tag cut, %s' % ('[C7] at %s' % ln_('C7') if 'C7' in le_ else '[C8] at %s' % ln_('C8') if 'C8' in le_ else 'by the dispatch tool’s reading'))
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R377) ratified.** Its components as the ferry orders them (relay data/b767_ferry.txt), each read below from its bank; no author’s word beside the ruling before the root.', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b766), %s; OPEN_TRAILS.md in %d groups, each under its own dated head, %s; this record.' % (
                 f['corr_line'], (':%s (the entry)' % fj['entry_line']) if fj.get('entry_line') else 'the entry at step [12], not yet landed', len(f['led_groups']), keys_), '',
             '**b766 at its weight** ((R377)(1)): closed at relay %s and PLACE-papers %s, the scores %d of %s HELD (%s); the corrigendum short at FINDINGS :%s, b766’s %s CLAIM items printed in '
             'full, the findings after its lock entered as events, the navigator’s %d claims entered CLAIM, no weight line (relay data/b766_scores_close.json, data/b767_corrigendum.txt).' % (
                 b7h_.group(1), b7h_.group(2), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', f['corr_line'], f['corr_claim'], len(nr_)), '',
             '**One key** ((R377)(8)): tools/standing/ from %s to %s by %d commit, with its planted control; %d repaired, %d read as designed, %d removed, %d carried. %s The row and its '
             'control: relay data/b767_repairs.txt, data/b767_repair_controls.txt.' % (
                 f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), len(rs_['REPAIRED']), len(rs_['READ AS DESIGNED']), len(rs_['REMOVED']), len(rs_['CARRIED']),
                 ' '.join(ap_(r_['sentence']).rstrip('.') + '.' for r_ in f['reps'])), '',
             '**The plan amended and the certificate** ((R377)(4)(a)): the combination in three forms, its controls %d of %d, the one width %d digits by the primes, %d by the integers, %d by '
             'parts at order %d; the plan, %d parts in the order of sending, at relay %s before the first dispatch (relay data/b767_certificate.txt, data/b767_plan.txt).' % (
                 f['cert_ctl'][0], f['cert_ctl'][1], f['cert_widths'][0], f['cert_widths'][1], f['cert_widths'][2], f['cert_widths'][3], len(f['plan_lemmas']), f['plan_commit']), '',
             '**The build from source** ((R377)(5)): [S1] at %s with W-ORD-SOURCE-BUILD’s entry line at :%s; the read and route (%s) banked, its controls %d of %d; the trial pair, %s; [S2] at '
             '%s (relay data/b767_source_build.txt, data/b767_controls.txt).' % (
                 ln_('S1'), (el2_.get('S1') or ['-'])[0], f['sb_route'][0], f['sb_ctl'][0], f['sb_ctl'][1],
                 ' and '.join('dispatch %d, run %s, the restore %s, %s, %s min' % (r_['n'], r_['run'], r_['restore'], r_['verdict'] or 'not read', '-' if r_['run_min'] is None else r_['run_min'])
                              for r_ in tr2_), ln_('S2')), '',
             '**The steps in Lean** ((R377)(4)(b)-(e)): push-b767-proof cut from push-b766-proof at %s; [P2] at %s, compiled at %s on push-b767-proof: %s; not sent within the hours of (3): '
             '%s; the E0 gate %d of %d (relay data/b767_dispatch_rows.json, data/b767_ledgers_c5.txt).' % (
                 K.WEIL_BRANCH_BASE[:8], ln_('P2'), p2m_.group(1)[:8], p2m_.group(2), p2m_.group(3), (g_['c5']['e0'] or (0, 0))[0], (g_['c5']['e0'] or (0, 0))[1]), '',
             '**The closing build from source** ((R377)(4)): %s, at %s with the restore off by route (i); THE PAIR: %s; MAIN AND THE TAG: %s; so %s (relay data/b767_controls.txt).' % (
                 '; '.join('dispatch %d, run %s, %s, %s min, the runner’s low %s MB' % (r_['n'], r_['run'], r_['verdict'] or 'exit %s' % r_['exit'], '-' if r_['run_min'] is None else r_['run_min'],
                                                                                    cm_(r_['low_mb']) if r_['low_mb'] is not None else '-') for r_ in cl_),
                 (K.RUNNER_COMMIT or '-')[:8], ap_(f['tr_pair_line']), ap_(f['tr_main_line']), mw_), '',
             '**The window at knots graded by octave** ((R377)(6)): registered at relay %s; the control as wanted at the uniform window; %d coefficients, the arithmetic side %s, H-GRADED-WINDOW '
             '%s, [%s] at %s; the combination’s primes %d, the sum of the |r| %s, the budget %d digits (relay data/b767_registration.txt, data/b767_window.txt).' % (
                 f['win_reg'], f['win_ncoef'], f['win_S'], f['win_reading'], f['win_key'], ln_(f['win_key']), f['win_primes'], f['win_sumr'], f['win_digits']), '',
             '**The rulings** ((R377)(7)): [R1] at %s with W-ORD-NOVEMBER-RIDERS’ entry line at :%s; [A2] at %s; open orders %d before and %d after (relay data/b767_ledgers_c2.txt).' % (
                 ln_('R1'), (el2_.get('R1') or ['-'])[0], ln_('A2'), f['led_roster'][0], f['led_roster'][1]), '',
             '**The Project set** ([K24]): built at the close at step [23a] from the close’s own export, the one carrying the root line, after this record and the mirror, its banks committed at '
             '[25]; printed in the closing message.', '',
             '**The dispatches:** SIDE-explicit-formula %d of at most %d, %d with the restore on of at most %d, each read by its run id, the exit file governing: %s; none elsewhere (relay '
             'data/b767_dispatch_rows.json).' % (
                 f['disp_ef'], K.MAX_DISPATCHES, f['tr_on'][0], on_max_, '; '.join('dispatch %d, item %s, the restore %s%s, run %s at %s, %s, %s min' % (
                     r_['n'], r_['item'], r_['restore'], (' (%s)' % r_['kind']) if r_['restore'] == 'on' and r_['kind'] else '', r_['run'], r_['sha'], r_['verdict'] or 'not read',
                     '-' if r_['run_min'] is None else r_['run_min']) for r_ in runs_) or 'none'), '',
             '**The reproduction run** ((R377)(12)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b767_reproduce.txt).' % (
                 f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
             '**The ceiling:** the lower sum %s h against %d h with %s h in reserve at step zero; read before the lock at %s, %s h spent, the last step dispatch at %s, %s h left of %d, %s '
             '(relay data/b767_price.txt, data/b767_ceiling.txt).' % (
                 f['pr_lower'], f['pr_ceiling'], cm_(f['pr_reserve']), f['ce_at'], f['ce_spent'], f['ce_last'], f['ce_left'], f['ce_ceiling'], f['ce_word'].lower()), '',
             '**The report of (10):** %s; the step rows by component, each dispatch by its run id, its kind and its minutes, and the price beside what each item took in the entry and the '
             'closing message; THE MEASURE: the lettered defects tagged REPEAT whose class is a key that data/b765_repairs.txt or data/b766_repairs.txt reads REPAIRED, %d of %d (%s), wanted 0; '
             'of the class a carried constant read with its previous meaning, %d of %d (%s), beside b766’s %s; the hours from the lock to the closing beside b766’s %s and b765’s %s in the '
             'closing message.' % (
                 r10h_, len(cnt_), len(repl_), ', '.join('(%s)' % x_ for x_ in cnt_) or 'none', len(cc_), len(all_), ', '.join('(%s)' % x_ for x_ in cc_) or 'none', m10_.group(3),
                 m10_.group(1), m10_.group(2)), '',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py’s output (its entry read outside quotations and hand sections, '
             'v1.27.0; a row ID’s token no order, v1.32.0).' % (len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s to %s by the %d commit of (8), with its planted control (relay data/b767_repairs.txt, data/b767_repair_controls.txt); HANDOFF.md written once '
             'by tools/standing/handoff.py before the gate, at relay %s.' % (f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), (K.HANDOFF_COMMIT or 'NOT SET')[:8]), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b767_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b767_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
             '**Act root:** b767 `%s` (previous `%s`, b766’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b767_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b767_repairs.txt); the standing '
             'report tool (relay data/b767_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** SIDE-explicit-formula’s main at %s (entering at %s), %s; %s at %s, the act’s Lean branch, at the remote and in the clone; %s, kept; v0.38 to %s %s, %s at '
              '%s; %s removed at its remote by b760, the clone’s branch kept at %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24’s main at %s, %s at %s, unmoved; no kernel beyond '
              'SIDE-explicit-formula touched, and there the files of (4) in SIDEExplicitFormula/Window/, print_targets.txt and, under (5), the workflow’s file; the %s branches as b767 '
              'found them; port-b707 at %s, its tag %s at it; SIDE-faces-join at %s with its one tag %s; no kernel branch removed; no lean process on this host.' % (
                  (K.EF_MAIN or '-')[:8], K.EF_BASE[:8], ('moved to the closing commit, %s cut there' % K.WEIL_TAG[0]) if moved_ else 'unmoved, no tag cut, %s not reached' % K.WEIL_TAG_CEILING,
                  K.WEIL_BRANCH[0], K.WEIL_BRANCH[1][:8],
                  ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (K.WEIL_BRANCH_B766, K.WEIL_BRANCH_B765, K.WEIL_BRANCH_B764, K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1],
                                                                       K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0])),
                  K.WEIL_TAG_B765[0], 'unmoved', K.WEIL_TAG_B765[0], K.WEIL_TAG_B765[2][:8], K.WEIL_BRANCH_B759[0], K.WEIL_BRANCH_B759[1][:8],
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root (the ferry’s Component 5), its set carrying OPEN_TRAILS as entered, HANDOFF.md among its files, its file named in the closing by '
              'its name, bytes and hash and its folder by role (relay data/b767_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b766’s %s, %s, %s, %s (relay data/b767_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b767_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % ap_(K.next_line()), '']
    return NL.join(rows_)


def _trail_text_b766_form():
    """b766's trail record over b766's objects: the ruling and the author's words; the lines entered in four groups; b765 at its weight;
    the three repairs of (7) with each row's sentence, the removal and the captures masked; the plan and the certificate of (4)(a); the
    steps in Lean and [P2] by its line at HEAD; the closing build from source and its repeat, each stopped, main not moved, no tag and no
    [C7] by the author's word; the three readings of (5); the rulings of (6); the Project set at [23a]; the dispatches; the reproduction
    run; the ceiling; the report of (9) and its measure; the open-orders line from tools/standing/orders.py's output over the trail at
    HEAD; the standing versions; the kernels. Every possessive the typographic apostrophe. b765's form, carried, stands below as
    _trail_text_b766_carried, not called."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    _r, _n, sh = seal_hashes()
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    b7h_ = _b7_head()
    r10h_, _r10p = _report10()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    nr_ = (cj_.get('navigator') or {}).get('rows') or []
    rs_, le_ = f['rep_states'], f['led_entered']
    ln_ = lambda k_: (':%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    ap_ = lambda s_: str(s_).replace('`', '’')
    cm_ = lambda x_: '{:,}'.format(int(x_)) if isinstance(x_, (int, float)) or str(x_).isdigit() else str(x_)
    kc_ = dict((k_, c_) for k_, _r2, c_, _b in K.KERNEL_COMMITS)
    q2_ = sorted(le_[k_][0] for k_ in le_ if k_.split('.')[0] == 'Q2')
    keys_ = ', '.join(('[Q2] x %d at :%d to :%d' % (len(q2_), q2_[0], q2_[-1])) if k_.split('.')[0] == 'Q2' else '[%s] at %s' % (k_, ln_(k_))
                      for k_ in f['led_keys'] if k_.split('.')[0] != 'Q2' or le_[k_][0] == q2_[0])
    p2m_ = re.search(r"of the plan's (\d+) lemmas, compiled at (\w+) on (\S+) \(built by runner run (\d+) [^)]*\): (.+?); the step that did not compile, or was "
                     r"not sent under the ceiling: (.+?), not sent; the proof continues there\.", _ot_line(*le_['P2'])) if 'P2' in le_ else None
    m9_ = re.search(r"beside b766's ([\d.]+) and b764's ([\d.]+);.*?beside b766's (\w+)\.", (rdn('%s_ferry.txt' % ACT).replace(chr(13), '').split(NL) + [''] * 40)[39])
    if not p2m_ or not m9_:
        sys.exit('### [P2] AT HEAD OR THE FERRY`S :40 NOT READ -- NOTHING COMPOSED')
    g_ = dict((x_['group'], x_) for x_ in f['led_groups'])
    st_ = _stops()
    off_ = [r_ for r_ in sorted(f['runs'], key=lambda r2_: r2_['n']) if r_['item'] in ('closing', 'repeat')]
    cnt_, repl_, c1_, all_ = _measure_b767()
    on_max_ = dict(K.MAX_DISPATCHES_KINDS)['restore']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R377) ratified.** Its components as the ferry orders them (relay data/b767_ferry.txt), each read below from its bank; the author’s three words of 2026-11-22 and word of '
             '2026-11-21 on the deposits and the keystones banked at step zero, and the author’s four words during the act (relay data/b767_author_words_preseal.txt :23, :26, :29, :32).', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b766), %s; OPEN_TRAILS.md in four groups, each under its own dated head, %s; this record.' % (
                 f['corr_line'], (':%s (the entry)' % fj['entry_line']) if fj.get('entry_line') else 'the entry at step [12], not yet landed', keys_), '',
             '**b766 at its weight** ((R377)(1)): closed at relay %s and PLACE-papers %s, the scores %d of %s HELD (%s); the corrigendum short at FINDINGS :%s, b766’s %s CLAIM items printed in '
             'full, the findings after its lock entered as events, the navigator’s own %d entered CLAIM, no weight line (relay data/b766_scores_close.json, data/b767_corrigendum.txt).' % (
                 b7h_.group(1), b7h_.group(2), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', f['corr_line'], f['corr_claim'], len(nr_)), '',
             '**The repairs** ((R377)(7)): tools/standing/ from %s to %s by %d commits, the three keys of (7), each with its planted control; %d repaired, %d read as designed, %d removed, %d '
             'carried. %s The rows and their controls: relay data/b767_repairs.txt, data/b767_repair_controls.txt and data/b767_capture_mask.txt.' % (
                 f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), len(rs_['REPAIRED']), len(rs_['READ AS DESIGNED']), len(rs_['REMOVED']), len(rs_['CARRIED']),
                 ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps'])), '',
             '**The plan and the certificate** ((R377)(4)(a)): the certificate banked, [%s] at %s, its controls %d of %d, K(n) at %d n, the arithmetic side one combination over %s primes; '
             'the plan, %d lemmas in the order of sending, at relay %s before the first dispatch (relay data/b767_certificate.txt, data/b767_plan.txt).' % (
                 f['cert_key'], ln_(f['cert_key']), f['cert_ctl'][0], f['cert_ctl'][1], f['cert_k'], cm_(f['cert_primes']), len(f['plan_lemmas']), f['plan_commit']), '',
             '**The steps in Lean** ((R377)(4)(b)-(d)): push-b767-proof cut from main at %s; [F1] at %s, L1 at %s; [F2] at %s, L2 to L5 at %s, the E0 gate %d of %d; [P2] at %s, of the plan’s '
             '%s lemmas, compiled at %s on %s: %s; not sent: %s; the E0 gate %d of %d (relay data/b767_dispatch_rows.json, data/b767_ledgers_c3.txt, data/b767_ledgers_c5.txt).' % (
                 K.EF_BASE[:8], ln_('F1'), kc_.get('prime', '-')[:8], ln_('F2'), kc_.get('window', '-')[:8], (g_['c3']['e0'] or (0, 0))[0], (g_['c3']['e0'] or (0, 0))[1], ln_('P2'),
                 p2m_.group(1), p2m_.group(2)[:8], p2m_.group(3), p2m_.group(5), p2m_.group(6), (g_['c5']['e0'] or (0, 0))[0], (g_['c5']['e0'] or (0, 0))[1]), '',
             '**The closing build from source and its repeat** ((R377)(4)): dispatches %s, runs %s, at %s with the restore off, each stopped under the hold at %s of %s jobs, the runner’s low %s '
             'MB, each axioms file one line; THE PAIR: %s; MAIN AND THE TAG: %s; no [C7] line, by the author’s word; the finding, that a build from source with the Window files does not pass '
             'the hold, carried to the next ruling (relay data/b767_controls.txt, data/b767_events.txt (94), (97), data/b767_author_words_preseal.txt :32).' % (
                 ' and '.join(str(r_['n']) for r_ in off_), ' and '.join(str(r_['run']) for r_ in off_), (K.RUNNER_COMMIT or '-')[:8], st_['jobs'][0], st_['jobs'][1],
                 ' and '.join(cm_(r_['low_mb']) for r_ in off_), ap_(f['tr_pair_line']), ap_(f['tr_main_line'])), '',
             '**The readings** ((R377)(5)): (a) [X1] at %s, %d rows of %d tables, KEYSTONE %d, UNPLACED %d; (b) [X2] at %s, declarations %s, named by a paper’s table %d, on a generated page '
             'alone %d, by neither %s, the navigator’s candidate %s; (c) [X3] at %s, entries %d, with a name the reader takes %d, no keystone %d, no such name %d of %s lines (relay '
             'data/b767_registry_cells.txt, data/b767_lean_join.txt, data/b767_sweep.txt).' % (
                 ln_('X1'), f['x1'][0], f['x1'][1], f['x1'][2], f['x1'][3], ln_('X2'), cm_(f['x2'][0]), f['x2'][1], f['x2'][2], cm_(f['x2'][3]), f['x2'][4].lower(),
                 ln_('X3'), f['x3'][0], f['x3'][1], f['x3'][4], f['x3'][5], cm_(f['x3'][6])), '',
             '**The rulings** ((R377)(6)): [M4] at %s with W-ORD-MAP-MERGE’s entry line; [Q2] x %d retired at :%d to :%d; [H5] at %s; [A1] at %s (relay data/b767_ledgers_c2.txt).' % (
                 ln_('M4'), len(q2_), q2_[0], q2_[-1], ln_('H5'), ln_('A1')), '',
             '**The Project set** ([K24]): built at the close at step [23a] from the close’s own export, the one carrying the root line, after this record and the mirror, its banks committed at '
             '[25]; printed in the closing message.', '',
             '**The dispatches:** SIDE-explicit-formula %d of at most %d, %d with the restore on of at most %d, the build from source and its repeat one each, each read by its run id, the exit '
             'file governing: %s; none elsewhere (relay data/b767_dispatch_rows.json).' % (
                 f['disp_ef'], K.MAX_DISPATCHES, f['tr_on'][0], on_max_, '; '.join('dispatch %d, item %s, the restore %s (%s), run %s at %s, %s, %s min' % (
                     r_['n'], r_['item'], r_['restore'], r_['kind'] or 'unread', r_['run'], r_['sha'], r_['verdict'] or 'not read', '-' if r_['run_min'] is None else r_['run_min'])
                     for r_ in sorted(f['runs'], key=lambda r2_: r2_['n'])) or 'none'), '',
             '**The reproduction run** ((R377)(11)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b767_reproduce.txt).' % (
                 f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
             '**The ceiling:** read at step zero, the lower sum %s h against %d h, %s; after (4)(c) at %s, %s h spent and %s h of the rows left, %s h against %d h, under by %s h, %s (relay '
             'data/b767_price.txt, data/b767_ceiling.txt).' % (
                 f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['ce_at'], f['ce_spent'], f['ce_left'], f['ce_sum'], f['ce_ceiling'], f['ce_under'], f['ce_word'].lower()), '',
             '**The report of (9):** %s; the step rows by component, each dispatch by its run id, its kind and its minutes, and the price beside what each item took in the entry and the '
             'closing message; THE MEASURE: the lettered defects tagged REPEAT whose class is a key that data/b764_repairs.txt or data/b766_repairs.txt reads REPAIRED, %d of %d (%s), wanted 0; '
             'of the class clause (1) names, %d of %d (%s), beside b766’s %s; the hours from the lock to the closing beside b766’s %s and b764’s %s in the closing message.' % (
                 r10h_, len(cnt_), len(repl_), ', '.join('(%s)' % x_ for x_ in cnt_) or 'none', len(c1_), len(all_), ', '.join('(%s)' % x_ for x_ in c1_) or 'none', m9_.group(3),
                 m9_.group(1), m9_.group(2)), '',
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py’s output (its entry read outside quotations and hand sections, '
             'v1.27.0; a row ID’s token no order, v1.32.0).' % (len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s to %s by the %d commits of (7), each with its planted control (relay data/b767_repairs.txt, data/b767_repair_controls.txt); HANDOFF.md written once '
             'by tools/standing/handoff.py before the gate, at relay %s.' % (f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), (K.HANDOFF_COMMIT or 'NOT SET')[:8]), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b767_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b767_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
             '**Act root:** b767 `%s` (previous `%s`, b766’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b767_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b767_repairs.txt); the standing '
             'report tool (relay data/b767_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** SIDE-explicit-formula’s main at %s (entering at %s), unmoved, no tag cut, %s not reached; %s at %s, the act’s Lean branch, kept at the remote and in the '
              'clone by the author’s word; push-b766-planted removed at its remote and in its clone after [K22]; %s, kept; v0.38 to %s unmoved, %s at %s; %s removed at its remote by b760, '
              'the clone’s branch kept at %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24’s main at %s, %s at %s, unmoved; no kernel beyond SIDE-explicit-formula touched, and there the files '
              'of (4) in SIDEExplicitFormula/Window/ and print_targets.txt; the %s branches as b767 found them; port-b707 at %s, its tag %s at it; SIDE-faces-join at %s with its one tag %s; '
              'no lean process on this host.' % (
                  (K.EF_MAIN or '-')[:8], K.EF_BASE[:8], K.WEIL_TAG_CEILING, K.WEIL_BRANCH[0], K.WEIL_BRANCH[1][:8],
                  ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (K.WEIL_BRANCH_B765, K.WEIL_BRANCH_B764, K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1], K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0])),
                  K.WEIL_TAG_B765[0], K.WEIL_TAG_B765[0], K.WEIL_TAG_B765[2][:8], K.WEIL_BRANCH_B759[0], K.WEIL_BRANCH_B759[1][:8],
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root (the ferry’s Component 5), its set carrying OPEN_TRAILS as entered, HANDOFF.md among its files, its file named in the closing by '
              'its name, bytes and hash and its folder by role (relay data/b767_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b766’s %s, %s, %s, %s (relay data/b767_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b767_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % ap_(K.next_line()), '']
    return NL.join(rows_)


def _trail_text_b767_carried():
    """b765's trail record carried into b766 before Component 5, over b765's objects; kept for the record and not called."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2)
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii)
    _r, _n, sh = seal_hashes()
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    b7h_ = _b7_head()
    r10h_, _r10p = _report10()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    nr_ = (cj_.get('navigator') or {}).get('rows') or []
    rs_, le_ = f['rep_states'], f['led_entered']
    ln_ = lambda k_: (':%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    kc_ = dict((k_, c_) for k_, _r2, c_, _b in K.KERNEL_COMMITS)
    xk_ = (f['xline'] or {}).get('key')
    held_ = f['tr_verdict'] == 'HELD'
    moved_ = held_ and (K.EF_MAIN or '')[:8] == (K.RUNNER_COMMIT or '-')[:8]
    tag_ = K.WEIL_TAG if moved_ and K.WEIL_TAG else None
    s2p_ = re.search(r'its axioms print (\[[^\]]*\])', _ot_line(*le_['S2'])) if 'S2' in le_ else None
    r1_ = _r1_line()
    psb_ = f['ps_build'] or {}
    cnt_, repl_ = _measure()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R377) ratified.** Its components as the ferry orders them (relay data/b767_ferry.txt), each read below from its bank; the author`s three words of 2026-11-21 amending it, Route A on W-ORD-H2-PI1 joined to (6) as (6)(d), the runner`s cache amending (4), and the save on main amending (4) and the word on the cache`s (iii), each an amendment row, [G2] PART ONE`s hypothesis unchanged (relay data/b767_author_words_preseal.txt, data/b767_amendments.json).', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b766), :%s (the entry); OPEN_TRAILS.md:%s under one dated head, %s; this record, [R1] in it.' % (
                 f['corr_line'], fj.get('entry_line'), f['led_head'][0], ', '.join('[%s] at %s' % (k_, ln_(k_)) for k_ in f['led_keys'])), '',
             '**b766 at its weight** ((R377)(1)): closed at relay %s and PLACE-papers %s, the scores %d of %s HELD (%s); the corrigendum short at FINDINGS :%s, b766`s %s CLAIM items printed in full, the findings after its lock entered as events, the navigator`s own %d entered CLAIM, no weight line (relay data/b766_scores_close.json, data/b767_corrigendum.txt).' % (
                 b7h_.group(1), b7h_.group(2), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', f['corr_line'], f['corr_claim'], len(nr_)), '',
             '**The repairs** ((R377)(8)): tools/standing/ from %s to %s by %d commits, the two keys of (8) and the kernel route that (4) and (11) allow, each with its planted control; %d repaired, %d read as designed, %d removed, %d carried. %s (relay data/b767_repairs.txt, data/b767_repair_controls.txt)' % (
                 f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), len(rs_['REPAIRED']), len(rs_['READ AS DESIGNED']), len(rs_['REMOVED']), len(rs_['CARRIED']),
                 ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps'])), '',
             '**The runner`s cache** ((R377)(4) and the author`s word on it): push-b767-centre at %s, the workflow`s key at %s and the word`s planted input at %s; THE PLANTED BUILD: %s; THE PAIR: %s; H-RUNNER-RESTORE %s; %s; [%s] at %s (relay data/b767_controls.txt, data/b767_dispatch_rows.json).' % (
                 (K.RUNNER_COMMIT or '-')[:8], kc_.get('workflow', '-')[:8], kc_.get('planted_input', '-')[:8], f['tr_planted_line'], f['tr_pair_line'], f['tr_verdict'],
                 ('main moved from %s to %s by the gated push and read back, %s; the save on main: %s' % (K.EF_BASE[:8], (K.RUNNER_COMMIT or '-')[:8], ('the tag %s cut after main`s read-back on the run with the restore off' % tag_[0]) if tag_ else 'no tag cut', f['tr_main_line']))
                 if moved_ else 'main not moved from %s, no tag cut, builds from source' % K.EF_BASE[:8], xk_ or '-', ln_(xk_ or '-')), '',
             '**The centre in steps** ((R377)(5)): (a) ControlFailureExists at %s, a definition of the control`s failure naming no zero and no frequency, its position DEFINITION, [S1] at %s; (b) the gate %s at data/b709_grid.txt :426 and :439, the lemma`s statement at %s and its proof in steps to %s, %s, [S2] at %s; (c) H-SPLINE-WINDOW %s at M 16 and d 3, the window banked with %d coefficients as rationals, [W%s] at %s (relay data/b767_dispatch_rows.json, data/b767_gauss_gate.txt, data/b767_window.txt).' % (
                 kc_.get('statement', '-')[:8], ln_('S1'), f['g_verdict'], kc_.get('gauss_statement', '-')[:8], kc_.get('step10', '-')[:8],
                 ('gaussArchQ proved whole, its axioms print %s' % s2p_.group(1)) if s2p_ else 'not proved whole', ln_('S2'),
                 f['w_verdict'], f['w_json'][0], '1' if f['w_verdict'] == 'HELD' else '2', ln_('W1' if f['w_verdict'] == 'HELD' else 'W2')), '',
             '**The readings** ((R377)(6)): (a) the eighteen premises, A HYPOTHESIS BY DESIGN %d, DERIVED %d, OF THE HYPOTHESIS’S STRENGTH %d, none of these compiled %d, no order retired, [Q1] at %s; (b) the map`s two files differing in %d lines, no line written, [M3] at %s; (c) the four held branches read, none removed, [B2] at %s; (d) W-ORD-H2-PI1 by Route A, %d of %d addresses reached and read, the order standing, [H4] at %s (relay data/b767_premise_positions.txt, data/b767_map_pair.txt, data/b767_held_branches.txt, data/b767_pi01_reading.txt).' % (
                 f['q_counts'][1], f['q_counts'][2], f['q_counts'][3], f['q_counts'][4], ln_('Q1'), f['m_lines'][0], ln_('M3'), ln_('B2'),
                 f['pi_counts'][1], f['pi_counts'][0], ln_('H4')), '']
    rows_ += ([r1_, ''] if r1_ else [])
    rows_ += ['**The project`s mirror repository** ((R377)(7)): %s (relay data/b767_project_set_control.txt, data/b767_project_set_repo.json%s).' % (
                  ('built once at this act`s close by tools/project_set.py from the export %s, verified CLEAN, its commit %s on the clone`s branch pushed by the gated route and the remote`s main read back equal, private, each file`s blob equal by md5 to the set; [R1] above' % (
                      ((psb_.get('write') or {}).get('meta') or {}).get('export', '-'), ((psb_.get('commit') or {}).get('sha') or '-')[:8])) if r1_
                  else 'created private and cloned; its build at the close not read back as wanted, printed in the closing message; [R1] not entered', ', data/b767_project_set_build.txt' if psb_ else ''), '',
              '**The author`s word of 2026-11-20 placed** ((R377)(9)): [T1] at %s, [T2] at %s, [T3] at %s, its upstream field present at its pin, its clause on W-ORD-H2-PI1 the word of 2026-11-21`s (relay data/b767_ledgers.txt).' % (
                  ln_('T1'), ln_('T2'), ln_('T3')), '',
              '**The dispatches:** SIDE-explicit-formula %d of at most %d, %d with the restore on of at most 10, each read by its run id, the exit file governing: %s; none elsewhere (relay data/b767_dispatch_rows.json).' % (
                  f['disp_ef'], K.MAX_DISPATCHES, f['tr_on'][0], '; '.join('the %s, restore %s, run %s at %s, %s, %s min' % (r_['item'], r_['restore'], r_['run'], r_['sha'], r_['verdict'] or 'not read',
                                                                                                                          '-' if r_['run_min'] is None else r_['run_min']) for r_ in f['runs']) or 'none'), '',
              '**The reproduction run** ((R377)(12)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b767_reproduce.txt).' % (
                  f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
              '**The ceiling:** read at step zero, the lower sum %s h against %d h, %s; after Component 2 at %s, %s h spent and the lower sum %s h against %d h, under by %s h, %s (relay data/b767_price.txt, data/b767_events.txt (52)).' % (
                  f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['ce_at'], f['ce_spent'], f['ce_sum'], f['ce_ceiling'], f['ce_under'], f['ce_word'].lower()), '',
              '**The report of (10):** %s; the parts of each pass by the cadence and the price beside what each item took in the entry and the closing message; THE MEASURE: the lettered defects tagged REPEAT whose class is a key that data/b766_repairs.txt reads REPAIRED %d of %d (%s), wanted 0, and the hours from the lock to the closing beside b766`s 4.32 and b763`s 4.59 in the closing message.' % (
                  r10h_, len(cnt_), len(repl_), ', '.join('(%s)' % x_ for x_ in cnt_) or 'none'), '',
              ORD.open_line(op), '',
              '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                  len(op), len(ORD.read(ORD.trail('HEAD')))), '',
              '**The standing versions:** %s to %s by the %d commits of (8) and (4), each with its planted control (relay data/b767_repairs.txt, data/b767_repair_controls.txt); HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay %s.' % (
                  f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), (K.HANDOFF_COMMIT or 'NOT SET')[:8]), '',
              '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b767_address_scan.txt).' % (f['addr'], f['orcid']), '',
              '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b767_touch.txt; the act’s counter '
              'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                   __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
              '**Act root:** b767 `%s` (previous `%s`, b766’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
              'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
              '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b767_author_answers.txt).' % (
                  n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                      ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
              '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b767_repairs.txt); the standing '
              'report tool (relay data/b767_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** SIDE-explicit-formula`s main at %s (entering at %s), %s; %s, kept for the next act`s step zero; push-b767-planted kept in the clone and at its remote, the one-call tool`s delete route refusing it before the lock, not fully merged, named in the closing message; %s, v0.38 to %s unmoved; %s removed at its remote by b760, the clone`s branch kept at %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24`s main at %s, %s at %s, unmoved; no kernel beyond SIDE-explicit-formula touched, and there the files of (5), print_targets.txt and the workflow`s file, the planted module on its branch alone; the %s branches as b767 found them; port-b707 at %s, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  (K.EF_MAIN or '-')[:8], K.EF_BASE[:8], 'moved to the closing Lean commit under HELD, read back at the remote' if moved_ else 'unmoved',
                  ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (K.WEIL_BRANCH, K.WEIL_BRANCH_B764, K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1], K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0])),
                  ('the tag %s cut on the run with the restore off' % tag_[0]) if tag_ else 'no tag cut',
                  K.ORDER_TAGS_B763[-1][0], K.WEIL_BRANCH_B759[0], K.WEIL_BRANCH_B759[1][:8],
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root (the ferry`s Component 5), its set carrying OPEN_TRAILS as entered, HANDOFF.md among its files, its file named in the closing by its name, bytes and hash and its folder by role (relay data/b767_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b766’s %s, %s, %s, %s (relay data/b767_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b767_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b766_kept():
    """b764's trail record over b764's objects, kept for the record and not called (b765, Component 5)."""
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
    op = ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1]
    b7h_ = _b7_head()
    r10h_, _r10p = _report10()
    # ### b765, Component 5 (the Edit tool): the trail over b765's objects, each figure from the banks' feet through _figs
    rs_, le_ = f['rep_states'], f['led_entered']
    ln_ = lambda k_: (':%d' % le_[k_][0]) if k_ in le_ else 'not entered'
    pw_ = lambda k_: '%s to %s h' % (f['pr_rows'][k_]['lo_h'], f['pr_rows'][k_]['hi_h'])
    moved_ = (K.EF_MAIN or '')[:8] == (K.RUNNER_COMMIT or '-')[:8]
    xk_ = (f['xline'] or {}).get('key')
    held_ = f['it_verdict'] == 'HELD'
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R377) ratified.** Its components as the ferry orders them (relay data/b767_ferry.txt), each read below from its bank; the author`s word of 2026-11-20 on (9)(b) amending [G1], [M1] and [M2] in that one matter (relay data/b767_author_words_preseal.txt).', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b766), :%s (the entry); ERRATA.md:%s ([E1]); OPEN_TRAILS.md:%s under one dated head, %s; BIBLIOGRAPHY.md:%s (its section 6); this record.' % (
                 f['corr_line'], fj.get('entry_line'), le_['E1'][0] if 'E1' in le_ else '-', f['led_head'][0],
                 ', '.join('[%s] at %s' % (k_, ln_(k_)) for k_ in f['led_keys']), f['led_bib']), '',
             '**b766 at its weight** ((R377)(1)): closed at relay %s and PLACE-papers %s, the scores %d of %s HELD (%s); the corrigendum short at FINDINGS :%s, b766`s %s CLAIM items printed in full, the findings after its lock entered as events, the navigator`s own five entered CLAIM, no weight line (relay data/b766_scores_close.json, data/b767_corrigendum.txt).' % (
                 b7h_.group(1), b7h_.group(2), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', f['corr_line'], f['corr_claim']), '',
             '**The repairs** ((R377)(5)): tools/standing/ from %s to %s by %d commits, one a key of (5) repaired or removed and one for (7), each with its planted control; %d repaired, %d read as designed, %d removed, %d carried. %s (relay data/b767_repairs.txt, data/b767_repair_controls.txt)' % (
                 f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), len(rs_['REPAIRED']), len(rs_['READ AS DESIGNED']), len(rs_['REMOVED']), len(rs_['CARRIED']),
                 ' '.join(r_['sentence'].rstrip('.') + '.' for r_ in f['reps'])), '',
             '**The close`s yield** ((R377)(6)): %s; the controls %d of %d (relay data/b767_close_yield.txt).' % (f['y_sentence'].rstrip('.'), f['y_ctl'][0], f['y_ctl'][1]), '',
             '**The runner** ((R377)(7)): push-b767-runner at %s, the workflow`s file alone; %s; the trial %s, its controls %d of %d; %s; [C1] at %s and [%s] at %s (relay data/b767_controls.txt, data/b767_dispatch_rows.json).' % (
                 (K.RUNNER_COMMIT or '-')[:8], f['tr_sentence'].rstrip('.'), f['tr_verdict'].lower(), f['tr_ctl'][0], f['tr_ctl'][1],
                 ('main moved from %s to %s by the gated push`s default mode and read back, no tag cut' % (K.EF_BASE[:8], (K.RUNNER_COMMIT or '-')[:8])) if moved_
                 else 'main not moved from %s, no tag cut' % K.EF_BASE[:8], ln_('C1'), xk_ or '-', ln_(xk_ or '-')), '',
             '**The orders** ((R377)(8)): W-ORD-E0-RANK-PROPAGATION %s; W-ORD-BIBLIOGRAPHY-LINK %s; W-ORD-LATE-BANKS, W-ORD-MATCHER-SHAPE and W-ORD-CORRESPONDENCE-BEHIND-SCOPE %s (relay data/b767_orders_reading.txt, data/b767_ledgers.txt).' % (
                 ('built, [D2] at %s' % ln_('D2')) if 'D2' in le_ else 'carried at %s' % pw_('(8) E0-RANK-PROPAGATION'),
                 ('built, the register`s section 6 at BIBLIOGRAPHY.md:%s, [D1] at %s' % (f['led_bib'], ln_('D1'))) if 'D1' in le_ else 'carried at %s' % pw_('(8) BIBLIOGRAPHY-LINK'),
                 ('each carried by name with its price, at %s, %s and %s' % (pw_('(8) LATE-BANKS'), pw_('(8) MATCHER-SHAPE'), pw_('(8) CORRESPONDENCE-BEHIND-SCOPE')))
                 if 'EACH CARRIED BY NAME' in f['or_words'] else 'as the reading`s foot gives them'), '',
             '**The landings** ((R377)(9)): (a) [E1] at ERRATA :%s and [F1] at %s, the deposit read %d files, %s; (b) [G1], %s, committed alone at %s before the tool`s run, %s at %d cells to %d digits, its controls %d of %d, %s at %s; (c) the centre priced anew in four readings, the cheapest by its upper figure %s, [L1] at %s; (d) [B1] at %s (relay data/b767_deposit_read.txt, data/b767_registration.txt, data/b767_imp2tau.txt, data/b767_price.txt).' % (
                 le_['E1'][0] if 'E1' in le_ else '-', ln_('F1'), f['dep_files'], 'none holding the paper' if f['dep_found'] == 0 else '%d holding it' % f['dep_found'],
                 f['reg_name'], f['reg_commit'], f['it_verdict'], f['it_cells'], f['it_digits'], f['it_ctl'][0], f['it_ctl'][1], '[M1]' if held_ else '[M2]',
                 ln_('M1' if held_ else 'M2'), f['pr_cheapest'], ln_('L1'), ln_('B1')), '',
             '**The predictions** ((R377)(10)): [P1] banked verbatim and committed alone at %s before Component 1; nothing of it computed (relay data/b767_navigator_predictions.txt).' % K.STEPZERO_PREDICTIONS[:8], '',
             '**The dispatches:** SIDE-explicit-formula %d, each read by its run id, the exit file governing: %s; none elsewhere (relay data/b767_dispatch_rows.json).' % (
                 f['disp_ef'], '; '.join('the %s, restore %s, run %s at %s, %s, %s min' % (r_['item'], r_['restore'], r_['run'], r_['sha'], r_['verdict'] or 'not read',
                                                                                            '-' if r_['run_min'] is None else r_['run_min']) for r_ in f['runs']) or 'none'), '',
             '**The reproduction run** ((R377)(13)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b767_reproduce.txt).' % (
                 f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
             '**The ceiling:** %d reading, after Component 2 at %s, %s h at the lower figures against %d h, %s; its plan %s (relay data/b767_ceiling.txt).' % (
                 f['ce_n'], f['ce_at'], f['ce_sum'], f['ce_ceiling'], f['ce_word'].lower(), f['ce_verdict']), '',
             '**The report of (11):** %s; the parts of each pass by the cadence, the price beside what each item took and the repairs by state in the entry and the closing message; THE MEASURE written there for the next act`s corrigendum.' % r10h_, '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s to %s by the %d commits of (5) and (7), each with its planted control (relay data/b767_repairs.txt, data/b767_repair_controls.txt); HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay %s.' % (
                 f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), (K.HANDOFF_COMMIT or 'NOT SET')[:8]), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b767_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b767_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b767 `%s` (previous `%s`, b766’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b767_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b767_repairs.txt); the standing '
             'report tool (relay data/b767_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** SIDE-explicit-formula`s main at %s (entering at %s), %s; %s, kept for the next act`s step zero; no tag cut, v0.38 to %s unmoved; %s removed at its remote by b760, the clone`s branch kept at %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24`s main at %s, %s at %s, unmoved; no kernel beyond SIDE-explicit-formula touched, and there the workflow`s file alone; the %s branches as b767 found them; port-b707 at %s, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  (K.EF_MAIN or '-')[:8], K.EF_BASE[:8], 'moved to the runner`s tip after the trial`s success, read back at the remote' if moved_ else 'unmoved',
                  ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (K.WEIL_BRANCH, K.ARITH_BRANCH_B763, K.ORDER_BRANCHES_B763[1], K.WEIL_BRANCH_B763, K.ORDER_BRANCHES_B763[0])),
                  K.ORDER_TAGS_B763[-1][0], K.WEIL_BRANCH_B759[0], K.WEIL_BRANCH_B759[1][:8],
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root (the ferry`s Component 5), its set carrying OPEN_TRAILS, ERRATA and the register as entered, HANDOFF.md among its files, its file named in the closing by its name, bytes and hash and its folder by role (relay data/b767_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b766’s %s, %s, %s, %s (relay data/b767_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b767_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)
#⟪END⟫
#⟪OVERRIDE record MARK df786768d1d9 87⟫
    # ### v1.38.17, (R375)(5) [K4]: record.tpl :2664-:2750, the b72x body the template keeps after SLOT 34, REMOVED from this act's render with the retained def that held it (_finding_text_b764, never called): it read the worklist's C3_RELAY, a constant the carry left empty "set as made", and the DEAD names
#⟪END⟫
#⟪OVERRIDE record MARK 44716f1971b1 58⟫
    # ### v1.38.17, (R375)(5) [K4]: record.tpl :2767-:2824, the b72x body the template keeps after SLOT 35, REMOVED from this act's render with the retained def that held it (_trail_text_b764, never called): it read the worklist's C3_RELAY
#⟪END⟫
#⟪SECTION regspec 1⟫
    # ### b767, Component 4 (the Edit tool; `carry.py ruled` R2, events (17), (51)): the cap read as (R377)(4)'s 40 where b766's text gave 20,
    # ### the act's own dispatches by their kinds from the worklist's EF_RUNS and the dispatch rows
    ('runner dispatch commands made', K.MAX_DISPATCHES, 'DISPATCHES', 'dispatches', '### N1: within the worklist`s MAX_DISPATCHES %d in SIDE-explicit-formula ((R377)(4): at most %d with the restore on; with the restore off the trial of (5), the closing build and one repeat of each where it stopped under the hold; no planted kind) and none in SIDE-dirichlet-mod-24; %d sent (relay data/b767_dispatch_rows.json); MEASURED off the command bank (each dispatch command at a command`s head).' % (K.MAX_DISPATCHES, dict(K.MAX_DISPATCHES_KINDS)['restore'], len(K.EF_RUNS))),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: every run read by its id from its artifact, the exit file governing (data/b767_dispatch_rows.json); MEASURED off the worklist`s EF_RUNS and M24_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b767*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; b763`s four push-b763-* branches, b764`s push-b764-runner, b765`s push-b765-centre, b766`s push-b766-proof at 3c67b8b5 and this act`s push-b767-proof beside them, push-b767-proof kept at its remote and in its clone ((R377)(4)); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('kernel branches removed at a kernel`s remote', 0, 0, 'branches', '### none ((R377)(12), N5): no rdelete route run; push-b766-proof, push-b767-proof and the four held branches of b725 to b730 kept.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b767 found them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing and kept; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b767*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act, the four unmoved; MEASURED off each branch against the act`s entering main 0ba9cd61.'),
    # ### b767, Component 4 (the Edit tool): main from 0ba9cd61 to 89fd5b54 adds 33 Lean files, b766's seventeen and this act's sixteen in
    # ### SIDEExplicitFormula/Window/, and modifies the workflow and print_targets.txt (git diff --name-status, 19:08:57Z, names alone)
    ('Lean files changed on SIDE-explicit-formula`s main', 33 if K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8] else 0, 'EFMAINLEAN', 'files', (('### (R377)(4): main moved to the closing Lean commit %s, the 33 Window files of push-b766-proof and push-b767-proof on it; ' % K.RUNNER_COMMIT[:8]) if K.EF_MAIN[:8] == K.RUNNER_COMMIT[:8] else '### (R377)(4): main not moved, the 33 Window files standing on push-b767-proof at 89fd5b54, b766`s seventeen beneath them at 3c67b8b5; ') + 'SIDE-dirichlet-mod-24 unmoved; MEASURED off git diff --name-only from 0ba9cd61 to main.'),
    ('tags cut by this act', 1 if K.WEIL_TAG else 0, 'EFTAGS', 'tags', (('### N5, (R377)(4): %s at the closing Lean commit after main`s read-back' % K.WEIL_TAG[0]) if K.WEIL_TAG else '### N5, (R377)(4): none -- v0.45 not cut') + '; v0.38 to v0.44 and v0.2.0 unmoved; MEASURED off SIDE-explicit-formula`s tags past v0.44.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b766-closing, push-b766-preroot, push-b766-record; PLACE-papers push-b766-preroot, push-b766-record; each by name, through the one-call tool, one per message, after the --merged listing and the citation check (data/b767_stepzero.txt :58-:61).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 1, 1, 'files', '### (R377)(5)(b), (c), (9): .github/workflows/build-module.yml on push-b767-proof by route (i) at f6f60590, the act`s opening Lean commit (data/b767_events.txt (60)); the other fourteen kernel commits write the Window files of (4) and print_targets.txt alone.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written (N3); no line added above the heading of rule [Q] (3), read by its digest.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none: REGISTRY not written; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R377)(1): FINDINGS :16080 (relay data/b767_corrigendum.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R377)(1): row (87).'),
    ('ERRATA entries filed', 0, 'ERRATAN', 'entries', '### none: ERRATA not written ((R377)(12), N3); MEASURED off the lines git diff adds to ERRATA.md from the act`s first PLACE-papers head to HEAD.'),
    ('the ruling`s texts entered, each equal to its text with its fields filled', 'RULINGS', 'RULINGS', 'texts', '### (R377)(4)-(7): [S1], [G1], [R1] and [A2] (group c2), [P2] and [S2] (c5)' + (', and the closing pair`s text (c6)' if os.path.exists(os.path.join(ROOT, 'data', 'b767_ledgers_c6.json')) else '') + ', in OPEN_TRAILS under their dated heads; MEASURED off relay data/b767_ledgers_c2.json to _c6.json`s entered.'),
    ('orders leaving the open count in the roster`s form', 'ORDCLOSED', 'ORDCLOSED', 'orders', '### none: W-ORD-SOURCE-BUILD entered open by [S1] and W-ORD-NOVEMBER-RIDERS by [R1], no order retired or discharged; MEASURED off relay data/b767_ledgers_c2.json to _c6.json`s rosters (the open count before, the orders added, the open count after).'),
    ('repairs rows, one a key of (8)', 1, 'REPAIRS', 'rows', '### (R377)(8): [K25] alone, REPAIRED; MEASURED off relay data/b767_repairs.txt`s states.'),
    ('the runner`s line composed for OPEN_TRAILS from its runs', 1 if os.path.exists(os.path.join(ROOT, 'data', 'b767_ledgers_c6.json')) and 'C7' in ((json.load(io.open(os.path.join(ROOT, 'data', 'b767_ledgers_c6.json'), encoding='utf-8')).get('entered')) or {}) else 0, 'TRIALLINE', 'lines', '### [C7] where the closing build from source and the restored build print different axioms files ((R377)(4)), none otherwise; MEASURED off relay data/b767_ledgers_c2.json to _c6.json.'),
    ('integration lines in the canon`s form', 1, 1, 'lines', '### (R377)(10): this act`s own, the entry`s last line, bare, as (10) gives it, written by no reader of the act`s banks.'),
    ('standing changes landed', 1, 'STANDINGV', 'changes', '### (R377)(8), (11): v1.38.24 to v1.38.25 by one commit, [K25], VERSION moved by it, its planted control printed before and after (relay data/b767_repair_controls.txt); MEASURED off git log of tools/standing/ from the act`s base.'),
    ('orders entered with the trail', 2, 'ORDADDED', 'orders', '### (R377)(5), (7)(c): W-ORD-SOURCE-BUILD by [S1] and W-ORD-NOVEMBER-RIDERS by [R1], each in the entry form tools/standing/orderstate.py :26 reads; no other; MEASURED off relay data/b767_ledgers_c2.json to _c6.json`s rosters added.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py`s full run at b767 as (R377)(12) orders it, in the foreground; MEASURED off data/b767_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### the tools` runs over the record, the runner`s prints and the reproduction run as (R377)(12) orders it, nothing computed at a zero: the price, the repair`s planted control, the certificate`s three forms, the read of the stopped runs, the window at graded knots, the dispatch tool`s controls and bank, the data files of L10 and L11b, the ceiling, the ledgers, the corrigendum, the orders, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 1, 'REGALONE', 'commits', '### (R377)(6): H-GRADED-WINDOW, as data/b767_registration.txt at relay b9224ba6, before the window tool`s run at graded knots (data/b767_events.txt (51)); MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 2, 'REGS', 'banks', '### (R377)(6): the window`s bank and its json (data/b767_window.txt and .json), each first added after the registration`s commit; the units file untracked; no row of a bank of zeros opened by the seat`s hand ((R377)(12)); MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 0, 'PREREG', 'banks', '### none (N2, N3): the registration before any cell at graded knots, nothing computed at a zero; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 16, 'EFNEW', 'modules', '### (R377)(4)(b)-(d): the sixteen files of SIDEExplicitFormula/Window/ on push-b767-proof from 3c67b8b5 to 89fd5b54, ArchJ.lean to ArchBandLocal.lean for L9a and L9b, LogData, LogBounds and LogConst for L10, PoleComb, LogNatBase, LogNatData and LogNat for L11a and L11b, each a module of its own; MEASURED off the act`s branch against its base 3c67b8b5.'),
    ('Lean files edited by the act`s own commits', 0, 'EFEDIT', 'files', '### none: no Lean file of push-b766-proof edited on push-b767-proof; MEASURED off the act`s branch against its base 3c67b8b5.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R377)(8), (11): tools/standing/ v1.38.24 to v1.38.25 by one version commit, [K25], commit.py and VERSION, its planted control printed before and after (relay data/b767_repair_controls.txt); tools/push_gated.sh and tools/project_set.py not written; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 4, 4, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended, row (87); HANDOFF.md by tools/standing/handoff.py before the gate ((R377)(13)); data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part and computation; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b767_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, the dispatches and the artifact downloads, the gh reads under the GitHub login, and the Project`s repository written and read back at the close under [K24]; none carries an identifier, nothing fetched from the web ((R377)(12)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b766, Component 5 (the Edit tool, before any run): the four ledgers banks of the rulings tool's groups c2 to c5, summed -- b766 writes
    # ### no data/b766_ledgers.json, so b765's single reader read 0 here by its exception
    # ### b767, Component 4 (the Edit tool): b767's groups c2 and c5, and c6 where the closing pair enters [C7] or [C8]; jcount reads 0 for a
    # ### bank absent
    def jsum(f):
        return sum(jcount('b767_ledgers_%s.json' % g_, f) for g_ in ('c2', 'c5', 'c6'))
    # ### b767 (R377)(6): the registered object H-GRADED-WINDOW, its figure banks the window's bank and json, each first added after the
    # ### registration's commit (K.REG_COMMIT b9224ba6); the units file untracked
    fig_banks = [p for p in ('data/b767_window.txt', 'data/b767_window.json')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    # ### b766: the runs' count read against the worklist's caps (SIDE-explicit-formula's alone, at most 20, M24_RUNS empty)
                    EFRUNS=len(K.EF_RUNS) + len(K.M24_RUNS),
                    # ### b766 (the Edit tool, before any run): main's Lean and commits past the entering main 0ba9cd61 (EF_BASE), the tags past
                    # ### v0.44 (b765's v0.44 stands at 0ba9cd61; the carried pattern from v0.44 would have read it as this act's), the texts entered,
                    # ### the ERRATA entries read off ERRATA.md (the carried reader took an entered key opening E as an ERRATA entry, which [E1] is
                    # ### not), the orders leaving the open count and added, the repairs rows, the runner's line, the standing commits; the four
                    # ### ledgers banks summed by jsum (regspec section 16)
                    EFMAINLEAN=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, 'main').split() if f_.endswith('.lean')),
                    EFTAGS=sum(1 for t_ in _git(K.EF_DIR, 'tag', '--list', 'v0.*').split() if re.match(r'^v0\.(4[5-9]|[5-9]\d)$', t_)),
                    RULINGS=jsum(lambda j: len(j.get('entered') or {})),
                    ERRATAN=len([l_ for l_ in _git(K.PP, 'diff', '--unified=0', K.PRE_PP, 'HEAD', '--', 'ERRATA.md').split(chr(10)) if l_.startswith('+') and not l_.startswith('+++')]),
                    # ### the orders leaving the open count: those open before, with the orders added, less those open after
                    ORDCLOSED=jsum(lambda j: int((j.get('roster') or {}).get('before_open') or 0) + len((j.get('roster') or {}).get('added') or [])
                                   - int((j.get('roster') or {}).get('after_open') or 0)),
                    ORDADDED=jsum(lambda j: len((j.get('roster') or {}).get('added') or [])),
                    REPAIRS=len(re.findall(r'; STATE: (?:REPAIRED|READ AS DESIGNED|REMOVED|CARRIED)\b', ' '.join(l_.strip() for l_ in io.open(os.path.join(ROOT, 'data', 'b767_repairs.txt'), encoding='utf-8').read().replace(chr(13), '').split(chr(10))))),
                    TRIALLINE=jsum(lambda j: 1 if ((j.get('runner') or {}).get('key') in ('C5', 'C6', 'C7')) else 0),
                    STANDINGV=len([h_ for h_ in _git(ROOT, 'log', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()]),
                    EFMAINCOMMITS=int(_git(K.EF_DIR, 'rev-list', '--count', '%s..main' % K.EF_BASE) or 0),
                    OTBLOCK=jsum(lambda j: (int((j.get('file') or {}).get('lines_after') or 0) - int((j.get('file') or {}).get('lines_before') or 0))
                                 if (j.get('file') or {}).get('path') == 'OPEN_TRAILS.md' else 0),   # ### b766: four groups, each writing one file, its row a dict
                    REPROWS=jcount('b767_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b767_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    # ### b767 (the Edit tool): the modules push-b767-proof adds past its base 3c67b8b5 ((R377)(4): sixteen) and the Lean files its
                    # ### commits edit (none), read against K.WEIL_BRANCH_BASE where b766's read against main's entering pin, its branch cut from main
                    EFNEW=len(set(f_ for b_ in [K.WEIL_BRANCH]
                                  for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=A', K.WEIL_BRANCH_BASE, b_[1]).split() if f_.endswith('.lean'))),
                    EFEDIT=len(set(f_ for b_ in [K.WEIL_BRANCH]
                                   for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=M', K.WEIL_BRANCH_BASE, b_[1]).split() if f_.endswith('.lean'))),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    # ### b767, Component 4 (the Edit tool): b767's computed banks, each by its own tool or scratch writer
                    COMPUTE=len([n_ for n_ in ('price', 'repair_controls', 'certificate', 'source_build', 'window', 'controls_control', 'controls',
                                               'logdata', 'natdata', 'ceiling', 'ledgers_c2', 'ledgers_c5', 'ledgers_c6', 'corrigendum', 'orders',
                                               'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b767_%s.txt' % n_))]),
                    # ### b767 (R377)(6): the registration of H-GRADED-WINDOW committed alone (b9224ba6), b765's reader
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b767_registration.txt').split()
                                  if _git(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split() == ['data/b767_registration.txt']]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFEDIT', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE', 'EFMAINLEAN', 'EFTAGS', 'RULINGS', 'ERRATAN', 'ORDCLOSED', 'ORDADDED', 'REPAIRS', 'TRIALLINE', 'STANDINGV', 'EFMAINCOMMITS', 'OTBLOCK',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b767_registration_%s.txt -- b767, THE PROOF BY THE BANKED WINDOW CONTINUED: b766 AT ITS WEIGHT; THE PLAN AMENDED; "
                             "THE ARCHIMEDEAN TERM AS THE COMBINATION; THE ENCLOSURES; THE INEQUALITY; THE CLOSING THEOREM; THE BUILD FROM SOURCE GIVEN ITS "
                             "ORDER AND TRIED; THE WINDOW AT KNOTS GRADED BY OCTAVE REGISTERED AND COMPUTED; THE AUTHOR`S RULINGS ENTERED; ONE KEY; "
                             "NO DEPOSIT, UNDER (R377)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b766's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b767 at Component 4: b766's
lines read banks this act does not write, and are not carried; the lines are b767's: the steps of (4)(b) to (4)(d) compiled at the closing
Lean commit, and the build from source tried, its closing pair, main and the tag, each read from the runner by its run id (KERNEL); the one
key of (8) by its planted control, the certificate's three forms of (4)(a), the source-build read of (5)(a)-(b), the data files of (4)(c)
and (4)(d), the dispatch tool and the reproduction run of (12) by their controls (CERTIFIED); the corrigendum, the price with the ceiling
read before the lock, the plan amended, the window at graded knots with its registration and the lines of (4) to (7) with the roster
(REGISTERED); the proof by the banked window, carried by [P2], and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b767, Component 4 (the Edit tool): the report's lines rewritten for b767's own banks, each figure from the record tool's figures
    # ### over them (REC._figs, record sections 4 and 5), the record's guard first; [P2]'s fields read at PLACE-papers HEAD by its line
    # ### (REC._ot_line), in the words tools/b767_rulings.py filled (P2_NAMES carries semicolons, P2_STEP commas), nothing typed. b766's
    # ### lines (its three repairs, the captures' masking, the data files of its (4)(c)-(d), its three readings, its two stopped builds)
    # ### read banks b767 does not write, and are not carried
    REC._guard(f)
    rs_, le_ = f['rep_states'], f['led_entered']
    g_ = dict((x_['group'], x_) for x_ in f['led_groups'])
    runs_ = sorted(f['runs'], key=lambda r_: r_['n'])
    on_ = [r_ for r_ in runs_ if r_['restore'] == 'on']
    on_ok_ = [r_ for r_ in on_ if str(r_['exit']) == '0']
    tn_, tf_, cl_, rr_ = ([r_ for r_ in runs_ if r_['item'] == i_] for i_ in ('trial-on', 'trial-off', 'closing', 'repeat'))
    p2m_ = re.search(r"of the plan[’']s four lemmas left by b766, compiled at (\w+) on push-b767-proof: (.+?); the step that did not compile, or was not sent "
                     r"within the hours of \(3\): (.+?), not sent; the proof continues there\.", REC._ot_line(*le_['P2'])) if 'P2' in le_ else None
    if not p2m_ or 'S2' not in le_ or not (tn_ and tf_ and cl_ and on_ok_):
        sys.exit('### [P2] AND [S2] AT HEAD, THE TRIAL`S TWO RUNS, THE CLOSING BUILD AND A RESTORED EXIT 0 NOT ALL READ -- NO LINE COMPOSED')
    # ------------------------------------------------------------------ KERNEL: (R377)(4)(b)-(d), the steps compiled, each read by its run id (the seat the template appends)
    sk = seat('%s_ledgers_c5.txt' % ACT, '  P2 ')
    sl_ = seat('%s_controls.txt' % ACT, '  THE LAST STEP`S DISPATCH: ')
    keys['STEPS'] = ('KERNEL -- THE STEPS OF (4)(b) TO (4)(d) COMPILED ((R377)(4), each read from the runner by its run id, the exit file governing): [P2] at '
                     'OPEN_TRAILS :%d, of the plan’s four lemmas left by b766, compiled at %s on push-b767-proof: %s; the %d theorems of SIDEExplicitFormula.Window '
                     'there each read at its statement by the E0 gate, each compiled at run %s with the restore on, its axioms within the standard three; %d runs '
                     'with the restore on exiting 0 of %d sent, %d of them steps of (4); the last step dispatched at %s. SOURCE %s ; %s.' % (
                         le_['P2'][0], p2m_.group(1)[:8], p2m_.group(2), (g_['c5']['e0'] or (0, 0))[1], on_ok_[-1]['run'], len(on_ok_), len(on_),
                         sum(1 for r_ in on_ if r_['item'] != 'trial-on'), f['tr_last'], sk['text'], sl_['text']))
    seats.append(sl_)
    # ------------------------------------------------------------------ KERNEL: (R377)(4), (5)(c), the trial, the closing pair, main and the tag
    ss_ = seat('%s_ledgers_c5.txt' % ACT, '  S2 ')
    sm_ = seat('%s_controls.txt' % ACT, '  MAIN AND THE TAG: ')
    c_ = cl_[-1]
    keys['MAIN'] = ('KERNEL -- THE BUILD FROM SOURCE TRIED, THE CLOSING PAIR, MAIN AND THE TAG ((R377)(4), (5)(c)): the trial at the act’s opening Lean commit, '
                    'run %s with the restore on and run %s with the restore off by route (%s), %s, entered at OPEN_TRAILS :%d; the closing build at the closing '
                    'Lean commit %s by the same route, run %s with the restore off, exit %s, part one %s modules, its low %s MB against the hold’s 2,560, build '
                    '%s min, its axioms file sha256 %s; THE PAIR: %s; MAIN AND THE TAG: %s; %d repeats sent; main at %s and %s (object %s) peeling to it, each '
                    'read back at the remote; push-b766-proof at %s. SOURCE %s ; %s.' % (
                        tn_[-1]['run'], tf_[-1]['run'], f['sb_route'][0], f['tr_trial_line'], le_['S2'][0], (K.RUNNER_COMMIT or '-')[:8], c_['run'],
                        c_['exit'], c_['p1_mods'], c_['low_p1'], c_['build_min'], c_['ax_sha'], f['tr_pair_line'], f['tr_main_line'], len(rr_),
                        (K.EF_MAIN or '-')[:8], K.WEIL_TAG[0], K.WEIL_TAG[1][:8], K.WEIL_BRANCH_B766[1][:8], ss_['text'], sm_['text']))
    seats.extend([ss_, sm_])
    # ------------------------------------------------------------------ HELD: (R377)(4)(b)-(e), the proof carried by [P2]
    sp_ = seat('%s_plan.txt' % ACT, '## THE LEMMAS, IN THE ORDER OF SENDING')
    keys['PROOF'] = ('HELD -- THE PROOF BY THE BANKED WINDOW, CARRIED BY [P2] ((R377)(4)(b)-(e)): of the plan’s %d parts, the step not sent within the hours '
                     'of (3): %s; the last step dispatched at %s, before the hour %s, and the closing build sent at %s; W-ORD-LI-ARITH carried, the proof '
                     'continuing there. SOURCE %s ; %s.' % (len(f['plan_lemmas']), p2m_.group(3), f['tr_last'], f['tr_last_hour'], c_['at'], sp_['text'], sk['text']))
    seats.append(sp_)
    # ------------------------------------------------------------------ REGISTERED: (R377)(1), the corrigendum for b766
    sc_ = seat('%s_corrigendum.txt' % ACT, '**ITEMS ')
    keys['CORRIGENDUM'] = ('REGISTERED -- THE CORRIGENDUM FOR b766, SHORT ((R377)(1)): %s items, CLAIM %s, CLOSE %s, %s repeats; the findings after b766’s lock '
                           'entered as events, CLAIM %s, CLOSE %s, REPEAT %s, and the navigator’s claims of (1) as CLAIM items; at FINDINGS :%s, the corrigenda '
                           'bank’s row (%s); PLACE-papers %s. SOURCE %s.' % (
                               f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_findings'][0], f['corr_findings'][1],
                               f['corr_findings'][2], f['corr_line'], f['corr_row'], K.C1_PP[:8], sc_['text']))
    seats.append(sc_)
    _B766_REPORT_2 = r'''
    sf_ = seat('%s_ledgers_c3.txt' % ACT, '  F1 ')
    keys['STEPS'] = ('KERNEL -- THE STEPS OF (4)(b) TO (4)(d) COMPILED ((R377)(4), each read from the runner by its run id, the exit file governing): [F1] at OPEN_TRAILS :%d, the prime '
                     'side as a finite sum at %s; [F2] at :%d, the data file and the three theorems of the window at %s, the E0 gate %d of %d; [P2] at :%d, of the plan’s %s lemmas, compiled at '
                     '%s on %s: %s; the %d theorems of SIDEExplicitFormula.Window there each read at its statement by the E0 gate, each compiled at run %s with the restore on, its axioms '
                     'within the standard three; %d runs with the restore on exiting 0 of %d sent. SOURCE %s ; %s.' % (
                         le_['F1'][0], kc_.get('prime', '-')[:8], le_['F2'][0], kc_.get('window', '-')[:8], (g_['c3']['e0'] or (0, 0))[0], (g_['c3']['e0'] or (0, 0))[1], le_['P2'][0],
                         p2m_.group(1), p2m_.group(2)[:8], p2m_.group(3), p2m_.group(5), (g_['c5']['e0'] or (0, 0))[1], on_ok_[-1]['run'] if on_ok_ else '-', len(on_ok_), f['tr_on'][0],
                         sf_['text'], sk['text']))
    seats.append(sf_)
    # ------------------------------------------------------------------ HELD: (R376)(4)(d), the proof carried by [P2]
    sp_ = seat('%s_plan.txt' % ACT, '## THE LEMMAS, IN THE ORDER OF SENDING')
    keys['PROOF'] = ('HELD -- THE PROOF BY THE BANKED WINDOW, CARRIED BY [P2] ((R377)(4)(d)): of the plan’s %s lemmas, not sent: %s; ratified by the author’s word (relay '
                     'data/b767_author_words_preseal.txt :29); W-ORD-LI-ARITH carried, the proof continuing there. SOURCE %s ; %s.' % (p2m_.group(1), p2m_.group(6), sp_['text'], sk['text']))
    seats.append(sp_)
    # ------------------------------------------------------------------ HELD: (R376)(4), the closing build from source and its repeat, main and the tag
    sb_ = seat('%s_controls.txt' % ACT, '  MAIN AND THE TAG: ')
    keys['BUILD'] = ('HELD -- THE CLOSING BUILD FROM SOURCE AND ITS REPEAT, EACH STOPPED UNDER THE HOLD ((R377)(4) and the author’s word of 2026-11-22): runs %s at the closing Lean '
                     'commit %s with the restore off, each exit file 143 and its axioms file one line; THE PAIR: %s; MAIN AND THE TAG: %s; no [C7] line, by the author’s word (relay '
                     'data/b767_author_words_preseal.txt :32); the finding, that a build from source with the Window files does not pass the hold, carried to the next ruling. SOURCE %s.' % (
                         ' and '.join(str(r_['run']) for r_ in off_), (K.RUNNER_COMMIT or '-')[:8], f['tr_pair_line'], f['tr_main_line'], sb_['text']))
    seats.append(sb_)
    # ------------------------------------------------------------------ REGISTERED: (R376)(1), the corrigendum for b765
    sc_ = seat('%s_corrigendum.txt' % ACT, '**ITEMS ')
    keys['CORRIGENDUM'] = ('REGISTERED -- THE CORRIGENDUM FOR b766, SHORT: %s items, CLAIM %s, CLOSE %s, %s repeats; b766’s %s CLAIM items printed in full; the findings after its lock '
                           'entered as events, the navigator’s own as CLAIM; at FINDINGS :%s, the corrigenda bank’s row (%s); PLACE-papers %s. SOURCE %s.' % (
                               f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'], f['corr_line'], f['corr_row'], K.C1_PP[:8], sc_['text']))
    seats.append(sc_)
'''   # ### b767, Component 4: b766's lines of this section above, kept as a string, not run
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: (R377)(8), the one key by its planted control
    sv = seat('%s_repairs.txt' % ACT, '    [K25] CLASS ')
    keys['REPAIRS'] = ('CERTIFIED -- THE ONE KEY OF (8), BY ITS PLANTED CONTROL: [K25], the kernel route for b767, %s; tools/standing/ from %s to %s by %d '
                       'commit, VERSION moved by it, the control read at the commit before the change and at its commit, both printed, a second kernel’s name '
                       'planted and read refused. SOURCE %s.' % (
                           ', '.join(r_['state'] for r_ in f['reps'] if r_['key'] == 'K25'), f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: (R377)(4)(a), the certificate's three forms by its controls
    sce_ = seat('%s_certificate.txt' % ACT, '**THE THREE FORMS READ: ')
    keys['CERTIFICATE'] = ('CERTIFIED -- THE CERTIFICATE’S THREE FORMS OF (4)(a), READ WITH NO DISPATCH BEFORE THE PLAN: %s; its controls %d of %d as wanted; the '
                           'form L10 encloses stated in the plan; no r, no K(n) and no window coefficient printed. SOURCE %s.' % (
                               '; '.join('(%s) %s, %s constants, the sum of the |r| %s, one width %d digits' % (k_, w_, '{:,}'.format(n_), s_, wd_)
                                         for k_, w_, n_, s_, _nd, wd_ in f['cert_forms']), f['cert_ctl'][0], f['cert_ctl'][1], sce_['text']))
    seats.append(sce_)
    # ------------------------------------------------------------------ CERTIFIED: (R377)(5)(a), (b), the source-build read and its route
    ssb_ = seat('%s_source_build.txt' % ACT, '**THE READ MADE: ')
    keys['SOURCEBUILD'] = ('CERTIFIED -- THE READ OF THE TWO STOPPED RUNS AND THE ROUTE OF (5)(a) AND (b), NO DISPATCH: its controls %d of %d as wanted; the route '
                           'chosen, (%s): %s; part one the target’s %d modules outside SIDEExplicitFormula/Window/ by name, their closure %d; a larger runner priced '
                           'in the bank and not ordered. SOURCE %s.' % (
                               f['sb_ctl'][0], f['sb_ctl'][1], f['sb_route'][0], f['sb_route'][1].replace('`', '’'), f['sb_part1'][0], f['sb_part1'][1], ssb_['text']))
    seats.append(ssb_)
    # ------------------------------------------------------------------ CERTIFIED: (R377)(4)(c), (d), the data files of L10a and L11b by their controls
    sd_ = seat('%s_logdata.txt' % ACT, '  CONTROLS ')
    sn_ = seat('%s_natdata.txt' % ACT, '  CONTROLS ')
    keys['DATA'] = ('CERTIFIED -- THE DATA FILES OF (4)(c) AND (4)(d), EACH WRITTEN BY A RELAY TOOL COMMITTED BEFORE ITS RUN AND READ BY ITS CONTROLS: L10a’s prime '
                    'table, %s keys (the primes up to %s), the series’ lengths the most %d and the sum %s, blocks %s, the widest interval %s against 2/10^22, '
                    'controls %d of %d; L11b’s factor runs, %s lists (m from 1 to %s), %s factor pairs, the most in one list %d, controls %d of %d. SOURCE %s ; %s.' % (
                        '{:,}'.format(f['ld_keys']), f['ld_upto'], f['ld_most'], '{:,}'.format(f['ld_sum']), f['ld_blocks'], f['ld_widest'], f['ld_ctl'][0],
                        f['ld_ctl'][1], '{:,}'.format(f['nd_lists']), f['nd_upto'], '{:,}'.format(f['nd_pairs']), f['nd_most'], f['nd_ctl'][0], f['nd_ctl'][1],
                        sd_['text'], sn_['text']))
    seats.extend([sd_, sn_])
    # ------------------------------------------------------------------ CERTIFIED: the dispatch and read tool by its own controls (the seat the template appends)
    sw = seat('%s_controls_control.txt' % ACT, '**THE TOOL`S CONTROLS: ')
    keys['CONTROLS'] = ('CERTIFIED -- tools/b767_controls.py BY ITS OWN CONTROLS: %d of %d as wanted, committed before its opening dispatch; every run read by its id '
                        'from the downloaded artifact, the exit file governing; %d dispatches of SIDE-explicit-formula of at most %d, %d with the restore on of at '
                        'most %d, with the restore off the trial %d, the closing build %d and repeats %d; %d in SIDE-dirichlet-mod-24. SOURCE %s.' % (
                            f['cc_ctl'][0], f['cc_ctl'][1], f['disp_ef'], K.MAX_DISPATCHES, f['tr_on'][0], f['tr_on'][1], len(tf_), len(cl_), len(rr_),
                            f['disp_m24'], sw['text']))
    # ------------------------------------------------------------------ CERTIFIED: (R377)(12), the reproduction run
    sr_ = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED: tools/research/reproduce.py’s full run in the foreground, rows %d, reproducing %d, differing %d, '
                     'not run %d (%s), the planted controls %d of %d as wanted, %d s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0],
                         f['rp_ctl'][1], f['rp_secs'], sr_['text']))
    seats.append(sr_)
    _B766_REPORT_3 = r'''
    sv = seat('%s_repairs.txt' % ACT, '    [K22] CLASS ')
    keys['REPAIRS'] = ('CERTIFIED -- THE THREE REPAIRS ((R377)(7)), EACH BY ITS PLANTED CONTROL: tools/standing/ from %s to %s by %d commits, VERSION moved by each, the control read at '
                       'the commit before each change and at its commit, both printed; %d repaired, %d read as designed, %d removed, %d carried; push-b766-planted removed at the kernel’s '
                       'remote and in its clone after [K22]. SOURCE %s.' % (
                           f['st_entering'], f['st_version'], len(K.STANDING_REPAIRS), len(rs_['REPAIRED']), len(rs_['READ AS DESIGNED']), len(rs_['REMOVED']), len(rs_['CARRIED']), sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: [K23], b765's captures masked
    sm_ = seat('%s_capture_mask.txt' % ACT, '**FILES ')
    keys['MASK'] = ('CERTIFIED -- b766’S CAPTURES MASKED AFTER [K23]: files %d, the name %d times before and %d after, the mask’s control %d of %d as wanted; the fifteen captures of b763 '
                    'and b764 not opened. SOURCE %s.' % (f['mask'][0], f['mask'][3], f['mask'][4], f['mask_ctl'][0], f['mask_ctl'][1], sm_['text']))
    seats.append(sm_)
    # ------------------------------------------------------------------ CERTIFIED: (R376)(4)(a), the certificate by its controls
    sce_ = seat('%s_certificate.txt' % ACT, '**THE CERTIFICATE BANKED, ')
    keys['CERTIFICATE'] = ('CERTIFIED -- THE CERTIFICATE OF (4)(a), BANKED AS DATA BEFORE ANY DISPATCH, [%s]: K(n) as exact rationals at %d n, the arithmetic side one combination over %s '
                           'primes with exact rational coefficients, its largest numerator %s digits, the budget %s constants; its controls %d of %d as wanted; %s. SOURCE %s.' % (
                               f['cert_key'], f['cert_k'], '{:,}'.format(int(f['cert_primes'])), f['cert_digits'], '{:,}'.format(int(f['cert_budget'][0])), f['cert_ctl'][0],
                               f['cert_ctl'][1], f['cert_form'], sce_['text']))
    seats.append(sce_)
    # ------------------------------------------------------------------ CERTIFIED: (R376)(4)(c) and (d), the data files by their controls
    sd_ = seat('%s_window_data.txt' % ACT, '**THE DATA FILE WRITTEN AND READ BACK')
    keys['DATA'] = ('CERTIFIED -- THE DATA FILES OF (4)(c) AND (4)(d), EACH WRITTEN BY A RELAY TOOL COMMITTED BEFORE ITS RUN AND READ BACK BY ITS CONTROL: %s; no coefficient and no '
                    'value printed. SOURCE %s.' % ('; '.join('%s %d of %d' % (REC.DATA_FILES.get(n_, n_), a_, b_) for n_, a_, b_ in f['data_ctl']), sd_['text']))
    seats.append(sd_)
    # ------------------------------------------------------------------ CERTIFIED: the dispatch and read tool by its own controls (the seat the template appends)
    sw = seat('%s_controls_control.txt' % ACT, '**THE TOOL`S CONTROLS: ')
    keys['CONTROLS'] = ('CERTIFIED -- tools/b767_controls.py BY ITS OWN CONTROLS: %d of %d as wanted, committed before its opening dispatch; every run read by its id from the downloaded '
                        'artifact, the exit file governing, %d dispatches in SIDE-explicit-formula of at most %d, %d with the restore on of at most %d, the build from source and its '
                        'repeat one each, and none elsewhere. SOURCE %s.' % (
                            f['cc_ctl'][0], f['cc_ctl'][1], f['disp_ef'], K.MAX_DISPATCHES, f['tr_on'][0], f['tr_on'][1], sw['text']))
    # ------------------------------------------------------------------ CERTIFIED: (R376)(11), the reproduction run
    sr_ = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED: tools/research/reproduce.py’s full run in the foreground, rows %d, reproducing %d, differing %d, not run %d (%s), '
                     'the planted controls %d of %d as wanted, %d s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1],
                         f['rp_secs'], sr_['text']))
    seats.append(sr_)
'''   # ### b767, Component 4: b766's lines of this section above, kept as a string, not run
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: (R377)(3), the price table and the ceiling read before the lock
    sq = seat('%s_price.txt' % ACT, '**THE PRICE TABLE: ')
    sce = seat('%s_ceiling.txt' % ACT, '**THE CEILING READ BEFORE THE LOCK')
    keys['PRICE'] = ('REGISTERED -- THE PRICE AND THE CEILING OF (3): the table banked before Component 1 from banked timings, step zero %s h, the lower sum %s h '
                     'against the ceiling %d h with %s h in reserve, the upper sum %s h, dispatches %d to %d of at most %d, the last step dispatch by %s; the ceiling '
                     'read before the lock at %s: %s h spent from the opening row, the last step dispatch at %s, %s h from it, %s h left of %d with the reserve %d h, '
                     'the close at b766’s %s h from its lock, %s h from the opening row: %s. SOURCE %s ; %s.' % (
                         f['pr_step0'], f['pr_lower'], f['pr_ceiling'], f['pr_reserve'], f['pr_upper'], f['pr_disp'][0], f['pr_disp'][1], f['pr_cap'], f['pr_last'],
                         f['ce_at'], f['ce_spent'], f['ce_last'], f['ce_last_h'], f['ce_left'], f['ce_ceiling'], f['ce_reserve'], f['ce_b766'], f['ce_close'],
                         f['ce_word'].lower(), sq['text'], sce['text']))
    seats.extend([sq, sce])
    # ------------------------------------------------------------------ REGISTERED: (R377)(4)(a), the plan amended
    spl = seat('%s_plan.txt' % ACT, '## THE FORM L10 ENCLOSES')
    keys['PLAN'] = ('REGISTERED -- THE PLAN AMENDED OF (4)(a), COMMITTED BEFORE ANY DISPATCH: %d parts in the order of sending, %s, each with its statement’s opening, '
                    'its kind, the datum of the certificate it consumes and its price; the form L10 encloses and why; the budget in the Lean beside the '
                    'certificate’s; at relay %s. SOURCE %s.' % (
                        len(f['plan_lemmas']), ', '.join('%s %s' % (l_, n_) for l_, n_ in f['plan_lemmas']), f['plan_commit'], spl['text']))
    seats.append(spl)
    # ------------------------------------------------------------------ REGISTERED: (R377)(6), the registration and the window at graded knots
    srg_ = seat('%s_registration.txt' % ACT, 'H-GRADED-WINDOW. THE OBJECT')
    swn_ = seat('%s_window.txt' % ACT, '  H-GRADED-WINDOW: ')
    keys['WINDOW'] = ('REGISTERED -- THE WINDOW AT KNOTS GRADED BY OCTAVE OF (6), H-GRADED-WINDOW %s, [%s]: the registration committed alone at relay %s before the '
                      'tool’s run; %s at the uniform window, S %s against the banked -6.62468014575; at %d knots and %d coefficients the control’s arithmetic side '
                      'S %s +- %s; reported beside it, unregistered: rational products %d, the combination’s primes %d, constants %d, the sum of the |r| %s, the '
                      'budget’s one width %d digits; %s h from the registration’s commit against the price’s upper %s h; no step of the proof moved to it, nothing '
                      'computed at a zero, the window’s frequency not printed. SOURCE %s ; %s.' % (
                          f['win_reading'], f['win_key'], f['win_reg'][:8], f['win_control'].lower(), f['win_uniform'], f['win_knots'], f['win_ncoef'], f['win_S'],
                          f['win_rad'], f['win_products'], f['win_primes'], f['win_constants'], f['win_sumr'], f['win_digits'], f['win_hours'], f['win_upper'],
                          srg_['text'], swn_['text']))
    seats.extend([srg_, swn_])
    # ------------------------------------------------------------------ REGISTERED: (R377)(4)-(7), the lines in OPEN_TRAILS by group, with the roster
    sg = seat('%s_ledgers_c2.txt' % ACT, '**THE LEDGERS, GROUP C2: ')
    sg5_ = seat('%s_ledgers_c5.txt' % ACT, '**THE LEDGERS, GROUP C5: ')
    so = seat('%s_orders.txt' % ACT, '**ORDERS ')
    ks_ = []
    for k_ in f['led_keys']:
        if k_.split('.')[0] not in ks_:
            ks_.append(k_.split('.')[0])
    keys['LEDGERS'] = ('REGISTERED -- THE LINES OF (4) TO (7) IN OPEN_TRAILS, IN %d GROUPS: %d lines entered, each group under its own dated head, no line moving: '
                       '%s; the orders added %s; REGISTRY, ERRATA, the census, the register and the two files of the map not written; controls %s; the roster %d '
                       'open before and %d after; at HEAD orders %d, open %d, closed %d. SOURCE %s ; %s ; %s.' % (
                           len(f['led_groups']), sum(x_['lines'] for x_ in f['led_groups']), ', '.join('[%s]' % k_ for k_ in ks_),
                           ', '.join(f['led_roster'][2]) or 'none', ', '.join('%d of %d' % tuple(c_) for c_ in f['led_ctl']), f['led_roster'][0],
                           f['led_roster'][1], f['ord_head'][0], f['ord_head'][1], f['ord_head'][2], sg['text'], sg5_['text'], so['text']))
    seats.extend([sg, sg5_, so])
    _B766_REPORT_4 = r'''
    pr_ = f['pr_rows']
    # ### b764, Component 6 (the Edit tool): a range printed once where its ends are equal, as the entry prints it
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    pw_ = lambda k_: '%s over %s' % (rg_(pr_[k_]['lo_h'], pr_[k_]['hi_h'], 'h'), rg_(pr_[k_]['dispatches'][0], pr_[k_]['dispatches'][1], 'dispatches'))
    # ------------------------------------------------------------------ REGISTERED: (R376)(3), the price table and the ceiling's reading after (4)(c)
    sq = seat('%s_price.txt' % ACT, '**THE PRICE TABLE: ')
    sce = seat('%s_ceiling.txt' % ACT, '**THE CEILING READ AFTER (4)(c)')
    keys['PRICE'] = ('REGISTERED -- THE PRICE AND THE CEILING OF (3): the table banked before Component 1 from banked timings, step zero %s h, the lower sum %s h against %d h, %s, the '
                     'upper sum %s h; the ceiling read after (4)(c) at %s, %s h spent and %s h of the rows left at their lower figures, %s h against %d h, under by %s h, %s. SOURCE %s ; %s.' % (
                         f['pr_step0'], f['pr_lower'], f['pr_ceiling'], f['pr_carried'].lower(), f['pr_upper'], f['ce_at'], f['ce_spent'], f['ce_left'], f['ce_sum'], f['ce_ceiling'],
                         f['ce_under'], f['ce_word'].lower(), sq['text'], sce['text']))
    seats.extend([sq, sce])
    # ------------------------------------------------------------------ REGISTERED: (R376)(4)(a), the plan
    spl = seat('%s_plan.txt' % ACT, '## THE LEMMAS, IN THE ORDER OF SENDING')
    keys['PLAN'] = ('REGISTERED -- THE PLAN OF (4)(a), COMMITTED WITH THE CERTIFICATE BEFORE ANY DISPATCH: %d lemmas in the order of sending, each with its kind, its datum and its price, '
                    'at relay %s. SOURCE %s.' % (len(f['plan_lemmas']), f['plan_commit'], spl['text']))
    seats.append(spl)
    # ------------------------------------------------------------------ REGISTERED: (R376)(5), the three readings
    sx1 = seat('%s_registry_cells.txt' % ACT, '**THE REGISTRY`S ROWS: ')
    sx2 = seat('%s_lean_join.txt' % ACT, '**THE LEAN JOINED TO THE PAPERS: ')
    sx3 = seat('%s_sweep.txt' % ACT, '**THE LEDGER AGAINST THE KEYSTONES: ')
    keys['READINGS'] = ('REGISTERED -- THE THREE READINGS TOWARD THE KEYSTONE SET, EACH A READING AND NO BUILD ((R377)(5)): (a) the registry’s rows, %d rows of %d tables, KEYSTONE %d, '
                        'UNPLACED %d, [X1]; (b) the Lean joined to the papers, declarations %s, named by a paper’s table %d, on a generated page alone %d, by neither %s, the navigator’s '
                        'candidate %s, [X2]; (c) the findings ledger against the keystones, entries %d, with a name the reader takes %d, no keystone %d, no such name %d, [X3]; no line of '
                        'REGISTRY, of the census or of a paper written. SOURCE %s ; %s ; %s.' % (
                            f['x1'][0], f['x1'][1], f['x1'][2], f['x1'][3], '{:,}'.format(f['x2'][0]), f['x2'][1], f['x2'][2], '{:,}'.format(f['x2'][3]), f['x2'][4].lower(),
                            f['x3'][0], f['x3'][1], f['x3'][4], f['x3'][5], sx1['text'], sx2['text'], sx3['text']))
    seats.extend([sx1, sx2, sx3])
    # ------------------------------------------------------------------ REGISTERED: (R376)(4)-(6), the lines in OPEN_TRAILS in four groups, with the roster
    sg = seat('%s_ledgers_c2.txt' % ACT, '**THE LEDGERS, GROUP C2: ')
    so = seat('%s_orders.txt' % ACT, '**ORDERS ')
    ks_ = []
    for k_ in f['led_keys']:
        if k_.split('.')[0] not in ks_:
            ks_.append(k_.split('.')[0])
    keys['LEDGERS'] = ('REGISTERED -- THE LINES OF (4) TO (6) IN FOUR GROUPS AND THE AUTHOR’S WORDS: OPEN_TRAILS took %d lines, each group under its own dated head, no line moving: %s; '
                       'REGISTRY, ERRATA, the census, the register and the two files of the map not written; controls %s; the roster %d open before and %d after; at HEAD orders %d, '
                       'open %d, closed %d. SOURCE %s ; %s.' % (
                           sum(x_['lines'] for x_ in f['led_groups']),
                           ', '.join(('[Q2] x %d' % sum(1 for k2_ in le_ if k2_.split('.')[0] == 'Q2')) if k_ == 'Q2' else '[%s]' % k_ for k_ in ks_),
                           ', '.join('%d of %d' % tuple(c_) for c_ in f['led_ctl']), f['led_roster'][0], f['led_roster'][1], f['ord_head'][0], f['ord_head'][1], f['ord_head'][2],
                           sg['text'], so['text']))
    seats.extend([sg, so])
'''   # ### b767, Component 4: b766's lines of this section above, kept as a string, not run
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R377)(12)) (the seat the template appends)
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    # ### b767, Component 4 (the Edit tool): each line's tier as its key gives it -- the steps compiled and the build from source with main
    # ### and the tag KERNEL; the one key, the certificate, the source-build read, the data files, the dispatch tool and the reproduction run
    # ### CERTIFIED; the corrigendum, the price, the plan, the window and the lines REGISTERED; the proof carried by [P2] and the draft HELD
    order = [('KERNEL', ['STEPS', 'MAIN']),
             ('CERTIFIED', ['REPAIRS', 'CERTIFICATE', 'SOURCEBUILD', 'DATA', 'CONTROLS', 'REPRO']),
             ('REGISTERED', ['CORRIGENDUM', 'PRICE', 'PLAN', 'WINDOW', 'LEDGERS']),
             ('HELD', ['PROOF', 'HELD'])]
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
