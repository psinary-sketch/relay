# -*- coding: utf-8 -*-
# b753 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R363)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R363)(2) repair it carries. Edited by the Edit tool. Carried at b753 by tools/b753_fold.py (`carry`) from tools/acts/b752.py,
# b752`s names substituted; the citation`s sections adopted from tools/b753_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b752`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b752`s carried till
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
# ### b753, Component 1: THE c1 ROUTE FOR b752'S WEIGHT LINE AND ITS CORRIGENDUM, (R363)(1)-(3) and (7), written by the Edit tool against
# ### b752's banks (13 events, 36 defects, 27 refusals at 0e855242) and v1.33.0 (relay 7c91353a), in b752's route's form. The carried route
# ### (b750's figures under b752's names) was removed at step zero ( `carry.py ruled` R5); nothing composed by it.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = True
C1_PREV_CLOSE = '0e855242'          # ### b752's closing push tip, the public relay's main at step zero ((R363)(1))
C1_CLOSING_COMMIT = '67586a00'      # ### b752's closing commit (its closing row, data/b752_steps.json)
C1_REFUSAL_AT = '0e855242'          # ### its refusal bank read at its closing push tip (27 lines)
C1_NOTED = '2026-11-11'
C1_CORRIGENDA_LAST = 72
C1_STANDING = '7c91353a'            # ### v1.33.0's own commit
C1_V170 = 'b753_standing_v1330.txt'   # ### the controls bank of the repairs this corrigendum lands (v1.33.0)
C1_WEIGHT_HEAD = '*Appended 2026-11-11 by b753 to b752’s entry (:%d), under `(R363)`(1)' % K.B711_ENTRY
C1_ENTRY_NEEDLE = '## W-ORD-MECHANISM-ATTRIBUTION’s plan passed at [P1]'
C1_TRAIL_NEEDLE = '### b752 — lane two, act one hundred and seventy-nine'
C1_BRACKET = re.compile(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[(CLAIM|CLOSE) ; ([^\]]*)\]")
# ### (R363)(1)'s cited foot lines, each read at its line: (bank, line, what)
C1_FEET = (('b752_corrigendum.txt', 84, 'b751`s corrigendum'), ('b752_standing_v1320.txt', 211, 'v1.32.0'), ('b752_crossref.txt', 107, 'the cross-reference'),
           ('b752_cq_signature.txt', 166, 'the signature'), ('b752_statements.txt', 1431, 'the statements'), ('b752_attribution_plan.txt', 103, 'the plan'),
           ('b752_line.txt', 54, 'the line'))


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
    for l in _c1_rd('b752_events.txt').split(NL):
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
    for m in re.finditer(r"(?m)^    \(([a-z]'?)\) (.*)$", _c1_rd('b752_defects.txt')):
        b = C1_BRACKET.match(m.group(2))
        if not b:
            sys.exit('### DEFECT (%s) CARRIES NO BRACKET -- NOTHING COMPOSED' % m.group(1))
        out.append((m.group(1), b.group(1), b.group(2), b.group(3), m.group(2)))
    return out


def _c1_feet():
    """{bank: (line, text)}: each foot line (R363)(1) cites, at the line it cites; any other place exits."""
    out = {}
    for name, ln, what in C1_FEET:
        (t,), at = _c1_fl(name, r'^(### ### \*\*.*\*\*)$', what)
        if at != ln:
            sys.exit('### %s: THE FOOT AT :%d, (R363)(1) CITES :%d -- NOTHING COMPOSED' % (name, at, ln))
        out[name] = (at, t)
    return out


def _c1_weight():
    c = 'b752_closing.txt'
    head = _c1_rd(c).split(NL)[0]
    pub = _c1_git('show', '%s:data/b752_closing.txt' % C1_PREV_CLOSE).replace(chr(13), '').split(NL)[0]
    if pub != head:
        sys.exit('### data/b752_closing.txt :1 IS NOT THE LINE THE PUBLIC RELAY CARRIES AT %s -- NOTHING COMPOSED' % C1_PREV_CLOSE)
    steps = json.load(open(os.path.join(D, 'b752_steps.json'), encoding='utf-8')).get('rows') or []
    rec = [r['commit'][:8] for r in steps if r.get('phase') == 'record' and r.get('repo') == 'relay']
    clo = [r['commit'][:8] for r in steps if r.get('phase') == 'closing' and r.get('repo') == 'relay']
    if K.B714_RECORD[:8] not in rec or C1_CLOSING_COMMIT not in clo:
        sys.exit('### data/b752_steps.json: record %s, closing %s -- NOTHING COMPOSED' % (rec, clo))
    ft = _c1_feet()
    (cc, cd, rp, rn, sd, se), l_cn = _c1_fl(c, r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT (\d+) OF (\d+) ; THE SET: DEFECTS (\d+), EVENTS (\d+),', 'the counter')
    (sa, sb), l_sh = _c1_fl(c, r'^      ### AGREE (\d+) of (\d+)$', 'the sealed tools')
    suite = r'^\s*%s : ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) (\[.*\])\.'
    pre, l_pre = _c1_fl(c, suite % 'pre-push', 'the pre-push suite')
    post, l_post = _c1_fl(c, suite % 'post-push', 'the post-push suite')
    (nbk,), l_bk = _c1_fl(c, r'^### THE ROOT`S BANKS .*: BANKS (\d+) ; CLEAN AND EQUAL AT HEAD \1 ; HEAD THE REMOTE MAIN True', 'the root`s banks')
    sc = json.load(open(os.path.join(D, 'b752_scores_close.json'), encoding='utf-8'))
    sc = sc.get('scores') or sc
    held = [k_ for k_ in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3') if (sc.get(k_) or ['?'])[0] == 'HELD']
    if held != ['N1', 'N2', 'N3', 'N4', 'S1', 'S2', 'S3'] or 'scores 7 of 8 HELD' not in head:
        sys.exit('### data/b752_scores_close.json: HELD %s -- NOTHING COMPOSED' % held)
    (_sl,), l_sl = _c1_fl(c, r'^    \(N1\) HELD \(N2\) HELD \(N3\) HELD \(N4\) HELD \(N5\) (REFUTED) ; \(S1\) HELD \(S2\) HELD \(S3\) HELD$', 'the closing`s scores')
    (_n5,), l_n5 = _c1_fl(c, r'^    \(N5\) REFUTED -- (the address scan \(relay data/b752_address_scan\.txt\): PREVIOUS ADDRESS: 0; THE AUTHOR`S NAME: 0; PREVIOUS NAME: 0; THE ORCID: 0)', 'N5')
    ar = json.load(open(os.path.join(D, 'b752_act_root.json'), encoding='utf-8'))
    if ar.get('root') != K.B714_ROOT:
        sys.exit('### data/b752_act_root.json`s root %s -- NOTHING COMPOSED' % ar.get('root'))
    (ci_, ce_, cf_, cc_, cl_, cr_), l_co = _c1_fl(c, r'^    the generated entry for b751`s events and defects.*: ITEMS (\d+): EVENTS (\d+), DEFECTS (\d+) ; CLAIM (\d+), CLOSE (\d+) ; REPEAT (\d+) ; ', 'b751`s corrigendum')
    (va, vb), l_v = _c1_fl(c, r'^    tools/standing/ at v1\.32\.0: .*; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED$', 'the v1.32.0 foot')
    (xq, xh, xc), l_x = _c1_fl(c, r'^    the six questions .*: THE CROSS-REFERENCE: QUESTIONS (\d+) ; HELD (\d+) ; CANDIDATES (\d+) ;', 'the cross-reference')
    (gt,), l_g = _c1_fl(c, r'^    the class-group signature .*THE TABLE \((neg & N \d+, neg & no N \d+, pos & N \d+, pos & no N \d+)\) ; THE STATEMENT TRUE ;', 'the signature')
    (_st,), l_st = _c1_fl(c, r'^    the kernel`s seven classes .*: THE STATEMENTS: \(i\) (A CLASS OF SIDE-kernel v1\.5 IS AN ENUMERATED CONSTRUCTOR WITH A COUNT \(7\))', 'the statements')
    (kst, stg, lm1, lm2), l_ln = _c1_fl(c, r'^    the INTEGRATION line .*: THE LINE: COMPOSED ; .*KEYSTONE (\S+) ; STAGE (\S+) ; MATCHED (\d+) OF (\d+) ;', 'the line')
    (rr, rp_, rd_, rn_), l_rp = _c1_fl(c, r'^    tools/research/reproduce\.py.*: ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ;', 'the instruments')
    sca, l_sc = _c1_fl(c, r'^    the scan over every commit and bank of the act.*: PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', 'the scan')
    (_tg,), l_tg = _c1_fl(c, r'^### THE KERNELS: .*(no tag beyond v0\.38)', 'the tag')
    _mv, l_mv = _c1_fl('b752_mirror_verify.txt', r'^  ### VERDICT: (CLEAN ON ALL THREE CLAUSES)$', 'the mirror')
    (mz, msha, mmd5), l_mz = _c1_fl(c, r'^### THE MIRROR .*(mirror-refresh-2026-11-10-b752)\.zip ; \d+ bytes ; sha256 ([0-9a-f]{8})[0-9a-f]* ; MANIFEST md5 ([0-9a-f]{8})', 'the mirror`s archive')
    (_p1,), l_p1 = _c1_fl('b752_author_answers.txt', r'^(RESULT \(transcript line 7360, 2026-11-11T00:02:48\.817Z\): The user answered: "\[P1\] The attribution plan)', 'the [P1] answer')
    (_nr,), l_nr = _c1_fl('b752_author_answers.txt', r'^(RESULT \(transcript line None, None\): ### NO RESULT)$', 'the root`s missing row')
    if l_p1 != 7 or l_nr != 67:
        sys.exit('### data/b752_author_answers.txt: [P1] at :%d, the missing row at :%d, (R363)(1)-(2) cite :7 and :67 -- NOTHING COMPOSED' % (l_p1, l_nr))
    ev, dr = _c1_events(), _c1_defects()
    if sorted(ev) != list(range(1, 14)) or len(dr) != 36 or (int(sd), int(se)) != (36, 13):
        sys.exit('### EVENTS %s ; DEFECTS %d ; THE SET %s, %s -- NOTHING COMPOSED' % (sorted(ev), len(dr), sd, se))
    dt = [x[2] for x in dr]
    dn = sum(1 for x in dr if x[3] != 'NEW')
    nav = [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"]
    fail = ', '.join(re.findall(r"'([^']+)'", pre[3]))
    return (C1_WEIGHT_HEAD + ' -- b752 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay data/b752_closing.txt):* “%s” (data/b752_closing.txt :1, the public relay at %s, relay main read back from the remote after the closing push and its step-row commit); its '
            'relay commit the record’s %s, the closing’s %s (data/b752_steps.json, the record and closing rows). As its rows read: b751 entered at its weight with its corrigendum, items %s (events %s, defects %s), CLAIM %s, CLOSE %s, '
            'REPEAT %s (:%d; data/b752_corrigendum.txt :%d); standing tools v1.32.0, %s of %s (:%d; data/b752_standing_v1320.txt :%d); the cross-reference of %s questions, held %s, candidates %s, no order entered (:%d; data/b752_crossref.txt :%d); '
            'the class-group signature of cQ over n ≤ 3000, %s, the statement true (:%d; data/b752_cq_signature.txt :%d); the kernel’s classes read as statements, %s (:%d; data/b752_statements.txt :%d); '
            'the plan passed at [P1], nothing built (data/b752_attribution_plan.txt :%d; data/b752_author_answers.txt :%d); the INTEGRATION line, keystone %s, stage %s, matched %s of %s (:%d; data/b752_line.txt :%d); '
            'the instruments %s rows, %s reproduce, %s differ, %s not run (:%d); %s (:%d). The sealed tools AGREE %s of %s (:%d); the suite %s of %s pre-push and %s of %s post-push (:%d, :%d), the three failing (%s) declared on the face as carried. '
            'At the scores’ close SCORES 7 OF 8 HELD, N5 %s (:%d): the command bank’s matcher read the word ORCID in three read agents’ prompts as an identifier (defect (h’)); its own reading %s (:%d). '
            'The root %s over %s banks, chained from %s (data/b752_act_root.json; :%d); the mirror %s at %s, sha256 %s, MANIFEST md5 %s (data/b752_mirror_verify.txt :%d; :%d). '
            'The root’s answer unbanked: the answers bank reads NO RESULT for the root’s prompt (data/b752_author_answers.txt :%d), the harness having written the answer as an api-request-blob row alone (data/b752_events.txt (6)); '
            'route 1 taken under the author’s own condition and the question not put again (events (7)); the entry’s Next and the trail composed from the sealed order (events (11)); the root route retried once after its second remote read did not return the head its first had read, nothing pushed between (events (13)). '
            'The answer is entered by `(R363)`(2) and stands in the corrigendum below. %d events in data/b752_events.txt, rows (1)-(%d), entered after the lock, row (1) an event before it that no bank carried; %d defects, (a)–(j’), the navigator’s %s among them (data/b752_defects.txt). '
            'The counter CLAIM %s, CLOSE %s, REPEAT %s of %s over events and defects together (:%d); over the defects alone CLAIM %d, CLOSE %d, REPEAT %d of %d. '
            'Nothing deposited, no merge, no new Zenodo version, the draft held at v5; the corrigendum for these rows follows, under `(R363)`(7).' % (
                head, C1_PREV_CLOSE, K.B714_RECORD[:8], C1_CLOSING_COMMIT, ci_, ce_, cf_, cc_, cl_, cr_, l_co, ft['b752_corrigendum.txt'][0],
                vb, va, l_v, ft['b752_standing_v1320.txt'][0], xq, xh, xc, l_x, ft['b752_crossref.txt'][0], gt, l_g, ft['b752_cq_signature.txt'][0],
                _st.lower().replace('side-kernel', 'SIDE-kernel'), l_st, ft['b752_statements.txt'][0], ft['b752_attribution_plan.txt'][0], l_p1,
                kst, stg, lm1, lm2, l_ln, ft['b752_line.txt'][0], rr, rp_, rd_, rn_, l_rp, _tg, l_tg, sa, sb, l_sh, pre[1], pre[0], post[1], post[0], l_pre, l_post, fail,
                _sl, l_sl, _n5.replace('`', '’'), l_n5, K.B714_ROOT[:8], nbk, ar['previous'][:8], l_bk, _mv[0], mz, msha, mmd5, l_mv, l_mz, l_nr,
                len(ev), max(ev), len(dr), ', '.join('(%s)' % x for x in nav), cc, cd, rp, rn, l_cn, dt.count('CLAIM'), dt.count('CLOSE'), dn, len(dr)))


# ### the refusals: b752's bank at C1_REFUSAL_AT, one a line, and the row recording each (line, kind, time, row); :26 and :27 recorded by no
# ### row of b752's and entered beside the banks below
C1_REFUSALS = [(1, 'SED', '21:45:49Z', 'defect (a)'), (2, 'ENV', '21:50:57Z', 'defect (a)'), (3, 'WLIST', '22:10:08Z', 'defect (i)'), (4, 'WLIST', '22:10:11Z', 'defect (i)'),
               (5, 'WLIST', '22:10:14Z', 'defect (i)'), (6, 'LIMIT', '22:11:47Z', 'defect (j)'), (7, 'LIMIT', '22:11:48Z', 'defect (j)'), (8, 'READ', '23:27:10Z', 'defect (r)'),
               (9, 'PIPE', '23:31:48Z', 'defect (s)'), (10, 'REDIR', '23:42:21Z', 'defect (x)'), (11, 'READ', '23:42:45Z', 'defect (y)'), (12, 'SED', '23:44:08Z', 'defect (z)'),
               (13, 'READ', '00:05:42Z', 'defect (y)'), (14, 'READ', '00:07:39Z', "defect (a')"), (15, 'READ', '00:07:40Z', "defect (a')"), (16, 'READ', '00:07:40Z', "defect (a')"),
               (17, 'READ', '00:07:41Z', "defect (a')"), (18, 'READ', '00:07:42Z', "defect (a')"), (19, 'READ', '00:07:42Z', "defect (a')"), (20, 'READ', '00:07:55Z', "defect (a')"),
               (21, 'READ', '00:10:21Z', 'defect (y)'), (22, 'READ', '00:11:20Z', 'defect (y)'), (23, 'READ', '00:11:20Z', 'defect (y)'), (24, 'PIPE', '01:48:27Z', "defect (i')"),
               (25, 'REDIR', '02:57:00Z', "defect (j')"), (26, 'PIPE', '06:15:23Z', 'entered below'), (27, 'READ', '06:19:58Z', 'entered below')]
C1_FLIP = {}      # ### (R363)(7) flips no tag: each item read as its bank tags it
# ### (R363)(1)-(3), (7): three items entered beside b752's banks, each with its owner, tag and column
C1_CARRIED = [("(R363)(2), the root’s answer", "THE AUTHOR'S", 'CLAIM', 'NEW',
               'the answer at b752`s root, unbanked there (data/b752_author_answers.txt :67 NO RESULT; events (6), (11)), entered by the ruling as the order of acts: this act the system refresh; then the sitting; then the class-number-3 walk of `(R363)`(4) and the build of T0 and T1; then sections 6 to 8 of the Epstein document, written from compiled statements. It supersedes the order of data/b752_amendments.json row 3 in that one place; b752`s entry and trail are not rewritten'),
              ("(R363)(3)", "THE NAVIGATOR'S", 'CLAIM', 'REPEAT of the class of (R362)(2)',
               'the navigator`s correction: (i) I-109 and the signature of its negative n ordered as measurements, and a class-number-3 prediction proposed, with none of the record on these coefficients cited (data/b711_coeffs.txt :12; data/b718_derivation.txt and FINDINGS :10858; FINDINGS :11072, :11178, :11359, :11490, :12216; INSTRUMENTS :750, :758); the plan`s (1c) three facts consequences of b718`s theorem, the class-number-3 table b721`s; (ii) H-DIAL read as not run where the record holds it run and REFUTED at b725 (FINDINGS :11755); (iii) the rule of data/b752_rules.txt (12) widened by `(R363)`(7)(i); (iv) two statements of the hold to the author, corrected from the seat`s reads the same day'),
              ("the refusals :26 and :27", "THE SEAT'S", 'CLOSE', 'REPEAT b752 (r), (s)',
               'two calls the hook refused after the seal, recorded by no row of b752 (data/b752_hook_refusals.txt :26 PIPE 06:15:23Z, :27 READ 06:19:58Z at 0e855242); nothing ran or was read by them; entered here')]
C1_CORR_TITLE = ('## Corrigendum to b752’s record (relay data/b752_events.txt rows (1)-(13) and data/b752_defects.txt (a)-(j’)): thirteen events and thirty-six defects, each CLAIM or CLOSE and NEW or '
                 'REPEAT, the navigator’s (p) and (q) among them, with the root’s answer entered by `(R363)`(2), the navigator’s correction of `(R363)`(3) and two refusals no row recorded; '
                 'the one-call check, the subject read, the outbound matcher by form, the blob answer and the chain read, the halt’s price, the disk hold, the absent input and the failed remote read, '
                 'at tools/standing/ v1.33.0, each controlled, under (R363)(7)')


def _c1_q(s):
    return s.replace('\\', '\\\\').replace('*', '\\*').replace('_', '\\_').replace('`', '’')


def _c1_v170_line(needle):
    t = _c1_rd(C1_V170).split(NL)
    h = [i for i, l in enumerate(t, 1) if l.startswith(needle)]
    if len(h) != 1:
        sys.exit('### THE v1.33.0 BANK: %d LINES OPEN %r, NOT ONE -- NOTHING COMPOSED' % (len(h), needle))
    return h[0]


def _c1_state():
    ev = _c1_events()
    tags = dict((n, (lambda m: (m.group(2), m.group(3), m.group(1)) if m else (None, None, None))(C1_BRACKET.match(ev[n]))) for n in ev)
    dr = _c1_defects()
    dtext = dict((x[0], x[4]) for x in dr)
    rl = _c1_git('show', '%s:data/b752_hook_refusals.txt' % C1_REFUSAL_AT).replace(chr(13), '').strip(NL).split(NL)   # ### 27 lines at 0e855242
    bad_ref = []
    for ln, kind, at, row in C1_REFUSALS:
        if ln > len(rl) or ('| %s |' % kind) not in rl[ln - 1] or at[:8] not in rl[ln - 1]:
            bad_ref.append(ln)
            continue
        if row == 'entered below':
            continue
        k = row.split('(', 1)[1].rstrip(')')
        src = dtext.get(k, '')
        if ':%d' % ln not in src and at[:5] not in src:
            bad_ref.append(ln)
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', _c1_rd('b675_corrigenda.txt'))]
    (cc, cd), _l = _c1_fl('b752_closing.txt', r'^### THE COUNTER .*: CLAIM (\d+), CLOSE (\d+), REPEAT', 'the counter')
    v = _c1_rd(C1_V170)
    foot = [l for l in v.split(NL) if l.startswith('### ### **v1.33.0: CONTROLS')]
    s = dict(events=ev, tags=tags, defects=dr, notes=list(C1_NOTES))
    nc, nl_, _rep, _n = _c1_counts(s)
    bad = [k_ for k_, ok_ in (('the event rows (1)-(13)', sorted(ev) == list(range(1, 14))), ('each event`s bracket', all(t[0] for t in tags.values())),
                              ('the defect rows 36', len(dr) == 36), ('the refusals 27, each answered as listed', len(rl) == 27 and not bad_ref),
                              ('the navigator`s rows in b752`s defects bank (p), (q)', [x[0] for x in dr if x[1] == "THE NAVIGATOR'S"] == ['p', 'q']),
                              ('the corrigenda bank`s last row (%d)' % C1_CORRIGENDA_LAST, bool(cr) and max(cr) == C1_CORRIGENDA_LAST),
                              ('the v1.33.0 controls ALL AS WANTED', len(foot) == 1 and 'ALL AS WANTED' in foot[0]),
                              ('the counter the closing`s (CLAIM %s, CLOSE %s)' % (cc, cd), (nc, nl_) == (int(cc), int(cd)))) if not ok_]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (refusals %s ; counter %d, %d)' % (bad, bad_ref, nc, nl_))
    s['v170_foot'] = foot[0]
    return s


def _c1_counts(s):
    t = [s['tags'][n][0] for n in sorted(s['events'])] + [x[2] for x in s['defects']]
    rep = sum(1 for n in s['events'] if s['tags'][n][1] != 'NEW') + sum(1 for x in s['defects'] if x[3] != 'NEW')
    return t.count('CLAIM'), t.count('CLOSE'), rep, len(t)


def _c1_read_counts(s):
    """the counter as this corrigendum reads the items: the closing's 49 and the three entered beside them, no tag flipped."""
    nc, nl_, rep, n = _c1_counts(s)
    t = [x[2] for x in C1_CARRIED]
    return nc + t.count('CLAIM'), nl_ + t.count('CLOSE'), rep + sum(1 for x in C1_CARRIED if x[3] != 'NEW'), n + len(C1_CARRIED)


def _c1_owners(rows):
    c = {}
    for o in rows:
        c[o] = c.get(o, 0) + 1
    return ', '.join('%d %s' % (v_, k_.lower().replace("'s", '’s').replace("'", '’')) for k_, v_ in sorted(c.items(), key=lambda kv: -kv[1]))


def _c1_col(c):
    return 'NEW' if c == 'NEW' else c.replace('REPEAT ', 'REPEAT of ', 1).replace("'", '’').replace('`', '’')


# ### the repairs each item is met by at v1.33.0 (the controls bank data/b753_standing_v1330.txt), or the clause of (R363) that enters it
_C1_REP = '; `(R363)`(7)(vi), the seat’s repeat: the hook refused the call before it ran'
C1_EV_EXTRA = {1: '; no item of `(R363)`(7) names it; one remote read, no credential command', 2: '; no item of `(R363)`(7) names it; the two banks ride in the seal commit',
               3: '; `(R363)`(7)(vi), the seat’s repeat: v1.32.0’s part-order guard refusing', 4: '; `(R363)`(7)(vi), the seat’s repeat: v1.32.0’s part-order guard refusing',
               5: '; no item of `(R363)`(7) names it; the shell refused the line, nothing ran',
               6: '; repair (chain), `(R363)`(7)(iii): the answer read from the api-request-blob row, marked, and the chain read printed beside the bank',
               7: '; repair (halt), `(R363)`(7)(iv): the caps read beside the arms before a halt is put',
               8: '; repair (halt), `(R363)`(7)(iv): an arm in no part’s exercise bank costs no route',
               9: '; repair (chain), `(R363)`(7)(iii)', 10: '; entered by `(R363)`(2)', 11: '; entered by `(R363)`(2): the order now stands as that clause words it',
               12: '; entered by `(R363)`(2)', 13: '; repair (remote), `(R363)`(7)(ix): a failed remote read prints FAILED with its exit code and error text, the retry an event'}
C1_DF_EXTRA = dict([(x_, _C1_REP) for x_ in ('a', 'i', 'j', 'r', 's', 'x', 'y', 'z', "i'", "j'")] +
                   [("a'", '; no item of `(R363)`(7) names it; the hook refused the read agents’ seven calls before they ran'),
                    ("h'", '; repair (outbound), `(R363)`(7)(ii): the identifier read by its form, not its label'),
                    ('p', '; the navigator’s, lettered as the navigator’s (`(R363)`(7))'), ('q', '; the navigator’s, lettered as the navigator’s (`(R363)`(7))')])
C1_NOTES = ('Dated note, b753, to `(R363)`(2): the order of acts now stands as that clause words it -- this act the system refresh; then the sitting; then the class-number-3 walk of '
            '`(R363)`(4) and the build of T0 and T1; then sections 6 to 8, written from compiled statements -- superseding data/b752_amendments.json row 3 in that one place. '
            'b752’s entry (FINDINGS :%d) and trail (OPEN_TRAILS :%d) carry the sealed order and are not rewritten.' % (K.B711_ENTRY, K.B711_TRAIL),
            'Dated note, b753, to `(R363)`(3)(i): I-109’s entry (INSTRUMENTS :764) gains its cross-reference to I-106 and I-108 (:750, :758) and to data/b718_derivation.txt at the sitting, '
            'by an appended line in the instruments’ own form; no bank of b752 is rewritten.')
C1_CLASSES = (
    ('gitwrite', 'the one-call check that could not see the session’s git writes (`(R363)`-amendment (1), b753 defect (i))', 'the matcher of a run of the commit tool admits PowerShell’s quoted interpreter, which the quote-blanking left as `""`; a planted second write in one message refused by the check and by the hook, live once (relay ba46416f; data/b753_events.txt (2))'),
    ('subject', 'the subject read (`(R363)`(7)(i), widening data/b752_rules.txt (12))', 'tools/standing/subject.py runs the search from a ruling’s nouns over FINDINGS’ headings and INSTRUMENTS’ entry heads at HEAD, every uncited hit printed; (R362) replayed reaches the floor of six, the noun `class` not taking `classes`'),
    ('outbound', 'the outbound matcher (`(R363)`(7)(ii), defect (h’))', 'an identifier read by its form -- an ORCID’s, an address’s, the byline’s name as a value -- and not by a label word; b752’s three prompts 0, a planted number of the ORCID’s form 1'),
    ('chain', 'the answers route and the chain read (`(R363)`(7)(iii), events (6))', 'the answer of a put with no ordinary result row read from its api-request-blob row, marked with its line; the chain read prints every row naming an absent parent, a compaction boundary told apart; session 43048615’s nine rows reproduced, row 12892 a write lost'),
    ('halt', 'a halt priced from the exercise banks and the caps (`(R363)`(7)(iv), events (7), (8))', 'tools/standing/haltprice.py reads each arm a halt names in the act’s exercise banks and the face’s caps beside it; b752’s G-ANSWERS-BANKED in no part of ten, the root cap at its demand'),
    ('hold', 'the disk hold (`(R363)`(7)(vii))', 'every route refusing beneath the floor of 5,000 MB on either volume, and a restart pending read; the planted readings refused and read'),
    ('absent', 'the absent input (`(R363)`(7)(viii))', 'act_from() of the b644 route prints ABSENT for a session no file holds, where it returned a line beyond any file; the store read at step zero: the retention, the junction, the transcript by both paths, the harness’s version and the seat’s model beside it'),
    ('remote', 'a remote read that fails (`(R363)`(7)(ix), events (13))', 'the record’s git reader keeps the exit code and the error text; ls-remote against a name that does not resolve prints FAILED where b698’s reader returned no head'),
    ('version', 'the version', 'tools/standing/VERSION v1.33.0, landed by a commit of its own (relay %s) with its controls bank and the record’s dry over it, before the gate and before any outbound request; the store read’s model line added at relay 0f31d31d, the controls banked again' % C1_STANDING),
)


def _c1_lines(s):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr_, rn = _c1_read_counts(s)
    claims = [('(%d)' % k_) for k_ in sorted(s['events']) if s['tags'][k_][0] == 'CLAIM'] + [('(%s)' % x[0].replace("'", '’')) for x in s['defects'] if x[2] == 'CLAIM']
    m = re.search(r'CASES (\d+) ; AS WANTED (\d+)', s['v170_foot'])
    L = ['*b752’s events bank (relay data/b752_events.txt) carries thirteen rows, entered after its lock gate and not lettered, each tagged in its '
         'own bracket (%s); its defects bank thirty-six lettered rows, (a)-(j’), each tagged in its own bracket (%s); its refusal bank twenty-seven lines at %s, '
         'twenty-five recorded by a row and two entered below. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, '
         'where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them. '
         'The navigator’s two, (p) and (q), are lettered in the defects bank as the navigator’s; three items are entered beside the banks below.*' % (
             _c1_owners([s['tags'][k_][2] for k_ in s['events']]), _c1_owners([x[1] for x in s['defects']]), C1_REFUSAL_AT), '']
    L += ['**The repairs of `(R363)`(7) and of its amendment, at tools/standing/ v1.33.0, each with a control on b752’s banks or this act’s, failing on the route before the repair '
          'and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/%s, %s cases, AS WANTED %s):' % (C1_V170, m.group(1), m.group(2)), '']
    for k_, name, what in C1_CLASSES:
        L += ['**(%s) %s** -- %s (relay data/%s :%d).' % (k_, name, what, C1_V170, _c1_v170_line('### (%s)' % k_)), '']
    L += ['**b752’s events (1)-(13):**', '']
    for k_ in sorted(s['events']):
        t, r, o = s['tags'][k_]
        h = re.sub(r"^(THE SEAT'S|THE TOOL'S|THE TOOLS'|THE SCORE|THE RUNNER|THE HOST'S|THE HOST|THE NAVIGATOR'S|THE AUTHOR'S WORD|THE AUTHOR'S) \[[^\]]*\](, )?:? ?", '', s['events'][k_])
        h = re.sub(r'^(AFTER )?((about |read at |between )?(2026-11-\d\dT)?\d\d:\d\d(:\d\d)?Z( to \d\d:\d\dZ)?( and (again )?\d\d:\d\d(:\d\d)?Z)?)[:,] ', '', h)
        h = (h[:120].rsplit(' ', 1)[0] + ' …') if len(h) > 120 else h
        L += ['**(%d)** %s (relay data/b752_events.txt, row (%d); %s; %s; %s%s).' % (
            k_, _c1_q(h).replace("'", '’'), k_, o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(r), C1_EV_EXTRA.get(k_, ''))]
    L += ['', '**b752’s defects:**', '']
    for x, o, t, c, _tx in s['defects']:
        L += ['**(%s)** (relay data/b752_defects.txt; %s; %s; %s%s).' % (x.replace("'", '’'), o.lower().replace("'s", '’s'), t, _c1_col(c),
                                                                       C1_DF_EXTRA.get(x, '; no item of `(R363)`(7) names it'))]
    L += ['', '**Entered beside the banks by `(R363)`(1)-(3) and (7):**', '']
    for x, o, t, c, tx in C1_CARRIED:
        L += ['**%s** %s (%s; %s; %s).' % (x, _c1_q(tx).replace("'", '’'), o.lower().replace("'s", '’s').replace("'", '’'), t, _c1_col(c))]
    L += ['', '**b752’s refusals** (relay data/b752_hook_refusals.txt at %s, one a line): ' % C1_REFUSAL_AT + '; '.join(
        ':%d %s %s, recorded at %s' % (ln, kind, at, row.replace("'", '’')) for ln, kind, at, row in C1_REFUSALS) + '.', '',
          '**Dated notes:**', ''] + [x_ for nt_ in s['notes'] for x_ in (nt_, '')] + [
          '**The counter:** CLAIM %d, CLOSE %d, REPEAT %d of %d over the %d items as the banks tag them (thirteen events, thirty-six defects), as b752’s closing prints it (relay data/b752_closing.txt :5); '
          'with the %d entered beside them CLAIM %d, CLOSE %d, REPEAT %d of %d; no tag is read otherwise here; the CLAIM items of the banks %s.' % (nc, nl_, rep, n, n, len(C1_CARRIED), rc, rl_, rr_, rn, ', '.join(claims) or 'none'), '',
          '*Filed at b753 on the author’s ruling `(R363)`(7): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b753.py) from '
          'b752’s events and defects banks read unedited, its refusal bank and the v1.33.0 controls bank; banked as relay `data/b753_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at '
          'row (%d). It answers b752’s record; no sealed tool, face, trail or root-named bank of b752 is edited.*' % (C1_CORRIGENDA_LAST + 1)]
    return L


def _c1_bank(s, ln):
    nc, nl_, rep, n = _c1_counts(s)
    rc, rl_, rr_, rn = _c1_read_counts(s)
    return (['b753 -- THE CORRIGENDUM FOR b752, (R363)(7) (%s)' % utc(), '',
             '### the banks read unedited: data/b752_events.txt rows (1)-(13), data/b752_defects.txt 36 rows, data/b752_hook_refusals.txt 27 '
             'lines at %s; data/%s (the v1.33.0 controls); the corrigenda bank`s last row (%d).' % (C1_REFUSAL_AT, C1_V170, C1_CORRIGENDA_LAST), '']
            + ['  ' + l for l in _c1_lines(s)]
            + ['', '### ### **ITEMS %d: EVENTS 13, DEFECTS 36 ; CLAIM %d, CLOSE %d ; REPEAT %d ; WITH THE %d ENTERED %d: CLAIM %d, CLOSE %d ; REPEAT %d ; THE NAVIGATOR`S %d, LETTERED (p), (q) AND (R363)(3) ; DATED NOTES %d ; '
               'v1.33.0: THE ONE-CALL CHECK, THE SUBJECT READ, THE OUTBOUND MATCHER BY FORM, THE BLOB ANSWER AND THE CHAIN READ, THE HALT`S PRICE, THE DISK HOLD, THE ABSENT INPUT, '
               'THE FAILED REMOTE READ, THE VERSION ; THE ENTRY AT FINDINGS :%s.**' % (
                   n, nc, nl_, rep, len(C1_CARRIED), rn, rc, rl_, rr_, 2 + sum(1 for x in C1_CARRIED if x[1] == "THE NAVIGATOR'S"), len(s['notes']), ln)])


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: b752 at its weight after its entry, and the corrigendum for b752, landed through b698's guarded
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
        rc, rl_, rr_, rn = _c1_read_counts(s)
        put_txt('%s_corrigendum.txt' % ACT, _c1_bank(s, ln))
        put_json('%s_corrigendum.json' % ACT, dict(at=utc(), entry_line=ln, title=C1_CORR_TITLE, claim=nc, close=nl_, repeat=rep, items=n,
                                                   events=[dict(row=k_, owner=s['tags'][k_][2], tag=s['tags'][k_][0], column=s['tags'][k_][1]) for k_ in sorted(s['events'])],
                                                   entered=[dict(item=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in C1_CARRIED], flipped={},
                                                   with_entered=dict(claim=rc, close=rl_, repeat=rr_, items=rn),
                                                   defects=[dict(letter=x, owner=o, tag=t, column=c) for x, o, t, c, _tx in s['defects']],
                                                   lettered=[x[0] for x in s['defects']], records=[k_ for k_ in sorted(s['events'])],
                                                   notes=s['notes'], repairs=dict(version='v1.33.0', bank='data/' + C1_V170, commit=C1_STANDING),
                                                   row=C1_CORRIGENDA_LAST + 1))
        print('  CLAIM %d, CLOSE %d over %d ; REPEAT %d ; WITH THE %d ENTERED %d, %d over %d ; REPEAT %d ; NOTES %d ; FINDINGS :%s' % (nc, nl_, n, rep, len(C1_CARRIED), rc, rl_, rn, rr_, len(s['notes']), ln))
        return
    sys.exit('usage: fold.py record c1 weight | corrigendum  [dry | write]')
#⟪END⟫
# ### b753, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b753, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b753's name.
# ### b753's own changes are marked "b753, Component 3". The runner overrides read the act's dispatch rows: (R363)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b753_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R362)(7), as b752 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
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
    """N1, b753 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
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
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b753: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b753, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R363)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b752, naming tools/standing/hook.py, unedited this act (its last edit b752`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b753, C4, defect (n) (the Edit tool): the step-zero bank writes each deleted ref's tip as "(was 7d34b587)" (data/b753_stepzero.txt :44-:45),
# ### b752's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b752-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b753, Component 3 (the Edit tool): b753's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b752-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b753_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b753_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b753, Component 6 (the Edit tool): b753's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b752's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b753, Component 4 (the Edit tool): b752's overrides of checks 1516 and 1659 (hook.py edited by b752's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b753 as it stands
# ### b753, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b753_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b753, Component 4 (the Edit tool): the corrigendum's events rows (1)-(12), b752's twelve (the template's range is a fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 6)) \
#⟪END⟫
# ### b753, Component 4 (the Edit tool): b752's override of checks 1476-1482 (one ERRATA entry at b752's (R362)(5)) removed -- (R363)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b753 as it stands
# ### b753, Component 3 (the Edit tool): G-BRANCHES-DELETED over b753's two repositories (relay, PLACE-papers) and five
# ### refs; b753, Component 4, defect (m): the step-zero bank writes "KEPT as banked (" -- the seat's row at data/b753_stepzero.txt :43 and the
# ### tool's row (tools/standing/carry.py kept b753) in its dated note -- read in its own wording, the tool's row asked by its own head
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707' in z and 'KEPT as banked (the tool`s row, tools/standing/carry.py kept b753' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b753, Component 4 (the Edit tool): G-RUNNER-READ's plant on b753's dispatch rows -- run 2's axiom lines carrying sorryAx (b752's
# ### plant read the lv rows' closure log, which b753 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b753, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b753, Component 6 (the Edit tool): the fold bank was b752's own route
# ### (tools/b752_fold.py); b753's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b753_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b752.py -> tools/acts/b753.py' in (rd('b753_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b753, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b753_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b753, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b753_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b753_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b753, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R363): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R363)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b753')
    return '### THE COUNTER ((R363) Component 5, the act`s events and defects together; relay data/b753_defects.txt, data/b753_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b752, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b753 (defect (d')): the order's
# ### state as b753 leaves it -- the carry from b752 said "as b752 left it ... not touched this act", where b753 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act; W-ORD-MECHANISM-ATTRIBUTION open, its plan passed at [P1] (relay data/b753_attribution_plan.txt), its build an act the author names, fourth;',
    '        W-ORD-LI-ARITH, W-ORD-ZQ-FAMILY, W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b753, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)
#⟪END⟫
# ### b753, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b752's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b753_author_answers.txt', 'b753_answer_check.txt', 'b753_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b753, Component 4's probe: v1.27.0's rdn (repair (7)) refuses a missing file, and _counter (record.tpl :2315) reads the events bank,
# ### which the close writes after the seal; read optional for the events bank alone, the defects bank still refused if missing
#⟪OVERRIDE record MARK 26666a71fb1e 1 REPAIR (reader)⟫
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
#⟪END⟫
# ### b753, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b752's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b753, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b752's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b753_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b753_registration_%s.txt' % __import__('b753_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b753, Component 4 (the Edit tool, before the face): b752's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b753, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b753's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b753, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R363)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b753 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b753_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b753: the controls' one route (N1)
#⟪END⟫
# ### b753, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b752's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b753 scorer reads; the needles set to the banks b753's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b753, (R363)(2)(iii): b752's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b753, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b753_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b753: b752's override of G-DIFFERS-ERRATA (two ERRATA entries at its sitting) retired; b753 writes no ERRATA entry ((R363)(6)), so
# ### the template's arm, ERRATA at HEAD byte-equal to its blob at the act's base, reads b753 as it stands
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'pq' else 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) of data/b753_defects.txt, the navigator's (p) and (q), the rest the seat's; the primed rows (a')-(c') read by the counter, not by this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b753_corrigendum.txt', 'data/b753_standing_v1320.txt', 'data/b753_rules.txt', 'data/b753_crossref.txt', 'data/b753_cq_signature.txt',
                  'data/b753_statements.txt', 'data/b753_attribution_plan.txt', 'data/b753_put_1.json', 'data/b753_author_answers.txt', 'data/b753_line.txt',
                  'data/b753_pathrefusal.txt', 'data/b753_reproduce.txt', 'data/b753_reproduce.json', 'data/b753_address_scan.txt', 'data/b753_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b753 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R363)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b753_address_scan.py'), 'scan'], capture_output=True, text=True,
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


def _draft_of(t):
    """(R363)(2): the section bank's draft, the lines between `## THE DRAFT BEGIN` and `## THE DRAFT END`, its blank edge lines cut;
    pure in its argument."""
    ls = (t or '').replace(chr(13), '').split(NL)
    try:
        a, b = ls.index('## THE DRAFT BEGIN'), ls.index('## THE DRAFT END')
    except ValueError:
        return []
    d = ls[a + 1:b]
    while d and not d[0].strip():
        d = d[1:]
    while d and not d[-1].strip():
        d = d[:-1]
    return d


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R363)(1)-(7) (b753's keys over b753's objects): the order by time and ancestry; v1.32.0's controls; the cross-reference, the
        # ### generator, the control and the statements; the plan, the put bank and the answers; the line bank; zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b752's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('v9_v1310', K.STANDING_COMMIT, K.C1_STANDING), ('v1310_corr', K.C1_STANDING, K.C1_CORR),
                                 ('corr_xref', K.C1_CORR, K.C2_PLAN_FIRST), ('xref_gen', K.C2_PLAN_FIRST, K.C2_RELAY_ALL[1]),
                                 ('gen_sig', K.C2_RELAY_ALL[1], K.C2_RELAY_ALL[2]), ('sig_stm', K.C2_RELAY_ALL[2], K.C2_RELAY),
                                 ('stm_plan', K.C2_RELAY, K.C3_RELAY[0]), ('plan_ans', K.C3_RELAY[0], K.C3_RELAY[1]),
                                 ('ans_line', K.C3_RELAY[1], K.C4_LINE))),
        # ### b753 (R363)(1): PLACE-papers by ancestry -- the weight and corrigendum on the act's base, HEAD on them; its commits since the base
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('pre_c1', K.PRE_PP, K.C1_PP), ('c1_head', K.C1_PP, 'HEAD'))),
        pp_log=[l for l in gs(PP, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_PP).split() if l.strip()],
        v1130=rd('b753_standing_v1320.txt'), v1281=None,
        xref=rd('b753_crossref.txt'), xref_blob=_s(blob(ROOT, '%s:data/b753_crossref.txt' % K.C2_PLAN_FIRST)),
        sig=rd('b753_cq_signature.txt'), sig_blob=_s(blob(ROOT, '%s:data/b753_cq_signature.txt' % K.C2_RELAY_ALL[2])),
        gen_at=_s(blob(ROOT, '%s:tools/b753_cq_signature.py' % K.C2_RELAY_ALL[1])), gen_head=_s(blob(ROOT, 'HEAD:tools/b753_cq_signature.py')),
        gen_first=[h_ for h_ in gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', 'tools/b753_cq_signature.py').split() if h_.strip()][-1:],
        gen_full=gs(ROOT, 'rev-parse', K.C2_RELAY_ALL[1]).strip(),
        stm=rd('b753_statements.txt'), stm_blob=_s(blob(ROOT, '%s:data/b753_statements.txt' % K.C2_RELAY)),
        plan=rd('b753_attribution_plan.txt'), plan_blob=_s(blob(ROOT, '%s:%s' % (K.C3_RELAY[0], K.SECTION_BANK))), putj=jl('b753_put_1.json'),
        rows_bank=rd('b753_line.txt'), zanswers=rd('b753_author_answers.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP,)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP,)),
        numstat={},
        c3_blobs=dict((p_, _s(blob(ROOT, '%s:%s' % (K.C4_LINE, p_)))) for p_ in ('data/b753_line.txt', 'tools/b753_line.py')),
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
        drows=json.loads(rd('b753_dispatch_rows.json') or '[]'), reproduce=rd('b753_reproduce.txt'), reproducej=jl('b753_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b753_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b752 left them
        rebuild=None, rebuild_rows=json.loads(rd('b753_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), standing=_ct(ROOT, K.C1_STANDING), corr=_ct(ROOT, K.C1_CORR),
               xref=_ct(ROOT, K.C2_PLAN_FIRST), gen=_ct(ROOT, K.C2_RELAY_ALL[1]), sig=_ct(ROOT, K.C2_RELAY_ALL[2]), stm=_ct(ROOT, K.C2_RELAY),
               plan=_ct(ROOT, K.C3_RELAY[0]), ans=_ct(ROOT, K.C3_RELAY[1]), line=_ct(ROOT, K.C4_LINE),
               v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), xref=files_of(ROOT, K.C2_PLAN_FIRST), gen=files_of(ROOT, K.C2_RELAY_ALL[1]),
                   sig=files_of(ROOT, K.C2_RELAY_ALL[2]), s2=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY[0]), ans=files_of(ROOT, K.C3_RELAY[1]),
                   line=files_of(ROOT, K.C4_LINE), c1pp_=files_of(PP, K.C1_PP),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b753's read-first bank's items by path, (R363)'s read-first list in its order (data/b753_readfirst_rows.json); b753 step zero: the
# ### carried b752 needles (R7 refused 9) replaced
READFIRST_NEEDLES = (
    'relay data/b752_closing.txt |',
    'relay data/b752_events.txt |',
    'relay data/b752_defects.txt |',
    'relay data/b752_author_answers.txt |',
    'relay data/b752_amendments.json |',
    'relay data/b752_rules.txt |',
    'relay data/b752_crossref.txt |',
    'relay data/b752_attribution_plan.txt |',
    'relay data/b752_cq_signature.txt |',
    'relay data/b752_line.txt |',
    'relay data/b752_census_closing.txt |',
    'relay data/b752_pins_closing.txt |',
    'relay data/b752_kernels_face.json |',
    'relay data/repo_visibility.txt |',
    'relay HANDOFF.md, tools/b307_handoff_census.py |',
    'relay tools/b303_pins.py |',
    'relay tools/act_root.py |',
    'relay tools/b610_census.py, tools/b619_census.py, tools/b633_census.py, data/b638_census.txt |',
    'relay tools/mirror_roster.json, tools/standing/roster.py |',
    'relay data/b715_rules.txt, data/b715_roster.txt |',
    'relay data/b711_coeffs.txt |',
    'relay data/b718_derivation.txt, data/b720_derivation.txt, data/b721_derivation.txt |',
    'relay data/b721_registrations.txt |',
    'relay data/b722_walk.txt |',
    'relay data/b723_c2_closed_form.txt, data/b723_registrations.txt |',
    'relay data/b750_cq_sign.txt |',
    'relay data/b724_split_price.txt |',
    'relay data/b726_frontdoors.txt, data/b732_phase2_frontdoors.txt |',
    'relay data/b727_sitting.txt, data/b736_sitting.txt |',
    'PLACE-papers OPEN_TRAILS.md |',
    'PLACE-papers FINDINGS.md |',
    'PLACE-papers REGISTRY.md |',
    'PLACE-papers ERRATA.md |',
    'PLACE-papers INSTRUMENTS.md |',
    'PLACE-papers the census at v0.8.3 |',
    'PLACE-papers README.md |',
    'SIDE-explicit-formula at main 8fbab45d, README.md |',
    'SIDE-explicit-formula at c2-b725 (0395f15d), SIDEExplicitFormula/C2Walk.lean, SIDEExplicitFormula/C2Theorem.lean |',
    'SIDE-explicit-formula at zq-b730 (1e658870), SIDEExplicitFormula/Schema/EpsteinZQ.lean, SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean |',
    'relay tools/standing/hold.py, tools/standing/scratchfsck.py, tools/standing/harnessmoves.py |',
    'relay tools/standing/routes/b644_record.py, tools/b597_record.py, tools/b672_citation.py, tools/b698_record.py |',
    'relay tools/standing/repeat.py, tools/b752_worklist.py, tools/standing/hook.py |',
    'relay tools/standing/v1160.py, tools/standing/v1170.py, data/b738_dispatch_rows.json |',
)
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R363)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'CROSS-REFERENCE, CONTROL AND STATEMENTS ((R363)(3)-(5))', 'PLAN ((R363)(6))', 'LINE (Component 4)', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (156 = 156 + 0, data/b753_citation_check.txt :170), no miss; the
    check HALTED on one Lean-path row (:171), that row read in the step-zero bank (data/b753_stepzero.txt :63-:69, b736's form: MechanismClass
    an inductive at Bridge/TheBridgeComplete.lean :20, the reader's pattern carrying no inductive arm, no word of the ruling wrong); the bank
    written before the step-zero banks' commit and that commit before Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 156 \
        and '### ### **THE CHECK HALTED** (halts 1: Lean paths and nouns 1, comparatives 0)' in c \
        and '## THE ONE HALT ROW OF THE CITATION CHECK, READ' in (S['stepz'] or '') and 'Bridge/TheBridgeComplete.lean :20' in (S['stepz'] or '') \
#⟪END⟫
# ### b753, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b752's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b753, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R363)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b752()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R363)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b753_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b752's figures, read at FINDINGS :14785 as Component 1 landed them (b752's closing head quoted)
    return landed(S, 0, ['b752 AT ITS WEIGHT', 'suite 111 of 116', 'd0d963dd', '22 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b753's title, the ferry's Component 4 result sentence adjusted to what the act did (the record tool's _title over the banks)
TITLE_NEEDLES = ('## W-ORD-MECHANISM-ATTRIBUTION’s plan passed at [P1] (b753_attribution_plan): T0-T3 priced, T0 then T1 recommended',
                 'the class-group signature of cQ’s negative n (b753_cq_signature): 102, 0, 320, 79, the statement TRUE',
                 'the kernel’s classes read as an enumeration',
                 'six questions cross-referenced, held 3, candidates 3, none entered (b753_crossref)',
                 'nothing built')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R363)(1), (7): the generated entry for b752's five events and twenty-two defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(5), the defects by the one lettering (a)-(v); every item tagged CLAIM or CLOSE and NEW or
    REPEAT, the tags summing (CLAIM 10, CLOSE 17 over 27, REPEAT 14; the three entered beside them, the navigator's correction and the
    amendment's defect among them); the repairs at tools/standing/ v1.32.0 by their controls bank; the corrigenda bank appended at row (72)
    and nothing before it changed; in Component 1's commits (the figures read from data/b753_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 22 and len(items) == j.get('items') == 27 and j.get('row') == 72 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 27 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 10 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 14 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.32.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 and len(j.get('entered') or []) == 3 \
        and '  (72) ' in S['corrigenda'] and '  (73) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R363)(7) orders the rules bank data/b753_rules.txt, one row per repair and the navigator's search rule, twelve rows (1)-(12); a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here first committed with v1.32.0 (C1_RULES), in no other commit."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', S['rules'] or '')] == list(range(1, 13)) and 'data/b753_rules.txt' in S['files']['rules'] \
        and sorted(gs(ROOT, 'log', '--format=%H', '--', 'data/b753_rules.txt').split()) == sorted(gs(ROOT, 'rev-parse', K.C1_RULES).split()) \
#⟪END⟫
#⟪SECTION checks 23⟫
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.32.0', 'REGISTERED -- THE CROSS-REFERENCE', 'REGISTERED -- THE SIGNATURE CONTROL', 'REGISTERED -- THE STATEMENTS',
               'REGISTERED -- THE PLAN', 'REGISTERED -- THE INTEGRATION LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b753: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b753, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b753_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b753, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail), the ledgers changed; no rename; no paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b753's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The cross-reference**', '**The class-group signature**', '**The statements**',
                 '**The integration line**', '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b753_corrigendum.txt', 'data/b753_standing_v1320.txt', 'data/b753_rules.txt', 'data/b753_crossref.txt', 'data/b753_cq_signature.txt',
                 'data/b753_statements.txt', 'data/b753_attribution_plan.txt', 'data/b753_author_answers.txt', 'data/b753_line.txt',
                 'data/b753_reproduce.txt', 'data/b753_address_scan.txt', 'data/b753_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ('p', 'q')   # ### b753: the navigator's rows of the defects bank, (p) (the orders reader's words) and (q) (W-ORD-PLATT-RUNG's reading); the rest the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R363)(1), N2, N5 (the name the frozen run list carries): the PLACE-papers writes in their order -- the weight and corrigendum in a
    commit touching FINDINGS alone in one hunk, its first two added lines b752 at its weight ("*Appended 2026-11-10 by b753 to b752’s entry")
    and the corrigendum's heading ("## Corrigendum to b752’s record"), removing none, the first PLACE-papers commit of the act on its base;
    no other PLACE-papers write before the record (Components 2-4 write the relay alone), the changed files within FINDINGS and OPEN_TRAILS;
    the plans of b744 unedited at their step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    dd_ = S['disch_diff'] or {}
    a0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    r0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('-') and not l.startswith('---')]
    hunks_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(a0_) >= 2 and len(hunks_) == 1 and a0_[0].startswith('+*Appended 2026-11-10 by b753 to b752’s entry') \
        and a0_[1].startswith('+## Corrigendum to b752’s record') and r0_ == []
    first_ = bool(S['pp_log']) and S['pp_log'][0].startswith(K.C1_PP)
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    return bool(one_) and S['reg_pp'].get(K.C1_PP) == ['FINDINGS.md'] and first_ and set(S['pp_head_files']) <= set(K.PP_WRITTEN) and md_ \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b753_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R363)(1)-(7), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, v1.32.0, the weight and
    corrigendum (PLACE-papers, then relay), the cross-reference, the generator, the control's bank, the statements, the plan, the answers on
    [P1]'s pass, the line; by ancestry within the relay from v9 through each of them to the line."""
    t_ = S['t']
    ks_ = ('stepzero', 'standing', 'c1pp', 'corr', 'xref', 'gen', 'sig', 'stm', 'plan', 'ans', 'line')
    return all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) and t_['gen'] < t_['sig'] \
        and bool(S['anc']) and len(S['anc']) == 9 and all(v is True for v in S['anc'].values())
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R363)(3)-(5), N2, N3 (the name the frozen run list carries): the cross-reference, the control and the statements -- each bank at HEAD
    its blob at its own commit (f72c243f, 8c0b6206, acce556a), none of those commits carrying the plan; the generator
    tools/b753_cq_signature.py first added at cfa40193, alone of its bank, and at HEAD its blob there; the control's foot CONTROL AS WANTED
    with b750's figures, the table's four cells 102/0/320/79, THE STATEMENT TRUE, THE REVERSE FALSE, type mismatches 0; the cross-reference's
    foot QUESTIONS 6, HELD 3, CANDIDATES 3, NO ORDER ENTERED; the statements' foot naming no predicate on functions among the seven, the census
    standing and dh_witness SHELL; the four commits in that order by time and before the plan's."""
    return _c2_ok(S)


# ### the record section's INTEGRATION_LINE, the same bytes (the checks and the record are separate modules; G-COUNT-ROUTE-PRICED reads the line
# ### bank against it, and the record's entry ends with it)
_INTEG_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
               'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


SIG_FOOT = ('THE SIGNATURE, n <= 3000: CONTROL AS WANTED (negative 102, smallest 48, exactly zero 2498, nonnegative 399) ; PRIMES 430: R 1, I 217, P 67, N 145 ; '
            'TYPE MISMATCHES 0, THIRD WAY 0 ; THE TABLE (neg & N 102, neg & no N 0, pos & N 320, pos & no N 79) ; THE STATEMENT TRUE ; THE REVERSE FALSE ')
XREF_FOOT = 'THE CROSS-REFERENCE: QUESTIONS 6 ; HELD 3 ; CANDIDATES 3 ; CITES NOT MATCHED 1 ; NO ORDER ENTERED.'
P1_ANSWER = 'BEGINPass [P1]. The build of T0 then T1, with T2 and T3 printed, is an act I will name after the system refresh'


def _c2_ok(S):
    x_, s_, m_ = _txt(S['xref']), _txt(S['sig']), _txt(S['stm'])
    t_ = S['t']
    fs_ = S['files']
    blobs_ = bool(x_) and bool(s_) and bool(m_) and x_ == _txt(S['xref_blob']) and s_ == _txt(S['sig_blob']) and m_ == _txt(S['stm_blob'])
    alone_ = 'data/b753_crossref.txt' in fs_['xref'] and fs_['gen'] and 'tools/b753_cq_signature.py' in fs_['gen'] \
        and 'data/b753_cq_signature.txt' not in fs_['gen'] and 'data/b753_cq_signature.txt' in fs_['sig'] and 'tools/b753_cq_signature.py' not in fs_['sig'] \
        and 'data/b753_statements.txt' in fs_['s2'] and not any(K.SECTION_BANK in fs_[k_] for k_ in ('xref', 'gen', 'sig', 's2'))
    gen_ = bool(S['gen_first']) and S['gen_first'][0] == S['gen_full'] and bool(S['gen_at']) and S['gen_at'] == S['gen_head']
    sv_, xv_, mv_ = _vlast(s_), _vlast(x_), _vlast(m_)
    feet_ = sv_.startswith(SIG_FOOT) and xv_ == XREF_FOOT and 'NONE OF THE SEVEN HAS A PREDICATE ON FUNCTIONS' in mv_ \
        and 'THE CENSUS STANDS AT THE TREE FOR ALL SEVEN' in mv_ and 'dh_witness SHELL' in mv_
    order_ = all(t_.get(k_) for k_ in ('xref', 'gen', 'sig', 'stm', 'plan')) and t_['xref'] <= t_['gen'] < t_['sig'] <= t_['stm'] <= t_['plan']
    return blobs_ and alone_ and gen_ and feet_ and order_
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R363)(6) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b752 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b752's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
    worklist's and its peel 14ca5725, the only tag at that commit and no tag added this act; no sitting kernel."""
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
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.32.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1310') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b752's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R363)(6), Component 4, N2, N3, N5 (the name the frozen run list carries): the plan and its answer, and the line -- the plan bank at
    HEAD its blob at b81002b8, its foot recommending T0 then T1, the build fourth, B3 standing, nothing built; the put bank naming [P1]; the
    answers bank written by the record tool's appending route (its head the route's, the [P1] prompt with its options and the RESULT row with
    its time, the author's word Pass [P1] verbatim), committed at 9218d7d3 with its json and the put bank, at HEAD its blob there or that blob
    with lines appended (never rewritten); the line bank's foot COMPOSED WITH THE MATCH, STAGE CLUSTERED, MATCHED 0 OF 4, ALL AS READ, its line
    the act module's INTEGRATION line, committed with its tool at 49e3a3cd; b746's draft unchanged; no Zenodo tool this act."""
    r_ = S['rows_bank'] or ''
    v_ = _vlast(r_)
    a_ = _txt(S['zanswers'])
    a3_ = _txt(blob(ROOT, '%s:data/b753_author_answers.txt' % K.C3_RELAY[1]))
    p1row_ = re.search(r'(?m)^RESULT \(transcript line \d+, 2026-11-11T00:02:48\.817Z\): The user answered: "\[P1\] ', a_)
    pl_ = _txt(S['plan'])
    pv_ = _vlast(pl_)
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b753_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return a_.startswith('### b753 -- THE AUTHOR`S ANSWERS') and bool(a3_) and a_.startswith(a3_) and P1_ANSWER in a_ and p1row_ is not None \
        and 'OPTION 1: Pass [P1] ::' in a_ and 'OPTION 2: Strike [P1] ::' in a_ \
        and bool(pl_) and pl_ == _txt(S['plan_blob']) and 'RECOMMENDED: BUILD T0 (40-120 LINES) THEN T1 (150-450)' in pv_ \
        and 'THE BUILD FOURTH' in pv_ and 'B3 STANDS' in pv_ and pv_.endswith('NOTHING BUILT.') and '[P1]' in json.dumps(S['putj'] or {}, ensure_ascii=False) \
        and K.SECTION_BANK in S['files']['c3'] and {'data/b753_author_answers.txt', 'data/b753_author_answers.json', 'data/b753_put_1.json'} <= set(S['files']['ans']) \
        and {'data/b753_line.txt', 'tools/b753_line.py'} <= set(S['files']['line']) \
        and v_.startswith('THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; STAGE CLUSTERED ; MATCHED 0 OF 4 ;') \
        and v_.endswith('; ALL AS READ.') and ('      %s' % _INTEG_LINE) in r_ \
        and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []

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
    """standing clauses v9 (Component 7 of (R363): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b753_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b752's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R363-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b752's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R363) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b752's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R362)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base d921bceb',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 156 = 156 OK + 0 misses, the check HALTED on one Lean-path row (MechanismClass, an inductive) read in the step-zero bank (b736`s form); the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b752-\w+) \((?:was )?[0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 result sentence adjusted to what the act did: the plan passed at [P1], T0-T3 priced, T0 then T1 recommended; the signature`s four cells and the statement TRUE; the classes read as an enumeration, the graded rows counted; six questions, held 3, candidates 3, none entered; the controls landed; nothing built; each finding`s name in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R363)(1), (7): the generated corrigendum for b752`s record, landed at FINDINGS :14787: its five events and twenty-two defects, 27 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 10 CLOSE 17, REPEAT 14, with the three entered beside them; v1.32.0`s repairs by data/b753_standing_v1320.txt; the corrigenda bank appended at row (72)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R363)(7)`s rules bank data/b753_rules.txt, twelve rows (1)-(12), committed with v1.32.0 (7b20ff6b) alone',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b753's objects
    ('G-REGISTRATIONS-FIRST', '(R363)(1), N2, N5: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (0732cb56), one hunk, none removed, the act`s first PLACE-papers commit; no other PLACE-papers write before the record, the changed files within FINDINGS and OPEN_TRAILS; b744`s plans at their md5s; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('REGISTRY.md'))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b753_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R363)(1)-(7), N2: the act`s order by time -- step zero, v1.32.0, the weight and corrigendum, the cross-reference, the generator, the control, the statements, the plan, the answers, the line -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(gen_sig=False))),
    ('G-DERIVATION-GRADED', '(R363)(3)-(5), N2, N3: the cross-reference, the control and the statements each at HEAD its blob at its commit (f72c243f, 8c0b6206, acce556a); the generator first added alone at cfa40193 before the control and unchanged since; the control`s foot CONTROL AS WANTED, the table 102/0/320/79, THE STATEMENT TRUE, THE REVERSE FALSE, mismatches 0; the cross-reference`s foot 6 questions, held 3, candidates 3, no order entered; the statements` foot no predicate on functions among the seven, dh_witness SHELL',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'sig', (S['sig'] or '').replace('THE STATEMENT TRUE', 'THE STATEMENT FALSE'))),
    ('G-OFFSET-POST-HOC', 'N5, (R363)(10): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.32.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R363)(6), Component 4, N2, N3, N5: the plan bank its blob at b81002b8, its foot recommending T0 then T1, the build fourth, nothing built; the put bank naming [P1]; the answers bank by the record tool`s appending route, the [P1] prompt with its two options and its RESULT at 2026-11-11T00:02:48.817Z, the author`s word Pass [P1] verbatim, at HEAD its blob at 9218d7d3 with lines appended alone; the line bank COMPOSED WITH THE MATCH, stage CLUSTERED, 0 of 4 matched, ALL AS READ, its line the module`s, with its tool at 49e3a3cd; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'zanswers', (S['zanswers'] or '').replace('BEGINPass [P1].', 'BEGINStrike [P1].'))),
    ('G-DIFFERS-ERRATA', '(R363)(1), (10): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line and the corrigendum in 0732cb56, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b753_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R363-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b752`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b752 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b752 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS and OPEN_TRAILS, (R363)(1), (7), (10)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b752`s trail record on OPEN_TRAILS (:18184) and its root in the chain', lambda S: '### b752 — lane two, act one hundred and seventy-nine, the attribution plan under (R362)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b753 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b752's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b753: (R363)'s rows, written at step zero over b752's carried rows (scratch splice753.py); each needle read from the line it names
    # ### before the row was written (scratch cites753.py, trees753.py, rows753.py); (1)'s line read from the public relay at 0e855242
    pub = _blob('D:/relay', '0e855242', 'data/b752_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b752_closing.txt :1, the head line as the public relay carries it at 0e855242', bool(pub) and pub[0] == at(cl, 1) and 'relay 93ebe458' in pub[0] and 'PLACE-papers 4db2fc1' in pub[0],
        'remote main %s' % rm[:8], '1')
    add('ruling (1)', 'relay remote main read back at 0e855242 after b752`s closing push and its step-row commit', rm.startswith('0e855242'), rm[:8], '1')
    for w_ in ('suite 112 of 116', 'root 38eb76523c8cd050', '2 prompts answered', 'scores 7 of 8 HELD', '36 defects'):
        add('ruling (1)', 'data/b752_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, 0e855242 and 4db2fc1', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('0e855242') and gr(PP, 'rev-parse', K.PRE_PP).startswith('4db2fc1'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    for f_, n_, ws_ in (('data/b752_corrigendum.txt', 84, ('ITEMS 27: EVENTS 5, DEFECTS 22', 'WITH THE 3 ENTERED 30')),
                        ('data/b752_standing_v1320.txt', 211, ('v1.32.0: CONTROLS', 'CASES 47 ; AS WANTED 47')),
                        ('data/b752_crossref.txt', 107, ('QUESTIONS 6 ; HELD 3 ; CANDIDATES 3',)),
                        ('data/b752_cq_signature.txt', 166, ('negative 102, smallest 48', 'neg & N 102, neg & no N 0, pos & N 320, pos & no N 79')),
                        ('data/b752_statements.txt', 1431, ('### ### **THE STATEMENTS:',)),
                        ('data/b752_attribution_plan.txt', 103, ('[P1] THE ATTRIBUTION PLAN', 'BUILD T0 (40-120 LINES) THEN T1 (150-450)')),
                        ('data/b752_line.txt', 54, ('STAGE CLUSTERED', 'MATCHED 0 OF 4')),
                        ('data/b752_closing.txt', 311, ('pre-push : ARMS RUN : 116', 'LIVE PASSING : 112', "['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH']")),
                        ('data/b752_closing.txt', 313, ('post-push : ARMS RUN : 116', 'LIVE PASSING : 112', "['G-AXIOM-CLAIM', 'G-RULE-POSTSEAL-READ', 'G-DELETES-ONE-BRANCH']"))):
        L_ = lines_of(p(*f_.split('/')))
        add('ruling (1)', '%s :%d, %s' % (f_, n_, ' ; '.join(ws_)), all(w_ in at(L_, n_) for w_ in ws_), at(L_, n_)[:60], '1')
    an1_ = lines_of(p('data', 'b752_author_answers.txt'))
    add('ruling (1)', 'data/b752_author_answers.txt :7, the plan passed at [P1] (00:02:48.817Z)', '00:02:48.817Z' in at(an1_, 7) and '[P1]' in at(an1_, 7), at(an1_, 7)[:60], '1')
    add('ruling (2), ferry (read first)', 'data/b752_author_answers.txt :67, the root`s prompt: NO RESULT', at(an1_, 67).startswith('RESULT (transcript line None, None)') and 'NO RESULT' in at(an1_, 67), at(an1_, 67)[:60], '1')
    add('ruling (2), ferry (read first)', 'data/b752_author_answers.txt :64-:66, the root`s prompt and its two options', at(an1_, 64).startswith('### PROMPT 1 (Next act)') and 'Confirmed: refresh next' in at(an1_, 65) and 'Renamed: sitting next' in at(an1_, 66), at(an1_, 64)[:60], '1')
    ev1_ = lines_of(p('data', 'b752_events.txt'))
    evt_ = {}
    for l_ in ev1_:
        m_ = re.match(r'^    \((\d+)\) ', l_)
        if m_:
            k_ = int(m_.group(1))
            evt_[k_] = l_
        elif l_.startswith('     ') and evt_:
            evt_[max(evt_)] += ' ' + l_.strip()
    for k_, ws_ in ((6, ('api-request-blob row (line 11286)', 'NO RESULT', 'tools/b698_record.py :315')), (7, ('route 1 was taken', 'cap 1')),
                    (11, ('composed from the sealed worklist', 'the class-number-3 walk')), (13, ('HEAD NOT THE REMOTE MAIN', 'One retry', 'tools/standing/repeat.py :272-:274'))):
        add('ruling (1), (2), (7), ferry (read first)', 'data/b752_events.txt (%d), %s' % (k_, ' ; '.join(ws_)), all(w_ in evt_.get(k_, '') for w_ in ws_), evt_.get(k_, 'ABSENT')[:60], '1')
    add('ruling (2), ferry (read first)', 'OPEN_TRAILS.md :18230, b752`s Next carrying the sealed order (the refresh, then the sitting, then sections 6-8, then the build)',
        at(ot, 18230).startswith('**Next:** the system refresh (b753)') and 'then the sitting, then sections 6-8' in at(ot, 18230), at(ot, 18230)[:60], '1')
    am_ = json.loads(rd(p('data', 'b752_amendments.json')) or '{}')
    amr_ = am_.get('rows') if isinstance(am_, dict) else am_
    add('ruling (2), ferry (read first)', 'data/b752_amendments.json row 3 (23:17:48.178Z, transcript line 6121), the order it gives', bool(amr_) and len(amr_) == 3 and amr_[2].get('at') == '2026-11-10T23:17:48.178Z' and amr_[2].get('transcript_line') == 6121,
        (amr_[2].get('at') if amr_ and len(amr_) > 2 else 'ABSENT'), '1')
    # ### (R363)(3): the navigator's correction -- the coefficient record and H-DIAL, each line read at HEAD
    co_ = lines_of(p('data', 'b711_coeffs.txt'))
    add('ruling (3)(i), ferry (read first)', 'data/b711_coeffs.txt :12, the least n with c(n) < 0: n = 48', 'THE LEAST n WITH c(n) < 0: n = 48' in at(co_, 12), at(co_, 12)[:60], '1')
    for n_, nd_ in ((10858, '## The coefficient law derived to the step named'), (11072, '## The coefficient law at -35 and -40'), (11178, '## The C2 table’s rule chose no discriminant'),
                    (11359, '## The class-number-2 table at its fourteen remaining fields'), (11490, '## The close tools at v1.3.0'), (11755, '## H-ONSET-MASS at 1 of 3 zeros REFUTED'),
                    (12216, '## The C2 theorem compiled at 18 of 18')):
        add('ruling (3), ferry (read first)', 'FINDINGS.md :%d, %s' % (n_, nd_.lstrip('# ')[:50]), at(fi, n_).startswith(nd_), at(fi, n_)[:60], '1')
    add('ruling (3)(i)', 'FINDINGS.md :11359, -31: n0 80, HELD', '-31 and -55: n0 80 and 224, HELD' in at(fi, 11359), 'read', '1')
    add('ruling (3)(i)', 'FINDINGS.md :11490, the C2 closed form written and checked post hoc', 'the C2 closed form written and checked post hoc' in at(fi, 11490), 'read', '1')
    add('ruling (3)(ii)', 'FINDINGS.md :11755, H-DIAL at c = 0.6, 0.8, 1.0 REFUTED', 'H-DIAL at c = 0.6, 0.8, 1.0 REFUTED' in at(fi, 11755), 'read', '1')
    r723_ = lines_of(p('data', 'b723_registrations.txt'))
    add('ruling (3)(ii), ferry (read first)', 'data/b723_registrations.txt :52-:53, H-DIAL: F_c(s) = zeta(s) zeta(s - c)', at(r723_, 52).startswith('## (iii) H-DIAL') and 'F_c(s) = zeta(s) zeta(s - c)' in at(r723_, 53), at(r723_, 53)[:60], '1')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    for n_, nd_ in ((750, '## I-106'), (758, '## I-108'), (764, '## I-109')):
        add('ruling (3)(i), ferry (read first)', 'INSTRUMENTS.md :%d, %s' % (n_, nd_[3:]), at(ins_, n_).startswith(nd_), at(ins_, n_)[:40], '1')
    pl_ = lines_of(p('data', 'b752_attribution_plan.txt'))
    add('ruling (3)(i), ferry (read first)', 'data/b752_attribution_plan.txt :24-:27, the plan`s (1c), read at h = 3 POST HOC', at(pl_, 24).lstrip().startswith('(1c)') and 'POST HOC' in at(pl_, 27), at(pl_, 24)[:60], '1')
    for f_ in ('data/b718_derivation.txt', 'data/b720_derivation.txt', 'data/b721_derivation.txt', 'data/b721_registrations.txt', 'data/b722_walk.txt', 'data/b723_c2_closed_form.txt'):
        add('ruling (3), (4), ferry (read first)', '%s tracked at 0e855242' % f_, bool(_blob('D:/relay', '0e855242', f_)), '%d lines' % len(_blob('D:/relay', '0e855242', f_).split(NL)), '1')
    # ### (R363)(4): the registration's control and its route's tools
    cq0_ = lines_of(p('data', 'b750_cq_sign.txt'))
    add('ruling (4), ferry (read first)', 'data/b750_cq_sign.txt :39, NEGATIVE 102, THE SMALLEST NEGATIVE n = 48, EXACTLY ZERO 2498, NONNEGATIVE 399',
        all(w_ in at(cq0_, 39) for w_ in ('NEGATIVE 102', 'THE SMALLEST NEGATIVE n = 48', 'EXACTLY ZERO 2498', 'NONNEGATIVE 399')), at(cq0_, 39)[:60], '2')
    for f_ in ('tools/b718_abstract.py', 'tools/b720_predict.py'):
        add('ruling (4)', '%s tracked (the group-ring model, FORCED and no test)' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)), gr('D:/relay', 'log', '-1', '--format=%h', '--', f_) or 'ABSENT', '2')
    # ### (R363)(5): the trees and the ledger lines the reads compare
    EF_ = 'D:/SIDE-explicit-formula'
    ef_ = lambda c_, f_: _blob(EF_, c_, f_).replace(chr(13), '').split(NL)   # noqa: E731
    rme_ = ef_('8fbab45d', 'README.md')
    add('ruling (5)(iii), ferry (read first)', 'SIDE-explicit-formula README.md at 8fbab45d :3 opens "A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS THIS PROGRAMME`S MATHEMATICS."',
        at(rme_, 3) == "**A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS THIS PROGRAMME'S MATHEMATICS.**", at(rme_, 3)[:60], '2')
    hd_ = [l_ for l_ in rme_ if l_.startswith('## ')]
    add('ruling (5)(iii)', 'the README`s eight sections, amended or appended at b566, b567, b569-b573 and b743', [re.search(r'act (b\d+)', l_).group(1) for l_ in hd_ if re.search(r'act (b\d+)', l_)] == ['b566', 'b567', 'b569', 'b570', 'b571', 'b572', 'b573', 'b743'],
        ' '.join(re.search(r'act (b\d+)', l_).group(1) for l_ in hd_ if re.search(r'act (b\d+)', l_)), '2')
    for b_, t_ in (('c2-b725', '0395f15d'), ('zq-b730', '1e658870'), ('keiper-b725', '01fd33c2'), ('detect-b729', '1023301c'), ('main', '8fbab45d')):
        add('ruling (5)(ii), (10)', 'SIDE-explicit-formula %s at %s' % (b_, t_), gr(EF_, 'rev-parse', b_).startswith(t_), gr(EF_, 'rev-parse', b_)[:8], '2')
    cw_ = ef_('0395f15d', 'SIDEExplicitFormula/C2Walk.lean')
    add('ruling (4), (5)(ii), ferry (read first)', 'C2Walk.lean at 0395f15d: rQ :50, aQ :55, bL :64, the bound 65536 at :192', at(cw_, 50).startswith('def rQ (D : Int)') and at(cw_, 55).startswith('def aQ (D : Int)') and at(cw_, 64).startswith('def bL (D : Int)') and 'N < 65536' in at(cw_, 192), at(cw_, 192)[:60], '2')
    ct_ = ef_('0395f15d', 'SIDEExplicitFormula/C2Theorem.lean')
    add('ruling (3)(i), ferry (read first)', 'C2Theorem.lean at 0395f15d: c2_value_law :72, c2_least_negative :76', at(ct_, 72).startswith('theorem c2_value_law') and at(ct_, 76).startswith('theorem c2_least_negative'), at(ct_, 72)[:40], '2')
    ezq_ = ef_('1e658870', 'SIDEExplicitFormula/Schema/EpsteinZQ.lean')
    ld_ = ef_('1e658870', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean')
    add('ruling (5)(ii), ferry (read first)', 'Schema/EpsteinZQ.lean :59 def rQ; Schema/ZQ/LogDeriv.lean :63-:65 def cQ, the recursion, at zq-b730 1e658870',
        at(ezq_, 59).startswith('def rQ (k : ℕ) : ℕ :=') and at(ld_, 63).startswith('def cQ (n : ℕ) : ℝ :=') and 'n.properDivisors' in at(ld_, 65), at(ld_, 63)[:40], '2')
    for n_, nd_ in ((762, '## I. Numerical & Empirical Findings'), (897, '**∏_v |x|_v = 1 is s-dark.**'), (901, '**RH proved (two-leg, honestly scoped).**'), (905, '**All zeros of ξ(s) are simple.**'),
                    (979, '**The proof of RH is complete in the two-leg sense.**'), (1084, '## How findings move'), (10596, '**The mirror’s roster**')):
        add('ruling (5)(iv), (6), ferry (read first)', 'FINDINGS.md :%d, %s' % (n_, nd_.strip('#* ')[:50]), at(fi, n_).startswith(nd_), at(fi, n_)[:60], '2')
    add('ruling (5)(iv)', 'FINDINGS.md :1094, the layer`s rule: RETIRED with its reason', 'RETIRED' in at(fi, 1094), 'read', '2')
    add('ruling (5)(iv)', 'FINDINGS.md :5924, conservation_of_spectra; :6862, simplicity', 'conservation_of_spectra' in at(fi, 5924) and 'simplicity' in at(fi, 6862), 'read', '2')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (5)(iii), ferry (read first)', 'REGISTRY.md :153, :188, :208, "two-leg" reworded on 2026-07-23', all('two-leg' in at(rg_, n_) and '2026-07-23' in at(rg_, n_) for n_ in (153, 188, 208)), 'read', '2')
    add('ruling (5)(iii), ferry (read first)', 'REGISTRY.md :492-:496, the rows of 2026-07-23', all(at(rg_, n_).startswith('| 2026-07-23 |') for n_ in range(492, 497)), 'read', '2')
    add('ruling (5)(iv), ferry (read first)', 'REGISTRY.md :953, THE CEILING LINE', at(rg_, 953).startswith('**THE CEILING LINE'), at(rg_, 953)[:40], '2')
    er_ = lines_of(os.path.join(PP, 'ERRATA.md'))
    add('ruling (5)(iv), ferry (read first)', 'ERRATA.md :486, E-2026-09-25-1', at(er_, 486).startswith('## E-2026-09-25-1'), at(er_, 486)[:40], '2')
    for d_ in ('D:/PLACE-phase1.5', 'D:/PLACE-phase2'):
        add('ruling (5)(v), PATHS', '%s, a shelf, present' % d_, os.path.isdir(d_), 'present' if os.path.isdir(d_) else 'ABSENT', '2')
    for f_ in ('data/repo_visibility.txt', 'data/b752_pins_closing.txt', 'data/b752_kernels_face.json', 'tools/b303_pins.py', 'tools/act_root.py', 'HANDOFF.md', 'tools/b307_handoff_census.py',
               'data/b752_census_closing.txt', 'tools/mirror_roster.json', 'tools/standing/roster.py', 'data/b715_rules.txt', 'data/b715_roster.txt', 'tools/b610_census.py',
               'tools/b619_census.py', 'tools/b633_census.py', 'data/b638_census.txt', 'data/b724_split_price.txt', 'data/b726_frontdoors.txt', 'data/b727_sitting.txt',
               'data/b732_phase2_frontdoors.txt', 'data/b736_sitting.txt', 'data/b752_rules.txt', 'data/b752_crossref.txt'):
        add('ruling (5), (6), ferry (read first)', '%s tracked at 0e855242' % f_, bool(_blob('D:/relay', '0e855242', f_)), '%d lines' % len(_blob('D:/relay', '0e855242', f_).split(NL)), '2')
    for n_, nd_ in ((11417, '> LANE THREE'), (13944, '*Appended 2026-10-12 by b654'), (14438, '*Appended 2026-10-16 by b672'), (18184, '### b752 — lane two, act one hundred and seventy-nine'),
                    (18196, '**The open orders:**'), (18198, '**The orders by the tool:**')):
        add('ruling (6), (11), ferry (read first)', 'OPEN_TRAILS.md :%d, %s' % (n_, nd_.strip('>#*  ')[:50]), at(ot, n_).startswith(nd_), at(ot, n_)[:60], '2')
    add('ruling (6), (11)', 'OPEN_TRAILS.md :14438, THE LEDGER SPLIT', 'THE LEDGER SPLIT' in at(ot, 14438), 'read', '2')
    # ### (R363)(7): the hold's lines at HEAD, each by path and line
    for f_, n_, nd_ in (('tools/standing/routes/b644_record.py', 38, "SESSION_ID = 'f004d01d-"), ('tools/standing/routes/b644_record.py', 105, '    return 10 ** 9'),
                        ('tools/b597_record.py', 32, "SESSION = 'C:/Users/echo chamber/.claude/projects/D--/a5f76775-"), ('tools/b672_citation.py', 33, "SESSION = 'C:/Users/echo chamber/.claude/projects/D--/b895aca8-"),
                        ('tools/b698_record.py', 92, "    return subprocess.run(['git', '-C', repo] + list(a)"), ('tools/b698_record.py', 1272, "    rem = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main')"),
                        ('tools/standing/repeat.py', 274, "                len(bad), ', '.join(bad[:6]), '' if s['pushed'] else ' ; HEAD NOT THE REMOTE MAIN'"),
                        ('tools/b752_worklist.py', 33, "SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/0fa2f3b7e932577a/"), ('tools/standing/hook.py', 282, "CALLS = os.path.join(tempfile.gettempdir()"),
                        ('tools/standing/hook.py', 306, "    return os.path.join(tempfile.gettempdir(), 'standing-gitwrite-"), ('tools/standing/fold/record.tpl', 3045, "    SP = os.environ.get('B713_SCRATCH') or 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/3bbc6267-"),
                        ('tools/standing/v130.py', 40, "SCR = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/02c7cf38-"), ('tools/standing/v1160.py', 21, "SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-"),
                        ('tools/standing/v1170.py', 24, "SP736 = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/7c29db99-"), ('tools/standing/v1170.py', 186, "    g += guard(L, 'snapshot', 'THE THIRD LOSS"),
                        ('tools/standing/v1110.py', 41, "TRANSCRIPT = os.path.expanduser('~/.claude/projects/D--/7c29db99-"), ('tools/standing/commit.py', 316, "CALLS = os.path.join(__import__('tempfile').gettempdir()"),
                        ('tools/standing/remotecache.py', 25, "DIR = os.path.join(tempfile.gettempdir(), 'relay_remote_cache')")):
        L_ = lines_of(p(*f_.split('/')))
        add('ruling (7)(vii)-(ix), ferry (hold)', '%s :%d' % (f_, n_), at(L_, n_).startswith(nd_), at(L_, n_)[:60], '1')
    for f_ in ('tools/standing/hold.py', 'tools/standing/scratchfsck.py', 'tools/standing/harnessmoves.py', 'data/b738_dispatch_rows.json'):
        add('ruling (7), ferry (hold)', '%s tracked' % f_, bool(gr('D:/relay', 'ls-files', '--', f_)), gr('D:/relay', 'log', '-1', '--format=%h', '--', f_) or 'ABSENT', '1')
    rl_ = lines_of(p('data', 'b752_rules.txt'))
    add('ruling (3)(iii), (7)(i)', 'data/b752_rules.txt (12), the navigator`s search rule', any(l_.startswith('(12) ') for l_ in rl_), 'read', '1')
    add('ruling (scope), (7)(vii)', 'FINDINGS.md :14813 and :14862, the session change', '(session)' in at(fi, 14813) and 'session change' in at(fi, 14862), 'read', '1')
    v0_ = (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip()   # ### entering the act: v1.33.0's commit's parent once it lands, HEAD's blob before
    add('ferry', 'tools/standing/VERSION v1.32.0 entering the act', v0_ == 'v1.32.0', v0_, '1')
    # ### b753 step zero: the two rows "tracked and clean at step zero" for the carried files removed -- (R363)(9) commits them after the
    # ### check, and section 8's rows read them in that order (TO BE COMMITTED, then committed alone); the first dry run missed on both
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (7), ferry (read first)', 'events (1)-(13) and 36 defects (data/b752_events.txt, data/b752_defects.txt)',
        starts == list(range(1, 14)) and len(letters) == 36, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    A_, S_, H_, N_ = "THE AUTHOR'S", "THE SEAT'S", "THE HOST'S", "THE NAVIGATOR'S"
    for n_, k_, w_ in ((4, 1, A_ + ' [CLOSE ; NEW]'), (10, 2, S_ + ' [CLOSE ; NEW]'), (13, 3, S_ + ' [CLOSE ; REPEAT b751 (2)]'), (15, 4, S_ + ' [CLOSE ; REPEAT b751 (2)]'),
                       (17, 5, S_ + ' [CLOSE ; NEW]'), (22, 6, H_ + ' [CLAIM ; NEW]'), (29, 7, A_ + ' [CLOSE ; NEW]'), (35, 8, S_ + ' [CLAIM ; NEW]'),
                       (38, 9, S_ + ' [CLOSE ; NEW]'), (40, 10, A_ + ' [CLOSE ; NEW]'), (45, 11, S_ + ' [CLAIM ; NEW]'), (49, 12, A_ + ' [CLOSE ; NEW]'),
                       (53, 13, S_ + ' [CLOSE ; NEW]')):
        add('ruling (7), ferry (read first)', 'data/b752_events.txt :%d, (%d) %s' % (n_, k_, w_), at(ev, n_).startswith('    (%d) %s' % (k_, w_)), at(ev, n_)[:60], '1')
    df_ = lines_of(p('data', 'b752_defects.txt'))
    TAGS_ = (('a', S_, 'CLOSE ; REPEAT b751 (a)'), ('b', S_, 'CLAIM ; REPEAT b751 (b)'), ('c', S_, 'CLOSE ; REPEAT b751 (c)'), ('d', S_, 'CLOSE ; REPEAT b751 (d)'),
             ('e', S_, 'CLOSE ; NEW'), ('f', S_, 'CLOSE ; NEW'), ('g', S_, 'CLOSE ; NEW'), ('h', S_, 'CLOSE ; NEW'),
             ('i', S_, 'CLOSE ; REPEAT b751 (r)'), ('j', S_, 'CLOSE ; REPEAT b751 (p)'), ('k', S_, 'CLOSE ; NEW'), ('l', S_, 'CLOSE ; NEW'),
             ('m', S_, 'CLOSE ; NEW'), ('n', S_, 'CLAIM ; NEW'), ('o', S_, 'CLOSE ; NEW'), ('p', N_, 'CLAIM ; NEW'),
             ('q', N_, 'CLAIM ; NEW'), ('r', S_, 'CLOSE ; REPEAT b751 (u)'), ('s', S_, 'CLOSE ; REPEAT, the class of standing row (14), its earlier letters not looked up this act'),
             ('t', S_, 'CLOSE ; REPEAT b749 (h)'), ('u', S_, 'CLAIM ; NEW'), ('v', S_, 'CLAIM ; NEW'), ('w', S_, 'CLOSE ; NEW'),
             ('x', S_, 'CLOSE ; REPEAT b752 (s)'), ('y', S_, 'CLOSE ; REPEAT b752 (r)'), ('z', S_, 'CLOSE ; REPEAT b752 (a)'),
             ("a'", S_, 'CLOSE ; NEW'), ("b'", S_, 'CLAIM ; NEW'), ("c'", S_, 'CLOSE ; NEW'), ("d'", S_, 'CLOSE ; NEW'), ("e'", S_, 'CLOSE ; NEW'),
             ("f'", S_, 'CLOSE ; NEW'), ("g'", S_, 'CLOSE ; NEW'), ("h'", S_, 'CLAIM ; NEW'), ("i'", S_, 'CLOSE ; REPEAT b752 (x)'), ("j'", S_, 'CLOSE ; REPEAT b752 (x)'))
    for n_, (l_, o_, t_) in zip(range(7, 43), TAGS_):
        add('ruling (7), ferry (read first)', "data/b752_defects.txt :%d, (%s) %s [%s]" % (n_, l_, o_, t_[:40]), at(df_, n_).startswith("    (%s) %s [%s]" % (l_, o_, t_)), at(df_, n_)[:60], '1')
    add('ruling (7)', 'data/b752_defects.txt, the navigator`s (p) and (q) alone', [x_ for x_, o_, _t in TAGS_ if o_ == N_] == ['p', 'q'], 'p q', '1')
    add('ruling (7)(ii)', "data/b752_defects.txt :40 (h'), the command bank`s matcher reading the word as the identifier", 'OUTBOUND REQUESTS 3, AN IDENTIFIER IN 3' in at(df_, 40), at(df_, 40)[:60], '1')
    add('ruling (3), (7)', 'data/b752_defects.txt :22 (p) the orders reader`s words; :23 (q) W-ORD-PLATT-RUNG', 'from its entry form alone' in at(df_, 22) and 'W-ORD-PLATT-RUNG' in at(df_, 23), at(df_, 23)[:60], '1')
    add('ruling (1), (7)', 'FINDINGS :%d, b752`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## W-ORD-MECHANISM-ATTRIBUTION’s plan passed at [P1]'), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b751`s weight line and corrigendum (b752`s), the form b753`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), at(fi, K.B711_WEIGHT).startswith('*Appended 2026-11-10 by b752') and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b751'), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b752`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b752 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (1)', 'OPEN_TRAILS :%d, b752`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store at D:/claude-store/projects-D--, reached by the harness`s projects path', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file D:/.claude/settings.json by its hash alone', bool(__import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), __import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.32.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.32.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R363)(1): b752's export, the mirror's last
    add('ruling (1)', '%s, b752`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: SIDE-explicit-formula and the other clones at the paths the worklist holds, each listed, a path absent printed absent
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R363)(3), (5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), (6)', 'the push-b752-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R363)(3), (5): act_current alone, then b752's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b752_relay_push-b752-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['tools/mirror_prevbuild.json'])):
        if fs_ == ['tools/mirror_prevbuild.json'] and not c_:   # ### b753: committed alone if it differs from HEAD's blob beyond line endings, else restored
            hb_ = gr('D:/relay', 'rev-parse', 'HEAD:tools/mirror_prevbuild.json')
            add('ruling (3)', 'tools/mirror_prevbuild.json at HEAD`s blob %s (equal, or to be committed alone after this check)' % hb_[:8], True,
                'blob %s ; HEAD %s' % (gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json')[:8], hb_[:8]), '0')
            continue
        if not c_:
            add('ruling (3), (5)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3), (5)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3), (6)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (3), (6)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3), (6)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b753_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b753_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b753 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b752_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.32.0's controls and the rules, the cross-reference, the signature control and the statements, the plan and the answers bank, the line bank, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R363)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R363)(7)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R363)(6): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b753 ((R363)(7)); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R362)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b753 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTY, THE SYSTEM REFRESH: b752 AT ITS WEIGHT; THE AUTHOR`S ROOT ANSWER ENTERED WITH ITS ORDER; '
              'THE NAVIGATOR`S CORRECTION ON THE COEFFICIENT RECORD; THE CLASS-NUMBER-3 WALK REGISTERED, NOT RUN; THE HOLD OF 2026-11-11 ENTERED AND THE TRANSCRIPT STORE READ; '
              'THE KERNELS RECONCILED, THE CRITERION KERNEL`S BRANCHES MAPPED, THE FRONT DOORS` HEADS AND THE REFERENCE LAYER`S ANCHORS READ, THE SHELVES LISTED; '
              'THE CENSUS`S NEXT EDITION, THE HANDOFF PAGE, THE MIRROR`S ROSTER, THE HARNESS UNDER THE RECORD AND THE UNLEDGERED INTENTIONS PUT; NOTHING BUILT, UNDER (R363).**')   # ### b753 step zero: the ferry`s ACT line (:35); R7 refused the carried title
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b752's sections over b752's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.32.0: the repairs of (R363)(7), twelve controls over 47 cases, each case failing before its repair and passing after', 'b753_standing_v1320.txt'),
                ('the twelve rules of (R363)(7), the navigator`s search rule among them', 'b753_rules.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE CROSS-REFERENCE, CONTROL AND STATEMENTS ((R363)(3)-(5))', [
                ('the six questions read against the corpus before anything was put: three held, three candidates, no order entered', 'b753_crossref.txt'),
                ('the class-group signature of cQ`s negative n, n <= 3000, its control first: the table 102, 0, 320, 79, the statement true, the reverse false', 'b753_cq_signature.txt'),
                ('the kernel`s seven classes read as statements, the declarations graded, none a predicate on functions', 'b753_statements.txt')]),
            ('THE PLAN ((R363)(6))', [
                ('W-ORD-MECHANISM-ATTRIBUTION`s plan, T0-T3 priced, T0 then T1 recommended, put as [P1]; nothing built', 'b753_attribution_plan.txt'),
                ('the author`s answers appended by the record tool`s route, the [P1] answer and its time before the lock', 'b753_author_answers.txt',
                 r'(?m)^### b753 -- THE AUTHOR`S ANSWERS[^\n]*'),
                ('the probe-path refusal printed before the lock gate', 'b753_pathrefusal.txt')]),
            ('THE LINE (Component 4)', [
                ('the INTEGRATION line from REGISTRY and SPIRAL_MAP with the match, stage CLUSTERED, 0 of 4 names matched, the earlier lines read again, none rewritten', 'b753_line.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b753_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b752`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument entered, a planted wrong figure per run row', 'b753_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R362)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R363)(6)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b752 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b752-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the cross-reference, the signature control and the statements committed before the plan, the generator committed before its bank, each tool`s controls before its figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: the plan read where it stands -- B3 and A9 of the survey cited, no class said to be attributed, no candidate called new, nothing said of what the catalogue meets ; no sentence saying a thing was deposited, published or versioned ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ; N5: no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b753_address_scan.txt, data/b753_address_scan_postlock.txt, data/b753_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) ; no paper written ; no door or ledger row edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b753`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.32.0 by (R363)(7) ; D:/.claude/settings.json unedited this act ; the per-act tools of b698-b752 unedited, act_current`s shared_edits empty ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS THE AUTHOR ORDERED AT [P1]`S PASS**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, each from its bank: the root`s question on the order after this act (the refresh, the sitting, sections 6-8, the build), its answer in relay data/b753_author_answers.txt ;',
    '        the build of T0 then T1, T2 and T3 printed, in an act the author names (relay data/b753_attribution_plan.txt, [P1] passed) ; the cross-reference`s three candidates, none entered (relay data/b753_crossref.txt) ; b752`s line read again CLUSTERED, its heading naming no finding (relay data/b753_defects.txt (b’)) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b753_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b752 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b753: the standing repairs are v1.32.0's ((R363)(7), relay data/b753_standing_v1320.txt, read in the corrigendum section); the
    # ### carry's diffs here (b753 carried at step zero before the fold; its tools since are the templates and tools/acts/b753.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b752 left them; port-b707 at b712`s tip %s)' % (
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
    b753's form over b753's objects: the corrigendum's foot and v1.32.0's controls; the cross-reference's foot; the signature's foot; the
    statements' grades; the plan's foot; the line bank's foot; the rules bank's rows; the citation check; the reproduction run; the address scan; each by its own lines through _bfig,
    which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1320.txt' % ACT, r'\*\*v1\.32\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.32.0`s controls')
    xr_ = _bfig('%s_crossref.txt' % ACT, r'\*\*THE CROSS-REFERENCE: QUESTIONS (\d+) ; HELD (\d+) ; CANDIDATES (\d+) ; CITES NOT MATCHED (\d+) ; NO ORDER ENTERED\.\*\*',
                'the cross-reference`s foot')
    sg_ = _bfig('%s_cq_signature.txt' % ACT, r'\*\*THE SIGNATURE, n <= (\d+): CONTROL AS WANTED \(negative (\d+), smallest (\d+), exactly zero (\d+), nonnegative (\d+)\) ; '
                r'PRIMES (\d+): R (\d+), I (\d+), P (\d+), N (\d+) ; TYPE MISMATCHES (\d+), THIRD WAY (\d+) ; THE TABLE \(neg & N (\d+), neg & no N (\d+), pos & N (\d+), '
                r'pos & no N (\d+)\) ; THE STATEMENT (TRUE|FALSE) ; THE REVERSE (TRUE|FALSE) \((\d+) counterexamples among nonzero\) ;', 'the signature`s foot')
    stt_ = rdn('%s_statements.txt' % ACT)
    _stf = _bfig('%s_statements.txt' % ACT, r'\*\*THE STATEMENTS: \(i\) A CLASS OF SIDE-kernel v1\.5 IS AN ENUMERATED CONSTRUCTOR WITH A COUNT \((\d+)\)', 'the statements` foot')
    st_rows_ = len([l_ for l_ in stt_[stt_.find('## THE GRADES'):].split(NL) if re.search(r' -- (?:DERIVES|INTERFACES|ENCODES-CONCLUSION/SHELL|a DEFINITION)\b', l_)])
    st_grades_ = dict((w_, len(re.findall(r'\b%s\b' % re.escape(w_), stt_[stt_.find('## THE GRADES'):]))) for w_ in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION/SHELL'))
    pl_ = _bfig(K.SECTION_BANK.split('/')[-1], r'\*\*\[P1\] THE ATTRIBUTION PLAN: .*RECOMMENDED: BUILD T0 \((\d+)-(\d+) LINES\) THEN T1 \((\d+)-(\d+)\), PRINT T2 AND T3-f ;.*(NOTHING BUILT)\.\*\*',
                'the plan`s foot')
    p1_ = 'PASSED' if 'BEGINPass [P1].' in rdn('%s_author_answers.txt' % ACT) else ('STRUCK' if 'BEGINStrike [P1]' in rdn('%s_author_answers.txt' % ACT) else 'UNANSWERED')
    ln_ = _bfig('%s_line.txt' % ACT, r'\*\*THE LINE: (COMPOSED) ; FROM REGISTRY 1\.5c-21 TO 1\.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE (\S+) ; STAGE (\w+) ; '
                r'MATCHED (\d+) OF (\d+) ; THE EARLIER LINES READ AGAIN (\d+), NONE REWRITTEN ; (ALL AS READ)\.\*\*', 'the line bank`s foot')
    reps_ = [int(x_) for x_ in re.findall(r'(?m)^\((\d+)\) ', rdn('%s_rules.txt' % ACT))]   # ### the rules bank's rows
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b753: no order entered this act ((R363) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], rules_rows=reps_,
                repairs=len(reps_),   # ### the rules bank's rows, one per repair of (R363)(7) and the navigator's search rule
                xr_q=int(xr_[0]), xr_held=int(xr_[1]), xr_cand=int(xr_[2]), xr_nomatch=int(xr_[3]),
                sg_n=int(sg_[0]), sg_neg=int(sg_[1]), sg_small=int(sg_[2]), sg_zero=int(sg_[3]), sg_nonneg=int(sg_[4]), sg_primes=int(sg_[5]),
                sg_types=tuple(int(x_) for x_ in sg_[6:10]), sg_mism=int(sg_[10]), sg_third=int(sg_[11]), sg_table=tuple(int(x_) for x_ in sg_[12:16]),
                sg_stmt=sg_[16], sg_rev=sg_[17], sg_counter=int(sg_[18]),
                st_count=int(_stf[0]), st_rows=st_rows_, st_grades=st_grades_,
                pl_t0=(int(pl_[0]), int(pl_[1])), pl_t1=(int(pl_[2]), int(pl_[3])), p1=p1_,
                ln_keystone=ln_[1], ln_stage=ln_[2], ln_matched=int(ln_[3]), ln_of=int(ln_[4]), ln_earlier=int(ln_[5]), ln_ok=(ln_[6] == 'ALL AS READ'),
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R363)(3): the kernel rows of one kind as banked (data/b753_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R363): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
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
        'the seat`s commands running lean or lake on this host (relay data/b753_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b753_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b753's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b753_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b753_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b753_standing_v1320.txt', '## THE CONTROLS', '### ### **v1.32.0: CONTROLS '),
               ('data/b753_cq_signature.txt', '## THE CONTROL:', '## THE TABLE:'),
               ('data/b753_statements.txt', '## (i)', '## THE GRADES'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, the plan: the cross-reference, the generator, the signature control and the statements each committed before the plan, the
# ### generator before its bank (the bank's stamp after the generator's commit)
N2_SECTIONS = ()


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R363): the cross-reference committed before the generator, the generator before its bank (the bank's stamp after the generator's
    commit), the bank before the statements, the statements before the plan, the plan before the answers, the answers before the line; each
    tool's controls before its figures; the standing version before the gate; the (W) regeneration, the pre-lock comparison and the
    probe-path refusal before the lock gate. Step zero, v1.32.0, the weight and corrigendum (PLACE-papers, then relay), the cross-reference,
    the generator, the signature bank, the statements, the plan, the answers and the line in that order by time; v1.32.0 an ancestor of the
    line bank's commit, and that of HEAD; Components 2-4 writing the relay alone."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.C2_PLAN_FIRST),
              (ROOT, K.C2_RELAY_ALL[1]), (ROOT, K.C2_RELAY_ALL[2]), (ROOT, K.C2_RELAY), (ROOT, K.C3_RELAY[0]), (ROOT, K.C3_RELAY[1]), (ROOT, K.C4_LINE)]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.C4_LINE], capture_output=True).returncode == 0 \
        and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C4_LINE, 'HEAD'], capture_output=True).returncode == 0
    ppl_ = [x for x in g(PP, 'rev-list', '%s..HEAD' % K.PRE_PP).split() if x.strip()]
    disch_ = sorted(x for x in g(PP, 'show', '--name-only', '--format=', K.C1_PP).split() if x.strip()) == ['FINDINGS.md'] \
        and not [h_ for h_ in ppl_ if int((g(PP, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) < tm_[-1] and not h_.startswith(K.C1_PP)]
    genf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_RELAY_ALL[1]).split() if x.strip()]
    sigf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_RELAY_ALL[2]).split() if x.strip()]
    sig_ = rdn('%s_cq_signature.txt' % ACT)
    st_ = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', sig_.split(NL)[0] if sig_ else '')
    st_ep_ = __import__('calendar').timegm(time.strptime(st_.group(1), '%Y-%m-%dT%H:%M:%SZ')) if st_ else None
    gen_ = 'tools/b753_cq_signature.py' in genf_ and 'data/b753_cq_signature.txt' not in genf_ and 'data/b753_cq_signature.txt' in sigf_ \
        and _first_add('tools/b753_cq_signature.py') == g(ROOT, 'rev-parse', K.C2_RELAY_ALL[1]).strip() \
        and st_ep_ is not None and tm_[5] <= st_ep_ <= tm_[6]
    planf_ = [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C3_RELAY[0]).split() if x.strip()]
    cites_ = [p_ for p_ in ('data/b753_crossref.txt', 'data/b753_cq_signature.txt', 'data/b753_statements.txt') if p_ in planf_]   # ### a bank the plan stands on committed with the plan, not before it
    agenda_first_ = bool(all(tm_)) and tm_[4] <= tm_[5] < tm_[6] <= tm_[7] <= tm_[8]
    sect_ = gen_ and not cites_ and agenda_first_
    route_ = disch_ and sect_
    same_ = True
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the weight and corrigendum (PLACE-papers %s) FINDINGS alone, no other PLACE-papers write before the line: %s; the cross-reference (relay %s), the generator, its bank, the statements (relay %s) and the plan in that order: %s; the generator first added alone of its bank, the bank`s stamp between the generator`s commit and its own: %s; the banks the plan stands on committed with the plan and not before it: %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.32.0, the weight and corrigendum, the corrigendum banks, the cross-reference, the generator, the signature, the statements, the plan, the answers and the line in that order by time: %s (%s), v1.32.0 an ancestor of the line bank`s commit and that of HEAD: %s; the tools` controls before their figures: %s' % (
            K.C1_PP[:8], disch_, K.C2_PLAN_FIRST, K.C2_RELAY, agenda_first_, gen_, ', '.join(cites_) or 'none',
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b753's objects; b752's in git at b752's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b753_standing_v1320.txt', ('ALL AS WANTED',)), ('b753_crossref.txt', ('THE CROSS-REFERENCE: QUESTIONS 6', 'NO ORDER ENTERED')),
             ('b753_cq_signature.txt', ('CONTROL AS WANTED', 'THE STATEMENT TRUE', 'THE REVERSE FALSE')),
             ('b753_statements.txt', ('THE STATEMENTS:', 'NONE OF THE SEVEN HAS A PREDICATE ON FUNCTIONS', 'dh_witness SHELL')),
             ('b753_attribution_plan.txt', ('[P1] THE ATTRIBUTION PLAN', 'B3 STANDS', 'NOTHING BUILT')),
             ('b753_line.txt', ('THE LINE: COMPOSED', 'STAGE CLUSTERED', 'ALL AS READ')),
             ('b753_corrigendum.txt', ('ITEMS',)), ('b753_citation_check.txt', ('THE CHECK HALTED',)), ('b753_reproduce.txt', ('REPRODUCES',)), ('b753_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### the entry's last line, the INTEGRATION line, in canon XXIII (A)'s form, read from REGISTRY and SPIRAL_MAP with the match of
# ### v1.32.0 through tools/b753_line.py (relay data/b753_line.txt): the Epstein instance, its keystone THE_EPSTEIN_CONTROL_OBJECT,
# ### CLUSTERED, 0 of 4 FINDING names matched (no keystone line written this act)
INTEGRATION_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) ; '
                    'keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) ; stage CLUSTERED')
FIXED_SENTENCES = ()   # ### b753: no fixed sentence ordered by (R363)


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()


def _section_body(n):
    """the paper's section n as PLACE-papers carries it at HEAD: the lines from its heading to the next heading."""
    t = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '')
    i = t.find('\n## %d. ' % n)
    j = t.find('\n## %d.' % (n + 1), i + 1)
    return t[i + 1:j] if i >= 0 and j > i else ''


def _section_cites(bank):
    """the cites a section bank prints (tools/standing/citeprint.py's form): a head `  (n) [relay |PLACE-papers ]<path>[ at <rev>] :a[-:b]`,
    then its lines `      NNN  <text>`; returned (heads, [(where, path, rev, line, text)])."""
    sb_ = rdn(bank)
    reg_ = sb_[sb_.find('### EVERY CITE'):sb_.find('### THE CHECKS')]
    heads_, cites_, cur_ = [], [], None
    for l_ in reg_.split(NL):
        h_ = re.match(r'^  \((\d+)\) (?:(relay|PLACE-papers) )?(\S+)(?: at ([0-9A-Za-z]+))? :(\d+)(?:-:(\d+))?\s*$', l_)
        if h_:
            cur_ = (h_.group(2) or 'lean', h_.group(3), h_.group(4))
            heads_.append(h_.groups())
            continue
        p_ = re.match(r'^ {6,}(\d+)  (.*)$', l_)
        if cur_ and p_:
            cites_.append(cur_ + (p_.group(1), p_.group(2)))
    return heads_, cites_


def _cite_src(where, path, rev, n):
    """the source line a cite names, read from its tree: Lean at its revision under SIDEExplicitFormula/Schema/, the ledger in PLACE-papers at
    its revision, a relay bank from the working file."""
    if where == 'lean':
        s_ = _show(K.EF_DIR, rev, 'SIDEExplicitFormula/Schema/%s' % path) or ''
    elif where == 'PLACE-papers':
        s_ = g(PP, 'show', '%s:%s' % (rev or 'HEAD', path)) or ''
    else:
        s_ = rd(os.path.join(ROOT, *path.split('/'))) or ''
    s_ = s_.replace(chr(13), '').split(NL)
    return s_[int(n) - 1] if 0 < int(n) <= len(s_) else None
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R363): no sentence says anything was deposited, published or versioned; the plan cites B3 (PATHS :396) and A9 (:389) and says
    B3 stands; no sentence of the plan or the entry says a class is attributed the zero, the catalogue meets the zero, or a candidate is new
    or the earliest, outside a negation; the entry's INTEGRATION line its last line, reading REGISTRY 1.5c-21 and SPIRAL_MAP's Epstein row
    as they stand; no sentence calling the work the earliest of its kind in any assistant, none naming zeta, RH or h2 as moved outside a
    negation; the banks' nouns in the entry; the root prompt's sentences about the entry the composer's. From the banks' last lines, the
    plan bank, REGISTRY at PLACE-papers HEAD, the entry's sentences and the root prompt in the answers bank."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b753: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    # ### N3 over the plan as banked (relay data/b753_attribution_plan.txt, the bank put at [P1]): B3 and A9 cited by their lines, B3
    # ### standing; no sentence saying a class is attributed the zero or the catalogue meets it, none calling a candidate new or the earliest,
    # ### outside a negation; none naming ζ, RH or h2 as moved
    _rl = lambda p_: (rd(os.path.join(PP, *p_.split('/'))) or '').replace(chr(13), '').split(NL)
    plan_ = rdn(K.SECTION_BANK.split('/')[-1])
    psents_ = [x for x in re.split(r'(?<=[.;])\s+', ' '.join(l_.strip() for l_ in plan_.split(NL) if l_.strip() and not l_.startswith('### '))) if x.strip()]
    said_ = bool(plan_) and all(w_ in plan_ for w_ in ('PATHS_TO_THE_CRITICAL_LINE.md :396', '(:389)', 'A9', 'B3 STANDS'))
    neg_ = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither)\b'
    lit_ = [x for x in psents_ + sents if re.search(r'\b(?:earliest|novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine))\b', x, re.I)
            and not re.search(neg_, x)]
    meant_ = [x for x in psents_ + sents if re.search(r'\b(?:is attributed|attributes the zero|falls in (?:a |the )?class|the catalogue meets|meets the zero)\b', x, re.I)
              and not re.search(neg_, x)]
    more_ = lit_ + meant_   # ### N3: no class attributed, no meeting claimed, no candidate called new
    nsents_ = psents_
    dep_ = [x for x in nsents_ + sents if re.search(r'\b(?:deposited|published|versioned)\b', x) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(r'\b(?:RH|GRH|h2|ζ)\b.*\b(?:holds|fails|proved|refuted|moved)\b', x) and not re.search(neg_, x)]
    lines_ = [l for l in text.split(NL) if l.strip()]
    rg_ = _rl('REGISTRY.md')
    sm_ = rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''
    integ_ = bool(lines_) and lines_[-1].strip() == INTEGRATION_LINE \
        and any(l.startswith('| 1.5c-21 |') for l in rg_) and '| **The Epstein instance** (seated 2026-11-09, b750) |' in sm_ and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in sm_
    fixed_ = []
    nouns_ = [w_ for w_ in ('W-ORD-MECHANISM-ATTRIBUTION', '[P1]', 'T0', 'T1', 'B3', 'MechanismClass', 'cQ',
                            'data/%s_crossref.txt' % ACT, 'data/%s_cq_signature.txt' % ACT, 'data/%s_statements.txt' % ACT,
                            'data/%s_attribution_plan.txt' % ACT, 'data/%s_line.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and said_ and not more_ and not dep_ and not first_ and not loc_ and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the plan read where it is banked -- B3 (PATHS :396) and A9 (:389) cited, B3 standing: %s; a sentence of the plan or the entry calling a candidate new or the earliest, or saying a class is attributed the zero or the catalogue meets it, outside a negation: %s; a sentence of the plan or the entry saying a thing was deposited, published or versioned outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY 1.5c-21 and SPIRAL_MAP`s Epstein row read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), said_, more_ or 'NONE', dep_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE', integ_, nouns_ or 'NONE',
            'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R363) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R363)(5))
# ### (R363)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R363)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
    # ### same reader the ceiling takes; the face's `locked at (UTC)` line no longer dates it
    import lockdate as LD
    lc = LD.lock_of(ACT, os.path.join(ROOT, 'data'))
    lock = LD.lock_epoch(lc, ROOT) if lc else None
    # ### v1.30.0, (R363)(3)(viii), b752 events (12): the lock's time printed from the one reader's epoch; b752's module left lock_iso unset and
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
    # ### (R363) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b752's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b753, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b752's face
# ### read them; (R363)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
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
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R363)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R363)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b752 left them; the address scan's count from its bank (relay data/b753_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R363)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R363)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R363)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    # ### v1.30.0, (R363)(3)(vi), b752 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R363)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and not zdel_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b753_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b753 step zero: R7 refused the carried head (b752's title under the next ordinal); the ruling's ordinal and title (the ferry's
    # ### ACT line, :35), the act's own figures added when its banks stand
    return ('### b753 — lane two, act one hundred and eighty, the system refresh under (R363): b752 at its weight; the author`s root answer entered with its order; '
            'the navigator`s correction on the coefficient record; the class-number-3 walk registered, not run; the hold of 2026-11-11 entered; nothing built')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 result sentence adjusted to what the act did: the plan of
    W-ORD-MECHANISM-ATTRIBUTION passed at [P1], T0-T3 priced, T0 then T1 recommended, T2 not abstracting at the pin, T3 printed as a finding;
    the signature's four cells and its statement; the classes read as an enumeration and the graded rows counted; the cross-reference's
    questions, held and candidates; v1.32.0's controls landed; nothing built. Each finding's name in the heading, for the line reader. Every
    figure from the banks (the plan's foot and the answers bank, the signature's foot, the statements' grades, the cross-reference's foot,
    v1.32.0's controls)."""
#⟪END⟫
#⟪SECTION record 31⟫
    ctl_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if not all(c_ in ctl_ for c_ in ('recall', 'orders', 'cites', 'version')):
        sys.exit('### v1.32.0`S CONTROLS DO NOT NAME (recall), (orders), (cites) AND (version) -- NOTHING COMPOSED')
    if f['rules_rows'] != list(range(1, len(f['rules_rows']) + 1)) or len(f['rules_rows']) < 3:
        sys.exit('### THE RULES BANK`S ROWS ARE NOT (1)-(n) IN ORDER -- NOTHING COMPOSED')
    if not f['ln_ok'] or f['p1'] != 'PASSED' or f['sg_stmt'] != 'TRUE' or f['sg_mism'] != 0 or f['xr_held'] + f['xr_cand'] != f['xr_q']:
        sys.exit('### THE LINE BANK, THE ANSWER ON [P1], THE SIGNATURE OR THE CROSS-REFERENCE NOT AS READ -- NOTHING COMPOSED')
    return ('## W-ORD-MECHANISM-ATTRIBUTION’s plan %s at [P1] (b753_attribution_plan): T0-T3 priced, T0 then T1 recommended, T2 not abstracting at the pin, '
            'T3 printed as a finding; the class-group signature of cQ’s negative n (b753_cq_signature): %d, %d, %d, %d, the statement %s; the kernel’s classes read '
            'as an enumeration, %d rows graded or described (b753_statements); %s questions cross-referenced, held %d, candidates %d, none entered (b753_crossref); '
            'the navigator’s correction and v1.32.0’s %d controls landed; nothing built' % (
                f['p1'].lower(), f['sg_table'][0], f['sg_table'][1], f['sg_table'][2], f['sg_table'][3], f['sg_stmt'], f['st_rows'],
                {6: 'six'}.get(f['xr_q'], str(f['xr_q'])), f['xr_held'], f['xr_cand'], len(ctl_)))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the twelve rules of relay data/b753_rules.txt, the seat`s reading of (R363)(7) and the navigator`s search rule, each for the author`s strike; (2) the plan`s reading that (i) of the order is answered by the record without a build -- no class of SIDE-kernel v1.5`s seven carries a predicate on functions -- and that T3-f is printable now, as [P1] put it and the author passed it (relay data/b753_attribution_plan.txt (2), data/b753_statements.txt (i)); (3) b752`s INTEGRATION line, written SYNTHESISED, read again CLUSTERED by the same match because its heading carries no finding name, printed and not rewritten (relay data/b753_line.txt (C), data/b753_defects.txt (b’)); '
            +
            '(4) %s and the seat’s %s defect%s as lettered' % (
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b753: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
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
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R363)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b753's objects; b752's composer in git at
    b752's record tool). Its last line the INTEGRATION line (Component 4)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    if f['p1'] not in ('PASSED', 'STRUCK'):
        sys.exit('### THE ANSWERS BANK CARRIES NO WORD ON [P1] -- NOTHING COMPOSED')
    rep, tot = _repeats()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R363)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R362)(2)(v)
    co_ = jl('%s_corrigendum.json' % ACT)
    sg_ = f['sg_table']
    e = ['', _title(), '',
         'W-ORD-MECHANISM-ATTRIBUTION (OPEN_TRAILS :17932) was planned and not built. The plan was put to the author once as [P1] and %s (relay data/b753_attribution_plan.txt, data/b753_author_answers.txt). It reads the order’s first clause as answered by the record without a build: a class of SIDE-kernel v1.5’s MechanismClass is an enumerated constructor (%d of them, Bridge/TheBridgeComplete.lean :20-:25) whose per-class predicate is a Prop about a real sigma; none of the seven carries a predicate on functions, so no theorem in the kernel’s present vocabulary can say a zero of Z_Q0 falls in a class, and the finding T3-f is printable now (relay data/b753_statements.txt (i)). It names the second clause’s premise, the Euler product and the sign of the log-derivative’s coefficients, and prices two theorems for it: T0, the coefficients rQ n / 2 not multiplicative (%d-%d lines), then T1, cQ not nonnegative through cQ 48 < 0 beside vonMangoldt_nonneg (%d-%d lines); T2, the general edge theorem, does not abstract at the pin, Mathlib’s route to ζ’s line at e960b841 running on Dirichlet characters through their Euler products; B3 stands (PATHS_TO_THE_CRITICAL_LINE.md :396). The build is fourth, after the system refresh, the sitting and sections 6-8, in an act the author names.' % (
             f['p1'].lower(), f['st_count'], f['pl_t0'][0], f['pl_t0'][1], f['pl_t1'][0], f['pl_t1'][1]), '',
         '*Filed at b753 on the author’s ruling `(R363)`; %d question%s put before the root. Banks: relay '
         '`data/b753_corrigendum.txt`, `data/b753_standing_v1320.txt`, `data/b753_rules.txt`, `data/b753_crossref.txt`, `data/b753_cq_signature.txt`, `data/b753_statements.txt`, `data/b753_attribution_plan.txt`, `data/b753_put_1.json`, `data/b753_author_answers.txt`, `data/b753_line.txt`, `data/b753_prelock.txt`, `data/b753_pathrefusal.txt`, '
         '`data/b753_reproduce.txt`, `data/b753_address_scan.txt`, `data/b753_touch.txt`, `data/b753_standing_figures.txt`, `data/b753_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the carried items** ((R363)(1), (2), (7); %s, %s, %s): b752 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b752’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- with %d entered beside them (the unbanked refusal of 21:20:10Z, the navigator’s correction of `(R363)`(2), the navigator’s defect of the author’s amendment) '
         '-- at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b753_corrigendum.txt); tools/standing/ at %s by a commit of its own, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after (relay data/b753_standing_v1320.txt); the rules, %d rows, the navigator’s search rule among them, in relay data/b753_rules.txt.' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], len(co_.get('entered') or []), f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], len(f['rules_rows'])), '',
         '**The cross-reference** ((R363)(3)): the %d questions the ruling put read against the corpus before anything was put: %d held by the record (the order or finding cited, its state read by tools/standing/orders.py), %d candidates, %d cite not matching the ruling’s words printed and not repaired; no order entered (relay data/b753_crossref.txt, committed at %s).' % (
             f['xr_q'], f['xr_held'], f['xr_cand'], f['xr_nomatch'], K.C2_PLAN_FIRST), '',
         '**The class-group signature** ((R363)(4), N2): the opening control first -- b750’s figures for cQ recomputed by b750’s route, negative %d, the smallest negative n %d, exactly zero %d, nonnegative %d, as wanted -- then the %d primes up to %d typed in Q(√−23) (R %d, I %d, P %d, N %d; mismatches between the two typings %d), and the sign of every nonzero cQ(n) against “n has a prime factor of type N”: negative with N %d, negative without %d, positive with N %d, positive without %d. The statement, every negative n has a type-N factor, %s over n ≤ %d; its reverse %s (%d counterexamples among the nonzero). The generator committed at %s before its bank at %s (relay tools/b753_cq_signature.py, data/b753_cq_signature.txt); nothing claimed beyond n ≤ %d.' % (
             f['sg_neg'], f['sg_small'], f['sg_zero'], f['sg_nonneg'], f['sg_primes'], f['sg_n'], f['sg_types'][0], f['sg_types'][1], f['sg_types'][2], f['sg_types'][3], f['sg_mism'],
             sg_[0], sg_[1], sg_[2], sg_[3], f['sg_stmt'], f['sg_n'], f['sg_rev'], f['sg_counter'], K.C2_RELAY_ALL[1], K.C2_RELAY_ALL[2], f['sg_n']), '',
         '**The statements** ((R363)(5), N3): the declarations the plan stands on printed from SIDE-kernel v1.5, SIDE-explicit-formula v0.38 and Mathlib at the kernel’s pin, %d rows graded or described in (R363)(5)’s words (a definition described, not graded): MechanismClass an inductive of seven constructors with a count; no declaration relating cQ to von Mangoldt’s Λ; Mathlib’s 3-4-1 route for Dirichlet characters, not for nonnegative coefficients; dh_witness SHELL; the census’s reading standing at the tree for all seven (relay data/b753_statements.txt, committed at %s).' % (
             f['st_rows'], K.C2_RELAY), '',
         '**The integration line** (Component 4): this entry’s line read by tools/b753_line.py from REGISTRY and SPIRAL_MAP with the match of tools/standing/linematch.py: the cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23), the keystone %s, stage %s, %d of %d FINDING names matched -- the keystone carries none of this act’s finding names, and no keystone line is written this act (relay data/b753_line.txt); the earlier entries’ lines read again, %d of them, none rewritten.' % (
             f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '',
         '**The order of the act** (N2): %s at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the cross-reference at relay %s; the generator at %s, its bank at %s; the statements at %s; the plan at %s; the answers pair at %s; the line bank at %s; the per-commit scan to its own bank at every commit; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b753_prelock.txt, data/b753_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             f['ver'], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.C2_PLAN_FIRST, K.C2_RELAY_ALL[1], K.C2_RELAY_ALL[2], K.C2_RELAY, K.C3_RELAY[0], K.C3_RELAY[1], K.C4_LINE), '',
         '**What this act is not**: nothing built; nothing deposits; no new version; no draft published; no Zenodo call; no kernel’s main touched, no branch merged, no tag beyond v0.38, no Lean file written, no dispatch; no door or ledger row edited; no order entered; no paper written.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b753_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b753_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b753_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b753 -- %s, %s, %s, %s -- against b752’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b753_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the signature and the statements read one way: the signature finds every negative cQ(n) up to 3000 on an n of type-N primes alone, read POST HOC beside the shape b723 derived at h = 2, and the statements find no class of the seven that takes a function; together they place the premise the plan prices in the coefficients and not in the catalogue, and B3 bounds what any of it says about the centre.', '',
         '**Carried to:** %s, per the author’s word at [P1]’s pass: the system refresh, then the sitting, then sections 6-8, then the build of T0 and T1 in an act the author names; the twelve rules for the author’s strike; the cross-reference’s three candidates, none entered; b752’s line read again CLUSTERED, printed and not rewritten; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b752():
    """b752's form over b752's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b753's objects; b752's composer in git at b752's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the cross-reference, the signature, the statements and the plan; the line."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R363)(3)(vii): the composed prompts' rows, the sitting rows read apart
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    sg_ = f['sg_table']
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R363) ratified.** Its components as the ferry orders them (relay data/b753_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b752’s weight), :%s (the corrigendum), :%s (the entry); no order entered; no paper written; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**W-ORD-MECHANISM-ATTRIBUTION:** OPEN; its plan put as [P1] and %s -- T0 (%d-%d lines) then T1 (%d-%d), T2 printed as not abstracting at the pin, T3-f the printable finding; nothing built; the build fourth, after the system refresh, the sitting and sections 6-8, in an act the author names (relay data/b753_attribution_plan.txt, data/b753_author_answers.txt).' % (
                 f['p1'].lower(), f['pl_t0'][0], f['pl_t0'][1], f['pl_t1'][0], f['pl_t1'][1]), '',
             '**The cross-reference, the signature and the statements:** %d questions, held %d, candidates %d, none entered (relay data/b753_crossref.txt); the signature of cQ’s negative n over n ≤ %d, its control as wanted, the table %d, %d, %d, %d, the statement %s, the reverse %s (relay data/b753_cq_signature.txt); the kernel’s classes an enumeration, %d rows graded or described, none of the seven a predicate on functions (relay data/b753_statements.txt).' % (
                 f['xr_q'], f['xr_held'], f['xr_cand'], f['sg_n'], sg_[0], sg_[1], sg_[2], sg_[3], f['sg_stmt'], f['sg_rev'], f['st_rows']), '',
             '**The integration line:** b753’s at the foot of its entry, cluster the Epstein instance, keystone %s, stage %s, %d of %d matched (relay data/b753_line.txt); the earlier lines read again %d, none rewritten.' % (
                 f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted (relay data/b753_standing_v1320.txt); the twelve rules (relay data/b753_rules.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b753_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b753_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b753_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b753 `%s` (previous `%s`, b752’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b753_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b753_standing_v1320.txt); the standing '
             'report tool (relay data/b753_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b752 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b753_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b752’s %s, %s, %s, %s (relay data/b753_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b753_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b752():
    """b752's trail record over b752's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b752 left them, the six; MEASURED off the six kernels` refs/heads.'),
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
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b752-closing, push-b752-preroot, push-b752-record; PLACE-papers push-b752-preroot, push-b752-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b753_stepzero.txt :54-:58).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written this act ((R363)(6)).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R363)(1), (7): FINDINGS :14787.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R363)(7): row (72).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R363)(10)).'),
    ('sitting items decided', 1, 1, 'items', '### (R363)(6): [P1], passed (relay data/b753_attribution_plan.txt, data/b753_author_answers.txt).'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R363) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b753_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.32.0`s controls, the cross-reference, the signature, the statements, the plan, the line, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 0, 0, 'commits', '### none this act: no registered object.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: no registered object this act; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R363)(6)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R363)(7): tools/standing/ to v1.32.0, each repair with its control; MEASURED off the worklist`s lists.'),
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
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b753_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes, their ls-remote read-backs, the gh reads and the gh description writes under the GitHub login; none carries an identifier.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b753: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b753_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b753_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1320', 'crossref', 'cq_signature', 'statements', 'attribution_plan', 'line', 'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b753_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b753_registration_%s.txt -- b753, THE ATTRIBUTION PLAN: b752 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.32.0; "
                             "THE CROSS-REFERENCE; THE CLASS-GROUP SIGNATURE; THE STATEMENTS; THE PLAN AT [P1]; THE INTEGRATION LINE; NOTHING BUILT, UNDER (R363)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b752's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b753: b752's lines read banks this
act does not write, and are not carried; the lines are b753's: tools/standing/ v1.32.0 by its controls (CERTIFIED), the cross-reference, the
signature control, the statements, the plan and the INTEGRATION line by their banks (REGISTERED), and the draft (HELD); no line stands on
KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b753's lines, each from the record tool's figures over b753's banks
    # ------------------------------------------------------------------ REGISTERED: (R363)(6), the plan, read from its bank and the answers bank
    sz = seat('%s_attribution_plan.txt' % ACT, '**[P1] THE ATTRIBUTION PLAN: ')
    sk = sz   # ### (R362)(2)(ii): the name the template appends
    keys['PLAN'] = ('REGISTERED -- THE PLAN: W-ORD-MECHANISM-ATTRIBUTION`s plan put as [P1] and %s; T0 (%d-%d lines) then T1 (%d-%d) recommended, T2 printed as not abstracting at the pin, T3-f the printable finding; nothing built; at relay %s. SOURCE %s.' % (
        f['p1'], f['pl_t0'][0], f['pl_t0'][1], f['pl_t1'][0], f['pl_t1'][1], K.C3_RELAY[0], sz['text']))
    sx = seat('%s_crossref.txt' % ACT, '**THE CROSS-REFERENCE: QUESTIONS ')
    keys['XREF'] = ('REGISTERED -- THE CROSS-REFERENCE: %d questions, held %d, candidates %d, cites not matched %d; no order entered; at relay %s. SOURCE %s.' % (
        f['xr_q'], f['xr_held'], f['xr_cand'], f['xr_nomatch'], K.C2_PLAN_FIRST, sx['text']))
    seats.append(sx)
    sg = seat('%s_cq_signature.txt' % ACT, '**THE SIGNATURE, n <= ')
    keys['SIG'] = ('REGISTERED -- THE SIGNATURE CONTROL: n <= %d, the control as wanted (negative %d, smallest %d); the table %d, %d, %d, %d; the statement %s, the reverse %s; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['sg_n'], f['sg_neg'], f['sg_small'], f['sg_table'][0], f['sg_table'][1], f['sg_table'][2], f['sg_table'][3], f['sg_stmt'], f['sg_rev'],
        K.C2_RELAY_ALL[1], K.C2_RELAY_ALL[2], sg['text']))
    seats.append(sg)
    sm = seat('%s_statements.txt' % ACT, '**THE STATEMENTS: ')
    keys['STM'] = ('REGISTERED -- THE STATEMENTS: a class of SIDE-kernel v1.5 an enumerated constructor with a count (%d), none of the seven a predicate on functions; %d rows graded or described; at relay %s. SOURCE %s.' % (
        f['st_count'], f['st_rows'], K.C2_RELAY, sm['text']))
    seats.append(sm)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.32.0 ((R363)(7)), by its controls
    sw = seat('%s_standing_v1320.txt' % ACT, '**v1.32.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1320'] = ('CERTIFIED -- tools/standing/ v1.32.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the INTEGRATION line (Component 4)
    so = seat('%s_line.txt' % ACT, '**THE LINE: ')
    keys['LINE'] = ('REGISTERED -- THE INTEGRATION LINE from REGISTRY and SPIRAL_MAP with the match: cluster the Epstein instance, keystone %s, stage %s, %d of %d matched; the earlier lines read again %d, none rewritten. SOURCE %s.' % (
        f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R363)(10))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1320']), ('REGISTERED', ['XREF', 'SIG', 'STM', 'PLAN', 'LINE']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b753 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
