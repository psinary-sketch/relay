# -*- coding: utf-8 -*-
# b763 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R373)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R373)(2) repair it carries. Edited by the Edit tool. Carried at b763 by tools/b763_fold.py (`carry`) from tools/acts/b762.py,
# b762`s names substituted; the citation`s sections adopted from tools/b763_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b762`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b762`s carried till
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
# ### b763, Component 1: THE c1 ROUTE FOR b762'S SHORT CORRIGENDUM, (R373)(1), written by the Edit tool against b762's banks (59 events, 11
# ### defects, 2 refusals; no post-seal events bank at b762), the seventeen findings after b762's lock, entered as this act's events from the
# ### seat's own closing message (data/b763_events.txt (14)-(30)), and the navigator's own (i)-(v), entered as the navigator's, CLAIM (rows
# ### (31)-(35)), printed in full in the ruling's words read from the ferry bank (data/b763_ferry.txt :9), each row read against them. b762's
# ### banks carry six CLAIM rows (its events (24)-(29)), each printed in full in its bank's words. [I1] entered from the ferry bank by its
# ### markers, its one field filled from SPIRAL_MAP's cluster table (the row naming d1-8 or the page; "Day 1" where none does) and nothing else
# ### changed, REGISTRY's row d1-8 read by predicate. (1) states b762's weight from its closing's head and orders no line of its own, so the
# ### weight route refuses; (9) carries OPEN_TRAILS' lines under one dated head, so the next route too. (11)'s six items are named with their
# ### rows. b762's route (tools/acts/b762.py :28-:282) carried by hand in place of the stub; nothing composed by the stub. The title under the
# ### title rule: no backtick (titlerule.py, v1.35.8).
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_NOTED = '2026-11-19'
C1_CORRIGENDA_LAST = 82
C1_ROW = re.compile(r"^\(((?:[a-z]'*)|\d+)\) (THE [A-Z' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
C1_BANKS = (('events', 'b762_events.txt'), ('defects', 'b762_defects.txt'))
C1_EVENTS_N = 59
C1_DEFECTS = (11, 'k')
C1_REFUSALS = 2
C1_CLAIMS = tuple(('events', str(i_)) for i_ in range(24, 30))   # ### b762's banks: six CLAIM rows, its events (24)-(29) (the counter at data/b762_closing.txt :5, CLAIM 6)
C1_HEAD = ('b762 closed: relay efb9acb6, PLACE-papers 87cab4f; suite 111 of 116;', 'scores 7 of 8 HELD; 11 defects')   # ### data/b762_closing.txt :1, read by the state
C1_FINDINGS_BANK = 'b763_events.txt'
C1_FINDINGS_IDS = tuple(str(i_) for i_ in range(14, 31))
C1_NAV_IDS = tuple(str(i_) for i_ in range(31, 36))
C1_NAV_MARKS = ('i', 'ii', 'iii', 'iv', 'v')
C1_RULED = (('14', ('15:36:25Z', '430 s', 'G-DELETE-FREE')), ('15', ('15:45:50Z', '274 s')), ('16', ('15:50:32Z', '92 passing', '23 failing')),
            ('17', ('15:50:50Z', '248 s', '5 changed')), ('18', ('15:55:13Z', '441 s', 'DIVERGE 16')), ('19', ('16:04:43Z', '204 s', "KeyError 'registration'")),
            ('20', ('16:08:54Z', 'exited 0')), ('21', ('16:09:48Z', '027ae0f1')), ('22', ('16:18:37Z', '16:36:46Z', ':18953')),
            ('23', ('16:22:51Z', '581.6 s', '593 s')), ('24', ('190356', '16:35:26', '16:35:51Z')), ('25', ('16:37:06Z', 'marker')),
            ('26', ('16:40:29Z', '17:32:10Z', '444 s', '383 s')), ('27', ('17:25:28Z', '18:14:15Z', 'run cache')), ('28', ('17:28:57Z', '21.17 s')),
            ('29', ('18:18:20Z', ':229', 'ROWS 33')), ('30', ('18:20:19Z', 'b763_address_scan_commits.txt')))   # ### the closing message's "Findings after the lock" list, its seventeen items in its order
C1_REPAIRS = (('those (R372)(11) names', "b762's corrigendum, data/b762_corrigendum.txt, eight by name"),
              ("the KeyError on 'registration' in two arms of the pass in the previous act's mode, of one class with the KeyError on 'pp_epstein'", "b761's events (25); b763's events (19)"),
              ("the closing's touch-read row, which reads a figure the touch bank quotes and not that bank's foot", "b762's events (55); b763's events (29)"),
              ('step [21] of the close order, not taken at two acts', "the closing messages of b761 and b762; b763's events, the head of rows (14)-(30)"),
              ("the desk route's marker, not met at two acts", "b763's events (25)"),
              ("the rule arms and the parts that pass by reading nothing, named as b762's finding 14 names them", "b763's events (27)"))   # ### (R373)(11), in its order and words
C1_I1 = ('---- [I1] for the corrigendum, one line', '---- end [I1]')
C1_I1_FIELD = '<the cluster SPIRAL_MAP\'s table gives d1-8, or "Day 1" where the table gives none>'
C1_CORR_TITLE = ('## Corrigendum to b762’s record, short (relay data/b762_events.txt rows (1)-(59) and data/b762_defects.txt (a)-(k)): its events and '
                 'defects by count from their banks, its six CLAIM items printed in full, the findings after the lock entered as events with their '
                 'times, the navigator’s own entered as CLAIM, its integration read from REGISTRY’s row d1-8 by [I1], and the repairs of (R373)(11) '
                 'carried by name')
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
    """a bank's own words for the ledger (b754's form, carried): markdown's marks escaped; a pair of backticks quoting a span read as quotes,
    every other backtick as an apostrophe; the template's placeholder brackets as angles."""
    s = s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_')
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
    """the navigator's own, (i)-(v), in (R373)(1)'s words: the ferry bank's one line opening "(1) b762 AT ITS WEIGHT.", its text after
    "CLAIM: " cut at each mark; [(mark, words)], the words with their closing ";" or "." removed. Any other count exits, nothing composed."""
    (t_,), _l = _c1_fl('%s_ferry.txt' % ACT, r'^\(1\) b762 AT ITS WEIGHT\..*?each entered as the navigator.s, CLAIM: (.*)$', 'the navigator`s own')
    parts = re.split(r'(?:^|(?<=; ))\((i|ii|iii|iv|v|vi)\) ', t_)
    items = [(parts[i], parts[i + 1].rstrip().rstrip(';.').rstrip()) for i in range(1, len(parts) - 1, 2)]
    if [m_ for m_, _w in items] != list(C1_NAV_MARKS):
        sys.exit('### THE NAVIGATOR`S OWN: MARKS %s, NOT (i)-(v) -- NOTHING COMPOSED' % [m_ for m_, _w in items])
    return items, _l


def _c1_i1():
    """[I1], read from the ferry bank between its two marker lines, one line; its one field filled from SPIRAL_MAP's cluster table (the
    section opening '### Clusters', its table's rows read at PLACE-papers' tree): the cluster of the row naming d1-8 or the page's file stem,
    "Day 1" where no row names either; REGISTRY's row d1-8 read by predicate, one line naming d1-8 and the page's file stem. Any other count
    exits, nothing composed. Returns (text, its ferry line, the cluster, the table's row lines, the REGISTRY line)."""
    F = _c1_rd('%s_ferry.txt' % ACT).split(NL)
    a_ = [i for i, l in enumerate(F) if l == C1_I1[0]]
    b_ = [i for i, l in enumerate(F) if l == C1_I1[1]]
    if len(a_) != 1 or len(b_) != 1 or b_[0] - a_[0] != 2 or F[a_[0] + 1].count(C1_I1_FIELD) != 1:
        sys.exit('### [I1]: ITS MARKERS %s %s OR ITS FIELD NOT AS READ -- NOTHING COMPOSED' % (a_, b_))
    pp = os.path.dirname(R.FIND)
    S_ = _c1_rd('SPIRAL_MAP.md', pp).split(NL)
    h_ = [i for i, l in enumerate(S_) if l.startswith('### Clusters')]
    if len(h_) != 1:
        sys.exit('### SPIRAL_MAP: %d CLUSTER SECTIONS, NOT ONE -- NOTHING COMPOSED' % len(h_))
    rows_, named_, seen_ = [], [], False
    for i in range(h_[0] + 1, len(S_)):
        l = S_[i]
        if l.startswith('#'):
            break
        if l.startswith('|'):
            seen_ = True
            c_ = [x.strip() for x in l.split('|')]
            if len(c_) > 2 and c_[1] != 'Cluster' and not set(c_[1]) <= set('-: '):
                rows_.append(i + 1)
                if re.search(r'd1-8|ONE_PAGE_PROOF', l):
                    named_.append((i + 1, c_[1]))
        elif seen_ and not l.strip():
            break
    if not rows_ or len(named_) > 1:
        sys.exit('### SPIRAL_MAP`S CLUSTER TABLE: ROWS %d, NAMING d1-8 OR THE PAGE %s -- NOTHING COMPOSED' % (len(rows_), named_))
    cl_ = (re.match(r'\*\*(.+?)\*\*', named_[0][1]) or re.match(r'(.*)', named_[0][1])).group(1).strip() if named_ else 'Day 1'
    G_ = _c1_rd('REGISTRY.md', pp).split(NL)
    g_ = [i for i, l in enumerate(G_, 1) if re.search(r'(^|[|\s`])d1-8([|\s`]|$)', l) and 'ONE_PAGE_PROOF' in l]
    if len(g_) != 1:
        sys.exit('### REGISTRY: %d LINES NAMING d1-8 AND THE PAGE, NOT ONE -- NOTHING COMPOSED' % len(g_))
    return F[a_[0] + 1].replace(C1_I1_FIELD, cl_), a_[0] + 2, cl_, rows_, g_[0]


def _c1_state():
    s = dict((k_, _c1_rows(n_)) for k_, n_ in C1_BANKS)
    ev, df = s['events'], s['defects']
    tot = _c1_tally(ev + df)
    cnt, l_cn = _c1_fl('b762_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    head = _c1_rd('b762_closing.txt').split(NL)[0]
    rf = [l for l in _c1_rd('b762_hook_refusals.txt').split(NL) if l.strip()]
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
    i1, l_i1, cl_, rows_, l_g = _c1_i1()
    bad = [k_ for k_, ok_ in (
        ('the closing`s head as (1) reads it', all(h_ in head for h_ in C1_HEAD)),
        ('the event rows (1)-(%d)' % C1_EVENTS_N, [int(r[0]) for r in ev] == list(range(1, C1_EVENTS_N + 1))),
        ('no post-seal events bank at b762', not os.path.exists(os.path.join(D, 'b762_events_postseal.txt'))),
        ('the defect rows %d, the last (%s)' % C1_DEFECTS, len(df) == C1_DEFECTS[0] and df[-1][0] == C1_DEFECTS[1]),
        ('the counter the closing`s', (tot['claim'], tot['close'], tot['repeat'], tot['total'], len(df), len(ev)) == tuple(int(x) for x in cnt)),
        ('the CLAIM rows %s' % [(k_, r[0]) for k_, r in claims], [(k_, r[0]) for k_, r in claims] == list(C1_CLAIMS)),
        ('the refusals %d, each by its kind' % C1_REFUSALS, len(rf) == C1_REFUSALS and '?' not in kinds),
        ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr_) and max(cr_) == C1_CORRIGENDA_LAST),
        ('the seventeen findings, each with its date and time', all(fnd) and all(_c1_time(r[4]) for r in fnd)),
        ('the findings, each in its row: missing %s' % ruled, not ruled),
        ('the navigator`s own, each a CLAIM row in the ruling`s words: off %s' % nav_bad, not nav_bad),
    ) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (the tally %s)' % (bad, tot))
    s.update(tally=tot, l_counter=l_cn, refusals=len(rf), kinds=kinds, findings=fnd, claims=claims, nav=nav, l_nav=l_nav, nav_rows=nav_rows,
             i1=i1, l_i1=l_i1, cluster=cl_, cl_rows=rows_, l_reg=l_g)
    return s


def _c1_lines(s):
    t = s['tally']
    per = dict((k_, _c1_tally(s[k_])) for k_, _n in C1_BANKS)
    kinds = ', '.join('%s %d' % kv for kv in sorted(s['kinds'].items(), key=lambda kv: (-kv[1], kv[0])))
    pe, pd = per['events'], per['defects']
    ft = _c1_tally(s['findings'])
    L = ['*b762 closed at relay efb9acb6 and PLACE-papers 87cab4f, suite 111 of 116, scores 7 of 8 HELD, 11 defects, 1 prompt answered (relay '
         'data/b762_closing.txt :1); the relay’s main read back at 3fe5b17c after the closing push. Its events bank (relay data/b762_events.txt) '
         'carries %d rows, (1)-(%d): CLAIM %d, CLOSE %d, REPEAT %d; its defects bank (relay data/b762_defects.txt) %d lettered rows, (a)-(k): CLAIM '
         '%d, CLOSE %d, REPEAT %d. Together CLAIM %d, CLOSE %d, REPEAT %d of %d, as b762’s closing counter prints it (relay data/b762_closing.txt '
         ':%d). Its refusals bank %d lines (relay data/b762_hook_refusals.txt), by kind %s. No post-seal events bank at b762. Each item is tagged '
         'in its own bracket; the tags are the banks’ own and this entry edits none of them. Its %d CLAIM items are printed in full below.*' % (
             pe['total'], pe['total'], pe['claim'], pe['close'], pe['repeat'], pd['total'], pd['claim'], pd['close'], pd['repeat'],
             t['claim'], t['close'], t['repeat'], t['total'], s['l_counter'], s['refusals'], kinds, len(s['claims'])), '']
    L += ['**b762’s CLAIM items**, each printed in full in its bank’s words (relay data/b762_events.txt rows (24)-(29)): %s.' % '; '.join(
        '(%s) %s [CLAIM ; %s]' % (r[0], _c1_sq(_c1_q(r[4]).rstrip('.')), _c1_col(r[3])) for _k, r in s['claims']), '']
    L += ['**The findings after b762’s lock**, entered as events of b763 from the seat’s closing message (transcript line 191162, '
          '2026-11-19T18:22:32Z), which gave them there and not in a bank, the events bank being among the banks the root hashes and step [21] '
          'of the close order not taken; each time read from the message (relay data/b763_events.txt rows (14)-(30)), each on 2026-11-19: '
          'CLAIM %d, CLOSE %d, REPEAT %d of %d. %s.' % (
              ft['claim'], ft['close'], ft['repeat'], ft['total'],
              '; '.join('(%s) %s, %s [%s ; %s]' % (r[0], _c1_sq(_c1_q(_c1_head(r[4]))), _c1_time(r[4]), r[2], _c1_col(r[3])) for r in s['findings'])), '']
    L += ['**The navigator’s own**, each entered as the navigator’s, CLAIM, in the words of `(R373)`(1) (relay data/%s_ferry.txt :%d; relay '
          'data/b763_events.txt rows (31)-(35)), printed in full: %s.' % (
              ACT, s['l_nav'], '; '.join('(%s) %s [CLAIM ; %s]' % (m_, _c1_sq(_c1_q(w_)), _c1_col(r[3])) for (m_, w_), r in zip(s['nav'], s['nav_rows']))), '']
    L += ['*b762’s integration by [I1] of `(R373)`(1), entered from relay data/%s_ferry.txt :%d with its one field filled: SPIRAL_MAP’s cluster '
          'table (%d rows, :%d-:%d) %s, so “%s”; REGISTRY :%d is the row d1-8, naming the deposited page, whose next edition '
          'day1/ONE\\_PAGE\\_PROOF\\_v2\\_0.md is.*' % (
              ACT, s['l_i1'], len(s['cl_rows']), s['cl_rows'][0], s['cl_rows'][-1],
              'names neither d1-8 nor the page' if s['cluster'] == 'Day 1' else 'names the page in the row of that cluster', s['cluster'], s['l_reg']), '',
          s['i1'], '']
    L += ['**The repairs `(R373)`(11) carries**, each named, to one act of the record’s upkeep, which the root’s question offers: %s. No repair of '
          'these is made under tools/standing/ at this act.' % '; '.join('%s (%s)' % (_c1_sq(_c1_q(w_)), _c1_sq(_c1_q(c_))) for w_, c_ in C1_REPAIRS), '']
    L += ['*Filed at b763 on the author’s ruling `(R373)`(1): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the '
          'act’s override in relay tools/acts/b763.py) from b762’s events, defects and refusals banks read unedited and b763’s events rows (14)-(35); '
          'banked as relay `data/b763_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (%d). It answers b762’s record; no '
          'sealed tool, face, trail or root-named bank of b762 is edited. No weight line is written: `(R373)`(1) states b762’s weight from its closing’s '
          'head.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    t = s['tally']
    ft = _c1_tally(s['findings'])
    return (['b763 -- THE CORRIGENDUM FOR b762, SHORT, (R373)(1) (%s)' % utc(), '',
             '### the banks read unedited: data/b762_events.txt rows (1)-(%d), data/b762_defects.txt %d rows, data/b762_hook_refusals.txt %d lines; no '
             'post-seal events bank at b762; data/b762_closing.txt :1 (the head) and :%d (the counter); data/%s rows (14)-(30) (the findings after the '
             'lock) and (31)-(35) (the navigator`s own, read against data/%s_ferry.txt :%d); [I1] from data/%s_ferry.txt :%d, its field "%s" from '
             'SPIRAL_MAP`s cluster table (%d rows) and REGISTRY :%d; the corrigenda bank`s last row (%d).' % (
                 len(s['events']), len(s['defects']), s['refusals'], s['l_counter'], C1_FINDINGS_BANK, ACT, s['l_nav'], ACT, s['l_i1'], s['cluster'],
                 len(s['cl_rows']), s['l_reg'], C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS %d, DEFECTS %d ; CLAIM %d, CLOSE %d ; REPEAT %d ; THE CLAIM ITEMS OF b762`S BANKS %d, PRINTED IN FULL ; THE '
               'FINDINGS AFTER THE LOCK %d: CLAIM %d, CLOSE %d, REPEAT %d ; THE NAVIGATOR`S OWN %d, CLAIM %d ; [I1] CLUSTER %s ; THE REPAIRS OF (11) %d, '
               'CARRIED BY NAME ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :%s.**' % (
                   t['total'], len(s['events']), len(s['defects']), t['claim'], t['close'], t['repeat'], len(s['claims']), ft['total'], ft['claim'],
                   ft['close'], ft['repeat'], len(s['nav']), sum(1 for r in s['nav_rows'] if r[2] == 'CLAIM'), s['cluster'], len(C1_REPAIRS), ln)])


def c1(*a):
    """`c1 corrigendum [dry|write]`: the short corrigendum for b762, landed through b698's guarded landing (the title rule of v1.35.8 in front of
    it); dry prints and writes nothing. (R373)(1) orders no weight line and (9) carries OPEN_TRAILS' lines: `c1 weight` and `c1 next` refuse."""
    route = a[0] if a else ''
    dry = 'write' not in a
    if route == 'weight':
        sys.exit('### (R373)(1) ORDERS NO WEIGHT LINE FOR b762 -- NOTHING COMPOSED')
    if route == 'next':
        sys.exit('### (R373)(9) CARRIES OPEN_TRAILS` LINES UNDER ONE DATED HEAD -- NOTHING COMPOSED HERE')
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
                                                   claims=[dict(bank=k_, id=r[0], owner=r[1], column=r[3]) for k_, r in s['claims']], in_full=len(s['claims']),
                                                   findings=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_FINDINGS_IDS), claim=ft['claim'],
                                                                 close=ft['close'], repeat=ft['repeat'],
                                                                 times=dict((r[0], _c1_time(r[4])) for r in s['findings']),
                                                                 claims=[dict(id=r[0], owner=r[1], column=r[3]) for r in s['findings'] if r[2] == 'CLAIM']),
                                                   navigator=dict(bank='data/' + C1_FINDINGS_BANK, rows=list(C1_NAV_IDS), ferry_line=s['l_nav'],
                                                                  marks=list(C1_NAV_MARKS), claim=sum(1 for r in s['nav_rows'] if r[2] == 'CLAIM')),
                                                   i1=dict(ferry_line=s['l_i1'], text=s['i1'], cluster=s['cluster'], cluster_rows=s['cl_rows'], registry_line=s['l_reg']),
                                                   refusals=dict(lines=s['refusals'], kinds=s['kinds']),
                                                   repairs=dict(ordered=[w_ for w_, _c in C1_REPAIRS], where=[c_ for _w, c_ in C1_REPAIRS]),
                                                   weight_line=None, row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; THE CLAIM ITEMS OF b762`S BANKS %d, IN FULL ; THE FINDINGS %d, CLAIM %d ; THE NAVIGATOR`S OWN %d ; [I1] %s ; THE REPAIRS %d ; FINDINGS :%s' % (
            t['claim'], t['close'], t['total'], t['repeat'], len(s['claims']), ft['total'], ft['claim'], len(s['nav']), s['cluster'], len(C1_REPAIRS), ln))
        return
    sys.exit('usage: fold.py record c1 corrigendum  [dry | write]')
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
    """N1, b763 ((R373)(5), (6)-(8), N1; b759's form, the Edit tool at Component 3): every dispatch of the act a row of the dispatch bank,
    its kernel named, its free memory read before the send at or above the hold; the run ids the worklist's, EF_RUNS in
    SIDE-explicit-formula within MAX_DISPATCHES and none in SIDE-dirichlet-mod-24 (M24_RUNS empty, its cap 0: (5) writes no kernel beyond
    SIDE-explicit-formula), no dispatch row of another kernel; each read once after it by that id, the read's free memory at or above the
    hold; the plant a dispatch row with no kernel and no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    ef_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-explicit-formula']
    m4_ = [int(r.get('run')) for r in ds if r.get('kernel') == 'SIDE-dirichlet-mod-24']
    return bool(ds) and ef_ == list(K.EF_RUNS) and len(ef_) <= K.MAX_DISPATCHES and m4_ == list(K.M24_RUNS) and len(m4_) <= K.MAX_DISPATCHES_M24 \
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
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit (the act named here drifted one act at each carry, b753 at b754 to b758 at b762; the name dropped at b763), naming tools/standing/hook.py, unedited this act (v1.34.6`s commit eac02515 not among its writers; its blob at the act`s base the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool), carried: the step-zero bank writes each deleted ref's tip as "(was 28255aea, 19:01:51Z)"
# ### (data/b755_stepzero.txt :57-:59), b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b762-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b755: the step-zero bank rides in the step-zero banks' commit 77ae83fe (STEPZERO_BANKS = STEPZERO_BANK_COMMIT); five push-b754-* refs
# ### deleted at step zero (relay three, PLACE-papers two, data/b755_stepzero.txt :55-:60), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b763_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b754, Component 6 (the Edit tool), carried: the step-zero bank words the row "THE --MERGED LISTING, PRINTED BEFORE THE DELETES"
# ### (data/b755_stepzero.txt :55); b758: "THE --MERGED LISTING, before the deletes" (data/b758_stepzero.txt :54); b759, before the lock:
# ### b759's bank words it "THE --MERGED LISTING (18:41Z)" and its deletes "THE DELETES, AFTER THE CHECK" (data/b759_stepzero.txt :60, :62);
# ### b760, Component 6: "THE --MERGED LISTING (08:42:28Z)" and "THE DELETES, AFTER THE CHECK" (data/b760_stepzero.txt :59, :61)
# ### b761, Component 6: "THE --MERGED LISTING (21:59:32Z, scratch merged761.py)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b761_stepzero.txt :63, :65)
# ### b762, Component 6: "THE --MERGED LISTING (10:12:5xZ)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b762_stepzero.txt :64, :66)
# ### b763, Component 3 (the Edit tool): "THE --MERGED LISTING (19:08:17Z)" and "THE DELETES, AFTER THE CHECK, ONE PER MESSAGE" (data/b763_stepzero.txt :65, :67)
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING (19:08:17Z)' in z and 'THE DELETES, AFTER THE CHECK' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's overrides of checks 1516 and 1659 (hook.py edited by b753's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b754 as it stands
# ### b754, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b763_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b756, Component 6 (the Edit tool): the corrigendum's json (data/b756_corrigendum.json, written by the act's c1 route) carries the
# ### counts and no rows -- items 46, CLAIM 0, CLOSE 46, REPEAT 20, the CLAIM items 0, the corrigenda row (76); the rows stand in the bank by
# ### their banks (data/b756_corrigendum.txt); the template's row range read as the json's counts
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('items') == 70 == j.get('claim') + j.get('close') and evs == [] and dfs == [] \
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
        and '| ruling (4) | port-b707 kept on SIDE-lv-conservation | local |' in (S['citation'] or '') and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b759, before the lock (the Edit tool): G-DELETES-ONE-BRANCH over b759's deletes -- the five step-zero refs, each by the one-call tool's
# ### delete route, and (3)'s five kernel branches, each removed at its kernel's remote by (4)(i)'s route `<repo> rdelete <branch>`
# ### (data/b759_events.txt (24)), which the standing capture reader (tools/standing/delread.py v1.30.0, its TOOL_ARGS) does not read: the
# ### act's reader below reads them segment by segment as delread reads the delete route, wanted equal to the worklist's KERNEL_DELETES; every
# ### delete of either route read against the ruling's own delete clauses through the standing allowance reader; port-b707 undeleted at its tip
#⟪OVERRIDE checks MARK 61379f7e4609 2⟫
        and sorted(_rdeletes(S)) == sorted(b_ for b_, _t in K.KERNEL_DELETES) and not [b for b in got if b not in NAMED_PUSH] \
        and STW.deletes_read([('-', b) for b in got + _rdeletes(S)], S['ferry'], STW.words_of(ACTN))['ok'] \
        and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP \
#⟪END⟫
#⟪OVERRIDE checks MARK 23e17a97edcc 1⟫
    ('G-DELETES-ONE-BRANCH', '(⟪RUL⟫)(4): the command capture`s branch deletes, each one branch, no glob, no variable, nothing chained after; the five step-zero deletes of the push-b762-* branches by the tool`s delete route, each allowed by the ruling`s own delete clause read through tools/standing/allow.py; no kernel branch removed (the worklist`s KERNEL_DELETES empty, no rdelete route run); port-b707 undeleted at its tip; the command bank`s count',
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
                                                                          or (bool(S['report_tool']) and 'tools/acts/b762.py -> tools/acts/b763.py' in (rd('b763_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b763_report.py' not in (S['sealj'].get('tools') or {})   # ### b763, Component 3 (the Edit tool): the carried stub set for the act, b759's body with the act's name
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b763_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:   # ### b763, Component 3 (the Edit tool): the carried stub set for the act, b759's body with the act's name
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b763')
    return '### THE COUNTER ((R373) Component 5, the act`s events and defects together; relay data/b763_defects.txt, data/b763_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d; b755,
# ### Component 6 (the Edit tool, defect (n)): the plan's pass read where it stands, b752's [P1] (relay data/b752_attribution_plan.txt; data/
# ### b752_closing.txt :182), where the carries shifted its act name to b753 (b754's closing :2407) and here to b754, a bank absent from the tree
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE read RETIRED by [A11] and [A12], W-ORD-PREMISE-POSITIONS ENTERED by [B2], the other renderings carried with their triggers ((R373)(9));',
    '        W-ORD-LI-ARITH, W-ORD-SIGN-SECTORS and W-ORD-STATEMENT-FILE by the build lines of (6), (7) and the author`s word; none entered, retired or closed by the seat; the orders before this act as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)   # ### b763, Component 3 (the Edit tool): the carried stub set, b759's body (b763's listing at 19:08:17Z, data/b763_stepzero.txt :65)
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b763_author_answers.txt', 'b763_answer_check.txt', 'b763_events.txt'))   # noqa: E731,E702
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
REG = os.path.join(ROOT, 'data', 'b763_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b763_registration_%s.txt' % __import__('b763_worklist').DATE)   # ### the gate imports no worklist of its own
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
    ('commits on any kernel`s main', 'EFMAINCOMMITS', 'EFMAINCOMMITS', 'commits', '### (R373)(6), (8): SIDE-explicit-formula`s main moved from a3aad4cc to the tip of push-b763-form by the gated push`s default mode after run 44646848292`s success, build one`s three commits, and to an order`s tip where (8) landed one; SIDE-dirichlet-mod-24`s main unmoved; MEASURED off git rev-list --count a3aad4cc..main.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 18c1a19a6cb6 1⟫
    ('scratch branches cut on a kernel', 0, 0, 'branches', '### none: v1.37.2`s planted control read in the relay`s own tool (data/b763_standing_v1372.txt), no kernel branch for it.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK a2b9535083e6 1⟫
    ('push branches cut on a kernel for the push procedure', 2 + len(K.ORDER_BRANCHES), 2 + len(K.ORDER_BRANCHES), 'branches', '### (R373)(5)-(8): push-b763-form, push-b763-arith and the branch of each order of (8) sent (push-b763-squares, push-b763-keiper) in SIDE-explicit-formula, each made at main by the one-call tool and carried by the gated push`s branch mode, kept for the next act`s step zero ((R373)(4)).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 42ab3bdb112d 1⟫
    ('kernel merges made', 0, 0, 'merges', '### none: main moved to the tip of push-b763-form by the gated push, a fast-forward, and to an order`s tip the same way where (8) landed one.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 63e5424dd90e 1⟫
    ('tags made or moved', 'TAGSMADE', 'TAGSMADE', 'tags', '### N5, (R373)(6), (8): v0.42 at 4964e957 and the tag of each order of (8) built in full, each cut at main`s read-back and its peel read back at the remote equal to main; v0.38 at 14ca5725, v0.39 at d1afb4fc, v0.40 at 630cba16, v0.41 at a3aad4cc and v0.2.0 at e5ebdd15 unmoved; MEASURED off SIDE-explicit-formula`s tags past v0.41, SIDE-dirichlet-mod-24`s past v0.2.0, and the template`s other kernels as before.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 5381b10a2ae6 1⟫
    ef_tags_after = [t for t in _git(K.EF_DIR, 'tag', '--contains', K.EF_V037).split(chr(10)) if t.strip() and t.strip() not in ('v0.37', 'v0.38', 'v0.39', 'v0.40', 'v0.41')] + [t for t in _git(K.M24_DIR, 'tag', '--list').split(chr(10)) if t.strip() and t.strip() not in ('v0.1.0', 'v0.2.0')]   # ### b763: v0.38 b745`s, v0.39 and v0.40 b758`s, v0.41 b759`s, v0.2.0 b757`s; the tags past them, the act`s own
#⟪END⟫
#⟪OVERRIDE regspec MARK 100638d8d84e 1⟫
    ('kernel branches deleted', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### none ((R373)(4): no clause of this ruling removes a kernel branch); port-b707, the pin, challenge and rebuild branches and the held branches kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 51acd0ac8ef1 1⟫
    ('branches deleted beyond the step zero`s list', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### none: the five push-b762-* refs of (R373)(4) alone; port-b707 kept.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK b6204f4e0fa8 1⟫
    ('census editions written on main', 0, 0, 'editions', '### none: no census written this act ((R373)(12)).'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 0daf7a1cb287 1⟫
    ('papers moved, renamed or written beyond FINDINGS, OPEN_TRAILS and REGISTRY', 1, 1, 'papers', '### (R373)(9): phase1.5/method/THE_METHOD_CANON.md, its section XXV appended at its end by [C1], no byte above it changed; none moved or renamed.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 46160108b751 1⟫
    ('README edits', 0, 0, 'edits', '### none this act: no kernel`s README written.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 2d7a99569826 1⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 'OTBLOCK', 'OTBLOCK', 'lines', '### (R373)(9), (6)-(8): the block at the file`s end from :18955, no line moving -- under one dated head the line naming [W1]`s bank, [A1] to [A12], [B1], [B2] and the build lines of (6), (7) and (8) -- by one PLACE-papers commit; MEASURED off relay data/b763_ledgers.json`s OPEN_TRAILS row.'),
#⟪END⟫
#⟪OVERRIDE regspec MARK 44ff8bc9f5d4 1⟫
    ('faces ledger update blocks appended', 0, 0, 'blocks', '### none: FACES_LEDGER not written this act ((R373)(13)`s list).'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b763_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
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
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijkl'))   # ### b763: the seat's rows of data/b763_defects.txt as the template's reader takes them, (a) to (l), each THE SEAT'S ((a)-(d) at step zero, (e)-(g) in Component 1, (h)-(j) in Component 2, (k) and (l) at Component 6's preparation); set again at the seal where a row is added; no navigator's row
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b763_misses.txt', 'data/b763_price.txt', 'data/b763_price.json', 'data/b763_corrigendum.txt', 'data/b763_corrigendum.json',   # ### step zero and Component 1
                  'data/b763_standing_v1372.txt', 'data/b763_controls_control.txt',                                        # ### (5)
                  'data/b763_presend_s123.txt', 'data/b763_presend_s4.txt', 'data/b763_presend_s5.txt', 'data/b763_presend_sf.txt',   # ### Component 2, (6)
                  'data/b763_dispatch_rows.json', 'data/b763_outcomes.txt', 'data/b763_outcomes.json', 'data/b763_xlines.json',
                  'data/b763_author_words_preseal.txt',                                                                    # ### the author's word on the statement file
                  'data/b763_presend_s7.txt',                                                                              # ### Component 3, (7)
                  'data/b763_presend_s24.txt', 'data/b763_presend_skp.txt', 'data/b763_imp2tau.txt', 'data/b763_imp2tau.json',   # ### Component 4, (8)
                  'data/b763_author_rulings.txt', 'data/b763_ledgers.txt', 'data/b763_ledgers.json', 'data/b763_orders.txt',   # ### Component 5, (9)
                  'data/b763_reproduce.txt', 'data/b763_reproduce.json', 'data/b763_recut_inputs.txt',                     # ### (12) and (10)
                  'data/b763_ceiling.txt', 'data/b763_author_answers.txt', 'data/b763_address_scan.txt', 'data/b763_touch.txt',   # ### b763, Component 6: the act's banks by its components, in place of b762's carried names; no amendments bank and no rules bank this act (none written); the template's standing banks follow
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b763_address_scan.py'), 'scan'], capture_output=True, text=True,
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
    c = [('v9', K.STANDING_COMMIT)] + list(K.CHAIN)
    in_ = set(h_[:8] for _k, h_ in K.CHAIN)
    c += [(k_, h_) for k_, h_ in (('passed', K.PASSED_BANK), ('handoff', K.HANDOFF_COMMIT), ('lockgate', K.C1_LOCKGATE)) if h_ and h_[:8] not in in_]
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
        # ### b763, Component 6: the act's banks its arms read -- the author's words and the canon's section and trail lines of (9), the
        # ### roster, the outcomes of (6)-(8) with their build lines, the price, the IMP2-TAU reading, the answers, the ceiling at HEAD and at
        # ### the commit of its last reading; and the sha256 (16 hex) of each PLACE-papers file's blob at the commit that wrote it (the
        # ### worklist's PP_WRITES), against which the banks' digests are read; b762's registration, map and page have no counterpart here
        rulingst=rd('b763_author_rulings.txt'), ledgersj=jl('b763_ledgers.json'), ledgerst=rd('b763_ledgers.txt'), orderst=rd('b763_orders.txt'),
        outj=jl('b763_outcomes.json'), outt=rd('b763_outcomes.txt'), xlinesj=jl('b763_xlines.json'), pricej=jl('b763_price.json'),
        imp2j=jl('b763_imp2tau.json'), answerst=rd('b763_author_answers.txt'), wordst=rd('b763_author_words_preseal.txt'),
        gwb=dict((n_, (files_of(ROOT, c_), files_of(ROOT, k_), rd(b_.split('/', 1)[1]), _s(blob(ROOT, '%s:%s' % (k_, b_))))) for n_, _t, b_, c_, k_ in K.GENS_WITH_BANK),
        ceiling=(rd('b763_ceiling.txt'), _s(blob(ROOT, '%s:data/b763_ceiling.txt' % K.C1_CEILING))),
        pp_shas=dict(('%s:%s' % (c_[:8], f_), hashlib.sha256(blob(PP, '%s:%s' % (c_, f_)) or b'').hexdigest()[:16]) for _k, f_, c_ in K.PP_WRITES),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        pp_files=dict((k_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        numstat=dict((k_, gs(PP, 'show', '--numstat', '--format=', h_).split()) for k_, h_ in K.PP_CHAIN),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        kst=_kernel_state(),   # ### b757: the two kernels' refs, tags and the kernel commits' containing refs (G-OFFSET-POST-HOC)
        drows=json.loads(rd('b763_dispatch_rows.json') or '[]'),
        reproduce=rd('b763_reproduce.txt'), reproducej=jl('b763_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b763_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (b759's form); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b763_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [(k_, _ct(PP, h_)) for k_, h_ in K.PP_CHAIN]
               + [('c1', _ct(ROOT, K.C1_RELAY)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)), ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING) if K.C1_STANDING else [], lockgate=files_of(ROOT, K.C1_LOCKGATE) if K.C1_LOCKGATE else [], c2=[],   # ### b757: the lock gate set when made; no Component 2 relay bank of b756's kind
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
READFIRST_NEEDLES = (
    'relay data/b762_closing.txt |',
    'relay data/b762_defects.txt |',
    'relay data/b762_events.txt |',
    'relay data/b762_misses.txt |',
    'relay data/b762_author_answers.txt |',
    'relay data/b757_ferry.txt (2), (3), (5) and (7) |',
    'relay data/b757_price.txt |',
    'relay data/b759_ferry.txt, its clause on the build |',
    'relay data/b759_presend.txt |',
    'relay data/b752_attribution_plan.txt |',
    'relay data/b725_interference.txt, its head |',
    'PLACE-papers FINDINGS.md :10198, the entry of b709 |',
    'relay tools/standing/orders.py |',
    'relay tools/standing/cadence.py |',
    'relay data/b754_close_yield.txt (A) |',
    'PLACE-papers OPEN_TRAILS.md :17714 and :18783 |',
    'PLACE-papers phase1.5/method/THE_METHOD_CANON.md XXIV to its end |',
    'PLACE-papers OPEN_TRAILS.md, the entries of the orders (8) and [A1] to [A12] name |',
    'SIDE-explicit-formula at v0.41, the files SCOPE READ names, with print_targets.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R373)(1)-(2))',   # ### the template's heading (closing.tpl :389), not the ferry's numbering
 'PRICE AND THE CEILING ((R373)(3))', 'ROUTE FOR KERNEL WRITES ((R373)(5))', 'BUILD ONE AND THE STATEMENT FILE ((R373)(6), the author`s word of 2026-11-19)',
 'CENTRE ((R373)(7))', 'ORDERS PRICED BESIDE IT ((R373)(8))', 'AUTHOR`S WORDS ((R373)(9))',
 'RESEARCH INSTRUMENTS REPRODUCED ((R373)(12), the standing arm G-RESEARCH-REPRODUCES)',
 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')   # ### b763, Component 6: closing 7's headings as written over b763's banks, in its order
#⟪END⟫
#⟪SECTION checks 12⟫
    """b763: the citation check's bank: every cite checked, OK and misses summing (83 = 83 + 0, data/b763_citation_check.txt :138), no miss;
    the ferry's paths 38, OK 33, NONE 0 (:139); the check HALTED on one Lean-path row (:140, halts 1: Lean paths and nouns 1, comparatives
    0), SCOPE READ's "Schema/Wide/HalfScale.lean at wide_detector" read against the next clause's paths, the cite true and the halt read in
    the step-zero bank before the deletes (defect (c)), as the step-zero bank enters it (data/b763_stepzero.txt :54-:57, after the read-first
    bank, before the subject read and the deletes); the bank written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 83 \
        and '### ### **THE FERRY`S PATHS 38 ; OK 33 ; NONE 0.**' in c \
        and '### ### **THE CHECK HALTED** (halts 1: Lean paths and nouns 1, comparatives 0)' in c \
        and 'BANKED (19:05:59Z, data/b763_citation_check.txt, .json): CITES CHECKED 83 ;' in (S['stepz'] or '') \
        and 'THE FERRY\'S PATHS 38 ; OK 33 ; NONE 0 ; THE CHECK HALTED, halts 1' in (S['stepz'] or '') and 'the halt read here before the deletes' in (S['stepz'] or '') \
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
                    MISSES=tfirst('b763_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b763, (R373)(1): no weight line ordered (the c1 route refuses one; data/b763_corrigendum.txt's foot NO WEIGHT LINE), so the
    # ### record-lines bank holds none; b762 at its weight stands in the corrigendum's line, FINDINGS :15797 (PLACE-papers 6034501c, step 9),
    # ### read through the corrigendum's landing bank, its head through conv; a planted record-lines line is read in its place
    return landed(S if S['rl'] else dict(S, rl=jl('b763_corrigendum_landing.json')), 0,
                  ['b762 closed at relay efb9acb6 and PLACE-papers 87cab4f', 'carries 59 rows, (1)-(59)', '11 lettered rows, (a)-(k)', 'Its 6 CLAIM items are printed in full below'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b763's title by its objects, the ferry's ACT line (data/b763_ferry.txt :131) adjusted to what the act did (record 31's _title over the
# ### banks: b762 at its weight; the outcomes of (6), (7) and (8) (data/b763_outcomes.json); the price and the ceiling; the author's words
# ### and the roster (data/b763_ledgers.txt, data/b763_orders.txt); the dispatches); each needle a fixed part of the composed title, with the
# ### typographic apostrophe, no backtick, conv(title) == title; read against the composed title at the dry
TITLE_NEEDLES = ('## The control’s failure from its coefficients under (R373): b762’s close ',
                 ' (b763_corrigendum); the finite and signed parts of the form compiled at v0.42, 5 statements of 5, and One Page’s 19 rows of this kernel stated and built in one file (b763_outcomes)',
                 'the statement of the control’s failure committed and compiled before its proof, no proof sent (b763_outcomes, b763_ceiling)',
                 'the orders priced beside it, ', ' (b763_price, b763_outcomes)',
                 'the author’s words on the waiting orders and canon XXV entered, 84 open to 83 (b763_author_rulings, b763_ledgers, b763_orders)',
                 ' dispatches')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R373)(1): the generated corrigendum for b762's record landed, short (its line in the json, FINDINGS :15797, the title at that line
    through conv): b762's 59 events and 11 defects by count from their banks, 70 items, CLAIM 6 and CLOSE 64, REPEAT 50, the six CLAIM
    items printed in full; the seventeen findings after b762's lock entered as b763's events (14)-(30) (CLAIM 0, CLOSE 17, REPEAT 14), each
    with its time; the navigator's own five entered as b763's events (31)-(35), CLAIM 5; [I1] with its cluster Day 1; the six repairs of (11)
    carried by name; no weight line; the corrigenda bank appended at row (83) and nothing before it changed; in Component 1's commits (the
    figures read from data/b763_corrigendum.json and the bank's foot, :21)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and j.get('row') == 83 and j.get('claim') == 6 == len(j.get('claims') or []) and j.get('close') == 64 and j.get('repeat') == 50 \
        and '### ### **ITEMS 70: EVENTS 59, DEFECTS 11 ; CLAIM 6, CLOSE 64 ; REPEAT 50 ; THE CLAIM ITEMS OF b762`S BANKS 6, PRINTED IN FULL ; THE FINDINGS AFTER THE LOCK 17: CLAIM 0, CLOSE 17, REPEAT 14 ; ' in (S['corrt'] or '') \
        and 'THE NAVIGATOR`S OWN 5, CLAIM 5 ; [I1] CLUSTER Day 1 ; THE REPAIRS OF (11) 6, CARRIED BY NAME ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :15797.**' in (S['corrt'] or '') \
#⟪END⟫
#⟪SECTION checks 19⟫
        and [(c_.get('bank'), c_.get('id')) for c_ in (j.get('claims') or [])] == [('events', str(n_)) for n_ in range(24, 30)] and j.get('in_full') == 6 \
        and (j.get('findings') or {}).get('rows') == [str(n_) for n_ in range(14, 31)] \
        and [(j.get('findings') or {}).get(k_) for k_ in ('claim', 'close', 'repeat')] == [0, 17, 14] \
        and (j.get('navigator') or {}).get('rows') == [str(n_) for n_ in range(31, 36)] and (j.get('navigator') or {}).get('claim') == 5 \
        and j.get('weight_line') is None and len((j.get('repairs') or {}).get('ordered') or []) == 6 \
        and '  (83) ' in S['corrigenda'] and '  (84) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R373) orders no rules bank for this act; the rule it works by is b756's, data/b756_rules.txt,
    its rows (a) to (c) in force from b757 by (R366)(2), with b760's row (a) (data/b760_rules.txt); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here b756's rows (a) to (c), lettered as (R366)(2) letters them, in b756's Component 1 commit (relay 0a151012) and no other, the working
    tree its blob at HEAD; no data/b763_rules.txt written (the worklist's C1_RULES None); data/b760_rules.txt and data/b754_rules.txt not
    rewritten by this act."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and re.findall(r'(?m)^  \(([a-z])\) ', rd('b756_rules.txt') or '') == ['a', 'b', 'c'] \
        and not r1 and K.C1_RULES is None and not os.path.exists(os.path.join(D, 'b763_rules.txt')) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', 'data/b754_rules.txt').split()][:1] == [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', K.PRE_RELAY, '--', 'data/b754_rules.txt').split()][:1] \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', 'data/b760_rules.txt').split()][:1] == [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', K.PRE_RELAY, '--', 'data/b760_rules.txt').split()][:1] \
        and _txt(rd('b756_rules.txt')) == _txt(blob(ROOT, 'HEAD:' + K.B756_RULES[0])) \
        and [h_[:8] for h_ in gs(ROOT, 'log', '--format=%H', '--', K.B756_RULES[0]).split()] == [K.B756_RULES[1][:8]] \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b763's report lines (report sections 2-5): each key a phrase its line carries, the outcomes as banked (data/b763_outcomes.json:
# ### (6) LANDED, COMPILED, the statement file BUILT, (7) STATEMENT COMPILED, NO PROOF SENT), each tier read by the report's footing
REPORT_KEYS = ('KERNEL -- THE FINITE AND SIGNED PARTS OF THE FORM LANDED', 'KERNEL -- THE STATEMENT FILE BUILT, BY THE AUTHOR`S WORD',
               'KERNEL -- THE STATEMENT OF THE CONTROL`S FAILURE COMPILED BEFORE ITS PROOF',
               'CERTIFIED -- tools/standing/ v1.37.2, THE ONE CHANGE (5) REQUIRED', 'CERTIFIED -- tools/b763_controls.py BY ITS OWN CONTROLS',
               'CERTIFIED -- THE PRE-SEND READS AND THE SALT CHECK BEFORE EACH SEND', 'CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED',
               'REGISTERED -- THE CORRIGENDUM FOR b762, SHORT', 'REGISTERED -- THE PRICE AND THE CEILING OF (3)', 'REGISTERED -- THE AUTHOR`S WORDS ENTERED',
               'HELD -- (7)`s PROOF, NOT SENT', 'HELD -- THE ORDERS OF (8) NOT BUILT IN FULL',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b763 ((R373)(5)-(8), N1; b759's form): every runner dispatch of the act sent by tools/b763_controls.py's dispatch route, one
    command in the capture for each dispatch row (one to MAX_DISPATCHES, each in SIDE-explicit-formula, none in SIDE-dirichlet-mod-24), each
    read once after it by its run id, every dispatch and read row's free memory at or above the hold; no earlier act's rebuild, axiom or lv
    route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### b763: the act's own rows, each dispatch and its read; the order read by the loop above, by run id
    order = order and len(seq_) == 2 * len([r for r in rows if r.get('kind') == 'dispatch'])
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b763_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) + len(K.M24_RUNS) == len(cmds) \
        and 1 <= len(K.EF_RUNS) <= K.MAX_DISPATCHES == 18 and len(K.M24_RUNS) == K.MAX_DISPATCHES_M24 == 0 \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]   # ### b763, N1: the runs within the price table's upper figures ((6) 17, (7)'s statement 1), none in SIDE-dirichlet-mod-24 ((5))
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N3, N5, (R373)(1), (9), (13): PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the corrigendum and the entry;
    OPEN_TRAILS: the lines of (9) and the build lines under the dated head, and the trail; phase1.5/method/THE_METHOD_CANON.md: section
    XXV of [C1] at its end), the ledgers changed; REGISTRY not written; no rename; no other paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b763's headings and banks, as its _finding_text (record 34) writes them; the last the INTEGRATION line by (R373)(10)'s rule, bare,
# ### its cluster the one SPIRAL_MAP's table gives THE_EPSTEIN_CONTROL_OBJECT (:276, "The Epstein instance"), stage CLUSTERED where a
# ### declaration of (6) or (7) compiled (_integ_line, written by the rule and by no reader of the act's banks)
ENTRY_NEEDLES = ('**b762 at its weight and the corrigendum**', '**The route for kernel writes**', '**Build one**', '**The statement file**', '**The centre**',
                 '**The orders priced beside it**', '**The author’s words**', '**The research instruments reproduced**', '**The price and the ceiling**',
                 '**The order of the act**', '**What this act is not**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**The report of (10)**', '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b763_misses.txt', 'data/b763_corrigendum.txt', 'data/b763_price.txt', 'data/b763_ceiling.txt', 'data/b763_standing_v1372.txt',
                 'data/b763_controls_control.txt', 'data/b763_presend_s123.txt', 'data/b763_presend_s4.txt', 'data/b763_presend_s5.txt', 'data/b763_presend_sf.txt',
                 'data/b763_presend_s7.txt', 'data/b763_presend_s24.txt', 'data/b763_presend_skp.txt', 'data/b763_imp2tau.txt',
                 'data/b763_dispatch_rows.json', 'data/b763_outcomes.txt', 'data/b763_xlines.json',
                 'data/b763_author_words_preseal.txt', 'data/b763_author_rulings.txt', 'data/b763_ledgers.txt', 'data/b763_orders.txt',
                 'data/b763_reproduce.txt', 'data/b763_recut_inputs.txt', 'data/b763_events.txt', 'data/b763_address_scan.txt', 'data/b763_touch.txt',
                 'The act’s counter CLAIM ',
                 'INTEGRATION: cluster The Epstein instance ; keystone phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md ; stage CLUSTERED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()   # ### b755: no navigator's row in the defects bank; the navigator's figure of (R365)(3) stands as events (12)
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R373)(1), (9), N3, N4, N5 (the name the frozen run list carries): PLACE-papers written by the worklist's PP_CHAIN in its order and
    by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone, the act's first on its base (no weight line,
    (1) ordering none), removing no line; (9)'s ledgers in one commit touching OPEN_TRAILS and the canon alone, removing no line, each
    file's bytes at HEAD before a prefix of its new bytes and its blob there the sha256 the ledgers json wrote; REGISTRY in no commit (N3);
    the changed files since the base within PP_WRITTEN; by ancestry the base, each commit of the chain and HEAD; the earlier acts'
    registrations at HEAD their blobs."""
    pf_, ns_, sh_ = S['pp_files'] or {}, S['numstat'] or {}, S['pp_shas'] or {}
    pc_ = dict(K.PP_CHAIN)
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    la_ = dict((f_.get('path'), f_) for f_ in (lj_.get('files') or []) if isinstance(f_, dict))
    def sha_(c_, f_, w_):
        return bool(w_) and sh_.get('%s:%s' % (c_[:8], f_)) == w_
    lf_ = ['OPEN_TRAILS.md', 'phase1.5/method/THE_METHOD_CANON.md']
    want_ = [('c1pp', ['FINDINGS.md'], True),
             ('ledgerspp', lf_, sorted(la_) == sorted(lf_) and all((la_.get(p_) or {}).get('prefix') is True
                                                                  and sha_(pc_.get('ledgerspp') or '-', p_, (la_.get(p_) or {}).get('sha_after')) for p_ in lf_))]
    rows_ = [(k_, sorted(pf_.get(k_) or []) == sorted(fs_) and bool(ns_.get(k_))
              and all(x_ == '0' for x_ in (ns_.get(k_) or [])[1::3]) and ok_) for k_, fs_, ok_ in want_]
    order_ = [h_[:8] for h_ in (S['pp_log'] or [])[:len(K.PP_CHAIN)]] == [h_[:8] for _k, h_ in K.PP_CHAIN]
    return len(rows_) == len(K.PP_CHAIN) == 2 and set(k_ for k_, _o in rows_) == set(pc_) and all(o_ for _k, o_ in rows_) and order_ \
        and 'REGISTRY.md' not in S['pp_head_files'] and not any('REGISTRY.md' in (fs_ or []) for fs_ in pf_.values()) \
        and set(S['pp_head_files']) <= set(K.PP_WRITTEN) \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b763_address_scan.py run live over every commit of the act (relay,
    PLACE-papers and SIDE-explicit-formula's commits from its base, the kernel's commits and tag messages among them; fields, messages and
    added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the
    address 0, the author's name 0, the previous name 0, the ORCID 0; no byline excepted, (R373)'s N5 writing none (defect (k)), the bank's
    exception line NONE TAKEN; its eight controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 8 OF 8 AS WANTED' in out \
        and '## THE EXCEPTION, THE BYLINE UNDER I-23: NONE TAKEN: R373`S N5' in out and '## THE EXCEPTION, THE BYLINE UNDER I-23: NONE TAKEN: R373`S N5' in (S['address'] or '') \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R373)(1)-(13), N2, N4 (the name the frozen run list carries): the act's order by time -- the worklist's TIME_ORDER, relay and
    PLACE-papers together (the act_current commit, step zero's banks, the ceiling's tool and its repair, the c1 route, PLACE-papers'
    corrigendum and the corrigendum banks, the standing change of (5), the dispatch tool and the pre-send tool before any kernel write, each
    act tool before its bank, the outcomes and the ceiling's readings, the rulings tool and its banks, PLACE-papers' ledgers and the roster,
    the reproduction run, the carried close tools), then the handoff page and the lock gate where made; by ancestry within the relay from
    v9 through each commit of _chain; the one standing version's bank (v1.37.2) at HEAD its blob at its commit d34f7323, its foot ALL AS
    WANTED at the worklist's 10 cases, VERSION and the bank's tool in that commit's files; the act's commits under tools/standing/ that one
    and no other ((R373)(11): (5) alone moves tools/standing/)."""
    t_ = S['t']
    ks_ = list(K.TIME_ORDER) + [k_ for k_, _h in S['r366_chain'] if k_ in ('passed', 'handoff', 'lockgate') and k_ not in K.TIME_ORDER]
    sb_ = []
    for v_, c_, b_, n_ in K.STANDING_BANKS:
        bk_ = (S['stbanks'] or {}).get(v_, (None, None))[0]
        bl_ = _s(blob(ROOT, '%s:%s' % (dict(K.CHAIN).get('standing_bank') or '-', b_)))   # ### b763: the controls run after the standing commit (N2), banked at step 12 (ace66e00)
        m_ = re.match(r'^%s: CONTROLS .* ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.$' % re.escape(v_), _vlast(_txt(bk_)))
        ck_ = [k_ for k_, h_ in K.CHAIN if h_ == c_]
        sb_.append(bool(bk_) and _txt(bk_) == _txt(bl_) and bool(m_) and int(m_.group(1)) == int(m_.group(2)) == n_ and len(ck_) == 1
                   and 'tools/standing/VERSION' in S['files'].get('rc_' + ck_[0], []) and b_ in S['files'].get('rc_standing_bank', []))
    st_ = [h_[:8] for h_ in S['st_commits'] or []] == [c_[:8] for _v, c_, _b, _n in K.STANDING_BANKS]
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) \
        and bool(S['anc']) and len(S['anc']) == len(S['r366_chain']) - 1 and all(v is True for v in S['anc'].values()) \
        and len(sb_) == len(K.STANDING_BANKS) == 1 and all(sb_) and st_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R373)(3), (5)-(9), (12), N2, N3 (the name the frozen run list carries): each tool of K.GENS first added by a commit of its own,
    every one of its commits carrying it and not its bank, the bank's commit carrying the bank and not the tool and after every tool commit,
    the bank at HEAD its blob there (the ceiling, the dispatch tool's controls, the pre-send reads with each send's salt check, the
    outcomes of (6)-(8), the IMP2-TAU reading, the author's rulings, the ledgers of (9) and the recut inputs of (10)); K.GENS_WITH_BANK empty, no bank of this act
    riding with its tool; the ceiling at HEAD its blob at the commit of its last reading, two readings, (8)'s two carried by name and three
    built where they fit, dispatches 5 of 18 at that reading; the outcomes' foot the outcomes json's words for (6), the statement file and
    (7); the controls', each pre-send bank's (its salt check PASSED, the no-zero control over (7)'s file), the IMP2-TAU reading's, the
    author's rulings', the ledgers', the roster's, the corrigendum's and the reproduction run's feet as the entry reads them."""
    gk_ = _gens_ok(S)
    ce_ = S['ceiling'] or (None, None)
    ceil_ = bool(ce_[0]) and _txt(ce_[0]) == _txt(ce_[1]) and _vlast(_txt(ce_[0])) == (
        'THE CEILING: READINGS 2 ; THE LAST AFTER COMPONENT 3 AT 2026-11-20T03:46:09Z, 30.27 h AT THE LOWER FIGURES AGAINST 24 h, CARRIED (8) BESSEL-BOUND-TIGHTEN, '
        '(8) EXPLICIT-FORMULA-C1 ; BUILT WHERE IT FITS: SQUARES-AT-24, IMP2-TAU, KEIPER-FACE ; DISPATCHES 5 OF 18.')
    oj_ = S['outj'] if isinstance(S['outj'], dict) else {}
    of_ = re.match(r'^THE OUTCOMES: \(6\) (.+?), STATEMENTS COMPILED (\d) OF 5 ; THE STATEMENT FILE (.+?) ; \(7\) (.+?) ; (.+) ; BUILD LINES (\d+) ; CONTROLS (\d+) OF (\d+)\.$',
                   _vlast(_txt(S['outt'])))
    out_ = bool(of_) and of_.group(1) == (oj_.get('form') or {}).get('outcome') == 'LANDED, COMPILED' and of_.group(2) == '5' \
        and of_.group(3) == (oj_.get('statement_file') or {}).get('outcome') == 'BUILT' \
        and of_.group(4) == (oj_.get('arith') or {}).get('outcome') == 'STATEMENT COMPILED, NO PROOF SENT' and of_.group(7) == of_.group(8) \
        and int(of_.group(6)) == len((S['xlinesj'] or {}).get('lines') or [])
    pf_ = []
    for s_ in K.PRESEND_SENDS:
        v_ = _vlast(_txt(rd('b763_presend_%s.txt' % s_)))
        pf_.append(v_.startswith('THE PRE-SEND READS AT ') and ': DUPLICATES 0 (OVER THE TARGETS 0) ; ' in v_
                   and ' ; REFUSED BY THE FILTER 2 (:358, :359), THE TWO KNOWN YES ; ' in v_ and ' ; THE SALT CHECK OF SEND %s PASSED (' % s_ in v_
                   and (s_ != 's7' or ' ; THE NO-ZERO CONTROL PASSED ; ' in v_) and v_.endswith(' ; CONTROLS 30 OF 30.'))
    feet_ = [('b763_controls_control.txt', 'THE TOOL`S CONTROLS: 20 OF 20 AS WANTED ; ALL AS WANTED.'),
             ('b763_imp2tau.txt', 'THE IMP2-TAU READING: THE TRANSCRIBED PRINCIPAL VALUE DIVERGES AT f(1) NOT 0, ITS STEP A DECADE -f(1) ln 10 (TRI -1.151292479) ; '
                                  'THE COMPARISON WITH -A NOT MADE ; CONTROLS 6 OF 6 ; 2 s.'),
             ('b763_author_rulings.txt', 'THE AUTHOR`S RULINGS: WORDS 1, VERBATIM FROM THE FERRY ; RENDERINGS 12, THE NAVIGATOR`S, EACH VERBATIM ; NOTHING CHANGED.'),
             ('b763_corrigendum.txt', 'ITEMS 70: EVENTS 59, DEFECTS 11 ; CLAIM 6, CLOSE 64 ; REPEAT 50 ; THE CLAIM ITEMS OF b762`S BANKS 6, PRINTED IN FULL ; THE FINDINGS AFTER THE LOCK 17: '
                                      'CLAIM 0, CLOSE 17, REPEAT 14 ; THE NAVIGATOR`S OWN 5, CLAIM 5 ; [I1] CLUSTER Day 1 ; THE REPAIRS OF (11) 6, CARRIED BY NAME ; NO WEIGHT LINE ; THE ENTRY AT FINDINGS :15797.'),
             ('b763_reproduce.txt', 'ROWS 68 ; REPRODUCES 64 ; DIFFERS 0 ; NOT RUN 4 ; PLANTED CONTROLS AS WANTED 64 OF 64 ; 330 s.'),
             ('b763_recut_inputs.txt', 'THE RECUT INPUTS: (6) 42 DECLARATIONS OF 5 STATEMENTS FOR 7 PAPERS ; THE STATEMENT FILE 19 FOR 1 PAPER ; (7) 10 FOR 1 PAPER ; CONTROLS 7 OF 7.')]
    ft_ = [_vlast(_txt(rd(n_))) == w_ for n_, w_ in feet_]
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    lr_ = lj_.get('roster') or {}
    lv_ = re.match(r'^THE LEDGERS: FILES 2 OF 2 APPENDED, NO LINE MOVING ; \[C1\] AS SECTION XXV ; \[A1\] TO \[A12\], \[B1\], \[B2\] AND (\d+) BUILD LINES ; '
                   r'THE ROSTER 83 OPEN WITH THE LINES UP TO \[B2\], WANTED 83, (\d+) OF (\d+) AS WANTED ; CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.$', _vlast(_txt(S['ledgerst'])))
    led_ = bool(lv_) and lv_.group(2) == lv_.group(3) and lv_.group(4) == lv_.group(5) and int(lv_.group(1)) == len(lj_.get('build_lines') or []) \
        and lr_.get('before_open') == 84 and lr_.get('mid_open') == 83 == lr_.get('want')
    om_ = re.match(r'^ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', _vlast(_txt(S['orderst'])))
    ro_ = bool(om_) and int(om_.group(2)) == lr_.get('after_open') and int(om_.group(1)) == int(om_.group(2)) + int(om_.group(3))
    return len(gk_) == len(K.GENS) == 9 and all(o_ for _n, o_ in gk_) and K.GENS_WITH_BANK == () \
        and ceil_ and out_ and len(pf_) == len(K.PRESEND_SENDS) == 7 and all(pf_) and all(ft_) and led_ and ro_


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


#⟪END⟫
#⟪SECTION checks 35⟫
    """N1, N5, (R373)(4)-(8), (12) (the name the frozen run list carries): the two kernels as the act left them, read locally with no
    remote read -- SIDE-explicit-formula's main locally and at its tracking ref at the worklist's EF_MAIN, the peel of the last tag the act
    cut (v0.42 = 4964e957 after (6), and each tag of an order of (8) built in full after it, K.ORDER_TAGS), each tag's object and peel the
    worklist's; v0.39 to d1afb4fc, v0.40 to 630cba16 and v0.41's object 390506fc to a3aad4cc, the act's entering main, unmoved; no other
    tag past v0.38, v0.38's object 21c6edaf and peel 14ca5725; its four held branches at their entering tips locally and at origin, zq-b730
    at 1e658870; push-b763-form, push-b763-arith and each order's push-b763-* branch at its tip locally and at origin, kept for the next
    act's step zero; no kernel branch removed by this act (KERNEL_DELETES empty), push-b759-weil absent from its tracking refs as b760 left
    it, its local branch kept at a3aad4cc; each kernel commit of the worklist on the remote ref it names, the commits on their own branches
    not on the remote main; SIDE-dirichlet-mod-24's main at e5ebdd15 at its tracking ref and locally, v0.2.0's object e5c84316 peeling to
    e5ebdd15, v0.1.0 at 597b0869 and no other tag, push-b757-mod24 absent from its tracking refs; no sitting kernel."""
    ks_ = S['kst'] or {}
    ef_, m4_, ct_ = ks_.get('ef') or {}, ks_.get('m24') or {}, ks_.get('contains') or {}
    def h_(d_, r_):
        return (d_.get(r_) or ('', ''))[0]
    def p_(d_, r_):
        return (d_.get(r_) or ('', ''))[1]
    mn_ = h_(ef_, 'refs/heads/main')
    tags_ = [K.WEIL_TAG] + list(K.ORDER_TAGS)
    tg_ = sorted(r for r in ef_ if re.match(r'^refs/tags/v0\.(39|[4-9]\d)', r))
    ef_ok = mn_ == h_(ef_, 'refs/remotes/origin/main') == K.EF_MAIN == tags_[-1][2] \
        and all(h_(ef_, 'refs/heads/' + b) == t == h_(ef_, 'refs/remotes/origin/' + b) for b, t in K.EF_BRANCHES) and K.ZQ_TIP == K.ZQ_ENTERING \
        and h_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[1] and p_(ef_, 'refs/tags/' + K.ZQ_TAG[0]) == K.ZQ_TAG[2] \
        and tg_ == sorted(['refs/tags/v0.39', 'refs/tags/v0.40', 'refs/tags/v0.41'] + ['refs/tags/' + t_[0] for t_ in tags_]) \
        and p_(ef_, 'refs/tags/v0.39') == K.LAND_BRANCH[1] and p_(ef_, 'refs/tags/v0.40') == K.COEFF_LAND_BRANCH[1] \
        and h_(ef_, 'refs/tags/v0.41') == K.WEIL_TAG_B759[1] and p_(ef_, 'refs/tags/v0.41') == K.WEIL_TAG_B759[2] == K.EF_BASE \
        and all(h_(ef_, 'refs/tags/' + n_) == o_ and p_(ef_, 'refs/tags/' + n_) == pl_ for n_, o_, pl_ in tags_) \
        and all(h_(ef_, 'refs/heads/' + b_) == t_ == h_(ef_, 'refs/remotes/origin/' + b_) for b_, t_ in (K.WEIL_BRANCH, K.ARITH_BRANCH) + tuple(K.ORDER_BRANCHES)) \
        and not K.KERNEL_DELETES and 'refs/remotes/origin/' + K.WEIL_BRANCH_B759[0] not in ef_ \
        and h_(ef_, 'refs/heads/' + K.WEIL_BRANCH_B759[0]) == K.WEIL_BRANCH_B759[1]
    kc_ = len(K.KERNEL_COMMITS) == 6 \
        and all(('refs/remotes/origin/' + b) in ct_.get(k, []) for k, _kn, _c, b in K.KERNEL_COMMITS) \
        and all('refs/remotes/origin/main' not in ct_.get(k, []) for k, _kn, _c, b in K.KERNEL_COMMITS if b != 'main')
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
    arm list since b762's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R373)(6)-(9), (12), N1, N3 (the name the frozen run list carries): the counts the entry and the root prompt carry, each read from
    its bank -- (9)'s ledgers: OPEN_TRAILS and the canon each appended with its bytes before a prefix, the identifiers' counts equal and 0
    added, [C1], [A1] to [A12], [B1] and [B2] entered, the build lines of data/b763_xlines.json after them; the roster 84 open before,
    W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE CLOSED and W-ORD-PREMISE-POSITIONS entering OPEN with the lines up to [B2], no other moving, 83
    open, wanted 83, 4 of 4 as wanted; after the build lines, each status that moves an order of (8) built in full; the orders bank's foot
    at that figure; the outcomes' runs each a run of the worklist's EF_RUNS, the dispatch rows' runs EF_RUNS in order within MAX_DISPATCHES;
    b746's draft unchanged; no Zenodo tool."""
    lj_ = S['ledgersj'] if isinstance(S['ledgersj'], dict) else {}
    ro_ = lj_.get('roster') or {}
    oj_ = S['outj'] if isinstance(S['outj'], dict) else {}
    want_ = sorted(['C1'] + ['A%d' % i_ for i_ in range(1, 13)] + ['B1', 'B2'])
    xl_ = (S['xlinesj'] or {}).get('lines') or []
    full8_ = set(o_.get('order') for o_ in oj_.get('orders') or [] if o_.get('outcome') == 'BUILT IN FULL')
    mv_ = list(ro_.get('moved_after_b2') or [])
    led_ = sorted(f_.get('path') for f_ in lj_.get('files') or [] if isinstance(f_, dict)) == ['OPEN_TRAILS.md', 'phase1.5/method/THE_METHOD_CANON.md'] \
        and all(f_.get('prefix') is True and f_.get('ids_equal') is True and not f_.get('ids_added') for f_ in lj_.get('files') or []) \
        and sorted(lj_.get('entered') or {}) == want_ and len(lj_.get('build_lines') or []) == len(xl_) >= 2 \
        and ro_.get('before_open') == 84 and ro_.get('mid_open') == ro_.get('want') == 83 \
        and len(ro_.get('rows') or []) == 4 and all(r_[2] is True for r_ in ro_.get('rows') or []) \
        and set(mv_) <= full8_ and ro_.get('after_open') == 83 - len(mv_)
    om_ = re.match(r'^ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', _vlast(_txt(S['orderst'])))
    ord_ = bool(om_) and int(om_.group(2)) == ro_.get('after_open')
    def runs_(x_):
        return [int(r_.get('run') if isinstance(r_, dict) else r_) for r_ in (x_ or {}).get('runs') or []]
    orun_ = runs_(oj_.get('form')) + runs_(oj_.get('statement_file')) + runs_(oj_.get('arith')) + [r_ for o_ in oj_.get('orders') or [] for r_ in runs_(o_)]
    disp_ = bool(orun_) and set(orun_) <= set(K.EF_RUNS) \
        and [int(r_.get('run')) for r_ in S['drows'] or [] if r_.get('kind') == 'dispatch'] == list(K.EF_RUNS) and len(K.EF_RUNS) <= K.MAX_DISPATCHES
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b763_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return led_ and ord_ and disp_ and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []


RIDERS = ('data/b763_steps.json', 'data/b763_address_scan_commits.txt')   # ### the step row and the per-commit scan, in every commit by the one-call tool

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
    """standing clauses v9 (Component 6 of (R373): the close "as the standing clauses order them", the touch read of v9 banked before the root), N4: the touch read banked as data/b763_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b762's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R373-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b762's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R373) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b762's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R339)(7), carried in the run list: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base; run at b763 as (R373)(12) orders it, 64 REPRODUCES, 0 DIFFERS, 4 NOT RUN, the plants 64 of 64',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 83 = 83 OK + 0 misses; the ferry`s paths 38, OK 33, NONE 0; the check HALTED on one Lean-path row (halts 1), the cite true and the halt read in the step-zero bank before the deletes (defect (c)), as the step-zero bank enters it after the read-first bank and before the subject read and the deletes; the bank before the step-zero banks` commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b762-\w+) \((?:was )?[0-9a-f]{7,8}', r'\1 (', S['stepz']))),   # ### b763: the tip removed from "(was 622ea434, 21:59:39Z)" and the four after it (data/b763_stepzero.txt :66-:67); b762's form, the carried plant having wanted the tip closed by its paren
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s ACT line adjusted to what the act did: the control`s failure from its coefficients under (R373); b762 at its weight; the finite and signed parts of the form compiled at v0.42, 5 statements of 5, and One Page`s 19 rows of this kernel in one file; the statement of the control`s failure compiled before its proof, no proof sent; the orders priced beside it; the author`s words and canon XXV entered, 84 open to 83; the dispatches; each object`s bank in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R373)(1): the generated corrigendum for b762`s record, short, landed at FINDINGS :15797: b762`s 59 events and 11 defects by count from their banks, 70 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 6 CLOSE 64, REPEAT 50, the six CLAIM items (b762`s events (24)-(29)) printed in full; the seventeen findings after b762`s lock entered as b763`s events (14)-(30), CLAIM 0 CLOSE 17 REPEAT 14, each with its time; the navigator`s own five as events (31)-(35), CLAIM 5; [I1] with its cluster Day 1; the six repairs of (11) carried by name; no weight line; the corrigenda bank appended at row (83)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); by (R366)(2), data/b756_rules.txt`s rows (a) to (c), in force from b757, in b756`s commit 0a151012 and no other, the working tree its blob at HEAD; no data/b763_rules.txt, (R373) ordering no rules row; data/b760_rules.txt and data/b754_rules.txt not rewritten',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b763's objects
    ('G-REGISTRATIONS-FIRST', '(R373)(1), (9), N3, N4, N5: PLACE-papers written by the worklist`s chain of two in its order and by nothing else before the record -- the corrigendum in one commit touching FINDINGS alone (6034501c), no weight line; (9)`s ledgers in one commit appending to OPEN_TRAILS and the canon alone, each file`s bytes before a prefix, removing no line; each blob at its commit the sha the ledgers bank wrote; REGISTRY in no commit; the changed files within the act`s list; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('phase1.5/method/INSTRUMENTS.md'))),   # ### b763: a file outside the list (SPIRAL_MAP.md, the carried plant, is in b763's)
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b763_address_scan.py run live over every commit of the act in the relay, PLACE-papers and SIDE-explicit-formula, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, no byline excepted, (R373)`s N5 writing none (defect (k)), eight controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R373)(1)-(13), N2, N4: the act`s order by time across the relay and PLACE-papers -- the act_current commit and step zero`s banks, the ceiling tool, the c1 route and the corrigendum, the standing change of (5), the dispatch and pre-send tools before any kernel write, each act tool before its bank, the outcomes and the ceiling`s readings, the rulings tool and the ledgers, the reproduction run, then the handoff page and the lock gate -- and by ancestry within the relay; v1.37.2 the one standing version, its bank ALL AS WANTED at 10 cases, the one act commit under tools/standing/ ((R373)(11))',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update({next(iter(d), 'none'): False}))),   # ### b763: the first pair of the chain's ancestry set False (b762's planted key stood in no state of b763's)
    ('G-DERIVATION-GRADED', '(R373)(3), (5)-(9), N2, N3: each of the act`s eight generator rows (the ceiling, the dispatch tool`s controls, the pre-send reads of (6) and of (8), the outcomes, the IMP2-TAU reading, the author`s rulings, the ledgers) first added by a commit of its own, every one of its commits without its bank and the bank`s without it, the bank at HEAD its blob there; no row committed with its bank; the outcomes` words, each pre-send bank`s salt check, the controls`, the IMP2-TAU reading`s, the rulings`, the ledgers`, roster`s, corrigendum`s and reproduction run`s feet; the ceiling at HEAD its blob at its last reading`s commit, two readings, two of (8) carried and three built where they fit, dispatches 5 of 18 at it',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'ceiling', ((S['ceiling'] or (None, None))[0], 'planted'))),
    ('G-OFFSET-POST-HOC', 'N1, N5, (R373)(4)-(8), (12): the two kernels as the act left them -- SIDE-explicit-formula`s main locally and at origin at the peel of the last tag the act cut (v0.42 = 4964e957 after (6), and each tag of an order of (8) built in full), each tag`s object and peel the worklist`s; v0.39 at d1afb4fc, v0.40 at 630cba16 and v0.41 at a3aad4cc unmoved, v0.38 peeling to 14ca5725; its four held branches at their tips; push-b763-form, push-b763-arith and each order`s branch at its tip locally and at origin; no kernel branch removed by this act, push-b759-weil absent at origin, its local branch kept; each kernel commit on the remote ref it names, those on their own branches off the remote main; SIDE-dirichlet-mod-24`s main at e5ebdd15 at origin, push-b757-mod24 absent there, v0.2.0 peeling to main, v0.1.0 at 597b0869 and no other tag',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'kst', lambda d: d['ef'].update({'refs/tags/v0.40': ('0' * 40, K.WEIL_TAG[2])}))),   # ### b763: v0.40's peel planted at main a3aad4cc, a tag moved
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.34.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R373)(6)-(9), (12), N1, N3: the counts read from their banks -- (9)`s ledgers: OPEN_TRAILS and the canon appended, each a prefix, the identifiers 0 added, [C1], [A1] to [A12], [B1] and [B2] entered and the build lines after them; W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE CLOSED, W-ORD-PREMISE-POSITIONS entering OPEN, 84 open to 83, wanted 83; after the build lines each move an order of (8) built in full; the roster`s foot; the outcomes` runs within EF_RUNS, the dispatch rows` runs EF_RUNS in order; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: _mut(S, 'ledgersj', lambda d: (d.get('roster') or {}).update(before_open=83))),   # ### b763: the roster planted at 83 open before the lines, where 84 is wanted
    ('G-DIFFERS-ERRATA', '(R373)(1), (13): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD byte-equal to its blob at the act`s base, ERRATA in no commit of the act; no differs bank; the corrigendum in 6034501c, FINDINGS the one file there, its head at FINDINGS :15797; no weight line, (R373)(1) ordering none',
#⟪END⟫
# ### b763, Component 6: G-DIFFERS-ERRATA for (R373), which orders no ERRATA entry ((13)'s (W) list names no ERRATA.md) and no weight line
# ### -- the template's predicate (checks.tpl :1562-:1567) wants a weight line in FINDINGS; replaced whole here, b762's override (its two
# ### ERRATA entries of BLOCK E) retired with it
#⟪OVERRIDE checks MARK dd4dd9cb3d4b 6⟫
    """(R373)(1), (13): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md's working tree byte-equal to its blob at the act's base,
    ERRATA in none of PLACE-papers' commits of the act; no differs bank and no errata bank; the corrigendum at FINDINGS in Component 1's
    PLACE-papers commit, FINDINGS the one file there, its head at the worklist's CORR_LINE; no weight line, (R373)(1) ordering none."""
    pre_, now_ = S['errata_pp_pre'] or b'', S['errata_pp_now'] or b''
    return bool(pre_) and now_ == pre_ and not any('ERRATA.md' in (fs_ or []) for fs_ in (S['pp_files'] or {}).values()) \
        and not S['differs'] and not S['errata'] and K.ERRATA_LINE is None \
        and K.DIFFERS_LINE is None and K.WEIGHT_LINE is None and S['files']['c1pp'] == ['FINDINGS.md'] \
        and fline(S, K.CORR_LINE).startswith('## Corrigendum to b762')
#⟪END⟫
# ### b760, Component 5 (the Edit tool), defect (f): v1.36.2 taught the kernels face's writer to name SIDE-dirichlet-mod-24 (record.tpl :634)
# ### and not the suite's reader of the face (checks.tpl :611, its list without it), so G-KERNELS-UNTOUCHED's first clause (the face's
# ### kernels equal the kernels read) failed at the standing-a2 probe (05:51:52Z), 24 against 23; the reader takes the writer's own list, in
# ### the act's module for this act, the standing line carried to the next act's standing change (the misses read before the lock)
#⟪OVERRIDE checks MARK f8d771e18f03 1 REPAIR (face)⟫
        kern_face=(jl('b763_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns() + ['SIDE-faces-join', 'SIDE-dirichlet-mod-24'])),
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b763_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R373-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and the standing G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal to its blob at the act`s base 15f762dd (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R373)(5)-(8): every dispatch of the act a row of the dispatch bank, its kernel SIDE-explicit-formula, its free memory before the send at or above the hold; the run ids the worklist`s EF_RUNS within MAX_DISPATCHES, none in SIDE-dirichlet-mod-24; each read once after it by that id; the plant a dispatch row with no kernel and no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4, (R373)(5)-(8): each dispatch sent by tools/b763_controls.py`s dispatch route, one command in the capture for each dispatch row, each read once after it by its run id, every dispatch and read row`s free memory at or above the hold, the runs within the price table`s upper figures (b759`s form); no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel written beyond SIDE-explicit-formula ((R373)(5), (12); its main and tags read by G-OFFSET-POST-HOC): each repaired wave 1 kernel`s rebuild-b721 as b762 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at the worklist`s EF_MAIN, moved by the gated push`s default mode after a run`s success, and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS: the corrigendum and the entry; OPEN_TRAILS: the lines of (9) and the build lines under the dated head, and the trail; phase1.5/method/THE_METHOD_CANON.md: section XXV of [C1]; (R373)(1), (9), (13)); REGISTRY not written (N3); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    # ### b763, Component 3 (the Edit tool): the carried stub replaced -- b762's trail head as OPEN_TRAILS :18897 carries it (scratch ent763.py
    # ### through the masks, 2026-11-20T03:1xZ), in place of the carried needle, which named b761's head under b762's name
    ('G-PRIOR-CLOSED-PUSHED', 'b762`s trail record on OPEN_TRAILS (:18897) and its root in the chain', lambda S: '### b762 — lane two, act one hundred and eighty-nine, The re-cut of One Page under (R372)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the canon): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved; v0.38 to v0.41, b760`s removed branch and SIDE-dirichlet-mod-24 read by G-OFFSET-POST-HOC) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: each a row of the dispatch bank, within MAX_DISPATCHES; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b760 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b758's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b763: (R373)'s rows, written at step zero in place of b762's carried rows (the carry's stub, its body in the carry's diff bank); each
    # ### needle read from the line it names before the row was written (scratch facts763.py and fc763.py, read-only, 18:4xZ-19:2xZ; PLACE-papers
    # ### lines through qrule760.py, rule [Q] (3)'s heading found by its digest; kernel lines read as predicates, none printed). A place is named
    # ### by its role or its file name, never by a folder of the host (N5). A PLACE-papers file the act edits is read at the act's start
    # ### (K.PRE_PP) where a row asserts its text, so a later run reads the same; REGISTRY's protected section by predicate and digest alone.
    import hashlib as _h
    EF_ = 'D:/SIDE-explicit-formula'
    MOD_ = 'D:/SIDE-dirichlet-mod-24'
    KN_ = 'D:/SIDE-kernel'
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling SCOPE', 'relay main at the act`s start 3fe5b17c, b762`s closing step row, read back at the remote (or an ancestor of the remote`s main)',
        gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('3fe5b17c') and bool(rm) and gr('D:/relay', 'merge-base', '3fe5b17c', rm).startswith('3fe5b17c'), 'remote main %s' % rm[:8], '0')
    npp_, tpp_ = gr(PP, 'rev-list', '--count', K.PRE_PP), gr(PP, 'tag', '--list').split()
    add('ruling SCOPE', 'PLACE-papers main at the act`s start 87cab4f2: 2,218 commits and 2 tags there', gr(PP, 'rev-parse', K.PRE_PP).startswith('87cab4f2') and npp_ == '2218' and len(tpp_) == 2,
        '%s ; %s commits ; %d tags' % (K.PRE_PP[:8], npp_, len(tpp_)), '0')
    TAGS_ = (('v0.38', '21c6edaf', '14ca5725'), ('v0.39', '69da6cd7', 'd1afb4fc'), ('v0.40', 'd86d8cf5', '630cba16'), ('v0.41', '390506fc', 'a3aad4cc'))
    er_ = _remote_heads(EF_)
    erm_ = er_.get('refs/heads/main') or ''
    add('ruling SCOPE, (5), (6), (12), N5', 'SIDE-explicit-formula: main a3aad4cc (v0.41) at the act`s start, push-b763-form`s base ((6)); v0.38 to v0.41 the tag objects 21c6edaf, 69da6cd7, d86d8cf5 and 390506fc peeling to 14ca5725, d1afb4fc, 630cba16 and a3aad4cc (to peel so at the close); the remote`s main a3aad4cc or its descendant ((6) and (7) move it after a run`s success alone); push-b759-weil absent at the remote',
        K.EF_MAIN.startswith('a3aad4cc') and all(gr(EF_, 'rev-parse', t_).startswith(o_) and gr(EF_, 'rev-parse', t_ + '^{commit}').startswith(c_) for t_, o_, c_ in TAGS_)
        and bool(erm_) and gr(EF_, 'merge-base', 'a3aad4cc', erm_).startswith('a3aad4cc') and 'refs/heads/push-b759-weil' not in er_,
        'remote main %s ; push-b759-weil %s ; v0.41 peel %s' % (erm_[:8] or '-', 'PRESENT' if 'refs/heads/push-b759-weil' in er_ else 'absent', gr(EF_, 'rev-parse', 'v0.41^{commit}')[:8]), '0')
    mr_ = _remote_heads(MOD_)
    add('ruling (12), N5', 'SIDE-dirichlet-mod-24: the remote`s main e5ebdd15 with v0.2.0, the tag object e5c84316, peeling to it (to peel so at the close; no kernel beyond SIDE-explicit-formula touched)',
        gr(MOD_, 'rev-parse', 'v0.2.0').startswith('e5c84316') and gr(MOD_, 'rev-parse', 'v0.2.0^{commit}').startswith('e5ebdd15') and (mr_.get('refs/heads/main') or '').startswith('e5ebdd15'),
        'remote main %s ; v0.2.0 peel %s' % ((mr_.get('refs/heads/main') or '-')[:8], gr(MOD_, 'rev-parse', 'v0.2.0^{commit}')[:8]), '0')
    add('ruling (12), N5', 'SIDE-kernel`s clone: v1.5 the tag object 922c0fc7 peeling to 0e5233f0, its main at f8534ef2, nothing changed (no kernel beyond SIDE-explicit-formula touched)',
        gr(KN_, 'rev-parse', 'v1.5').startswith('922c0fc7') and gr(KN_, 'rev-parse', 'v1.5^{commit}').startswith('0e5233f0') and gr(KN_, 'rev-parse', 'main').startswith('f8534ef2')
        and not gr(KN_, 'status', '--porcelain', '-uno'), 'v1.5 peel %s ; main %s' % (gr(KN_, 'rev-parse', 'v1.5^{commit}')[:8], gr(KN_, 'rev-parse', 'main')[:8]), '0')
    mi_ = lines_of(p('data', 'b762_mirror.txt'))
    add('ruling SCOPE', 'data/b762_mirror.txt :3, b762`s mirror: MANIFEST md5 a4290f9b2dd085db4566390af36c5ed3 (the SCOPE line`s a4290f9b), 84 files with MANIFEST',
        'md5 a4290f9b2dd085db4566390af36c5ed3' in at(mi_, 3) and 'files 84 + MANIFEST' in at(mi_, 3), at(mi_, 3)[:60], '0')
    # ### (R373)(1): b762 at its weight, from its closing bank's head line; (4): its carried list (f) and (g)
    add('ruling (1)', 'data/b762_closing.txt :1, the head line: relay efb9acb6, PLACE-papers 87cab4f, suite 111 of 116, 1 prompt answered, scores 7 of 8 HELD, 11 defects',
        at(cl, 1).startswith('b762 closed: relay efb9acb6, PLACE-papers 87cab4f; suite 111 of 116;') and '1 prompt answered; scores 7 of 8 HELD; 11 defects' in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (4)', 'data/b762_closing.txt :829-:834, CARRIED FORWARD (f) and (g): the push-b762* branches left for this step zero, the kept branches by name, the closing push-out bank for this act to commit',
        at(cl, 829).lstrip().startswith('(f) Branches left for the next act`s step zero: the push-b762* branches of relay and PLACE-papers. KEPT, not for deletion:')
        and 'port-b707 of SIDE-lv-conservation' in at(cl, 830) and 'push-b759-weil' in at(cl, 831) and 'push-b757-workflow of SIDE-dirichlet-mod-24' in at(cl, 832) and 'corrigendum-b723' in at(cl, 832)
        and at(cl, 834).lstrip().startswith('(g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.'), 'present', '0')
    # ### N3, N5: REGISTRY's heading of rule [Q] (3) by its digest alone, at the act's start (REGISTRY not written this act); the canon's XXIV
    # ### and its foot line, after which [C1] is appended as XXV ((R373)(9))
    rg0_ = _blob(PP, K.PRE_PP, 'REGISTRY.md').split(NL)
    hq_ = [k_ for k_, l_ in enumerate(rg0_, 1) if _h.sha256(l_.encode('utf-8')).hexdigest().startswith('53d53060a58f6b9b')]
    add('N3, N5', 'REGISTRY at the act`s start: rule [Q] (3)`s heading found by the sha256 of its line, opening 53d53060a58f6b9b, at one line (:374); no line of the section printed; REGISTRY not written this act',
        hq_ == [374], 'lines carrying the digest %d, at %s' % (len(hq_), hq_), '5')
    cn0_ = _blob(PP, K.PRE_PP, 'phase1.5/method/THE_METHOD_CANON.md').split(NL)
    add('ruling (9), ferry (read first)', 'THE_METHOD_CANON.md at the act`s start: :384 XXIV, what a keystone carries; :388 b761`s appended note; :390 the foot line beside XXIII (C), the file`s last (390 lines); [C1] appended after it as XXV',
        at(cn0_, 384).startswith('## XXIV. What a keystone carries (added 2026-11-18, b761') and at(cn0_, 388).startswith("*Appended by b761 on the author's ruling")
        and at(cn0_, 390).startswith('*Beside XXIII (C), added 2026-11-18 by b761') and len(cn0_) == 391 and cn0_[-1] == '', '%d lines' % (len(cn0_) - 1), '5')
    # ### [I1] and (10): REGISTRY's row d1-8, the page's file beside it, and SPIRAL_MAP's cluster table at the act's start -- the cluster of
    # ### THE_EPSTEIN_CONTROL_OBJECT read at its row; no cluster row naming d1-8 or One Page, so [I1]'s cluster reads "Day 1"
    sm0_ = _blob(PP, K.PRE_PP, 'SPIRAL_MAP.md').split(NL)
    cr_ = [k_ for k_ in range(247, 294) if 'd1-8' in at(sm0_, k_) or 'ONE_PAGE' in at(sm0_, k_)]
    add('ruling [I1], (1)(iv)', 'REGISTRY :90, the row d1-8, One Page at v1.0 by `day1/ONE_PAGE_PROOF.md`; day1/ONE_PAGE_PROOF_v2_0.md, its next edition, present by its blob`s type; SPIRAL_MAP`s cluster table (:247-:293) naming neither d1-8 nor One Page, so the cluster reads "Day 1"',
        at(rg0_, 90).startswith('| d1-8 | One-Page Proof (supplement) | `day1/ONE_PAGE_PROOF.md` | v1.0 |') and gr(PP, 'cat-file', '-t', K.PRE_PP + ':day1/ONE_PAGE_PROOF_v2_0.md') == 'blob'
        and at(sm0_, 247).startswith('### Clusters') and at(sm0_, 294).startswith('### Cross-cluster bridges') and not cr_, 'cluster rows naming it %s' % (cr_ or 'none'), '1')
    add('ruling (10)', 'SPIRAL_MAP :276, the cluster row of THE_EPSTEIN_CONTROL_OBJECT: The Epstein instance (seated 2026-11-09, b750), its keystone phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md, present at the act`s start',
        at(sm0_, 276).startswith('| **The Epstein instance** (seated 2026-11-09, b750) | `phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md` -- keystone')
        and gr(PP, 'cat-file', '-t', K.PRE_PP + ':phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md') == 'blob', 'present', '6')
#⟪END⟫
#⟪SECTION citation 2⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 2); the body carried, 0 code lines, stands in the carry`s diff bank
    # ### b761: no row between the events bank's read and its numbers
#⟪END⟫
#⟪SECTION citation 3⟫
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
# ### CARRIED STUB (tools/standing/carry.py v1.34.0): a citation section (SECTION citation 3); the body carried, 0 code lines, stands in the carry`s diff bank
    # ### b761: no row between the events' numbers and the defects bank's read
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b763 step zero: (R373)(1)'s counts over b762's banks, written in place of b762's rows over b761's: its events (1)-(59) and its
    # ### defects (a)-(k), each row tagged by the reader's owner form -- the events 53 CLOSE and 6 CLAIM, the defects 11 CLOSE and 0 CLAIM, as
    # ### the banks read at 18:4xZ (scratch facts763.py a); no post-seal events bank at b762 (the seventeen findings after the lock stand in its
    # ### closing message, entered as b763's events with their times); the navigator's own items (i)-(v) of (1), CLAIM, enter b763's corrigendum
    add('ruling (1), ferry (read first)', 'b762`s events (1)-(59) and its 11 lettered defects (a)-(k), no post-seal events bank (data/b762_events.txt, data/b762_defects.txt)',
        starts == list(range(1, 60)) and letters == list('abcdefghijk') and not os.path.exists(p('data', 'b762_events_postseal.txt')),
        'events %s ; letters %d (%s-%s) ; post-seal %s' % (starts[-1:], len(letters), letters[:1], letters[-1:], 'absent' if not os.path.exists(p('data', 'b762_events_postseal.txt')) else 'PRESENT'), '1')
    TAG_ = re.compile(r"^    \((?:\d+|[a-z]'*)\) THE ([A-Z' ]+?)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    for f_, L_, nr_, ncl_ in (('data/b762_events.txt', ev, 59, 6), ('data/b762_defects.txt', dl, 11, 0)):
        rr_ = [l_ for l_ in L_ if re.match(r"^    \((\d+|[a-z]'*)\) ", l_)]
        tg_ = [m_.group(2) for m_ in (TAG_.match(l_) for l_ in rr_) if m_]
        add('ruling (1), ferry (read first)', '%s: %d rows, each tagged by the reader`s owner form, CLAIM %d and CLOSE %d' % (f_, nr_, ncl_, nr_ - ncl_),
            len(rr_) == nr_ and len(tg_) == nr_ and tg_.count('CLAIM') == ncl_ and tg_.count('CLOSE') == nr_ - ncl_,
            'rows %d ; tagged %d ; CLAIM %d ; CLOSE %d' % (len(rr_), len(tg_), tg_.count('CLAIM'), tg_.count('CLOSE')), '1')
    fi0_ = _blob(PP, K.PRE_PP, 'FINDINGS.md').split(NL)
    ot0_ = _blob(PP, K.PRE_PP, 'OPEN_TRAILS.md').split(NL)
    add('ruling (1)', 'FINDINGS :%d, b762`s entry, the re-cut of One Page under (R372); :%d, b761 at its weight inside it' % (K.B711_ENTRY, 15757),
        at(fi0_, K.B711_ENTRY).startswith('## The re-cut of One Page under (R372): b761’s close at its weight') and at(fi0_, 15757).startswith('**b761 at its weight and the corrigendum** ((R372)(1))'),
        'present', '1')
    add('ruling (1), [I1], Component 6', 'FINDINGS :%d, b762`s corrigendum to b761`s record, short, the form b763`s follows; no weight line of its own; FINDINGS` last line :15795 at the act`s start, b762`s bare INTEGRATION line, which [I1] corrects' % K.B711_CORRIGENDUM,
        at(fi0_, K.B711_CORRIGENDUM).startswith('## Corrigendum to b761’s record, short') and K.B711_WEIGHT is None and max([k_ for k_, l_ in enumerate(fi0_, 1) if l_.strip()] or [0]) == 15795
        and at(fi0_, 15795) == 'INTEGRATION: cluster no seat in the cluster table ; keystone none yet ; stage BANKED', 'present', '1')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b762`s trail record' % K.B711_TRAIL, at(ot0_, K.B711_TRAIL).startswith('### b762 — lane two, act one hundred and eighty-nine, The re-cut of One Page under (R372)'),
        'present', '1')
    add('ruling (1), (9)', 'OPEN_TRAILS :%d, b762`s open-orders line, 84 open; :18951, its scores line (N2 REFUTED); :18953, its Next line, the file`s last at the act`s start' % K.TRAIL_ORDERS,
        at(ot0_, K.TRAIL_ORDERS).startswith('**The open orders:** 84 open') and at(ot0_, 18951).startswith('**N1 HELD · N2 REFUTED · N3 PENDING · N4 HELD · N5 HELD')
        and at(ot0_, 18953).startswith('**Next:**') and max([k_ for k_, l_ in enumerate(ot0_, 1) if l_.strip()] or [0]) == 18953, 'present', '1')
    # ### SCOPE READ, (7), (9): W-ORD-LI-ARITH's entry and the author's word on it; b762's dated head and the bank line of the author's word
    add('ruling SCOPE, (7), ferry (read first)', 'OPEN_TRAILS :17714, W-ORD-LI-ARITH entered (b743); :18783, the author`s word (1) on it, of 2026-11-18; :18849, b762`s dated head for (R372)(7) and (8); :18881, the bank line of the author`s word of 2026-11-18',
        at(ot0_, 17714).startswith('**`W-ORD-LI-ARITH` ENTERED at b743') and at(ot0_, 18783).startswith('(1), on `W-ORD-LI-ARITH` (its first line :17714)')
        and at(ot0_, 18849).startswith('**Dated head, 2026-11-19, b762, `(R372)`(7) and (8)') and at(ot0_, 18881).startswith('The author’s word of 2026-11-18'), 'present', '5')
    # ### (8), (9): the orders the ruling names, each carried by its entry's lines at the act's start; W-ORD-PREMISE-POSITIONS, which [B2]
    # ### enters, carried by none
    ORD_ = ('W-ORD-KEIPER-FACE', 'W-ORD-E2-SEPARATION', 'W-ORD-BESSEL-BOUND-TIGHTEN', 'W-ORD-EXPLICIT-FORMULA-C1', 'W-ORD-WINDOW-CERTIFY', 'W-ORD-SQUARES-AT-24',
            'W-ORD-IMP2-TAU', 'W-ORD-ADMISSIBLE-CONE', 'W-ORD-STATEMENT-PIN', 'W-ORD-BIBLIOGRAPHY-LINK', 'W-ORD-E0-RANK-PROPAGATION', 'W-ORD-ZETA23-SERIAL-BUILD',
            'W-ORD-LI-WEIL-BRIDGE', 'W-ORD-ZQ-FAMILY', 'W-ORD-P2-9-RESYNC', 'W-ORD-GW-IMPORT', 'W-ORD-TABLE-SHAPE', 'W-ORD-SIGN-SECTORS', 'W-ORD-SEAM-UPSTREAM',
            'W-ORD-VENDOR-FINALMULT', 'W-ORD-PNT-CHI', 'W-ORD-STRICT-BOUND', 'W-ORD-H2-PI1', 'W-ORD-LI-ARITH', 'W-ORD-STATEMENT-FILE', 'W-ORD-PRINT-TARGETS')
    nb_ = [o_ for o_ in ORD_ if not any('`%s`' % o_ in l_ for l_ in ot0_)]
    pp2_ = any('`W-ORD-PREMISE-POSITIONS`' in l_ for l_ in ot0_)
    add('ferry (read first), (8), (9)', 'OPEN_TRAILS at the act`s start: each of the %d orders that (8), [A1] to [A12], [B1] and (9)`s held five name, with W-ORD-LI-ARITH, W-ORD-STATEMENT-FILE and W-ORD-PRINT-TARGETS, carried by its entry`s lines; W-ORD-PREMISE-POSITIONS, which [B2] enters, carried by none' % len(ORD_),
        len(ORD_) == 26 and not nb_ and not pp2_, 'unfound %s ; PREMISE-POSITIONS %s' % (nb_ or 'none', 'FOUND' if pp2_ else 'absent'), '5')
    # ### PATHS: by role, as the ruling spells none and N5 names no folder of the host in a bank
    add('PATHS', 'the relay and PLACE-papers at the places the seat`s file and progress note hold, each a clone', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), 'present', '0')
    add('PATHS', 'the two shelves', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'the clones of SIDE-explicit-formula and SIDE-kernel (each read at its tag by (6), no touch) and SIDE-dirichlet-mod-24 (read alone)', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git') and os.path.isdir('D:/SIDE-dirichlet-mod-24/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file by its hash alone', bool(_h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), _h.sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry, (5), (11)', 'tools/standing/ at v1.37.1 entering the act, moved where (5) requires and nowhere else, VERSION with it ((R373)(11), N2, read at the act`s start)', (_blob('D:/relay', K.PRE_RELAY, 'tools/standing/VERSION') or '').strip() == 'v1.37.1',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '0')
    # ### b762's mirror the last built, by its file name and hash, the folder that holds it not printed (N5)
    mz_ = open(K.MIRROR_ZIP, 'rb').read() if os.path.exists(K.MIRROR_ZIP) else b''
    add('ruling SCOPE, (13)', 'b762`s mirror, the last built: %s (sha256 %s, 5,044,723 bytes); this act`s mirror carries the canon`s XXV' % (os.path.basename(K.MIRROR_ZIP), _h.sha256(mz_).hexdigest()[:8]),
        _h.sha256(mz_).hexdigest().startswith('874f495b3f052675') and len(mz_) == 5044723 and 'b762' in K.MIRROR_ZIP, '%d bytes' % len(mz_), '6')
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [os.path.basename(k_) for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R373)(5), (12), N5: the three kernels' clones at step zero, clean, as b762 left them (SIDE-explicit-formula on push-b759-weil at
    # ### main's commit, switched to push-b763-form by (5)'s route; SIDE-dirichlet-mod-24 on push-b757-mod24 at its main's commit; SIDE-kernel on main)
    kc2_ = [(os.path.basename(r_), gr(r_, 'rev-parse', '--abbrev-ref', 'HEAD'), gr(r_, 'status', '--porcelain', '-uno')) for r_ in (EF_, MOD_, KN_)]
    add('ruling (5), (12), N5', 'the three kernels` clones with nothing changed or staged at step zero: SIDE-explicit-formula on push-b759-weil (or main, or a push-b763-* branch), SIDE-dirichlet-mod-24 on push-b757-mod24 (or main), SIDE-kernel on main',
        (kc2_[0][1] in ('push-b759-weil', 'main') or kc2_[0][1].startswith('push-b763-')) and kc2_[1][1] in ('push-b757-mod24', 'main') and kc2_[2][1] == 'main' and not any(s_ for _n, _h2, s_ in kc2_),
        ' ; '.join('%s %s %s' % (n_, h_, 'clean' if not s_ else 'CHANGED') for n_, h_, s_ in kc2_), '0')
#⟪END⟫
#⟪SECTION citation 6⟫
    # ### b763: (R373)(3)-(12)'s rows. A relay tool is read at the act's start (K.PRE_RELAY); a kernel file at its tag v0.41, by predicate
    rr0_ = lambda path_: _blob('D:/relay', K.PRE_RELAY, path_).replace(chr(13), '').split(NL)   # noqa: E731
    # ### (R373)(5): the route -- the one-call tool's kernel tables at the act's start open SIDE-explicit-formula for b757 to b759 and name no
    # ### b763, so (5)'s one change under tools/standing/ admits this act's branch names (VERSION moved, a planted control); the gated push;
    # ### b759's controls tool and its pre-send reads, carried
    cm_ = rr0_('tools/standing/commit.py')
    add('ruling (5)', 'tools/standing/commit.py :134 KERNEL_ACTS, :141 FF_ACTS and :145 PUSHTO_ACTS at the act`s start: SIDE-explicit-formula opened for b757 to b759, b763 named by none -- the route to be opened for b763 by (5)`s one change, VERSION moved and a planted control',
        at(cm_, 134).startswith('KERNEL_ACTS = {') and "'b759': ('SIDE-explicit-formula',)}" in at(cm_, 136) and at(cm_, 141).startswith('FF_ACTS = {') and "'b759': ('SIDE-explicit-formula',)}" in at(cm_, 142)
        and at(cm_, 145).startswith('PUSHTO_ACTS = {}') and not any("'b763'" in l_ for l_ in cm_), 'b763 named %s' % any("'b763'" in l_ for l_ in cm_), '1')
    add('ruling (5)', 'tools/push_gated.sh, the gated push: its branch mode for a dispatch, its default mode to move main without force', os.path.exists(p('tools', 'push_gated.sh')),
        'present' if os.path.exists(p('tools', 'push_gated.sh')) else 'ABSENT', '1')
    bc_ = rr0_('tools/b759_controls.py')
    add('ruling (5)', 'tools/b759_controls.py :2, the dispatch and the read b759 used (560 lines); :61, the kernel ef by build-module.yml; :66, the remote heads it reads -- carried to this act and committed before its opening dispatch',
        at(bc_, 2).startswith('"""tools/b759_controls.py -- (R369)(5): THE DISPATCH AND THE READ') and "workflow='build-module.yml'" in at(bc_, 61) and at(bc_, 66).startswith('REMOTE_HEADS = re.compile(') and len(bc_) == 561,
        '%d lines' % (len(bc_) - 1), '1')
    ps_ = lines_of(p('data', 'b759_presend.txt'))
    add('ruling (5), (6), ferry (read first)', 'data/b759_presend.txt :1, the pre-send reads of (R368)(4), carried; :49, the salt check printed before the send',
        at(ps_, 1).startswith('b759 -- (R369)(5): THE PRE-SEND READS OF (R368)(4), CARRIED') and at(ps_, 49).startswith('### (R369)(5): the salt check, printed before the send'), 'present', '1')
    f757_ = lines_of(p('data', 'b757_ferry.txt'))
    f759_ = lines_of(p('data', 'b759_ferry.txt'))
    add('ruling (5), ferry (read first)', 'data/b757_ferry.txt :13, (3) the route for kernel writes; data/b759_ferry.txt :17, (5) the build on push-b759-weil made at main',
        at(f757_, 13).startswith('(3) THE ROUTE FOR KERNEL WRITES, BEFORE ANY BUILD.') and at(f759_, 17).startswith('(5) THE STATEMENT AND THE PRINT LINES, in SIDE-explicit-formula. The branch push-b759-weil is made at main 630cba16.'),
        'present', '1')
    # ### (R373)(3): the price table's form and the banked prices it reads
    pr_ = lines_of(p('data', 'b757_price.txt'))
    ap_ = lines_of(p('data', 'b752_attribution_plan.txt'))
    add('ruling (3), ferry (read first)', 'data/b757_price.txt :1, the price table`s form, :6 its banked timings, :11 its table, :39 its ceiling of 24 hours against the lower figures; data/b752_attribution_plan.txt :52 and :62, a Lean price from its nearest compiled neighbours',
        at(pr_, 1).startswith('b757 -- STEP ZERO, (R367)(2): THE PRICE TABLE, FROM BANKED TIMINGS') and at(pr_, 6).startswith('## THE BANKED TIMINGS THE TABLE READS') and at(pr_, 11).startswith('## THE TABLE')
        and at(pr_, 39).startswith('## THE CEILING ((R367)(2)): 24 hours against the lower figures') and at(ap_, 52).lstrip().startswith('PRICE: 40-120 lines') and at(ap_, 62).lstrip().startswith('PRICE: 150-450 lines'),
        'present', '0')
    # ### (R373)(6), (7): the definitions and lemmas each statement rests on, and the names (7)'s control forbids, at SIDE-explicit-formula
    # ### v0.41, each at its line, read as predicates (no kernel line printed)
    DQ_ = lambda n_: r'\b(theorem|lemma|def|abbrev|structure|inductive|instance)\s+(\S+\.)?' + re.escape(n_) + r'\b'   # noqa: E731
    EFD_ = (('primeSum', 'SIDEExplicitFormula/B321Identity.lean', 33), ('poleTerm', 'SIDEExplicitFormula/B321Identity.lean', 29), ('archTerm', 'SIDEExplicitFormula/B321Identity.lean', 37),
            ('classK', 'SIDEExplicitFormula/H2Sign.lean', 24), ('h2_sign', 'SIDEExplicitFormula/H2Sign.lean', 29), ('h2_sign_upto', 'SIDEExplicitFormula/DetectionRegion.lean', 29),
            ('primeTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 112), ('bracketQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 117), ('archTermQ', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 121),
            ('classK_of_real_even', 'SIDEExplicitFormula/PowerWindow.lean', 52), ('weilTest_phiC', 'SIDEExplicitFormula/PowerWindow.lean', 64), ('paperFT', 'Zeta23/Defs.lean', 60),
            ('tilde', 'Zeta23/ExplicitFormula.lean', 64), ('weilTest', 'Zeta23/ExplicitFormula.lean', 68), ('paperFT_weilTest', 'Zeta23/ExplicitFormula.lean', 205),
            ('liCoeff', 'SIDEExplicitFormula/Schema/Wide/Converse.lean', 32), ('zqZeroConfig', 'SIDEExplicitFormula/Schema/ZQ/Zeros.lean', 319), ('cQ', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 63),
            ('cQ_one', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 225), ('cQ_forty_eight', 'SIDEExplicitFormula/Schema/ZQ/Mechanism/CoeffSign.lean', 281))
    efm_ = [n_ for n_, f_, k_ in EFD_ if not re.search(DQ_(n_), at(_blob(EF_, 'v0.41', f_).split(NL), k_))]
    add('ruling (6), (7), SCOPE', 'the %d definitions and lemmas the statements of (6) and (7) rest on at SIDE-explicit-formula v0.41 (primeSum, poleTerm, archTerm, classK, h2_sign, h2_sign_upto, primeTermQ, bracketQ, archTermQ, classK_of_real_even, weilTest_phiC, paperFT, tilde, weilTest, paperFT_weilTest, Wide.liCoeff, zqZeroConfig, cQ, cQ_one, cQ_forty_eight), each at its line; misses 0 (no line printed)' % len(EFD_),
        len(EFD_) == 20 and not efm_, 'misses %d (%s)' % (len(efm_), ', '.join(efm_) or 'none'), '2')
    ZN_ = (('zq_offline_zero', 'SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 32), ('zq_li_nonneg_fails', 'SIDEExplicitFormula/Schema/ZQ/OffZero/SP4.lean', 36),
           ('wide_detector', 'SIDEExplicitFormula/Schema/Wide/HalfScale.lean', 277), ('detector', 'SIDEExplicitFormula/Schema/Detector.lean', 99),
           ('zq_arith_side_re_neg', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean', 26), ('zq_weil_positivity_fails', 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean', 44),
           ('h2_sign_iff_rh', 'SIDEExplicitFormula/Seam.lean', 101))
    znm_ = [n_ for n_, f_, k_ in ZN_ if not re.search(DQ_(n_), at(_blob(EF_, 'v0.41', f_).split(NL), k_))]
    add('ruling (7), [C1]', 'the five names (7)`s control forbids (zq_offline_zero and zq_li_nonneg_fails, Schema/ZQ/OffZero/SP4.lean :32, :36; wide_detector, Schema/Wide/HalfScale.lean :277; detector, Schema/Detector.lean :99; zq_arith_side_re_neg, Schema/Wide/HalfScaleControl.lean :26) and the two [C1] works at (zq_weil_positivity_fails, :44 there; h2_sign_iff_rh, Seam.lean :101), each at its line at v0.41; misses 0',
        not znm_, 'misses %d (%s)' % (len(znm_), ', '.join(znm_) or 'none'), '3')
    pt_ = _blob(EF_, 'v0.41', 'print_targets.txt').split(NL)
    P1_ = ('b321_identity', 'h2_sign_chi_iff_grh_chi', 'h2_sign_cfg_iff_target', 'arith_limit_nonneg_iff_rh', 'h2_sign_iff_forall_upto', 'liCoeff_one_pos')
    add('ruling (6), [P1] of (R372)', 'print_targets.txt at v0.41 (489 lines) holding none of the six names [P1] adds; its last line the qualified zq_weil_positivity_fails',
        not any(re.search(r'\b' + re.escape(q_) + r'\b', l_) for q_ in P1_ for l_ in pt_) and len(pt_) == 490 and at(pt_, 489) == 'SIDEExplicitFormula.Schema.ZQ.zq_weil_positivity_fails',
        '%d lines' % (len(pt_) - 1), '2')
    wf_ = _blob(EF_, 'v0.41', '.github/workflows/build-module.yml').split(NL)
    add('ruling (5), (6)', 'SIDE-explicit-formula v0.41, .github/workflows/build-module.yml, the workflow a dispatch runs (146 lines)', len(wf_) == 147, '%d lines' % (len(wf_) - 1), '2')
    # ### (R373)(7), (12): b709's entry, the one read the window's choice may take; the bank of zeros whose head line alone is read
    hz_ = open(p('data', 'b725_interference.txt'), encoding='utf-8', errors='replace').readline() if os.path.exists(p('data', 'b725_interference.txt')) else ''
    add('ruling (7), (12), ferry (read first)', 'FINDINGS :10198, b709`s entry on the fine grid (a = 10.3853 for the band zero`s family, a = 6.8384 at rho_0`s), read for (7)`s window alone; data/b725_interference.txt :1, a bank of zeros, its head line alone read, no row opened',
        at(fi0_, 10198).startswith('## The sign-onset radius at the Epstein zeta of x² + xy + 6y² on the fine grid: a = 10.3853') and 'a = 6.8384' in at(fi0_, 10198)
        and hz_.startswith('b725 -- (R335)(9): H-INTERFERENCE'), 'present', '3')
    # ### (R373)(1), (9), (10), (12): b762's banks, the reader, the hours' form, the cadence and the reproduction
    ms_ = lines_of(p('data', 'b762_misses.txt'))
    aa_ = lines_of(p('data', 'b762_author_answers.txt'))
    add('ruling (1), ferry (read first)', 'data/b762_misses.txt :1-:20, the seat`s read of what (R372) missed, whose (6) to (10) the navigator`s items (i) to (v) cite; data/b762_author_answers.txt :7, the result of the root`s one prompt',
        at(ms_, 1).startswith("b762 -- THE SEAT'S READ OF WHAT (R372) MISSES") and len(ms_) == 21 and at(aa_, 7).startswith('RESULT (transcript line 190063, 2026-11-19T16:16:19.599Z)'),
        '%d lines' % (len(ms_) - 1), '1')
    od_ = rr0_('tools/standing/orders.py')
    add('ruling (9), ferry (read first)', 'tools/standing/orders.py :2, the open orders generated from the record (435 lines at the act`s start), run after the lines of (6) to (9)',
        at(od_, 2).startswith('"""standing/orders.py -- THE OPEN ORDERS GENERATED FROM THE RECORD') and len(od_) == 436, '%d lines' % (len(od_) - 1), '5')
    cy_ = lines_of(p('data', 'b754_close_yield.txt'))
    cd_ = rr0_('tools/standing/cadence.py')
    add('ruling (10), ferry (read first)', 'data/b754_close_yield.txt :43, (A) the hours by the step rows; tools/standing/cadence.py :2, v1.34.9, the cadence of the passes (600 lines at the act`s start)',
        at(cy_, 43).startswith('## (A) THE HOURS BY THE STEP ROWS') and 'THE CADENCE OF THE PASSES' in at(cd_, 2) and len(cd_) == 601, '%d lines' % (len(cd_) - 1), '6')
    add('ruling (12)', 'tools/research/reproduce.py, the reproduction the standing clauses order run in full', os.path.exists(p('tools', 'research', 'reproduce.py')), 'present', '6')
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (4)', 'the push-b762-* branches of %s, --merged into main before their deletes (no local branch left after them)' % ('the relay' if repo_ == 'D:/relay' else 'PLACE-papers'),
            sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R373)(3): act_current alone, then b762's carried files through the one-call tool, in the worklist's order (K.STEPZERO_CARRIED), each
    # ### commit read for its files -- all three carried: the closing push-out bank alone; tools/mirror_prevbuild.json (2 lines of content, not
    # ### line ends alone) with data/act_current.json naming it in shared_edits; the scan bank alone
    WANT_ = {'9fbd3ac6': ['data/b762_relay_push-b762-closing_push_out.txt'], 'b17f66d6': ['data/act_current.json', 'tools/mirror_prevbuild.json'],
             'dc063f7d': ['data/b763_address_scan_commits.txt']}
    if not K.ACT_CURRENT_COMMIT:
        add('ruling (3)', 'data/act_current.json -- TO BE COMMITTED at step zero', False, 'NOT COMMITTED', '0')
    else:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', K.ACT_CURRENT_COMMIT).split()
        add('ruling (3)', 'data/act_current.json committed alone at %s, an ancestor of HEAD' % K.ACT_CURRENT_COMMIT, nm_ == ['data/act_current.json']
            and gr('D:/relay', 'merge-base', K.ACT_CURRENT_COMMIT, 'HEAD').startswith(K.ACT_CURRENT_COMMIT), ' '.join(nm_)[:90], '0')
    for c_, s_, w_ in K.STEPZERO_CARRIED:
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3)', 'b762`s carried files, %s, committed at %s (step %d), an ancestor of HEAD' % (w_, c_, s_), sorted(nm_) == sorted(WANT_.get(c_, ['?']))
            and gr('D:/relay', 'merge-base', c_, 'HEAD').startswith(c_), '%d files' % len(nm_), '0')
    add('ruling (3)', 'the three carried files of (3) committed: the closing push-out bank, tools/mirror_prevbuild.json and data/b763_address_scan_commits.txt',
        sorted(f_ for c_, _s, _w in K.STEPZERO_CARRIED for f_ in WANT_.get(c_, []) if f_ != 'data/act_current.json')
        == sorted(['data/b762_relay_push-b762-closing_push_out.txt', 'tools/mirror_prevbuild.json', 'data/b763_address_scan_commits.txt']) and K.STEPZERO_PREVBUILD == 'b17f66d6',
        '%d commits' % len(K.STEPZERO_CARRIED), '0')
    left_ = gr('D:/relay', 'status', '--porcelain', '--', 'data/b762_relay_push-b762-closing_push_out.txt', 'tools/mirror_prevbuild.json')
    add('ruling (3)', 'the closing push-out bank and the builder`s state file b762 left uncommitted, each clean at HEAD after its commit', not left_, left_.replace(NL, ' | ') or 'clean', '0')
    fb_ = open(p('data', 'b763_ferry.txt'), 'rb').read() if os.path.exists(p('data', 'b763_ferry.txt')) else b''
    fbl_ = fb_.split(b'\n')
    add('ruling PATHS, (3)', 'data/b763_ferry.txt, the one-part delivery banked: 147 lines, LF line ends, sha256 ae0a4b1b142de092..., RULING (R373) BEGIN at :1 and FERRY END at :147',
        len(fbl_) >= 147 and b'\r' not in fb_ and _h.sha256(fb_).hexdigest().startswith('ae0a4b1b142de092') and fbl_[0] == b'RULING (R373) BEGIN' and fbl_[146] == b'FERRY END',
        '%d bytes ; %d line ends ; sha256 %s' % (len(fb_), fb_.count(b'\n'), _h.sha256(fb_).hexdigest()[:8]), '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (4)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    add('ruling (4)', 'push-b759-weil kept on SIDE-explicit-formula`s clone at a3aad4cc, absent at the remote (b762`s list (f), :831)',
        gr('D:/SIDE-explicit-formula', 'rev-parse', '--verify', '--quiet', 'push-b759-weil').startswith('a3aad4cc'), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (4)', '%s as banked on %s' % (K.PIN_BRANCH, k_), True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3)', 'tools/mirror_prevbuild.json, the builder`s state file the mirror reads, committed at step zero (b17f66d6)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '0')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ruling (3), ferry (read first)', 'data/b763_readfirst.txt, the readfirst bank, written by its tool before this check', os.path.exists(p('data', 'b763_readfirst.txt')),
        'present' if os.path.exists(p('data', 'b763_readfirst.txt')) else 'ABSENT', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair, carried: the needle reads both wordings of a version ("data/standing_clauses_v9.txt" and "standing clause v9")
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 6) are the corrigendum with b762 at its weight and the seat's read of what the ruling misses, the price table and the
ceiling's readings of (3), the dispatch tool's controls and the standing change of (5), the pre-send reads and the outcomes of (6), (7)
and (8) with the statement file of the author's word, the author's words, canon XXV and the trail's lines of (9) with the roster read
after them, the reproduction run of (12), the name and address scan, the touch read of v9 and the standing arms, each row by its bank's
verdict line or by the line its pattern names (section_reading);
(R373)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the commits section;
the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried items for the next
act ((R373)(13)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. SIDE-explicit-formula alone written this act ((R373)(5), (12), N5): each commit by the one-call
tool on a push-b763-* branch made at a named commit, each branch pushed by the gated push's branch mode, each run dispatched by
tools/b763_controls.py and read by its run id from its artifact, the exit file governing; main moved from a branch by the gated push's
default mode after a run's success alone, each tag cut at main's read-back and its peel read back; no kernel branch removed, no other
kernel written, no tag of an earlier act moved, no pin moved.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for the act after b763 ((R373)(13) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R365)(2)(iv)(c): the outbound sentence from the one clause
# ### b763, Component 3 (the Edit tool): the outcomes of (6), (7) and (8) read from their bank at import (data/b763_outcomes.json, written by
# ### tools/b763_outcomes.py) and the ledgers' foot, for the title line, the ferry's ACT line (data/b763_ferry.txt :131) its form, b759's body
# ### its model; the kernel's landings and tags for the kernel lines
_FT5 = lambda n_: ([l_ for l_ in (rd(n_) or '').split(NL) if l_.startswith('### ### **')] or [''])[-1]
_OJ5 = jl('b763_outcomes.json') or {}
_OF5, _OA5 = _OJ5.get('form') or {}, _OJ5.get('arith') or {}
_O85 = [o_ for o_ in (_OJ5.get('orders') or []) if isinstance(o_, dict)]
_LT5 = ([(_OF5.get('tag'), (_OF5.get('peel') or '')[:8])] if (_OF5.get('outcome') or '').startswith('LANDED') else []) + [
    (o_.get('tag'), (o_.get('peel') or '')[:8]) for o_ in _O85 if o_.get('outcome') == 'BUILT IN FULL']
TITLE_LINE = ('b763 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND NINETY, THE CONTROL’S FAILURE FROM ITS COEFFICIENTS: b762 AT ITS WEIGHT; '
              '%s; %s; %s; %s; UNDER (R373).**' % (
                  ('THE FINITE AND SIGNED PARTS OF THE FORM COMPILED AT %s' % _OF5.get('tag')) if _OF5.get('outcome') == 'LANDED, COMPILED' else 'THE FINITE AND SIGNED PARTS OF THE FORM NOT LANDED',
                  'THE STATEMENT OF THE FAILURE COMMITTED AND COMPILED BEFORE ITS PROOF, NO PROOF SENT' if _OA5.get('outcome') == 'STATEMENT COMPILED, NO PROOF SENT'
                  else 'THE STATEMENT OF THE FAILURE NOT COMPILED',
                  ('THE ORDERS PRICED BESIDE IT, %s BUILT' % ' AND '.join(o_.get('order') for o_ in _O85 if o_.get('outcome') == 'BUILT IN FULL'))
                  if any(o_.get('outcome') == 'BUILT IN FULL' for o_ in _O85) else 'THE ORDERS PRICED BESIDE IT, CARRIED WITH THEIR PRICES',
                  'THE AUTHOR’S WORDS ON THE WAITING ORDERS AND ON A STATEMENT’S POSITION ENTERED' if 'WANTED 83, ' in _FT5('b763_ledgers.txt')
                  else 'THE AUTHOR’S WORDS NOT ALL ENTERED'))   # ### the ferry`s ACT line (data/b763_ferry.txt :131) adjusted to what the act did
_K5_MAIN = ('moved to %s' % ' and then to '.join('%s, %s cut at its read-back' % (p_, t_) for t_, p_ in _LT5)) if _LT5 else 'unmoved, no tag cut'
_K5_DEL = 'no kernel branch removed by this act ((R373)(4))'   # ### b763: KERNEL_DELETES empty; this act's push-b763-* branches stay for the next act's step zero
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b762's sections over b762's objects not carried, b763's set at Component 6), headed as CLOSING_SECTIONS names them. A row
    of two reads its bank's verdict line by vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('b762 at its weight, as its closing record`s head line gives it ((R373)(1))', 'b762_closing.txt', r'(?m)^b762 closed: [^\n]*'),
                ('the seat`s read of what the ruling misses, made after the citation check and the deletes ((R373)(3)), its head', 'b763_misses.txt', r'(?m)^b763 -- [^\n]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE PRICE AND THE CEILING ((R373)(3))', [
                ('the price table from banked timings, banked before Component 1, the seat`s own readings printed as the seat`s', 'b763_price.txt'),
                ('the readings against 24 hours at the table`s lower figures, after Component 2 and after Component 3, banked by the committed tool', 'b763_ceiling.txt')]),
            ('THE ROUTE FOR KERNEL WRITES ((R373)(5))', [
                ('tools/standing/ v1.37.2 admitting this act`s branch names in SIDE-explicit-formula, its planted control', 'b763_standing_v1372.txt'),
                ('the dispatch and read tool`s controls, the tool committed before its opening dispatch', 'b763_controls_control.txt')]),
            ('BUILD ONE AND THE STATEMENT FILE ((R373)(6), the author`s word of 2026-11-19)', [
                ('the pre-send reads and the salt check of the statement file`s send at its commit, printed before the send', 'b763_presend_sf.txt'),
                ('the outcomes of (6), (7) and (8), each sentence the ruling`s with its fields filled from its run, and the statement file`s line', 'b763_outcomes.txt')]),
            ('THE CENTRE ((R373)(7))', [
                ('the pre-send reads, the salt check and the control that no zero is used, over the statement`s file, printed before its send', 'b763_presend_s7.txt')]),
            ('THE ORDERS PRICED BESIDE IT ((R373)(8))', [
                ('the pre-send reads and the salt check of SQUARES-AT-24`s send at its commit, printed before the send', 'b763_presend_s24.txt'),
                ('the pre-send reads and the salt check of KEIPER-FACE`s first file at its commit, printed before the send', 'b763_presend_skp.txt'),
                ('IMP2-TAU built as a tool of this act: its controls and its reading of the transcribed principal value', 'b763_imp2tau.txt')]),
            ('THE AUTHOR`S WORDS ((R373)(9))', [
                ('the author`s word [W1], verbatim from the ferry, beside the renderings [A1] to [A12]', 'b763_author_rulings.txt'),
                ('[C1] as canon XXV; the line naming the bank, [A1] to [A12], [B1], [B2] and the build lines under one dated head at OPEN_TRAILS` end, no line moving', 'b763_ledgers.txt'),
                ('the roster read after them by tools/standing/orders.py, its count at PLACE-papers HEAD', 'b763_orders.txt', r'(?m)(?<=^### ### \*\*)ORDERS \d+ ; OPEN \d+ ; CLOSED \d+')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED ((R373)(12), the standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run in the foreground', 'b763_reproduce.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b763_address_scan.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R365)(2)(vi): composed, not carried
    '    SIDE-explicit-formula`s tree alone, as (R373)(5) opens it: main from ' + WL.EF_BASE[:8] + ' ' + _K5_MAIN + ', by the gated push`s default mode after each run`s success, never forced ; ' + ' ; '.join('%s at %s, pushed --scratch and read back, kept for the next act`s step zero' % (b_, t_[:8]) for b_, t_ in (WL.WEIL_BRANCH, WL.ARITH_BRANCH) + tuple(WL.ORDER_BRANCHES)) + ' ; ' + WL.ZQ_TAG[0] + ', v0.39, v0.40 and ' + WL.WEIL_TAG_B759[0] + ' peeling as before ;',
    '    the local main of SIDE-explicit-formula fast-forwarded to each landing by the one-call tool, read back equal ; SIDE-dirichlet-mod-24`s main ' + WL.M24_MAIN + ' and ' + WL.M24_TAG[0] + ' peeling to ' + WL.M24_TAG[2][:8] + ', unmoved, nothing pushed there ;',
    '    the four held branches of SIDE-explicit-formula at their tips, zq-b730 at ' + WL.ZQ_TIP[:8] + ' unmoved ; ' + _K5_DEL + ' ; the rebuild-b721 branches of the wave 1 kernels as b763 found them ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches in SIDE-explicit-formula of the ' + str(WL.MAX_DISPATCHES) + ' the price table`s upper figures allow, each read by its run id from its artifact, the exit file governing (relay data/b763_dispatch_rows.json) ; none in SIDE-dirichlet-mod-24 (' + str(len(WL.M24_RUNS)) + ' rows) ; no pin moved ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each record route, suite part and dispatch ;',
    '    the push-b762-* branches of relay and PLACE-papers deleted at step zero by name, one per message, the --merged listing printed before them as captured shell commands ; N2: the step-zero reads, the chain read and the carry before any write ; tools/standing/ v1.37.2, one version commit with its controls in its bank, before any kernel write ((R373)(5)) ; each act tool committed before its run ; a kernel`s main moved after its run`s success alone ; the (W) regeneration and the pre-lock dry before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: no file under day1/, phase1.5/, phase2/ or internal/ differing from its bytes at 87cab4f2 but the canon, by its appended section XXV ; REGISTRY not written ; OPEN_TRAILS and FINDINGS each a prefix of its new bytes ; each text of the ruling as entered equal to the ruling`s text with its fields filled, and each sentence of (6) and (7) equal to the ruling`s with its fields filled from a run (relay data/b763_ledgers.json, data/b763_outcomes.json) ; (7)`s statement committed and compiled before any line of a proof ; the roster as (9) wants it (relay data/b763_orders.txt) ; no sentence of the act beyond the canon`s section saying that anything of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved ; a sentence about the control naming the side ; the entry`s INTEGRATION line in the form (10) gives ;',
    '    N5: of PLACE-papers and the other private repositories, what rows (6) to (9) of relay data/b754_rules.txt allow, and of the lines of [Q]`s row (3) their path, line and digest ; the reproduction run as (12) orders it ; no identifier of the author in anything the act wrote, committed or pushed, the kernel`s commits and tag messages among them, and no byline (relay data/b763_address_scan.txt, data/b763_address_scan_postlock.txt, data/b763_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no anchor edited ; in OPEN_TRAILS under (9)`s one dated head the line naming the author`s words` bank, [A1] to [A12], [B1], [B2] and the build lines of (6), (7) and (8) and of the author`s word ; no order entered, retired or closed by the seat beyond those lines and the roster`s reading of them ;',
    '    on PLACE-papers main FINDINGS (the corrigendum, the entry), phase1.5/method/THE_METHOD_CANON.md ([C1] as section XXV at its end, no byte above it changing), OPEN_TRAILS ((9)`s block and the trail) ; no other sentence of a paper written or edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b763`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; no rules bank written, data/b754_rules.txt not rewritten ;',
    '    tools/standing/ v1.37.2, one version commit with its controls in its bank (relay data/b763_standing_v1372.txt) ; ' + (('HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay ' + WL.HANDOFF_COMMIT[:8]) if WL.HANDOFF_COMMIT else 'HANDOFF.md not written') + ' ; act_current`s shared_edits as standing/carry.py shared reads them ; the mirror zip and the two ledgers` cuts written outside every repository by tools/mirror_build.ps1 over the',
    '    roster it reads from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R373)(13) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s one question on the act after this one ((R373)(13)), its answer in relay data/b763_author_answers.txt ;',
    '        W-ORD-LI-ARITH carried with its statement compiled and both forms priced (relay data/b763_outcomes.txt, data/b763_price.txt) ; the orders of (8) not built, each carried by name with its price (relay data/b763_ceiling.txt) ; W-ORD-STATEMENT-FILE with its object for the three rows of SIDE-kernel ;',
    '        [A1] to [A12], [B1] and [B2] by their triggers, W-ORD-PREMISE-POSITIONS among them (relay data/b763_ledgers.txt) ; the repairs of (11), each named, for one act of the record`s upkeep (relay data/b763_corrigendum.txt) ; the registration H-ONSET-DENSITY as b762 left it ;',
    '        the items of the seat`s read of what the ruling misses, printed again before the lock (relay data/b763_misses.txt) ; the declarations that compiled with the paper each is an input of (relay data/b763_recut_inputs.txt) ;',
    '        the defects of relay data/b763_defects.txt for the next corrigendum ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; ' + WL.WEIL_BRANCH_B759[0] + ', removed at the kernel`s remote by b760, its local branch on the clone kept at ' + WL.WEIL_BRANCH_B759[1][:8] + ';',
    '        ' + ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (WL.WEIL_BRANCH, WL.ARITH_BRANCH) + tuple(WL.ORDER_BRANCHES)) + ' of SIDE-explicit-formula, this act`s, at the remote and on the clone, for the next act`s step zero;',
    '        push-b757-workflow of SIDE-dirichlet-mod-24, a local branch of its clone, merged into its main at ' + WL.M24_MAIN + '; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b763 found them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written ((R373)(12)), SIDE-explicit-formula alone written ; '
          'SIDE-explicit-formula main %s (' + ', '.join('%s at %s' % (t_, p_) for t_, p_ in _LT5) + (' cut at main`s read-back' if _LT5 else 'unmoved, no tag cut') + '), v0.37 %s, v0.17 %s, v0.38 peeling to ' + WL.ZQ_TAG[2][:12] + ', v0.39, v0.40 and v0.41 as b758 and b759 cut them, '
          + 'the held branches off main, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b763: one standing change, v1.37.2, where (R373)(5) required it (commit.py's KERNEL_ACTS and FF_ACTS admitting b763 at
    # ### SIDE-explicit-formula); its controls in data/b763_standing_v1372.txt
#⟪END⟫
#⟪SECTION record 1⟫
    # ### b763 (R373)(4), (5), (6), (8): SIDE-explicit-formula written on push-b763-* branches, main moved from push-b763-form at v0.42 and
    # ### from an order's branch at each tag of ORDER_TAGS; (7)'s branch holds its statement alone; no kernel branch removed (KERNEL_DELETES
    # ### empty); SIDE-dirichlet-mod-24 untouched, as b759 left it
    print('  kernels read: %d (SIDE-explicit-formula at main %s: %s peeling to %s, cut at main`s read-back after (6)`s run%s; this act`s branches, '
          'none removed: %s, and %s holding (7)`s statement alone; SIDE-dirichlet-mod-24 at main %s with %s peeling to %s, untouched)' % (
              len(ks), K.EF_MAIN[:8], K.WEIL_TAG[0], K.WEIL_TAG[2][:8],
              ''.join('; %s peeling to %s, cut at main`s read-back after (8)`s run' % (t_[0], t_[2][:8]) for t_ in K.ORDER_TAGS),
              ', '.join('%s at %s' % (b_, s_[:8]) for b_, s_ in (K.WEIL_BRANCH,) + tuple(K.ORDER_BRANCHES)),
              '%s at %s' % (K.ARITH_BRANCH[0], K.ARITH_BRANCH[1][:8]), K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8]))
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
    b763's form over b763's objects ((R373)(1)-(13)): the corrigendum's foot and json; the standing version v1.37.2 of (5) by its controls
    bank; the price table and the ceiling's two readings of (3); the dispatch tool's control bank; each send's pre-send reads; the outcomes
    of (6), (7) and (8), their json and the build lines; the dispatch rows and each run's hours; [W1]'s bank; the ledgers of (9), their json's
    two files, roster, build lines and paragraphs by line; the roster at HEAD by tools/standing/orders.py; (12)'s reproduction run; b762's
    scores close; the citation check; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its
    figure, the json banks read whole and refused where they are not the act's; the counter from the act's defects and events banks; nothing
    typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    vs_ = [(v_,) + _bfig(b_.split('/', 1)[1], r'\*\*%s: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*' % re.escape(v_), '%s`s controls' % v_)
           for v_, _c, b_, _n in K.STANDING_BANKS]
    # ### b763, Component 3 (the Edit tool): this section rewritten for b763's own banks, b762's registration, map and page read no more
    # ### (defect (g)'s carried section): the price table and the ceiling's two readings of (3); the dispatch tool's control of (5) beside
    # ### the standing change above; each send's pre-send reads; the outcomes of (6), (7) and (8) with the statement file's line and the
    # ### build lines; the dispatch rows, each run's hours beside its item's price ((10)'s report); [W1]'s bank, the ledgers of (9) and the
    # ### roster at HEAD; (12)'s reproduction run; b762's close; the citation check; the address scan. Each refuses by name where its bank
    # ### does not carry its figure (_bfig, rdn).
    prj_ = jl('%s_price.json' % ACT)
    if not isinstance(prj_, dict) or not prj_.get('rows'):
        sys.exit('### data/%s_price.json DOES NOT CARRY ITS ROWS -- NOTHING COMPOSED' % ACT)
    prow_ = dict((r_['key'], r_) for r_ in prj_['rows'])
    prf_ = _bfig('%s_price.txt' % ACT, r'\*\*THE PRICE TABLE: STEP ZERO ([\d.]+) h ; THE LOWER SUM ([\d.]+) h AGAINST THE CEILING (\d+) h, CARRIED ([^;]+?) ; THE UPPER SUM ([\d.]+) h ;',
                 'the price table`s foot')
    ce_ = _bfig('%s_ceiling.txt' % ACT, r'\*\*THE CEILING: READINGS (\d+) ; THE LAST AFTER (COMPONENT \d) AT (\S+), ([\d.]+) h AT THE LOWER FIGURES AGAINST (\d+) h, '
                r'(NOTHING CARRIED|CARRIED [^;]+?) ; ([^;]+?) ; DISPATCHES (\d+) OF (\d+)\.\*\*', 'the ceiling`s readings')
    cej_ = (jl('%s_ceiling.json' % ACT) or {}).get('readings') or []
    if [r_.get('point') for r_ in cej_] != ['c2', 'c3'] or int(ce_[0]) != 2 or ce_[1] != 'COMPONENT 3':
        sys.exit('### data/%s_ceiling.json DOES NOT CARRY THE TWO READINGS (3) ORDERS, AFTER COMPONENT 2 AND AFTER COMPONENT 3 -- NOTHING COMPOSED' % ACT)
    cc_ = _bfig('%s_controls_control.txt' % ACT, r'\*\*THE TOOL`S CONTROLS: (\d+) OF (\d+) AS WANTED ; ALL AS WANTED\.\*\*', 'the dispatch tool`s control bank')
    PS_ = (r'\*\*THE PRE-SEND READS AT ([0-9a-f]{8}): DUPLICATES (\d+) \(OVER THE TARGETS (\d+)\) ; ANONYMOUS PAIRS (\d+) \(OF (\d+), (\d+) UNREAD\) ; '
           r'REFUSED BY THE FILTER (\d+) \(([^)]*)\), THE TWO KNOWN (YES|NO) ; TARGETS (\d+) MODULES FOR (\d+) NAMES, (\d+) REFUSED, MODULES REFUSED (\d+) ; '
           r'THE SALT CHECK OF SEND (\w+) ([A-Z ]+?) \((\d+) OF (\d+) STATEMENTS\) ;(?: THE NO-ZERO CONTROL ([A-Z ]+?) ;)? CONTROLS (\d+) OF (\d+)\.\*\*')
    ps_ = [(s_,) + _bfig('%s_presend_%s.txt' % (ACT, s_), PS_, 'the pre-send reads of send %s' % s_) for s_ in K.PRESEND_SENDS]
    if any(p_[14] != p_[0] for p_ in ps_):
        sys.exit('### A PRE-SEND BANK NAMES ANOTHER SEND THAN ITS OWN -- NOTHING COMPOSED')
    of_ = _bfig('%s_outcomes.txt' % ACT, r'\*\*THE OUTCOMES: \(6\) ([A-Z, ]+?), STATEMENTS COMPILED (\d+) OF 5 ; THE STATEMENT FILE ([A-Z, ]+?) ; \(7\) ([A-Z, ]+?) ; '
                r'\(8\) (.+?) ; BUILD LINES (\d+) ; CONTROLS (\d+) OF (\d+)\.\*\*', 'the outcomes` foot')
    oj_ = jl('%s_outcomes.json' % ACT)
    xj_ = (jl('%s_xlines.json' % ACT) or {}).get('lines')
    if not isinstance(oj_, dict) or (oj_.get('form') or {}).get('outcome') != of_[0] or (oj_.get('statement_file') or {}).get('outcome') != of_[2] \
            or (oj_.get('arith') or {}).get('outcome') != of_[3] or not isinstance(xj_, list) or len(xj_) != int(of_[5]) \
            or sum(1 for s_ in (oj_['form'].get('statements') or []) if s_.get('compiled')) != int(of_[1]) \
            or any(s_.get('unfilled') for s_ in oj_['form'].get('statements') or []) or (oj_.get('arith') or {}).get('unfilled') \
            or (of_[0] == 'LANDED, COMPILED' and not (oj_['form'].get('tag') == 'v0.42' and oj_['form'].get('peel') and oj_['form'].get('tag_object'))):
        sys.exit('### data/%s_outcomes.json DOES NOT CARRY ITS FOOT`S OUTCOMES, FILLED, WITH v0.42 WHERE (6) LANDED, AND ITS BUILD LINES -- NOTHING COMPOSED' % ACT)
    dr_rows_ = json.loads(rdn('%s_dispatch_rows.json' % ACT)) or []
    # ### each run's hours, its dispatch row's time to its read row's (the run's completion), for (10)'s "what each item took"
    rd_at_ = dict((str(r_.get('run')), r_.get('at')) for r_ in dr_rows_ if r_.get('kind') == 'read')
    runs_ = [(r_.get('item'), int(r_.get('n')), str(r_.get('run')), r_.get('sha', '')[:8], r_.get('at'), rd_at_.get(str(r_.get('run'))),
              (round((calendar_gm(rd_at_[str(r_.get('run'))]) - calendar_gm(r_.get('at'))) / 3600.0, 2) if rd_at_.get(str(r_.get('run'))) else None))
             for r_ in dr_rows_ if r_.get('kind') == 'dispatch' and r_.get('kernel') == 'SIDE-explicit-formula']
    rl_ = _bfig('%s_author_rulings.txt' % ACT, r'\*\*THE AUTHOR`S RULINGS: WORDS (\d+), VERBATIM FROM THE FERRY ; RENDERINGS (\d+), THE NAVIGATOR`S, EACH VERBATIM ; NOTHING CHANGED\.\*\*',
                'the rulings` foot')
    lf_ = _bfig('%s_ledgers.txt' % ACT, r'\*\*THE LEDGERS: FILES (\d+) OF 2 APPENDED, NO LINE MOVING ; \[C1\] AS SECTION XXV ; \[A1\] TO \[A12\], \[B1\], \[B2\] AND (\d+) BUILD LINES ; '
                r'THE ROSTER (\d+) OPEN WITH THE LINES UP TO \[B2\], WANTED (\d+), (\d+) OF (\d+) AS WANTED ; CONTROLS (\d+) OF (\d+) AS WANTED ; WRITTEN\.\*\*', 'the ledgers` foot')
    lj_ = jl('%s_ledgers.json' % ACT)
    ro_ = (lj_.get('roster') or {}) if isinstance(lj_, dict) else {}
    lt_ = rdn('%s_ledgers.txt' % ACT)
    pl_ = re.search(r'(?m)^## THE PARAGRAPHS BY LINE: (.+)$', lt_)
    paras_ = dict((k_.strip(), int(n_)) for k_, n_ in re.findall(r'(?:^|; )([\w ]+?) :(\d+)', pl_.group(1))) if pl_ else {}
    hd_ = re.search(r'(?m)^## THE HEADS: the canon`s section XXV at :(\d+) ; OPEN_TRAILS` first appended line :(\d+)$', lt_)
    want_k_ = ['head', 'W1 line'] + ['A%d' % i_ for i_ in range(1, 13)] + ['B1', 'B2']
    if not isinstance(lj_, dict) or [x_.get('path') for x_ in lj_.get('files') or []] != ['phase1.5/method/THE_METHOD_CANON.md', 'OPEN_TRAILS.md'] \
            or not all(x_.get('prefix') is True for x_ in lj_['files']) or ro_.get('mid_open') != int(lf_[2]) or ro_.get('want') != int(lf_[3]) \
            or len(lj_.get('build_lines') or []) != int(lf_[1]) or [b_[0] for b_ in lj_.get('build_lines') or []] != [x_.get('key') for x_ in xj_] \
            or not hd_ or paras_.get('head') != int(hd_.group(2)) or not all(k_ in paras_ for k_ in want_k_ + [x_.get('key') for x_ in xj_]):
        sys.exit('### data/%s_ledgers.json DOES NOT CARRY ITS FOOT`S TWO FILES, THE ROSTER, THE BUILD LINES AND THE PARAGRAPHS` LINES -- NOTHING COMPOSED' % ACT)
    od_ = _bfig('%s_orders.txt' % ACT, r'(?m)^### ### \*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', 'the roster at HEAD')
    rp_ = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ; (\d+) s\.\*\*', 'the reproduction run`s foot')
    rpj_ = jl('%s_reproduce.json' % ACT)
    rp_notruns_ = [r_.get('id') for r_ in (rpj_ or {}).get('rows') or [] if r_.get('grade') == 'NOT RUN']
    b7c_ = jl('b762_scores_close.json') or {}
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS (\d+) OF (\d+) '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                corr_findings=((co.get('findings') or {}).get('claim'), (co.get('findings') or {}).get('close'), (co.get('findings') or {}).get('repeat')),
                vers=[(v_, c_, int(n_), int(w_)) for v_, c_, n_, w_ in vs_],   # ### b763: the one, v1.37.2, where (R373)(5) required it
                changes=sum(1 for _v, _c, n_, w_ in vs_ if int(n_) == int(w_)),
                pr_rows=prow_, pr_step0=prf_[0], pr_lower=prf_[1], pr_ceiling=int(prf_[2]), pr_carried=prf_[3], pr_upper=prf_[4],
                pr_rate=(prj_.get('rate_lines_h'), prj_.get('h_per_dispatch')),
                ce_n=int(ce_[0]), ce_at=ce_[2], ce_sum=ce_[3], ce_ceiling=int(ce_[4]), ce_word=ce_[5], ce_verdict=ce_[6], ce_disp=(int(ce_[7]), int(ce_[8])),
                ce_readings=[dict(point=r_.get('point'), at=r_.get('at'), spent=r_.get('spent_h'), total=r_.get('total_h'), carried=list(r_.get('carried') or []),
                                  after=r_.get('after_carry_h'), verdict=r_.get('verdict'), used=r_.get('used')) for r_ in cej_],
                ce_proof_left=cej_[0].get('proof_left_h'), ce_left8=cej_[1].get('left_for_8_h'),
                ce_plan=[(p_.get('key'), p_.get('word'), p_.get('hi_h'), p_.get('left_h')) for p_ in cej_[1].get('plan') or []],
                cc_ctl=(int(cc_[0]), int(cc_[1])),
                ps=dict((p_[0], dict(rev=p_[1], dup=int(p_[2]), anon=(int(p_[4]), int(p_[5]), int(p_[6])), refused=int(p_[7]), refused_lines=p_[8], known=p_[9],
                                     modules=int(p_[10]), names=int(p_[11]), names_refused=int(p_[12]), salt=p_[15], salt_n=(int(p_[16]), int(p_[17])),
                                     nozero=p_[18], ctl=(int(p_[19]), int(p_[20])))) for p_ in ps_),
                oc_form=oj_['form'], oc_sf=oj_.get('statement_file') or {}, oc_arith=oj_.get('arith') or {}, oc_orders=list(oj_.get('orders') or []),
                oc_words=(of_[0], of_[2], of_[3], of_[4]), oc_ctl=(int(of_[6]), int(of_[7])), xlines=xj_,
                runs=runs_, disp_ef=len(runs_), read_ef=sum(1 for r_ in dr_rows_ if r_.get('kind') == 'read' and r_.get('kernel') == 'SIDE-explicit-formula'),
                # ### b763, Component 6 (the Edit tool): each run's read row by its id, its verdict and its new names, for the entry's runs and (8)'s orders
                rd_rows=dict((str(r_.get('run')), dict(verdict=r_.get('verdict'), new_n=len(r_.get('new_names') or {}), new_within=bool(r_.get('new_all_within'))))
                             for r_ in dr_rows_ if r_.get('kind') == 'read' and r_.get('kernel') == 'SIDE-explicit-formula'),
                disp_m24=sum(1 for r_ in dr_rows_ if r_.get('kind') == 'dispatch' and r_.get('kernel') == 'SIDE-dirichlet-mod-24'),
                rl_words=int(rl_[0]), rl_renders=int(rl_[1]),
                led_files=[(x_['path'], x_['lines_before'], x_['lines_after'], x_['first_new'], x_.get('sha_before'), x_.get('sha_after')) for x_ in lj_['files']],
                led_xv=int(hd_.group(1)), led_head=int(hd_.group(2)), led_build=int(lf_[1]), led_roster=(ro_.get('before_open'), ro_.get('mid_open'), ro_.get('after_open'), ro_.get('want')),
                led_rows=(int(lf_[4]), int(lf_[5])), led_ctl=(int(lf_[6]), int(lf_[7])), led_lines=paras_, led_moved_after=list(ro_.get('moved_after_b2') or []),
                ord_head=(int(od_[0]), int(od_[1]), int(od_[2])),
                close_word='at its weight' if rdn('b762_closing.txt', optional=True) and b7c_ else 'carried',
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
    """N1 (R373): "no lean process runs on this host; each build is a runner dispatch read by its run id from the artifact, the exit file
    governing; the dispatch counts stay within the price table's upper figures; nothing is fetched from the web; each record route and
    dispatch under the holds." Read (b759's form): no seat command running lean or lake; each dispatch row with one read row of its run, the
    read's exit read; the dispatch counts within the worklist's caps, MAX_DISPATCHES in SIDE-explicit-formula (the price table's upper
    figures, data/b763_price.txt) and 0 in SIDE-dirichlet-mod-24, the worklist's EF_RUNS and M24_RUNS each the runs of its kernel's
    dispatch and read rows; each dispatch under the memory hold (free_mb at or above 2,560 MB) and the disk hold (each volume at or above
    5,000 MB) as its row banks them, each read row carrying free_mb; each dispatch row naming the licence of step zero's banks; the dispatch
    commands in the capture as many as the dispatch rows and the sends refused; no suite part in the background. From the command bank (the
    seat's commands, read live from the capture by the `commands` route), the dispatch rows beside the worklist's runs, and the hook's
    refusal bank (a suite part sent in the background refused BACKGROUND)."""
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
    lic_ = [r for r in _ef_kind(rows_, 'dispatch') if not str((r.get('licence') or {}).get('commit') if isinstance(r.get('licence'), dict) else r.get('licence') or '').startswith(K.STEPZERO_BANKS[:8])]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(_ef_kind(rows_, 'dispatch')) + len(refused_) and runs_ and not twice_ \
        and not free_ and not unexit_ and not lic_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b763_commands.json): %s; dispatch commands in the capture: %s, against the dispatch rows %d and the sends refused by the host (no run) %d; by kernel, dispatches against the worklist`s cap (the price table`s upper figures) and the worklist`s runs each a dispatch row`s and a read row`s: %s; reads %d, a run read twice: %s; each read`s exit file: %s; a read with no exit read: %s; dispatch rows under the memory hold 2,560 MB or the disk hold 5,000 MB, or a row without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b763_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(_ef_kind(rows_, 'dispatch')), len(refused_),
            ', '.join('%s %d of %d, the runs %s' % (k_, n_, c_, o_) for k_, n_, c_, o_ in per_), len(reads_), ', '.join(twice_) or 'none', '; '.join(exits_),
            unexit_ or 'NONE', free_ or 'NONE', K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b763's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line).
# ### The ceiling's (data/b763_ceiling.txt :3 before :13), the outcomes' (:3 before :19), the IMP2-TAU reading's (:6 before :14), each
# ### pre-send bank's (its controls before its salt check) and the ledgers' banks print their controls before their figures; the dispatch
# ### tool's and v1.37.2's controls stand in banks of their own, read by time against the opening dispatch and the first kernel commit. The
# ### author-rulings, orders and corrigendum banks carry no controls section (the rulings copy the ferry, the roster reads, the corrigendum
# ### screens at its landing): each is read by its foot at N3; the reproduction run's planted controls stand per row
N2_CONTROLS = (('data/b763_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b763_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b763_ceiling.txt', '## THE CONTROLS', '## THE READING AFTER COMPONENT 2'),
               ('data/b763_outcomes.txt', '## THE CONTROLS', '## (6) BUILD ONE'),
               ('data/b763_imp2tau.txt', '## THE CONTROLS', '## THE READINGS, T(eps)'),
               ('data/b763_presend_s123.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND s123 '),
               ('data/b763_presend_s4.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND s4 '),
               ('data/b763_presend_s5.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND s5 '),
               ('data/b763_presend_sf.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND sf '),
               ('data/b763_presend_s7.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND s7 '),
               ('data/b763_presend_s24.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND s24 '),
               ('data/b763_presend_skp.txt', '## THE CONTROLS', '## THE SALT CHECK OF SEND skp '),
               ('data/b763_ledgers.txt', '## THE CONTROLS', '## THE ROSTER BY tools/standing/orders.py'),
               ('data/b763_recut_inputs.txt', '## THE CONTROLS', '## THE PAPERS'))
# ### b763: the one standing change of (5), v1.37.2 (relay d34f7323), its controls run after its commit and before the first kernel commit
# ### (ec82fed0, step 16) that its route admits; read by N2's standing clause below
N2_USES = ()
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
N2_SECTIONS = ()
N2_RIDERS = ('data/b763_steps.json', 'data/b763_address_scan_commits.txt')   # ### the step row and the per-commit scan, riding in every commit by the one-call tool


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
    """N2 (R373): "the step-zero reads, the chain read and the carry print before any write, a scratch file among the writes; each tool this
    act writes commits before its run, the tools the carry writes at step zero and the ceiling tool carried from the act before running as
    the standing route runs them; tools/standing/ at the close is tree-equal to tools/standing/ at b762's close unless (5) moved it, in which
    case VERSION moved with it; the kernel's main moves after a run's success and at no other time." Read: the chain read, the step-zero
    reads and the carry by the step-zero bank's times, in that order, before the act_current commit; the act's commits in the worklist's
    TIME_ORDER by time, relay and PLACE-papers together; tools/standing/ moved by (5)'s one commit alone (K.C1_STANDING), its tree at HEAD
    that commit's, VERSION at HEAD K.STANDING_VERSION and moved from b762's close; each tool of K.GENS first added by a commit of its own
    carrying it and not its bank, its commits before the bank's, the bank's commit not the tool; each act tool committed before its first
    run, read from the command bank; SIDE-explicit-formula's main at the peel of the act's last tag, each tag's peel the commit a dispatch
    built whose read reads KERNEL with the exit file 0; each tool's controls before its figures; the (W) regeneration, the pre-lock
    comparison and the probe-path refusal before the lock gate."""
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
    # ### b763: tools/standing/ moved by (5)'s one commit alone (K.C1_STANDING, v1.37.2), its tree at HEAD that commit's, VERSION moved with it
    st_commits_ = [h_ for h_ in g(ROOT, 'log', '--reverse', '--format=%H', '%s..HEAD' % K.PRE_RELAY, '--', 'tools/standing').split() if h_.strip()]
    st_tree_ = (g(ROOT, 'rev-parse', 'HEAD:tools/standing').strip(), g(ROOT, 'rev-parse', '%s:tools/standing' % K.C1_STANDING).strip())
    st_ver_ = (g(ROOT, 'show', 'HEAD:tools/standing/VERSION') or '').strip()
    st_ver0_ = (g(ROOT, 'show', '%s:tools/standing/VERSION' % K.PRE_RELAY) or '').strip()
    standing_ = [h_[:8] for h_ in st_commits_] == [K.C1_STANDING[:8]] and bool(st_tree_[0]) and st_tree_[0] == st_tree_[1] \
        and st_ver_ == K.STANDING_VERSION and bool(st_ver0_) and st_ver0_ != st_ver_ and len(K.STANDING_BANKS) == 1
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
    gen_ = len(gens_ok_) == len(K.GENS) + len(K.GENS_WITH_BANK) == 9 and all(o_ for _n, o_ in gens_ok_)   # ### b763: the nine generator rows of the worklist
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
    # ### b763: the kernel's main moved after a run's success and at no other time -- main at the last tag's peel, each tag's peel a commit a
    # ### dispatch built whose read reads KERNEL with the exit file 0; no kernel branch deleted
    drw_ = jl('%s_dispatch_rows.json' % ACT) or []
    okrun_ = set(str(r_.get('run')) for r_ in _ef_kind(drw_, 'read') if r_.get('verdict') == 'KERNEL' and str(r_.get('build_exit')) == '0')
    built_ = set((r_.get('sha') or '')[:8] for r_ in _ef_kind(drw_, 'dispatch') if str(r_.get('run')) in okrun_)
    tags_ = [K.WEIL_TAG] + list(K.ORDER_TAGS)
    efm_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/main').strip()
    before_kw_ = efm_ == K.EF_MAIN == tags_[-1][2] and all(t_[2][:8] in built_ for t_ in tags_) and not K.KERNEL_DELETES
    # ### the standing commit before the first kernel commit its route admits (relay d34f7323 at 19:53:55Z, SIDE-explicit-formula ec82fed0 at 20:32:07Z)
    anc_ = 0 < ct_(ROOT, K.C1_STANDING) < ct_(K.EF_DIR, K.KERNEL_COMMITS[0][2])
    sect_ = stepzero_ and standing_ and gen_ and before_kw_ and runs_ok_
    route_ = sect_
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT, optional=True)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the chain read, the step-zero reads and the carry printed before any write, in that order (%s, each by the step-zero bank, before the act_current commit %s): %s; tools/standing/ moved by (5)`s one commit %s alone, its tree at HEAD that commit`s (trees %s and %s), the act`s commits under it %s, VERSION %s against %s, moved from %s: %s; SIDE-explicit-formula`s main %s at the last tag`s peel, each tag`s peel a commit a dispatch built whose read reads KERNEL with the exit file 0 (%s; the built commits %s), kernel deletes %d: %s; the standing commit before the first kernel commit: %s; each tool first added by a commit of its own carrying it and not its bank, its commits before the bank`s, the bank`s commit not the tool (%s): %s; each act tool committed before its first run, a dry run of its controls among its runs (tool, its first commit and time, its first run read from the command bank): %s: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; the act`s %d commits in the worklist`s order by time, relay and PLACE-papers together: %s (%s); the tools` controls before their figures: %s' % (
            ', '.join('%s %s' % (n_, ('%sZ' % m_.group(1)) if m_ else 'unread') for n_, m_ in szt_), K.ACT_CURRENT_COMMIT, stepzero_,
            K.C1_STANDING[:8], st_tree_[0][:12] or 'NONE', st_tree_[1][:12] or 'NONE', ' '.join(h_[:8] for h_ in st_commits_) or 'none', st_ver_ or 'unread', K.STANDING_VERSION, st_ver0_ or 'unread', standing_,
            efm_[:8] or 'NONE', ', '.join('%s = %s' % (t_[0], t_[2][:8]) for t_ in tags_), ' '.join(sorted(built_)) or 'none', len(K.KERNEL_DELETES), before_kw_, anc_,
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
N3_GRADED = (('b763_corrigendum.txt', ('ITEMS 70', 'NO WEIGHT LINE', 'THE ENTRY AT FINDINGS :15797')),
             ('b763_price.txt', ('THE PRICE TABLE: STEP ZERO', 'THE UPPER SUM')),
             ('b763_ceiling.txt', ('THE CEILING: READINGS 2', 'THE LAST AFTER COMPONENT 3')),
             ('b763_standing_v1372.txt', ('v1.37.2: CONTROLS', 'ALL AS WANTED')),
             ('b763_controls_control.txt', ('THE TOOL`S CONTROLS: ', 'ALL AS WANTED')),
             ('b763_outcomes.txt', ('THE OUTCOMES: (6) ', 'CONTROLS 12 OF 12')),
             ('b763_author_rulings.txt', ('THE AUTHOR`S RULINGS: WORDS 1', 'NOTHING CHANGED')),
             ('b763_ledgers.txt', ('THE LEDGERS: FILES 2 OF 2 APPENDED, NO LINE MOVING', 'WANTED 83', 'WRITTEN.')),
             ('b763_reproduce.txt', ('ROWS ', 'PLANTED CONTROLS AS WANTED ')),
             ('b763_citation_check.txt', ('### ### **THE CHECK ', '** (halts ')), ('b763_address_scan.txt', ('PREVIOUS ADDRESS',))) \
    + tuple(('b763_presend_%s.txt' % s_, ('THE SALT CHECK OF SEND %s PASSED' % s_, 'CONTROLS 30 OF 30')) for s_ in K.PRESEND_SENDS)
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
N3_BANKS = ('stepzero', 'misses', 'corrigendum', 'price', 'ceiling', 'outcomes', 'ledgers', 'reproduce', 'events', 'defects')
N3_BANKS_OPTIONAL = ('recut_inputs',)
# ### N3 (k), (R373): no figure of the navigator's workspace printed as a banked figure -- the ruling's figures of the navigator's own
# ### reads that no bank of this act computes: the mirror export's MANIFEST md5 the navigator read (SCOPE READ, data/b763_ferry.txt :3,
# ### "opening a4290f9b"); the roster's 83 the ruling's WANTED is computed by this act's own tool (data/b763_ledgers.txt) and is not one.
# ### In the act's own sentences and the entry's, each occurrence wants the navigator named in its sentence
N3_NAV_FIGS = r'\ba4290f9b\b'
# ### b762, N3 (a) to (f): the trees the act may not change but for the page of (6), added; the three files that take appended bytes alone;
# ### the page against BLOCK P; each of the ruling's texts by the file it is entered in -- the trail's twenty-two by the trail tool's digests
# ### (data/b762_ledgers.json entered, sha256 of the filled text, as tools/b762_rulings.py writes them), [G1] and [G2] in REGISTRY, [H] the
# ### registration's bytes, [W1] in the author-rulings bank; the roster as (7) wants it; the registration alone and before the map's tool
N3_TREES = ('day1', 'phase1.5', 'phase2', 'internal')
N3_CANON = 'phase1.5/method/THE_METHOD_CANON.md'   # ### (R373)(9): the one paper this act edits, by an appended section
N3_PREFIXED = ('OPEN_TRAILS.md', 'FINDINGS.md')   # ### (R373) N3: REGISTRY not written, read apart
N3_OT_KEYS = tuple(['A%d' % i_ for i_ in range(1, 13)] + ['B1', 'B2'])   # ### (9)'s lines of OPEN_TRAILS; [C1], [I1], [W1] and the build lines read apart
# ### a hit of the matchers over the act's PLACE-papers writes passes only by a hand verdict pinned here by (path, line, the sentence's
# ### digest (sha256, 16 hex)) -> the verdict, each read before the lock; the words not quoted. b763: none pinned before the scores dry
N3_HAND = {}
N3_CONTROL = r'\b(?:control|Epstein|zq_\w+)\b|x\^2 \+ xy \+ 6y\^2'   # ### a sentence about the control: the control named, the Epstein function, a zq_ name, the form
N3_SIDE_NAMED = r'\b(?:arithmetic|spectral|zero|prime-power) side\b'
import hashlib as _hs   # noqa: E402  ### the notes' digests, sha256 of each line (16 hex), as tools/b757_notes.py writes them; _hs, not _h, which record.tpl :2633 binds to its height formatter (defect (t))


def _side_bad(x):
    """N3 (R367): a sentence about the control that speaks of positivity and names no side of the explicit formula."""
    return bool(re.search(N3_SIDE, x, re.I) and re.search(N3_CONTROL, x) and not re.search(N3_SIDE_NAMED, x))


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
    ls_ = (t or '').replace(chr(13), '').split(NL)
    rows_ = [l_.strip() for l_ in ls_ if ' | ' in l_ and not l_.startswith('### ')]
    return _own_sentences(NL.join(l_ for l_ in ls_ if ' | ' not in l_)) + rows_


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
INTEG_NAMES = ('b763_corrigendum', 'b763_outcomes', 'b763_ceiling', 'b763_price', 'b763_author_rulings', 'b763_ledgers', 'b763_orders')
INTEG_KEYSTONE = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'   # ### (R373)(10): the keystone the rule names


def _integ_line(f):
    """b763, (R373)(10): the entry's last line, bare, "written by this rule and by no reader of the act's banks": `INTEGRATION: cluster <the
    cluster SPIRAL_MAP's table gives THE_EPSTEIN_CONTROL_OBJECT> ; keystone phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md ; stage
    CLUSTERED` where a declaration of (6) or (7) compiled, and stage BANKED where none did. The cluster read from SPIRAL_MAP's cluster table
    at PLACE-papers HEAD (between its '### Clusters' and '### Cross-cluster bridges' heads), the one row whose cells name the keystone, its
    bold name; the canon's form (THE_METHOD_CANON.md :351) read as the line's shape; whether a declaration compiled read from the outcomes
    bank (the form's statements compiled, or (7)'s statement compiled). The reading kept in _INTEG for the record's N3 sentence."""
    if 'line' not in _INTEG:
        sm_ = g(PP, 'show', 'HEAD:SPIRAL_MAP.md').replace(chr(13), '').split(NL)
        a_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Clusters')), None)
        b_ = next((i_ for i_, l_ in enumerate(sm_) if l_.startswith('### Cross-cluster bridges')), None)
        if a_ is None or b_ is None or b_ <= a_:
            sys.exit('### SPIRAL_MAP AT HEAD CARRIES NO CLUSTER TABLE BETWEEN ITS TWO HEADS -- NOTHING COMPOSED')
        rows_ = [(i_ + 1, re.match(r'^\| \*\*([^*]+)\*\*', sm_[i_])) for i_ in range(a_, b_) if '`%s`' % INTEG_KEYSTONE in sm_[i_]]
        rows_ = [(n_, m_.group(1).strip()) for n_, m_ in rows_ if m_]
        if len(rows_) != 1:
            sys.exit('### SPIRAL_MAP`S CLUSTER TABLE: %d ROWS NAMING THE KEYSTONE, NOT ONE -- NOTHING COMPOSED' % len(rows_))
        form_ = g(PP, 'show', 'HEAD:phase1.5/method/THE_METHOD_CANON.md').replace(chr(13), '').split(NL)
        form_ok_ = len(form_) > 351 and all(w_ in form_[350] for w_ in ('INTEGRATION: cluster <', ' ; keystone <', ' ; stage <'))   # ### the form held within :351 (read by predicate, 03:3xZ)
        n6_ = sum(1 for s_ in (f['oc_form'].get('statements') or []) if s_.get('compiled'))
        a7_ = f['oc_arith'].get('outcome') == 'STATEMENT COMPILED, NO PROOF SENT' or str(f['oc_arith'].get('outcome') or '').startswith('PROOF')
        st_ = 'CLUSTERED' if n6_ or a7_ else 'BANKED'
        _INTEG.update(line='INTEGRATION: cluster %s ; keystone %s ; stage %s' % (rows_[0][1], INTEG_KEYSTONE, st_), cluster=rows_[0][1], cluster_line=rows_[0][0],
                      stage=st_, form=form_ok_, why='(6) compiled %d of 5, (7)`s statement %s' % (n6_, 'compiled' if a7_ else 'not compiled'), names=list(INTEG_NAMES))
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
    """N3 (a) to (c), (R373): the files under day1/, phase1.5/, phase2/ and internal/ differing at PLACE-papers HEAD from the act's base
    (K.PRE_PP, 87cab4f2), against the canon alone, its bytes at the base a prefix of its bytes at HEAD (a section appended); REGISTRY's bytes
    at HEAD its bytes at the base (not written); OPEN_TRAILS and FINDINGS each a byte prefix of its bytes at HEAD. Returns (the files
    changed, the canon appended, REGISTRY unwritten, [(file, a prefix)])."""
    ch_ = [p_.strip() for p_ in g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD', '--', *N3_TREES).split(NL) if p_.strip()]
    cb_, ch2_ = _blob(K.PRE_PP, N3_CANON), _blob('HEAD', N3_CANON)
    canon_ = bool(cb_) and ch2_.startswith(cb_) and len(ch2_) > len(cb_)
    rg_ = bool(_blob('HEAD', 'REGISTRY.md')) and _blob(K.PRE_PP, 'REGISTRY.md') == _blob('HEAD', 'REGISTRY.md')
    pre_ = []
    for p_ in N3_PREFIXED:
        b_, h_ = _blob(K.PRE_PP, p_), _blob('HEAD', p_)
        pre_.append((p_, bool(b_) and h_.startswith(b_) and len(h_) > len(b_)))
    return ch_, canon_, rg_, pre_


def _proof_n3(f):
    """N3 (f) and (g), (R373)(7): the statement of (7) committed and compiled before a line of its proof -- its commit on push-b763-arith,
    its run read compiled, and the branch's tip the statement's commit where no proof was sent (no commit after it, so no line of a proof),
    or the proof's commit after the statement's run where one was; and the file that carries the proof passing the control that no zero is
    used, VACUOUS where no proof was written, the statement file's own control read beside it (data/b763_presend_s7.txt). Returns (compiled,
    before, a proof sent, the proof file's control: PASSED | FAILED | VACUOUS, the statement file's control, the statement's commit, the tip)."""
    kc_ = dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS)
    st_, tip_ = kc_.get('arith') or '', K.ARITH_BRANCH[1]
    out_ = str(f['oc_arith'].get('outcome') or '')
    proof_ = out_.startswith('PROOF')
    compiled_ = out_ == 'STATEMENT COMPILED, NO PROOF SENT' or proof_
    before_ = bool(st_) and (tip_.startswith(st_) if not proof_ else bool(f['oc_arith'].get('proof_after_statement')))
    pf_ = (f['ps'].get('s7p') or {}).get('nozero') if proof_ else 'VACUOUS'
    return compiled_, before_, proof_, pf_ or 'UNREAD', f['ps']['s7']['nozero'], st_, tip_[:8]


def _sentences_n3(f, text, conv):
    """N3 (e), (R373)(6) and (7): each sentence of (6) and (7) as entered equal to the ruling's with its fields filled from a run -- each
    compiled statement's sentence and (7)'s, as the outcomes bank composed them from the ferry's text (data/b763_outcomes.json), whole in the
    entry, no field left, and the run id each cites one of the act's dispatch rows. Returns [(key, whole in the entry, filled, its run read)]."""
    runs_ = set(r_ for _i, _n, r_, _s, _a, _b, _h in f['runs'])
    rows_ = []
    for s_ in [s_ for s_ in f['oc_form'].get('statements') or [] if s_.get('compiled')] + ([dict(f['oc_arith'], key='(7)')] if f['oc_arith'].get('sentence') else []):
        t_ = s_.get('sentence') or ''
        rid_ = re.findall(r'\brun (\d{8,})', t_)
        rows_.append((s_.get('key'), bool(t_) and (t_ in text or conv(t_) in text), bool(t_) and not s_.get('unfilled') and not re.search(r'<[a-z][^>]*>', t_),
                      bool(rid_) and all(x_ in runs_ for x_ in rid_)))
    return rows_


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


def _texts_n3():
    """N3 (d), (R373): each text of the ruling as entered equal to the ruling's text with its fields filled -- [A1] to [A12], [B1] and [B2],
    each whole as a line of OPEN_TRAILS at HEAD and by the digest the trail tool banked (data/b763_ledgers.json entered); [C1], <DATE> the
    ledgers' date, whole in the canon at HEAD and by its digest; [I1], its cluster field the corrigendum's reading (data/b763_corrigendum.txt,
    "[I1] CLUSTER ..."), whole in FINDINGS at HEAD; [W1], each of its lines whole, stripped, as a line of the author-rulings bank; and each
    build line ([X1] to [X3] and the statement file's, from data/b763_xlines.json) a line of OPEN_TRAILS at HEAD by the digest the trail tool
    banked, no field left. Returns [(key, file, ok)]."""
    X_ = _ferry_texts()
    lj_ = jl('%s_ledgers.json' % ACT) or {}
    ej_ = lj_.get('entered') or {}
    ot_ = _blob('HEAD', 'OPEN_TRAILS.md').decode('utf-8', 'replace').replace(chr(13), '')
    otl_ = ot_.split(NL)
    cn_ = _blob('HEAD', N3_CANON).decode('utf-8', 'replace').replace(chr(13), '')
    fd_ = _blob('HEAD', 'FINDINGS.md').decode('utf-8', 'replace').replace(chr(13), '')
    rows_ = []
    for k_ in N3_OT_KEYS:
        t_ = X_.get(k_) or ''
        rows_.append((k_, 'OPEN_TRAILS.md', bool(t_) and not re.search(r'<[A-Za-z][^>]*>', t_) and t_ in otl_ and _sha16(t_) == ej_.get(k_)))
    c1_ = (X_.get('C1') or '').replace('<DATE>', str(lj_.get('date') or K.DATE))
    rows_.append(('C1', N3_CANON, bool(c1_) and '<DATE>' not in c1_ and (NL + c1_ + NL) in (NL + cn_ + NL) and _sha16(c1_) == ej_.get('C1')))
    cl_ = re.search(r'\[I1\] CLUSTER ([^;*]+?) ;', rdn('%s_corrigendum.txt' % ACT))
    i1_ = re.sub(r'<the cluster [^>]*>', cl_.group(1).strip(), X_.get('I1') or '') if cl_ else ''
    rows_.append(('I1', 'FINDINGS.md', bool(i1_) and not re.search(r'<the cluster', i1_) and i1_ in fd_))
    aw_ = [l_.strip() for l_ in rdn('%s_author_rulings.txt' % ACT).replace(chr(13), '').split(NL)]
    w_ = [l_.strip() for l_ in (X_.get('W1') or '').split(NL) if l_.strip()]
    rows_.append(('W1', 'data/%s_author_rulings.txt' % ACT, bool(w_) and all(l_ in aw_ for l_ in w_)))
    shas_ = dict((_sha16(l_), l_) for l_ in otl_ if l_.strip())
    for k_, s_, _f, _r in lj_.get('build_lines') or []:
        rows_.append((k_, 'OPEN_TRAILS.md', s_ in shas_ and not re.search(r'<[a-z][^>]*>', shas_[s_])))
    return rows_


def _orders_n3():
    """N3 (h), (R373)(9): after (9) the roster as WANTED -- W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE CLOSED, W-ORD-PREMISE-POSITIONS entered
    OPEN, no other order's status moved, 83 open with the lines up to [B2] -- read from the trail tool's roster in memory before its write,
    each of its rows as wanted (data/b763_ledgers.json roster), and from tools/standing/orders.py's foot at HEAD after it (data/b763_orders.txt),
    its open count the roster's with the build lines beside. Returns (ok, [(row, as wanted)])."""
    ro_ = (jl('%s_ledgers.json' % ACT) or {}).get('roster') or {}
    ft_ = re.search(r'(?m)^### ### \*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', rdn('%s_orders.txt' % ACT))
    rows_ = ro_.get('rows') or []
    ok_ = len(rows_) == 4 and all(r_[-1] is True for r_ in rows_) and ro_.get('mid_open') == ro_.get('want') == 83 \
        and bool(ft_) and int(ft_.group(2)) == ro_.get('after_open')
    return ok_, [(r_[0], r_[-1]) for r_ in rows_]


def _pp_units():
    """N3 (i) and (j) over the act's PLACE-papers writes: the appended text at HEAD of OPEN_TRAILS and of the canon (each from the trail
    json's first_new to lines_after), each line's quoted spans dropped as _own_sentences drops them, each line cut at . ; ? before a space,
    for the centre matcher (outside a negation; the canon's section left out by (i)'s own words, "beyond the canon's section"), the side
    matcher (a line a dated record heads left out, (R368)(9)) and the catalogue matcher (printed); a hit named by path, line and the
    sentence's digest, never by its words, passing only by a hand verdict of N3_HAND. Returns (units read, hits (place, digest, kinds,
    verdict or None), the catalogue's hits by place)."""
    lines_ = []
    for x_ in (jl('%s_ledgers.json' % ACT) or {}).get('files') or []:
        hl_ = _blob('HEAD', x_['path']).decode('utf-8', 'replace').replace(chr(13), '').split(NL)
        lines_ += [(x_['path'], n_, hl_[n_ - 1]) for n_ in range(x_['first_new'], x_['lines_after'] + 1) if 0 < n_ <= len(hl_)]
    units_, hits_, cat_ = 0, [], []
    for p_, n_, l_ in lines_:
        dated_ = _dated_line(l_)
        for x_ in _own_sentences(l_):
            units_ += 1
            kinds_ = [k_ for k_, bad_ in (('centre', p_ != N3_CANON and bool(re.search(N3_LOC, x_)) and not re.search(N3_NEG, x_)),
                                          ('side', not dated_ and _side_bad(x_))) if bad_]
            d_ = _sha16(x_)
            if re.search(N3_CAT, x_):
                cat_.append('%s :%s %s' % (p_, n_, d_))
            if kinds_:
                hits_.append(('%s :%s' % (p_, n_), d_, '+'.join(kinds_), N3_HAND.get((p_, n_, d_))))
    return units_, hits_, cat_
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R373): "no file under day1/, phase1.5/, phase2/ or internal/ differs from its bytes at 87cab4f2, the canon alone changed and by an
    appended section; REGISTRY is not written; OPEN_TRAILS and FINDINGS are each a byte prefix of their new bytes; each text of this ruling
    as entered equals the ruling's text with its fields filled; each sentence of (6) and (7) as entered equals the ruling's with its fields
    filled from a run; the statement of (7) is committed and compiled before a line of its proof; the file that carries its proof passes the
    control that no zero is used; after (9) the roster reads as WANTED; no sentence of the act beyond the canon's section says that anything
    of zeta, RH, GRH or Weil positivity on classK for zeta holds, fails or moved; no sentence about the control speaks of positivity without
    naming the side; no figure of the navigator's workspace is printed as a banked figure." Read: (a) the files changed under the four trees,
    the canon alone, its base bytes a prefix of its new; (b) REGISTRY's bytes at HEAD its bytes at the base; (c) OPEN_TRAILS and FINDINGS each
    a byte prefix; (d) [A1] to [A12], [B1], [B2] by line and by the trail tool's digests, [C1] in the canon, [I1] in FINDINGS, [W1] in its bank,
    each build line by its digest; (e) each compiled statement's sentence and (7)'s whole in the entry, filled, its run read; (f) (7)'s
    statement's commit on its branch, compiled, before any commit of a proof; (g) the proof file's control, VACUOUS where no proof was written,
    the statement file's PASSED beside it; (h) the roster's rows as wanted, 83 open with the lines up to [B2], the foot at HEAD the roster's
    with the build lines; (i) the centre matcher over the act's own sentences -- its banks', the entry's and its PLACE-papers writes' beyond
    the canon's section -- a PLACE-papers hit passing by a pinned hand verdict alone; (j) the side matcher over the same and the canon's
    section; (k) the navigator's figure with no navigator named; each bank's foot carrying its grade; each matcher's control caught; the
    entry's last line (10)'s INTEGRATION line; the banks' nouns in the entry; the root prompt's sentences about the entry the composer's
    ((R373)(13), "composed from the banks"). The novelty and catalogue matchers printed with their yields and graded by no clause of (R373)."""
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
    row_n_ = '  mirror navigator  AS THE NAVIGATOR READ IT: the MANIFEST md5; its head | md5 a4290f9b\n'
    row_x_ = '  mirror  THE EXPORT: the MANIFEST md5; its head | md5 a4290f9b\n'
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
                 nav=_nav_bad('The export`s MANIFEST md5 opens a4290f9b.') and not _nav_bad('The navigator read the MANIFEST md5 opening a4290f9b.')
                 and not _nav_bad('The md5 opens a4290f9bc.'),
                 nav_row=any(_nav_bad(x_) for x_ in _own_sentences(row_n_)) and not any(_nav_bad(x_) for x_ in _nav_units(row_n_))
                 and any(_nav_bad(x_) for x_ in _nav_units(row_x_)))
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    side_ = [x[:80] for x in sents + nsides_ if _side_bad(x)]   # ### (R368)(9): the banks' sentences with the dated records' lines left out; (R373) N3 (j), graded
    cat_ = [x[:80] for x in sents + nsents_ if re.search(N3_CAT, x)]   # ### (R369)'s catalogue clause: printed, graded by no clause of (R373)
    # ### (a) to (c) the trees, REGISTRY and the prefixed files; (d) the ruling's texts; (e) the sentences of (6) and (7); (f), (g) the
    # ### statement before the proof and the control that no zero is used; (h) the roster; (i), (j) the PLACE-papers writes; (k) the navigator
    tr_ch_, canon_ok_, reg_ok_, tr_pre_ = _trees_n3()
    trees_ok_ = tr_ch_ == [N3_CANON] and canon_ok_
    pre_ok_ = len(tr_pre_) == 2 and all(o_ for _p, o_ in tr_pre_)
    tx_rows_ = _texts_n3()
    se_rows_ = _sentences_n3(f, text, conv)
    pf_ = _proof_n3(f)
    pf_ok_ = pf_[0] and pf_[1] and pf_[3] in ('PASSED', 'VACUOUS') and pf_[4] == 'PASSED'
    ord_ok_, ord_rows_ = _orders_n3()
    ppn_, pph_, ppcat_ = _pp_units()
    ppbad_ = [h_ for h_ in pph_ if not h_[3] and 'centre' in h_[2]]
    ppside_ = [h_ for h_ in pph_ if not h_[3] and 'side' in h_[2]]
    navfig_ = [x[:80] for x in navs_ + sents if _nav_bad(x)]
    il_ = _integ_line(f)
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, il_, conv)
    nouns_ = [w_ for w_ in ('data/%s_corrigendum.txt' % ACT, 'data/%s_price.txt' % ACT, 'data/%s_ceiling.txt' % ACT, 'data/%s_outcomes.txt' % ACT,
                            'data/%s_author_rulings.txt' % ACT, 'data/%s_ledgers.txt' % ACT, 'data/%s_orders.txt' % ACT, 'data/%s_reproduce.txt' % ACT,
                            'W-ORD-LI-ARITH', 'W-ORD-STATEMENT-FILE')
              if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT, optional=True) or ''
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    # ### b763: (R373)'s eleven clauses and the carried ones beside them; more_, first_ and cat_ printed, graded by no clause of (R373)
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and not loc_ and not side_ and trees_ok_ and reg_ok_ and pre_ok_ \
        and len(tx_rows_) == len(N3_OT_KEYS) + 3 + f['led_build'] and all(o_ for _k, _p, o_ in tx_rows_) \
        and bool(se_rows_) and all(all(r_[1:]) for r_ in se_rows_) and pf_ok_ and ord_ok_ and not ppbad_ and not ppside_ and not navfig_ \
        and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty sentence and two centre sentences each caught, an Epstein sentence and (7)`s classK sentence passed, (5)`s ruled sentence passed and its words for zeta caught, the catalogue clause caught either way and a sentence of the open order passed, a negation read, a sentence of positivity at the control naming no side caught and one naming the arithmetic side passed, a quotation wrapped over two lines dropped and the text after it kept, a navigator`s price caught where no navigator is named, passed where one is, and a longer number passed, a table row naming the navigator before its semicolon caught by the sentence cut and passed read whole, and a row naming none caught): %s; '
        '(a) the files under day1/, phase1.5/, phase2/ and internal/ differing at PLACE-papers HEAD from the act`s base %s: %s, against the canon alone, its bytes at the base a prefix of its bytes at HEAD (%s): %s; '
        '(b) REGISTRY`s bytes at HEAD its bytes at the base, not written: %s; (c) OPEN_TRAILS and FINDINGS each a byte prefix of its bytes at HEAD: %s: %s; '
        '(d) each text of the ruling as entered equal to the ruling`s text with its fields filled (DATE %s, [I1]`s cluster the corrigendum`s), and each build line by the trail tool`s digest: %s; '
        '(e) each sentence of (6) and (7) as entered whole in the entry, filled, its run among the act`s dispatch rows: %s; '
        '(f) (7)`s statement committed at %s on its branch, its tip %s, compiled %s, before any line of a proof %s, a proof sent %s; (g) the control that no zero is used over the file that carries the proof: %s (the statement file`s own control %s); '
        '(h) the roster after (9) as WANTED, the trail tool`s rows (relay data/%s_ledgers.json) and tools/standing/orders.py`s foot at HEAD (relay data/%s_orders.txt): %s: %s; '
        'over %d of the act`s own sentences in its banks and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation (graded by no clause of (R373)): %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant (graded by no clause of (R373)): %s; (i) a sentence saying zeta, RH, GRH or Weil positivity on classK holds, fails or moved outside a negation: %s; (j) a sentence about the control speaking of positivity with no side named, the lines a dated record heads left out ((R368)(9)): %s; a sentence saying the mechanism catalogue has or has not met the zero ((R369)`s clause, graded by no clause of (R373)): %s, in the PLACE-papers writes %s; '
        'over %d units of the act`s PLACE-papers writes (OPEN_TRAILS` appended text and the canon`s section, the quoted spans dropped, the canon`s section read by no centre matcher by (i)`s words), the hits of the centre and side matchers by place and digest, the words not quoted: %s, of the centre matcher passed by no hand verdict: %s, of the side matcher passed by no hand verdict: %s; '
        '(k) a sentence printing a figure of the navigator`s workspace with no navigator named: %s; the entry`s last line (10)`s INTEGRATION line (%s; %s): %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())),
            K.PRE_PP[:8], tr_ch_ or 'NONE', canon_ok_, trees_ok_,
            reg_ok_, ', '.join('%s %s' % x_ for x_ in tr_pre_), pre_ok_,
            (jl('%s_ledgers.json' % ACT) or {}).get('date'), ', '.join('%s in %s %s' % x_ for x_ in tx_rows_),
            ', '.join('%s whole %s, filled %s, its run read %s' % x_ for x_ in se_rows_) or 'NONE',
            pf_[5][:8], pf_[6], pf_[0], pf_[1], pf_[2], pf_[3] + (' (no file of a proof written, so the clause reads nothing: VACUOUS)' if pf_[3] == 'VACUOUS' else ''), pf_[4],
            ACT, ACT, '; '.join('%s %s' % x_ for x_ in ord_rows_) or 'NONE', ord_ok_,
            len(nsents_), more_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', side_ or 'NONE', cat_ or 'NONE', ppcat_ or 'NONE',
            ppn_, '; '.join('%s %s %s%s' % (p_, d_, k_, (' HAND: %s' % v_) if v_ else '') for p_, d_, k_, v_ in pph_) or 'NONE', ppbad_ or 'NONE', ppside_ or 'NONE',
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
    # ### b763, (R373)(6)-(8), N5: SIDE-explicit-formula's main and tags against b762's face moved by the act's landings alone (b759's form) --
    # ### main at the last tag's peel (v0.42 = 4964e957 after (6), and each tag of an order of (8) built in full, K.ORDER_TAGS), the tags
    # ### b762's face read and each of the act's tags at its peel, no other; the tags containing v0.37 v0.37 to v0.41 and the act's; v0.38
    # ### peeling to 14ca5725 and v0.41 to a3aad4cc
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    _tags5 = [K.WEIL_TAG] + list(K.ORDER_TAGS)
    _new5 = dict((t_[0], t_[2][:7]) for t_ in _tags5)
    _main5 = _tags5[-1][2]
    tag_one = _ef_now[0] == _main5[:7] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **_new5)
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main.startswith(_main5[:8]) and _main5 == K.EF_MAIN \
        and set(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) == set(['v0.37', 'v0.38', 'v0.39', 'v0.40', 'v0.41'] + list(_new5)) \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.41^{commit}').strip().startswith(K.WEIL_TAG_B759[2][:8]) and ch_ok \
        and bool(prev) and tag_one and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main and tags against b762`s face moved by the act`s landings alone ((R373)(6)-(8): main at the last tag`s peel; v0.42 at 4964e957 and each tag of an order of (8) built in full; v0.38 to v0.41 as before; read in full in N5`s kernel clause below), the challenge branch %s at %s with no tag and '
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
    land5_ = [dict(tag=t_[0], peel=t_[2]) for t_ in [K.WEIL_TAG] + list(K.ORDER_TAGS)]
    main5_ = K.EF_MAIN
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
                if kn in own_k_ and (r_[0].startswith('refs/heads/push-b763-')
                                     or (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/main' and bool(land5_) and r_[1].startswith(main5_[:8]))
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
    # ### b763: each tag the act cut, its gated push's capture reading main back at the remote equal to the tag's commit and the tag's peel
    # ### local and remote equal to it (the capture of the branch main moved from: push-b763-form for v0.42, each order's own for its tag)
    br5_ = dict([(K.WEIL_TAG[0], K.WEIL_BRANCH[0])] + [(t_[0], b_[0]) for t_, b_ in zip(K.ORDER_TAGS, [x_ for x_ in K.ORDER_BRANCHES if x_[1] in [y_[2] for y_ in K.ORDER_TAGS]])])
    efl_ = []
    for r_ in land5_:
        c_ = rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, br5_.get(r_.get('tag'), '-')), optional=True) or ''
        rb_ = re.findall(r'(?m)^push_gated: main read back at the remote: ([0-9a-f]{40})$', c_)
        pl_ = re.findall(r'(?m)^push_gated: tag %s peeled local ([0-9a-f]{40}) remote ([0-9a-f]{40})$' % re.escape(r_.get('tag') or '-'), c_)
        loc_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', '%s^{commit}' % (r_.get('tag') or '-')).strip()
        efl_.append((r_.get('tag'), loc_[:8] or 'NONE', bool(loc_) and loc_.startswith((r_.get('peel') or '-')[:8]) and rb_[-1:] == [loc_] and pl_[-1:] == [(loc_, loc_)]))
    ef_new_tags_ = sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--list', 'v0.39*', 'v0.40*', 'v0.41*', 'v0.42*', 'v0.43*', 'v0.44*', 'v0.45*').split() if t_.strip())
    v038_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip()
    v039_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.39^{commit}').strip()
    v040_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.40^{commit}').strip()
    v041_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.41^{commit}').strip()
    v041o_ = g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/v0.41').strip()
    # ### b763, (R373)(4): no kernel branch removed by this act (KERNEL_DELETES empty); b760's removal of push-b759-weil as b760 left it, its
    # ### tracking ref absent in the clone and the clone's own branch kept at its tip; each push-b763-* branch read back at the remote in
    # ### its capture at its tip
    rm_trk_ = [b_ for b_, _t in (K.WEIL_BRANCH_B759,) if g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/%s' % b_).strip()]
    rm_loc_ = [(b_, g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/%s' % b_).strip()[:8] or 'NONE') for b_, _t in (K.WEIL_BRANCH_B759,)]
    ef_rb_ = [(b_, b_ not in rm_trk_ and l_ == t_[:8]) for (b_, t_), (_b, l_) in zip((K.WEIL_BRANCH_B759,), rm_loc_)]
    pushed5_ = [K.WEIL_BRANCH, K.ARITH_BRANCH] + list(K.ORDER_BRANCHES)
    ef_rb_ += [(b_, bool(re.search(r'(?m)^push_gated: branch %s read back at the remote: %s' % (re.escape(b_), t_ or '-'),
                                   rdn('%s_SIDE-explicit-formula_%s_push_out.txt' % (ACT, b_), optional=True) or ''))) for b_, t_ in pushed5_]
    efb_ok = ef_new_tags_ == sorted(['v0.39', 'v0.40', 'v0.41'] + [t_ for t_, _l, _o in efl_]) and all(o_ for _t, _l, o_ in efl_) \
        and v038_.startswith('14ca5725') and v039_.startswith('d1afb4fc') and v040_.startswith('630cba16') \
        and v041_.startswith(K.WEIL_TAG_B759[2][:8]) and v041o_.startswith(K.WEIL_TAG_B759[1][:8]) and not K.KERNEL_DELETES \
        and all(o_ for _b, o_ in ef_rb_)
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
            'the address scan (relay data/b763_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of any '
            'kernel, the act owning none (no push-b763-* branch, no tag, SIDE-explicit-formula`s main at %s unmoved), or a .lean file in a kernel`s tree (%d kernels read): %s; the act`s own refs read: %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; SIDE-dirichlet-mod-24`s tag %s peeling locally to %s, its local main %s: %s; SIDE-explicit-formula: the tags v0.39* to v0.42* %s, v0.38 at %s, v0.39 at %s, v0.40 at %s, v0.41 at %s by its tag object %s; the kernel branches this act removes %s, b760`s removal of %s as b760 left it, its tracking ref absent in the clone and its local branch kept at its tip (%s): %s; '
            'gh repo edit run by a captured command (the carried reader): %s; gh repo edit sent from inside a tool, read by its rows bank (the taught reader, tools/b757_ghcalls.py): %s, none wanted: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (main5_[:8], len(kps_), lean_w or 'NONE', ', '.join(own_r) or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                K.M24_TAG[0], m24_loc_[:8] or 'NONE', m24_main_[:8] or 'NONE', m24_ok,
                ef_new_tags_ or 'NONE', v038_[:8] or 'NONE', v039_[:8] or 'NONE', v040_[:8] or 'NONE', v041_[:8] or 'NONE', v041o_[:8] or 'NONE',
                ', '.join(b_ for b_, _t in K.KERNEL_DELETES) or 'none', K.WEIL_BRANCH[0], ', '.join('%s %s' % x_ for x_ in rm_loc_) + '; tracking refs left %s' % (rm_trk_ or 'NONE'), efb_ok,
                'UNREAD (no command bank)' if gho_ is None else (ghr_ or 'NONE'), '; '.join('tools/%s.py %s' % (s_, v_) for s_, v_ in ghs_.items()) or ('UNREAD (no command bank)' if gho_ is None else 'NONE'), gh_ok,   # ### defect (x): NONE printed unread
                ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b763, Component 3 (the Edit tool): the ruling's ordinal and title (the ferry's ACT line, data/b763_ferry.txt :131) as the act did it,
    # ### read from the banks: data/b763_outcomes.json (the form's outcome and its statements, (7)'s outcome, each (8) order's), the ledgers'
    # ### foot (data/b763_ledgers.txt, THE ROSTER n OPEN ... WANTED 83) and the standing version's bank; the apostrophe typographic, (R368)(3)
    oj_ = jl('%s_outcomes.json' % ACT) or {}
    f_, a_ = oj_.get('form') or {}, oj_.get('arith') or {}
    o8_ = [o_ for o_ in (oj_.get('orders') or []) if o_.get('outcome') == 'BUILT IN FULL']
    lt_ = rdn('%s_ledgers.txt' % ACT)
    m_ = re.search(r'THE ROSTER (\d+) OPEN WITH THE LINES UP TO \[B2\], WANTED (\d+)', lt_)
    return ('### b763 — lane two, act one hundred and ninety, The control’s failure from its coefficients under (R373): b762 at its weight; %s; %s; %s; %s; '
            'tools/standing/ at v1.37.2 for (5)’s route' % (
                'the finite and signed parts of the form compiled at %s' % f_.get('tag') if f_.get('outcome') == 'LANDED, COMPILED'
                and sum(1 for s_ in (f_.get('statements') or []) if s_.get('compiled')) == 5 else 'the finite and signed parts of the form not all compiled',
                'the statement of the control’s failure compiled before its proof, no proof sent' if a_.get('outcome') == 'STATEMENT COMPILED, NO PROOF SENT'
                else 'the statement of the control’s failure not compiled',
                ('%s built, the other orders of (8) priced and carried' % ' and '.join(o_['order'] for o_ in o8_)) if o8_ else 'the orders of (8) priced and carried',
                'the author’s words on the waiting orders and on a statement’s position entered' if m_ and m_.group(1) == m_.group(2) == '83'
                else 'the author’s words not all entered'))
#⟪END⟫
#⟪SECTION record 29⟫
# ### b756: the figures of the title, entry and trail read from the banks' feet (_figs); the guard refuses where the feet disagree with
# ### one another, never on a verdict
# ### b759, before the lock: the guard over (R369)(1)-(11)'s feet


def _guard(f):
    """the composer's refusals before any sentence, where the banks' feet disagree with one another (never on a verdict), b763's: the one
    standing version of (5) with its cases all as wanted; the ceiling's cap equal to the worklist's and its count at the last reading no
    more than the dispatch rows; the dispatch rows each read once; each send's salt check and controls whole, the no-zero control over
    (7)'s send; the outcomes' controls whole; the ledgers' two files, controls and build lines; the roster's counts summing at HEAD; the
    reproduction run's rows summing. A roster otherwise than WANTED is printed and lettered by (9), never refused here."""
    if len(f['vers']) != 1 or f['vers'][0][0] != K.STANDING_VERSION or f['changes'] != 1:
        sys.exit('### THE STANDING VERSION OF (5) DOES NOT STAND ALONE WITH ITS CASES AS WANTED -- NOTHING COMPOSED')
    if f['ce_disp'][1] != K.MAX_DISPATCHES or f['ce_disp'][0] > f['disp_ef'] or f['disp_m24'] != 0 or f['read_ef'] != f['disp_ef']:
        sys.exit('### THE CEILING`S DISPATCHES, OR THE DISPATCH ROWS AND THEIR READS, DISAGREE -- NOTHING COMPOSED')
    if any(p_['salt'] != 'PASSED' or p_['salt_n'][0] != p_['salt_n'][1] or p_['ctl'][0] != p_['ctl'][1] for p_ in f['ps'].values()) \
            or (f['ps'].get('s7') or {}).get('nozero') != 'PASSED':
        sys.exit('### A SEND`S SALT CHECK, ITS CONTROLS OR (7)`S NO-ZERO CONTROL IS NOT WHOLE -- NOTHING COMPOSED')
    if f['oc_ctl'][0] != f['oc_ctl'][1] or f['cc_ctl'][0] != f['cc_ctl'][1]:
        sys.exit('### THE OUTCOMES` OR THE DISPATCH TOOL`S CONTROLS ARE NOT WHOLE -- NOTHING COMPOSED')
    if len(f['led_files']) != 2 or f['led_ctl'][0] != f['led_ctl'][1] or f['led_build'] != len(f['xlines']):
        sys.exit('### THE LEDGERS` FILES, CONTROLS OR BUILD LINES DISAGREE -- NOTHING COMPOSED')
    if f['ord_head'][1] + f['ord_head'][2] != f['ord_head'][0]:
        sys.exit('### THE ROSTER`S COUNTS DO NOT SUM -- NOTHING COMPOSED')
    if f['rp_repro'] + f['rp_differs'] + f['rp_notrun'] != f['rp_rows'] or f['rp_ctl'][0] != f['rp_ctl'][1]:
        sys.exit('### THE REPRODUCTION RUN`S ROWS DO NOT SUM -- NOTHING COMPOSED')
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects (the ferry's ACT line, data/b763_ferry.txt :131, adjusted to what the act did): b762's close at its
    weight (b763_corrigendum); the finite and signed parts of the form and the statement file (b763_outcomes); the statement of the control's
    failure before its proof (b763_outcomes, b763_ceiling); the orders priced beside it (b763_price, b763_outcomes); the author's words and
    canon XXV entered with the roster read after them (b763_author_rulings, b763_ledgers, b763_orders); the dispatches. Each object's name in
    the heading, the act's FINDINGS names for the line reader; every figure from the banks' feet, in digits; the apostrophe typographic and
    no backtick, (R368)(3)'s rule, which tools/standing/titlerule.py refuses at the landing."""
#⟪END⟫
#⟪SECTION record 31⟫
    _guard(f)
    fo_, ar_ = f['oc_form'], f['oc_arith']
    n6_ = sum(1 for s_ in fo_.get('statements') or [] if s_.get('compiled'))
    b8_ = [o_ for o_ in f['oc_orders'] if o_.get('outcome') == 'BUILT IN FULL']
    return ('## The control’s failure from its coefficients under (R373): b762’s close %s (b763_corrigendum); the finite and signed parts of the form %s, '
            '%d statements of 5, and One Page’s 19 rows of this kernel %s (b763_outcomes); the statement of the control’s failure %s (b763_outcomes, b763_ceiling); '
            'the orders priced beside it, %s (b763_price, b763_outcomes); the author’s words on the waiting orders and canon XXV entered, %d open to %d '
            '(b763_author_rulings, b763_ledgers, b763_orders); %d dispatches' % (
                f['close_word'], ('compiled at %s' % fo_.get('tag')) if f['oc_words'][0] == 'LANDED, COMPILED' else 'not landed', n6_,
                'stated and built in one file' if f['oc_words'][1] == 'BUILT' else 'stated, the file not built',
                'committed and compiled before its proof, no proof sent' if f['oc_words'][2] == 'STATEMENT COMPILED, NO PROOF SENT' else 'not compiled',
                ('%s built at %s' % (' and '.join(o_['order'][6:] for o_ in b8_), ' and '.join(o_.get('tag') for o_ in b8_))) if b8_ else 'each carried with its price',
                f['led_roster'][0], f['ord_head'][1], f['disp']))
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
    m_ = re.match(r'^b762 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root \w+…; (\d+) prompts? answered; scores (\d+) of (\d+) HELD; (\d+) defects',
                  rdn('b762_closing.txt').split(NL)[0])
    if not m_:
        sys.exit('### b762`S CLOSING HEAD LINE NOT READ -- NOTHING COMPOSED')
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
    return ('the classes repeating three acts running, by the tags (v9 row (83), each the next act’s opening component, printed for the '
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R373)(8)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b763's objects; b762's composer in git at
    b762's record tool). Its last line this act's own INTEGRATION line, bare, written by (R373)(10)'s rule and by no reader of the act's
    banks (_integ_line)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    _guard(f)
    rep, tot = _repeats()
    # ### b762: b761's closing head line (data/b761_closing.txt :1), the corrigendum's rows, the trail lines' paragraphs by line, the
    # ### report of (10)
    b7h_ = _b7_head()
    cj_ = jl('%s_corrigendum.json' % ACT) or {}
    fr_, nr_ = (cj_.get('findings') or {}).get('rows') or [], (cj_.get('navigator') or {}).get('rows') or []
    if not fr_ or not nr_:
        sys.exit('### THE CORRIGENDUM`S ROWS NOT READ -- NOTHING COMPOSED')
    pl_ = f['led_lines']
    r10h_, r10p_ = _report10()
    # ### b763, Component 3 (the Edit tool): the outcomes, the runs and the prices read once for the paragraphs below
    fo_, ar_, sf_ = f['oc_form'], f['oc_arith'], f['oc_sf']
    st6_ = [s_ for s_ in fo_.get('statements') or [] if s_.get('compiled')]
    true_ = [s_['sentence'] for s_ in st6_] + ([ar_['sentence']] if ar_.get('sentence') else [])
    # ### b763, Component 6 (the Edit tool): a range printed once where its ends are equal ("0 dispatches", "1 dispatch", "0.33 hours")
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    pw_ = lambda k_: '%s over %s' % (rg_(f['pr_rows'][k_]['lo_h'], f['pr_rows'][k_]['hi_h'], 'hours'), rg_(f['pr_rows'][k_]['dispatches'][0], f['pr_rows'][k_]['dispatches'][1], 'dispatches'))
    # ### b763, Component 6 (the Edit tool): each run's state worded for the reader -- the read row's verdict where the run broke or stopped, and what
    # ### compiled where it compiled (the outcomes tool's FORM, FILE and COMPILED)
    sw_ = {'FORM': 'KERNEL, the five statements compiled', 'FILE': 'KERNEL, the five statements and the statement file compiled', 'COMPILED': 'KERNEL'}
    rw_ = lambda it_: '; '.join('dispatch %d, run %s at %s, %s h, %s' % (n_, r_, s_, h_ if h_ is not None else 'not read', (lambda st_: sw_.get(st_) or (
        f['rd_rows'].get(r_) or {}).get('verdict') or st_)(next(
        (x_.get('state') for x_ in (fo_.get('runs') if it_ == 'form' else ar_.get('runs') if it_ == 'arith' else []) or [] if str(x_.get('run')) == r_), 'read')))
        for i_, n_, r_, s_, _a, _b, h_ in f['runs'] if i_ == it_)
    # ### b763, Component 6 (the Edit tool): what each order of (8) not built in full did build, named; the IMP2-TAU reading from its bank's foot
    i2_ = re.search(r'(?m)^### ### \*\*THE IMP2-TAU READING: ([^\n]*?) ; CONTROLS (\d+) OF (\d+) ; ', rdn('%s_imp2tau.txt' % ACT))
    nb8_ = {'W-ORD-KEIPER-FACE': lambda o_: 'its first file, SIDEExplicitFormula/KeiperPolygamma.lean, %d declarations on Mathlib`s digamma -- its analyticity on the right half-plane, its functional equation at every order and N times, its value from its partial sums where the tail tends to 0, the tail a named premise -- compiled on push-b763-keiper at %s, run %s, %s; the order in full needs the Keiper-Taylor identity`s fourth obligation at every index and the bounds on the Stieltjes constants, so main did not move to its branch' % (
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
             'Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from a run (relay data/b763_outcomes.txt); One Page`s 19 rows of '
             'SIDE-explicit-formula stated in one file, each closed by the name that proves it, %s (the author`s word of 2026-11-19); every build a runner dispatch read by its '
             'run id, %d in SIDE-explicit-formula and none elsewhere (relay data/b763_dispatch_rows.json); no lean process on this host.' % (
                 ('built at run %s' % (sf_.get('runs') or ['-'])[-1]) if f['oc_words'][1] == 'BUILT' else 'the file not built', f['disp_ef'])), '',
         '*Filed at b763 on the author’s ruling `(R373)` and the author’s word of 2026-11-19 on the statement file; %d question%s put before the root%s. Banks: relay '
         '`data/b763_misses.txt`, `data/b763_corrigendum.txt`, `data/b763_price.txt`, `data/b763_ceiling.txt`, `data/b763_standing_v1372.txt`, '
         '`data/b763_controls_control.txt`, `data/b763_presend_s123.txt`, `data/b763_presend_s4.txt`, `data/b763_presend_s5.txt`, `data/b763_presend_sf.txt`, '
         '`data/b763_presend_s7.txt`, `data/b763_presend_s24.txt`, `data/b763_presend_skp.txt`, `data/b763_imp2tau.txt`, '
         '`data/b763_dispatch_rows.json`, `data/b763_outcomes.txt`, `data/b763_xlines.json`, the gated push`s captures '
         '`data/b763_SIDE-explicit-formula_push-b763-*_push_out.txt`, `data/b763_author_words_preseal.txt`, `data/b763_author_rulings.txt`, `data/b763_ledgers.txt`, '
         '`data/b763_orders.txt`, `data/b763_reproduce.txt`, `data/b763_recut_inputs.txt`, '
         '`data/b763_author_answers.txt`, `data/b763_events.txt`, `data/b763_defects.txt`, `data/b763_prelock.txt`, `data/b763_pathrefusal.txt`, '
         '`data/b763_address_scan.txt`, `data/b763_touch.txt`, `data/b763_standing_figures.txt`, `data/b763_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b762 at its weight and the corrigendum** ((R373)(1)): b762 closed at relay %s and PLACE-papers %s, suite %s of %s, its scores %d of %s HELD (%s), %s defects, as its closing record`s head line gives it; the relay`s main read back at %s after its closing push (relay data/b762_closing.txt, data/b762_scores_close.json). '
         'The corrigendum, short: b762’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items printed in full; '
         'what the seat found after b762`s lock entered as this act`s events (%s) to (%s) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; the navigator`s own %d entered as the navigator`s, CLAIM, events (%s) to (%s), the fourth corrected by [I1], b762`s integration read from REGISTRY`s row d1-8 with the cluster %s; the repairs of (11) carried, each named, to one act of the record`s upkeep, none made here; at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b763_corrigendum.txt, route %s, banks %s; PLACE-papers %s).' % (
             b7h_.group(1), b7h_.group(2), b7h_.group(3), b7h_.group(4), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', b7h_.group(8), K.PRE_RELAY[:8],
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'],
             fr_[0], fr_[-1], f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], len(nr_), nr_[0], nr_[-1], i1_.group(1) if i1_ else 'unread', f['corr_line'], f['corr_row'],
             K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8]), '',
         '**The route for kernel writes** ((R373)(5)): tools/standing/ %s at relay %s, the one change that admits this act`s branch names: commit.py`s KERNEL_ACTS and FF_ACTS each a row for b763 at SIDE-explicit-formula alone, VERSION moved from v1.37.1, its planted control among %d cases, %d as wanted (relay data/b763_standing_v1372.txt); its first commit refused, the standing dry not staged, and committed with the dry after (relay data/b763_defects.txt (f)). '
         'The dispatch and the read by tools/b763_controls.py, carried from tools/b759_controls.py, each item capped at its upper dispatches in the price table, committed before its opening dispatch, its controls %d of %d (relay data/b763_controls_control.txt); the pre-send reads of (R368)(4) and each send`s salt check by tools/b763_presend.py, committed before its run. '
         'Each kernel commit by the one-call tool with the scan over the staged set, its author and committer the noreply identity; each branch pushed by the gated push`s branch mode and read back; no kernel beyond SIDE-explicit-formula written.' % (
             f['vers'][0][0], K.C1_STANDING[:8], f['vers'][0][2], f['vers'][0][3], f['cc_ctl'][0], f['cc_ctl'][1]), '',
         '**Build one** ((R373)(6)), on push-b763-form made at main %s (v0.41): commit %s, (S1) to (S3) in SIDEExplicitFormula/FormFinite.lean and PoleAutocorrelation.lean, the six names of [P1] and the new names in print_targets.txt; commit %s, (S4) in ParitySplit.lean and (S5) in AdmissibleWeights.lean with the import that run 1 lacked; commit %s, the statement file and its 19 names. '
         'Each send`s salt check printed before it, each statement beside the definitions it rests on, binding no hypothesis beyond its sentence`s: %s (relay data/b763_presend_s123.txt, data/b763_presend_s4.txt, data/b763_presend_s5.txt, data/b763_presend_sf.txt). '
         'The runs: %s. Run 1 broke on three lemma names that Mathlib holds outside its file`s import closure, read in Mathlib`s tree in place of the closure (relay data/b763_defects.txt (i)); run 3 stopped under the runner`s memory hold upstream of the statement file, a reading of the runner, and run 4 built the same commit (relay data/b763_events.txt (52), (53)). '
         'Each statement of (6) compiled: the exit file 0, 0 error lines, each new name`s axioms line within propext, Classical.choice and Quot.sound, no line naming sorryAx. %s The grade read against (6) from each compiled statement before it was written: %s, binding no premise.' % (
             K.EF_BASE[:8], kc_.get('form13', '-')[:8], kc_.get('form45', '-')[:8], kc_.get('statement', '-')[:8],
             '; '.join('%s %s, %d of %d statements' % (s_, f['ps'][s_]['salt'], f['ps'][s_]['salt_n'][0], f['ps'][s_]['salt_n'][1]) for s_ in ('s123', 's4', 's5', 'sf') if s_ in f['ps']),
             rw_('form'),
             ('Main moved from %s to %s by the gated push`s default mode after run %s`s success, never forced; %s cut at main`s read-back, its tag object %s, its peel read back equal at the remote (relay data/b763_SIDE-explicit-formula_push-b763-form_push_out.txt); the kernel`s local main fast-forwarded by the one-call tool, read back equal.' % (
                 K.EF_BASE[:8], (fo_.get('peel') or '')[:8], fo_.get('run'), fo_.get('tag'), (fo_.get('tag_object') or '')[:8])) if f['oc_words'][0] == 'LANDED, COMPILED' else 'Main stands at %s, no tag cut.' % K.EF_BASE[:8],
             ', '.join(sorted(set(s_.get('grade') or '-' for s_ in st6_))) or '-'), '',
         '**The statement file** (the author`s word of 2026-11-19, amending (R372)(8) and (R373)(6) in this one matter; relay data/b763_author_words_preseal.txt :2-:7): SIDEExplicitFormula/OnePageStatement.lean, written on the seat`s defect (j) in the form of the vendored Zeta23/Statement.lean: One Page v2.0`s 19 rows of SIDE-explicit-formula at v0.41, each stated apart from its proof and closed by the name its row cites, the three rows of SIDE-kernel v1.5 named in its header with their file and lines and stated nowhere; its salt check %s, %d of %d; %s. '
         'W-ORD-STATEMENT-FILE CARRIED by the word: its 19 rows of SIDE-explicit-formula closed by the file at %s, its object from here the same file for the three rows in SIDE-kernel, its trigger the next runner build of SIDE-kernel (relay data/b763_outcomes.txt, data/b763_xlines.json).' % (
             f['ps']['sf']['salt'], f['ps']['sf']['salt_n'][0], f['ps']['sf']['salt_n'][1],
             ('built at run %s at %s, the exit file 0, each of its 19 names within the standard three' % ((sf_.get('runs') or ['-'])[-1], kc_.get('statement', '-')[:8])) if f['oc_words'][1] == 'BUILT' else 'not built: %s' % f['oc_words'][1],
             (fo_.get('tag') or kc_.get('statement', '-')[:8])), '',
         '**The centre** ((R373)(7)), on push-b763-arith made at main %s (v0.42): SIDEExplicitFormula/ControlFailureStatement.lean committed at %s before any line of a proof. FORM B, ControlFailureB: a named test function k in classK, the autocorrelation of a cosine-modulated B-spline of order six whose frequency is read from b709`s banked family (relay data/b709_grid.txt :46), vanishing outside [-log 1024, log 1024], at which the real part of poleTerm k - primeTermQ cQ k + archTermQ k is below 0. FORM A, ControlFailureA n: Wide.liCoeff zqZeroConfig n < 0. Each a definition of a Prop with no proof and no sorry. '
         'The control that no zero is used %s over the file: its imports 4, none under Schema/ZQ/OffZero, neither Schema/Detector nor a detector of Schema/Wide, none of the five names; its salt check %s, %d of %d (relay data/b763_presend_s7.txt). The run: %s (relay data/b763_outcomes.txt). '
         'The ceiling after Component 2: spent %s h from the delivery, %s h at the lower figures against 24 h, carried by name %s; what it left for the proof %s h, where FORM B`s upper %s h and FORM A`s %s h each do not fit; so no line of a proof was written, and [X2] is the line (relay data/b763_ceiling.txt).' % (
             (fo_.get('peel') or K.EF_BASE)[:8], kc_.get('arith', '-')[:8], f['ps']['s7']['nozero'], f['ps']['s7']['salt'], f['ps']['s7']['salt_n'][0], f['ps']['s7']['salt_n'][1],
             rw_('arith') + ('; the exit file 0, its ten names within the standard three' if f['oc_words'][2] == 'STATEMENT COMPILED, NO PROOF SENT' else ''),
             c2_['spent'], c2_['total'], ', '.join(k_[4:] for k_ in c2_['carried']) or 'none', f['ce_proof_left'], f['pr_rows']['(7) B']['hi_h'], f['pr_rows']['(7) A']['hi_h']), '',
         '**The orders priced beside it** ((R373)(8)): each priced in the table from its entry and its statements (relay data/b763_price.txt). The ceiling after Component 3: spent %s h from the delivery; left for (8), (9) and the close at their lower figures %s h; in ascending order of upper hours, %s (relay data/b763_ceiling.txt). %s' % (
             c3_['spent'], f['ce_left8'], '; '.join('%s, upper %s h against %s h left, %s' % (k_[4:], h_, l_, w_.lower()) for k_, w_, h_, l_ in f['ce_plan']),
             ' '.join(('%s BUILT IN FULL at %s = %s, run %s, its line [X3] (relay data/b763_outcomes.txt).' % (o_['order'], o_.get('tag'), (o_.get('peel') or '')[:8], o_.get('run')))
                      if o_.get('outcome') == 'BUILT IN FULL' else ('%s not built in full: %s; carried by name with its price, %s, no line written for it.' % (
                          o_['order'], nb8_[o_['order']](o_) if o_['order'] in nb8_ else ('its runs %s' % ', '.join(str(x_.get('run')) for x_ in o_.get('runs') or []) if o_.get('runs') else 'no run sent'),
                          pw_('(8) ' + o_['order'][6:])))
                      for o_ in f['oc_orders']) + ' ' + ' '.join(
                 '%s carried by name with its price, %s%s.' % ('W-ORD-' + k_[4:], pw_(k_), {'(8) IMP2-TAU': (': built as a relay computation of this act and banked -- the transcribed principal value diverges at every test function with f(1) not 0, its step a decade -f(1) ln 10 (read %s at f(1) = 1/2 against -1.1512925465), and each test function the order names is an autocorrelation with f(1) the square of its norm, above 0, so its comparison with -A is not made and no regularization is put in place of CC`s; its controls %s of %s (relay data/b763_imp2tau.txt). Not built in full, and as a relay computation and no kernel build it takes no line [X3], which carries a kernel`s fields' % (
                     (re.search(r'\(TRI (-?[\d.]+)\)', i2_.group(1)) or re.search(r'()', '')).group(1) or 'unread', i2_.group(2), i2_.group(3))) if i2_ else ': its bank`s foot unread',
                                                                                         '(8) BESSEL-BOUND-TIGHTEN': ': its every run computes at zeros, which (12) forbids',
                                                                                         '(8) E2-SEPARATION': ': its test opens a bank of zeros, which (12) forbids'}.get(k_, ''))
                 for k_, w_, _h, _l in f['ce_plan'] if not any(('(8) ' + o_['order'][6:]) == k_ for o_ in f['oc_orders']))), '',
         '**The author’s words** ((R373)(9)): [W1], the author`s word of 2026-11-19 on the form of a statement, banked verbatim from the ferry beside the navigator`s renderings of the author`s words on the orders, %d of them, each verbatim, nothing changed (relay data/b763_author_rulings.txt). '
         'By tools/b763_rulings.py, committed before its run, each file`s bytes at HEAD a prefix of its new bytes, no line moving: THE_METHOD_CANON.md took [C1] as section XXV at :%d, the one paper this act edits; OPEN_TRAILS took, under one dated head at :%d after b762`s trail and before this act`s own, the line naming the bank at :%d, [A1] to [A12] at :%d to :%d, [B1] at :%d and [B2] at :%d, then the build lines %s; controls %d of %d (relay data/b763_ledgers.txt). '
         'The roster by tools/standing/orders.py`s rule: open %d before, %d with the lines up to [B2], wanted %d, the rows %d of %d as wanted; W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE RETIRED by [A11] and [A12], W-ORD-PREMISE-POSITIONS ENTERED by [B2]; %d with the build lines beside, %s; at PLACE-papers HEAD orders %d, open %d, closed %d (relay data/b763_orders.txt). Three orders held as they stand and two keeping their entries’ events took no line.' % (
             f['rl_renders'], f['led_xv'], f['led_head'], pl_['W1 line'], pl_['A1'], pl_['A12'], pl_['B1'], pl_['B2'],
             ', '.join('%s at :%d' % (x_.get('key'), pl_.get(x_.get('key'), 0)) for x_ in f['xlines']) or 'none', f['led_ctl'][0], f['led_ctl'][1],
             f['led_roster'][0], f['led_roster'][1], f['led_roster'][3], f['led_rows'][0], f['led_rows'][1], f['led_roster'][2],
             ('the statuses moving after [B2] ' + ', '.join(f['led_moved_after'])) if f['led_moved_after'] else 'no status moving after [B2]',
             f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
         '**The research instruments reproduced** ((R373)(12), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (%s, as at b762), the planted controls %d of %d as wanted, %d s (relay data/b763_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], ', '.join(str(x_) for x_ in f['rp_notruns']) or 'none', f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The price and the ceiling** ((R373)(3)): the price table banked before Component 1 from 100 banked runs over 18 dispatch-row banks and zq-b730`s rate, %s lines an hour and %s h a dispatch, each item with its lines, its dispatches and its hours, the seat`s own readings printed as the seat`s: the lower sum %s h against %d h at step zero, carried by name %s, the upper sum %s h (relay data/b763_price.txt). '
         'Read again by tools/b763_ceiling.py, committed before its run: after Component 2 at %s, %s h, %s; after Component 3 at %s, %s h, %s; dispatches %d against the worklist`s %d (relay data/b763_ceiling.txt). '
         'The runs took %s h of wall time each against the table`s %s h a dispatch, the runner rebuilding the kernel from source at each dispatch; the table`s figures governed the ceiling as (3) orders, and the report of (10) prints each item beside what it took. The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b763_misses.txt).' % (
             f['pr_rate'][0], f['pr_rate'][1], f['pr_lower'], f['pr_ceiling'], f['pr_carried'], f['pr_upper'],
             c2_['at'], c2_['total'], ('carried ' + ', '.join(k_[4:] for k_ in c2_['carried'])) if c2_['carried'] else 'nothing carried',
             c3_['at'], c3_['total'], ('carried ' + ', '.join(k_[4:] for k_ in c3_['carried'])) if c3_['carried'] else 'nothing carried',
             f['ce_disp'][0], f['ce_disp'][1], ', '.join('%s' % h_ for *_x, h_ in f['runs'] if h_ is not None) or 'none', f['pr_rate'][1]), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b763_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; tools/standing/ moved once, to %s, where (5) required it, VERSION moved with it and its controls banked; each act tool committed before its run, a dry run of its controls among its runs; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after a run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b763_prelock.txt, data/b763_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero')), K.STANDING_VERSION), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula; no push forced; no tag moved, v0.38 to v0.41 and v0.2.0 among them; no pin moved; no sentence of any paper written or edited beyond the canon`s section XXV; REGISTRY not written; no line of a proof of (7) written; nothing computed at a zero and no row of a bank of zeros opened, b709`s banked family read for (7)`s window alone; nothing fetched from the web; no lean process on this host; no byline; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act, the kernel`s commits and tag messages among them, no byline written: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its controls %d of %d as wanted (relay data/b763_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places'], f['addr_ctl'][0], f['addr_ctl'][1]), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b763_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b763 -- %s, %s, %s, %s -- against b762’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b763_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b763_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**The report of (10)**: the hours by the step rows, as relay data/b754_close_yield.txt (A) reads them: %s (the closing comes after this entry and its row is printed in the closing message). '
         'The parts of each pass by the cadence (tools/standing/cadence.py %s), tools/standing/ at %s: %s; the pass after the push runs after this entry, its parts printed in the closing message. '
         'The price table`s figures beside what each item took, by its runs’ dispatch and read rows (relay data/b763_price.txt, data/b763_dispatch_rows.json): %s.' % (
             r10h_, __import__('standing.cadence', fromlist=['VERSION']).VERSION, K.STANDING_VERSION, ' ; '.join(r10p_),
             '; '.join(['(6) priced %s to %s h over %d to %d dispatches, took %d dispatches and %s h of runs' % ((
                 round(sum(r_['lo_h'] for r_ in p6_), 2), round(sum(r_['hi_h'] for r_ in p6_), 2), sum(r_['dispatches'][0] for r_ in p6_), sum(r_['dispatches'][1] for r_ in p6_)) + tk_('form')),
                        '(7)`s statement priced %s, took %d dispatch and %s h of runs' % ((pw_('(7) statements'),) + tk_('arith')),
                        '(7)`s proof priced %s for FORM B and %s for FORM A, took none, no line sent' % (pw_('(7) B'), pw_('(7) A'))]
                       + ['(8) %s priced %s, took %d dispatch%s and %s h of runs' % ((k_[4:], pw_(k_)) + tk_(i_)[:1] + ('' if tk_(i_)[0] == 1 else 'es',) + tk_(i_)[1:])
                          for i_, k_ in ((o_.get('item'), '(8) ' + o_['order'][6:]) for o_ in f['oc_orders']) if tk_(i_)[0]]
                       + ['each other order of (8) priced in the table and taking none'])), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): (S1) makes the prime-power side on a window a finite sum over n up to e^L for any weights, which is what lets FORM B of (7) be stated and proved from finitely many coefficients; (S3) puts the pole term`s sign on the parity of h, negative at an odd window in classK, and (S4) splits each term of the form on the even and the odd part, so the sign of the form at a real test function is read part by part; (S5) makes the weights at which the form stands at or above 0 on each window of a width a convex set fixed by the pole and archimedean terms and decided by finitely many weights, the reading canon XXV gives a width; and the control`s failure is now stated from its coefficients at a named window with no zero in it, compiled before its proof. Each is a statement about the explicit formula`s terms and about the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R373)(13), as the author answers the one question at the root: one act of the record`s upkeep, carrying the repairs of (11), the orders [T8] to [T10] of (R372), [A5] and [A6]; or the act that computes the registration H-ONSET-DENSITY, with W-ORD-ADMISSIBLE-CONE joined to it by [A2]; or the reading of the eighteen named premises under W-ORD-PREMISE-POSITIONS; or another the author names. '
         'W-ORD-LI-ARITH carried with its statement compiled and both forms priced; the orders of (8) not built carried by name with their prices; W-ORD-STATEMENT-FILE with its object the same file for the three rows of SIDE-kernel. Orders open after the act: %d (relay data/b763_orders.txt); the push-b763-* branches of SIDE-explicit-formula kept for the next act`s step zero; the draft held at v5.' % (
             K.NEXT_ACT, f['ord_head'][1]), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b762_rest(f, sc_, sv_, vw_, pc_, ch_, n_ans, n_ref, cc, cw_, cwl_, checks, S, rep, tot):
    """b759's paragraphs over b759's objects, kept for the record and not called (b761, Component 6)."""
    w5_ = f['oc']['weil']
    nl_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_ in f['notes'])
    el_ = '; '.join('%s at PLACE-papers %s, %d line%s' % (f_, c_[:8], n_, '' if n_ == 1 else 's') for _k, f_, c_, n_, _x in f['errata'])
    true5_ = [s_ for s_ in (w5_['sentence'], f['c6_sentence'], f['c8_sentence'], f['c9_sentence']) if s_]
    lp5_ = ('Main moved to the tip %s by the gated push`s default mode after the run`s success, v0.41 cut at main`s read-back (tag object %s) and its peel read back at '
            'the remote equal to main (relay data/b763_SIDE-explicit-formula_push-b763-weil_push_out.txt); the kernel`s local main fast-forwarded to it by the one-call tool, '
            'read back equal.' % (w5_['peel'], w5_['tag_object'])) if f['weil_word'].startswith('LANDED') else 'Main stands at %s, no tag cut.' % K.EF_BASE[:8]
    e = ['', _title(), '',
         ' '.join(true5_) + (
             ' Each sentence is the ruling`s for the outcome the act`s banks read, its fields filled from them (relay data/b763_outcomes.txt, data/b763_c3table.txt, '
             'data/b763_compose.txt, data/b763_corpus.txt); every build a runner dispatch read by its run id, %d in SIDE-explicit-formula of the 3 (5) allows and '
             'none elsewhere (relay data/b763_dispatch_rows.json); no lean process on this host.' % f['disp_ef']), '',
         '*Filed at b763 on the author’s ruling `(R373)`; %d question%s put before the root%s. Banks: relay '
         '`data/b763_misses.txt`, `data/b763_corrigendum.txt`, `data/b763_standing_v1363.txt` to `data/b763_standing_v1367.txt`, `data/b763_presend.txt`, '
         '`data/b763_controls_control.txt`, `data/b763_controls.txt`, `data/b763_dispatch_rows.json`, `data/b763_outcomes.txt`, the gated push`s capture '
         '`data/b763_SIDE-explicit-formula_push-b763-weil_push_out.txt`, `data/b763_c3table.txt`, `data/b763_costlaw.txt`, `data/b763_fields.txt`, '
         '`data/b763_fields_corpus.txt`, `data/b763_compose.txt`, `data/b763_notes.json`, `data/b763_corpus.txt`, `data/b763_errata.json`, `data/b763_reproduce.txt`, '
         '`data/b763_ceiling.txt`, `data/b763_author_answers.txt`, `data/b763_events.txt`, `data/b763_defects.txt`, `data/b763_prelock.txt`, `data/b763_pathrefusal.txt`, '
         '`data/b763_address_scan.txt`, `data/b763_touch.txt`, `data/b763_standing_figures.txt`, `data/b763_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**b762 at its weight and the corrigendum** ((R373)(1)): b762 closed at relay c25f8b53 and PLACE-papers 4ea41948, its scores %d of 8 HELD (%s), as its closing record`s head line gives it (relay data/b762_closing.txt, data/b762_scores_close.json); N4 stays REFUTED on the plant`s repair after its lock and is not argued. '
         'The corrigendum of b762’s %s events and %s defects by count from their banks, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- no CLAIM item among them; '
         'what the seat found after b762`s lock entered as this act`s events (17) to (21) from the seat`s closing message, each with its time, CLAIM %s, CLOSE %s, %s repeats; at FINDINGS :%s, the corrigenda bank appended at row (%s); no weight line (relay data/b763_corrigendum.txt, route %s, banks %s; PLACE-papers %s). The version at the close %s.' % (
             f['b7_held'], ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted',
             f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'],
             f['corr_findings'][0], f['corr_findings'][1], f['corr_findings'][2], f['corr_line'], f['corr_row'], K.C1_RELAY[:8], K.C1_CORR[:8], K.C1_PP[:8], f['ver']), '',
         '**The four standing changes** ((R373)(4)), each a commit of its own moving VERSION, its planted controls printed before its use: (i) the route that removes a named branch at a kernel`s remote, refused for main, for a kept name and for a tip that is no ancestor of the remote`s main, read back absent, %s (relay data/b763_standing_v1363.txt); '
         '(ii) the plant of G-DELETES-ONE-BRANCH reading kept each clause that covers a named ref, (R372) replayed with its clauses (2) and (5) both read, %s (relay data/b763_standing_v1364.txt); '
         '(iii) the row writer taking the phase repair, b762`s repair commit f401a81e replayed, %s (relay data/b763_standing_v1365.txt); '
         '(iv) the suite`s reader of the kernels face naming SIDE-dirichlet-mod-24, made on checks.tpl :663 where the ruling named :611, b762`s face read as 24 kernels, %s (relay data/b763_standing_v1366.txt). '
         'The changes: %d of 4. The kernel route, the one-call tool opened for this act in SIDE-explicit-formula before its first kernel write, a standing change (4) does not name, %s, counted apart (relay data/b763_standing_v1367.txt). '
         'The branches of (3): at the relay and PLACE-papers the five push-b762-* branches by the tool`s route after the merged listing; at the kernels’ remotes %s, each by (i)`s route after its controls, each an ancestor of its remote`s main; each read absent after, one a message (relay data/b763_stepzero.txt, data/b763_events.txt (13), (24)); no clone`s branch removed; push-b763-weil kept for the next act`s step zero.' % (
             vw_('v1.36.3'), vw_('v1.36.4'), vw_('v1.36.5'), vw_('v1.36.6'), f['changes'], vw_('v1.36.7'), ', '.join('%s (was %s)' % (b_, t_[:8]) for b_, t_ in K.KERNEL_DELETES)), '',
         '**The statement and the print lines** ((R373)(5)): push-b763-weil made at main %s; commit one %s, the four lines rQ_one, cQ_eq, detector and h2_sign_iff_rh after print_targets.txt :484, none of them there before; commit two %s, zq_weil_positivity_fails with its docstring in Schema/Wide/HalfScaleControl.lean :37-:51 after zq_arith_side_re_neg, no line above it moved, ComplexOrder opened for it alone, and its line at print_targets.txt :489. '
         'The salt check printed before the send, h2_sign`s body taken into the control`s names under a negation equal to the statement, no binder before its colon: %s; the pre-send reads at %s: duplicates %d; refused by the filter %d (%s), the two known; anonymous pairs %d of %d (%d unread); %d modules for %d names, %d refused; controls %d of %d (relay data/b763_presend.txt). '
         'The dispatch and the read by tools/b763_controls.py, carried from b762`s and set for this act`s one item and its cap, committed before its opening dispatch, its own controls %d of %d (relay data/b763_controls_control.txt); dispatch 1 of 3 at the branch`s tip, run %s: the exit file 0, 0 error lines, %s axioms lines each within the standard three, the five new names among them, no line naming sorryAx (relay data/b763_controls.txt, data/b763_outcomes.txt). '
         'The grade read against the clause from the compiled statement before it was written anywhere: %s, binding no premise. %s' % (
             K.EF_BASE[:8], K.KERNEL_COMMITS[0][2][:8], K.KERNEL_COMMITS[1][2][:8], f['ps_salt'].lower(), f['ps_rev'], f['ps_dup'], f['ps_refused'], f['ps_refused_lines'],
             f['ps_anon'][0], f['ps_anon'][1], f['ps_anon'][2], f['ps_modules'], f['ps_names'], f['ps_names_refused'], f['ps_ctl'][0], f['ps_ctl'][1],
             f['cc_ctl'][0], f['cc_ctl'][1], w5_['run'], w5_['axiom_lines'], w5_['grade'], lp5_), '',
         '**The table of Appendix A** ((R373)(6)), a reproduction and no registered prediction, by tools/b763_c3table.py committed before its run: the plant printed first, the wanted table with beta at (3,2) read -2 reported unequal by each route at that cell and no other, %s; route one, the group-ring model of INSTRUMENTS I-105, %d of %d cells agreeing; route two, the form`s own count at -23 by the recursion of tools/b750_cq_sign.py, the primes 2, 3, 13 and 29 read as wanted and b(n) = c(n)/log n exact at each instance, %d of %d; route three, (a) the closed form of Step 4 for e from 1 to 24, %s, and (b) over every pattern of at most 8 prime factors counted with multiplicity, beta negative at none of the patterns containing none of (4,1), (3,2), (2,1,1) and (1,1,1,1), %s: %s, the law entering as %s (relay data/b763_c3table.txt).' % (
             f['c3_plant'].lower(), f['c3_one'][0], f['c3_one'][1], f['c3_two'][0], f['c3_two'][1], f['c3_a'].lower(), f['c3_b'].lower(), f['c3_word'], f['law_word']), '',
         '**The fields** ((R373)(7)), filled by tools/b763_fields.py from the banks and from no recall: %d filled, then N and DEPOSITS by its corpus route after (9), N %d and DEPOSITS %s; the pin %s, read equal to the run`s built ref; %d AX cells, each the axioms line of its name from the run that printed it, units24_iso_signs from b757`s; BLOCK F`s texts by (5)`s outcome and the law and the appendix by (6)`s; the six module md5s at 14ca5725 agreeing with data/b742_offlinezero.txt :68; HISTORY, v0.1 :3-:19 byte for byte; controls %d of %d and the route`s %d of %d (relay data/b763_fields.txt, data/b763_fields_corpus.txt). '
         'F1 and F2 by tools/b763_costlaw.py committed before its run: F1 = %s beside the quotient of the two banked figures, %s, %s, the sentence %s, its first figure read at data/b744_zetabox_plan.txt :135 where (7) cites :134; F2 = %s, INSTRUMENTS :556 carrying both heights; controls %d of %d (relay data/b763_costlaw.txt).' % (
             f['fd_filled'], f['fc_n'], f['fc_word'].lower(), f['fd_pin'], f['fd_ax'], f['fd_ctl'][0], f['fd_ctl'][1], f['fc_ctl'][0], f['fc_ctl'][1],
             f['cl_f1'], f['cl_quot'], f['cl_agree'].lower(), f['cl_word'].lower(), f['cl_f2'], f['cl_ctl'][0], f['cl_ctl'][1]), '',
         '**The document** ((R373)(8)): phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md composed by tools/b763_compose.py, committed before its run, beside v0.1, which is not edited: %d lines; BLOCK B %d of %d, each OLD once in v0.1 at its line; %d cites read, %d corrected where the name or figure stands once, %d listed where it does not; section 9.9 %s; brackets left %d; the banned stems %s; v0.1 %s, its sha256 equal before and after; controls %d of %d (relay data/b763_compose.txt); one PLACE-papers commit, %s. '
         'Written where else it is by tools/b763_notes.py, each note read back equal and committed alone: %s (relay data/b763_notes.json) -- REGISTRY`s row %s at :%s after 1.5c-23, its status "REVIEW; entered at v0.2 by b763; not deposited", no cell blank and no grade conferred, and a dated note at the file`s end giving v0.41 with its tag object and peel and closing "The tags confer no deposit."; FACES_LEDGER`s and the census`s each made of the document`s own dated head and the sentences of (5) and (8) that came true.' % (
             f['cp_lines'], f['cp_b'][0], f['cp_b'][1], f['cp_cites'], f['cp_corrected'], f['cp_listed'], f['cp_99'].lower(), f['cp_left'], f['cp_stems'].lower(), f['cp_v01'].lower(),
             f['cp_ctl'][0], f['cp_ctl'][1], K.C3_DOC_PP[1][:8], nl_, f['notes_reg'].get('id', '-'), f['notes_reg'].get('row_line', '-')), '',
         '**The corpus lines** ((R373)(9)): the hold on a paper`s sentences lifted for the fourteen lines of BLOCK D alone; each OLD read once at its line and replaced by its NEW by tools/b763_corpus.py, committed before its run, one PLACE-papers commit a document through the one-call tool, each confirmed at HEAD: %s; re-cut %d of %d, left %d, orders %d; REGISTRY`s deposit pins read for the nine documents, one deposited copy, A Place to Stand at REGISTRY :83, not read and not touched, C4 and C5 standing there as deposited; controls %d of %d (relay data/b763_corpus.txt, data/b763_corpus.json).' % (
             '; '.join('%s at %s' % (p_, c_) for p_, c_ in f['corpus_docs']), f['cr_recut'], f['cr_of'], f['cr_left'], f['cr_orders'], f['cr_ctl'][0], f['cr_ctl'][1]), '',
         '**ERRATA and the orders** ((R373)(10)), by tools/b763_errata.py committed before its run, each write read back equal and committed alone: %s (relay data/b763_errata.json) -- ERRATA`s entries %s at the file`s end in the form of E-2026-11-09-1, E-2026-11-06-1 not edited; OPEN_TRAILS’ block under one dated head after b762`s trail, no line moving: b762`s root answer; W-ORD-MECHANISM-ATTRIBUTION`s condition as the navigator read it, not met, T0 and T1 entered beside it and the order left open on the author`s word; the five orders W-ORD-WSC-KERNEL-CITES, W-ORD-LI-INDEX, W-ORD-CAPACITY-ATTRIBUTION, W-ORD-BIBLIOGRAPHY-LINK and W-ORD-EPSTEIN-SECTIONS-3-4 entered by name, each priced by no build; no order of a re-cut left, (9) leaving no line.' % (
             el_, ', '.join(((dict((r_[0], r_[4]) for r_ in f['errata']).get('errata')) or {}).get('entries') or [])), '',
         '**The research instruments reproduced** ((R373)(11), the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py`s full run in the foreground, nothing else writing to tools/ or data/ while it ran: rows %d, reproducing %d, differing %d, not run %d (I-56, I-57, I-61 and I-107, as at b755), the planted controls %d of %d as wanted, %d s (relay data/b763_reproduce.txt).' % (
             f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs']), '',
         '**The ceiling** ((R373)(2)): %d reading%s against 16 hours from the delivery, each before the work of a component began, the last at %s, %s h, %s, dispatches %d of %d (relay data/b763_ceiling.txt). The seat`s read of what the ruling misses printed to the author before Component 1 and once more before the lock (relay data/b763_misses.txt).' % (
             f['ce_n'], '' if f['ce_n'] == 1 else 's', f['ce_at'], f['ce_sum'], f['ce_word'].lower(), f['ce_disp'][0], f['ce_disp'][1]), '',
         '**The order of the act** (N2): the chain read, the step-zero reads and the carry before any write (relay data/b763_stepzero.txt); step zero from %s (data/act_current.json) to its banks at %s; then, by time, %s; each standing change a commit of its own moving VERSION with its controls bank, before its use; each act tool committed before it ran; each kernel commit by the one-call tool, each push by the gated push, SIDE-explicit-formula`s main moved after its run`s success and at no other time; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b763_prelock.txt, data/b763_pathrefusal.txt).' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], '; '.join('%s at %s %s' % (K.CHAIN_WORDS.get(k_, k_), 'PLACE-papers' if k_ in pc_ else 'relay', (pc_.get(k_) or ch_.get(k_) or '-')[:8])
                                                                       for k_ in K.TIME_ORDER if k_ not in ('actcur', 'stepzero'))), '',
         '**What this act is not**: nothing deposits; no Zenodo call; no kernel touched beyond SIDE-explicit-formula`s tree and the five branches of (3); no push forced; no tag moved, v0.38, v0.39, v0.40 and v0.2.0 among them; no toolchain or Mathlib pin moved; no sentence of any paper edited beyond (8)`s new file and (9)`s fourteen lines, v0.1 byte-equal before and after; no ledger row edited; no lean process on this host; the draft held at v5.', '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b763_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b763_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',
         '**The standing arms**: the four figures at b763 -- %s, %s, %s, %s -- against b762’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b763_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, %s, a pass that could not fire (relay data/b763_citation_check.txt%s); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
             ('%s comparative words in %s banks, %s rows' % (cw_.group(2), cw_.group(1), cw_.group(3))) if cw_ else 'its line unread',
             (' :%d' % cwl_) if cwl_ else '', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the control now stands in one document read from its coefficients and from its zeros -- on its arithmetic side the failure of positivity compiled at v0.41 beside the statement it negates, the coefficient law at class number 3 by written proof with its table reproduced by two routes, and the corpus`s sentences about it re-cut to what is proved, compiled and observed; each is a statement about the Epstein zeta function of x^2 + xy + 6y^2, promoting nothing, and none is a finding about zeta.', '',
         '**Carried to:** %s, per (R373)(11), as the author answers the one question at the root: the same re-cut, map before write, for the keystone the author names, Which Structure Confines standing nearest with three of this act`s orders on it; or the class-number-3 law priced for a kernel; or W-ORD-BIBLIOGRAPHY-LINK; or another the author names. W-ORD-MECHANISM-ATTRIBUTION and the five orders of (10) open; push-b763-weil kept; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)


def _finding_text_b762_body():
    """b755's paragraphs over b755's objects, kept for the record and not called (b756, Component 6): held as text, their names b755's
    locals, which the gate's report dry (tools/standing/reportdry.py unbound) read as live unbound globals beside _finding_text's own (defect (j))."""
    return r"""
    e = [
         'The coefficient law at class number 3, H-C3-LAW, read at its registration`s blob (relay data/b753_registrations.txt at `%s`), %s at %d of its %d fields, refuted at %d and not scorable at %d, its control rows -23 and -31 %s and %s, every row read through %d over exact rational arithmetic; the three least split primes the principal form does not represent stood as each row`s at %d of %d, and a cubic of the second route agreed with the form`s own enumeration at %d of %d with %d mismatches (relay data/b763_walk.txt). %s of the navigator`s candidates were reproduced from their statements alone, each by the seat`s generator committed before its run, and %s planted errors each failed as wanted (relay data/b763_candidates.txt). At -59, where no value of the Epstein zeta function had been read before the two rules and the list of roots were committed, the certified list to height %s located %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b763_list_59.txt): H-ZEROS-FROM-PRIMES %s, %d zeros of real part at least 0.85 against %d listed roots%s; H-RECURRENCE %s, S = %d of %d pairs against the largest of %d draws, %d (relay data/b763_zeros_from_primes_59.txt, data/b763_recur_59.txt). No sentence here says why either verdict fell as it did. Nothing was built.' % (
             K.REG_WALK[1], 'held' if f['wk_refuted'] == 0 and f['wk_unscorable'] == 0 else 'read', f['wk_held'], f['wk_of'], f['wk_refuted'], f['wk_unscorable'],
             f['wk_c23'], f['wk_c31'], f['wk_bound'], f['wk_primes'][0], f['wk_primes'][1], f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'],
             num_word(f['cd_rep']).capitalize(), num_word(f['cd_plants']), f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_draws'], f['rc_max']), '',
         '*Filed at b763 on the author’s ruling `(R373)` and its two amendment rows (relay data/b763_amendments.json); %d question%s put before the root%s. Banks: relay '
         '`data/b763_corrigendum.txt`, `data/b763_carried_faults.txt`, `data/b763_standing_v1346.txt`, `data/b763_walk.txt`, `data/b763_coeffs_controls.json`, `data/b763_literature.txt`, '
         '`data/b763_cand_a.txt` to `data/b763_cand_l_plant.txt`, `data/b763_candidates.txt`, `data/b763_ceiling.txt`, `data/b763_registrations.txt`, `data/b763_roots_59.txt`, '
         '`data/b763_list_59.txt`, `data/b763_list_59_controls.txt`, `data/b763_zeros_from_primes_59.txt`, `data/b763_recur_59.txt`, `data/b763_recur_control.txt`, '
         '`data/b763_census_from_primes.txt`, `data/b763_l16.json`, `data/b763_put_1.json`, `data/b763_put_2.json`, `data/b763_author_answers.txt`, `data/b763_events.txt`, '
         '`data/b763_defects.txt`, `data/b763_prelock.txt`, `data/b763_pathrefusal.txt`, `data/b763_reproduce.txt`, `data/b763_address_scan.txt`, `data/b763_touch.txt`, '
         '`data/b763_standing_figures.txt`, `data/b763_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The weight, the corrigendum and the standing change** ((R373)(1), (2); relay %s, %s, PLACE-papers %s): b762 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b762’s %s events, %s post-seal events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- its %s CLAIM items in full, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b763_corrigendum.txt). Its three repairs: the lock gate carried as tools/b763_lockgate.py at relay %s, reading the handoff census`s STOPPED line as that gate`s pass; '
         'no post-seal events bank at this act, what the seat finds after the lock printed with its times in the closing message; the mirror`s folder named by role, by one standing change -- tools/standing/ to %s at relay %s, VERSION moved with it and its controls %d of %d as wanted, the one-call tool`s act phases gaining components 5 and 6 inside it on the author`s answer (relay data/b763_standing_v1346.txt; the amendment row 1). '
         'The open items of b762`s closing message banked as its carried faults, %d rows from %d items, none repaired here (relay data/b763_carried_faults.txt). The version at the close %s.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], ps_, f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], co_.get('claim', '-'), f['corr_line'], f['corr_row'], K.C1_LOCKGATE[:8], v_, K.C1_STANDING[:8], vw_, vn_,
             f['cf_rows'], f['cf_items'], f['ver']), '',
         '**The walk** ((R373)(3)): the registration read at its blob (relay data/b753_registrations.txt at `%s`: the rule :14-:16, the table :29-:46, the falsifier :54) and not from the ruling; the generator tools/b763_coeffs.py, carried from tools/b722_coeffs.py with the three changes the ruling orders, committed at relay %s before its run; its controls printed before any row (relay data/b763_coeffs_controls.json); the fourteen rows each on the falsifier, %d HELD, %d REFUTED, %d NOT SCORABLE; the control rows -23 %s and -31 %s; the three primes as the row`s at %d of %d; a monic cubic of the second route at %d of %d fields, its primes below 20,000 against the form`s with %d mismatches; the group-ring model`s reading, FORCED and no test, agreeing at %d of %d; through %d in %d s (relay data/b763_walk.txt at %s). The sixteen fields read are all the fields of class number 3 by Watkins`s Table 4, read at content (relay data/b763_literature.txt T8.b, R9).' % (
             K.REG_WALK[1], K.C2_PLAN_FIRST[:8], f['wk_held'], f['wk_refuted'], f['wk_unscorable'], f['wk_c23'], f['wk_c31'], f['wk_primes'][0], f['wk_primes'][1],
             f['wk_cubic'][0], f['wk_cubic'][1], f['wk_mism'], f['wk_model'][0], f['wk_model'][1], f['wk_bound'], f['wk_secs'], K.C2_RELAY[:8]), '',
         '**The prior clause and the literature bank** ((R373)(5)(i)): %d queries sent and their fetches printed, %d sources read at content (%s) with each sentence taken at its line and page, %d rows not read (%s), the ruling`s figures and attributions read against the print in the R-rows (relay data/b763_literature.txt at %s); the prior clause banked with the candidates at relay %s, before either rule (relay data/b763_registrations.txt (1)).' % (
             f['lt_queries'], f['lt_content'], f['lt_content_rows'], f['lt_notread'], f['lt_notread_rows'], K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8]), '',
         '**The candidates** ((R373)(4)): %s reproduced (%s), each by the seat`s own generator from its statement alone, committed before its run, its figures printed beside the navigator`s where the navigator kept an output, then run once more with its planted error: %s plants, each failing as wanted, (c)`s first plant run defective and made again by the repaired generator (relay data/b763_defects.txt (k)); (b) and (d) cited and not run, (e) forced, (f) checked line by line and priced, (g) no test. Each row carries its sourcing line under (S1) and the prior work the ruling names, at content or NOT READ: (h) a zero as a point where a ratio of two L-functions takes a fixed value, Lee, and the alignment of the small primes’ phases, Bombieri and Ghosh; (j) the form of the equation, Bombieri and Ghosh`s Theorem 7; (k) classical genus theory, NOT READ; (l) almost-periods from rational approximations to ratios of logarithms of primes, van de Lune and te Riele (relay data/b763_candidates.txt, data/b763_cand_a.txt to data/b763_cand_l_plant.txt). The navigator`s figures stand beside the act`s and in no bank.' % (
             num_word(f['cd_rep']).capitalize(), f['cd_labels'], num_word(f['cd_plants'])), '',
         '**The two rules and their test** ((R373)(5)(ii), (iii)): each rule committed alone, H-ZEROS-FROM-PRIMES at relay %s and H-RECURRENCE at %s with its null`s generator and seed %d; the list of roots at -59 committed at %s before any tool read a value of the function there, %d roots to height %s, %d of real part at least 0.85 and %d in [0.83, 0.85) (relay data/b763_roots_59.txt); the certified engine at %s, its own controls run after the list of roots was committed and before any band, %s (relay data/b763_list_59_controls.txt); then the list band by band in the foreground, %d bands, %d complete, to height %s: %d zeros on the line and %d off-line pairs, the largest real part among them %s (relay data/b763_list_59.txt at %s). '
         'H-ZEROS-FROM-PRIMES read against its rule: %s, %d zeros of real part at least 0.85 against %d roots%s; the zero and the root with real part in [0.83, 0.85), which the rule lets serve as partners and asks none of, printed beside it (relay data/b763_zeros_from_primes_59.txt, data/b763_events.txt (16)). '
         'H-RECURRENCE read against its rule: %s, S = %d of %d pairs over %d heights against the null`s %d draws of as many heights, mean %s, largest %d, seed %d (relay data/b763_recur_59.txt); its control at -23, (4)(l) by the same tool, S = %d against the null`s largest %d, as wanted (relay data/b763_recur_control.txt). Neither verdict reads anything written after its rule.' % (
             K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], f['rc_seed'], K.C4_ROOTS[:8], f['rt_all'], f['rt_height'], f['rt_high'], f['rt_band'], K.C4_ENGINE[:8], f['ls_ctl'],
             f['ls_bands'], f['ls_complete'], f['ls_height'], f['ls_online'], f['ls_offline'], f['ls_maxre'], K.C4_LIST[:8],
             f['zf_verdict'], f['zf_zeros'], f['zf_roots'], vac_, f['rc_verdict'], f['rc_s'], f['rc_pairs'], f['rc_heights'], f['rc_draws'], f['rc_mean'], f['rc_max'], f['rc_seed'],
             f['rcc_s'], f['rcc_max']), '',
         '**After both verdicts, exploratory and marked so** ((R373)(6)): at -23 to height %s the route`s roots of real part at least 0.85 at P = 3 x 10^5: %d; the least height of a root with real part above 1: %s; its control to %d, the roots against the banked off-line zeros, %s, printed after the figures (relay data/b763_defects.txt (l)); its generator committed at relay %s before its run (relay data/b763_census_from_primes.txt at %s). Nothing in it is read as held or refuted.' % (
             f['cs_height'], f['cs_count'], f['cs_least'], f['cs_ctl_to'], f['cs_ctl'].lower(), K.C5_GEN[:8], K.C5_RELAY[:8]), '',
         '**The line of (7)** ((R373)(7)): [L16] appended at OPEN_TRAILS’ end under a dated head before this act’s own trail, by its generator committed at relay %s before its run, %s; the file`s lines %s before and %s after (relay data/b763_l16.json).' % (
             K.L16_GEN[:8], f['l16_confirm'], f['l16_counts'][0], f['l16_counts'][1]), '',
         '**The price and the ceiling** ((R373)(8)): the price table at step zero from banked timings where a bank held one (relay data/b763_stepzero.txt); the ceiling read again after Component 3, the lower sum %s h against %d h: %s (relay data/b763_ceiling.txt at %s).' % (
             f['ce_lower'], f['ce_ceiling'], f['ce_word'].lower(), K.C1_CEILING[:8]), '',
         '**The order of the act** (N2): the step-zero reads, the chain read and the carry before any write (relay data/b763_stepzero.txt); step zero from %s (data/act_current.json) through b762`s carried files to its banks at %s; tools/standing/ v1.34.6 at %s, before the gate; the lock gate carried at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the walk`s generator at %s and its bank at %s; the literature at %s; each candidate`s generator before its bank; the candidates with the prior clause at %s; the ceiling at %s; the two rules at %s and %s; the roots at %s; the engine at %s; the list and the two verdicts at %s; the census`s generator at %s and its bank at %s; [L16]’s generator at %s and its write at PLACE-papers %s; the per-commit scan to its own bank at every commit; the pre-lock comparison and the probe-path refusal printed before the lock gate (relay data/b763_prelock.txt, data/b763_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.ACT_CURRENT_COMMIT[:8], K.STEPZERO_BANKS[:8], K.C1_STANDING[:8], K.C1_LOCKGATE[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST[:8], K.C2_RELAY[:8],
             K.C3_LITERATURE[:8], K.C3_CANDIDATES[:8], K.C1_CEILING[:8], K.C4_RULE_ZEROS[:8], K.C4_RULE_RECUR[:8], K.C4_ROOTS[:8], K.C4_ENGINE[:8], K.C4_LIST[:8],
             K.C5_GEN[:8], K.C5_RELAY[:8], K.L16_GEN[:8], K.L16_PP[:8]), '',
         '**What this act is not**: nothing built; nothing deposits; no Zenodo call; no kernel touched, no kernel branch merged, created, moved or deleted, no tag, no Lean file written, no dispatch; no README, description or anchor edited; no ledger row edited beyond the weight line, the corrigendum, this entry, the trail and (7)`s line; no order entered; data/b753_registrations.txt not written again; nothing computed at a field of class number 3 beyond what (3) and (5) order; the draft held at v5.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b763_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b763_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b763_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s. %s' % (f['claim'], f['close'], rep, tot,
                                                                                                        _runs3_line(), __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b760: [U3] in force, the counter's line as it prints (its event in data/b760_events.txt (22))
         '**The standing arms**: the four figures at b763 -- %s, %s, %s, %s -- against b762’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b763_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked, %s OK, %s missed, each printed; the comparative read vacuous, a pass that could not fire (relay data/b763_citation_check.txt, data/b763_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the walk and the two rules read the same three primes two ways: at the fourteen fields chosen before any was computed they set the index at which the logarithmic derivative turns negative at %d of the %d registered rows, and at -59 the rule on the zeros far from the line read %s with %d zeros against %d roots at its threshold%s, and the recurrence of their heights the two least of those primes predict read %s; the candidates and the literature bank credit each equation used to its print; none is a finding about zeta.' % (
             f['wk_held'], f['wk_of'], f['zf_verdict'], f['zf_zeros'], f['zf_roots'], (', vacuous there' if vac_ else ''), f['rc_verdict']), '',
         '**Carried to:** %s, per (R373)(8), as the author answers the one question at the root: the clearing act as b763 (the twelve work-orders the triage of b724 read as ready; the tool changes of [U1] and [U2]; the README route with [B1] and [B3]; [H1]’s held part; the carried faults of (2); closing lines for checkpoints CP-6 and CP-7), or the build of T0 and T1 as b763 with the clearing act after it; defects (b), (e) and the tools’ (d) open for the author; the instruments NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or fails, that Weil positivity on classK holds or fails for zeta, or about the zeros of zeta.*', '',
         _integ_line(f), '']
    return _title(), NL.join(e)
"""


def _finding_text_b762():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b763's objects): the writes; b762 at its weight; the route of (5); build one of (6) and the statement file;
    the centre of (7); the orders of (8); the author's words of (9); the dispatches; the reproduction run; the ceiling; the report of (10);
    the open-orders line from tools/standing/orders.py's output over the trail at HEAD; the standing version v1.37.2; the kernels."""
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
    pl_ = f['led_lines']
    fo_, ar_ = f['oc_form'], f['oc_arith']
    b8_ = [o_ for o_ in f['oc_orders'] if o_.get('outcome') == 'BUILT IN FULL']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R373) ratified.** Its components as the ferry orders them (relay data/b763_ferry.txt), each read below from its bank; the author`s word of 2026-11-19 on W-ORD-STATEMENT-FILE amending (R372)(8) and (R373)(6) in that one matter (relay data/b763_author_words_preseal.txt).', '',
             '**Entered:** FINDINGS.md:%s (the corrigendum for b762), :%s (the entry); phase1.5/method/THE_METHOD_CANON.md:%s ([C1], section XXV); OPEN_TRAILS.md:%s under the dated head of (9), the build lines after its texts; this record.' % (
                 f['corr_line'], fj.get('entry_line'), f['led_xv'], f['led_head']), '',
             '**b762 at its weight** ((R373)(1)): closed at relay %s and PLACE-papers %s, the scores %d of %s HELD (%s); the corrigendum short at FINDINGS :%s, b762`s %s CLAIM items printed in full, the findings after its lock entered as events, the navigator`s own entered CLAIM, [I1] in it, no weight line (relay data/b762_scores_close.json, data/b763_corrigendum.txt).' % (
                 b7h_.group(1), b7h_.group(2), f['b7_held'], b7h_.group(7), ', '.join('%s REFUTED' % k_ for k_ in f['b7_refuted']) or 'none refuted', f['corr_line'], f['corr_claim']), '',
             '**The route** ((R373)(5)): tools/standing/ %s, its cases %d of %d as wanted; the dispatch tool`s controls %d of %d (relay data/b763_standing_v1372.txt, data/b763_controls_control.txt).' % (
                 f['vers'][0][0], f['vers'][0][3], f['vers'][0][2], f['cc_ctl'][0], f['cc_ctl'][1]), '',
             '**Build one** ((R373)(6)): %s, statements compiled %d of 5, %s, run %s, the grade DERIVES; the statement file %s by the author`s word (relay data/b763_outcomes.txt).' % (
                 f['oc_words'][0].lower(), sum(1 for s_ in fo_.get('statements') or [] if s_.get('compiled')),
                 ('%s = %s' % (fo_.get('tag'), (fo_.get('peel') or '')[:8])) if f['oc_words'][0] == 'LANDED, COMPILED' else 'no tag cut', fo_.get('run'), f['oc_words'][1].lower()), '',
             '**The centre** ((R373)(7)): %s, run %s at %s; the no-zero control %s; FORM A priced at %s and FORM B at %s, neither fitting the %s h the ceiling left; [X2] (relay data/b763_outcomes.txt, data/b763_ceiling.txt).' % (
                 f['oc_words'][2].lower(), ar_.get('run'), (ar_.get('sha') or '')[:8], f['ps']['s7']['nozero'].lower(), (ar_.get('prices') or {}).get('A', '-'), (ar_.get('prices') or {}).get('B', '-'), f['ce_proof_left']), '',
             '**The orders priced beside it** ((R373)(8)): %s; %s%s; W-ORD-IMP2-TAU built as a relay computation, the transcribed principal value diverging at each test function the order names and its comparison with -A not made, carried; the others carried by name with their prices, no line written for any order not built in full (relay data/b763_ceiling.txt, data/b763_outcomes.txt, data/b763_imp2tau.txt).' % (
                 '; '.join('%s %s' % (k_[4:], w_.lower()) for k_, w_, _h, _l in f['ce_plan']),
                 ('built in full ' + ', '.join('%s at %s = %s, run %s' % (o_['order'], o_.get('tag'), (o_.get('peel') or '')[:8], o_.get('run')) for o_ in b8_)) if b8_ else 'none built, each carried by name with its price',
                 # ### b763, Component 6 (the Edit tool): each order of (8) begun on a branch and not built in full, by what compiled
                 ''.join('; %s not built in full, its first file compiled on its branch at %s, run %s, carried' % (
                     o_['order'], dict((k_, c_) for k_, _r, c_, _b in K.KERNEL_COMMITS).get(o_.get('item'), '-')[:8], ', '.join(str(x_.get('run')) for x_ in o_.get('runs') or []))
                         for o_ in f['oc_orders'] if o_.get('outcome') != 'BUILT IN FULL' and o_.get('runs'))), '',
             '**The author`s words** ((R373)(9)): [W1] banked verbatim beside %d renderings; [C1] as canon XXV at :%d; the bank line, [A1] to [A12], [B1], [B2] and %d build lines from OPEN_TRAILS :%d; the roster %d open before, %d with the lines up to [B2], wanted %d; at HEAD %d orders, %d open, %d closed (relay data/b763_author_rulings.txt, data/b763_ledgers.txt, data/b763_orders.txt).' % (
                 f['rl_renders'], f['led_xv'], f['led_build'], f['led_head'], f['led_roster'][0], f['led_roster'][1], f['led_roster'][3], f['ord_head'][0], f['ord_head'][1], f['ord_head'][2]), '',
             '**The dispatches:** SIDE-explicit-formula %d, each read by its run id, the exit file governing: %s; none elsewhere (relay data/b763_dispatch_rows.json).' % (
                 f['disp_ef'], '; '.join('%s %s at %s, %s h' % (i_, r_, s_, h_ if h_ is not None else '-') for i_, _n, r_, s_, _a, _b, h_ in f['runs'])), '',
             '**The reproduction run** ((R373)(12)): rows %d, reproducing %d, differing %d, not run %d, controls %d of %d (relay data/b763_reproduce.txt).' % (
                 f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1]), '',
             '**The ceiling:** %d readings, after Component 2 %s h and after Component 3 %s h at the lower figures against %d h, the last %s (relay data/b763_ceiling.txt).' % (
                 f['ce_n'], f['ce_readings'][0]['total'], f['ce_readings'][1]['total'], f['ce_ceiling'], f['ce_verdict'].lower()), '',
             '**The report of (10):** %s; the parts of each pass by the cadence and the price beside what each item took in the entry and the closing message.' % r10h_, '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD')))), '',
             '**The standing versions:** %s (relay data/b763_standing_v1372.txt), the one change (5) required; HANDOFF.md written once by tools/standing/handoff.py before the gate, at relay %s.' % (
                 '; '.join('%s %d of %d' % (v_, w_, n_) for v_, _c, n_, w_ in f['vers']), (K.HANDOFF_COMMIT or 'NOT SET')[:8]), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b763_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b763_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s. %s' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line(),
                                                                                                  __import__('standing.counter', fromlist=['refusals_line']).refusals_line(ACT)), '',   # ### b755: [U3] in force, the counter's line as it prints (its event in data/b755_events.txt (22))
             '**Act root:** b763 `%s` (previous `%s`, b762’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b763_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b763_standing_v1372.txt); the standing '
             'report tool (relay data/b763_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    lt5_ = ([fo_] if f['oc_words'][0] == 'LANDED, COMPILED' else []) + b8_
    rows_ += ['**The kernels:** SIDE-explicit-formula`s main at %s (entering at %s), %s, each peel read back at the remote; %s, kept for the next act`s step zero; v0.38 to %s unmoved; %s removed at its remote by b760, the clone`s branch kept at %s; zq-b730 at %s, unmoved; SIDE-dirichlet-mod-24`s main at %s, %s at %s, unmoved; no kernel beyond SIDE-explicit-formula touched; the %s branches as b763 found them; port-b707 at %s, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  ((lt5_[-1].get('peel') or '')[:8] if lt5_ else K.EF_BASE[:8]), K.EF_BASE[:8], ', '.join('%s at %s' % (x_.get('tag'), (x_.get('peel') or '')[:8]) for x_ in lt5_) or 'no tag cut',
                  ', '.join('%s at %s' % (b_, t_[:8]) for b_, t_ in (K.WEIL_BRANCH, K.ARITH_BRANCH) + tuple(K.ORDER_BRANCHES)), K.WEIL_TAG_B759[0],
                  K.WEIL_BRANCH_B759[0], K.WEIL_BRANCH_B759[1][:8],
                  K.ZQ_TIP[:8], K.M24_MAIN[:8], K.M24_TAG[0], K.M24_TAG[2][:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG,
                  K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root (the ferry`s Component 6), its set carrying OPEN_TRAILS and the canon as entered, HANDOFF.md among its files, its file named in the closing by its name, bytes and hash and its folder by role (relay data/b763_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b762’s %s, %s, %s, %s (relay data/b763_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b763_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b762():
    """b753's trail record over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: within the worklist`s MAX_DISPATCHES 18 in SIDE-explicit-formula (the price table`s upper figures for (6), (7)`s statement and the orders of (8) the ceiling left) and none in SIDE-dirichlet-mod-24; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: every run read by its id from its artifact, the exit file governing (data/b763_dispatch_rows.json); MEASURED off the worklist`s EF_RUNS and M24_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b763*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved, the act`s push-b763-* branches made beside them (slot 3); MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('kernel branches removed at a kernel`s remote', len(K.KERNEL_DELETES), len(K.KERNEL_DELETES), 'branches', '### none ((R373)(4): no clause of this ruling removes a kernel branch); push-b759-weil removed at SIDE-explicit-formula`s remote by b760, the clone`s branch kept; the four held branches of b725 to b730 kept.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b763 found them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b763*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act, the four unmoved; MEASURED off each branch against a3aad4cc.'),
    ('Lean files changed on SIDE-explicit-formula`s main', 'EFMAINLEAN', 'EFMAINLEAN', 'files', '### (R373)(6): the five modules of build one (FormFinite, PoleAutocorrelation, ParitySplit, AdmissibleWeights and OnePageStatement), and an order`s module where (8) landed one, main moved after each run`s success; SIDE-dirichlet-mod-24 unmoved; MEASURED off git diff --name-only from a3aad4cc to main.'),
    ('tags cut at main`s read-back', 'EFTAGS', 'EFTAGS', 'tags', '### (R373)(6), (8): v0.42 at 4964e957 and the tag of each order of (8) built in full, each peel read back at the remote equal to main; v0.38 to v0.41 and v0.2.0 unmoved; MEASURED off SIDE-explicit-formula`s tags of the worklist`s WEIL_TAG and ORDER_TAGS.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b762-closing, push-b762-preroot, push-b762-record; PLACE-papers push-b762-preroot, push-b762-record; each by name, through the one-call tool, one per message, after the --merged listing and the citation check (data/b763_stepzero.txt :64-:69).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: the workflow at v0.41 takes a ref and a target alone, the names read from print_targets.txt ((R373)(5)).'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written (N3); no line added above the heading of rule [Q] (3), read by its digest.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none: REGISTRY not written; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R373)(1): FINDINGS :15797 (relay data/b763_corrigendum.json).'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R373)(1): row (83).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none: (R373) orders no ERRATA entry and its (W) list names no ERRATA.'),
    ('the ruling`s texts entered, each equal to its text with its fields filled', 'RULINGS', 'RULINGS', 'texts', '### (R373)(9): [C1] as the canon`s section XXV; [A1] to [A12], [B1] and [B2] in OPEN_TRAILS under one dated head beside the line naming [W1]`s bank; MEASURED off relay data/b763_ledgers.json`s entered.'),
    ('orders closed in the roster`s form', 'ORDCLOSED', 'ORDCLOSED', 'orders', '### (R373)(9): W-ORD-GW-IMPORT and W-ORD-TABLE-SHAPE CLOSED by [A11] and [A12], and each order an [X3] line moves after them; MEASURED off relay data/b763_ledgers.json`s roster (the open count before, after [B2] and after the build lines).'),
    ('statements of (6) compiled at their tag', 'FORMSTMTS', 'FORMSTMTS', 'statements', '### (R373)(6): (S1) to (S5), each read against (6) before its grade, each new name`s axioms line within the standard three at run 44646848292 (v0.42 = 4964e957); MEASURED off relay data/b763_outcomes.json`s form, the statements read compiled.'),
    ('build lines composed for OPEN_TRAILS from the runs', 'BUILDLINES', 'BUILDLINES', 'lines', '### (R373)(6)-(8): SF_BUILT by the author`s word, X2 for (7), and an [X3] line for each order of (8) built in full; MEASURED off relay data/b763_xlines.json.'),
    ('integration lines in the canon`s form', 1, 1, 'lines', '### (R373)(10): this act`s own, the entry`s last line, bare, written by (10)`s rule and by no reader of the act`s banks.'),
    ('standing changes landed', 1, 1, 'changes', '### (R373)(5): v1.37.2 at relay d34f7323, commit.py`s KERNEL_ACTS and FF_ACTS admitting b763 at SIDE-explicit-formula alone, VERSION moved, its planted control among its ten cases (relay data/b763_standing_v1372.txt).'),
    ('orders entered with the trail', 'ORDADDED', 'ORDADDED', 'orders', '### (R373)(9): W-ORD-PREMISE-POSITIONS by [B2], OPEN; MEASURED off relay data/b763_ledgers.json`s roster rows.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py`s full run at b763 as (R373)(12) orders it, in the foreground; MEASURED off data/b763_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### the tools` runs over the record, the runner`s prints and the reproduction run as (R373)(12) orders it, nothing computed at a zero: v1.37.2`s controls, the dispatch tool`s controls, the seven pre-send reads, the outcomes, the ceiling, the IMP2-TAU reading, the corrigendum, the author`s rulings, the trail lines, the orders, the reproduction, the probe-path refusal, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### none: (R373) registers no test, a theorem taking a compile outcome and no verdict ((6)), and no data/b763_registrations.txt is written; MEASURED off git.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act, nothing of H-ONSET-DENSITY computed and no row of a bank of zeros opened ((R373)(12)); MEASURED off git.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2): no registered object this act, nothing computed at a zero; MEASURED off git.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### (R373)(6)-(8): build one`s five on push-b763-form, (7)`s ControlFailureStatement on push-b763-arith, and (8)`s SquaresAt24 and KeiperPolygamma on push-b763-squares and push-b763-keiper; MEASURED off the act`s branches against a3aad4cc, each module once.'),
    ('Lean files edited by the act`s own commits', 'EFEDIT', 'EFEDIT', 'files', '### none: no Lean file the act found edited, print_targets.txt alone taking each send`s names; MEASURED off the act`s branches against a3aad4cc.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R373)(5): tools/standing/ v1.37.2, commit.py and VERSION changed and v1372.py its controls tool, by one version commit (relay d34f7323) with its controls in its bank (data/b763_standing_v1372.txt); MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 4, 4, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended; HANDOFF.md by tools/standing/handoff.py before the gate ((R373)(13)); data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part and computation; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b763_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound requests are the pushes and their ls-remote read-backs, the branch removals of (4), the dispatches and the artifact downloads, and the gh reads under the GitHub login; none carries an identifier, nothing fetched from the web ((R373)(12)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b763: no registered object and no figure bank ((R373) registers no test)
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    # ### b763: the runs' count read against the worklist's caps (SIDE-explicit-formula's alone, at most 18, M24_RUNS empty)
                    EFRUNS=len(K.EF_RUNS) + len(K.M24_RUNS),
                    # ### b763: main's Lean and commits past the entering main a3aad4cc (EF_BASE), the act's tags, the statements of (6) compiled,
                    # ### the build lines, the texts entered, the orders the roster moved and added, the OPEN_TRAILS block's lines
                    EFMAINLEAN=sum(1 for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, 'main').split() if f_.endswith('.lean')),
                    EFTAGS=sum(1 for t_ in [K.WEIL_TAG] + list(K.ORDER_TAGS) if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/tags/' + t_[0])),
                    RULINGS=jcount('b763_ledgers.json', lambda j: len(j.get('entered') or {})),
                    # ### the ledgers bank keeps the open counts and the WANTED rows, not the moved names: closed = before - after [B2] + entered + moved after
                    ORDCLOSED=jcount('b763_ledgers.json', lambda j: int((j.get('roster') or {}).get('before_open') or 0) - int((j.get('roster') or {}).get('mid_open') or 0)
                                     + len([r_ for r_ in ((j.get('roster') or {}).get('rows') or []) if str(r_[0]).endswith(' enters OPEN') and r_[2]])
                                     + len((j.get('roster') or {}).get('moved_after_b2') or [])),
                    ORDADDED=jcount('b763_ledgers.json', lambda j: len([r_ for r_ in ((j.get('roster') or {}).get('rows') or []) if str(r_[0]).endswith(' enters OPEN') and r_[2]])),
                    FORMSTMTS=jcount('b763_outcomes.json', lambda j: len([s_ for s_ in ((j.get('form') or {}).get('statements') or []) if s_.get('compiled')])),
                    BUILDLINES=jcount('b763_xlines.json', lambda j: len(j.get('lines') or [])),
                    EFMAINCOMMITS=int(_git(K.EF_DIR, 'rev-list', '--count', '%s..main' % K.EF_BASE) or 0),
                    OTBLOCK=jcount('b763_ledgers.json', lambda j: sum(int(f_.get('lines_after') or 0) - int(f_.get('lines_before') or 0) for f_ in (j.get('files') or []) if f_.get('path') == 'OPEN_TRAILS.md')),
                    REPROWS=jcount('b763_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b763_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    # ### b763: the modules the act's branches add past a3aad4cc, each once, and the Lean files their commits edit ((R373)(6)-(8))
                    EFNEW=len(set(f_ for b_ in [K.WEIL_BRANCH, K.ARITH_BRANCH] + list(K.ORDER_BRANCHES)
                                  for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=A', K.EF_BASE, b_[1]).split() if f_.endswith('.lean'))),
                    EFEDIT=len(set(f_ for b_ in [K.WEIL_BRANCH, K.ARITH_BRANCH] + list(K.ORDER_BRANCHES)
                                   for f_ in _git(K.EF_DIR, 'diff', '--name-only', '--diff-filter=M', K.EF_BASE, b_[1]).split() if f_.endswith('.lean'))),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1372', 'controls_control', 'presend_s123', 'presend_s4', 'presend_s5', 'presend_sf',
                                               'presend_s7', 'presend_s24', 'presend_skp', 'outcomes', 'ceiling', 'imp2tau', 'corrigendum',
                                               'author_rulings', 'ledgers', 'orders', 'reproduce', 'pathrefusal', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b763_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b763_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFEDIT', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE', 'EFMAINLEAN', 'EFTAGS', 'RULINGS', 'ORDCLOSED', 'ORDADDED', 'FORMSTMTS', 'BUILDLINES', 'EFMAINCOMMITS', 'OTBLOCK',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b763_registration_%s.txt -- b763, THE CONTROL`S FAILURE FROM ITS COEFFICIENTS: b762 AT ITS WEIGHT; THE FINITE "
                             "AND SIGNED PARTS OF THE FORM COMPILED AT v0.42; THE STATEMENT FILE BUILT; THE STATEMENT OF THE FAILURE COMPILED BEFORE "
                             "ITS PROOF; THE ORDERS OF (8) BUILT WHERE THE CEILING LEFT THEM; THE AUTHOR`S WORDS AND THE CANON`S SECTION ENTERED; ONE "
                             "STANDING CHANGE; NO DEPOSIT, UNDER (R373)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b762's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b763: b762's lines read banks this
act does not write, and are not carried; the lines are b763's: the form's five statements landed at v0.42, the statement file built, (7)'s
statement compiled before its proof and each order of (8) built in full, each read from the runner by its run id (KERNEL); tools/standing/
v1.37.2, the dispatch tool, the pre-send reads and the reproduction run by their controls (CERTIFIED); the corrigendum, the price with the
ceiling's two readings, and the author's words with the canon's section, the trail's lines and the roster (REGISTERED); what did not land,
(7)'s proof not sent, the orders of (8) carried by name, and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b763's lines, each from the record tool's figures over b763's banks (REC._figs), the record's guard first
    REC._guard(f)
    fo_, sf_, ar_ = f['oc_form'], f['oc_sf'], f['oc_arith']
    n6_ = sum(1 for s_ in fo_.get('statements') or [] if s_.get('compiled'))
    # ------------------------------------------------------------------ KERNEL or HELD: (R373)(6), the five statements, read by run id (the seat the template appends)
    sk = seat('%s_outcomes.txt' % ACT, '## (6) BUILD ONE')
    keys['FORM'] = (('KERNEL -- THE FINITE AND SIGNED PARTS OF THE FORM LANDED: %d of 5 statements compiled (%s), %s cut at main`s read-back = %s (tag object %s), run %s, each new name`s axioms line within propext, Classical.choice and Quot.sound, no sorryAx; the grade %s, binding no premise, read against (6) from each compiled statement before it was written. SOURCE %s.' % (
        n6_, ', '.join(s_.get('key') for s_ in fo_.get('statements') or [] if s_.get('compiled')), fo_.get('tag'), (fo_.get('peel') or '')[:8], (fo_.get('tag_object') or '-')[:8], fo_.get('run'),
        ', '.join(sorted(set(s_.get('grade') or '-' for s_ in fo_.get('statements') or [] if s_.get('compiled')))), sk['text'])) if f['oc_words'][0] == 'LANDED, COMPILED' else (
        'HELD -- (6), NOT LANDED AS ORDERED: %s, statements compiled %d of 5, main unmoved. SOURCE %s.' % (f['oc_words'][0].lower(), n6_, sk['text'])))
    # ------------------------------------------------------------------ KERNEL or HELD: the statement file, by the author's word of 2026-11-19
    ss = seat('%s_outcomes.txt' % ACT, 'THE STATEMENT FILE (the author`s word')
    keys['SF'] = (('KERNEL -- THE STATEMENT FILE BUILT, BY THE AUTHOR`S WORD OF 2026-11-19: SIDEExplicitFormula/OnePageStatement.lean, One Page v2.0`s 19 rows of SIDE-explicit-formula each stated apart from its proof and closed by the name that proves it, the three rows of SIDE-kernel v1.5 named in its header and stated nowhere; its 19 names within the standard three at run %s, landed with %s; W-ORD-STATEMENT-FILE CARRIED, its object the same file for the three rows of SIDE-kernel. SOURCE %s.' % (
        (sf_.get('runs') or ['-'])[-1], fo_.get('tag') or '-', ss['text'])) if f['oc_words'][1] == 'BUILT' else (
        'HELD -- THE STATEMENT FILE, NOT BUILT: %s; W-ORD-STATEMENT-FILE CARRIED whole with the build`s reading. SOURCE %s.' % (f['oc_words'][1].lower(), ss['text'])))
    seats.append(ss)
    # ------------------------------------------------------------------ KERNEL or HELD: (R373)(7), the statement of the control's failure, before its proof
    sa = seat('%s_outcomes.txt' % ACT, '## (7) THE CENTRE')
    keys['ARITH'] = (('KERNEL -- THE STATEMENT OF THE CONTROL`S FAILURE COMPILED BEFORE ITS PROOF: ControlFailureB (FORM B, at a named test function in classK and a named width) and ControlFailureA n (FORM A), each a definition of a Prop with no proof and no sorry, committed on push-b763-arith at %s before any line of a proof, run %s, its names within the standard three; the control that no zero is used %s over its file. SOURCE %s.' % (
        (ar_.get('sha') or '')[:8], ar_.get('run'), f['ps']['s7']['nozero'], sa['text'])) if f['oc_words'][2] == 'STATEMENT COMPILED, NO PROOF SENT' else (
        'HELD -- (7)`s STATEMENT, NOT COMPILED AS ORDERED: %s. SOURCE %s.' % (f['oc_words'][2].lower(), sa['text'])))
    seats.append(sa)
    # ------------------------------------------------------------------ KERNEL: (R373)(8), each order built in full, its line [X3]
    s8 = seat('%s_outcomes.txt' % ACT, '## (8) THE ORDERS PRICED BESIDE IT')
    for o_ in [o_ for o_ in f['oc_orders'] if o_.get('outcome') == 'BUILT IN FULL']:
        keys['O8_' + o_['item']] = 'KERNEL -- %s BUILT IN FULL UNDER (8): %s cut at main`s read-back = %s (tag object %s), run %s, its names within the standard three, no sorryAx; its line [X3]. SOURCE %s.' % (
            o_['order'], o_.get('tag'), (o_.get('peel') or '')[:8], (o_.get('tag_object') or '-')[:8], o_.get('run'), s8['text'])
    seats.append(s8)
    # ------------------------------------------------------------------ REGISTERED: (R373)(1), the corrigendum for b762
    sc_ = seat('%s_corrigendum.txt' % ACT, '**ITEMS ')
    keys['CORRIGENDUM'] = ('REGISTERED -- THE CORRIGENDUM FOR b762, SHORT: %s items, CLAIM %s, CLOSE %s, %s repeats; b762`s %s CLAIM items printed in full; the findings after its lock entered as events, the navigator`s own as CLAIM, [I1] among them; at FINDINGS :%s, the corrigenda bank`s row (%s); PLACE-papers %s. SOURCE %s.' % (
        f['corr_items'], f['corr_claim'], f['corr_close'], f['corr_repeat'], f['corr_claim'], f['corr_line'], f['corr_row'], K.C1_PP[:8], sc_['text']))
    seats.append(sc_)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.37.2 ((R373)(5)), by its controls
    sv = seat('%s_standing_v1372.txt' % ACT, '**v1.37.2: CONTROLS ')
    keys['VERSIONS'] = ('CERTIFIED -- tools/standing/ v1.37.2, THE ONE CHANGE (5) REQUIRED, by a commit of its own moving VERSION from v1.37.1: commit.py admitting b763 at SIDE-explicit-formula alone, %s. SOURCE %s.' % (
        '; '.join('%s at relay %s, %d cases, %d as wanted, the planted control among them' % (v_, K.C1_STANDING[:8], n_, wv_) for v_, _c, n_, wv_ in f['vers']), sv['text']))
    seats.append(sv)
    # ------------------------------------------------------------------ CERTIFIED: the dispatch and read tool by its own controls (the seat the template appends)
    sw = seat('%s_controls_control.txt' % ACT, '**THE TOOL`S CONTROLS: ')
    keys['CONTROLS'] = ('CERTIFIED -- tools/b763_controls.py BY ITS OWN CONTROLS: %d of %d as wanted, committed before its opening dispatch; every run read by its id from the downloaded artifact, the exit file governing, %d dispatch%s in SIDE-explicit-formula against the worklist`s %d and none elsewhere. SOURCE %s.' % (
        f['cc_ctl'][0], f['cc_ctl'][1], f['disp_ef'], '' if f['disp_ef'] == 1 else 'es', f['ce_disp'][1], sw['text']))
    # ------------------------------------------------------------------ CERTIFIED: the pre-send reads of (R368)(4) and each send's salt check
    sp_ = [seat('%s_presend_%s.txt' % (ACT, s_), '**THE PRE-SEND READS AT ') for s_ in K.PRESEND_SENDS]
    keys['PRESEND'] = ('CERTIFIED -- THE PRE-SEND READS AND THE SALT CHECK BEFORE EACH SEND, by tools/b763_presend.py committed before its run: %s; the control that no zero is used over (7)`s file %s. SOURCE %s.' % (
        '; '.join('%s at %s %s, %d of %d statements, controls %d of %d' % (s_, f['ps'][s_]['rev'], f['ps'][s_]['salt'], f['ps'][s_]['salt_n'][0], f['ps'][s_]['salt_n'][1], f['ps'][s_]['ctl'][0], f['ps'][s_]['ctl'][1])
                  for s_ in K.PRESEND_SENDS), f['ps']['s7']['nozero'], ' ; '.join(x_['text'] for x_ in sp_)))
    seats.extend(sp_)
    # ------------------------------------------------------------------ CERTIFIED: (R373)(12), the reproduction run
    sr_ = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('CERTIFIED -- THE RESEARCH INSTRUMENTS REPRODUCED: tools/research/reproduce.py`s full run in the foreground, rows %d, reproducing %d, differing %d, not run %d, the planted controls %d of %d as wanted, %d s. SOURCE %s.' % (
        f['rp_rows'], f['rp_repro'], f['rp_differs'], f['rp_notrun'], f['rp_ctl'][0], f['rp_ctl'][1], f['rp_secs'], sr_['text']))
    seats.append(sr_)
#⟪END⟫
#⟪SECTION report 4⟫
    ppw_ = dict((k_, c_) for k_, _p, c_ in K.PP_WRITES)
    pr_ = f['pr_rows']
    # ### b763, Component 6 (the Edit tool): a range printed once where its ends are equal, as the entry prints it
    rg_ = lambda a_, b_, u_: ('%s %s' % (a_, u_[:-2] if (u_ == 'dispatches' and a_ == 1) else u_)) if a_ == b_ else '%s to %s %s' % (a_, b_, u_)
    pw_ = lambda k_: '%s over %s' % (rg_(pr_[k_]['lo_h'], pr_[k_]['hi_h'], 'h'), rg_(pr_[k_]['dispatches'][0], pr_[k_]['dispatches'][1], 'dispatches'))
    # ------------------------------------------------------------------ REGISTERED: (R373)(3), the price table and the ceiling's two readings
    sq = seat('%s_price.txt' % ACT, '**THE PRICE TABLE: ')
    sce = seat('%s_ceiling.txt' % ACT, '**THE CEILING: READINGS ')
    keys['PRICE'] = ('REGISTERED -- THE PRICE AND THE CEILING OF (3): the table banked before Component 1 from banked timings, the lower sum %s h against %d h at step zero, carried %s, the upper sum %s h; the ceiling read after Component 2 at %s, %s h, %s, and after Component 3 at %s, %s h, %s; dispatches %d against %d. SOURCE %s ; %s.' % (
        f['pr_lower'], f['pr_ceiling'], f['pr_carried'], f['pr_upper'],
        f['ce_readings'][0]['at'], f['ce_readings'][0]['total'], f['ce_readings'][0]['verdict'], f['ce_readings'][1]['at'], f['ce_readings'][1]['total'], f['ce_readings'][1]['verdict'],
        f['ce_disp'][0], f['ce_disp'][1], sq['text'], sce['text']))
    seats.extend([sq, sce])
    # ------------------------------------------------------------------ REGISTERED: (R373)(9), the author's words, the canon's section XXV, the trail's lines and the roster
    sr = seat('%s_author_rulings.txt' % ACT, '**THE AUTHOR`S RULINGS: WORDS ')
    sg = seat('%s_ledgers.txt' % ACT, '**THE LEDGERS: FILES ')
    so = seat('%s_orders.txt' % ACT, '**ORDERS ')
    keys['WORDS'] = ('REGISTERED -- THE AUTHOR`S WORDS ENTERED: [W1] banked verbatim beside the navigator`s %d renderings (%s); THE_METHOD_CANON.md took [C1] as section XXV at :%d, no byte above it changing; OPEN_TRAILS took the bank line, [A1] to [A12], [B1], [B2] and %d build lines under one dated head from :%d, no line moving, controls %d of %d (%s); one PLACE-papers commit, %s; the roster %d open before, %d with the lines up to [B2], wanted %d, %d of %d as wanted; at HEAD orders %d, open %d, closed %d. SOURCE %s.' % (
        f['rl_renders'], sr['text'], f['led_xv'], f['led_build'], f['led_head'], f['led_ctl'][0], f['led_ctl'][1], sg['text'], ppw_.get('trails', '-')[:8],
        f['led_roster'][0], f['led_roster'][1], f['led_roster'][3], f['led_rows'][0], f['led_rows'][1], f['ord_head'][0], f['ord_head'][1], f['ord_head'][2], so['text']))
    seats.extend([sr, sg, so])
    # ------------------------------------------------------------------ HELD: (R373)(7), the proof not sent, by the ceiling after Component 2
    if not str(f['oc_words'][2]).startswith('PROOF'):
        keys['PROOF7'] = ('HELD -- (7)`s PROOF, NOT SENT: the ceiling after Component 2 left %s h for it, where FORM B`s upper %s h and FORM A`s %s h each do not fit; FORM A priced at %s and FORM B at %s; W-ORD-LI-ARITH carried by [X2], its statement compiled. SOURCE %s.' % (
            f['ce_proof_left'], pr_['(7) B']['hi_h'], pr_['(7) A']['hi_h'], pw_('(7) A'), pw_('(7) B'), sce['text']))
    # ------------------------------------------------------------------ HELD: (R373)(8), each order not built in full, carried by name with its price
    b8_ = set('(8) ' + o_['order'][6:] for o_ in f['oc_orders'] if o_.get('outcome') == 'BUILT IN FULL')
    keys['CARRIED8'] = ('HELD -- THE ORDERS OF (8) NOT BUILT IN FULL, EACH CARRIED BY NAME WITH ITS PRICE, NO LINE WRITTEN FOR IT: %s. SOURCE %s.' % (
        '; '.join('W-ORD-%s, %s, %s' % (k_[4:], pw_(k_), w_.lower()) for k_, w_, _h, _l in f['ce_plan'] if k_ not in b8_) or 'none', sce['text']))
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R373)(12)) (the seat the template appends)
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    land_ = [k_ for k_, ok_ in (('FORM', f['oc_words'][0] == 'LANDED, COMPILED'), ('SF', f['oc_words'][1] == 'BUILT'), ('ARITH', f['oc_words'][2] == 'STATEMENT COMPILED, NO PROOF SENT')) if ok_] \
        + ['O8_' + o_['item'] for o_ in f['oc_orders'] if o_.get('outcome') == 'BUILT IN FULL']   # ### b763: each line`s tier by its outcome
    order = [('KERNEL', land_), ('CERTIFIED', ['VERSIONS', 'CONTROLS', 'PRESEND', 'REPRO']), ('REGISTERED', ['CORRIGENDUM', 'PRICE', 'WORDS']),
             ('HELD', [k_ for k_ in ('FORM', 'SF', 'ARITH') if k_ not in land_] + [k_ for k_ in ('PROOF7',) if k_ in keys] + ['CARRIED8', 'HELD'])]
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
